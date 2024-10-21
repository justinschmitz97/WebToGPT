#run.py

"""
This script runs both the sitemapper and scraper scripts sequentially for multiple sites,
either using site keys from a configuration file or a provided base URL.
"""

import argparse
import concurrent.futures
import subprocess
import json
from urllib.parse import urlparse


def run_site(site_key):
    """
    Execute sitemapper and scraper with the given site key.

    :param site_key: The site key to use from the config.
    """
    subprocess.run(["python", "sitemapper.py", "--site_key", site_key], check=True)
    subprocess.run(["python", "scraper.py", "--site_key", site_key], check=True)


def run_with_url(url):
    """
    Ensure the provided URL includes a scheme and run sitemapper with the normalized base URL.

    :param url: The base URL to run the scripts with.
    """
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "https://" + url

    subprocess.run(["python", "sitemapper.py", "--url", url], check=True)
    site_key = url.replace("https://", "").replace("http://", "").replace("/", "_")
    subprocess.run(["python", "scraper.py", "--site_key", site_key], check=True)


def load_all_site_keys(config_file):
    """
    Load all site keys from the JSON config file, excluding the "default" key.

    :param config_file: Path to the JSON config file.
    :return: A list of site keys.
    """
    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)
    return [key for key in config.keys() if key != "default"]


def main():
    """
    Main function to parse command-line options and run the scripts accordingly.
    """
    parser = argparse.ArgumentParser(
        description="Run both sitemapper and scraper scripts in sequence for multiple sites."
    )
    parser.add_argument(
        "--config", help="The site key(s) to use from the config.", nargs="*"
    )
    parser.add_argument("--url", help="A base URL to run the scripts with.")
    args = parser.parse_args()

    if args.url:
        run_with_url(args.url)
    elif args.config:
        site_keys = args.config
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(run_site, site_keys)
    else:
        config_file = "config.json"
        site_keys = load_all_site_keys(config_file)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(run_site, site_keys)


if __name__ == "__main__":
    main()
