#!/usr/bin/python3
"""Module for tweep program"""
import tweepy
from credentials import *

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Connection test
user = api.me()
print (user.name)

# Follow everyone following
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone that is following " + user.name)

"""
def mainFunction():
    search = "Supply Chain"

    numberOfTweets = 10

    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print('Retweeted the tweet')

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
"""
