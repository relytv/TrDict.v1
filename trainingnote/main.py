from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from trainingnote.user.router import router as user_router
from trainingnote.training.router import router as training_router
from trainingnote.exercise.router import router as exercise_router
from redis import asyncio as aioredis

app = FastAPI()


@app.get("/", tags=["root"])
async def hello():
    return {"messege": "hello"}


app.include_router(user_router)
app.include_router(training_router)
app.include_router(exercise_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
