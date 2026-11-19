from fastapi import FastAPI
from config.database import Base, SessionLocal, engine
from schemas.feedback_schemas import TrainerFeedBackBase, TrainerFeedBackCreate, TrainerFeedBackResponse, TrainerFeedBackUpdate
from services import feedback_services as services
app = FastAPI(
    title="Fast API",
    version="41:0:14"
)

Base.metadata.create_all(bind=engine)
@app.post("/add", response_model=TrainerFeedBackResponse)
def add_feedback(data:TrainerFeedBackCreate):
    db = SessionLocal()
    return services.add_new_feedback(db,data)

@app.get("/get_all",response_model=list[TrainerFeedBackResponse])
def get_all():
    db = SessionLocal()
    return services.get_all_feedback(db)

@app.get("/get_by_id{feedback_id}", response_model=TrainerFeedBackResponse)
def get_by_id(feedback_id:int):
    db = SessionLocal()
    return services.get_by_id(db,feedback_id)
    
@app.put("/update{feedback_id}", response_model=TrainerFeedBackResponse)
def update(feedback_id:int, data:TrainerFeedBackUpdate):
    db = SessionLocal()
    return services.update(db,feedback_id,data)


@app.delete("/delete/{feedback_id}",response_model=TrainerFeedBackResponse)
def delete(feedback_id:int):
    db = SessionLocal()
    deleted = services.delete(db, feedback_id)
    if deleted:
        return {"message": "feedback deleted successfully"}

    return {"message": "feedback not found"} 

@app.get(
    "/bytrainer/{trainer_name}",
    response_model=list[TrainerFeedBackResponse]
)
def bytrainer(trainer_name: str):
    db = SessionLocal()
    return services.by_trainer(db, trainer_name)