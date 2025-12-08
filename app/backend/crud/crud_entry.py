from typing import Optional

from data.database import session
from models import Entry
from schemas.entry import EntryRead, EntryCreate, EntryUpdate, EntryReadOwner
from utils import secret_generator
from .base import CRUDHandler

class EntryCRUD(CRUDHandler[Entry, EntryRead, EntryCreate, EntryUpdate]):

    def __init__(self):
        super().__init__("entry", session, Entry, EntryRead, EntryCreate, EntryUpdate)

    def create(self, data: EntryCreate) -> EntryReadOwner:
        if not data.secret:
            data.secret = secret_generator.generate_secret()
        db_item = Entry(**data.model_dump())
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        return EntryReadOwner.model_validate(db_item)

    def get_admin(self, object_id: int) -> Optional[EntryReadOwner]:
        db_item = self.session.query(self.db_model).filter(self.db_model.id == object_id).first()
        if not db_item:
            return None
        return EntryReadOwner.model_validate(db_item)

handler: EntryCRUD = EntryCRUD()