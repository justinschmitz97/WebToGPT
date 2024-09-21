# WebToGPT

WebToGPT is a two-stage web crawler and scraper tool designed for parsing and extracting main content from web documentation sites.
The content is saved as a text file to use as custom knowledge files for enhancing Language Model capabilities.

It consists of two main scripts: `sitemapper.py` for crawling URLs and `scraper.py` for extracting and cleaning content.

The entire process can be executed sequentially using `run.py`.

## Features

- Supports excluding specific URL patterns and file extensions
- Fetches and parses HTML content
- Extracts main content from pages
- Configurable via `config.json`
- Sequential execution with `run.py`

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/justinschmitz97/WebToGPT.git
cd WebToGPT
pip install -r requirements.txt
```

## Configuration

Modify the `config.json` file to add or update site configurations:

```json
{
  "default": {
    "base_url": "",
    "excluded_patterns": [],
    "max_concurrency": 10
  },
  "react": {
    "base_url": "https://react.dev",
    "excluded_patterns": ["community"]
  }
  // Add your additional site configurations here
}
```

## Usage

Run the entire process for a specific site key:

```bash
python run.py <site_key>
```

Run the sitemapper or scraper individually:

```bash
python sitemapper.py <site_key>
python scraper.py <site_key>
```

## License

This project is licensed under the Apache 2.0 License.

## Contribution

Feel free to open issues or submit pull requests to improve this project.

Special thanks to the developers and documenters of the libraries and tools used in this project.

---

Happy crawling and scraping!
