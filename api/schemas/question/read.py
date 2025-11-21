from pydantic import BaseModel
from schemas.answer_type import AnswerType

class Read(BaseModel):
    id: int
    header: str
    description: str
    answer_type: AnswerType