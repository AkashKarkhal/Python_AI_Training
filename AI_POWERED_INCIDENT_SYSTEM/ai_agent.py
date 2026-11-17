from services.ai_services import analyze
from models.ai_models import IncidentRequest


def incident_agent(state):

    request = IncidentRequest(
        employee_id=state["employee_id"],
        employee_name=state["employee_name"],
        department=state["department"],
        issue=state["issue"]
    )

    return analyze(request) 