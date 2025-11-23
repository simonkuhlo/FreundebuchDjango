from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from models.base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from answer import Answer
    from user import User

class Entry(Base):
    __tablename__ = "entry"
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship("User", back_populates="entries")
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="entry")

    def __repr__(self) -> str:
        return f"Entry(id={self.id!r})"