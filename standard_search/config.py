# python 3rd party module to authenticate and access Twitter API
import tweepy
from tweepy import OAuthHandler

# insert twitter dev credentials below
consumer_key = ''
consumer_secret = ''

# authenticate and build object to be handle by object
auth = OAuthHandler(consumer_key, consumer_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)