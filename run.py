import argparse
import concurrent.futures
import subprocess

def run_site(site_key):
    # Run the site mapper script
    subprocess.run(['python', 'sitemapper.py', site_key], check=True)
    
    # Run the scraper script
    subprocess.run(['python', 'scraper.py', site_key], check=True)

def main():
    parser = argparse.ArgumentParser(description='Run both sitemapper and scraper scripts in sequence for multiple sites.')
    parser.add_argument('site_keys', nargs='+', help='The site keys to use from the config.')

    args = parser.parse_args()
    site_keys = args.site_keys

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map the site_keys to the run_site function, running them concurrently
        executor.map(run_site, site_keys)

if __name__ == '__main__':
    main()