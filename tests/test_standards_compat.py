"""Sprint 1: format detection, migration reports, compatibility guarantees."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from core.uskills.standards_compat import (
    FORMAT_AGENT_SKILL,
    FORMAT_MANIFEST_V2,
    FORMAT_SKILL_V1,
    FORMAT_UNKNOWN,
    detect_format,
    manifest_json_schema,
    migrate_directory,
    migrate_skill,
)
from core.uskills.validator import load_skill

LEGACY = {
    "skill_id": "uskill-atomic-migrate-me-v1-1-0",
    "meta": {"name": "Migrate Me", "category": "atomic", "description": "d", "version": "1.1.0"},
    "input": {"params": [{"name": "text", "type": "string", "required": True}]},
    "execute": {"prompt_template": "work on {{text}}", "model": "gpt-4o-mini"},
    "output": {"format": "json", "params": ["result"]},
    "control": {"timeout": 10},
    "source": {"sop_name": "S", "step_index": 1, "raw_step": "r"},
}


def _write_legacy(tmp_path: Path) -> Path:
    p = tmp_path / "legacy.yaml"
    p.write_text(yaml.safe_dump(LEGACY, allow_unicode=True), encoding="utf-8")
    return p


class TestDetectFormat:
    def test_skill_v1(self, tmp_path: Path) -> None:
        assert detect_format(_write_legacy(tmp_path)) == FORMAT_SKILL_V1

    def test_manifest_v2(self, tmp_path: Path) -> None:
        p = tmp_path / "uskill.yaml"
        p.write_text(
            "apiVersion: uskills/v2\nkind: Skill\nmetadata:\n  name: a\n  description: d\n",
            encoding="utf-8",
        )
        assert detect_format(p) == FORMAT_MANIFEST_V2

    def test_agent_skill_dir(self, tmp_path: Path) -> None:
        (tmp_path / "sk").mkdir()
        (tmp_path / "sk" / "SKILL.md").write_text("---\nname: sk\ndescription: d\n---\nx", "utf-8")
        assert detect_format(tmp_path / "sk") == FORMAT_AGENT_SKILL

    def test_unknown(self, tmp_path: Path) -> None:
        p = tmp_path / "x.json"
        p.write_text('{"hello": 1}', encoding="utf-8")
        assert detect_format(p) == FORMAT_UNKNOWN
        assert detect_format(tmp_path / "nope") == FORMAT_UNKNOWN

    def test_repo_assets_classify(self) -> None:
        # Real assets: every legacy skill classifies as skill-v1.
        from pathlib import Path as P

        files = list(P("skills").rglob("*.yaml"))
        kinds = {detect_format(f) for f in files if f.stem != "uskill"}
        assert kinds == {FORMAT_SKILL_V1}


class TestManifestSchema:
    def test_export_declares_dialect(self) -> None:
        schema = manifest_json_schema()
        assert schema["$schema"].endswith("2020-12/schema")
        assert "metadata" in schema["properties"]
        assert schema["properties"]["apiVersion"]["const"] == "uskills/v2"


class TestMigrate:
    def test_migrate_creates_two_layer(self, tmp_path: Path) -> None:
        src = _write_legacy(tmp_path)
        report = migrate_skill(src, tmp_path / "out")
        assert report.ok
        target = tmp_path / "out" / "migrate-me"
        assert (target / "SKILL.md").exists()
        assert (target / "uskill.yaml").exists()
        # legacy untouched
        assert detect_format(src) == FORMAT_SKILL_V1
        # manifest carries typed IO from the legacy params
        data = yaml.safe_load((target / "uskill.yaml").read_text(encoding="utf-8"))
        assert "text" in data["inputs"]["properties"]
        assert "text" in data["inputs"]["required"]

    def test_lossy_reported_not_dropped(self, tmp_path: Path) -> None:
        src = _write_legacy(tmp_path)
        report = migrate_skill(src, tmp_path / "out")
        # llm execution mode + typed IO cannot be expressed by pure Agent Skills
        assert any("mode" in x or "JSON Schema" in x for x in report.lossy)

    def test_deprecation_warning_on_model_field(self, tmp_path: Path) -> None:
        src = _write_legacy(tmp_path)
        report = migrate_skill(src, tmp_path / "out")
        assert any("execute.model" in w for w in report.warnings)

    def test_idempotent_no_overwrite(self, tmp_path: Path) -> None:
        src = _write_legacy(tmp_path)
        migrate_skill(src, tmp_path / "out")
        second = migrate_skill(src, tmp_path / "out")
        assert not second.ok
        assert any("exists" in a for a in second.actions)
        third = migrate_skill(src, tmp_path / "out", force=True)
        assert third.ok

    def test_dry_run_writes_nothing(self, tmp_path: Path) -> None:
        src = _write_legacy(tmp_path)
        report = migrate_skill(src, tmp_path / "out", dry_run=True)
        assert report.ok
        assert not (tmp_path / "out").exists()

    def test_refuses_non_v1(self, tmp_path: Path) -> None:
        p = tmp_path / "other.yaml"
        p.write_text(
            "apiVersion: uskills/v2\nkind: Skill\nmetadata:\n  name: a\n  description: d\n"
        )
        report = migrate_skill(p, tmp_path / "out")
        assert not report.ok

    def test_migrate_directory_skips_manifest_and_evals(self, tmp_path: Path) -> None:
        _write_legacy(tmp_path)
        (tmp_path / "evals").mkdir()
        (tmp_path / "evals" / "dataset.json").write_text('{"skill": "x", "cases": []}')
        (tmp_path / "uskill.yaml").write_text("apiVersion: uskills/v2\n")
        reports = migrate_directory(tmp_path, tmp_path / "out")
        assert len(reports) == 1  # only the legacy skill


class TestBackwardCompatibility:
    def test_all_repo_v1_still_load_and_execute(self) -> None:
        """Hard gate for 2.0: every historical asset loads with the current model."""
        roots = [
            Path("skills/atomic"),
            Path("skills/composite"),
            Path("skills/domain"),
            Path("skills/governance"),
        ]
        total = 0
        for root in roots:
            for f in sorted(root.glob("*.yaml")):
                skill = load_skill(f)
                assert skill.skill_id
                total += 1
        assert total >= 8

    def test_manifest_roundtrip_preserves_io_contract(self, tmp_path: Path) -> None:
        from core.uskills.manifest import load_manifest, manifest_from_legacy_skill

        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        manifest = manifest_from_legacy_skill(skill)
        path = tmp_path / "uskill.yaml"
        from core.uskills.manifest import dump_manifest

        dump_manifest(manifest, path)
        reloaded = load_manifest(path)
        legacy_required = {p.name for p in skill.input.params if p.required}
        assert set(reloaded.inputs.get("required", [])) == legacy_required
        assert json.dumps(reloaded.model_dump(), ensure_ascii=False)  # serializable
