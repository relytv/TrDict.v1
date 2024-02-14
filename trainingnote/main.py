from fastapi import FastAPI
from trainingnote.user.router import router as user_router
from trainingnote.training.router import router as training_router
from trainingnote.exercise.router import router as exercise_router

app = FastAPI()


@app.get("/", tags=["root"])
async def hello():
    return {"messege": "hello"}


app.include_router(user_router)
app.include_router(training_router)
app.include_router(exercise_router)
