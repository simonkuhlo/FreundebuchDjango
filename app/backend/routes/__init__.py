from fastapi import APIRouter
from .crud import users, answers, entries, question_collections, questions

main_router = APIRouter(prefix="/api", tags=["api"])
main_router.include_router(users.router)
main_router.include_router(answers.router)
main_router.include_router(entries.router)
main_router.include_router(question_collections.router)
main_router.include_router(questions.router)
