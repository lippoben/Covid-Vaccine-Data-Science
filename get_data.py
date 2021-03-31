import os
import tweepy as tw
import pandas as pd

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
search_words = "#Vaccine -filter:retweets -filter:media -filter:native_video -filter:periscope -filter:vine"
date_since = "2018-11-16"
number_tweets = 5

tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(number_tweets)

# Collect a list of tweets
tweets = [tweet.text for tweet in tweets]
print(tweets)



