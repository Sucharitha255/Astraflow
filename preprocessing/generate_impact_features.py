import pandas as pd

from config.settings import PROCESSED_DATA_PATH
from core.impact_engine import calculate_impact


df = pd.read_csv(PROCESSED_DATA_PATH)

results = df.apply(calculate_impact, axis=1)

df["impact_score"] = results.apply(
    lambda x: x["impact_score"]
)

df["impact_level"] = results.apply(
    lambda x: x["impact_level"]
)

df.to_csv(
    PROCESSED_DATA_PATH,
    index=False
)

print("Impact features generated.")