from pydantic import BaseModel
from typing import List, Literal

class TicketRequest(BaseModel):
    ticket_id:str
    employee_name:str
    department:str
    issue_description:str
    
class TicketResponse(BaseModel):
    responsefromAI:str
        