import pandas as pd
import numpy as np

# sample stock price data
df = pd.DataFrame({
    "date": pd.to_datetime([
        "2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02",
        "2026-02-01", "2026-02-01"
    ]),
    "stock_name": ["A", "B", "A", "B", "A", "B"],
    "open_price": [100, 200, 105, 195, 110, 210],
    "close_price": [105, 190, 110, 205, 120, 200]
})

# calculate percentage daily return
df["daily_return"] = (
    (df["close_price"] - df["open_price"]) / df["open_price"]
) * 100

# extract month from date
df["month"] = df["date"].dt.to_period("M")

# calculate monthly return per stock
monthly_return = (
    df.groupby(["month", "stock_name"])["daily_return"]
      .sum()
      .reset_index()
)

# top gaining stock per month
top_gainers = monthly_return.loc[
    monthly_return.groupby("month")["daily_return"].idxmax()
]

# top losing stock per month
top_losers = monthly_return.loc[
    monthly_return.groupby("month")["daily_return"].idxmin()
]

# compute rolling volatility (7-day window)
df = df.sort_values(["stock_name", "date"])
df["rolling_volatility"] = (
    df.groupby("stock_name")["daily_return"]
      .rolling(7)
      .std()
      .reset_index(level=0, drop=True)
)

# print results
print("Daily Returns:")
print(df[["date", "stock_name", "daily_return"]])

print("\nTop Gaining Stocks per Month:")
print(top_gainers)

print("\nTop Losing Stocks per Month:")
print(top_losers)

print("\nRolling Volatility:")
print(df[["date", "stock_name", "rolling_volatility"]])
