# setting up models to create tables in database

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from typing import List

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# TODO: Need foreign keys to tie data. Add tables to ERD and complete flow

class Flashcard(Base):
    __tablename__="flashcard"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[str] = mapped_column(db.String(350), unique=True, nullable=False)
    question: Mapped[str] = mapped_column(db.String(350), unique=True, nullable=False)
    answer: Mapped[str] = mapped_column(db.String(350), nullable=False)
    tags: Mapped[str] = mapped_column(db.String(150), nullable=False)
    emotion: Mapped[str] = mapped_column(db.String(150))
    narrative_type: Mapped[str] = mapped_column(db.String(150), nullable=False)
    usage_mode: Mapped[str] = mapped_column(db.String(150), nullable=False)

class Vaultcard(Base):
    __tablename__="vaultcard"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[str] = mapped_column(db.String(350), unique=True, nullable=False)
    headline: Mapped[str] = mapped_column(db.String(350), nullable=False)
    body: Mapped[str] = mapped_column(db.String(350), nullable=False)
    prompt: Mapped[str] = mapped_column(db.String(150), nullable=False)
    tags: Mapped[str] = mapped_column(db.String(150), nullable=False)
    emotion: Mapped[str] = mapped_column(db.String(150))
    narrative_type: Mapped[str] = mapped_column(db.String(150), nullable=False)
    usage_mode: Mapped[str] = mapped_column(db.String(150), nullable=False)

class AssessmentQuestion(Base):
    __tablename__="assessment_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(db.String(350), unique=True, nullable=False)
    conditions: Mapped[str] = mapped_column(db.String(350), unique=True, nullable=False)


