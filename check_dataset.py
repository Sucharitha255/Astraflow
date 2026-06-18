import pandas as pd

from config.settings import PROCESSED_DATA_PATH

df = pd.read_csv(PROCESSED_DATA_PATH)

cols = [

    "event_type",

    "event_cause",

    "priority",

    "zone",

    "junction",

    "requires_road_closure"

]

for col in cols:

    print("\n====================")

    print(col)

    print("====================")

    print(df[col].value_counts().head(10))