import pandas as pd


def extract_time_features(df):

    df["hour"] = df["start_datetime"].dt.hour

    df["weekday"] = df["start_datetime"].dt.day_name()

    df["is_weekend"] = df["weekday"].isin(
        ["Saturday", "Sunday"]
    )

    # Fill missing hour values

    df["hour"] = df["hour"].fillna(0)

    return df


def create_duration_features(df):

    # Event duration in minutes

    df["event_duration"] = (

        df["end_datetime"]

        -

        df["start_datetime"]

    ).dt.total_seconds() / 60

    # Resolution duration in minutes

    df["resolution_duration"] = (

        df["resolved_datetime"]

        -

        df["start_datetime"]

    ).dt.total_seconds() / 60

    # Remove negative values

    df["event_duration"] = (

        df["event_duration"]

        .clip(lower=0)

    )

    df["resolution_duration"] = (

        df["resolution_duration"]

        .clip(lower=0)

    )

    # Fill missing durations

    df["event_duration"] = (

        df["event_duration"]

        .fillna(0)

    )

    df["resolution_duration"] = (

        df["resolution_duration"]

        .fillna(0)

    )

    return df


def create_location_features(df):

    # Fill missing values first

    df["zone"] = (

        df["zone"]

        .fillna("Unknown Zone")

    )

    df["junction"] = (

        df["junction"]

        .fillna("Unknown Junction")

    )

    df["location_id"] = (

        df["zone"]

        .astype(str)

        +

        "_"

        +

        df["junction"]

        .astype(str)

    )

    return df


def create_frequency_features(df):

    location_counts = (

        df["location_id"]

        .value_counts()

    )

    df["historical_frequency"] = (

        df["location_id"]

        .map(location_counts)

    )

    # Fill missing frequencies

    df["historical_frequency"] = (

        df["historical_frequency"]

        .fillna(1)

    )

    return df


def engineer_features(df):

    # Fill priority

    df["priority"] = (

        df["priority"]

        .fillna("Low")

    )

    df = extract_time_features(df)

    df = create_duration_features(df)

    df = create_location_features(df)

    df = create_frequency_features(df)

    return df