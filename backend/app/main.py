from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Enterprise AI Document Assistant",
    description="Production-grade RAG API",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise AI Document Assistant 🚀"
    }

app.include_router(health_router)