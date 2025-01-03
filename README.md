WebToGPT is a two-stage web crawler and scraper tool designed for parsing and extracting main content from web documentation sites. The content is saved as text files to be used as custom knowledge bases for enhancing Language Model capabilities, such as for training AI assistants.

It consists of two main scripts:

1. `sitemapper.py` for crawling URLs and generating sitemaps.
2. `scraper.py` for extracting and cleaning content from the crawled URLs.

The entire process can be executed sequentially using the `main.py` script (if provided), or you can run each step individually.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Installation](#installation)
  - [Additional Installation Steps](#additional-installation-steps)
- [Configuration](#configuration)
  - [config.json](#configjson)
  - [Site Configuration Parameters](#site-configuration-parameters)
- [Usage](#usage)
  - [Running the Entire Process](#running-the-entire-process)
  - [Running Individual Scripts](#running-individual-scripts)
    - [Running the Sitemapper](#running-the-sitemapper)
    - [Running the Scraper](#running-the-scraper)
- [Examples](#examples)
  - [Example Configuration for MDN Web Docs](#example-configuration-for-mdn-web-docs)
  - [Running the Sitemapper for MDN](#running-the-sitemapper-for-mdn)
  - [Running the Scraper for MDN](#running-the-scraper-for-mdn)
- [Output](#output)
  - [Sitemapper Output](#sitemapper-output)
  - [Scraper Output](#scraper-output)
- [Dependencies](#dependencies)
- [License](#license)
- [Contribution](#contribution)

---

## Features

- **Configurable Crawling and Scraping**: Customize crawling and scraping behavior using `config.json`.
- **Pattern-Based URL Inclusion/Exclusion**: Include or exclude URLs based on regex patterns.
- **Domain Restriction**: Crawl within a specified domain or URL prefix.
- **Extension Filtering**: Exclude URLs pointing to unwanted file types (e.g., images, videos).
- **Asynchronous Fetching**: Efficiently fetch pages using asynchronous I/O.
- **Content Extraction**: Extracts main content from pages, removing headers, footers, and unwanted elements.
- **Markdown Conversion**: Converts fetched HTML content into clean Markdown files.
- **Caching**: Caches fetched pages to avoid redundant requests.
- **Logging**: Provides detailed logging for monitoring the crawling and scraping processes.

---

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/justinschmitz97/WebToGPT.git
cd WebToGPT
pip install -r requirements.txt
```

### Additional Installation Steps

Some of the dependencies, like `playwright`, require additional setup:

1. **Install Playwright Browsers**:

   ```bash
   playwright install
   ```

---

## Configuration

The behavior of the crawler and scraper is controlled via the `config.json` file and individual site configuration files.

### config.json

The `config.json` file contains site-specific configurations. Each site key corresponds to a unique set of configurations for crawling and scraping.

```jsonc
{
  "default": {
    "url": "",
    "excluded_patterns": [],
    "final_include_patterns": [],
    "included_patterns": [],
    "excluded_classes": [],
    "strict": false
  },
  "site_key_example": {
    "url": "https://example.com",
    "final_include_patterns": ["https://example.com/docs/"],
    "excluded_patterns": ["login", "signup"],
    "included_patterns": ["/docs/"],
    "excluded_classes": ["header", "footer"],
    "strict": true
  }
}
```

### Site Configuration Parameters

- **url** (string): The base URL to start crawling from.
- **strict** (boolean): If `true`, only URLs starting with the base URL are crawled.
- **included_patterns** (list of strings): Regex patterns to include during crawling.
- **excluded_patterns** (list of strings): Regex patterns to exclude during crawling.
- **final_include_patterns** (list of strings): Patterns to filter the final list of URLs after crawling.
- **excluded_classes** (list of strings): CSS class names to exclude during scraping.
- **excluded_extensions** (list of strings): File extensions to exclude during crawling (e.g., `.jpg`, `.pdf`).
- **max_concurrency** (integer): Maximum number of concurrent requests during crawling.

---

## Usage

### Running the Entire Process

To run the crawler and scraper sequentially for a specific site configuration:

```bash
python main.py <site_key>
```

> **Note**: Replace `<site_key>` with the key corresponding to your site in `config.json`.

### Running Individual Scripts

#### Running the Sitemapper

The sitemapper crawls the website and generates a sitemap based on the configurations.

```bash
python sitemapper.py --site_key <site_key> [--strict]
```

- `--site_key`: The key of the site configuration in `config.json`.
- `--strict`: (Optional) Overrides the `strict` mode in the configuration to enforce URL prefix filtering.

#### Running the Scraper

The scraper processes the URLs generated by the sitemapper, extracts the main content, and saves it as Markdown files.

```bash
python scraper.py --site_key <site_key>
```

- `--site_key`: The key of the site configuration in `config.json`.

---

## Examples

### Example Configuration for MDN Web Docs

```json
"mdn": {
  "url": "https://developer.mozilla.org/en-US/docs/Web/HTML/",
  "final_include_patterns": [
    "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/",
    "https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/"
  ],
  "excluded_patterns": [".txt", "/input/", "/rel/"],
  "strict": true
}
```

### Running the Sitemapper for MDN

```bash
python sitemapper.py --site_key mdn --strict
```

### Running the Scraper for MDN

```bash
python scraper.py --site_key mdn
```

---

## Output

### Sitemapper Output

The sitemapper saves the list of crawled URLs into the `urls/` directory as JSON files named after the site key:

- `urls/<site_key>.json`

Example `urls/mdn.json`:

```json
{
  "timestamp": "2023-10-25T14:00:00Z",
  "site_key": "mdn",
  "domain": "https://developer.mozilla.org/en-US/docs/Web/HTML/",
  "total_urls": 150,
  "failed_urls": {},
  "urls": [
    "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a",
    "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div"
    // More URLs...
  ]
}
```

### Scraper Output

The scraper saves the extracted content into the `data/` directory as Markdown files named after the site key:

- `data/<site_key>.md`

Example `data/mdn.md`:

```markdown
# https://developer.mozilla.org/en-US/docs/Web/HTML/

## <a> - The Anchor element

[Read the full article](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)

<!-- Extracted and cleaned content in Markdown format -->

## <div> - The Content Division element

[Read the full article](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)

<!-- Extracted and cleaned content in Markdown format -->
```

---

## Dependencies

The project depends on several Python packages listed in `requirements.txt`. Key dependencies include:

- `aiohttp`: For asynchronous HTTP requests.
- `aiohttp_retry`: For retrying failed HTTP requests.
- `beautifulsoup4`: For parsing HTML content.
- `markdownify`: For converting HTML to Markdown.
- `playwright`: For handling dynamic web pages (if needed).
- `requests`: For synchronous HTTP requests (fallback).
- `lxml`: For fast HTML parsing.

**Note**: Ensure that you have the necessary system dependencies to install these packages, such as build tools for compiling Python packages.

---

## License

This project is licensed under the Apache 2.0 License.

---

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Special thanks to the developers and documenters of the libraries and tools used in this project.

---

Happy crawling and scraping!
