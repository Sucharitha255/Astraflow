import pandas as pd


def calculate_risk_score(row):

    score = 0

    # Event type weight

    high_risk_events = [

        "construction",

        "public_event",

        "accident"

    ]

    if str(row["event_cause"]).lower() in high_risk_events:

        score += 30

    else:

        score += 15

    # Priority weight

    priority = str(

        row["priority"]

    ).lower()

    if priority == "high":

        score += 25

    elif priority == "medium":

        score += 15

    else:

        score += 5

    # Road closure weight

    road_closure = str(

        row["requires_road_closure"]

    ).lower()

    if road_closure in [

        "yes",

        "true",

        "1"

    ]:

        score += 20

    # Historical frequency weight

    historical_frequency = min(

        row["historical_frequency"],

        20

    )

    score += historical_frequency

    return min(score, 100)


def generate_risk_scores(df):

    df["risk_score"] = (

        df.apply(

            calculate_risk_score,

            axis=1

        )

    )

    return df