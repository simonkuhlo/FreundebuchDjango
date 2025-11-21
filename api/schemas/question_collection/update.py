from pydantic import BaseModel

class Update(BaseModel):
    name: str
    description: str
    question_ids: list[int]