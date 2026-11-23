from fastapi import FastAPI
from services.service_role_based import anaylyze_python_role_based
from models.model_role_based import PythonAIReponse, PythonAIRequest

app=  FastAPI(
    title="Running",
    version="1:0:0"
)

@app.post("/v1/api/analyzedata",response_model=PythonAIReponse)
def analyze(request:PythonAIRequest):
    return anaylyze_python_role_based(request)