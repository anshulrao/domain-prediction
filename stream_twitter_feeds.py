# This code will simply stream the twitter feeds.
# The stream will be filtered based on the company name entered.
#
# @author anshul_rao
#
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#User credentials to access Twitter API
access_token = "ENTER_ACCESS_TOKEN"
access_token_secret = "ENTER_TOKEN_SECRET"
consumer_key = "ENTER_CONSUMER_KEY"
consumer_secret = "ENTER_CONSUMER_SECRET"

f = open("twitter_company_stream.txt", "w")

#This is a listener that will write the feeds in the file "twitter_company_stream".
class Listener(StreamListener):

    def on_data(self, data):
        f.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    company_name=str(input())
    listener = Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    Stream(auth, listener).filter(track=[company_name])
    
f.close()
