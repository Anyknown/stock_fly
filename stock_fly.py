import os
import sys


if not os.path.exists(".yfinance-installed"):
    print("Installing yfinance...")
    os.system("pip install yfinance")
    open(".yfinance-installed", "w").close()

import yfinance as yf
import pandas as pd


percent_change = 0

tickers = sys.argv[1:]


data = pd.DataFrame()


data["Purchase Price"] = []
data["Current Price"] = []
data["% Change"] = []


for ticker in tickers:
    stock = yf.Ticker(ticker)
    current_price = stock.price
    data.loc[data["Current Price"] == "", "Current Price"] = current_price


for index, row in data.iterrows():
    
if row["Purchase Price"] != 0:
        percent_change = (current_price - row["Purchase Price"]) / row["Purchase Price"]
    else:
        percent_change = 0

data.loc[index, "% Change"] = percent_change


print(data)
