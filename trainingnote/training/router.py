from datetime import date
from fastapi import APIRouter, Depends
from trainingnote.training.dao import TrainingDAO
from trainingnote.user.dependencies import get_current_user
from trainingnote.user.models import User


router = APIRouter(prefix="/trainigs", tags=["Trainings"])


@router.post("/add")
async def add_training(
    description: str,
    date: date | None = None,
    user: User = Depends(get_current_user),
):
    return await TrainingDAO.add(user_id=user.id, description=description, date=date)


@router.get("/get_all")
async def get_all(user: User = Depends(get_current_user)):
    return await TrainingDAO.find_all(user_id=user.id)


@router.delete("/delete")
async def delete_training(training_id: int, user: User = Depends(get_current_user)):
    return await TrainingDAO.delete(model_id=training_id)


@router.patch("/update/{training_id}")
async def update_training(training_id: int, new_description: str | None = None, user: User = Depends(get_current_user)):
    await TrainingDAO.update(training_id, description=new_description)
    return {"updated_fields": {"description": new_description}}