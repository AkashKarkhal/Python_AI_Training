from fastapi import FastAPI

from models.ai_models import (
    CafeteriaRequest,
    CafeteriaResponse
)

from services.ai_services import analyze_request


app = FastAPI(title="Running")


@app.get("/")
def home():
    return {
        "message": "running successfully"
    }


@app.post("/api/v1/ask",response_model=CafeteriaResponse)
def analysiss(req: CafeteriaRequest):
    return analyze_request(req)

