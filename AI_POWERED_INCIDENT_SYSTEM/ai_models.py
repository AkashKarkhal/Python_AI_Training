from pydantic import BaseModel
from typing import Literal


class IncidentRequest(BaseModel):
    employee_id: str
    employee_name: str
    department: str
    issue: str


class IncidentAnalysis(BaseModel):
    category: str
    priority: Literal["critical", "high", "medium", "low"]
    summary: str
    business_impact: str
    suggested_resolution: str


class IncidentResponse(BaseModel):
    employee_id: str
    employee_name: str
    department: str
    issue: str
    category: str
    priority: str
    summary: str
    business_impact: str
    suggested_resolution: str
    escalation_required: bool
    email_sent: bool
    status: str
    notification: str