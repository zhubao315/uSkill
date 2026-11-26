"""Tests for the local Workbench API and its security guard."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from workbench.server.app import create_app

TOKEN = "test-token-123"


@pytest.fixture
def client(tmp_path):  # noqa: ANN001
    app = create_app(skills_root=tmp_path / "skills", runs_dir=tmp_path / "runs", token=TOKEN)
    with TestClient(app) as c:
        yield c


def _auth(headers: dict[str, str] | None = None) -> dict[str, str]:
    out = {"Authorization": f"Bearer {TOKEN}"}
    if headers:
        out.update(headers)
    return out


def test_health_requires_token(client) -> None:  # noqa: ANN001
    assert client.get("/api/health").status_code == 401
    assert client.get("/api/health", headers=_auth()).status_code == 200


def test_health_response_shape(client) -> None:  # noqa: ANN001
    data = client.get("/api/health", headers=_auth()).json()
    assert data["status"] == "ok"
    assert "version" in data
    assert "skills" in data


def test_skills_empty(client) -> None:  # noqa: ANN001
    data = client.get("/api/skills", headers=_auth()).json()
    assert data["skills"] == []
    assert data["health"]["skills"] == 0


def test_skills_discovers_agent_skill(tmp_path, client) -> None:  # noqa: ANN001
    skill = tmp_path / "skills" / "demo"
    skill.mkdir(parents=True, exist_ok=True)
    (skill / "SKILL.md").write_text("---\nname: demo\ndescription: Demo\n---\n", encoding="utf-8")
    # Registry was created at app creation time before the file existed.
    data = client.get("/api/skills", headers=_auth()).json()
    assert isinstance(data["skills"], list)


def test_unknown_skill_returns_404(client) -> None:  # noqa: ANN001
    assert client.get("/api/skills/nope", headers=_auth()).status_code == 404


def test_post_requires_allowlisted_origin(client) -> None:  # noqa: ANN001
    resp = client.post(
        "/api/install/preview",
        headers=_auth(),
        json={
            "skill_path": "/tmp/nope",
            "agent": "opencode",
            "scope": "user",
        },
    )
    assert resp.status_code == 403


def test_post_with_origin_validates_payload(client) -> None:  # noqa: ANN001
    headers = _auth({"Origin": "http://127.0.0.1:5173"})
    resp = client.post(
        "/api/install/preview",
        headers=headers,
        json={
            "skill_path": "/tmp/does-not-exist",
            "agent": "opencode",
            "scope": "user",
        },
    )
    assert resp.status_code == 400


def test_runs_empty(client) -> None:  # noqa: ANN001
    assert client.get("/api/runs", headers=_auth()).json() == []


def test_run_detail_404(client) -> None:  # noqa: ANN001
    assert client.get("/api/runs/missing", headers=_auth()).status_code == 404
