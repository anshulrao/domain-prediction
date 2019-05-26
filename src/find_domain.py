#!/usr/bin/env python3

# A simple trick to predict domain of company from the streamed twitter feeds.
# 
# Example:
#  > Company: microsoft
#  > Domains: com, edu, in, io, ...
#  > Stream twitter feeds. Filter the stream via company name, i.e., "microsoft" -> microsoft_twitter_stream.py
#  > Look for  the different domains in the feeds, i.e., search for ".com", ".edu", etc.
#  > The domain with maximum count wins!
#
# @author anshulrao
#

DOMAIN_COUNT = 3
f = open("../data/microsoft_twitter_stream.txt", "r")
count = [0] * DOMAIN_COUNT
domains = [".com", ".edu", ".io"]
maximum = 0
index = 0
for line in f:
    for i in range(DOMAIN_COUNT):
        if domains[i] in str(line):
            count[i] = count[i] + 1
            if maximum < count[i]:
                maximum = count[i]
                index = i

print("microsoft%s" % domains[index])
f.close()
