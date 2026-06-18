def recommend_barricades(

    risk_score,

    historical_frequency,

    requires_road_closure

):

    barricades = 1

    if risk_score >= 80:

        barricades += 3

    elif risk_score >= 60:

        barricades += 2

    if historical_frequency >= 10:

        barricades += 1

    if requires_road_closure:

        barricades += 2

    return barricades