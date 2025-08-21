from research_crew.tools.custom_tool import arxiv_tool, wikipedia_tool
from crewai import LLM

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
load_dotenv(override=True)

import os

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
        model="gemini/gemini-2.5-flash",
        api_key=gemini_api_key
    )

@CrewBase
class ResearchPaperCrew():
    """Research paper Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self)->Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=llm,
            tools=[arxiv_tool, wikipedia_tool],
            max_iter=5,
            max_rpm=20,
            verbose=True
        )
    @agent
    def analyst(self)->Agent:
        return Agent(
            config=self.agents_config['analyst'],
            llm=llm,
            max_iter=5,
            max_rpm=20,
            verbose=True
        )

    @task
    def research_task(self)->Task:
        return Task(
            config=self.tasks_config['research_task']
        )
    @task
    def reporting_task(self)->Task:
        return Task(
            config=self.tasks_config['reporting_task']
        )

    @crew
    def crew(self)->Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )