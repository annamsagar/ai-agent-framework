from core.agent import Agent

class ResearchAgent(Agent):
    """
    Performs a mock research step.
    """

    def run(self, state: dict) -> dict:
        query = state["input"]
        research_output = f"Research findings about: {query}"
        return {
            "research": research_output
        }
