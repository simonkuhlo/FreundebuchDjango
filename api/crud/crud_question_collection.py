from database import session
from models import QuestionCollection
from schemas.question_collection import QuestionCollectionRead, QuestionCollectionCreate, QuestionCollectionUpdate
from .base import CRUDHandler

class QuestionCollectionCRUD(CRUDHandler[QuestionCollection, QuestionCollectionRead, QuestionCollectionCreate, QuestionCollectionUpdate]):

    def __init__(self):
        super().__init__(session, QuestionCollection, QuestionCollectionRead, QuestionCollectionCreate, QuestionCollectionUpdate)

handler: QuestionCollectionCRUD = QuestionCollectionCRUD()