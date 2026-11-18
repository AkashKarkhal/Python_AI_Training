from fastapi import FastAPI
from modes.ai_models import TrainerResponse, TrainerRequest
from workflow.ai_worklow import workflow_graph

app = FastAPI(title="AI Trainer Feedback Analyzer", version="1.0.0"
)

@app.get("/")
def home(): return {"message": "AI Trainer Feedback Analyzer" }


@app.post("/api/v1/trainer", response_model=TrainerResponse)
def analyze(request: TrainerRequest):

    result = workflow_graph.invoke({
        "trainer_name": request.trainer_name,
        "learner_name": request.learner_name,
        "trainer_topic": request.trainer_topic,
        "trainer_feedback": request.trainer_feedback,
        "trainer_rating": request.trainer_rating
    })

    return TrainerResponse(
        trainer_name=result["trainer_name"],
        sentiments=result["sentiments"],
        performance_level=result["performance_level"],
        strength=result["strength"],
        improvements_areas=result["improvements_areas"],
        implementation_recommendation=result["implementation_recommendation"],
        ai_summary=result["ai_summary"],
        action_taken=result["action_taken"]
    )