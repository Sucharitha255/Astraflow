import joblib
import pandas as pd


model = joblib.load(
    "models/similarity_model.pkl"
)

encoders = joblib.load(
    "models/similarity_encoders.pkl"
)

dataset = joblib.load(
    "models/similarity_dataset.pkl"
)


FEATURES = [

    "event_type",

    "event_cause",

    "priority",

    "zone",

    "hour",

    "historical_frequency",

    "requires_road_closure"

]


def get_similar_events(event_data):

    event = event_data.copy()

    # Encode categorical values

    for col in [

        "event_type",

        "event_cause",

        "priority",

        "zone"

    ]:

        event[col] = encoders[col].transform(

            [str(event[col])]

        )[0]

    # Convert road closure

    event["requires_road_closure"] = int(

        str(

            event["requires_road_closure"]

        ).lower()

        in [

            "true",

            "yes",

            "1"

        ]

    )

    input_df = pd.DataFrame(

        [event]

    )[FEATURES]

    distances, indices = model.kneighbors(

        input_df

    )

    # Get matched rows

    similar_events = dataset.iloc[

        indices[0]

    ].copy()

    # Decode values

    for col in [

        "event_type",

        "event_cause",

        "priority",

        "zone"

    ]:

        similar_events[col] = (

            encoders[col]

            .inverse_transform(

                similar_events[col]

            )

        )

    # Select only useful columns

    columns = [

        "event_type",

        "event_cause",

        "zone",

        "junction",

        "corridor",

        "priority",

        "historical_frequency",

        "impact_level"

    ]

    similar_events = similar_events[

        columns

    ]

    # Remove NaN

    similar_events = similar_events.fillna(

        "Unknown"

    )

    return similar_events.to_dict(

        orient="records"

    )