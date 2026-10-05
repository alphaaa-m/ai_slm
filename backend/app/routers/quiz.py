"""Quiz + progress routes — TODO Phase 4: POST /quiz/submit, GET /progress."""
from fastapi import APIRouter

router = APIRouter(tags=["quiz"])


@router.get("/quiz/_stub")
def stub_quiz() -> dict:
    return {"todo": "Phase 4: MCQs with topic label, score per topic, <60% creates revision task"}
