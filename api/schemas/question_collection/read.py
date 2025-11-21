from pydantic import BaseModel
from ..question import QuestionRead

class Read(BaseModel):
    id: int
    name: str
    description: str
    questions: list[QuestionRead]