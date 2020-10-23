#!/usr/bin/env python3

# This script will simply stream the twitter feeds.
# The stream will be filtered based on the company name entered.
#
# @author anshulrao
#
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import time

# user credentials to access Twitter API
# below entries aer bogus since the real ones are confidential.
access_token = "2238719426-q1TcqfS9FCpkclFWMrR0OEHKKAfdgdfvwqvL"
access_token_secret = "qVjXKNXVKVx3bY4paSlRIEurasaPUJwB56SdRQ7G"
consumer_key = "3nx4HvvQ3a4luiolhKedHpmuEh"
consumer_secret = "ViSxTWY9ffWe9HgLWMkn2RsMgdfgd57JLmFbEaTHKcGOKIT"

"""
> python3 stream_twitter_feeds.py
amazon

"""


def dump_stream_feeds(company_name):
    f = open(f"../data/twitter_{company_name}_stream.txt", "w")

    class MyListener(StreamListener):
        """
        A listener that will write the feeds in the file.
        The default time limit is 1 minute, i.e., 60 seconds.

        """
        def __init__(self, time_limit=60):
            self.start_time = time.time()
            self.limit = time_limit

        def on_data(self, data):
            if (time.time() - self.start_time) < self.limit:
                f.write(data)
                return True
            else:
                f.close()
                return False

        def on_error(self, status):
            print(status)

    listener = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=[company_name])
    stream.disconnect()


def main():
    dump_stream_feeds(str(input()))


if __name__ == '__main__':
    main()
