from fastapi import FastAPI
from trainingnote.user.router import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/", tags=["root"])
async def hello():
    return {"messege": "hello"}
