"""
This script fetches and parses URLs from a JSON file, extracts the main content,
converts it to Markdown, and saves it into an output directory.
"""

import argparse
import json
import logging
import os
import re
import requests
from bs4 import BeautifulSoup
import html2text
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


def fetch_and_parse(url: str) -> str:
    """
    Fetch and parse the URL's HTML content.

    :param url: URL to fetch and parse.
    :return: Cleaned text extracted from the main content or an empty string on failure.
    """
    for attempt in range(RETRIES):
        try:
            logger.debug("Fetching URL: %s", url)
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()  # Raise an HTTPError for bad requests
            soup = BeautifulSoup(response.text, "html.parser")

            main_content = extract_main_content(soup)
            if main_content:
                cleaned_text = clean_main_content(main_content)
                return cleaned_text
            logger.warning("No main content found in %s", url)
            return ""

        except requests.RequestException as e:
            logger.warning(
                "Error fetching %s (attempt %d): %s", url, attempt + 1, str(e)
            )
            if attempt + 1 == RETRIES:
                return ""


def extract_main_content(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Extract main content from the BeautifulSoup object.

    :param soup: BeautifulSoup object containing the HTML.
    :return: The main content as a BeautifulSoup object.
    """
    main_content = soup.find("main") or soup.find("article") or soup.body
    if main_content:
        for tag in main_content.find_all(["header", "footer", "aside", "nav"]):
            tag.decompose()
    return main_content


def clean_main_content(content: BeautifulSoup) -> str:
    """
    Extract and clean the text from the main content and convert it to Markdown.

    :param content: BeautifulSoup object of the main content.
    :return: Markdown formatted string.
    """
    html = str(content)
    markdown_text = html2text.html2text(html)
    # Remove image tags using regex
    markdown_text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", markdown_text)
    # Remove empty lines
    non_empty_lines = [line for line in markdown_text.split("\n") if line.strip()]
    return "\n".join(non_empty_lines)


def main(site_key: str):
    """
    Main function to load URLs, process them, and save the extracted content.

    :param site_key: The site key to use from the config.
    """
    file_path = os.path.join(BASE_URL_PATH, f"{site_key}.json")
    data = load_metadata_from_file(file_path)
    urls = data.get("urls", [])
    timestamp = data.get("timestamp", "")
    domain = data.get("domain", "unknown")

    if not urls:
        logger.error("No URLs found in %s", file_path)
        return

    all_text = f"Domain: {domain}\nTimestamp: {timestamp}\n\n"
    progress_bar = tqdm(urls, desc=f"Processing {site_key} URLs", unit="url")

    for url in progress_bar:
        text = fetch_and_parse(url)
        all_text += text + "\n"

    all_text = all_text.strip()

    output_file = os.path.join(OUTPUT_DIR, f"{site_key}.md")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(all_text)

    logger.info("All text has been written to %s", output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape and parse content from specified URLs."
    )
    parser.add_argument(
        "--site_key", required=True, help="The site key to use from the config."
    )
    args = parser.parse_args()

    main(args.site_key)
