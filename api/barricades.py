from fastapi import APIRouter

from core.barricade_engine import recommend_barricades


router = APIRouter(

    prefix="/api",

    tags=["Barricades"]

)


@router.get("/barricades")

def get_barricades():

    barricades = recommend_barricades(

        risk_score=75,

        historical_frequency=8,

        requires_road_closure=True

    )

    return {

        "barricades_required":

        barricades

    }