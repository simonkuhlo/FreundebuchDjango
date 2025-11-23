from typing import Optional, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from models.base import Base
if TYPE_CHECKING:
    from answer import Answer
    from entry import Entry

class User(Base):
    __tablename__ = "user_account"
    name: Mapped[str] = mapped_column(String(30))
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="user")
    entries: Mapped[list["Entry"]] = relationship("Entry", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}"