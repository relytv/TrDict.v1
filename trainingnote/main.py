from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["root"])
async def hello():
    return {"messege": "hello"}
