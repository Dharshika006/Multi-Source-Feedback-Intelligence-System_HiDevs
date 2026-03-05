from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook")
def receive_feedback(data: dict):
    return {"received": data}