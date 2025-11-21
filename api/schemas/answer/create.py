from pydantic import BaseModel

class Answer(BaseModel):
    question_id: int
    entry_id: int
    string_value: str