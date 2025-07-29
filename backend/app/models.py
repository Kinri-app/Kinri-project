# setting up models to create tables in database

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Text, DateTime, Integer, JSON, Float
from datetime import date
from typing import List
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

# TODO: Need foreign keys to tie data. Add tables to ERD and complete flow

class Flashcard(Base):
    __tablename__="flashcard"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[str] = mapped_column(String(350), nullable=False)
    question: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)
    answer: Mapped[str] = mapped_column(String(350), nullable=False)
    condition: Mapped[str] = mapped_column(String(150))
    emotion: Mapped[str] = mapped_column(String(350))
    narrative_type: Mapped[str] = mapped_column(String(350))
    usage_mode: Mapped[str] = mapped_column(String(350))


class Vaultcard(Base):
    __tablename__="vaultcard"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)
    headline: Mapped[str] = mapped_column(String(350))
    body: Mapped[str] = mapped_column(String(350), nullable=False)
    prompt: Mapped[str] = mapped_column(String(150), nullable=False)
    tags: Mapped[str] = mapped_column(String(150), nullable=False)
    emotion: Mapped[str] = mapped_column(String(150))
    narrative_type: Mapped[str] = mapped_column(String(150), nullable=False)
    usage_mode: Mapped[str] = mapped_column(String(150), nullable=False)

class AssessmentQuestion(Base):
    __tablename__="assessment_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)
    conditions: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)

class Conversation(Base):
    __tablename__ = "conversation"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    messages: Mapped[List["Message"]] = relationship(back_populates="conversation", cascade="all, delete-orphan") #delete-orphan will delete all child entries once parent is deleted


class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversation.id"), nullable=False)
    role: Mapped[str] = mapped_column(String(10), nullable=False)  # 'user' or 'assistant'
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")

class User(Base):
    __tablename__="user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(150), nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    location: Mapped[str] = mapped_column(String(250))
    current_emotion: Mapped[str] = mapped_column(String(100))
    last_emotion: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)) #Using lambda so this is recorded when the row is created
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    

    assessments: Mapped[list["AssessmentResult"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class AssessmentResult(Base):
    __tablename__ = "assessment_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    results: Mapped[dict] = mapped_column(JSON, nullable=False)  # store the JSON structure here
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user: Mapped["User"] = relationship(back_populates="assessments")

class Condition(Base):
    __tablename__ = "conditions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    weights: Mapped[List["QuestionConditionWeight"]] = relationship(back_populates="condition") #


class AssessmentQuestion(Base):
    __tablename__ = "assessment_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)

    condition_weights: Mapped[List["QuestionConditionWeight"]] = relationship(back_populates="question", cascade="all, delete-orphan")


class QuestionConditionWeight(Base):
    __tablename__ = "question_condition_weights"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("assessment_questions.id"), nullable=False)
    condition_id: Mapped[int] = mapped_column(ForeignKey("conditions.id"), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)

    question: Mapped["AssessmentQuestion"] = relationship(back_populates="condition_weights")
    condition: Mapped["Condition"] = relationship(back_populates="weights")


class UserSessions(Base):
    __tablename__ = "user_sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    conversation: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    associate_vault_card_id: Mapped[int] = mapped_column(ForeignKey("vaultcard.id"))

    user_vault_card: Mapped["Vaultcard"] = relationship(back_populates="vaultcard")
    user_session: Mapped["User"] = relationship(back_populates="user")

