from fastapi import APIRouter
from .dao import UserDAO
from trainingnote.user.schemas import SUser

router = APIRouter(prefix="/user", tags=["Auth&User"])


@router.post("/add")
async def creat_user(user: SUser):
    await UserDAO.add(email=user.email, hashed_password=user.password)
    return {"message": "User has been created"}
