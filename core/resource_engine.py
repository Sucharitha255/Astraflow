def recommend_resources(risk_score):

    recommendation = {}

    if risk_score >= 80:

        recommendation = {
            "traffic_police": 6,
            "diversion_routes": 3,
            "signal_adjustments": 2,
            "priority": "Critical"
        }

    elif risk_score >= 60:

        recommendation = {
            "traffic_police": 4,
            "diversion_routes": 2,
            "signal_adjustments": 1,
            "priority": "High"
        }

    elif risk_score >= 40:

        recommendation = {
            "traffic_police": 2,
            "diversion_routes": 1,
            "signal_adjustments": 1,
            "priority": "Medium"
        }

    else:

        recommendation = {
            "traffic_police": 1,
            "diversion_routes": 0,
            "signal_adjustments": 0,
            "priority": "Low"
        }

    return recommendation