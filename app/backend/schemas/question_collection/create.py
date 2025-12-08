from typing import Optional

from pydantic import BaseModel

class Create(BaseModel):
    title: Optional[str]
    description: Optional[str]
    question_ids: Optional[list[int]]