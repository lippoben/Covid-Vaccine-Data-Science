import os
import tweepy as tw
import pandas as pd
import numpy as np


pd.set_option('display.width', 32000)
np.set_printoptions(linewidth=32000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)

'''
API Key = L3oCvIZuE3YXROTL3L4L8FCLb
API Secret Key = WPvbN8NhBXpMMcBNa4UJrcS7wEy8mqSbK6R5HOPXppwYXW6fJN
Bearer Token = AAAAAAAAAAAAAAAAAAAAADisOAEAAAAA0p4UGsNPi2CQjR%2B0pTyJYRjcybY%3Dc4CZLk7SA44fryXMC28s1tuMtvkoJinGwVhtVLesWwgMhHwKHv
Access Token = 1375065604068106241-faoRSTkxKoXF6BX2fTvUALmc9Oy1sd
Access Token Secret = 6Trgdv4ztS9VgMipVEbb0lPHwM8FEZYiMYnjRepBMMHwt
'''

consumer_key= 'L3oCvIZuE3YXROTL3L4L8FCLb'
consumer_secret= 'WPvbN8NhBXpMMcBNa4UJrcS7wEy8mqSbK6R5HOPXppwYXW6fJN'
access_token= '1375065604068106241-faoRSTkxKoXF6BX2fTvUALmc9Oy1sd'
access_token_secret= '6Trgdv4ztS9VgMipVEbb0lPHwM8FEZYiMYnjRepBMMHwt'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term, the date_since date and the number of tweets as variables
# Can prevent certain things coming up in tweets: https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
search_words = "#Vaccine -filter:retweets -filter:media -filter:native_video -filter:periscope -filter:vine"
date_since = "2018-11-16"
number_tweets = 5

tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(number_tweets)


tweet_data = [[tweet.user.screen_name, tweet.text, tweet.user.location] for tweet in tweets]

tweet_dataframe = pd.DataFrame(data=tweet_data,
                    columns=['username', 'text', "location"])

print(tweet_dataframe)



