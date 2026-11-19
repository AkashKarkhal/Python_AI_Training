from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional

class TrainerFeedBackBase(BaseModel):
    learner_name: str
    trainer_name: str
    course_name: str
    session_date: date
    

    content_rating: int = Field(..., ge=1, le=5)
    trainer_rating: int = Field(..., ge=1, le=5)
    hands_on_rating: int = Field(..., ge=1, le=5)

    comments: Optional[str] = None
    would_recommend: bool


class TrainerFeedBackCreate(TrainerFeedBackBase):
    pass


class TrainerFeedBackUpdate(BaseModel):
    content_rating: Optional[int] = Field(None, ge=1, le=5)
    trainer_rating: Optional[int] = Field(None, ge=1, le=5)
    hands_on_rating: Optional[int] = Field(None, ge=1, le=5)
    comments: Optional[str] = None
    would_recommend: Optional[bool] = None


class TrainerFeedBackResponse(TrainerFeedBackBase):
    feedback_id: int

    model_config = ConfigDict(from_attributes=True)