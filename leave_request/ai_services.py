from openai import OpenAI
from models.ai_models import LeaveRequest, EmployeeResponse
from prompts.ai_prompts import SYSTEM_PROMPT, HUMAN_PROMPT

from config.settings import (
    AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINTS
)

llm = OpenAI(
    api_key = AZURE_OPENAI_API_KEY,
    base_url = f"{AZURE_OPENAI_ENDPOINTS.rstrip('/')}/openai/v1/"
)

def generate_response(request:LeaveRequest) -> EmployeeResponse:
    user_prompt = HUMAN_PROMPT.format(
        employee_name = request.employee_name,
        department = request.department,
        leave_type= request.leave_type,
        start_date = request.start_date,
        end_date = request.end_date,
        reason = request.reason
    )
    
    response = llm.responses.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt
    )
    
    ai_text = response.output_text
    return EmployeeResponse(
        responsefromAI=ai_text
    )