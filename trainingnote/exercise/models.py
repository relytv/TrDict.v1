from datetime import date

from sqlalchemy import ForeignKey

from trainingnote.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    training_id: Mapped[int] = mapped_column(ForeignKey)
    
