from crewai import Crew, Process

from agents.editor_agent import editor_agent
from agents.writer_agent import writer_agent
from agents.research_agents import research_agent

from tasks.editor_task import create_editor_task
from tasks.research_task import create_research_task
from tasks.writer_tasks import create_writer_task


def main():

    topic = input("Enter your topic: ")

    if len(topic.strip()) == 0:
        raise ValueError("Topic should be at least 1 character")

    research_task = create_research_task(topic)

    writer_task = create_writer_task(research_task)

    editor_task = create_editor_task(writer_task)

    crew = Crew(
        agents=[
            research_agent,
            writer_agent,
            editor_agent
        ],
        tasks=[
            research_task,
            writer_task,
            editor_task
        ],
        process=Process.sequential,
        verbose=True
    )

    try:
        crew.kickoff()

        print("______________________________________")
        print(research_task.output.raw)

        print("______________________________________")
        print(writer_task.output.raw)

        print("______________________________________")
        print(editor_task.output.raw)

    except Exception as error:
        print(
            "Unable to generate content:",
            type(error).__name__,
            error
        )


if __name__ == "__main__":
    main()