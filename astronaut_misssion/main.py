from fastapi import FastAPI
from models.atro_models import AstroNautAnalyst, AstroNautResponse,AstroNautsRequest
from services.atro_services import analyze_astronaut

app = FastAPI(title="Running")


@app.post("/api/v1/analyse",response_model=AstroNautResponse)
def analysis(request:AstroNautsRequest):
    response = analyze_astronaut(request)
    return response




