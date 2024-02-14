from typing import TYPE_CHECKING
from datetime import date, datetime
from pydantic import BaseModel
from trainingnote.exercise.schemas import ExerciseDTO

if TYPE_CHECKING:
    from trainingnote.user.schemas import UserDTO


class AddTrainingDTO(BaseModel):
    description: str
    date: datetime | None = None
    user_id: int


class TrainingDTO(AddTrainingDTO):
    id: int
    exercise: list["ExerciseDTO"]


class RelTrainingDTO(AddTrainingDTO):
    users: "UserDTO"
