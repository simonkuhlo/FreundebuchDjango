from pydantic import BaseModel
from .user import User

class Answer(BaseModel):
    question_id:int
    user:User
    entry_id:int
    string_value:str