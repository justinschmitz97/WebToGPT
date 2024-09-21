import argparse
import concurrent.futures
import subprocess
import json
from urllib.parse import urlparse

def run_site(site_key):
    # Execute sitemapper and scraper with the given site key
    subprocess.run(['python', 'sitemapper.py', '--site_key', site_key], check=True)
    subprocess.run(['python', 'scraper.py', '--site_key', site_key], check=True)

def run_with_url(base_url):
    # Ensure the provided URL includes a scheme
    parsed_url = urlparse(base_url)
    if not parsed_url.scheme:
        base_url = 'https://' + base_url
    
    # Run sitemapper with the normalized base URL
    subprocess.run(['python', 'sitemapper.py', '--base_url', base_url], check=True)
    
    # Generate a site key by transforming the base URL
    site_key = base_url.replace('https://', '').replace('http://', '').replace('/', '_')
    
    # Run scraper with the generated site key
    subprocess.run(['python', 'scraper.py', '--site_key', site_key], check=True)

def load_all_site_keys(config_file):
    # Load all site keys from the JSON config file, excluding the "default" key
    with open(config_file, 'r') as f:
        config = json.load(f)
    return [key for key in config.keys() if key != "default"]

def main():
    # Set up argument parser for command-line options
    parser = argparse.ArgumentParser(description='Run both sitemapper and scraper scripts in sequence for multiple sites.')
    parser.add_argument('--config', help='The site key(s) to use from the config.', nargs='*')
    parser.add_argument('--url', help='A base URL to run the scripts with.')

    args = parser.parse_args()

    if args.url:
        run_with_url(args.url)  # Run with the provided URL
    elif args.config:
        # Run concurrently for each provided site key
        site_keys = args.config
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(run_site, site_keys)
    else:
        # Load all site keys from default config file and run concurrently
        config_file = 'config.json'
        site_keys = load_all_site_keys(config_file)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(run_site, site_keys)

if __name__ == '__main__':
    main()