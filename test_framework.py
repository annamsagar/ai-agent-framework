from core.agent import Agent
from core.task import Task
from core.flow import Flow
from core.orchestrator import Orchestrator


class DummyAgent(Agent):
    def run(self, state):
        # simple logic: add 1 to input or previous value
        base = state.get("input", 0)
        for key in state:
            if key != "input":
                base = state[key]["value"]
        return {"value": base + 1}


# Build flow
flow = Flow("test_flow")

flow.add_task(Task("step1", DummyAgent(), ["step2"]))
flow.add_task(Task("step2", DummyAgent()))

flow.set_start("step1")

# Run orchestrator
result = Orchestrator().run(flow, 1)

print("FINAL STATE:")
print(result)
