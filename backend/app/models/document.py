"""documents table (uploaded lecture PDFs)."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[int | None] = mapped_column(ForeignKey("courses.id", ondelete="SET NULL"), nullable=True, index=True)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(1024), nullable=False)
    extracted_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)

    course: Mapped["Course | None"] = relationship("Course", back_populates="documents")
    study_kit: Mapped["StudyKit | None"] = relationship("StudyKit", back_populates="document", cascade="all, delete-orphan", uselist=False)
    quiz_results: Mapped[list["QuizResult"]] = relationship("QuizResult", back_populates="document")
