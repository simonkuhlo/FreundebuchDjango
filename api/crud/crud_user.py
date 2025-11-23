from database import session
from models import User
from schemas.user import UserRead, UserCreate, UserUpdate
from .base import CRUDHandler

class UserCRUD(CRUDHandler[User, UserRead, UserCreate, UserUpdate]):

    def __init__(self):
        super().__init__(session, User, UserRead, UserCreate, UserUpdate)

handler: UserCRUD = UserCRUD()