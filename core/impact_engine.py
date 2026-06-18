def calculate_impact(event):

    score = 0

    # Priority

    if str(event["priority"]).lower() == "high":
        score += 30

    # Road closure

    if bool(event["requires_road_closure"]):
        score += 30

    # Event cause

    cause = str(event["event_cause"]).lower()

    cause_weights = {
        "vehicle_breakdown": 20,
        "construction": 25,
        "public_event": 25,
        "accident": 20
    }

    score += cause_weights.get(cause, 0)

    # Historical frequency

    score += min(
        int(event["historical_frequency"]),
        15
    )

    # Planned vs unplanned

    if str(event["event_type"]).lower() == "unplanned":
        score += 10

    # Convert score to impact level

    if score <= 30:
        impact_level = "Low"

    elif score <= 60:
        impact_level = "Medium"

    elif score <= 80:
        impact_level = "High"

    else:
        impact_level = "Severe"

    return {
        "impact_score": score,
        "impact_level": impact_level
    }