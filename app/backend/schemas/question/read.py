from pydantic import BaseModel
from ..answer_type import AnswerType

class Read(BaseModel):
    id: int
    title: str
    description: str
    short: bool = False
    #answer_type: AnswerType

    class Config:
        from_attributes = True