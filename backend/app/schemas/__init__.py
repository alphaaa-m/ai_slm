"""Pydantic schemas — STUDENT FILLS IN from Phase 1 onward.

Phase 0 only ships a shared health/error envelope so the pattern is clear.
Each router will gain its own schema file, e.g.:
  schemas/auth.py, schemas/course.py, schemas/task.py, ...
"""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app: str
    env: str
