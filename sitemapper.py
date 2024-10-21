import asyncio
import logging
import json
import os
import argparse
from datetime import datetime, timezone
from urllib.parse import urlparse
from crawlee.playwright_crawler import PlaywrightCrawler
from crawlee import ConcurrencySettings


class SimpleCrawler:
    def __init__(self, url, config):
        self.url = self.normalize_url(url)
        self.base_domain = urlparse(self.url).netloc
        self.visited_urls = set()
        self.failed_urls = []
        self.excluded_patterns = config.get("excluded_patterns", [])
        self.included_patterns = config.get("included_patterns", [])
        self.max_concurrency = config.get("max_concurrency", 50)
        logging.basicConfig(level=logging.INFO)

    def normalize_url(self, url):
        # Use urlparse and _replace to force https and normalize URL
        parsed_url = urlparse(url)
        return parsed_url._replace(
            scheme="https", path=parsed_url.path.rstrip("/")
        ).geturl()

    def should_visit(self, url):
        url = self.normalize_url(url)  # Normalize URL to HTTPS
        parsed_url = urlparse(url)
        is_same_domain = parsed_url.netloc == self.base_domain
        is_not_excluded = not any(pattern in url for pattern in self.excluded_patterns)

        should_visit = is_same_domain and is_not_excluded
        logging.info(f"URL: {url}, Should Visit: {should_visit}")
        return should_visit

    async def crawl(self):
        concurrency_settings = ConcurrencySettings(max_concurrency=self.max_concurrency)
        crawler = PlaywrightCrawler(concurrency_settings=concurrency_settings)

        @crawler.router.default_handler
        async def request_handler(context):
            url = self.normalize_url(context.request.url)  # Normalize URL to HTTPS
            context.log.info(f"Processing {url} ...")

            # Enqueue links only if they should be visited
            if self.should_visit(url):
                await context.enqueue_links(
                    transform_request=lambda req: req.set_url(
                        self.normalize_url(req.url)
                    )
                )
                self.visited_urls.add(url)
                context.log.info(f"Enqueued links from {url}")
            else:
                context.log.info(f"Skipped {url} due to filtering")

        await crawler.run([self.url])

    def save_results(self, site_key):
        os.makedirs("urls", exist_ok=True)
        filtered_urls = [
            url
            for url in self.visited_urls
            if not self.included_patterns
            or any(pattern in url for pattern in self.included_patterns)
        ]
        output_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "domain": self.url,
            "crawl_metadata": {
                "excluded_patterns": self.excluded_patterns,
                "included_patterns": self.included_patterns,
                "excluded_extensions": [],
            },
            "total_urls": len(filtered_urls),
            "urls": sorted(filtered_urls),
            "failed_urls": self.failed_urls,
        }
        with open(f"urls/{site_key}.json", "w", encoding="utf-8") as file:
            json.dump(output_data, file, indent=4)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site_key", help="The site key to use from the config.")
    parser.add_argument("--url", help="A base URL to run the script with.")
    args = parser.parse_args()

    with open("config.json", "r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    site_config = config.get(args.site_key, config.get("default", {}))
    url = args.url or site_config.get("url", "")

    if not url:
        logging.error("No base URL found for site key: %s", args.site_key)
        return

    crawler = SimpleCrawler(url, site_config)
    await crawler.crawl()
    site_key = args.site_key or url.replace("https://", "").replace(
        "http://", ""
    ).replace("/", "_")
    crawler.save_results(site_key)


if __name__ == "__main__":
    asyncio.run(main())
