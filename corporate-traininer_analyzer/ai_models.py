from pydantic import BaseModel
from typing import List


class TrainerRequest(BaseModel):
    learner_id: str
    learner_name: str
    training_program: str
    topics_completed: List[str]
    assignments_assigned: int
    assignments_completed: int
    attendance_percentage: float
    coding_assessment_score: float
    trainer_feedback: str


class TrainerAnalysis(BaseModel):
    completion_percentage: float
    learning_level: str
    strong_topics: List[str]
    weak_topics: List[str]
    readiness_score: float
    improvements_priority: List[str]


class TrainerResponse(BaseModel):
    learner_id: str
    learner_name: str
    analysis: TrainerAnalysis
    recommended_practice: List[str]
    next_learning_plan: str
    trainer_recommendation: str
    ai_summary: str