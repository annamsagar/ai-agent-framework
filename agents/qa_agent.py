from core.agent import Agent

class QAAgent(Agent):
    """
    Generates an answer based on the embedding output.
    """

    def run(self, state: dict) -> dict:
        embedding = state["embed"]["embedding"]
        return {
            "answer": f"Answer generated using embedding size {embedding}"
        }
