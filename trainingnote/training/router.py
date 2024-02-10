from datetime import date
from fastapi import APIRouter, Depends
from trainingnote.training.dao import TrainingDAO
from trainingnote.user.dependencies import get_current_user


router = APIRouter(prefix="/trainigs", tags=["Trainings"])


@router.post("/add")
async def add_training(
    description: str,
    date: date | None = None,
    user=Depends(get_current_user),
):
    return await TrainingDAO.add(user_id=user.id, description=description, date=date)
