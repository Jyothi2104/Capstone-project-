import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table}",
        engine
    )

    print(table, ":", count.iloc[0]["cnt"])