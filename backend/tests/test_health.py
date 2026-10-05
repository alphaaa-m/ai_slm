"""Phase 0 smoke tests — no DB required."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_openapi_exposes_health():
    r = client.get("/openapi.json")
    assert r.status_code == 200
    assert "/health" in r.text
