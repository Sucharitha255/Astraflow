import pandas as pd

from config.settings import PROCESSED_DATA_PATH

df = pd.read_csv(PROCESSED_DATA_PATH)

print("Total rows:", len(df))

features = [

    "event_type",

    "event_cause",

    "priority",

    "zone",

    "junction",

    "requires_road_closure",

    "hour",

    "historical_frequency",

    "event_duration",

    "impact_level"

]

print("\nMissing values")

print(

    df[features]

    .isnull()

    .sum()

)