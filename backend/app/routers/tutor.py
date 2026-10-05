"""AI tutor routes — TODO Phase 5: POST /tutor/chat with mode + optional document_id."""
from fastapi import APIRouter

router = APIRouter(prefix="/tutor", tags=["tutor"])


@router.get("/_stub")
def stub_tutor() -> dict:
    return {"todo": "Phase 5: 4 mode templates (Beginner/Exam/Example/Quick Revision)"}
