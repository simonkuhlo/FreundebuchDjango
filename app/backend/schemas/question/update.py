from typing import Optional
from pydantic import BaseModel
from ..answer_type import AnswerType

class Update(BaseModel):
    title: str
    description: str
    short: Optional[bool] = False
    #answer_type: AnswerType