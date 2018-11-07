# python 3rd party module for Twitter API and handling api authentication
import tweepy
from tweepy import OAuthHandler

# insert your twitter dev credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# authenticate and build object to be handle by object
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)