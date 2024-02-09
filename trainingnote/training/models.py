from typing import TYPE_CHECKING
from trainingnote.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date

if TYPE_CHECKING:
    from trainingnote.user.models import User

from ..exercise.models import Exercise

class Training(Base):
    __tablename__ = "trainings"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str]
    date: Mapped[date | None]
    user: Mapped["User"] = relationship(back_populates="training")
    exercise: Mapped[list["Exercise"]] = relationship(back_populates="training")
