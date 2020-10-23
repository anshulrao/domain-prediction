#!/usr/bin/env python

# Fetch the urls from google search for the given query(company_name)
#
# @author anshulrao
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib


def crawl_google(company_name, display=False):
    """
    Crawl google search results for given company name and return relevant/valid web addresses.

    > python3 get_top_urls.py
    amazon
    1 :: www.amazon.in
    2 :: www.primevideo.com
    3 :: www.amazon.com
    4 :: www.aboutamazon.com


    """

    query = company_name.strip().split()
    query = "+".join(query)
    links = set()
    for i in range(5):
        html = "https://www.google.co.in/search?site=&source=hp&q=" + query + "&gws_rd=ssl" + "&start=" + str(i)
        req = urllib.request.Request(html, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
                                                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                  'Chrome/35.0.1916.47 Safari/537.36'})
        soup = BeautifulSoup(urlopen(req).read(), "html.parser")
        # parsing web urls
        for item in soup.findAll('cite'):
            link = item.text
            if link.startswith(("https://", 'www.')) and ' ' not in link:
                links.add(link)

    if display:
        for i, link in enumerate(links):
            print(i+1, "::", link)

    return links


def main():
    """
    The main function.

    """
    crawl_google(str(input()), display=True)


if __name__ == "__main__":
    main()

