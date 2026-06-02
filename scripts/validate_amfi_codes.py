import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Total fund_master codes:", len(fund_codes))
print("Total nav_history codes:", len(nav_codes))
print("Missing codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in nav_history.")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)