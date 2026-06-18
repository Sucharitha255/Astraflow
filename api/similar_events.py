from fastapi import APIRouter

from core.similarity_engine import get_similar_events


router = APIRouter(

    prefix="/api",

    tags=["Similar Events"]

)


@router.get("/similar-events")

def similar_events():

    sample = {

        "event_type":"planned",

        "event_cause":"construction",

        "priority":"High",

        "zone":"Central Zone 2",

        "hour":10,

        "historical_frequency":5,

        "requires_road_closure":True

    }

    return get_similar_events(

        sample

    )