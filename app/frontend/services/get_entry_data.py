from typing import Optional
from backend.schemas.entry import EntryRead
from backend.schemas.answer import AnswerRead, EntryAnswerRead
from backend.schemas.question import QuestionRead
from backend.schemas.user import UserRead
import httpx
import settings

async def get_entry_data_new(entry_id:int) -> Optional[EntryRead]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.api_url}/crud/entry/{entry_id}")
        try:
            response.raise_for_status()
        except:
            return None
        entry = EntryRead.model_validate(response.json())
        return entry

async def get_entry_data(entry_id:int) -> Optional[EntryRead]:
    if entry_id < 0:
        return None
    if entry_id == 3:
        return None
    fake_question = QuestionRead(
        id = 0,
        title = "Fake Question",
        description = "Fake Question",
    )
    fake_answer = EntryAnswerRead(
        id = entry_id,
        question = fake_question,
        string_value = "Fake Answer",
    )
    fake_user = UserRead(
        id = entry_id,
        name = "Fake User",
        admin = False
    )
    fake_entry = EntryRead(
        id = entry_id,
        user = fake_user,
        answers = [fake_answer, fake_answer, fake_answer, fake_answer, fake_answer],
    )
    return fake_entry