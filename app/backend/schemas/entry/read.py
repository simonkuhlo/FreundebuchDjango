from typing import Optional

from pydantic import BaseModel
from ..answer.read_entry import EntryAnswerRead
from ..user import UserRead


class EntryRead(BaseModel):
    id: int
    owner: Optional[UserRead] = None
    published: bool
    answers: list[EntryAnswerRead]

    class Config:
        from_attributes = True