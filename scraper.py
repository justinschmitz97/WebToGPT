import argparse
import json
import logging
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# --- Configuration ---
BASE_URL_PATH = "urls/"
OUTPUT_DIR = "data/"
RETRIES = 3  # Number of retries for network requests
REQUEST_TIMEOUT = 10  # Timeout for network requests in seconds
LOG_LEVEL = logging.INFO
# ---------------------


class TqdmLoggingHandler(logging.Handler):
    """
    Custom logging handler that integrates with tqdm.
    """

    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
            self.flush()
        except Exception:
            self.handleError(record)


# Initialize Logger
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[TqdmLoggingHandler()],
)
logger = logging.getLogger(__name__)


def load_metadata_from_file(file_path: str) -> dict:
    """
    Load metadata and URLs from a JSON file.

    :param file_path: Path to the JSON file.
    :return: Dictionary containing the metadata and URLs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict) and "urls" in data:
                return data
            logger.error("Unexpected JSON structure in %s", file_path)
            return {}
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error("Error reading %s: %s", file_path, str(e))
        return {}


def fetch_and_parse(
    url: str, excluded_classes: list, custom_main_indicator: str, selector: str
) -> dict:
    """Fetch and parse the URL's HTML content."""
    for attempt in range(RETRIES):
        try:
            logger.debug("Fetching URL: %s", url)
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()  # Raise an HTTPError for bad requests
            soup = BeautifulSoup(response.text, "html.parser")
            main_content = extract_main_content(
                soup, excluded_classes, custom_main_indicator, selector
            )
            if main_content:
                title = soup.title.string if soup.title else "No Title"
                structured_content = extract_structured_content(main_content)
                return {"url": url, "title": title, "content": structured_content}
            logger.warning("No main content found in %s", url)
            return {}
        except requests.RequestException as e:
            logger.warning(
                "Error fetching %s (attempt %d): %s", url, attempt + 1, str(e)
            )
            if attempt + 1 == RETRIES:
                return {}


def extract_main_content(
    soup: BeautifulSoup,
    excluded_classes: list,
    custom_main_indicator: str,
    selector: str,
) -> BeautifulSoup:
    """Extract main content from the BeautifulSoup object."""
    if selector:
        main_content = soup.select_one(selector)
    elif custom_main_indicator:
        main_content = soup.select_one(custom_main_indicator)
    else:
        main_content = soup.find("main") or soup.find("article") or soup.body

    if main_content:
        for tag in main_content.find_all(["header", "footer", "aside", "nav"]):
            tag.decompose()
        for class_name in excluded_classes:
            for tag in main_content.find_all(class_=class_name):
                tag.decompose()
    return main_content


def extract_structured_content(content: BeautifulSoup) -> list:
    """Extract structured content from the main content."""
    structured_content = []
    for element in content.descendants:
        if element.name and element.name.startswith("h") and element.name[1:].isdigit():
            level = int(element.name[1:])
            structured_content.append(
                {"type": "header", "level": level, "text": element.get_text(strip=True)}
            )
        elif element.name == "p":
            structured_content.append(
                {"type": "p", "text": element.get_text(strip=True)}
            )
        elif element.name in ["ul", "ol"]:
            list_items = [li.get_text(strip=True) for li in element.find_all("li")]
            structured_content.append({"type": "list", "items": list_items})
        elif element.name == "pre":
            code = element.get_text(strip=True)
            structured_content.append({"type": "code", "code": code})
    return structured_content


def main(site_key: str):
    """Main function to load URLs, process them, and save the extracted content."""
    file_path = os.path.join(BASE_URL_PATH, f"{site_key}.json")
    data = load_metadata_from_file(file_path)
    urls = data.get("urls", [])
    domain = data.get("domain", "unknown")
    excluded_classes = data.get("excluded_classes", [])
    custom_main_indicator = data.get("custom_main_indicator", "")
    selector = data.get("selector", "")

    if not urls:
        logger.error("No URLs found in %s", file_path)
        return

    domain_data = {"name": domain, "url": f"https://{domain}", "pages": []}

    progress_bar = tqdm(urls, desc=f"Processing {site_key} URLs", unit="url")
    for url in progress_bar:
        page_data = fetch_and_parse(
            url, excluded_classes, custom_main_indicator, selector
        )
        if page_data:
            domain_data["pages"].append(page_data)

    output_file = os.path.join(OUTPUT_DIR, f"{site_key}.json")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(domain_data, file, ensure_ascii=False, indent=4)
    logger.info("All data has been written to %s", output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape and parse content from specified URLs."
    )
    parser.add_argument(
        "--site_key", required=True, help="The site key to use from the config."
    )
    args = parser.parse_args()

    main(args.site_key)
