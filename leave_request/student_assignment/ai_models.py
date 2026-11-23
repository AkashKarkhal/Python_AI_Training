from pydantic import BaseModel, Field

class AssignRequest(BaseModel):
    student_name:str
    course_name:str
    assignment_title:str
    assignment_description:str
    evaluation_criteria:list[str]
    
class AssignResponse(BaseModel):  
    responsefromAI:str
      