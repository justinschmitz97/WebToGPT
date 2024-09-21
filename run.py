# run.py

import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Run both sitemapper and scraper scripts in sequence.')
    parser.add_argument('site_key', help='The site key to use from the config.')

    args = parser.parse_args()
    site_key = args.site_key

    # Run the site mapper script
    subprocess.run(['python', 'sitemapper.py', site_key], check=True)
    
    # Run the scraper script
    subprocess.run(['python', 'scraper.py', site_key], check=True)

if __name__ == '__main__':
    main()