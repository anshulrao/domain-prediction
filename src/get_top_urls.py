#!/usr/bin/env python

# Fetch the urls from google search for the given query(company_name)
# for top 50 results, i.e., five pages.
#
# @author anshulrao
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

# keep count of all the links
link_count = 1


def crawl_google(val, page_count):
    """
    Crawl google search results for given search variable=val and that too up to 'page_count' no. of pages.

    >>> crawl_google('google', 5)
    1 :: https://www.google.com/
    2 :: https://twitter.com/Google
    3 :: https://www.facebook.com/Google/
    4 :: https://www.youtube.com/user/googleindia
    5 :: https://www.youtube.com/Google
    6 :: https://www.google.co.in/maps
    7 :: https://twitter.com/google?lang=en
    8 :: https://www.facebook.com/Google/
    9 :: https://www.youtube.com/user/googleindia
    10 :: https://www.youtube.com/Google
    11 :: https://www.google.co.in/maps
    12 :: https://www.google.co.in/alerts
    13 :: https://en.wikipedia.org/wiki/Google
    14 :: https://about.google/intl/en/
    15 :: https://www.thinkwithgoogle.com/
    16 :: https://www.android.com/tv/
    17 :: https://twitter.com/google?lang=en
    18 :: https://www.facebook.com/Google/
    19 :: https://www.youtube.com/user/googleindia
    20 :: https://www.youtube.com/Google
    21 :: https://www.google.co.in/maps
    22 :: https://www.google.co.in/alerts
    23 :: https://en.wikipedia.org/wiki/Google
    24 :: https://about.google/intl/en/
    25 :: https://www.android.com/
    26 :: https://www.thinkwithgoogle.com/
    27 :: https://twitter.com/google?lang=en
    28 :: https://www.facebook.com/Google/
    29 :: https://www.youtube.com/user/googleindia
    30 :: https://www.youtube.com/Google
    31 :: https://www.google.co.in/maps
    32 :: https://www.google.co.in/alerts
    33 :: https://en.wikipedia.org/wiki/Google
    34 :: https://about.google/intl/en/
    35 :: https://www.android.com/
    36 :: https://www.thinkwithgoogle.com/
    37 :: https://twitter.com/google?lang=en
    38 :: https://www.facebook.com/Google/
    39 :: https://www.youtube.com/user/googleindia
    40 :: https://www.youtube.com/Google
    41 :: https://www.google.co.in/maps
    42 :: https://www.google.co.in/alerts
    43 :: https://en.wikipedia.org/wiki/Google
    44 :: https://about.google/intl/en/
    45 :: https://www.android.com/
    46 :: https://www.thinkwithgoogle.com/
    """

    query = val.strip().split()
    query = "+".join(query)
    global link_count
    for count in range(page_count):
        html = "https://www.google.co.in/search?site=&source=hp&q=" + query + "&gws_rd=ssl" + "&start=" + str(count)
        req = urllib.request.Request(html, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
                                                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                  'Chrome/35.0.1916.47 Safari/537.36'})
        soup = BeautifulSoup(urlopen(req).read(), "html.parser")
        links = []
        # parsing web urls
        for item in soup.findAll('cite'):
            link = item.text
            if link.startswith("https://"):
                links.append(link)
        for link in links:
            print(str(link_count) + " :: " + link)
            link_count += 1
        count += 10


company_name = input("Enter company name :: ")
crawl_google(str(company_name), 5)
