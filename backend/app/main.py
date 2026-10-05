"""FastAPI app factory + router wiring."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import auth, documents, health, plan, quiz, tasks, tutor


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, version="0.1.0-phase0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Real routes (Phase 0)
    app.include_router(health.router)

    # Stubs (student implements Phase 1-5)
    app.include_router(auth.router)
    app.include_router(tasks.router)
    app.include_router(plan.router)
    app.include_router(documents.router)
    app.include_router(quiz.router)
    app.include_router(tutor.router)

    return app


app = create_app()
