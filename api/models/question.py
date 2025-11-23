from typing import Optional
from sqlalchemy import String, Column
from .questions_in_collection import association_table
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from models.base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from answer import Answer
    from question_collection import QuestionCollection

class Question(Base):
    __tablename__ = "question"
    title: Mapped[str]
    value: Mapped[str]
    collections: Mapped[list["QuestionCollection"]] = relationship(secondary=association_table, back_populates="questions")
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="question")

    def __repr__(self) -> str:
        return f"Question(id={self.id!r})"