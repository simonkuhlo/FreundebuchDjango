from pydantic import BaseModel

class Read(BaseModel):
    id: str
    name: str