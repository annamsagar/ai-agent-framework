from fastapi import FastAPI
from pydantic import BaseModel

from core.flow import Flow
from core.task import Task
from core.orchestrator import Orchestrator

from agents.ingest_agent import IngestAgent
from agents.embed_agent import EmbedAgent
from agents.qa_agent import QAAgent


app = FastAPI(title="AI Agent Framework API")


class InputRequest(BaseModel):
    text: str


@app.get("/")
def health():
    return {"status": "running"}

@app.post("/run/document-qa")
def run_document_qa(request: InputRequest):
    try:
        flow = Flow("document_qa_api")

        flow.add_task(Task("ingest", IngestAgent(), ["embed"]))
        flow.add_task(Task("embed", EmbedAgent(), ["answer"]))
        flow.add_task(Task("answer", QAAgent()))

        flow.set_start("ingest")

        result = Orchestrator().run(flow, request.text)
        return result

    except Exception as e:
        return {
            "error": "API execution failed",
            "details": str(e)
        }
