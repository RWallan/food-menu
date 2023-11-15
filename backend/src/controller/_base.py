from typing import Generic, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class BaseCRUD(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def read(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def read_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, schema: CreateSchemaType) -> ModelType:
        created = self.model(**schema.model_dump())

        db.add(created)
        db.commit()
        db.refresh(created)

        return created
