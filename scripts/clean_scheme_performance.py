import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

# Convert to numeric
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for non-numeric values
print("Missing Numeric Values:")
print(df[return_cols].isna().sum().sum())

# Expense ratio validation
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies:", len(anomalies))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())