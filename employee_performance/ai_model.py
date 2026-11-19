from pydantic import BaseModel, Field
from typing import List

class EmployeeRequest(BaseModel):
    employee_name:str
    reviewer_name:str
    project_name:str
    performance_rating:int = Field(ge=1,le=5)
    feedback:str
    
class EmployeeResponse(BaseModel): 
    responsefromAI:str
    