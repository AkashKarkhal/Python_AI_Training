from fastapi import FastAPI
from config.database import Base, SessionLocal, engine
from schemas.player_schema import CricketPlayerCreate, CricketPlayerResponse, CricketPlayerUpdate,StrikeRateResponse
from services import player_services as services

app = FastAPI(
    title="Fast API",
    version="41:0:14"
)


Base.metadata.create_all(bind=engine)


@app.post("/addplayer", response_model=CricketPlayerResponse)
def add_player(data: CricketPlayerCreate):
    db = SessionLocal()
    return services.add_player(db, data)


@app.get("/get_all", response_model=list[CricketPlayerResponse])
def get_all_player():
    db = SessionLocal()
    return services.Get_all_player(db)

@app.get("/get_by_id/{player_id}", response_model=CricketPlayerResponse)
def get_by_id(player_id:int):
    db = SessionLocal()
    return services.get_player_by_id(db, player_id)
    
    
@app.put("/update/{player_id}", response_model=CricketPlayerResponse)
def update(data:CricketPlayerUpdate, player_id:int):
    db= SessionLocal()
    return services.get_update(db, player_id, data)


@app.delete("/delete/{player_id}", response_model=CricketPlayerResponse)
def delete(player_id:int):
    db = SessionLocal()
    deleted = services.delete(db, player_id)
    if deleted:
        return {"message": "Employee deleted successfully"}

    return {"message": "Employee not found"}  


@app.get("/get_by_team_name/{team_name}", response_model=list[CricketPlayerResponse])
def by_team_name(team_name:str):
    db = SessionLocal()
    return services.filter_by_team(db, team_name)


@app.get("/allrounder",response_model=list[CricketPlayerResponse])
def get_allrounder():
    db = SessionLocal()
    return services.allrounder_with_10_wickets(db)

@app.get("/top_5_scorer",response_model=list[CricketPlayerResponse])
def top_5_scorers():
    db = SessionLocal()
    return services.top_5_runs(db)


@app.get(
    "/strikerate/{player_id}",
    response_model=StrikeRateResponse
)
def get_strikerate(player_id: int):
    db = SessionLocal()
    return services.strikerate(db, player_id)