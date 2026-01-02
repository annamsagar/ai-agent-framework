from core.agent import Agent

class IngestAgent(Agent):
    """
    Reads raw input and prepares it for downstream agents.
    """

    def run(self, state: dict) -> dict:
        text = state["input"]
        return {
            "text": text
        }
