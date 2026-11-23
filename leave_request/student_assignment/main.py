from fastapi import FastAPI
from dotenv import load_dotenv
from models.ai_models import AssignResponse, AssignRequest
from services.ai_services import assign

load_dotenv()

app = FastAPI(
    title='Running',
    version="1:0:0"
)

@app.post("/api/v1/assign", response_model=AssignResponse)
def studentass(request:AssignRequest):
    result = assign(request)
    return result