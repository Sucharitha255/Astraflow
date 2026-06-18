from fastapi import APIRouter

from core.diversion_engine import recommend_diversion


router = APIRouter(

    prefix="/api",

    tags=["Diversion"]

)


@router.get("/diversion")

def get_diversion():

    return recommend_diversion(

        zone="Central Zone 2",

        corridor="Unknown",

        risk_score=75,

        requires_road_closure=True

    )