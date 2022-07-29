from fastapi import FastAPI

from src.database import init_db
from src.users.routes import router as user_routers
from src.hello_world.routes import router as hello_world_routs

app = FastAPI()


@app.on_event("startup")
async def start_db():
    await init_db()


app.include_router(user_routers)
app.include_router(hello_world_routs)


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your FastApi app!"}
