"""Planner scoring — STUB for Phase 0, implemented in Phase 2.

PRD formula (keep exactly):
    score = (difficulty x 2) + (10 - days_until_due)
    exams get +5 bonus. Higher score is scheduled first.

Phase 2 will add: generate_weekly_plan(tasks, daily_hours) -> sessions.
"""
from datetime import date


def priority_score(difficulty: int, due_date: date | None, kind: str = "assignment", today: date | None = None) -> float:
    """TODO(Phase 2): implement the PRD formula. Stub returns 0 for now."""
    raise NotImplementedError("Phase 2: implement priority_score per PRD formula")
