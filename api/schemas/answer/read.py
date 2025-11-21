from pydantic import BaseModel
from ..user import UserRead

class Answer(BaseModel):
    id: int
    question_id: int
    user: UserRead
    entry_id: int
    string_value: str