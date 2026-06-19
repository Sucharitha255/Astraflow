from fastapi import APIRouter

import pandas as pd

from config.settings import PROCESSED_DATA_PATH


router = APIRouter(

    prefix="/api",

    tags=["Analytics"]

)


@router.get("/analytics")

def get_analytics():

    df = pd.read_csv(

        PROCESSED_DATA_PATH

    )


    total_events = len(df)


    high_risk = len(

        df[df["risk_score"] >= 70]

    )


    zones_covered = df["zone"].nunique()


    ai_modules = 6


    event_causes = (

        df["event_cause"]

        .value_counts()

        .head(5)

        .reset_index()

    )

    event_causes.columns = [

        "cause",

        "count"

    ]


    zone_events = (

        df["zone"]

        .value_counts()

        .head(5)

        .reset_index()

    )

    zone_events.columns = [

        "zone",

        "count"

    ]


    risk_distribution = [

        {

            "name":"Low",

            "value":len(

                df[df["risk_score"] < 40]

            )

        },

        {

            "name":"Medium",

            "value":len(

                df[

                    (df["risk_score"] >= 40)

                    &

                    (df["risk_score"] < 70)

                ]

            )

        },

        {

            "name":"High",

            "value":len(

                df[df["risk_score"] >= 70]

            )

        }

    ]


    return {

        "total_events": total_events,

        "high_risk": high_risk,

        "zones_covered": zones_covered,

        "ai_modules": ai_modules,

        "event_causes": event_causes.to_dict(

            orient="records"

        ),

        "zone_events": zone_events.to_dict(

            orient="records"

        ),

        "risk_distribution": risk_distribution

    }