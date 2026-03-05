from fastapi import FastAPI
from feedback_intelligence.src.api.endpoints import router

app = FastAPI(title="Feedback Intelligence System")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Feedback Intelligence System Running"}