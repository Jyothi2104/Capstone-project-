import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# -----------------------------
# Create DB Folder if Missing
# -----------------------------

db_dir = Path("data/db")
db_dir.mkdir(parents=True, exist_ok=True)

db_path = db_dir / "bluestock_mf.db"

# -----------------------------
# Create SQLite Connection
# -----------------------------

engine = create_engine(
    f"sqlite:///{db_path}"
)

print("Database Created:", db_path)

# -----------------------------
# Load Fund Master
# -----------------------------

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded:", len(fund_master))

# -----------------------------
# Load NAV History
# -----------------------------

nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded:", len(nav))

# -----------------------------
# Load Investor Transactions
# -----------------------------

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded:", len(transactions))

# -----------------------------
# Load Scheme Performance
# -----------------------------

performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded:", len(performance))

# -----------------------------
# Verify Row Counts
# -----------------------------

print("\nVerification:")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        engine
    )

    print(
        table,
        ":",
        count.iloc[0]["cnt"]
    )

print("\nAll datasets loaded successfully!")