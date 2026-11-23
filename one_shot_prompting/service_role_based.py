from config.setings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT
from models.model_role_based import PythonAIReponse, PythonAIRequest
from prompts.prompt_role_based import SYSTEM_PROMPT, HUMAN_PROMPT
from openai import OpenAI
import json

llm = OpenAI(
    api_key = AZURE_OPENAI_API_KEY,
    base_url = f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)


def anaylyze_python_role_based(request:PythonAIRequest) -> PythonAIReponse:
    use_input = HUMAN_PROMPT.format(
        learner_name = request.learner_name,
        qustion = request.qustion,
        experience_level = request.experience_level
    )
    
    response = llm.responses.parse(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=use_input,
        text_format=PythonAIReponse
    )
    
    ai_text = response.output_text
    parse_data = json.loads(ai_text)
    
    return PythonAIReponse(**parse_data)