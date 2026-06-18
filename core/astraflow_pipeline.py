from fastapi.encoders import jsonable_encoder

import math

from core.impact_engine import calculate_impact

from core.risk_engine import calculate_risk_score

from core.similarity_engine import get_similar_events

from core.decision_engine import get_decisions


def clean_nan(obj):

    if isinstance(

        obj,

        dict

    ):

        return {

            k: clean_nan(v)

            for k, v in obj.items()

        }

    elif isinstance(

        obj,

        list

    ):

        return [

            clean_nan(v)

            for v in obj

        ]

    elif isinstance(

        obj,

        float

    ):

        if math.isnan(

            obj

        ):

            return None

        return obj

    return obj


def run_astraflow(event):

    event = event.copy()

    # Impact

    impact = calculate_impact(

        event

    )

    event["impact_score"] = impact[

        "impact_score"

    ]

    event["impact_level"] = impact[

        "impact_level"

    ]

    # Risk

    risk_score = calculate_risk_score(

        event

    )

    event["risk_score"] = risk_score

    # Similar Events

    similar_events = get_similar_events(

        event

    )

    # Recommendations

    recommendations = get_decisions(

        event

    )

    response = {

        "impact": impact,

        "risk_score": risk_score,

        "similar_events": similar_events,

        "recommendations": recommendations

    }

    response = clean_nan(

        response

    )

    return jsonable_encoder(

        response

    )