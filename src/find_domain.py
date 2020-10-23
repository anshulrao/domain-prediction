#!/usr/bin/env python3

# A simple trick to predict domain of company from the streamed twitter feeds.
# 
# Example:
#  > Company: microsoft
#  > Domains: com, edu, in, etc.
#  > Stream twitter feeds. Filter the stream via company name, i.e., "microsoft" -> twitter_microsoft_stream.py
#  > Look for  the different domains in the feeds, i.e., search for ".com", ".edu", etc.
#  > The domain with maximum count wins!
#
# @author anshulrao
#
from get_top_urls import crawl_google
from stream_twitter_feeds import dump_stream_feeds

import sys

"""
> python3 find_domain.py amazon
Top domains obtained by crawling Google:  {'www.amazon.com', 'www.aboutamazon.com',
                                           'www.amazon.in', 'www.primevideo.com'}
Domain Prediction: amazon.com


"""


def main():
    """
    The main function

    """
    company = sys.argv[1]
    dump_stream_feeds(company)
    f = open(f"../data/twitter_{company}_stream.txt", "r")

    # the list is not exhaustive and has only common ones for now
    suffixes = [".com", ".edu", ".org", ".net", ".gov"]
    count = [0] * len(suffixes)

    for line in f:
        for i, suffix in enumerate(suffixes):
            if suffix in str(line):
                count[i] += count[i]

    print("Top domains obtained by crawling Google: ", crawl_google(company))
    print(f"Domain Prediction: {company}{suffixes[count.index(max(count))]}")
    f.close()


if __name__ == "__main__":
    main()