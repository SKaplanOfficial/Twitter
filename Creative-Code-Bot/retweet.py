import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#creativecode').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        sleep(120)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
