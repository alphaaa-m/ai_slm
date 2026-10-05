"""study_kits table (one row per document, JSON columns keep schema small)."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

# JSONB on Postgres, plain JSON elsewhere (e.g. tests on SQLite).
JSONType = JSON().with_variant(JSONB(), "postgresql")


class StudyKit(Base):
    __tablename__ = "study_kits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    summary: Mapped[str] = mapped_column(Text, nullable=False, default="")
    concepts: Mapped[list | dict] = mapped_column(JSONType, nullable=False, default=list)
    flashcards: Mapped[list | dict] = mapped_column(JSONType, nullable=False, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)

    document: Mapped["Document"] = relationship("Document", back_populates="study_kit")
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="kit", cascade="all, delete-orphan")
