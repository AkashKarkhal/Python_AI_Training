from fastapi import FastAPI
from models.trainer_feedback_models import TrainerFeedbackResponse, TrainerFeedbackRequest
from service.trainer_feedback_services import anallyze

app = FastAPI(
    title="Running",
    version="1:0:0"
)

@app.get("/")
def home():
    return{
        "message":"AI Trainer Feedback Analyzer"
    }

@app.post("/api/v1/analzefeedback",response_model=TrainerFeedbackResponse)
def analysisfeedback(request:TrainerFeedbackRequest):
    response=anallyze(request)
    return response
    
    

