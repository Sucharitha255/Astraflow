from fastapi import FastAPI
from api.predict import router as predict_router
from fastapi.middleware.cors import CORSMiddleware
from api.resources import router as resource_router

from api.barricades import router as barricade_router

from api.diversion import router as diversion_router
from api.similar_events import router as similar_router

from api.risk import router as risk_router



app = FastAPI(
    title="AstraFlow",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(risk_router)
app.include_router(similar_router)
app.include_router(resource_router)

app.include_router(barricade_router)

app.include_router(diversion_router)
app.include_router(
    predict_router
)
@app.get("/")
def home():

    return {
        "message": "AstraFlow Backend Running"
    }