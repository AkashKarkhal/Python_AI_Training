from decimal import Decimal
from sqlalchemy import desc, select, func
from sqlalchemy.orm import session
from sqlalchemy.exc import IntegrityError
from models.feedback_models import TrainerFeedback

def add_new_feedback(db:session,data):
    feedback = TrainerFeedback(**data.model_dump())
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def get_all_feedback(db:session):
    query = select(TrainerFeedback).order_by(TrainerFeedback.feedback_id)
    result = db.scalars(query).all()
    return result

def get_by_id(db:session, feedback_id:int):
    return db.get(TrainerFeedback, feedback_id)
   
   
def update(db: session, feedback_id: int, data):
    feedback = db.get(TrainerFeedback, feedback_id)

    if feedback is None:
        return False

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(feedback, key, value)

    try:
        db.commit()
        db.refresh(feedback)
        return feedback

    except IntegrityError:
        db.rollback()
        raise
    
    
def delete(db:session, feedback_id:int):
   feedback = db.get(TrainerFeedback, feedback_id)
   if feedback is None:
       return False
   db.delete(feedback)
   db.commit()
   return True         

def by_trainer(db: session, trainer_name: str):
    query = select(TrainerFeedback).where(
        TrainerFeedback.trainer_name == trainer_name
    )

    result = db.scalars(query).all()
    return result