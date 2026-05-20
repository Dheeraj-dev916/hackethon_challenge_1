from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from workflow_engine import AntigravityWorkflowEngine

app = FastAPI(title="Google Antigravity Autonomous Insight-to-Action System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = AntigravityWorkflowEngine()


class ReportRequest(BaseModel):
    content: str


@app.get("/")
def read_root():
    return {"status": "Antigravity backend is running", "version": "1.0.0"}

@app.get("/test")
def test_api():
    import google.generativeai as genai
    import traceback
    try:
        models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                models.append(m.name)
        return {"status": "success", "available_models": models}
    except Exception as e:
        return {"status": "error", "error_message": str(e), "traceback": traceback.format_exc()}


@app.post("/analyze")
def analyze(request: ReportRequest):
    return engine.orchestrate(request.content)


@app.get("/workflow-trace")
def workflow_trace():
    return engine.runtime.logs


@app.get("/system-state")
def system_state():
    return engine.runtime.state_manager.get_state()
