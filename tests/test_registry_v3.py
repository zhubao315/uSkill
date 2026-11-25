"""Tests for unified Registry 3.0 discovery (add as tests/test_registry_v3.py)."""

from __future__ import annotations

import json
from pathlib import Path

from core.uskills.registry import SkillRecord, SkillRegistryV3


def _make_skill_dir(
    root: Path, name: str, description: str, *, frontmatter_extra: str = ""
) -> Path:
    d = root / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n{frontmatter_extra}---\n\n# Body\n\nInstructions.\n",
        encoding="utf-8",
    )
    return d


def test_discovers_pure_agent_skill_dir(tmp_path: Path) -> None:
    _make_skill_dir(tmp_path, "code-review", "Review code for quality")
    registry = SkillRegistryV3(tmp_path)
    records = registry.all_records()
    assert len(records) == 1
    assert records[0].format == "agent-skill"
    assert records[0].name == "code-review"
    assert records[0].content_hash


def test_discovers_two_layer_skill(tmp_path: Path) -> None:
    d = _make_skill_dir(tmp_path, "two-layer", "Layered skill")
    (d / "uskill.yaml").write_text(
        "apiVersion: uskills/v2\nkind: Skill\nmetadata:\n  name: two-layer\n", encoding="utf-8"
    )
    registry = SkillRegistryV3(tmp_path)
    assert any(r.format == "agent-skill+manifest" for r in registry.all_records())


def test_invalid_frontmatter_is_reported(tmp_path: Path) -> None:
    d = tmp_path / "bad"
    d.mkdir()
    (d / "SKILL.md").write_text("not frontmatter\n", encoding="utf-8")
    registry = SkillRegistryV3(tmp_path)
    assert registry.health()["ok"] is False
    assert registry.broken


def test_search_modes(tmp_path: Path) -> None:
    _make_skill_dir(tmp_path, "text-summarize", "Summarize long Chinese text")
    registry = SkillRegistryV3(tmp_path)
    assert registry.search_records("summarize", mode="name")
    assert registry.search_records("Chinese", mode="keyword")
    assert registry.search_records("agent-skill", mode="format")


def test_duplicate_detection(tmp_path: Path) -> None:
    a = _make_skill_dir(tmp_path, "alpha", "Same content")
    b = _make_skill_dir(tmp_path, "beta", "Same content")
    (b / "SKILL.md").write_bytes((a / "SKILL.md").read_bytes())
    registry = SkillRegistryV3(tmp_path)
    assert registry.duplicates  # identical SKILL.md hash


def test_same_name_different_content_conflict(tmp_path: Path) -> None:
    _make_skill_dir(tmp_path, "dup-name", "First version", frontmatter_extra="version: '1.0'\n")
    d = tmp_path / "other"
    d.mkdir()
    (d / "SKILL.md").write_text(
        "---\nname: dup-name\ndescription: Second version\nversion: '2.0'\n---\n\n# Body\n\nDifferent.\n",
        encoding="utf-8",
    )
    registry = SkillRegistryV3(tmp_path)
    assert any("same name" in b.get("error", "") for b in registry.broken)


def test_report_is_machine_readable(tmp_path: Path) -> None:
    _make_skill_dir(tmp_path, "report-test", "Report test skill")
    registry = SkillRegistryV3(tmp_path)
    report = registry.report()
    encoded = json.dumps(report, ensure_ascii=False)
    assert "report-test" in encoded
    assert report["health"]["skills"] >= 1


def test_extra_roots(tmp_path: Path) -> None:
    a = tmp_path / "a"
    b = tmp_path / "b"
    _make_skill_dir(a, "skill-a", "From A")
    _make_skill_dir(b, "skill-b", "From B")
    registry = SkillRegistryV3(a, extra_roots=[b])
    names = {r.name for r in registry.all_records()}
    assert {"skill-a", "skill-b"} <= names


def test_skill_record_to_dict_shape(tmp_path: Path) -> None:
    record = SkillRecord(
        skill_id="x",
        name="X",
        description="D",
        format="agent-skill",
        path="x/SKILL.md",
    )
    d = record.to_dict()
    for key in ("skill_id", "name", "format", "content_hash", "risk_level", "lifecycle_status"):
        assert key in d
