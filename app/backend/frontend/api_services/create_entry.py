from typing import Optional
from backend.schemas.entry import EntryRead, EntryCreate
from backend.schemas.answer import AnswerRead, EntryAnswerRead
from backend.schemas.question import QuestionRead
from backend.schemas.user import UserRead
import json
import httpx
import settings

async def create_entry(user_id):
    async with httpx.AsyncClient() as client:
        dict = {"user_id": user_id}
        response = await client.post(f"{settings.api_url}/entry/", content=json.dumps(dict))
        try:
            response.raise_for_status()
        except:
            return None
        entry = EntryRead.model_validate(response.json())
        return entry