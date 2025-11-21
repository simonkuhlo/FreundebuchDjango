from pydantic import BaseModel

class Create(BaseModel):
    name: str
    description: str
    question_ids: list[int]