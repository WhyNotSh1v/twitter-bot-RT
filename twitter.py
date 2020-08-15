import tweepy
import time


auth = tweepy.OAuthHandler('bcp6jbqOQuAwGblkXGbFyFisr','ivpzRBT4bLVdVllhHC1CIDbNUzkaR1rMlM2x1RTRBEKLwRLAYv')
auth.set_access_token('1293555958291943429-PhaIDEF1IfYWLkbZPshQakbL33rWLG','FBWCNjBWJ8T6mGRKfwnON9uKai87H7XE2qPGehJo37aXy')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Madurai'
nrTweets = 500

for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Tweet RTed')
        tweet.retweet()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
