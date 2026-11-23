from pydantic import BaseModel, Field
from typing import Literal

class PythonAIRequest(BaseModel):
    learner_name:str
    qustion:str
    experience_level:Literal["Fresher","intermediate","Experienced"]
    
class PythonAIReponse(BaseModel):
    learner_name:str
    role:str
    answer:str
    
        