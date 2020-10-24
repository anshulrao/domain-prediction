# Domain Prediction

Simple tool to predict domain names of companies.

**Input**: Company Name

**Output**: Domain of the company

**Examples**:

 1.) Microsoft: microsoft.com
 
 2.) Split an Atom: splitanatom.com

How are we predicting domain?

1. We stream twitter feeds for the given company name.
2. We have buckets of popular doman suffixes like ".com, ".org", etc. and we filter the stream and put the frequency of suffixes in these buckets.
3. The bucket with maximum frequency wins!

This is very basic and a lot of nuances need to be taken care of so that it to works for a a wider range of company names:-
- Having an exhaustive list of domain suffixes.
- Extracting full domain name from feeds instead of looking for only suffixes.
- Handling long complicated company names.


There is another way to predict the domain names by crawling google search results but it is yet to be explored in detail and it is slightly volatile since google
keeps changing frequently and crawling it effectively for a long time is challenging.
Still, I am printing the top domains by crawling google in the main script. Just for the sake of information.

**USAGE**:
```
>> python3 find_domain.py amazon
Top domains obtained by crawling Google:  {'www.amazon.com', 'www.aboutamazon.com', 
                                           'www.amazon.in', 'www.primevideo.com'}
Domain predicted (using twitter streams): amazon.com
```
