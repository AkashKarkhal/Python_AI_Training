from decimal import Decimal
from pydantic import (BaseModel, Field, EmailStr, ConfigDict)

class EmployeeBase(BaseModel):
    employee_name: str = Field(min_length=2)
    department: str = Field(min_length=2)
    designation: str = Field(min_length=2)
    salary: int = Field(ge=20000, le=100000)
    performance_rating: float = Field(ge=1, le=5)
    projects_completed: int = Field(ge=0)
    attendance_percentage: float = Field(ge=0, le=100)
    review_year: int = Field(ge=2000, le=2100)
    
class EmployeeCreate(EmployeeBase):
        pass
class EmployeeUpdate(EmployeeBase):
        pass
class EmployeeResponse(EmployeeBase):
    employee_id:int
    model_config = ConfigDict(from_attributes=True)    
    
class DepartmentAverage(BaseModel):
    department: str
    average_rating: float    
    
class EmployeeCategory(BaseModel):
    employee_id: int
    employee_name: str
    category: str    