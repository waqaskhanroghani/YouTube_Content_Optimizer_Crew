from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class YouTubeOptimizerCrew:
    """YouTube Content Optimizer crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def title_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["title_generator"],
            tools=[SerperDevTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def description_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["description_writer"],
            tools=[SerperDevTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def tag_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["tag_researcher"],
            tools=[SerperDevTool()],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def generate_title_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_title_task"],
            agent=self.title_generator(),
        )

    @task
    def create_description_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_description_task"],
            agent=self.description_writer(),
        )

    @task
    def research_tags_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_tags_task"],
            agent=self.tag_researcher(),
            output_file="youtube_optimization.json",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the YouTube Content Optimizer crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
