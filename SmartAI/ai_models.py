from pydantic import BaseModel
from typing import List

class RequestModel(BaseModel):
    ticket_id:str
    employee_id:str
    employee_name:str
    department:str
    issue_description:str
    affected_system:str
    
class AnalysisModel(BaseModel):
    issue_category:str
    priority_level:str
    suspected_root_cause:str
    impact_level:str
    troubleshooting_steps:List[str]
    estimated_resolution_time:str
    
class ResponseModel(BaseModel):
    ticket_id:str
    ticket_status:str
    analysis:AnalysisModel
    recomemended_actions:list[str]
    escalation_required:bool
    ai_summary:str
    
    
    
            
    