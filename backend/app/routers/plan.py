"""Planner routes — TODO Phase 2: POST /plan/generate, GET /plan, PATCH /sessions/{id}."""
from fastapi import APIRouter

router = APIRouter(tags=["plan"])


@router.get("/plan/_stub")
def stub_plan() -> dict:
    return {"todo": "Phase 2: priority scoring + weekly schedule in services/planner.py"}
