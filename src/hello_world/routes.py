from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Hello World"], prefix="/hello-world")


@router.get("/")
async def hello_world() -> dict:
    return {"message": "Hello World...!"}
