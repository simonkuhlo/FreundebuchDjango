from pydantic import BaseModel
from ..user import UserRead


class EntryRead(BaseModel):
    id: int
    user: UserRead