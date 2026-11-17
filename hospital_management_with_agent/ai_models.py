from pydantic import BaseModel

class HospitalRequest(BaseModel):
    user_role: str
    question: str


class HospitalResponse(BaseModel):
    answer: str
    tools_used: list[str]