from models.ai_models import RequestModel,ResponseModel,AnalysisModel
from config.settings import(
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

from openai import AzureOpenAI
from prompts.ai_prompts import SYSTEM_PROMPT, HUMAN_PRPOMPT
import json

llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)

def analyze(request:RequestModel) -> ResponseModel:
    user_prompt = HUMAN_PRPOMPT.format(
            ticket_id = request.ticket_id,
            employee_id = request.employee_id,
            employee_name=request.employee_name,
            department = request.department,
            issue_description = request.issue_description,
            affected_system = request.affected_system
    )
    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
                
                },
            {
                "role":"user",
                "content":user_prompt
            }
        ],
        response_format={"type":"json_object"}
    )
    
    ai_text = response.choices[0].message.content
    
    if not ai_text:
        raise ValueError("Empty Respons")
    
    data = json.loads(ai_text)
    
    analysis = AnalysisModel(
            issue_category = data["issue_category"],
            priority_level=data["priority_level"],
            suspected_root_cause=data["suspected_root_cause"],
            impact_level=data["impact_level"],
            troubleshooting_steps = data["troubleshooting_steps"],
            estimated_resolution_time = data["estimated_resolution_time"]
    )
    
    return ResponseModel(
    ticket_id=request.ticket_id,
    ticket_status=data["ticket_status"],
    analysis=analysis,
    recomemended_actions=data["recomemended_actions"],
    escalation_required=data["escalation_required"],
    ai_summary=data["ai_summary"]
)