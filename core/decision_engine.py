from core.resource_engine import recommend_resources

from core.barricade_engine import recommend_barricades

from core.diversion_engine import recommend_diversion


def get_decisions(event):

    risk_score = event["risk_score"]

    resources = recommend_resources(

        risk_score

    )

    barricades = recommend_barricades(

        risk_score,

        event["historical_frequency"],

        event["requires_road_closure"]

    )

    diversion = recommend_diversion(

    zone=event["zone"],

    corridor=event.get(

        "corridor",

        "Unknown"

    ),

    risk_score=risk_score,

    requires_road_closure=event[

        "requires_road_closure"

    ]

)

    return {

        "resources": resources,

        "barricades": barricades,

        "diversion": diversion

    }