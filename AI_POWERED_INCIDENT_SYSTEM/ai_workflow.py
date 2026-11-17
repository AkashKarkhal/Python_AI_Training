from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agent.ai_agent import incident_agent
from tools.ai_tools import send_incident_email

class IncidentState(TypedDict):
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
       
def analyze_node(state):

    result = incident_agent(state)

    return {
        "category": result.category,
        "priority": result.priority,
        "summary": result.summary,
        "business_impact": result.business_impact,
        "suggested_resolution": result.suggested_resolution
    }
    

def check_priority(state):

    if state["priority"] in ["critical", "high"]:
        return "email"

    return "resolution"


def send_email_node(state):

    return {
        "escalation_required": True,
        "email_sent": True,
        "status": "Escalated",
        "notification": "Email sent successfully to IT Support Team"
    }
    return result
def provide_resolution(state):

    return {
        "escalation_required": False,
        "email_sent": False,
        "status": "Resolution Suggested",
        "notification": "No email required"
    }
 
workflow = StateGraph(IncidentState)

workflow.add_node("analyze", analyze_node)
workflow.add_node("email", send_email_node)
workflow.add_node("resolution", provide_resolution)

workflow.add_edge(START, "analyze")

workflow.add_conditional_edges(
    "analyze",
    check_priority,
    {
        "email": "email",
        "resolution": "resolution"
    }
)

workflow.add_edge("email", END)
workflow.add_edge("resolution", END)

incident_workflow = workflow.compile()