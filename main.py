import numpy as np
import pandas as pd 
import fetch
from sklearn.neighbors import NearestNeighbors
from joblib import load
import plotter


if __name__ == '__main__':

    NN = load("NN.joblib")

    SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD = fetch.get_lw_data()

    x = fetch.pack_week(SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD)

    dist, indices = NN.kneighbors([x])
    dist, indices = dist[0][0], indices[0][0]

    dataset = pd.read_csv("/home/bartek/Desktop/MSSMW/data/complete_dataset.csv")
    print(dataset)

    plotter.plot_last_week()
    plotter.plot_historical_week(indices)