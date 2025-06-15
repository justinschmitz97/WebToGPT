# scraper.py

import argparse
import asyncio
import hashlib
import json
import os
import sys

from aiohttp import ClientSession, ClientTimeout
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from openai import AsyncOpenAI

import trafilatura

import re
import nltk
from nltk.corpus import stopwords

# Load environment variables from .env file
load_dotenv()

nltk.download("stopwords")

CACHE_DIR = "cache"
DATA_DIR = "data"
URLS_DIR = "urls"

STOPWORDS = set(stopwords.words("english"))

# Initialize OpenAI client
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)


def cleanup_text(text):
    # 1. Replace any newline characters with a space.
    text = text.replace("\n", " ")
    # 2. Remove multiple spaces (collapse into a single space).
    text = re.sub(r"\s+", " ", text).strip()
    return text


async def process_content_with_ai(text: str):
    """
    Process the extracted text with an AI model to summarize and structure it.
    """
    if not text or not isinstance(text, str) or len(text.strip()) < 100:
        print("Text is too short to process, skipping AI structuring.")
        return None

    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert developer assistant. Your task is to analyze a software changelog or blog post and extract the key information into a structured JSON format.

The user will provide the raw text content of a webpage.

Your output must be a JSON object with the following schema:
{
  "summary": "A concise, developer-focused summary of the most important changes. Focus on the 'what' and 'why'.",
  "changes": [
    {
      "type": "Feature" | "Breaking Change" | "Deprecation" | "Performance" | "Fix" | "Other",
      "title": "A short, descriptive title for the change.",
      "description": "A detailed but clear explanation of the change, including code examples if available in the source text. Keep it technical and to the point."
    }
  ]
}

Focus exclusively on technical changes. Omit marketing fluff, introductory paragraphs, author bios, and other non-essential information. If the text does not appear to be a changelog or technical update, return an empty "changes" array.
""",
                },
                {"role": "user", "content": text},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error processing content with AI: {e}")
        return None


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
    """Process a single URL: fetch, extract, structure with AI, and return JSON content."""
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

    # Use Trafilatura to extract the main text content
    plain_text = trafilatura.extract(html_content, include_comments=False)

    if not plain_text:
        print(f"Trafilatura failed to extract content from URL: {url}")
        return None

    # Process the text with our AI function to get structured data
    structured_data_str = await process_content_with_ai(plain_text)

    if not structured_data_str:
        print(f"AI processing failed or returned no data for URL: {url}")
        return None

    # Add the source URL to the structured data
    try:
        structured_data = json.loads(structured_data_str)
        structured_data["source"] = url
        return json.dumps(structured_data)
    except json.JSONDecodeError:
        print(f"Failed to decode JSON from AI for URL: {url}")
        return None


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
