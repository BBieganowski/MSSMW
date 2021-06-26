import pandas as pd

dataset = pd.read_csv('data/headlines/FINAL_0_1.csv').drop(['Unnamed: 0'], axis = 1)
dataset['date'] = pd.to_datetime(dataset['date'])

def get_headlines(date):
    date = pd.to_datetime(date)
    wkd = date.weekday()
    week_start = date - pd.Timedelta(days = wkd)
    week_end = week_start + pd.Timedelta(days = 7)
    return dataset[(dataset['date'] > week_start) & (dataset['date'] < week_end)].sort_values('words_in_headline', ascending=False)


print(get_headlines('2001-09-11'))