from crewai import Agent
from config.settings import llm

research_agent = Agent(
    role="You are Experienced Research Agent",
    goal="Research the Content given by User",
    backstory=(
        "You are Experienced Research specialist "
        "you have research thousands of researches"
    ),
    llm = llm,
    verbose = True,
    allow_delegation = False
)

