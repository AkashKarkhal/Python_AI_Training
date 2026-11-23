from crewai import Task
from agents.research_agents import research_agent

def create_research_task(topic):

    research_task = Task(
        description=f"""
        Research about {topic}.
        Analyze the topic and provide information in a simple format.
        Use simple language and a readable format.
        """,
        expected_output="""
        Explain what it is, how it works, use cases and real-world examples.
        Output should be clean and clear.
        """,
        agent=research_agent
    )

    return research_task