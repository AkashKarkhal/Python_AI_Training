from fastapi import FastAPI
from models.ai_models import LeaveRequest, EmployeeResponse
from services.ai_services import generate_response

app = FastAPI(
    title="Running",
    version="1:0:0"
)

@app.post("/api/v1/review-leave-request",response_model=EmployeeResponse)
def leaverev(request:LeaveRequest):
    result = generate_response(request)
    return result
    