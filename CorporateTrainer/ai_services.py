from models.ai_models import TrainerAnalysis, TrainerRequest, TrainerResponse
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
from prompts.ai_prompts import SYSTEM_PROMPT, HUMAN_PROMPT
from openai import AzureOpenAI
import json


llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)


def anaylyze(request: TrainerRequest) -> TrainerResponse:

    user_prompt = HUMAN_PROMPT.format(
        learner_id=request.learner_id,
        learner_name=request.learner_name,
        training_program=request.training_program,
        topics_completed=request.topics_completed,
        assignments_assigned=request.assignments_assigned,
        assignments_completed=request.assignments_completed,
        attendance_percentage=request.attendance_percentage,
        coding_assessment_score=request.coding_assessment_score,
        trainer_feedback=request.trainer_feedback
    )

    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    ai_text = response.choices[0].message.content

    if not ai_text:
        raise ValueError("Empty Response")

    data = json.loads(ai_text)

    analysis = TrainerAnalysis(
        completion_percentage=data["completion_percentage"],
        learning_level=data["learning_level"],
        strong_topics=data["strong_topics"],
        weak_topics=data["weak_topics"],
        readiness_score=data["readiness_score"],
        improvements_priority=data["improvements_priority"]
    )

    return TrainerResponse(
        learner_id=request.learner_id,
        learner_name=request.learner_name,
        analysis=analysis,
        recommended_practice=data["recommended_practice"],
        next_learning_plan=data["next_learning_plan"],
        trainer_recommendation=data["trainer_recommendation"],
        ai_summary=data["ai_summary"]
    )
