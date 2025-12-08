from typing import Annotated

from fastapi import Form

from .crud_handler_router import CRUDHandlerRouter
from fastapi.requests import Request
from crud import question
from schemas.question import QuestionUpdate

router = CRUDHandlerRouter(question)

@router.put("/from_form/{question_id}")
async def create_otp(request: Request, question_id: int, new_question: Annotated[QuestionUpdate, Form()]):
    updated_question = question.update(question_id, new_question)
    return updated_question