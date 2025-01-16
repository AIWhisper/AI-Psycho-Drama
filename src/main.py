from fastapi import FastAPI
from core.session import SessionManager
from core.safety import SafetyControls
from utils.logger import Logger

app = FastAPI(title="AI Psycho Drama Testing Environment")

@app.on_event("startup")
async def startup_event():
    Logger.init()
    return {"status": "Environment initialized"}

@app.get("/")
async def root():
    return {"status": "AI Psycho Drama Testing Environment Active"}
