import tweepy, json
from time import sleep
from credentials import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

def doRetweet(id_string):
    try:
        print ('Retweeted the tweet.')
        print('---------------------------\n')
        # authenticate against the Twitter API
        api = tweepy.API(auth1)
        # actually do the retweet
        api.retweet(id_string)
        return
    except tweepy.TweepError as e:
        print(e.reason)
        print('---------------------------\n')


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        #print ('')
        # looks at the json and see if we have pic.twitter.com there somewhere
        tweet_id = decoded['id_str']
        tweet_user = decoded['user']['screen_name']
        print('---------------------------\nTweet by: @'+tweet_user)
        if (tweet_user != "CreativeCodeBot"):
            print(tweet_id)
            doRetweet(tweet_id)
        else:
            print('Not going to retweet myself!')
        return True

    def on_error(self, status_code):
        print('---------------------------\n')
        print(status_code)

#This handles Twitter authetification and the connection to Twitter 
l = MyStreamListener()
auth1 = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(OATH_KEY, OATH_SECRET)
stream = Stream(auth=auth1, listener=l)

#This line filter Twitter Streams to capture data
stream.filter(track=['#creativecode','#generativeart','#creativecoding','#creativecoding','creativecode','#p5js','#procedural','#generative','#procgen'])
