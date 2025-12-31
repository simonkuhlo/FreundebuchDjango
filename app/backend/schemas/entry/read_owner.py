from typing import Optional
from pydantic import BaseModel
from ..answer.read_entry import EntryAnswerRead
from ..user import UserRead


class EntryReadOwner(BaseModel):
    id: int
    secret: Optional[str] = None
    owner: Optional[UserRead] = None
    published: bool
    answers: list[EntryAnswerRead]

    class Config:
        from_attributes = True