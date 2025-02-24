from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt

# 🔑 Replace with your actual Alpha Vantage API key
API_KEY = "T5QOTQM76WKT8EYF"

# Initialize Alpha Vantage API
ts = TimeSeries(key=API_KEY, output_format="pandas")

# Fetch daily data for S&P 500
df, meta_data = ts.get_daily(symbol="SPY", outputsize="full")

# Convert index to datetime format
df.index = pd.to_datetime(df.index)

# Keep only the last 2 years
df = df[df.index >= "2022-02-24"]

# Rename columns for clarity
df.columns = ["Open", "High", "Low", "Close", "Volume"]

# Save data as CSV (optional)
df.to_csv("sp500_data.csv")

# Plot closing prices
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Close"], label="S&P 500 Closing Price", color="blue")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("S&P 500 Closing Prices (Last 2 Years)")
plt.legend()
plt.grid()
plt.show()

# Print first 5 rows
print(df.head())
