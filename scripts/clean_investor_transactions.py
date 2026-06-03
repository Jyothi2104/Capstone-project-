import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Amount must be positive
df = df[df["amount_inr"] > 0]

# Validate KYC status
valid_kyc = ["Verified", "Pending", "Rejected"]
invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("Invalid KYC Records:", len(invalid_kyc))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())
print("Minimum Amount:", df["amount_inr"].min())