from datetime import datetime
from pydantic import BaseModel


class AddTrainingDTO(BaseModel):
    user_id: int
    description: str
    date: datetime


class TrainingDTO(AddTrainingDTO):
    id: int


class RelTrainingDTO(AddTrainingDTO):
    pass

