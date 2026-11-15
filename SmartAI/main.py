from fastapi import FastAPI
from services.ai_services import analyze
from models.ai_models import ResponseModel,RequestModel,AnalysisModel

app = FastAPI(
    title="Corporate Training Analyzer",
    version="1.0.0"
)


@app.post("/api/v1/analysis", response_model=ResponseModel)
def analysiss(request: RequestModel):
    return analyze(request)