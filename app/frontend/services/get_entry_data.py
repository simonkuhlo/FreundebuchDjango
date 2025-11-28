from typing import Optional
from api.schemas.entry import EntryRead
from api.schemas.answer import AnswerRead, EntryAnswerRead
from api.schemas.question import QuestionRead
from api.schemas.user import UserRead

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