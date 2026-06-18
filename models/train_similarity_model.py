import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

from config.settings import PROCESSED_DATA_PATH


# Load dataset

df = pd.read_csv(
    PROCESSED_DATA_PATH
)


features = [

    "event_type",

    "event_cause",

    "priority",

    "zone",

    "hour",

    "historical_frequency",

    "requires_road_closure"

]


# Remove missing values

df = df.dropna(
    subset=features
)


# Encode categorical columns

categorical_cols = [

    "event_type",

    "event_cause",

    "priority",

    "zone"

]


encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(

        df[col].astype(str)

    )

    encoders[col] = encoder


# Convert road closure safely

df["requires_road_closure"] = (

    df["requires_road_closure"]

    .astype(str)

    .str.lower()

    .isin(

        ["true", "yes", "1"]

    )

    .astype(int)

)


X = df[features]


model = NearestNeighbors(

    n_neighbors=3,

    metric="euclidean"

)


model.fit(X)


joblib.dump(

    model,

    "models/similarity_model.pkl"

)


joblib.dump(

    encoders,

    "models/similarity_encoders.pkl"

)


# Save processed data too

joblib.dump(

    df,

    "models/similarity_dataset.pkl"

)


print(

    "Similarity model saved successfully"

)