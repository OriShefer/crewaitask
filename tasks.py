from crewai import Task
from textwrap import dedent


class CustomTasks:

    def __init__(self,POI,GOAL):
        self.POI = POI
        self.GOAL = GOAL

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def POIResearch_task(self,agent):
        return Task(
            description=dedent(
                f"""
            study about the {self.POI} in depth, research the background, past, development over the years and his/their stated intentions and goals as well as those inferred 
            from the actions he/they performs. You will learn about entities and relationships that come into contact with them. 
            You need to produce in-depth research on the subject for use by analysts who will investigate the information and its relationship to other factors.
            {self.__tip_section()}
        
        """
            ),
            agent=agent

        )
    
    def GOALResearch_task(self,agent):
        return Task(
            description=dedent(
                f"""
            study about the {self.GOAL} in depth, research the background, past, development over the years and his/their stated intentions and goals as well as those inferred 
            from the actions he/they performs. You will learn about entities and relationships that come into contact with them. 
            You need to produce in-depth research on the subject for use by analysts who will investigate the information and its relationship to other factors.                {self.__tip_section()}
        """
            ),
            agent=agent

        )
    
    def dataAnalyst_connection_task(self,agent):
        return Task(
            description=dedent(
                f"""
                Identify key correlations and connections between the {self.POI} and the {self.GOAL} for actionable insights. list all the important connection 
                and make sure to uncover the things that would get to know the {self.POI} and the relation to the {self.GOAL} 
                 """
            ),
            agent=agent


        )
    
    def dataAnalyst_risk_task(self,agent):
        return Task(
            description=dedent(
                f"""
                Conduct a critical analysis to identify potential risks associated with the provided {self.POI} related to the {self.GOAL}.
                make sure to uncover the things that would help get to know the {self.POI} in relation to {self.GOAL} and add to the insights of the connection specialist
                {self.__tip_section()}
                 """
            ),
            agent=agent


        )
    
    def project_manager_task(self, agent):
        return Task(
            description=dedent(
                f"""
                 master the information that was collected between the research team and the analyst team and to make sure that the output and result of the crew
                shows information about the {self.POI} in relation to {self.GOAL}. The goal is to learn everything that is important to know about {self.POI} and its connection to
                 the {self.GOAL} and to prioritize the importance of the information and present it.
                 making sure that a collaboration between the teams was done and pick out the information given by each analystand prioritize 
                 it in order to give the best and most beneficial output
                {self.__tip_section()}
                 """
            ),
            agent=agent,
            expected_output=f"""output and result of the crew is a 5-10 sentences report about the {self.POI} in relation to {self.GOAL}. make it in bullet points"""

        )