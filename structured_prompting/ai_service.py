from models.ai_models import TrainingAnalysis, TrainingRequest, TrainingResponse
from prompts.ai_prompts import SYSTEM_PROMPT, HUMAN_PROMPT
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
from openai import AzureOpenAI
import json


llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)


def analyze(requst:TrainingRequest)->TrainingResponse:
    user_prompt = HUMAN_PROMPT.format(
    learner_name=requst.learner_name,
    department=requst.department,
    pythonscore=requst.pythonscore,
    sqlscore=requst.sqlscore,
    fastapiscore=requst.fastapiscore,
    attendanceperecentage=requst.attendanceperecentage,
    assignmentcompleted=requst.assignmentcompleted,
    totalassignment=requst.totalassignment,
    averagescore="",
    performancelevel="",
    strongesttech="",
    weaktech="",
    technicnalassessment="",
    recommendation=""
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
    
    analysis = TrainingAnalysis(
        averagescore = data["averagescore"],
        performancelevel = data["performancelevel"],
        strongesttech = data["strongesttech"],
        weaktech = data["weaktech"],
        technicnalassessment = data["technicnalassessment"],
        recommendation = data["recommendation"]
    
    )
    
    return TrainingResponse(
    learner_name=data["learner_name"],
    department=data["department"],
    analysis=TrainingAnalysis(
        averagescore=data["averagescore"],
        performancelevel=data["performancelevel"],
        strongesttech=data["strongesttech"],
        weaktech=data["weaktech"],
        technicnalassessment=data["technicnalassessment"],
        recommendation=data["recommendation"]
    ),
    finalrecommendation=data["finalrecommendation"]
)