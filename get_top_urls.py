# Fetch the urls from google search for the given query(company_name) 
# for top 50 results, i.e., five pages.
#
# @author anshul_rao
#

from urllib2 import urlopen
from bs4 import BeautifulSoup
import urllib2
import re

#keep count of all the links
link_count=1

def crawlGoogle(val, page_count):
	query=val.strip().split()
	query="+".join(query)
	global link_count
	for count in range(page_count):		
		html = "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"+"&start="+str(count)
		req = urllib2.Request(html, headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(urlopen(req).read(),"html.parser")
		reg=re.compile(".*&sa=")
		links = []
		#parsing web urls
		for item in soup.find_all('h3', attrs={'class' : 'r'}):
    			line = (reg.match(item.a['href'][7:]).group())
    			links.append(line[:-4])
		for link in links:
			print(str(link_count)+" :: "+link+"\n")
			link_count+=1
		count+=10

x=input()
crawlGoogle(str(x), 5)
