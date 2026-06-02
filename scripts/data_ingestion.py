from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

csv_files = raw_path.glob("*.csv")

for file in csv_files:
    print("\n" + "=" * 60)
    print(f"Dataset: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")