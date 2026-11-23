from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT,
)

from models.atro_models import AstroNautAnalyst, AstroNautResponse, AstroNautsRequest
from prompts.atro_prompts import HUMAN_PROMPT, SYSTEM_PROMPT

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)

prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("user", HUMAN_PROMPT)])
chain = prompt | llm.with_structured_output(AstroNautResponse)

def check_eligibility(req: AstroNautsRequest) -> AstroNautAnalyst:
    # 1. Check each rule (True or False)
    age_ok = 25 <= req.age <= 55
    training_ok = req.training_hours >= 200
    medical_ok = req.medical_clearance
    experience_ok = req.previous_mission >= 1 or req.mission_type != "Exploration"

    # 2. Collect any failed rules
    failed = []
    if not age_ok:
        failed.append("age")
    if not training_ok:
        failed.append("training")
    if not medical_ok:
        failed.append("medical")
    if not experience_ok:
        failed.append("experience")

    # 3. Decide risk level
    if not medical_ok:
        risk = "HIGH"
    elif failed:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return AstroNautAnalyst(
        age_eligible=age_ok,
        training_eligible=training_ok,
        medical_eligible=medical_ok,
        experience_eligible=experience_ok,
        failed_checks=failed,
        risk_level=risk,
    )


def analyze_astronaut(req: AstroNautsRequest) -> AstroNautResponse:
    analysis = check_eligibility(req)

    # Set readiness status
    status = "NOT READY" if analysis.failed_checks else "READY"

    # Combine request data, analysis data, and status for the prompt
    prompt_data = req.model_dump() | analysis.model_dump() | {"status": status}

    return chain.invoke(prompt_data)
