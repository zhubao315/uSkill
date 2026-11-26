"""FastAPI application for the local Workbench UI.

All data comes from existing uSkill Core modules. This service never runs a
skill, never executes a skill script, and never writes to Agent directories
without an explicitly approved InstallPlan.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from core.uskills import __version__
from core.uskills.agents_hub import InstallScope, all_adapters
from core.uskills.registry import SkillRegistryV3
from core.uskills.runtime.state import RunStore

from .security import LocalAPIGuard


class StudioBuildRequest(BaseModel):
    source_text: str
    name: str = "source"


class StudioValidateRequest(BaseModel):
    skill_path: str


class EvalCompareRequest(BaseModel):
    current_report: str
    baseline_report: str


class InstallPreviewRequest(BaseModel):
    skill_path: str
    agent: str
    scope: str = "user"
    project: str = "."


def create_app(
    *,
    skills_root: str | Path = "skills",
    runs_dir: str | Path = ".uskills/runs",
    static_dir: str | Path | None = None,
    token: str = "",
) -> FastAPI:
    app = FastAPI(title="uSkill Workbench Local API", version=__version__)
    app.add_middleware(LocalAPIGuard, token=token)
    registry = SkillRegistryV3(skills_root)
    store = RunStore(runs_dir)

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        return {"status": "ok", "version": __version__, "skills": len(registry.all_records())}

    @app.get("/api/skills")
    def skills(
        query: str = "",
        category: str = "",
        source_type: str = "",
        status: str = "",
    ) -> dict[str, Any]:
        records = registry.search_records(
            query,
            category=category or None,
            source_type=source_type or None,
            status=status or None,
            limit=2000,
        )
        return {"skills": [r.to_dict() for r in records], "health": registry.health()}

    @app.get("/api/skills/{skill_id}")
    def skill_detail(skill_id: str) -> dict[str, Any]:
        record = registry.record(skill_id)
        if not record:
            raise HTTPException(404, f"unknown skill: {skill_id}")
        data = record.to_dict()
        skill_md = Path(registry.roots[0]) / record.path / "SKILL.md"
        if skill_md.exists():
            data["skill_md"] = skill_md.read_text(encoding="utf-8", errors="replace")
        return data

    @app.get("/api/agents")
    def agents(project: str = ".") -> list[dict[str, Any]]:
        out = []
        for adapter in all_adapters(project_root=Path(project)):
            out.append(
                {
                    "agent": adapter.name,
                    "detected": adapter.detect(),
                    "official_docs": adapter.official_docs,
                    "locations": [
                        {"scope": loc.scope.value, "path": str(loc.path), "priority": loc.priority}
                        for loc in adapter.list_skill_locations()
                    ],
                    "installed": [s.to_dict() for s in adapter.get_installed_skills()],
                }
            )
        return out

    @app.post("/api/install/preview")
    def install_preview(req: InstallPreviewRequest) -> dict[str, Any]:
        source = Path(req.skill_path)
        if not source.exists() or not (source / "SKILL.md").exists():
            raise HTTPException(400, "skill_path must be a directory containing SKILL.md")
        if req.scope not in {"user", "project"}:
            raise HTTPException(400, "invalid scope")
        adapter = next(
            (a for a in all_adapters(project_root=Path(req.project)) if a.name == req.agent), None
        )
        if not adapter:
            raise HTTPException(404, f"unknown agent: {req.agent}")
        plan = adapter.preview_install(source, InstallScope(req.scope))
        return plan.to_dict()

    @app.get("/api/runs")
    def runs() -> list[dict[str, Any]]:
        out = []
        for run_id in store.list_runs():
            try:
                record = store.load(run_id)
            except Exception:  # noqa: BLE001
                continue
            out.append(
                {
                    "run_id": record.run_id,
                    "skill_id": record.skill_id,
                    "status": record.status.value,
                    "started_at": record.started_at,
                    "finished_at": record.finished_at,
                    "execution_time": record.execution_time,
                }
            )
        return out

    @app.get("/api/runs/{run_id}")
    def run_detail(run_id: str) -> dict[str, Any]:
        try:
            return store.load(run_id).to_dict()
        except FileNotFoundError:
            raise HTTPException(404, f"unknown run: {run_id}") from None

    @app.post("/api/studio/build")
    def studio_build(req: StudioBuildRequest) -> dict[str, Any]:
        from .studio import build_studio_draft

        if not req.source_text.strip():
            raise HTTPException(400, "source_text is empty")
        return build_studio_draft(req.source_text, req.name)

    @app.post("/api/studio/validate")
    def studio_validate(req: StudioValidateRequest) -> dict[str, Any]:
        from .studio import validate_skill_path

        return validate_skill_path(req.skill_path)

    @app.get("/api/eval/suites")
    def eval_suites() -> list[dict[str, Any]]:
        from .studio import eval_catalog

        suites, _ = eval_catalog()
        return suites

    @app.get("/api/eval/reports")
    def eval_reports() -> list[dict[str, Any]]:
        from .studio import eval_catalog

        _, reports = eval_catalog()
        return reports

    @app.post("/api/eval/compare")
    def eval_compare(req: EvalCompareRequest) -> dict[str, Any]:
        from .studio import compare_eval_reports

        try:
            return compare_eval_reports(req.current_report, req.baseline_report)
        except FileNotFoundError as exc:
            raise HTTPException(404, str(exc)) from None

    # Serve built frontend at / (never intercept /api)
    if static_dir and Path(static_dir).is_dir():
        static_path = Path(static_dir)

        @app.get("/")
        def index() -> FileResponse:
            return FileResponse(static_path / "index.html")

        app.mount("/", StaticFiles(directory=static_path, html=True), name="workbench")

    return app


__all__ = ["create_app"]
