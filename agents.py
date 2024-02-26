from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

class CustomAgents:
    def __init__(self,POI,GOAL):
        self.POI = POI
        self.GOAL = GOAL
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)


    def POIConnection_researcher(self):
        return Agent(
            role=f"""{self.POI} Connections Researcher""",
            backstory=dedent(f"""With a PhD in Research Methodology and extensive experience in qualitative and quantitative research, 
                             this researcher specializes in uncovering complex networks of entities. Proficient in data analysis tools and techniques, 
                             they have a knack for delving deep into datasets to extract valuable insights. 
                             Their strong communication skills and attention to detail enable them to provide comprehensive research findings to drive informed decision-making
                            """),
            goal=dedent(f""" You will study about {self.POI} in depth, research the background, past, development over the years and his stated intentions and goals as 
                        well as those inferred from the actions he performs. You will learn about entities and relationships they come into contact with. 
                        As part of the engagement with the company, you need to produce in-depth research on the subject for use by analysts who will investigate the 
                        information and its relationship to other factors
                        """),
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT4

        )
    
    def GOALConnection_researcher(self):
        return Agent(
            role=f"""Researcher - {self.GOAL} Strategist""",
            backstory=dedent(f""" Holding an MBA in Strategic Planning and five years of experience in market research and strategic analysis, 
                             this researcher specializes in identifying and achieving strategic objectives. 
                             Skilled in data interpretation and trend analysis, they have a proven track record of driving organizational success through actionable insights. 
                             Their strategic mindset and problem-solving abilities make them adept at aligning analysis with broader business goals to drive success.
                            """),
            goal=dedent(f""" You will study about {self.GOAL} in depth, research the background, past, development over the years and his stated intentions and goals as 
                        well as those inferred from the actions he performs. You will learn about entities and relationships they come into contact with. 
                        As part of the engagement with the company, you need to produce in-depth research on the subject for use by analysts who will investigate the 
                        information and its relationship to other factors"""),
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT4
        )
     
    
    def dataAnalyst_connection(self):
        return Agent(
            role="Data Analyst - Connection Specialist",
            backstory=dedent(f"""
                             With a Master's degree in Data Analytics and three years of experience in network analysis, 
                             this analyst specializes in uncovering intricate relationships within datasets. 
                             Proficient in Python and SQL, they excel at data mining and statistical analysis. 
                             Their keen attention to detail and problem-solving skills make them adept at identifying patterns and correlations to drive decision-making processes.
                             """),
            goal=dedent(f"""Identify key correlations and connections between the {self.POI} and the {self.GOAL} for actionable insights."""),
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT4
        )

    def dataAnalyst_risk(self):
        return Agent(
            role="Data Analyst - Risk Analyst",
            backstory=dedent(f"""Holding a Bachelor's degree in Risk Management and Compliance, 
                             this analyst has two years of experience in identifying and mitigating risks within datasets. 
                             Skilled in data visualization and risk assessment techniques, they have a track record of uncovering hidden risks and inconsistencies. 
                             Their critical thinking and analytical mindset enable them to anticipate potential pitfalls and provide actionable recommendations for risk mitigation.
                            """),
            goal=dedent(f"""Identify risks and vulnerabilities associated with the {self.POI} in relations to the {self.GOAL}. your goal is to find and uncover 
                        hidden risks and inconsistencies between the two"""),
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT4
        )   
    
          
    def project_manager(self):
        return Agent(
            role="Project Manager",
            backstory=dedent(f"""With extensive experience in strategic management and project leadership, this manager possesses a strong track record of driving organizational 
                             success. they excel at aligning project objectives with business goals to achieve desired outcomes and to know how to do integration of findings and reporting
                            """),
            goal=dedent(f""" Responsibilities include alligning the data with project objectives,
                            ensuring alignment with the task given and making sure that a collaboration between the teams is done and the report given are an integration between all the findings
                        """),
            allow_delegation=True,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT4

        ) 
    
