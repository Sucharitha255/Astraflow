from fastapi import APIRouter

import pandas as pd

from config.settings import PROCESSED_DATA_PATH

from core.risk_engine import generate_risk_scores

#router = APIRouter()
router = APIRouter(
    prefix="/api",
    tags=["Risk"]
)
@router.get("/risk")
def get_risk_scores():

    df = pd.read_csv(PROCESSED_DATA_PATH)

    df = generate_risk_scores(df)

    return df[
        [
            "event_type",
            "event_cause",
            "risk_score"
        ]
    ].head(10).to_dict(
        orient="records"
    )