import argparse
import asyncio
import re
import random
import json
import os
import logging
import time
from urllib.parse import urlparse, urljoin
from aiohttp import ClientSession
from aiohttp_retry import RetryClient, ExponentialRetry
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variables and constants
DEFAULT_EXCLUDED_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".svg",
    ".webp",
    ".ico",
    ".mp4",
    ".mp3",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".mkv",
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".rar",
    ".7z",
    ".gz",
    ".tar",
    ".css",
    ".js",
    ".json",
    ".xml",
]

visited_urls = set()
urls_to_visit = asyncio.Queue()
failed_urls = {}

# Throttling variables
throttling_enabled = False
throttling_delay_min = 2.0  # Minimum delay in seconds
throttling_delay_max = 5.0  # Maximum delay in seconds


def main():
    parser = argparse.ArgumentParser(
        description="Generate a sitemap for a given website."
    )
    parser.add_argument("--site_key", help="Site key from config.json to use.")
    parser.add_argument("--url", help="Base URL to start crawling from.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode for URL prefix filtering.",
    )
    args = parser.parse_args()

    # Load configuration
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    if args.site_key:
        site_config = config.get(args.site_key)
        if not site_config:
            logging.error(f"Site key '{args.site_key}' not found in config.json.")
            exit(1)
    else:
        site_config = config.get("default", {})
        site_config["url"] = args.url

    global base_url, base_domain, included_regex, excluded_regex, excluded_extensions, max_concurrency, final_include_patterns, strict_mode, url_prefix, throttling_enabled

    base_url = site_config.get("url")
    if not base_url:
        logging.error(
            "No URL provided. Please specify a URL using --url or in config.json."
        )
        exit(1)

    parsed_base_url = urlparse(base_url)
    if not parsed_base_url.scheme:
        base_url = "https://" + base_url
        parsed_base_url = urlparse(base_url)

    base_domain = parsed_base_url.netloc

    included_patterns = site_config.get("included_patterns", [])
    excluded_patterns = site_config.get("excluded_patterns", [])
    excluded_extensions = site_config.get(
        "excluded_extensions", DEFAULT_EXCLUDED_EXTENSIONS
    )
    max_concurrency = site_config.get("max_concurrency", 50)
    final_include_patterns = site_config.get("final_include_patterns", [])

    included_regex = (
        re.compile("|".join(included_patterns)) if included_patterns else None
    )
    excluded_regex = (
        re.compile("|".join(excluded_patterns)) if excluded_patterns else None
    )

    # Strict mode-related settings
    strict_mode = args.strict or site_config.get(
        "strict", False
    )  # Command-line flag overrides config
    url_prefix = base_url if strict_mode else None

    # Throttling settings
    throttling_enabled = site_config.get("throttling", False)

    # Start crawling
    urls_to_visit.put_nowait(base_url)
    start_time = time.time()
    asyncio.run(crawl())
    end_time = time.time()
    logging.info(f"Crawling completed in {end_time - start_time:.2f} seconds.")

    # Apply final filtering
    if final_include_patterns:
        final_include_regex = re.compile("|".join(final_include_patterns))
        filtered_urls = [url for url in visited_urls if final_include_regex.search(url)]
    else:
        filtered_urls = list(visited_urls)

    # Sort the URLs alphabetically
    filtered_urls = sorted(filtered_urls)

    # Save results
    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "site_key": args.site_key or "default",
        "domain": base_url,
        "total_urls": len(filtered_urls),
        "failed_urls": failed_urls,
        "urls": filtered_urls,
    }

    output_dir = "urls"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(
        output_dir, f"{(args.site_key or 'default').replace('.', '_')}.json"
    )
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
    logging.info(f"Results saved to {output_filename}")


async def crawl():
    semaphore = asyncio.Semaphore(max_concurrency)
    async with ClientSession() as session:
        retry_options = ExponentialRetry(attempts=2)
        retry_client = RetryClient(session, retry_options=retry_options)
        while not urls_to_visit.empty():
            tasks = []
            while not urls_to_visit.empty():
                url = await urls_to_visit.get()
                if url in visited_urls:
                    urls_to_visit.task_done()
                    continue
                visited_urls.add(url)
                task = asyncio.create_task(fetch(url, retry_client, semaphore))
                tasks.append(task)
                urls_to_visit.task_done()
            if tasks:
                await asyncio.gather(*tasks)


async def fetch(url, session, semaphore):
    logging.info(f"Fetching: {url}")
    async with semaphore:
        try:
            # Throttling: Introduce a randomized delay if enabled
            if throttling_enabled:
                delay = random.uniform(throttling_delay_min, throttling_delay_max)
                logging.info(f"Throttling enabled. Delaying for {delay:.2f} seconds...")
                await asyncio.sleep(delay)

            async with session.get(url, timeout=10) as response:
                if response.content_type != "text/html":
                    return
                html = await response.text()
                extract_links(html, url)
        except Exception as e:
            logging.error(f"Failed to fetch {url}: {e}")
            failed_urls[url] = str(e)


def extract_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    for link_tag in soup.find_all("a", href=True):
        href = link_tag.get("href")
        # Normalize URL
        href = urljoin(base, href)
        parsed_href = urlparse(href)
        # Remove fragments and query parameters
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        # Strict mode: discard links outside the specified prefix
        if strict_mode and not href.startswith(url_prefix):
            continue
        # Domain restriction
        if parsed_href.netloc != base_domain:
            continue
        # File extension filtering
        if any(href.endswith(ext) for ext in excluded_extensions):
            continue
        # Apply include and exclude patterns
        path = parsed_href.path
        if excluded_regex and excluded_regex.search(path):
            continue
        if included_regex and not included_regex.search(path):
            continue
        if href not in visited_urls:
            urls_to_visit.put_nowait(href)


if __name__ == "__main__":
    main()
