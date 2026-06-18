import pandas as pd

from core.risk_engine import (
    generate_risk_scores
)

df = pd.read_csv(
    "data/processed/processed_data.csv"
)

df = generate_risk_scores(df)

print(

    df[

        [

            "event_type",

            "event_cause",

            "priority",

            "risk_score"

        ]

    ].head()

)