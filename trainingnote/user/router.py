from fastapi import APIRouter, HTTPException, Response, status

from trainingnote.user.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from .dao import UserDAO
from trainingnote.user.schemas import SUser

router = APIRouter(prefix="/user", tags=["Auth&User"])


@router.post("/register", summary="Register a new user")
async def register_user(user_date: SUser):

    existing_user = await UserDAO.find_one_or_none(email=user_date.email)
    if existing_user:
        raise HTTPException(status_code=404)
    hashed_password = get_password_hash(user_date.password)
    await UserDAO.add(email=user_date.email, hashed_password=hashed_password)


@router.post("/login")
async def login(response: Response, user_date: SUser):
    user = await authenticate_user(email=user_date.email, password=user_date.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
