"""
scraper.py
This script scrapes a list of URLs based on the json file provided.
"""

import argparse
import json
import os
import sys
import time
import logging
import re

import hashlib
import aiohttp
import asyncio

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def parse_args():
    parser = argparse.ArgumentParser(description="Webpage to Markdown scraper.")
    parser.add_argument(
        "--site_key",
        required=True,
        help="The site key for the configuration JSON file (without .json extension).",
    )
    return parser.parse_args()


def load_configuration(site_key):
    config_path = os.path.join("urls", f"{site_key}.json")
    if not os.path.exists(config_path):
        logging.error(f"Configuration file {config_path} does not exist.")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing JSON configuration: {e}")
            sys.exit(1)
    return config


CACHE_DIR = "cache/"


def get_cache_filename(url):
    url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{url_hash}.cache")


def read_from_cache(url):
    filename = get_cache_filename(url)
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return None


def write_to_cache(url, content):
    os.makedirs(CACHE_DIR, exist_ok=True)
    filename = get_cache_filename(url)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def fetch_url(url, max_retries=3, delay=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/70.0.3538.77 Safari/537.36"
    }
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
            else:
                logging.warning(
                    f"Non-200 status code {response.status_code} for URL: {url}"
                )
        except requests.RequestException as e:
            logging.warning(f"Request error for URL {url}: {e}")
        retries += 1
        logging.info(f"Retrying ({retries}/{max_retries})...")
        time.sleep(delay)
    logging.error(f"Failed to fetch URL after {max_retries} retries: {url}")
    return None


def fetch_url_with_playwright(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, timeout=10000)  # Timeout after 10 seconds
            html_content = page.content()
            browser.close()
            return html_content
    except Exception as e:
        logging.error(f"Playwright failed to fetch URL {url}: {e}")
        return None


async def fetch_page_content(session, url):
    # Check cache first
    cached_content = read_from_cache(url)
    if cached_content:
        logging.info(f"Using cached content for URL: {url}")
        return cached_content

    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.text()
            write_to_cache(url, content)  # Save content to cache
            return content
    except Exception as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None


async def fetch_all_pages(urls, excluded_classes):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page_content(session, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)


def parse_content(html_content, excluded_classes):
    soup = BeautifulSoup(html_content, "lxml")

    # Remove unwanted elements by class name
    for class_name in excluded_classes:
        for element in soup.find_all(class_=class_name):
            element.decompose()

    # Remove unwanted elements by tag
    for tag in [
        "header",
        "footer",
        "nav",
        "aside",
        "form",
        "iframe",
        "script",
        "style",
    ]:
        for element in soup.find_all(tag):
            element.decompose()

    # Try to find main content
    main_content = soup.find("main") or soup.find("article")
    if main_content:
        return main_content
    else:
        logging.warning("Main content not found; using body content.")
        return soup.body or soup


def convert_to_markdown(element):
    # Handle code blocks separately
    for pre_tag in element.find_all("pre"):
        code_tag = pre_tag.find("code")
        if code_tag:
            # Attempt to get the language from class attributes
            classes = code_tag.get("class", [])
            language = ""
            for cls in classes:
                if "language-" in cls:
                    language = cls.split("language-")[1]
                    break
            code_content = code_tag.get_text()
            fenced_code = f"```{language}\n{code_content}\n```"
            pre_tag.replace_with(fenced_code)
        else:
            code_content = pre_tag.get_text()
            fenced_code = f"```\n{code_content}\n```"
            pre_tag.replace_with(fenced_code)

    # Now convert the modified HTML to Markdown
    md_content = md(str(element), heading_style="ATX")
    return md_content


def sanitize_markdown_content(content):
    # 1. Normalize newlines: replace multiple consecutive newlines with a single one.
    content = re.sub(r"\n\s*\n", "\n\n", content)

    # 2. Remove images markdown completely
    content = re.sub(r"!\[.*?\]\(.*?\)", "", content)

    # 3. Convert inline HTML links to Markdown links if they exist (overwrites the above)
    # Use BeautifulSoup to achieve this if not already done.
    soup = BeautifulSoup(content, "html.parser")
    for a in soup.find_all("a", href=True):
        markdown_link = f"[{a.get_text()}]({a['href']})"
        content = content.replace(str(a), markdown_link)

    # 4. Clean any remaining HTML residue
    content = re.sub(r"<[^>]+>", "", content)  # Simple regex to remove HTML tags

    # 5. Decode HTML entities and fix encoded issues
    content = content.replace("\\=", "=").replace("&gt;", ">").replace("&lt;", "<")

    return content


def write_markdown(output_path, content):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


async def main():
    args = parse_args()
    config = load_configuration(args.site_key)
    urls = config.get("urls", [])
    domain = config.get("domain", "Unknown Domain")
    excluded_classes = config.get("excluded_classes", [])

    if not urls:
        logging.error("No URLs found in the configuration.")
        sys.exit(1)

    markdown_content = f"# {domain}\n\n"

    # Fetch all pages concurrently
    fetched_contents = await fetch_all_pages(urls, excluded_classes)
    for url, content in zip(urls, fetched_contents):
        if content is None:
            logging.error(f"Failed to process content for URL: {url}")
            continue

        # Parse and process HTML (synchronously but efficiently to keep code simple)
        main_content = parse_content(content, excluded_classes)
        soup = BeautifulSoup(content, "lxml")
        page_title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "No Title"
        )
        md_content = convert_to_markdown(main_content)
        sanitized_content = sanitize_markdown_content(md_content)

        # Append to main markdown content
        markdown_content += f"## {page_title}\n\n"
        markdown_content += f"[Read the full article]({url})\n\n"
        markdown_content += sanitized_content + "\n\n"

    # Write to output file
    output_filename = f"{args.site_key}.md"
    output_path = os.path.join("data", output_filename)
    write_markdown(output_path, markdown_content)
    logging.info(f"Markdown file saved to: {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
