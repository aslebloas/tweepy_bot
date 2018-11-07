#!/usr/bin/python3
from datetime import date
import json
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

json_file = 'quotes.json'

startdate = date(2018, 11, 4)
today = date.today()
diff = today.toordinal() - startdate.toordinal()

with open(json_file) as file:
    quotes = json.load(file)
    for quote in quotes:
        if quote['step'] == diff:
            quote_s = "\"Step {}: {}\" #startup #ryanalliswisdom #100stepsto1million".format(
                quote['step'], quote['quote'])
            if len(quote_s) > 280:
                quote_s = "\"Step {}: {}\" #startup #ryanalliswisdom".format(
                    quote['step'], quote['quote'])

try:
    api.update_status(quote_s)
except Exception as e:
    print(e)
else:
    print("tweet posted!")
