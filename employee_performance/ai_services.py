import json
from openai import OpenAI
from models.ai_model import EmployeeRequest, EmployeeResponse
from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINTS
from prompt.ai_prompt import SYSTEM_PROMPT, HUMAN_PROMPT

# Create Azure OpenAI client
llm = OpenAI(
    api_key = AZURE_OPENAI_API_KEY,
    base_url = f"{AZURE_OPENAI_ENDPOINTS.rstrip('/')}/openai/v1/"
)


def generate_ai_response(request: EmployeeRequest) -> EmployeeResponse:

    user_prompt = HUMAN_PROMPT.format(
        employee_name=request.employee_name,
        reviewer_name=request.reviewer_name,
        project_name=request.project_name,
        performance_rating=request.performance_rating,
        feedback=request.feedback
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
