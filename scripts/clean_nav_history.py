import pandas as pd

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by scheme and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV > 0
df = df[df["nav"] > 0]

# Forward fill NAV within each scheme
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Save cleaned file
df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing NAV:", df["nav"].isna().sum())
print("Duplicates:", df.duplicated().sum())
print("Minimum NAV:", df["nav"].min())