import scrapy
from scrapy_playwright.page import PageMethod
import json
from datetime import datetime
from urllib.parse import urlparse

class SitemapSpider(scrapy.Spider):
    name = "sitemap"
    start_urls = ["https://platform.openai.com/"]
    custom_settings = {
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "PLAYWRIGHT_LAUNCH_OPTIONS": {"headless": True},
        "PLAYWRIGHT_ABORT_REQUEST": "sitemap_crawler.spiders.sitemap_spider.should_abort_request",
        "CONCURRENT_REQUESTS": 32,
        "DOWNLOAD_DELAY": 0,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 32,
        "CONCURRENT_REQUESTS_PER_IP": 32,
        "REACTOR_THREADPOOL_MAXSIZE": 20,
        "PLAYWRIGHT_MAX_CONTEXTS": 8,
        "PLAYWRIGHT_MAX_PAGES_PER_CONTEXT": 8,
        "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT": 30000,  # 30 seconds
        "LOG_LEVEL": "INFO",  # Reduce logging level to INFO
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",  # Use AsyncioSelectorReactor
    }

    excluded_patterns = ["/ru", "/ja", "/ko", "/es-ES", "/zh-CN"]
    excluded_extensions = [
        ".md", ".xml", ".epub", ".bz2", ".png", ".jpg", ".jpeg", ".gif", ".svg",
        ".webp", ".bmp", ".tiff", ".ico", ".zip"
    ]

    def __init__(self, *args, **kwargs):
        super(SitemapSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = [urlparse(url).netloc for url in self.start_urls]
        self.visited_urls = set()
        self.all_urls = set()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={"playwright": True, "playwright_include_page": True}, callback=self.parse)

    async def parse(self, response):
        page = response.meta["playwright_page"]
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)  # 30 seconds timeout
        except Exception as e:
            self.logger.error(f"Error waiting for load state: {e}")
            await page.close()
            return

        for link in response.css('a::attr(href)').getall():
            full_url = self.normalize_url(response.urljoin(link))
            if self.is_valid_url(full_url):
                self.all_urls.add(full_url)
                if full_url not in self.visited_urls:
                    self.visited_urls.add(full_url)
                    yield scrapy.Request(full_url, meta={"playwright": True, "playwright_include_page": True}, callback=self.parse)

        await page.close()

    def is_valid_url(self, url):
        if any(url.endswith(ext) for ext in self.excluded_extensions):
            return False
        if any(pattern in url for pattern in self.excluded_patterns):
            return False
        if not any(url.startswith(f"https://{domain}") for domain in self.allowed_domains):
            return False
        if '#' in url or '?' in url:
            return False
        return True

    def normalize_url(self, url):
        return url.rstrip('/')

    def closed(self, reason):
        sorted_urls = sorted(self.all_urls)
        sitemap = {
            "timestamp": datetime.utcnow().isoformat(),
            "domain": self.start_urls[0],
            "crawl_metadata": {
                "excluded_patterns": self.excluded_patterns,
                "excluded_extensions": self.excluded_extensions,
            },
            "total_urls": len(sorted_urls),
            "urls": sorted_urls,
            "failed_urls": []
        }
        with open("sitemap.json", "w") as f:
            json.dump(sitemap, f, indent=2)

def should_abort_request(request):
    """Abort requests to unwanted domains or resource types."""
    if request.resource_type in ["image", "media", "font", "stylesheet"]:
        return True
    referer = request.headers.get('Referer')
    if referer and urlparse(request.url).netloc != urlparse(referer).netloc:
        return True
    return False