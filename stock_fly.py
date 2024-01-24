import yahoo_fin
import pandas as pd
import sys

tickers = ["NFLX", "U", "TSLA", "DOCN"]

purchase_prices = sys.argv[1:]

data = pd.DataFrame()

data["Purchase Price"] = []
data["Current Price"] = []
data["% Change"] = []

for index, ticker in enumerate(tickers):
    data.loc[index, "Purchase Price"] = float(purchase_prices[index])

for ticker in tickers:
    stock = yahoo_fin.StockInfo(ticker)
    current_price = stock.current_price
    data.loc[data["Current Price"] == "", "Current Price"] = current_price

for index, row in data.iterrows():
    current_price = data.loc[index, "Current Price"]
    percent_change = (current_price - row["Purchase Price"]) / row["Purchase Price"]
    data.loc[index, "% Change"] = percent_change

print(data)
