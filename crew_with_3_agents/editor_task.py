from crewai import Task
from agents.editor_agent import editor_agent

def create_editor_task(writer_task):

    editor_task = Task(
        description="""
        Review the content written by the writer agent.
        Correct grammar and readability issues.
        Make the content concise and easy to understand.
        """,
        expected_output="""
        A polished and beginner-friendly final document.
        """,
        agent=editor_agent,
        context=[writer_task]
    )

    return editor_task