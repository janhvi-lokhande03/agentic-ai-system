from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from services.orchestrator import Orchestrator

app = FastAPI()

orchestrator = Orchestrator()

@app.get("/")
def home():
    return {
        "message": "Agentic AI System Running"
    }

@app.get("/run")
async def run_task():

    async def generator():

        async for result in orchestrator.execute(
            "Research AI tools"
        ):
            yield result

    return StreamingResponse(
        generator(),
        media_type="text/plain"
    )