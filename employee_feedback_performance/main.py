from fastapi import FastAPI
from dotenv import load_dotenv
from models.ai_model import EmployeeResponse, EmployeeRequest
from services.ai_services import generate_ai_response
load_dotenv()

app = FastAPI(
    title="running",
    version="1:0:0"
)

@app.post("/api/v1/analyze-employee", response_model=EmployeeResponse)
def analyze_employee(request:EmployeeRequest):
    result = generate_ai_response(request)
    return result

