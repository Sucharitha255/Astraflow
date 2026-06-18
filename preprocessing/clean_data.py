import pandas as pd

from config.settings import RAW_DATA_PATH


def load_data():

    df = pd.read_csv(RAW_DATA_PATH)

    return df


def clean_data(df):

    # remove duplicates

    df = df.drop_duplicates()

    # clean column names

    df.columns = df.columns.str.strip()

    # datetime columns

    datetime_cols = [

        "start_datetime",

        "end_datetime",

        "modified_datetime",

        "created_date",

        "closed_datetime",

        "resolved_datetime"

    ]

    for col in datetime_cols:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    return df


if __name__ == "__main__":

    df = load_data()

    df = clean_data(df)

    print(df.head())

    print(df.shape)