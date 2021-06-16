import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date

def get_lw_data():
    SP500   = yf.download(tickers='^GSPC', period='6d', interval='1d')['Adj Close']
    DJIA    = yf.download(tickers='^DJI', period='6d', interval='1d')['Adj Close']
    NASDAQ  = yf.download(tickers='^IXIC', period='6d', interval='1d')['Adj Close']
    EURUSD  = yf.download(tickers='EURUSD=X', period='6d', interval='1d')['Adj Close']
    OIL     = yf.download(tickers='CL=F', period='8d', interval='1d').iloc[:-1,:]['Adj Close']
    GOLD    = yf.download(tickers='GC=F', period='8d', interval='1d').iloc[:-1,:]['Adj Close']

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