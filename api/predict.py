from fastapi import APIRouter

from core.astraflow_pipeline import run_astraflow


router = APIRouter(

    prefix="/predict",

    tags=["AstraFlow"]

)


@router.post("/")

def predict(

    event: dict

):

    return run_astraflow(

        event

    )