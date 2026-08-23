from fastapi import FastAPI

app = FastAPI(title="NovaPay Digital Bank")

@app.get("/")
def home():
    return {
        "message": "Welcome to NovaPay Digital Bank",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }