import tweepy
import configparser
import pandas as pd

# read config credentials here
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication here
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class Linstener(tweepy.Stream):

    tweets = []
    limit = 100

    def on_status(self, status):
        self.tweets.append(status)
        # testing
        # print(status.user.screen_name + ": " + status.text)

        if len(self.tweets) == self.limit:
            self.disconnect()

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

# stream by keyword search here
keywords = ['2022', '#Ukraine']
stream_tweet.filter(track=keywords)


# stream by users here
#users = ['Ukraine']
#user_ids = []
#for user in users:
#    user_ids.append(api.get_user(screen_name=user).id)
# testing
#print(user_ids)   #[44196397, 168987151]
#stream_tweet.filter(follow=user_ids)


# create df
columns = ['User', 'Tweet', 'Time']
data = []

for tweet in stream_tweet.tweets:
    if not tweet.truncated:
        data.append([tweet.user.screen_name, tweet.text, tweet.created_at])
    else:
        data.append([tweet.user.screen_name, tweet.extended_tweet['full_text'], tweet.created_at])

df = pd.DataFrame(data, columns=columns)
#print to test
print(df)
#save to csv
df.to_csv('Ukraine Twitter.csv')