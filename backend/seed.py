"""Seed script — creates demo user + sample course/tasks.

Usage:
  py seed.py
Requires DATABASE_URL to point at a migrated DB (run `alembic upgrade head` first).
Idempotent: re-running will not duplicate the demo user.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from datetime import date, timedelta

from app.core.database import SessionLocal
from app.core.security import hash_password
from app.models import Course, Task, User

DEMO_EMAIL = "demo@studyos.local"
DEMO_PASSWORD = "demo1234"


def main() -> None:
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(email=DEMO_EMAIL).first()
        if user is None:
            user = User(email=DEMO_EMAIL, password_hash=hash_password(DEMO_PASSWORD), daily_hours=3.0)
            db.add(user)
            db.commit()
            db.refresh(user)
            print(f"created user {DEMO_EMAIL} / password {DEMO_PASSWORD}")
        else:
            print(f"user {DEMO_EMAIL} already exists (id={user.id})")

        if not user.courses:
            course = Course(user_id=user.id, name="CS101 — Intro to Computing")
            db.add(course)
            db.commit()
            db.refresh(course)
            today = date.today()
            samples = [
                ("Assignment 1 — Python basics", "assignment", today + timedelta(days=1), 3),
                ("Quiz 2 — SQL joins", "quiz", today + timedelta(days=2), 2),
                ("Midterm exam", "exam", today + timedelta(days=5), 5),
            ]
            for title, kind, due, diff in samples:
                db.add(Task(course_id=course.id, title=title, type=kind, due_date=due, difficulty=diff, status="pending"))
            db.commit()
            print("created sample course + 3 tasks")
        else:
            print("sample data already present")
    finally:
        db.close()


if __name__ == "__main__":
    main()
