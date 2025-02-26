import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Task 1A: Function to download stock data
def data_download(ticker, start_date, interval):
    data = yf.download(ticker, start=start_date, interval=interval)
    return data


# Task 1B: Test the function with two tickers, dates, and intervals
tickers = ["AAPL", "GOOG"]
dates = ["2024-02-01", "2024-02-15"]
intervals = ["1m", "5m"]

for ticker in tickers:
    for interval in intervals:
        stock_data = data_download(ticker, dates[0], interval)
        print(f"First 5 rows of {ticker} at {interval} interval:")
        print(stock_data.head())


# Task 2A: Function to visualize volume data
def volume_analysis(data, ticker, date, interval):
    plt.figure(figsize=(10, 5))
    plt.bar(data.index, data["Volume"], color="blue")
    plt.xlabel("Time")
    plt.ylabel("Volume")
    plt.title(f"Volume Analysis for {ticker} on {date} ({interval})")
    plt.xticks(rotation=45)
    plt.show()


# Task 2B: Test the volume analysis function
for ticker in tickers:
    for interval in intervals:
        stock_data = data_download(ticker, dates[0], interval)
        volume_analysis(stock_data, ticker, dates[0], interval)


# Task 3A: Function for price analysis
def price_analysis(data, ticker, date, interval):
    data["Mean Price"] = data[["Open", "High", "Low", "Close"]].mean(axis=1)
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["Mean Price"], label="Mean Price", color="red")
    plt.plot(data.index, data["Close"], label="Close Price", color="blue")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title(f"Price Analysis for {ticker} on {date} ({interval})")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()


# Task 3B: Test the price analysis function
for ticker in tickers:
    for interval in intervals:
        stock_data = data_download(ticker, dates[0], interval)
        price_analysis(stock_data, ticker, dates[0], interval)


# Task 4A: Function for violin plots
def violin_plots(data, ticker, date, interval):
    plt.figure(figsize=(10, 5))
    plt.violinplot(
        [data["Close"], data["Open"], data["Low"], data["High"]], showmeans=True
    )
    plt.xticks([1, 2, 3, 4], ["Close", "Open", "Low", "High"])
    plt.ylabel("Price")
    plt.title(f"Violin Plot for {ticker} on {date} ({interval})")
    plt.show()


# Task 4B: Test the violin plot function
for ticker in tickers:
    for interval in intervals:
        stock_data = data_download(ticker, dates[0], interval)
        violin_plots(stock_data, ticker, dates[0], interval)
