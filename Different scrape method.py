import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import numpy as np


def add_geocode(query, state, states_coords):
    query = query + " geocode:" + states_coords[state]
    return query


def add_dates(query, since, until):
    query = query + " since:" + since + " until:" + until
    return query


def scrape_tweets(query, max_tweets, state, start_date, end_date):
    # the scraped tweets, this is a generator
    scraped_tweets = sntwitter.TwitterSearchScraper(query).get_items()
    # slicing the generator to keep only the first 100 tweets
    sliced_scraped_tweets = itertools.islice(scraped_tweets, max_tweets)
    # convert to a DataFrame and keep only relevant columns
    df = pd.DataFrame(sliced_scraped_tweets)[['date', 'content', 'replyCount', 'retweetCount', 'likeCount']]
    df['state'] = state
    df['start date'] = start_date
    df['end date'] = end_date
    return df


def join_datasets(temp_ds, ds):
    ds = pd.concat([ds, temp_ds])
    return ds


pd.set_option('display.width', 32000)
np.set_printoptions(linewidth=32000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)

dates = ['2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01',
         '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01', '2021-03-01']

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
          'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

states_coordinates = {'Alabama': '33.281585,-86.894870,186km', 'Alaska': '57.032659,-154.276345,1084km',
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


# our search term, using syntax for Twitter's Advanced Search
general_search = '"Vaccine" OR "vaccine" OR "vaccination" OR "Vaccine" OR "Vaccination" OR "#Vaccine" OR "Pfizer" OR ' \
         '"Astrazeneca" OR "AstraZeneca" OR "BioNTech" OR "Moderna" lang:en -filter:retweets'
max_tweets_per_month = 2000
dataset = []
dataset_not_initiated = True


for i in states_coordinates:
    search_geo = add_geocode(general_search, i, states_coordinates)
    for j in range(0, len(dates) - 1):
        search_geo_date = add_dates(search_geo, dates[j], dates[j + 1])
        temp_dataset = scrape_tweets(search_geo_date, max_tweets_per_month, i, dates[j], dates[j + 1])
        print(len(temp_dataset))
        print(temp_dataset.head())
        if dataset_not_initiated:
            dataset = temp_dataset
            dataset_not_initiated = False
        else:
            dataset = join_datasets(temp_dataset, dataset)
    print(len(dataset))


dataset.to_csv('VaccineData.csv')
