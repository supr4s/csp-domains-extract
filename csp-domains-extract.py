import argparse
import requests
import re
import urllib3

# Disable warnings about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_csp(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        csp = response.headers.get('Content-Security-Policy', '')
        return csp
    except requests.RequestException:
        return ''

def extract_domains_from_csp(csp):
    # Pattern to match domains in the CSP
    pattern = re.compile(r"https?://(?:\*\.)?([a-zA-Z0-9.-]+)|(?:\*\.)?([a-zA-Z0-9.-]+)")
    matches = pattern.findall(csp)
    # Flatten the list of tuples and filter out empty strings
    domains = {match[0] or match[1] for match in matches if match[0] or match[1]}
    # Filter to keep only valid domain names
    valid_domains = {domain for domain in domains if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain)}
    return valid_domains

def main():
    parser = argparse.ArgumentParser(description='Extract domains from CSP headers.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', type=str, help='Single URL to process')
    group.add_argument('-ul', '--url-list', type=str, help='File containing list of URLs to process')
    parser.add_argument('-o', '--output', type=str, help='Output file to store results', required=False)

    args = parser.parse_args()

    urls = []
    if args.url:
        urls.append(args.url)
    elif args.url_list:
        try:
            with open(args.url_list, 'r') as file:
                urls = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File {args.url_list} not found.")
            return

    all_domains = set()
    for url in urls:
        csp = fetch_csp(url)
        if csp:
            domains = extract_domains_from_csp(csp)
            all_domains.update(domains)
    
    if args.output:
        with open(args.output, 'w') as file:
            for domain in sorted(all_domains):
                file.write(f"{domain}\n")
        print(f"Results saved to {args.output}")
    else:
        for domain in sorted(all_domains):
            print(domain)

if __name__ == '__main__':
    main()
