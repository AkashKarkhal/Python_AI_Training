from fastapi import FastAPI
from models.ai_models import HospitalRequest, HospitalResponse
from services.agent_service import hospital_assistant

app = FastAPI(
    title="Hospital AI Assistant",
    version="1.0.0"
)

@app.post(
    "/hospital/ask",
    response_model=HospitalResponse
)
def ask_hospital(request: HospitalRequest):
    return hospital_assistant(request)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "Hospital AI Assistant is running"
    }