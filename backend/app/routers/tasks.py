"""Course + task CRUD — TODO Phase 1: GET/POST /tasks, PUT/DELETE /tasks/{id}."""
from fastapi import APIRouter

router = APIRouter(tags=["tasks"])


@router.get("/tasks/_stub")
def stub_tasks() -> dict:
    return {"todo": "Phase 1: courses + tasks CRUD, only the user's own data"}
