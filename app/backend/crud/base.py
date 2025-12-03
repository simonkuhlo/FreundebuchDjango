from fastapi import HTTPException
from typing import Type, TypeVar, Generic, Optional, List
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.base import Base

ModelType = TypeVar("ModelType", bound=Base)
ReadSchema = TypeVar("ReadSchema", bound=BaseModel)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)

class CRUDHandler(Generic[ModelType, ReadSchema, CreateSchema, UpdateSchema]):
    def __init__(self,
                 name: str,
                 session: Session,
                 db_model: Type[ModelType],
                 read_schema: Type[ReadSchema],
                 create_schema: Type[CreateSchema],
                 update_schema: Type[UpdateSchema]
                 ):
        self.name = name
        self.session = session
        self.db_model = db_model
        self.read_schema = read_schema
        self.create_schema = create_schema
        self.update_schema = update_schema

    def list(self, start_id: Optional[int] = 0, limit: Optional[int] = 100) -> Optional[List[ReadSchema]]:
        statement = select(self.db_model).offset(start_id).limit(limit)
        read_object_list = []
        for db_item in self.session.scalars(statement):
            print(db_item)
            read_object_list.append(self.read_schema.model_validate(db_item))
        return read_object_list

    def get(self, object_id: int, raise_exceptions: bool = True) -> Optional[ReadSchema]:
        db_item = self.session.query(self.db_model).filter(self.db_model.id == object_id).first()
        if not db_item:
            if raise_exceptions:
                raise HTTPException(404, "Object not found")
            else:
                return None
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
            raise HTTPException(404, "Object not found")
        update_data = updated_object.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        self.session.commit()
        self.session.refresh(db_item)
        return self.read_schema.model_validate(db_item)

    def delete(self, object_id: int) -> None:
        self.session.query(self.db_model).filter(self.db_model.id == object_id).delete()
        self.session.commit()
