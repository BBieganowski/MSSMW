import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import fetch
from matplotlib.ticker import PercentFormatter

def plot_last_week():
    SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD = fetch.get_lw_data()

    days = ["PW Close", "Monday", "Tuesday", "Wednesday","Thursday", "Friday"]
    x_axis = [0, 1, 2, 3, 4, 5]
    plt.xticks(x_axis, days)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, SP500, label = "SP500", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, DJIA, label = "DJIA", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, NASDAQ, label = "NASDAQ", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, EURUSD, label = "EURUSD", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, OIL, label = "OIL", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, GOLD, label = "GOLD", linewidth = 5)


    plt.legend()
    plt.show()

def plot_historical_week(week):
    dataset = pd.read_csv("/home/bartek/Desktop/MSSMW/data/complete_dataset.csv")
    SP500 = [0]
    DJIA = [0]
    NASDAQ = [0]
    EURUSD = [0]
    OIL = [0]
    GOLD = [0]

    for i in [2, 8, 14, 20, 26]:
        SP500.append(dataset.iloc[week, i])
        DJIA.append(dataset.iloc[week, i+1])
        NASDAQ.append(dataset.iloc[week, i+2])
        EURUSD.append(dataset.iloc[week, i+3])
        OIL.append(dataset.iloc[week, i+4])
        GOLD.append(dataset.iloc[week, i+5])

    days = ["PW Close", "Monday", "Tuesday", "Wednesday","Thursday", "Friday"]
    x_axis = [0, 1, 2, 3, 4, 5]
    plt.xticks(x_axis, days)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, SP500, label = "SP500", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, DJIA, label = "DJIA", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, NASDAQ, label = "NASDAQ", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, EURUSD, label = "EURUSD", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, OIL, label = "OIL", linewidth = 5)

    plt.rcParams["figure.figsize"] = (20,10)
    plt.plot(x_axis, GOLD, label = "GOLD", linewidth = 5)


    plt.legend()
    plt.show()
        