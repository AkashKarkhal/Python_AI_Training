from pydantic import BaseModel, Field
from typing import Literal

class TrainerRequest(BaseModel):
    trainer_name:str
    learner_name:str
    trainer_topic:str
    trainer_feedback:str
    trainer_rating:int = Field(ge=1, le=5)
    
class TrainerResponse(BaseModel):
    trainer_name:str
    sentiments:str
    performance_level:str
    strength:list[str]
    improvements_areas:list[str]
    implementation_recommendation:list[str]
    ai_summary:str
    action_taken:str   
    
    
    