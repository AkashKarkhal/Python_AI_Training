from prompts.ai_prompts import SYSTEM_PROMPT, HUMAN_PROMPT

from models.ai_models import (
    CafeteriaRequest,
    CafeteriaAnalysis,
    CafeteriaResponse
)

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    temperature=0
)

structured_llm = llm.with_structured_output(
    CafeteriaAnalysis
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)

chain = prompt | structured_llm


def analyze_request(req: CafeteriaRequest) -> CafeteriaResponse:

    analysis = chain.invoke(
        {
            "employee_id": req.employee_id,
            "employee_name": req.employee_name,
            "food_preference": req.food_preference,
            "budget": req.budget,
            "question": req.question
        }
    )

    return CafeteriaResponse(
        employee_id=req.employee_id,
        employee_name=req.employee_name,
        analysis=analysis,
        suggested_meal=analysis.suggested_meal,
        estimated_price=analysis.estimated_price,
        reason=analysis.reason,
        status="success"
    )