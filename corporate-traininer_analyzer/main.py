from fastapi import FastAPI
from services.ai_services import anaylyze
from models.ai_models import TrainerRequest, TrainerResponse

app = FastAPI(
    title="Corporate Training Analyzer",
    version="1.0.0"
)


@app.post("/api/v1/analysis", response_model=TrainerResponse)
def analysiss(request: TrainerRequest):
    return anaylyze(request)