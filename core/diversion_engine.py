def recommend_diversion(

    zone,

    corridor,

    risk_score,

    requires_road_closure

):

    if requires_road_closure and risk_score >= 70:

        return {

            "diversion_required": True,

            "strategy": f"Activate alternate roads near {corridor}"

        }

    return {

        "diversion_required": False,

        "strategy": "Monitor traffic"

    }