from database import session
from models import Answer
from schemas.answer import AnswerRead, AnswerCreate, AnswerUpdate
from .base import CRUDHandler

class AnswerCRUD(CRUDHandler[Answer, AnswerRead, AnswerCreate, AnswerUpdate]):

    def __init__(self):
        super().__init__(session, Answer, AnswerRead, AnswerCreate, AnswerUpdate)

handler: AnswerCRUD = AnswerCRUD()