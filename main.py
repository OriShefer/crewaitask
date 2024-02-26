import os
from textwrap import dedent
from crewai import Crew, Process
from agents import CustomAgents
from tasks import CustomTasks


os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

class CustomCrew:
    def __init__(self, POI, goal):
        self.POI = POI
        self.goal = goal

    def run(self,POI, goal):
        self.POI = POI
        self.goal = goal
        agents = CustomAgents(self.POI,self.goal)
        tasks = CustomTasks(self.POI,self.goal)

        POIResearcher_agent = agents.POIConnection_researcher()
        GOALResearcheragent = agents.GOALConnection_researcher()
        dataAnalyst_connection_agent = agents.dataAnalyst_connection()
        dataAnalyst_risk_agent = agents.dataAnalyst_risk()

        project_manager = agents.project_manager()
        

        POIResearch_task = tasks.POIResearch_task( POIResearcher_agent)

        GOALResearch_task = tasks.GOALResearch_task(GOALResearcheragent)

        dataAnalyst_connection_task = tasks.dataAnalyst_connection_task(dataAnalyst_connection_agent)

        dataAnalyst_risk_task = tasks.dataAnalyst_risk_task(dataAnalyst_risk_agent)

        project_manager_task = tasks.project_manager_task(project_manager)

        crew = Crew(
            agents=[POIResearcher_agent, GOALResearcheragent, dataAnalyst_connection_agent, dataAnalyst_risk_agent, project_manager],
            tasks=[POIResearch_task, GOALResearch_task,dataAnalyst_connection_task, dataAnalyst_risk_task,project_manager_task],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("-------------------------------")
    POI = input(dedent("""Enter POI: """))
    GOAL = input(dedent("""Enter GOAL: """))
    print("-------------------------------")

    custom_crew = CustomCrew(POI, GOAL)
    result = custom_crew.run(POI, GOAL)
    print("\n\n########################")
    print("## Here is the crew run result:")
    print("########################\n")
    print(result)
