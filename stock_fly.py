import yahoo_fin
import pandas as pd
import sys


tickers = ["NFLX", "U", "TSLA", "DOCN"]


purchase_prices = sys.argv[1:]


purchase_prices = [float(price) for price in purchase_prices]


data = pd.DataFrame()


data["Purchase Price"] = []
data["Current Price"] = []
data["% Change"] = []


for index, ticker in enumerate(tickers):
  
if index < len(purchase_prices):
        data.loc[index, "Purchase Price"] = purchase_prices[index]
    else:
        data.loc[index, "Purchase Price"] = 0

for ticker in tickers:
    stock = yahoo_fin.StockInfo(ticker)
    current_price = stock.current_price
    data.loc[data["Current Price"] == "", "Current Price"] = current_price

for index, row in data.iterrows():
    current_price = data.loc[index, "Current Price"]
    if row["Purchase Price"] != 0:
        percent_change = (current_price - row["Purchase Price"]) / row["Purchase Price"]
    else:
        percent_change = 0
data.loc[index, "% Change"] = percent_change

print(data)
