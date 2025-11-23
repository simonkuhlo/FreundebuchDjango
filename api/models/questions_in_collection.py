from sqlalchemy import Column
from sqlalchemy import Table
from models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

association_table = Table("collection_has_questions",
                          Base.metadata,
                          Column("collection_id", Integer, ForeignKey("question_collection.id")),
                          Column("question_id", Integer, ForeignKey("question.id"))
                          )