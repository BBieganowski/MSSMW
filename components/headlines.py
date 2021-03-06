import pandas as pd
from newsapi import NewsApiClient
from pandas.io.json import json_normalize
import pandas as pd

dataset = pd.read_csv('data/headlines/FINAL_0_1.csv').drop(['Unnamed: 0'], axis = 1)
dataset['date'] = pd.to_datetime(dataset['date'])

def get_headlines(date):
    date = pd.to_datetime(date)
    wkd = date.weekday()
    week_start = date - pd.Timedelta(days = wkd)
    week_end = week_start + pd.Timedelta(days = 7)
    return dataset[(dataset['date'] > week_start) & (dataset['date'] < week_end)].sort_values('words_in_headline', ascending=False)


def get_modern_headlines():
    newsapi = NewsApiClient(api_key='ba102aa0d6874e328f96876e78cfb57a')
    country='us'
    category='business'       
    top_headlines =newsapi.get_top_headlines(category=category,
    language='en',country=country, page_size=100)     
    top_headlines=json_normalize(top_headlines['articles'])
    newdf=top_headlines[["title","url"]]    

    return newdf