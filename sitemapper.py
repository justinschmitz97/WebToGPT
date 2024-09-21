# sitemapper.py

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import logging
import async_timeout
import json
from datetime import datetime, timezone  # Import timezone from datetime
import os
import argparse

class AsyncURLCrawler:
    def __init__(self, base_url, config):
        self.base_url = self.normalize_url(base_url.rstrip('/'))
        self.base_parsed_url = urlparse(self.base_url)
        self.visited_urls = set()
        self.failed_urls = []
        self.urls_to_visit = asyncio.Queue()
        self.urls_to_visit.put_nowait(self.base_url)
        self.session = None
        self.user_agent = "Mozilla/5.0 (compatible; MyCrawler/1.0)"
        self.excluded_patterns = config.get("excluded_patterns", [])
        self.excluded_extensions = config.get("excluded_extensions", [".epub", ".bz2", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".tiff", ".ico", ".zip"])
        self.max_concurrency = config.get("max_concurrency", 10)
        logging.basicConfig(level=logging.INFO)

    def normalize_url(self, url):
        """ Convert HTTP URLs to HTTPS and normalize the URL by removing the trailing slash """
        parsed_url = urlparse(url)
        if parsed_url.scheme == 'http':
            parsed_url = parsed_url._replace(scheme='https')
        normalized_url = parsed_url._replace(path=parsed_url.path.rstrip('/'))
        return normalized_url.geturl()

    async def fetch_page(self, url):
        async with async_timeout.timeout(10):
            headers = {"User-Agent": self.user_agent}
            try:
                async with self.session.get(url, headers=headers) as response:
                    response.raise_for_status()  # Checks for HTTP errors
                    html = await response.text()
                    return html
            except aiohttp.ClientError as e:
                logging.error(f"Request failed: {url}, error: {e}")
                self.failed_urls.append({"url": url, "error": str(e)})
                return None

    def qualifies_url(self, url):
        """ Check if the URL fits the base_url path and doesn't contain excluded patterns or extensions """
        url = self.normalize_url(url)
        parsed_url = urlparse(url)
        if parsed_url.netloc != self.base_parsed_url.netloc or not parsed_url.path.startswith(self.base_parsed_url.path):
            return False

        # Exclude URLs with unwanted patterns
        for pattern in self.excluded_patterns:
            if pattern in parsed_url.path:
                return False

        # Exclude URLs with unwanted extensions
        for ext in self.excluded_extensions:
            if parsed_url.path.lower().endswith(ext):
                return False

        return True

    def parse_links(self, html, current_url):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Remove URL fragments and resolve relative URLs
            href = urljoin(current_url, href.split('#')[0].split('?')[0])
            href = self.normalize_url(href)
            if self.qualifies_url(href) and href not in self.visited_urls:
                self.urls_to_visit.put_nowait(href)

    async def crawl_single_url(self):
        while not self.urls_to_visit.empty():
            url = await self.urls_to_visit.get()
            if url in self.visited_urls:
                self.urls_to_visit.task_done()
                continue
            logging.info(f"Crawling: {url}")
            self.visited_urls.add(url)
            html = await self.fetch_page(url)
            if html:
                self.parse_links(html, url)
            self.urls_to_visit.task_done()

    async def crawl(self):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as self.session:
            tasks = [asyncio.create_task(self.crawl_single_url()) for _ in range(self.max_concurrency)]
            await self.urls_to_visit.join()  # Ensure all tasks are done
            for task in tasks:
                task.cancel()  # Cancel any remaining tasks

    def save_to_file_json(self, site_key):
        file_path = f"urls/{site_key}.json"
        
        unique_urls = sorted(set(self.visited_urls))
        output_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "domain": self.base_url,
            "crawl_metadata": {
                "user_agent": self.user_agent,
                "max_concurrency": self.max_concurrency,
                "excluded_patterns": self.excluded_patterns,
                "excluded_extensions": self.excluded_extensions,
            },
            "total_urls": len(unique_urls),
            "urls": unique_urls,
            "failed_urls": self.failed_urls
        }

        os.makedirs("urls", exist_ok=True)  # Ensure the directory exists before saving

        with open(file_path, 'w') as file:
            json.dump(output_data, file, indent=4)

async def main(site_key):
    # Load configuration
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    site_config = config.get(site_key, config["default"])
    BASE_URL = site_config.get("base_url", "")

    if not BASE_URL:
        logging.error(f"No base URL found for site key: {site_key}")
        return

    crawler = AsyncURLCrawler(BASE_URL, site_config)
    await crawler.crawl()
    crawler.save_to_file_json(site_key)
    logging.info(f"Crawling completed, {len(crawler.visited_urls)} URLs found.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("site_key", help="The site key to use from the config.")
    args = parser.parse_args()

    asyncio.run(main(args.site_key))