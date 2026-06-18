import pandas as pd

from config.settings import PROCESSED_DATA_PATH

df = pd.read_csv(PROCESSED_DATA_PATH)


def get_congestion_level(duration):

    if duration <= 30:
        return "Low"

    elif duration <= 60:
        return "Medium"

    elif duration <= 120:
        return "High"

    return "Critical"


df["congestion_level"] = df[
    "resolution_duration"
].apply(
    get_congestion_level
)

df.to_csv(
    PROCESSED_DATA_PATH,
    index=False
)

print(
    df["congestion_level"]
    .value_counts()
)