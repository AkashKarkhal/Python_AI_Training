from openai import OpenAI
from models.ai_models import AssignRequest, AssignResponse
from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINTS
from prompts.ai_prompts import SYSTEM_PROMPT,HUMAN_PROMPT

llm = OpenAI(
    api_key = AZURE_OPENAI_API_KEY,
    base_url = f"{AZURE_OPENAI_ENDPOINTS.rstrip('/')}/openai/v1/"
)

def assign(request:AssignRequest) -> AssignResponse:
    user_prompt = HUMAN_PROMPT.format(
        student_name = request.student_name,
        course_name = request.course_name,
        assignment_title = request.assignment_title,
        assignment_description = request.assignment_description,
        evaluation_criteria  = request.evaluation_criteria
    )
    response = llm.responses.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt
    )
    
    ai_text = response.output_text
    return AssignResponse(
        responsefromAI=ai_text
    )