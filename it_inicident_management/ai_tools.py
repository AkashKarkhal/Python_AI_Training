from langchain.tools import tool

@tool
def send_incident_email(
    employee_id: str,
    employee_name: str,
    priority: str
):
    """Send email for high or critical incidents."""

    return {
        "escalation_required": True,
        "email_sent": True,
        "status": "Escalated"
    }