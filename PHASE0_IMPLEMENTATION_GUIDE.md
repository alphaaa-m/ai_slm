# Phase 0 Implementation Guide — what was built and why

## Scope covered (plan §3, items 0.1–0.8)

| # | Deliverable | Where | Verify |
|---|---|---|---|
| 0.1 | Repo skeleton, README, .gitignore, .env.example | root, `backend/`, `frontend/` | clone → follow README |
| 0.2 | Postgres via Docker Compose | `docker-compose.yml` (pg16, volume, healthcheck) | `docker compose up -d` |
| 0.3 | All 9 tables as SQLAlchemy models | `backend/app/models/*.py` | `pytest tests/test_models.py` |
| 0.4 | Alembic + initial migration | `backend/alembic.ini`, `alembic/env.py`, `versions/0001_phase0_initial.py` | `alembic upgrade head` |
| 0.5 | FastAPI skeleton | `app/main.py`, `core/`, `routers/`, `services/`, `schemas/` | `/docs`, `/health` |
| 0.6 | Next.js skeleton | `frontend/app/*`, `lib/api.ts`, `components/` | `npm run dev` |
| 0.7 | Seed script | `backend/seed.py` | `py seed.py` (idempotent) |
| 0.8 | Handover doc | `PHASE0_HANDOVER.md` | student runs alone |

## .env requirements (full reference)

### Backend (`backend/.env` — copy from root `.env.example`)

| Var | Required in | Default | Notes |
|---|---|---|---|
| `DATABASE_URL` | Phase 0 | `postgresql+psycopg2://postgres:postgres@localhost:5432/aistudyos` | Docker Compose values must match. Inside Docker network use host `db`. |
| `JWT_SECRET_KEY` | Phase 1 | `change-me-...` | Generate: `py -c "import secrets; print(secrets.token_urlsafe(32))"`. Never commit. |
| `JWT_ALGORITHM` | Phase 1 | `HS256` | Keep default. |
| `JWT_EXPIRE_MINUTES` | Phase 1 | `10080` | 7 days. |
| `APP_ENV` | Phase 0 | `development` | Returned by `/health`; set `production` on Render/Railway. |
| `APP_NAME` | Phase 0 | `AI StudyOS` | OpenAPI title. |
| `BACKEND_CORS_ORIGINS` | Phase 0 | `http://localhost:3000` | Comma-separated; must include Vercel URL in prod. |
| `UPLOAD_DIR` | Phase 3 | `./uploads` | Created on demand; mount a volume in prod. |
| `MAX_UPLOAD_MB` | Phase 3 | `10` | PRD limit; enforced in upload endpoint. |
| `LLM_PROVIDER` | Phase 3 | `openai` | One of `openai|gemini|anthropic`. |
| `LLM_MODEL` | Phase 3 | `gpt-4o-mini` | Free-tier default. |
| `OPENAI_API_KEY` / `GOOGLE_API_KEY` / `ANTHROPIC_API_KEY` | Phase 3 | empty | Fill only the one you use. Key stays server-side. |

### Frontend (`frontend/.env.local` — copy from `frontend/.env.example`)

| Var | Required in | Default | Notes |
|---|---|---|---|
| `NEXT_PUBLIC_API_URL` | Phase 0 | `http://localhost:8000` | No trailing slash. `NEXT_PUBLIC_` prefix exposes it to the browser — never put secrets here. |

## Key decisions

1. **Sync SQLAlchemy + psycopg2 (not async).** Keeps `get_db` dependency and Alembic trivial for a student; async adds no MVP value.
2. **Integer PKs, not UUIDs.** Simpler URLs (`/tasks/3`), simpler forms, matches student level.
3. **JSON columns for concepts/flashcards/options.** Avoids 3 extra tables; `JSONB` variant on Postgres, plain JSON on SQLite tests.
4. **`course_id` nullable on documents.** Allows uploads before a course exists; FK is SET NULL so deleting a course keeps the file.
5. **`study_kits.document_id` UNIQUE.** Enforces one-kit-per-document at the DB level (PRD §6.1 saves one kit per upload).
6. **Stubs, not empty dirs.** Every future router/service exists with a `_stub` route + TODO so imports/wiring already work and the student replaces bodies.
7. **Two health endpoints.** `/health` needs no DB (proves the app boots); `/health/db` runs `SELECT 1` (proves wiring). Tests only hit the former so CI needs no Postgres.
8. **Seed is idempotent.** Lookup by email before insert; safe to run twice — required for the M0 demo.

## What was intentionally left for later

- Phase 1: real auth (JWT issue/verify, `get_current_user`), schemas per model, ownership filters.
- Phase 2: `priority_score` formula + `generate_weekly_plan`.
- Phase 3: `extract_text` (PyMuPDF), `generate_study_kit` (strict JSON + 1 retry), `BackgroundTasks`.
- Phase 4: quiz submit + `/progress` aggregation + <60% revision-task loop.
- Phase 5: `/tutor/chat` mode templates + context trimming.
- Phase 6: Recharts, Vercel/Render deploy, full test suite (LLM mocked).

## Verification log (mentor run, 2026-10-05)

- `py -m pytest -q` — 3 passed (`test_health_ok`, `test_openapi_exposes_health`, `test_all_tables_created`; models use SQLite in-memory, API via TestClient — no live DB needed).
- `npx tsc --noEmit` — exit 0. `npm run build` — Next 14.2.35, 9 routes compiled (/, /login, /register, /planner, /documents, /kits/[id], /tutor, /progress).
- `alembic history` — `<base> -> 0001_phase0 (head)`. `alembic upgrade head` requires a reachable Postgres with the correct password in `DATABASE_URL`; on this machine the local PG password differed from the `postgres/postgres` default, so `upgrade`/`check` correctly failed with `password authentication failed` until `DATABASE_URL` is set — this is the expected student setup step, not a code bug.
- `/health` needs no DB; `/health/db` runs `SELECT 1` to confirm wiring once the DB is up.
