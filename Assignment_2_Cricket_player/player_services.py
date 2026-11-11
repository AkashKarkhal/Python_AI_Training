from decimal import Decimal
from sqlalchemy import desc, select, func
from sqlalchemy.orm import session
from sqlalchemy.exc import IntegrityError

from models.player_model import CricketPlayer

def add_player(db:session, data):
    player = CricketPlayer(**data.model_dump())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def Get_all_player(db:session):
    query = select(CricketPlayer).order_by(CricketPlayer.player_id)
    result = db.scalars(query)
    return result.all()

def get_player_by_id(db:session, player_id:int):
    return db.get(CricketPlayer, player_id)

def get_update(db:session, player_id:int, data):
    player = db.get(CricketPlayer, player_id)
    if player is None:
        return None
    
    for Key, Value in data.model_dump().items():
        setattr(player, Key, Value)
        
    try:
        db.commit()
        db.refresh(player)
        return player  
    
    except IntegrityError:
        db.rollback()
        raise  
    
    
def delete(db:session, player_id:int):
    player =  db.get(CricketPlayer, player_id)
    if player is None:
        return False
    db.delete(player)
    db.commit()
    return True

def filter_by_team(db:session, team_name:str):
    query = select(CricketPlayer).where( 
    CricketPlayer.team_name == team_name
    )
    return db.scalars(query).all()

def allrounder_with_10_wickets(db:session):
    query = select(CricketPlayer).where(
        CricketPlayer.role =="all-rounder",
        CricketPlayer.wickets_taken >=10
    )
    result = db.scalars(query).all()
    return result



def top_5_runs(db:session):
    query = (
        select(CricketPlayer)
        .order_by(CricketPlayer.total_runs.desc())
        .limit(5)
    )

    result = db.scalars(query)
    return result.all()


from sqlalchemy import select

def strikerate(db: Session, player_id: int):
    player = db.get(CricketPlayer, player_id)

    if player is None:
        return None

    return {
        "player_id": player.player_id,
        "player_name": player.player_name,
        "strike_rate": round(
            (player.total_runs / player.balls_faced) * 100,
            2
        )
    }