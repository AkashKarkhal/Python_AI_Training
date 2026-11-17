from pydantic import BaseModel,Field

class TrainingRequest(BaseModel):
    learner_name:str = Field(min_length=1)
    department:str = Field(min_length=1)
    pythonscore:int = Field(ge=0, le=100)
    sqlscore:int = Field(ge=0, le=100)
    fastapiscore:int = Field(ge=0, le=100)
    attendanceperecentage:float = Field(ge=0, le=100)
    assignmentcompleted:int = Field(ge=0)
    totalassignment:int = Field(gt=0)
    
    
class TrainingAnalysis(BaseModel):
    averagescore:float
    performancelevel:str
    strongesttech:str
    weaktech:str
    technicnalassessment:str
    recommendation:list[str]
    
    
class TrainingResponse(BaseModel):
    learner_name:str
    department:str
    analysis:TrainingAnalysis
    finalrecommendation:str
    
        