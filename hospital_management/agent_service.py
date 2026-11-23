from langchain_core.messages import AIMessage

from agent.ai_agent import create_hospital_agent
from models.ai_models import (
    HospitalRequest,
    HospitalResponse
)

agent = create_hospital_agent()

def hospital_assistant(
    request: HospitalRequest
) -> HospitalResponse:

    result = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content": request.question
                }
            ]
        }
    )

    tools_used = []

    for message in result["messages"]:

        if isinstance(message, AIMessage):

            for tool_call in message.tool_calls:

                tools_used.append(
                    tool_call["name"]
                )

    answer = result["messages"][-1].content

    return HospitalResponse(
        answer=str(answer),
        tools_used=tools_used
    )