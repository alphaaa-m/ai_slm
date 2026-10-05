"""Auth routes — TODO Phase 1: POST /auth/register, POST /auth/login."""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/_stub")
def stub_auth() -> dict:
    return {"todo": "Phase 1: register/login with hashed passwords + JWT"}
