"""All 9 Phase 0 tables exist with expected columns (SQLite in-memory)."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import *  # noqa: F401,F403
from app.models.base import Base


def test_all_tables_created():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    tables = set(Base.metadata.tables.keys())
    expected = {
        "users",
        "courses",
        "tasks",
        "sessions",
        "documents",
        "study_kits",
        "questions",
        "quiz_results",
        "chat_messages",
    }
    assert expected.issubset(tables), f"missing: {expected - tables}"
    # Spot-check key columns
    assert "password_hash" in Base.metadata.tables["users"].c
    assert "daily_hours" in Base.metadata.tables["users"].c
    assert "options" in Base.metadata.tables["questions"].c
    assert "extracted_text" in Base.metadata.tables["documents"].c
