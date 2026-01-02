from core.flow import Flow
from core.task import Task
from core.orchestrator import Orchestrator

from agents.research_agent import ResearchAgent
from agents.validator_agent import ValidatorAgent


# Define Research → Validate workflow
flow = Flow("research_validate")

flow.add_task(Task("research", ResearchAgent(), ["validate"]))
flow.add_task(Task("validate", ValidatorAgent()))

flow.set_start("research")

# Run the workflow
result = Orchestrator().run(flow, "AI agent frameworks")
print("FINAL RESULT:")
print(result)
