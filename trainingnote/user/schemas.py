from pydantic import BaseModel, EmailStr

from trainingnote.training.schemas import TrainingDTO


class SUser(BaseModel):
    email: EmailStr
    password: str


class AddUserDTO(BaseModel):
    email: EmailStr
    #hashed_password: str


class UserDTO(AddUserDTO):
    id: int


class UserRelDTO(UserDTO):
    training: list["TrainingDTO"]
