from pydantic import BaseModel
from ..user import UserRead
from ..question import QuestionRead
from ..entry import EntryRead

class Answer(BaseModel):
    id: int
    question: QuestionRead
    user: UserRead
    entry: EntryRead
    string_value: str