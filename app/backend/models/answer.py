from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from models.base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entry import Entry
    from question import Question
    from user import User

class Answer(Base):
    __tablename__ = "answer"
    question: Mapped["Question"] = relationship("Question", back_populates="answers")
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    entry: Mapped["Entry"] = relationship("Entry", back_populates="answers")
    entry_id: Mapped[int] = mapped_column(ForeignKey("entry.id"))
    user: Mapped[Optional["User"]] = relationship("User", back_populates="answers")
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user_account.id"))
    value: Mapped[str]

    def __repr__(self) -> str:
        return f"Answer(id={self.id!r})"