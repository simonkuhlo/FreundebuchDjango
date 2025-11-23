from typing import Type, TypeVar, Generic, Optional, List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.base import Base  # Your SQLAlchemy Base

ModelType = TypeVar("ModelType", bound=Base)
ReadSchema = TypeVar("ReadSchema", bound=BaseModel)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)

class CRUDHandler(Generic[ModelType, ReadSchema, CreateSchema, UpdateSchema]):
    def __init__(self, session: Session, db_model: Type[ModelType],
                 read_schema: Type[ReadSchema],
                 create_schema: Type[CreateSchema],
                 update_schema: Type[UpdateSchema]):
        self.session = session
        self.db_model = db_model
        self.read_schema = read_schema
        self.create_schema = create_schema
        self.update_schema = update_schema

    def list(self) -> Optional[List[ReadSchema]]:
        # Implementation here...
        raise NotImplementedError

    def get(self, object_id: int) -> Optional[ReadSchema]:
        db_item = self.session.query(self.db_model).filter(self.db_model.id == object_id).first()
        if not db_item:
            raise Exception("Object not found")  # Replace with your HTTPException
        return self.read_schema.model_validate(db_item)

    def create(self, new_object: CreateSchema) -> ReadSchema:
        db_item = self.db_model(**new_object.model_dump())
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        return self.read_schema.model_validate(db_item)

    def update(self, object_id: int, updated_object: UpdateSchema) -> ReadSchema:
        db_item = self.session.query(self.db_model).filter(self.db_model.id == object_id).first()
        if not db_item:
            raise Exception("Object not found")  # Replace with your HTTPException
        update_data = updated_object.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        self.session.commit()
        self.session.refresh(db_item)
        return self.read_schema.model_validate(db_item)

    def delete(self, object_id: int) -> None:
        self.session.query(self.db_model).filter(self.db_model.id == object_id).delete()
        self.session.commit()
