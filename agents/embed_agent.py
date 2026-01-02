from core.agent import Agent

class EmbedAgent(Agent):
    """
    Generates a simple embedding representation.
    (Placeholder logic – will be optimized later with Intel OpenVINO)
    """

    def run(self, state: dict) -> dict:
        text = state["ingest"]["text"]
        embedding = len(text)  # simple placeholder embedding
        return {
            "embedding": embedding
        }
