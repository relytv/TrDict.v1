from typing import TYPE_CHECKING

from trainingnote.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from trainingnote.training.models import Training


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str]
    training: Mapped[list["Training"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User email={self.email}"
