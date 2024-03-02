from fastapi import APIRouter, Depends
from trainingnote.exercise.dao import ExerciseDAO
from trainingnote.exercise.schemas import ExerciseDTO
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


@router.patch("/update_exercise")
async def update_exercise(
    exercise: ExerciseDTO, user: User = Depends(get_current_user)
):
    d = dict(exercise)
    print(d)
    need_to_update = {}
    for k in d.keys():
        if (
            d[k] != 0
            and d[k] != "string"
            and k != "id"
            and k != "training_id"
        ):
            need_to_update[k] = d[k]

    if len(need_to_update) == 0:
        return {"message": "Nothing to update"}
    print(need_to_update)

    await ExerciseDAO.update(model_id=exercise.id, **need_to_update)
    return {"updated_fields": need_to_update}
