from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import traceback

from planner import create_plan
from executor import execute_plan
from reflection import review_document
from doc_generator import create_word

app = FastAPI(
    title="FluidAI Autonomous Agent",
    version="1.0"
)

class UserRequest(BaseModel):
    request: str

@app.get("/")
def home():
    return {
        "message": "FluidAI Autonomous Agent is running.",
        "docs": "/docs"
    }

@app.post("/agent")
def run_agent(user: UserRequest):
    try:
        print("Step 1: Planning...")
        plan = create_plan(user.request)

        print("Step 2: Executing...")
        draft = execute_plan(plan)

        print("Step 3: Reviewing...")
        reviewed = review_document(draft)

        print("Step 4: Creating Word document...")
        file_path = create_word(reviewed)

        print("Generated:", file_path)

        return FileResponse(
            path=file_path,
            filename="AI_Project_Proposal.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception:
        traceback.print_exc()
        raise