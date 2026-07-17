from fastapi import FastAPI

app = FastAPI(
    title="AttendAI",
    description="AI Powered WhatsApp Attendance Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "AttendAI",
        "message": "Welcome to AttendAI!",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }