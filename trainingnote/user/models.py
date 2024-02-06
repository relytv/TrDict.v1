import imp
from typing import List
from trainingnote.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..training import Training


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str]
    training: Mapped[List["Training"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User email={self.email}"
