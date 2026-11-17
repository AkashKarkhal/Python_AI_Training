from fastapi import FastAPI
from services.ai_service import analyze
from models.ai_models import TrainingResponse, TrainingRequest

app = FastAPI(title="running",version="1:0:0")

@app.post("/api/v1/ana",response_model=TrainingResponse)
def analysis(requst:TrainingRequest):
    return analyze(requst)