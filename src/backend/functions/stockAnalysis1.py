import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define stock symbols (you can modify this list to include more dividend stocks)
stocks = ["PG", "JNJ", "PEP", "KO", "MCD", "MSFT", "V"]

# Set filtering criteria
MIN_DIVIDEND_YIELD = 2.0  # Minimum dividend yield (%)
MAX_PAYOUT_RATIO = 60.0  # Maximum payout ratio (%)
MIN_DIVIDEND_GROWTH = 5.0  # Minimum 5-year dividend growth rate (%)


# Function to fetch stock data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    print(info)


# Retrieve data for all stocks
df = pd.DataFrame([get_stock_data(stock) for stock in stocks])

# Filter stocks based on criteria
df_filtered = df[
    (df["Dividend Yield (%)"] >= MIN_DIVIDEND_YIELD)
    & (df["Payout Ratio (%)"] <= MAX_PAYOUT_RATIO)
    & (df["Dividend Growth 5Y (%)"] >= MIN_DIVIDEND_GROWTH)
]

# Rank stocks based on Dividend Yield and Dividend Growth
df_filtered["Score"] = (
    df_filtered["Dividend Yield (%)"] + df_filtered["Dividend Growth 5Y (%)"]
)
df_filtered = df_filtered.sort_values(by="Score", ascending=False)


# Visualization: Dividend Yield vs Dividend Growth
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df_filtered["Dividend Growth 5Y (%)"],
    y=df_filtered["Dividend Yield (%)"],
    size=df_filtered["Market Cap (B)"],
    sizes=(20, 400),
    hue=df_filtered["Stock"],
    palette="viridis",
    alpha=0.8,
)
plt.xlabel("Dividend Growth 5Y (%)")
plt.ylabel("Dividend Yield (%)")
plt.title("Dividend Yield vs Dividend Growth")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid()
plt.show()
