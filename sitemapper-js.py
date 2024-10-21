import asyncio
from playwright.async_api import async_playwright
import json
import argparse
from datetime import datetime

# Configuration
EXCLUDED_EXTENSIONS = [
    ".md",
    ".xml",
    ".epub",
    ".bz2",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".bmp",
    ".tiff",
    ".ico",
    ".zip",
]


# Helper function to check if a URL should be excluded
def should_exclude(url, excluded_patterns):
    for pattern in excluded_patterns:
        if pattern in url:
            return True
    for ext in EXCLUDED_EXTENSIONS:
        if url.endswith(ext):
            return True
    return False


async def collect_urls(page, base_url, excluded_patterns, urls, failed_urls):
    try:
        await page.goto(base_url)
        await page.wait_for_load_state("networkidle")  # Ensure the page is fully loaded
        hrefs = await page.evaluate(
            """() => Array.from(document.querySelectorAll('a')).map(a => a.href)"""
        )
        for href in hrefs:
            if href.startswith(base_url) and not should_exclude(
                href, excluded_patterns
            ):
                urls.add(href)
    except Exception as e:
        failed_urls.append(base_url)


async def crawl(base_url, excluded_patterns):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        urls = set()
        failed_urls = []

        await collect_urls(page, base_url, excluded_patterns, urls, failed_urls)

        # Handle pagination or infinite scrolling if necessary
        # Example: Click "Load More" button until it disappears
        # while await page.is_visible('text="Load More"'):
        #     await page.click('text="Load More"')
        #     await page.wait_for_load_state('networkidle')
        #     await collect_urls(page, page.url, excluded_patterns, urls, failed_urls)

        # Close the browser
        await browser.close()

        # Prepare the JSON output
        sitemap = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "domain": base_url,
            "crawl_metadata": {
                "excluded_patterns": excluded_patterns,
                "excluded_extensions": EXCLUDED_EXTENSIONS,
            },
            "total_urls": len(urls),
            "urls": list(urls),
            "failed_urls": failed_urls,
        }

        # Write to a JSON file
        with open("sitemap.json", "w") as f:
            json.dump(sitemap, f, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Crawl a website and generate a sitemap JSON."
    )
    parser.add_argument("key", help="The key in the config.json to use for crawling.")
    args = parser.parse_args()

    # Read the config file
    with open("config.json", "r") as f:
        config = json.load(f)

    if args.key not in config:
        print(f"Error: Key '{args.key}' not found in config.json")
        return

    # Extract the configuration for the given key
    base_url = config[args.key].get("base_url")
    excluded_patterns = config[args.key].get("excluded_patterns", [])

    if not base_url:
        print(f"Error: 'base_url' is required for key '{args.key}'")
        return

    # Run the crawler
    asyncio.run(crawl(base_url, excluded_patterns))


if __name__ == "__main__":
    main()
