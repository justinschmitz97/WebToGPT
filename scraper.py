import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import logging
import os
from urllib.parse import urlparse
import argparse
import html2text  # Import html2text

# --- Configuration ---
BASE_URL_PATH = 'urls/'
OUTPUT_DIR = 'data/'
RETRIES = 3  # Number of retries for network requests
LOG_LEVEL = logging.INFO
# ----------------------

# Initialize Logger
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

def load_metadata_from_file(file_path: str) -> dict:
    """Load metadata and URLs from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, dict) and 'urls' in data:
                return data
            logger.error(f"Unexpected JSON structure in {file_path}")
            return {}
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Error reading {file_path}: {e}")
        return {}

def fetch_and_parse(url: str) -> str:
    """Fetch and parse the URL's HTML content."""
    for attempt in range(RETRIES):
        try:
            logger.debug(f"Fetching URL: {url}")
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad requests
            soup = BeautifulSoup(response.text, 'html.parser')
            
            main_content = extract_main_content(soup)
            if main_content:
                cleaned_text = clean_main_content(main_content)
                return cleaned_text
            logger.warning(f"No main content found in {url}")
            return ""
        
        except requests.RequestException as e:
            logger.warning(f"Error fetching {url} (attempt {attempt + 1}): {e}")
            if attempt + 1 == RETRIES:
                return ""

def extract_main_content(soup: BeautifulSoup) -> BeautifulSoup:
    """Extract main content from the BeautifulSoup object."""
    main_content = soup.find('main') or soup.find('article') or soup.body
    if main_content:
        for tag in main_content.find_all(['header', 'footer', 'aside', 'nav']):
            tag.decompose()
    return main_content

def clean_main_content(content: BeautifulSoup) -> str:
    """Extract and clean the text from the main content and convert it to Markdown."""
    html = str(content)
    markdown_text = html2text.html2text(html)
    return markdown_text

def main(site_key):
    file_path = os.path.join(BASE_URL_PATH, f"{site_key}.json")
    data = load_metadata_from_file(file_path)
    urls = data.get('urls', [])
    timestamp = data.get('timestamp', '')
    domain = data.get('domain', 'unknown')
    
    if not urls:
        logger.error(f"No URLs found in {file_path}")
        return
    
    all_text = f"Domain: {domain}\nTimestamp: {timestamp}\n\n"
    
    for url in urls:
        logger.info(f"Processing {url}")
        text = fetch_and_parse(url)
        all_text += text + " "  # Separate text from different pages with a space
    
    all_text = all_text.strip()  # Ensure no leading/trailing whitespace

    output_file = os.path.join(OUTPUT_DIR, f'{site_key}.md')  # Save as Markdown file

    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure output directory exists
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(all_text)
    
    logger.info(f"All text has been written to {output_file}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("site_key", help="The site key to use from the config.")
    args = parser.parse_args()

    main(args.site_key)