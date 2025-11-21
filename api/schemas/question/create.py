from pydantic import BaseModel
from ..answer_type import AnswerType

class Create(BaseModel):
    header: str
    description: str
    answer_type: AnswerType