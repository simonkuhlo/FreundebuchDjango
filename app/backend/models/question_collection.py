from typing import Optional
from sqlalchemy import String, Column
from .questions_in_collection import association_table
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from models.base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from question import Question

class QuestionCollection(Base):
    __tablename__ = "question_collection"
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    questions: Mapped[list["Question"]] = relationship(secondary=association_table, back_populates="collections")

    def __repr__(self) -> str:
        return f"Question(id={self.id!r})"