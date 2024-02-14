from fastapi import APIRouter
from trainingnote.exercise.dao import ExerciseDAO


router = APIRouter(prefix="/exercisies", tags=["Execises"])


@router.add("/add")
async def add_exerciese(
    training_id: int, 
    title: str,
    repetitions: int | None = None,
    weight: int | None = None
): 
    await ExerciseDAO.add(training_id=training_id, title=title, repetitions=repetitions, weight=weight)
    