from enum import Enum
from typing import Union
from pydantic import BaseModel

class BaseAnswerType(BaseModel):
    name = "string"

AnswerType = Union[BaseAnswerType]