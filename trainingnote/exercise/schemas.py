from pydantic import BaseModel


class ExerciseAddDTO(BaseModel):
    training_id: int
    title: str
    repetitions: int | None = None
    weight: int | None = None


class ExerciseDTO(ExerciseAddDTO):
    id: int


class ExerciseRelDTO(ExerciseDTO):
    pass
