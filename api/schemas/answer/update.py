from pydantic import BaseModel

class Answer(BaseModel):
    string_value: str