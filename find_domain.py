# A simple trick to predict domain of compant from the streamed twitter feeds.
# 
# Example:
#  > Company: microsoft
#  > Domains: com, edu, in, io, ...
#  > Stream twitter feeds. Filter the stream via company name, i.e., "microsoft" -> stream_twitter_feeds.py
#  > Look for  the different domains in the feeds, i.e., search for ".com", ".edu", etc.
#  > The domain with maximum count wins!
#
# @author anshul_rao
#

DOMAIN_COUNT=3
f = open("twitter_company_stream.txt", "r")
count=[0]*DOMAIN_COUNT
domains=[".com", ".edu", ".io"]
maximum=0
index=0
for line in f:
  for i in range(DOMAIN_COUNT):
    if domains[i] in str(line):
      count[i]=count[i]+1
      if maximum<count[i]:
	      maximum=count[i]
	      index=i
        
print(domains[index])
f.close()
