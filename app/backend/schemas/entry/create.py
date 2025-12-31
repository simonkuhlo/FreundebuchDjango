from typing import Optional, Any
from pydantic import BaseModel, model_validator
from utils import secret_generator


def empty_str_to_none(v):
    """Convert empty string to None before validation."""
    return None if v == "" else v

class EntryCreate(BaseModel):
    owner_id: Optional[int] = None
    secret: Optional[str] = secret_generator.generate_secret()
    published: bool = False

    @model_validator(mode='before')
    @classmethod
    def empty_str_to_none(cls, data: Any) -> Any:
        if isinstance(data, dict):
            return {k: None if isinstance(v, str) and v.strip() == '' else v
                    for k, v in data.items()}
        return data