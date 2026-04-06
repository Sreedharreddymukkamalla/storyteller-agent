from google.adk.agents.llm_agent import Agent


root_agent = Agent(
    model='gemini-2.5-flash',
    name='storyteller',
    description='Write story based on the outline provided by the user',
    instruction="""
        Write story based on the outline provided by the user. It will be of 100 words shorter version as it is for a short film.
    """
)
