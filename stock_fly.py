import os
import sys
import requests
import yfinance as yf
import pandas as pd
import numpy as np

if not os.path.exists(".yfinance-installed"):
    print("Installing yfinance...")
    os.system("pip install yfinance")
    open(".yfinance-installed", "w").close()

tickers = ["DOCN", "U", "TSLA", "AMZN"]
purchase_price = [None, None, None, None]

data = pd.DataFrame()

data["Purchase Price"] = purchase_price
data["Current Price"] = np.empty(len(tickers))
data["% Change"] = np.empty(len(tickers))

for ticker, purchase_price in zip(tickers, purchase_price):
    stock = yf.Ticker(ticker)
    stock_info = stock.info

    current_price = stock_info["regularMarketPrice"]
    if purchase_price is None:
        percent_change = 0
else:
        percent_change = (current_price - purchase_price) / purchase_price

        data.loc[data["Current Price"] == "", "Current Price"] = current_price
        data.loc[data["Purchase Price"] == "", "Purchase Price"] = purchase_price
        data.loc[data["% Change"] == "", "% Change"] = percent_change

print(data)
