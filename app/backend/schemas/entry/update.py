from typing import Optional
from pydantic import BaseModel


class EntryUpdate(BaseModel):
    owner_id: Optional[int] = None
    secret: Optional[str] = None
    published: Optional[bool] = False

    class Config:
        from_attributes = True