import tweepy
from dotenv import dotenv_values

# Load key variables from .env file
config = dotenv_values(".env")

# Access variables
consumer_key = config.get("CONSUMER_KEY")
consumer_secret = config.get("CONSUMER_SECRET")
access_token = config.get("ACCESS_TOKEN")
access_token_secret = config.get("ACCESS_TOKEN_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets
keyword = 'sport'
tweets = api.search_tweets(q=keyword)

# Print the tweets
for tweet in tweets:
    print(tweet.text)