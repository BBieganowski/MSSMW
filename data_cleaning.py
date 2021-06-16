from pandas.core.dtypes.missing import isna
from pandas.io.parsers import read_csv
import sklearn
import numpy as np
import pandas as pd
import os


// some data cleaning first

SP500 = pd.read_csv("/home/bartek/Desktop/MSSMW/data/S&P500.csv")
DJIA = pd.read_csv("/home/bartek/Desktop/MSSMW/data/DJIA.csv")
NASDAQ = pd.read_csv("/home/bartek/Desktop/MSSMW/data/NASDAQ.csv")
EURUSD = pd.read_csv("/home/bartek/Desktop/MSSMW/data/EURUSD.csv")
crudeoil = pd.read_csv("/home/bartek/Desktop/MSSMW/data/crudeoil.csv")
gold = pd.read_csv("/home/bartek/Desktop/MSSMW/data/gold.csv")
gold = gold.iloc[::-1].reset_index(drop = True)

data_list = [SP500, DJIA, NASDAQ, EURUSD, crudeoil, gold]

for i in data_list:
    i['Date'] = pd.to_datetime(i['Date'])
    i = i.set_index('Date')
 

total_data = pd.DataFrame({'Date':pd.date_range('1986-01-01', '2021-06-01')})
total_data = total_data.set_index('Date')


for i in data_list:
    total_data = total_data.merge(i, 'left', on = 'Date')


total_data.columns = ['Date', 'SP500', 'DJIA', 'NASDAQ', 'EURUSD', 'OIL_CRUDE', 'GOLD']
total_data = total_data.fillna(method='bfill')
total_data = total_data.drop_duplicates('Date')

total_data['weekday'] = total_data['Date'].dt.dayofweek

dictionary1 = {'Week_started':[],
    'Monday_SP500':[], 'Monday_DJIA':[], 'Monday_NASDAQ':[], 'Monday_EURUSD':[], 'Monday_OIL':[], 'Monday_GOLD':[],
    'Tuesday_SP500':[], 'Tuesday_DJIA':[], 'Tuesday_NASDAQ':[], 'Tuesday_EURUSD':[], 'Tuesday_OIL':[], 'Tuesday_GOLD':[],
    'Wednesay_SP500':[], 'Wednesay_DJIA':[], 'Wednesay_NASDAQ':[], 'Wednesay_EURUSD':[], 'Wednesay_OIL':[], 'Wednesay_GOLD':[],
    'Thursday_SP500':[], 'Thursday_DJIA':[], 'Thursday_NASDAQ':[], 'Thursday_EURUSD':[], 'Thursday_OIL':[], 'Thursday_GOLD':[],
    'Friday_SP500':[], 'Friday_DJIA':[], 'Friday_NASDAQ':[], 'Friday_EURUSD':[], 'Friday_OIL':[], 'Friday_GOLD':[]
}

for i in range(0, 1847):
    local_set = (total_data.iloc[(i*7)+3:(i*7)+11,:]).reset_index(drop = True)
    

    for i in local_set.columns[1:-1]:
        local_set[i+'_sinceFriClose'] = (local_set[i] / local_set[i][0] - 1)*100

    monday = local_set['Date'][3]
    vals = local_set.iloc[3:,8:].reset_index(drop = True).stack().values

    dictionary1['Week_started'].append(str(monday))
    for j, k in zip(vals, list(dictionary1.keys())[1:]):
        dictionary1[k].append(j)


complete_dataset = pd.DataFrame(dictionary1)
print(complete_dataset)

complete_dataset.to_csv("/home/bartek/Desktop/MSSMW/data/complete_dataset.csv")
