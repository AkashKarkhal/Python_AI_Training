from prompt.ai_prompt import SYSTEM_PROMPT, HUMAN_PROMPT
import json
from openai import OpenAI
from models.ai_models import TicketRequest, TicketResponse
from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINTS

llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url = f"{AZURE_OPENAI_ENDPOINTS.rstrip('/')}/openai/v1/"
    
)


def generate_ai_response(request:TicketRequest) -> TicketResponse:
    user_prompt = HUMAN_PROMPT.format(
        ticket_id = request.ticket_id,
        employee_name= request.employee_name,
        department = request.department,
        issue_description = request.issue_description
    )
    
    response = llm.responses.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    instructions=SYSTEM_PROMPT,
    input=user_prompt
)

    ai_text = response.output_text
    return TicketResponse(
        responsefromAI=ai_text
    )

