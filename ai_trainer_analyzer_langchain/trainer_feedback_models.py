from pydantic import BaseModel,Field
from typing import Literal

class TrainerFeedbackRequest(BaseModel):
    trainer_name:str
    training_topic:str
    learner_name:str
    rating:int = Field(ge=1, le=5)
    feedback:str
    
class TrainerFeedbackResponse(BaseModel):
    trainer_name:str
    sentiments:Literal["Positive", "Neutral", "Negative",]
    performance_level:Literal["Excelent","Good","Average","Needs Improvement"]
    strength:list[str]
    improvement_areas:list[str]
    recommendation:str
    overall_summary:str
        
        
