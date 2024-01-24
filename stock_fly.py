import yfinance as yf
import builtins
import pandas as pd
import webbrowser

def stock_fly(tickers, purchase_prices):
    
data = yf.download(tickers=tickers, period="1y", interval="1d")

    
change = (data["Close"] - purchase_prices)/purchase_prices

    
for ticker, price, change_percent in zip(data["ticker"], data["Close"], change):
        print(f"{ticker}: Price: ${price:,.2f} | Percent Change: {change_percent:.2%}")


tickers = input("Enter the ticker symbols you want to include (separated by spaces): ").split()
purchase_prices = []
for ticker in tickers:
    purchase_prices.append(float(input(f"Enter the purchase price for {ticker}: ")))


stock_fly(tickers, purchase_prices)


data.to_csv("stock_data.csv")


webbrowser.open("https://files.pythonanywhere.com/files/AnyKnown/stock_data.csv", new=2)
