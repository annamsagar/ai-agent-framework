from core.flow import Flow
from core.task import Task
from core.orchestrator import Orchestrator

from agents.ingest_agent import IngestAgent
from agents.embed_agent import EmbedAgent
from agents.qa_agent import QAAgent


# Define the Document QA workflow
flow = Flow("document_qa")

flow.add_task(Task("ingest", IngestAgent(), ["embed"]))
flow.add_task(Task("embed", EmbedAgent(), ["answer"]))
flow.add_task(Task("answer", QAAgent()))

flow.set_start("ingest")

# Run the workflow
result = Orchestrator().run(flow, "AI agents are powerful")
print("FINAL RESULT:")
print(result)
