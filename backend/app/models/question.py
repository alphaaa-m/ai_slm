"""questions table (MCQs belonging to a study kit)."""
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

JSONType = JSON().with_variant(JSONB(), "postgresql")


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    kit_id: Mapped[int] = mapped_column(ForeignKey("study_kits.id", ondelete="CASCADE"), nullable=False, index=True)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    options: Mapped[list] = mapped_column(JSONType, nullable=False, default=list)
    answer: Mapped[str] = mapped_column(String(500), nullable=False)
    topic: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)

    kit: Mapped["StudyKit"] = relationship("StudyKit", back_populates="questions")
