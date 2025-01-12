# scraper.py

import argparse
import asyncio
import hashlib
import json
import os
import sys

from aiohttp import ClientSession, ClientTimeout
from playwright.async_api import async_playwright

import trafilatura

import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

CACHE_DIR = "cache"
DATA_DIR = "data"
URLS_DIR = "urls"

STOPWORDS = set(stopwords.words("english"))


os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)


def cleanup_text(text):
    # 1. Replace any newline characters with a space.
    text = text.replace("\n", " ")
    # 2. Remove multiple spaces (collapse into a single space).
    text = re.sub(r"\s+", " ", text).strip()
    # 3. Remove stopwords.
    words = text.split()
    filtered = [w for w in words if w.lower() not in STOPWORDS]
    text = " ".join(filtered)
    return text


def get_cache_filename(url):
    """Generate a cache filename based on the URL hash."""
    url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{url_hash}.html")


def load_cached_content(url):
    """Load cached content for a URL if it exists."""
    cache_file = get_cache_filename(url)
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()
    return None


def cache_content(url, content):
    """Cache the content of a URL."""
    cache_file = get_cache_filename(url)
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(content)


async def fetch_with_aiohttp(url, session, retries=3):
    """Fetch content using aiohttp with retry logic."""
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print(f"Error {response.status} for URL: {url}")
            await asyncio.sleep(2**attempt)
        except Exception as e:
            print(f"Exception for URL {url}: {e}")
            await asyncio.sleep(2**attempt)
    print(f"Failed to fetch URL after {retries} retries: {url}")
    return None


async def fetch_with_playwright(url):
    """Fetch content using Playwright for JavaScript-heavy pages."""
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            content = await page.content()
            await browser.close()
            return content
    except Exception as e:
        print(f"Playwright exception for URL {url}: {e}")
        return None


def sanitize_backticks(json_text):
    """
    Remove extra newlines immediately following backticks in JSON text.
    """
    import re

    # Pattern to find backticks followed by newlines
    pattern = r"(`+)(\n+)(\S)"

    # Replace newlines between backticks and following text
    sanitized_text = re.sub(pattern, r"\1 \3", json_text)
    return sanitized_text


def save_json(site_key, json_content):
    """Save JSON content to a file."""
    output_file = os.path.join(DATA_DIR, f"{site_key}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(json_content)


async def process_url(url, domain, session):
    """Process a single URL: fetch, extract, sanitize, and return JSON content."""
    cached_content = load_cached_content(url)
    if cached_content:
        html_content = cached_content
    else:
        html_content = await fetch_with_aiohttp(url, session)
        if html_content is None:
            html_content = await fetch_with_playwright(url)
        if html_content:
            cache_content(url, html_content)
        else:
            print(f"Failed to retrieve content for URL: {url}")
            return None

    if not html_content:
        print(f"Failed to retrieve content for URL: {url}")
        return None

    # Use Trafilatura to extract content and metadata
    extracted = trafilatura.extract(
        html_content,
        url=url,
        output_format="json",
        with_metadata=True,
    )

    if not extracted:
        print(f"Trafilatura failed to extract content from URL: {url}")
        return None

    # Parse the extracted JSON content
    data = json.loads(extracted)

    # Keep only the 'source', 'title', and 'text' fields
    minimal_data = {k: data[k] for k in ("source", "title", "text") if k in data}

    # Clean up fields if they exist
    if "text" in minimal_data:
        # Ensure 'text' field is present and then clean
        if not minimal_data["text"]:
            print(f"No text extracted from URL: {url}")
            return None
        minimal_data["text"] = cleanup_text(minimal_data["text"])
    else:
        print(f"No text extracted from URL: {url}")
        return None

    # Convert back to JSON string
    extracted_json = json.dumps(minimal_data)
    return extracted_json


async def main():
    parser = argparse.ArgumentParser(
        description="Web scraper that converts web pages to JSON."
    )
    parser.add_argument(
        "--site_key",
        required=True,
        help="The site key corresponding to a JSON configuration file.",
    )
    args = parser.parse_args()

    site_key = args.site_key
    config_file = os.path.join(URLS_DIR, f"{site_key}.json")

    if not os.path.exists(config_file):
        print(f"Configuration file not found: {config_file}")
        sys.exit(1)

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
            urls = config["urls"]
            domain = config["domain"]
    except Exception as e:
        print(f"Error loading configuration: {e}")
        sys.exit(1)

    json_contents = []

    timeout = ClientTimeout(total=30)
    async with ClientSession(timeout=timeout) as session:
        tasks = []
        for url in urls:
            tasks.append(process_url(url, domain, session))
        results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            json_contents.append(result)

    if not json_contents:
        print("No content was scraped.")
        sys.exit(1)

    final_json = "[" + ",\n".join(json_contents) + "]"
    save_json(site_key, final_json)
    print(f"JSON content saved to {os.path.join(DATA_DIR, f'{site_key}.json')}")


if __name__ == "__main__":
    asyncio.run(main())
