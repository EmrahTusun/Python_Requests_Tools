import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

targetUrl = input("URL örnek ('https://example.com'): ").rstrip("/")
foundLinks = []

def getSource(url):
    try:
        response = requests.get(url, timeout=3)
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException:
        return None

def crawl(url):
    source = getSource(url)
    if not source:
        return

    for tag in source.find_all("a"):
        link = tag.get("href")
        if not link:
            continue

        full_link = urljoin(url, link)
        full_link = full_link.split("#")[0]

        if urlparse(full_link).netloc == urlparse(targetUrl).netloc:
            if full_link not in foundLinks:
                foundLinks.append(full_link)
                print("Bulundu URL -->", full_link)
                crawl(full_link)

crawl(targetUrl)
