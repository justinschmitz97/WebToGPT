import argparse
import json
import logging
import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
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


def merge_consecutive_p_types(data):
    """
    Merge consecutive 'p' types in the content array of the JSON structure.
    """
    for page in data.get("pages", []):
        merged_content = []
        temp_text = ""

        for content in page.get("content", []):
            if content["type"] == "p":
                # Accumulate text for consecutive 'p' types
                temp_text += content["text"] + " "
            else:
                # If a non-'p' type is encountered, finalize the accumulated text
                if temp_text:
                    merged_content.append({"type": "p", "text": temp_text.strip()})
                    temp_text = ""
                merged_content.append(content)

        # Add any remaining accumulated text
        if temp_text:
            merged_content.append({"type": "p", "text": temp_text.strip()})

        # Replace the original content with the merged content
        page["content"] = merged_content

    return data


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
                structured_content = list(extract_structured_content(main_content))
                page_data = {"url": url, "title": title, "content": structured_content}

                # Apply the merge_consecutive_p_types function here
                page_data = merge_consecutive_p_types({"pages": [page_data]})["pages"][
                    0
                ]

                return page_data
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


def merge_paragraphs(paragraphs: list) -> dict:
    return {"type": "p", "text": " ".join(paragraphs)}


def extract_structured_content(content: BeautifulSoup):
    current_paragraph = []

    for element in content.children:
        if isinstance(element, str) and not element.strip():
            continue  # Skip empty text nodes

        if isinstance(element, Tag):  # Only process Tag objects
            if element.name == "p":
                # Extract text and filter out paragraphs with fewer than 6 words
                paragraph_text = element.get_text(separator=" ", strip=True)
                if (
                    paragraph_text and len(paragraph_text.split()) >= 6
                ):  # Check word count
                    current_paragraph.append(paragraph_text)
            else:
                # Merge all accumulated paragraphs into one before processing non-paragraph elements
                if current_paragraph:
                    yield merge_paragraphs(current_paragraph)
                    current_paragraph = []  # Reset the paragraph accumulator list

                # Process specific element types
                if element.name in ["ul", "ol"]:
                    list_items = [
                        li.get_text(separator=" ", strip=True)
                        for li in element.find_all("li")
                    ]
                    # Filter out lists with only one item that has fewer than 6 words
                    if not (len(list_items) == 1 and len(list_items[0].split()) < 6):
                        yield {"type": "list", "items": list_items}
                elif element.name == "pre":
                    code = element.get_text(separator=" ", strip=True)
                    yield {"type": "code", "code": code}
                else:
                    # Recursively process other elements
                    yield from extract_structured_content(element)

    # After iterating, merge any remaining paragraphs
    if current_paragraph:
        yield merge_paragraphs(current_paragraph)


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
