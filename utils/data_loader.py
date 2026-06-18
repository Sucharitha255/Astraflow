import pandas as pd

from config.settings import PROCESSED_DATA_PATH


def get_processed_data():

    df = pd.read_csv(PROCESSED_DATA_PATH)

    return df