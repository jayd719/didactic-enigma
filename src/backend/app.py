import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


class StockDataModel:
    """Handles data fetching and processing."""

    def __init__(self, ticker, interval):
        self.ticker = ticker
        self.interval = interval
        self.data = None

    def download_data(self, start_date, end_date):
        try:
            self.data = yf.download(
                self.ticker, start=start_date, end=end_date, interval=self.interval
            )
            if self.data.empty:
                print("No data found for the given parameters.")
        except Exception as e:
            print(f"Error fetching data: {e}")

    def get_volume_data(self):
        return self.data[["Volume"]]

    def get_price_stats(self):
        self.data["Mean Price"] = self.data[["Open", "High", "Low", "Close"]].mean(
            axis=1
        )
        return self.data[["Close", "Mean Price"]]

    def get_violin_data(self):
        return self.data[["Close", "Open", "Low", "High"]]


class StockDataView:
    """Handles visualization of data."""

    @staticmethod
    def plot_volume(data, ticker):
        data.plot(kind="line", figsize=(10, 5), title=f"{ticker} Volume Analysis")
        plt.xlabel("Time")
        plt.ylabel("Volume")
        plt.show()

    @staticmethod
    def plot_price_analysis(data, ticker):
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data["Close"], label="Close Price", color="blue")
        plt.plot(
            data.index,
            data["Mean Price"],
            label="Mean Price",
            linestyle="dashed",
            color="red",
        )
        plt.title(f"{ticker} Price Analysis")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

    @staticmethod
    def plot_violin(data, ticker):
        plt.figure(figsize=(8, 6))
        plt.violinplot([data[col] for col in data.columns], showmeans=True)
        plt.xticks(range(1, len(data.columns) + 1), data.columns)
        plt.title(f"{ticker} Violin Plot")
        plt.xlabel("Price Type")
        plt.ylabel("Price")
        plt.show()


class StockController:
    """Handles user interaction and connects model and view."""

    def __init__(self, ticker, start_date, end_date, interval):
        self.model = StockDataModel(ticker, interval)
        self.view = StockDataView()
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        self.model.download_data(self.start_date, self.end_date)
        if self.model.data is not None and not self.model.data.empty:
            while True:
                print("\nSelect an option:")
                print("1. Volume Analysis")
                print("2. Price Analysis")
                print("3. Violin Plot")
                print("4. Exit")
                choice = input("Enter choice: ")
                if choice == "1":
                    self.view.plot_volume(
                        self.model.get_volume_data(), self.model.ticker
                    )
                elif choice == "2":
                    self.view.plot_price_analysis(
                        self.model.get_price_stats(), self.model.ticker
                    )
                elif choice == "3":
                    self.view.plot_violin(
                        self.model.get_violin_data(), self.model.ticker
                    )
                elif choice == "4":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice, try again.")


if __name__ == "__main__":
    ticker = "AAPL"  # Corrected ticker symbol
    start_date = "2024-01-01"  # Adjusted start date
    end_date = "2024-10-10"  # Adjusted end date
    interval = "1d"  # Adjusted interval
    controller = StockController(ticker, start_date, end_date, interval)
    controller.run()
