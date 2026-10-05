"""tasks table.

type:     assignment | quiz | exam        (exam gets +5 planner bonus, see services/planner.py)
difficulty: 1..5
status:   pending | done | missed  (Phase 2 adds scheduled handling via sessions)
"""
from datetime import date as date_type
from datetime import datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False, default="assignment")
    due_date: Mapped[date_type | None] = mapped_column(Date, nullable=True)
    difficulty: Mapped[int] = mapped_column(Integer, nullable=False, default=3)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)

    course: Mapped["Course"] = relationship("Course", back_populates="tasks")
    sessions: Mapped[list["StudySession"]] = relationship("StudySession", back_populates="task", cascade="all, delete-orphan")
