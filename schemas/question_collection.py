from pydantic import BaseModel
from .question import Question

class QuestionCollection(BaseModel):
    name: str
    description: str
    questions: list[Question]