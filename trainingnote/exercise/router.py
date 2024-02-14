from fastapi import APIRouter, Depends
from trainingnote.exercise.dao import ExerciseDAO
from trainingnote.user.models import User
from trainingnote.user.dependencies import get_current_user


router = APIRouter(prefix="/exercisies", tags=["Execises"])


@router.post("/add")
async def add_exerciese(
    training_id: int,
    title: str,
    repetitions: int | None = None,
    weight: int | None = None,
    user: User = Depends(get_current_user),
):
    await ExerciseDAO.add(
        training_id=training_id, title=title, repetitions=repetitions, weight=weight
    )


@router.get("/get_all")
async def get_all(training_id: int, user: User = Depends(get_current_user)):
    return await ExerciseDAO.find_all(training_id=training_id)


@router.delete("/delete")
async def delete_training(exercise_id: int, user: User = Depends(get_current_user)):
    return await ExerciseDAO.delete(model_id=exercise_id)
