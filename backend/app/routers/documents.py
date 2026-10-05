"""Document upload + study-kit routes — TODO Phase 3."""
from fastapi import APIRouter

router = APIRouter(tags=["documents"])


@router.get("/documents/_stub")
def stub_documents() -> dict:
    return {"todo": "Phase 3: PDF upload (10MB limit), PyMuPDF extract, LLM kit via services/ai.py"}
