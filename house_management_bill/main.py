from fastapi import FastAPI

from models.ai_models import QueryRequest, QueryResponse
from workflow.ai_workflow import workflow_graph

app = FastAPI(
    title="House Maintenance Bill Assistant"
)


@app.get("/")
def home():
    return {
        "message": "Running"
    }


@app.post(
    "/api/v1/ask",
    response_model=QueryResponse
)
def ask(data: QueryRequest):

    result = workflow_graph.invoke(
        {
            "question": data.question
        }
    )

    return QueryResponse(
        question=data.question,
        answer=result["answer"]
    )