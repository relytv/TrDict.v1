from pydantic import BaseModel, EmailStr

from trainingnote.training.schemas import TrainingDTO


class SUser(BaseModel):
    email: EmailStr
    password: str


class AddUserDTO(BaseModel):
    email: EmailStr
    password: str


class UserDTO(AddUserDTO):
    id: int


class RelUserDTO(UserDTO):
    trainings: list["TrainingDTO"]
