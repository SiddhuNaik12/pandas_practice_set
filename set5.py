import pandas as pd
import numpy as np

# sample transaction data
df = pd.DataFrame({
    "account_id": [101, 101, 102, 103, 101, 102, 104, 103],
    "transaction_date": pd.to_datetime([
        "2026-01-01", "2026-01-01", "2026-01-01", "2026-01-02",
        "2026-01-02", "2026-01-02", "2026-01-02", "2026-01-03"
    ]),
    "amount": [500, 7000, 300, 9000, 200, 4000, 15000, 8000],
    "transaction_type": ["credit", "debit", "credit", "credit",
                         "debit", "debit", "credit", "debit"]
})

# aggregate daily transaction totals per account
daily_total = (
    df.groupby(["account_id", "transaction_date"])["amount"]
      .sum()
      .reset_index()
)

# calculate total transaction volume per account
account_volume = df.groupby("account_id")["amount"].sum()

# find unusually high transaction volume
volume_threshold = account_volume.mean() + 2 * account_volume.std()
high_volume_accounts = account_volume[
    account_volume > volume_threshold
].index

# detect potential fraud using statistical threshold on single transactions
amount_threshold = df["amount"].mean() + 3 * df["amount"].std()
potential_fraud = df[df["amount"] > amount_threshold]
# print results
print("Daily transaction totals per account:")
print(daily_total)
print("\nAccounts with unusually high transaction volume:")
print(list(high_volume_accounts))
print("\nPotential fraudulent transactions:")
print(potential_fraud)
