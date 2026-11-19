from pydantic import BaseModel, Field, ConfigDict


class CricketPlayerBase(BaseModel):

    player_name: str = Field(min_length=2)
    team_name: str = Field(min_length=2)
    role: str = Field(min_length=2)
    matches_played: int = Field(ge=0, le=1000)
    total_runs: int = Field(ge=0, le=200000)
    wickets_taken: int = Field(ge=0, le=1000)
    balls_faced: int = Field(ge=0, le=300000)
    catches: int = Field(ge=0, le=4000)


class CricketPlayerCreate(CricketPlayerBase):
    pass


class CricketPlayerUpdate(CricketPlayerBase):
    pass


class CricketPlayerResponse(CricketPlayerBase):

    player_id: int

    model_config = ConfigDict(
        from_attributes=True
    )
    
class StrikeRateResponse(BaseModel):
    player_id: int
    player_name: str
    strike_rate: float    