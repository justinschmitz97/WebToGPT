# scraper.py

import argparse
import asyncio
import hashlib
import json
import os
import re
import sys

from aiohttp import ClientSession, ClientTimeout
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import async_playwright

from lxml import etree, html

CACHE_DIR = "cache"
DATA_DIR = "data"
URLS_DIR = "urls"


os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)


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


def sanitize_markdown(markdown_text):
    """Sanitize and normalize the Markdown content."""
    lines = markdown_text.splitlines()
    sanitized_lines = [line for line in lines if not line.strip().startswith("![")]
    return "\n".join(sanitized_lines)


async def fetch_with_aiohttp(url, session, retries=3):
    """Fetch content using aiohttp with retry logic."""
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print(f"Error {response.status} for URL: {url}")
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


def extract_content(html_content, xpaths):
    """Extract main content from HTML using lxml and site-specific XPath rules."""
    parser = html.HTMLParser(encoding="utf-8")
    tree = html.fromstring(html_content, parser=parser)
    for xpath_expr in xpaths:
        elements = tree.xpath(xpath_expr.path)
        for elem in elements:
            elem.getparent().remove(elem)
    main_content = (
        tree.xpath("//main") or tree.xpath("//article") or tree.xpath("//body")
    )
    if main_content:
        content_html = etree.tostring(
            main_content[0], encoding="unicode", method="html"
        )
        return content_html
    else:
        return None


def convert_to_markdown(html_content):
    """Convert HTML content to Markdown format."""
    markdown = md(html_content, heading_style="ATX")
    markdown = sanitize_markdown(markdown)
    return markdown


def sanitize_markdown(markdown_text):
    """Sanitize and normalize the Markdown content."""
    # Remove images
    lines = markdown_text.splitlines()
    sanitized_lines = [line for line in lines if not line.strip().startswith("![")]
    markdown_text = "\n".join(sanitized_lines)

    # Collapse multiple newlines into a single newline
    markdown_text = re.sub(r"\n\s*\n+", "\n\n", markdown_text)

    # Strip leading and trailing whitespace
    markdown_text = markdown_text.strip()

    return markdown_text


def save_markdown(site_key, markdown_content):
    """Save Markdown content to a file."""
    output_file = os.path.join(DATA_DIR, f"{site_key}.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)


async def process_url(url, domain, xpaths, session):
    """Process a single URL: fetch, extract, convert, and return Markdown content."""
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
            return None
    extracted_html = extract_content(html_content, xpaths)
    if not extracted_html:
        print(f"Failed to extract content from URL: {url}")
        return None
    markdown_content = convert_to_markdown(extracted_html)
    sanitized_markdown = sanitize_markdown(markdown_content)
    soup = BeautifulSoup(html_content, "lxml")
    title = soup.title.string.strip() if soup.title else "No Title"
    markdown_section = f"<<<<< {domain} >>>>>\n\n"
    markdown_section += f"# {title}\n\n"
    markdown_section += f"URL: {url}\n\n"
    markdown_section += sanitized_markdown
    markdown_section += "\n\n---\n\n"
    return markdown_section


async def main():
    parser = argparse.ArgumentParser(
        description="Web scraper that converts web pages to Markdown."
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

    try:
        from xpaths import CLEAN_XPATHS
    except ImportError:
        CLEAN_XPATHS = []

    markdown_contents = []

    timeout = ClientTimeout(total=30)
    async with ClientSession(timeout=timeout) as session:
        tasks = []
        for url in urls:
            tasks.append(process_url(url, domain, CLEAN_XPATHS, session))
        results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            markdown_contents.append(result)

    if not markdown_contents:
        print("No content was scraped.")
        sys.exit(1)

    final_markdown = "\n".join(markdown_contents)
    save_markdown(site_key, final_markdown)
    print(f"Markdown content saved to {os.path.join(DATA_DIR, f'{site_key}.md')}")


if __name__ == "__main__":
    asyncio.run(main())
