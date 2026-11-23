from crewai import Task
from agents.writer_agent import writer_agent

def create_writer_task(research_task):

    writer_task = Task(
        description="""
        Analyze the research provided by the research agent.
        Convert the research into well-structured content.
        Use simple and beginner-friendly language.
        """,
        expected_output="""
        Output should be clean, readable and professionally formatted.
        """,
        agent=writer_agent,
        context=[research_task]
    )

    return writer_task