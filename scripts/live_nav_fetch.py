import requests
import pandas as pd
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            file_path = f"data/raw/{scheme_name}_NAV.csv"

            nav_df.to_csv(file_path, index=False)

            print(f"Saved: {file_path} ({len(nav_df)} records)")

        else:
            print(f"Failed: {scheme_name}")

    except Exception as e:
        print(f"Error for {scheme_name}: {e}")