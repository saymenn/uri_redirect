import requests
import sys
from concurrent.futures import ThreadPoolExecutor
requests.packages.urllib3.disable_warnings()

def location_header_check(resp):
    status = resp.status_code
    if status == 302 or status == 301 or status == 308:
        headers = resp.headers
        if "Location" in headers:
            location = resp.headers['Location']
        elif "location" in headers:
            location = resp.headers['location']
        if location:
            if location == "https://google.com":
                return True
            else:
                return False
        else:
            print("[-] no location header error")
            sys.exit(0)

def main(url):
    url = url + payload
    try:
        resp = requests.get(url, verify = False, allow_redirects=False, timeout = 20)
        if location_header_check(resp):
            print("[+] potential redirect: ", url)
        else:
            pass
    except Exception as error:
        pass

payload = "//https://google.com"

script, urls_file, threads = sys.argv

if urls_file:
    with open(urls_file, 'r') as urls:
        with ThreadPoolExecutor(max_workers=int(threads)) as executor:
            executor.map(main, (url.strip() for url in urls))