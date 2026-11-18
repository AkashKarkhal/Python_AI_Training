from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from services.ai_services import analyze
from modes.ai_models import TrainerRequest


class TrainingFeedBack(TypedDict):
    trainer_name: str
    learner_name: str
    trainer_topic: str
    trainer_feedback: str
    trainer_rating: int
    sentiments: str
    performance_level: str
    strength: list[str]
    improvements_areas: list[str]
    implementation_recommendation: list[str]
    ai_summary: str
    action_taken: str


def analyze_training_feedback_node(state: TrainingFeedBack):

    request = TrainerRequest(
        trainer_name=state["trainer_name"],
        learner_name=state["learner_name"],
        trainer_topic=state["trainer_topic"],
        trainer_feedback=state["trainer_feedback"],
        trainer_rating=state["trainer_rating"]
    )

    result = analyze(request)

    return {
        "trainer_name": state["trainer_name"],
        "sentiments": result.sentiments,
        "performance_level": result.performance_level,
        "strength": result.strength,
        "improvements_areas": result.improvements_areas,
        "implementation_recommendation": result.implementation_recommendation,
        "ai_summary": result.ai_summary,
        "action_taken":result.action_taken
    }

def check_trainer_performance_level(state: TrainingFeedBack):

    if state["performance_level"].lower() == "needs improvement":
        return "change_trainer"

    return "continue_trainer"

def change_trainer_node(state: TrainingFeedBack):

    return {
        "action_taken": "Change Trainer"
    }


def continue_trainer_node(state: TrainingFeedBack):

    return {
        "action_taken": "Continue with Trainer"
    }


workflow = StateGraph(TrainingFeedBack)

workflow.add_node( "analyze_training_feedback_node", analyze_training_feedback_node
)

workflow.add_node("change_trainer_node",change_trainer_node
)

workflow.add_node("continue_trainer_node",continue_trainer_node
)

workflow.add_edge( START,"analyze_training_feedback_node"
)

workflow.add_conditional_edges("analyze_training_feedback_node",check_trainer_performance_level,
    {
        "change_trainer": "change_trainer_node",
        "continue_trainer": "continue_trainer_node"
    }
)

workflow.add_edge("change_trainer_node", END
)

workflow.add_edge("continue_trainer_node",END
)

workflow_graph = workflow.compile()