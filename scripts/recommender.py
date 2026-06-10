import pandas as pd

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

perf = pd.read_csv(
    BASE_DIR / "data" / "processed" / "07_scheme_performance_cleaned.csv"
)

def recommend_funds(risk_appetite):

    temp = perf[
        perf["risk_grade"].str.lower()
        == risk_appetite.lower()
    ]

    rec = (
        temp.sort_values(
            "sharpe_ratio",
            ascending=False
        )
        [
            [
                "scheme_name",
                "category",
                "sharpe_ratio",
                "risk_grade"
            ]
        ]
        .head(3)
    )

    return rec

print(
    recommend_funds("Moderate")
)