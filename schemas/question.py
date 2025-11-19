from pydantic import BaseModel
from .answer_type import AnswerType

class Question(BaseModel):
    header: str
    description: str
    answer_type: AnswerType