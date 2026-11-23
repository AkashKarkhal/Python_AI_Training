from crewai import Agent
from config.settings import llm

writer_agent = Agent(
    role="You are Writer Speciliast",
    goal = "Your goal is convert research into content",
    backstory = (
        "You are very well experienced in converitng research into content"
        "you have done thousands of content"
        "you provide simple and readable content"
    ),
    llm = llm,
    verbose= True,
    allow_delegation = False
)