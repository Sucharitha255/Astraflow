from pathlib import Path
from core.risk_engine import generate_risk_scores
from preprocessing.clean_data import (
    load_data,
    clean_data
)

from preprocessing.feature_engineering import (
    engineer_features
)

from config.settings import (
    PROCESSED_DATA_PATH
)


def build_dataset():

    df = load_data()

    df = clean_data(df)

    df = engineer_features(df)

    df = generate_risk_scores(df)

    Path(PROCESSED_DATA_PATH).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print("Dataset created successfully")

    print(df.shape)

    return df


if __name__ == "__main__":

    build_dataset()