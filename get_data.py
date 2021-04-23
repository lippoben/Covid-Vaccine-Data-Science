import tweepy as tw
import pandas as pd
import numpy as np


pd.set_option('display.width', 32000)
np.set_printoptions(linewidth=32000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)

states = {'Alabama': '33.281585,-86.894870,186km', 'Alaska': '57.032659,-154.276345,1084km',
          'Arizona': '33.966672,-111.868993,279km', 'Arkansas': '34.813039,-92.657925,216km',
          'California': '33.878785,-123.577868,671km', 'Colorado': '38.956353,-106.262055,224km',
          'Connecticut': '41.475136,-72.826763,58km', 'Delaware': '39.649232,-75.588967,19km',
          'Florida': '27.198446,-84.699117,494km', 'Georgia': '33.394949,-83.769366,191km',
          'Hawaii': '20.059015,-158.373655,581km', 'Idaho': '43.413682,-114.256366, 255km',
          'Illinois': '41.099193,-89.097585,181km', 'Indiana': '40.539248,-86.265865,164km',
          'Iowa': '42.167893,-93.564345,241km', 'Kansas': '38.385221,-96.837909,200km',
          'Kentucky': '37.873594,-84.347940,134km', 'Louisiana': '30.054156,-91.751547,199km',
          'Maine': '43.932264,-68.766803,184km', 'Maryland': '39.226707,-76.417279,62km',
          'Massachusetts': '42.183335,-70.674852,77km', 'Michigan': '43.372248,-84.624588,188km',
          'Minnesota': '45.182309,-94.422398,188km', 'Mississippi': '32.232354,-89.445932,231km',
          'Missouri': '38.519161,-92.478804,189km', 'Montana': '47.398283,-111.212020, 314km',
          'Nebraska': '41.221794,-98.488939,218km', 'Nevada': '36.568177,-115.389179,121km',
          'New Hampshire': '43.348584,-71.676609,83km', 'New Jersey': '40.625182,-74.483447,60km',
          'New Mexico': '34.426068,-106.204642,283km', 'New York': '40.614464,-73.293319,64km',
          'North Carolina': '35.612931,-79.886186,151km', 'North Dakota': '47.176798,-100.172405,249km',
          'Ohio': '40.300027,-82.826200,200km', 'Oklahoma': '35.438333,-96.994565,178km',
          'Oregon': '44.054582,-123.911371,247km', 'Pennsylvania': '40.784562,-78.609277,177km',
          'Rhode Island': '41.676939,-71.501845,30km', 'South Carolina': '33.157595,-81.374162,219km',
          'South Dakota': '44.017184,-99.929789,275km', 'Tennessee': '36.018890,-84.941055,211km',
          'Texas': '30.786928,-97.670580,379km', 'Utah': '39.726030,-111.971990,264km',
          'Vermont': '44.303859,-72.681658,79km', 'Virginia': '37.567801,-77.118923,132km',
          'Washington': '47.319320,-121.264931,192km', 'West Virginia': '38.678776,-80.604100,176km',
          'Wisconsin': '44.097676,-88.787992,183km', 'Wyoming': '42.870272,-107.572961,309km'}

consumer_key= 'L3oCvIZuE3YXROTL3L4L8FCLb'
consumer_secret= 'WPvbN8NhBXpMMcBNa4UJrcS7wEy8mqSbK6R5HOPXppwYXW6fJN'
access_token= '1375065604068106241-faoRSTkxKoXF6BX2fTvUALmc9Oy1sd'
access_token_secret= '6Trgdv4ztS9VgMipVEbb0lPHwM8FEZYiMYnjRepBMMHwt'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term, the date_since date and the number of tweets as variables
# Can prevent certain things coming up in tweets: https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
search_words = "#Vaccine -filter:retweets -filter:media -filter:native_video -filter:periscope -filter:vine " \
               "-filter:images -filter:twimg -filter:links -url:amazon"
date_since = "2018-11-16"
number_tweets = 10


tweets = tw.Cursor(api.search,
                    q=search_words,
                    geocode='54.600522,-4.153217,553km',
                    lang="en",
                    since=date_since).items(number_tweets)

tweet_data = [[tweet.user.screen_name, tweet.text, tweet.user.location, tweet.retweet_count, tweet.favorite_count,
               tweet.place] for tweet in tweets]

tweet_dataframe = pd.DataFrame(data=tweet_data,
                    columns=['username', 'text', 'location', 'No of retweets', 'likes', 'co ords'])

print(tweet_dataframe)

