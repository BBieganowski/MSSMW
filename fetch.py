import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date, datetime, timedelta
from sklearn.neighbors import NearestNeighbors
from joblib import dump, load


def get_last_workweek():
    x = datetime.today().weekday()
    today = datetime.today().date()

    if x == 0:
        x = today - timedelta(days = 3)
    elif x == 1:
        x = today - timedelta(days = 4)
    elif x == 2:
        x = today - timedelta(days = 5)
    elif x == 3:
        x = today - timedelta(days = 6)
    elif x == 4:
         x = today - timedelta(days = 7)
    elif x == 5:
        x = today - timedelta(days = 1)
    elif x == 6:
        x = today - timedelta(days = 2)

    l_fri = x - timedelta(days = 7)
    fri = x

    l_fri = pd.to_datetime(l_fri)
    fri = pd.to_datetime(fri)

    return(l_fri, fri)
        

def get_lw_data():

    last_workweek = get_last_workweek()

    SP500   = yf.download(tickers='^GSPC', period='14d', interval='1d')['Adj Close']
    DJIA    = yf.download(tickers='^DJI', period='14d', interval='1d')['Adj Close']
    NASDAQ  = yf.download(tickers='^IXIC', period='14d', interval='1d')['Adj Close']
    EURUSD  = yf.download(tickers='EURUSD=X', period='14d', interval='1d')['Adj Close']
    OIL     = yf.download(tickers='CL=F', period='14d', interval='1d').iloc[:-1,:]['Adj Close']
    GOLD    = yf.download(tickers='GC=F', period='14d', interval='1d').iloc[:-1,:]['Adj Close']

    SP500   = SP500[(SP500.index >= last_workweek[0]) & (SP500.index <= last_workweek[1])]
    DJIA   = DJIA[(DJIA.index >= last_workweek[0]) & (DJIA.index <= last_workweek[1])]
    NASDAQ   = NASDAQ[(NASDAQ.index >= last_workweek[0]) & (NASDAQ.index <= last_workweek[1])]
    EURUSD   = EURUSD[(EURUSD.index >= last_workweek[0]) & (EURUSD.index <= last_workweek[1])]
    OIL   = OIL[(OIL.index >= last_workweek[0]) & (OIL.index <= last_workweek[1])]
    GOLD   = GOLD[(GOLD.index >= last_workweek[0]) & (GOLD.index <= last_workweek[1])]
    

    SP500   = (SP500/SP500[0] - 1)*100
    DJIA    = (DJIA/DJIA[0] - 1)*100
    NASDAQ  = (NASDAQ/NASDAQ[0] - 1)*100
    EURUSD  = (EURUSD/EURUSD[0] - 1)*100
    OIL     = (OIL/OIL[0] - 1)*100
    GOLD    = (GOLD/GOLD[0] - 1)*100

    week_index = pd.date_range(last_workweek[0], last_workweek[1])
    
    SP500 = SP500.reindex(week_index).fillna(method = 'ffill')[3:]
    DJIA = DJIA.reindex(week_index).fillna(method = 'ffill')[3:]
    NASDAQ = NASDAQ.reindex(week_index).fillna(method = 'ffill')[3:]
    EURUSD = EURUSD.reindex(week_index).fillna(method = 'ffill')[3:]
    OIL = OIL.reindex(week_index).fillna(method = 'ffill')[3:]
    GOLD = GOLD.reindex(week_index).fillna(method = 'ffill')[3:]

    return SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD


def pack_week(SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD):
    values = []
    for i in range(0, 5):
        values.append(SP500[i])
        values.append(DJIA[i])
        values.append(NASDAQ[i])
        values.append(EURUSD[i])
        values.append(OIL[i])
        values.append(GOLD[i])

    return np.array(values)


def get_MSSMW():

    SP500_lw, DJIA_lw, NASDAQ_lw, EURUSD_lw, OIL_lw, GOLD_lw = get_lw_data()

    packed = pack_week(SP500_lw, DJIA_lw, NASDAQ_lw, EURUSD_lw, OIL_lw, GOLD_lw)
    model = load('NN.joblib')
    dist, indices = model.kneighbors([packed])
    datapoint = pd.read_csv("/home/bartek/Desktop/MSSMW/data/complete_dataset.csv").loc[indices[0]]
    date = datapoint['Week_started']

    sp500_his    = [datapoint.iloc[0, 2], datapoint.iloc[0, 8], datapoint.iloc[0, 14], datapoint.iloc[0, 20], datapoint.iloc[0, 26]]
    dija_his     = [datapoint.iloc[0, 3], datapoint.iloc[0, 9], datapoint.iloc[0, 15], datapoint.iloc[0, 21], datapoint.iloc[0, 27]]
    nasdaq_his   = [datapoint.iloc[0, 4], datapoint.iloc[0, 10], datapoint.iloc[0, 16], datapoint.iloc[0, 22], datapoint.iloc[0, 28]]
    eurusd_his    = [datapoint.iloc[0, 5], datapoint.iloc[0, 11], datapoint.iloc[0, 17], datapoint.iloc[0, 23], datapoint.iloc[0, 29]]
    oil_his       = [datapoint.iloc[0, 6], datapoint.iloc[0, 12], datapoint.iloc[0, 18], datapoint.iloc[0, 24], datapoint.iloc[0, 30]]
    gold_his      = [datapoint.iloc[0, 7], datapoint.iloc[0, 13], datapoint.iloc[0, 19], datapoint.iloc[0, 25], datapoint.iloc[0, 31]]

    SP500 = pd.DataFrame({"Last Week":SP500_lw, "Historical Week":sp500_his}).reset_index(drop = True)
    DJIA = pd.DataFrame({"Last Week":DJIA_lw, "Historical Week":dija_his}).reset_index(drop = True)
    NASDAQ = pd.DataFrame({"Last Week":NASDAQ_lw, "Historical Week":nasdaq_his}).reset_index(drop = True)
    EURUSD = pd.DataFrame({"Last Week":EURUSD_lw, "Historical Week":eurusd_his}).reset_index(drop = True)
    OIL = pd.DataFrame({"Last Week":OIL_lw, "Historical Week":oil_his}).reset_index(drop = True)
    GOLD = pd.DataFrame({"Last Week":GOLD_lw, "Historical Week":gold_his}).reset_index(drop = True)

    
    date = pd.to_datetime(date)+timedelta(days=3)

    return date, get_last_workweek()[1], SP500/100, DJIA/100, NASDAQ/100, EURUSD/100, OIL/100, GOLD/100

    