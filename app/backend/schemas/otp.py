from typing import Optional

from pydantic import BaseModel


class OTPCreate(BaseModel):
    name: Optional[str] = None
    key_length:int = 5

class OTPUse(BaseModel):
    secret: str

class OTPRead(BaseModel):
    name: str
    secret: str