import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date, datetime, timedelta

def get_last_workweek():
    x = datetime.today().weekday()
    today = datetime.today().date()
    print(today)

    if x == 0:
        x = today - timedelta(days = 3)
    elif x == 1:
        x = today - timedelta(days = 4)
    elif x == 1:
        x = today - timedelta(days = 5)
    elif x == 1:
        x = today - timedelta(days = 6)
    elif x == 1:
         x = today - timedelta(days = 7)
    elif x == 1:
        x = today - timedelta(days = 1)
    elif x == 1:
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

    return SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD


def pack_week(SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD):
    values = []
    for i in range(1, 6):
        values.append(SP500[i])
        values.append(DJIA[i])
        values.append(NASDAQ[i])
        values.append(EURUSD[i])
        values.append(OIL[i])
        values.append(GOLD[i])

    return np.array(values)