from core.agent import Agent

class ValidatorAgent(Agent):
    """
    Validates research output using simple guardrails.
    """

    def run(self, state: dict) -> dict:
        research_text = state["research"]["research"]

        # Guardrail rule
        if len(research_text) < 15:
            return {
                "status": "REJECTED",
                "reason": "Research output too short"
            }

        return {
            "status": "APPROVED",
            "validated_output": research_text
        }
