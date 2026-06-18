from fastapi import APIRouter

from core.resource_engine import recommend_resources


router = APIRouter(

    prefix="/api",

    tags=["Resources"]

)


@router.get("/resources/{risk_score}")

def get_resources(

    risk_score:int

):

    return recommend_resources(

        risk_score

    )