from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from services.ai_services import give_answer


class MaintenanceState(TypedDict):
    question: str
    answer: str


def answer_node(state: MaintenanceState):

    answer = give_answer(state["question"])

    return {
        "answer": answer
    }


workflow = StateGraph(MaintenanceState)

workflow.add_node(
    "answer_node",
    answer_node
)

workflow.add_edge(START, "answer_node")
workflow.add_edge("answer_node", END)

workflow_graph = workflow.compile()