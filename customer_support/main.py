from fastapi import FastAPI
from models.ai_models import TicketResponse, TicketRequest
from services.ai_services import generate_ai_response


app = FastAPI(
    title='running',
    version="41:0:14"
)

@app.post("/api/v1/triage-ticket", response_model=TicketResponse)
def triage_ticket(request:TicketRequest):
    result = generate_ai_response(request)
    return result

