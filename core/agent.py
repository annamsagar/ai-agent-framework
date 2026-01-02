from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def run(self, state: dict) -> dict:
        """
        Execute the agent logic.

        Args:
            state (dict): Shared workflow state containing inputs and
                          outputs of previous tasks.

        Returns:
            dict: Output produced by this agent.
        """
        pass
