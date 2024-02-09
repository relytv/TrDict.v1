from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import ForeignKey, String

from trainingnote.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ..training.models import Training


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    training_id: Mapped[int] = mapped_column(ForeignKey("trainings.id"), nullable=False)
    title: Mapped[String] = mapped_column(String(20))
    repetitions: Mapped[int | None]
    weight: Mapped[int | None]
    training: Mapped["Training"] = relationship(back_populates="exercise")
