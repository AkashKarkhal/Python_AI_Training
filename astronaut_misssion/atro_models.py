from pydantic import BaseModel, Field, field_validator
from typing import Literal

class AstroNautsRequest(BaseModel):
    astronaut_id:str = Field(min_length=1)
    astronaut_name:str =Field(min_length=1)
    age:int = Field(ge=18, le=65)
    training_hours:int = Field(ge=0)
    medical_clearance:bool
    previous_mission:int = Field(ge=0)
    mission_type: Literal["Research", "Maintenance", "Exploration"]
    
    
class AstroNautAnalyst(BaseModel):
    age_eligible:bool
    training_eligible:bool
    medical_eligible:bool
    experience_eligible:bool
    failed_checks:list[str]
    risk_level:Literal["LOW","MEDIUM","HIGH"]
    
        
class AstroNautResponse(BaseModel):
    astronaut_id:str
    astronaut_name:str
    mission_type:str
    readiness_status:Literal["READY","NOT_READY"]
    risk_level:Literal["LOW","MEDIUM","HIGH"]
    reason:str
    recommendation:str
    
    
