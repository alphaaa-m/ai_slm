"""Auth helpers — STUB for Phase 0, implemented in Phase 1.

Phase 1 will implement:
  - pwd_context.hash / verify (bcrypt)
  - create_access_token (PyJWT, HS256)
  - get_current_user dependency (reads Bearer token, loads user)

Kept here so imports already work for routers written later.
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# TODO(Phase 1): create_access_token(data: dict) -> str
# TODO(Phase 1): get_current_user dependency using PyJWT + settings.JWT_SECRET_KEY
