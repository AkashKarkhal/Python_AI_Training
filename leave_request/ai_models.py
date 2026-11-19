from pydantic import BaseModel, Field, model_validator
from datetime import date

class LeaveRequest(BaseModel):
    employee_name:str
    department:str
    leave_type:str
    start_date:date
    end_date:date
    reason:str
    
    @classmethod
    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date < self.start_date:
            raise ValueError("end date cannot be before start date")
        return self
    
    
class EmployeeResponse(BaseModel):
    responsefromAI:str
    status:str = "Pending Review"    