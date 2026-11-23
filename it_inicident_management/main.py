from fastapi import FastAPI
from models.ai_models import IncidentRequest
from workflow.ai_workflow import incident_workflow

app = FastAPI(
    title="IT Incident Management System",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "IT Incident Management API Running"}


@app.post("/analyze-incident")
def analyze_incident(request: IncidentRequest):

    result = incident_workflow.invoke(
        {
            "employee_id": request.employee_id,
            "employee_name": request.employee_name,
            "department": request.department,
            "issue": request.issue
        }
    )

    return result