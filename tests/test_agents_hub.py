"""Tests for Agent Install Hub adapters (3.0 Phase 2).

All tests use temporary directories and NEVER touch real Agent skill dirs.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from core.uskills.agents_hub import (
    ClaudeCodeAdapter,
    CodexAdapter,
    InstallScope,
    OpenCodeAdapter,
    all_adapters,
)


def _skill(root: Path, name: str = "demo-skill") -> Path:
    d = root / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Test skill\n---\n\n# Body\n",
        encoding="utf-8",
    )
    return d


def test_adapters_detect_paths_from_temp_home(tmp_path: Path) -> None:
    home = tmp_path / "home"
    project = tmp_path / "project"
    for adapter in all_adapters(home=home, project_root=project):
        locations = adapter.list_skill_locations()
        assert locations
        assert all(isinstance(loc.path, Path) for loc in locations)


def test_codex_uses_codex_home_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CODEX_HOME", str(tmp_path / "custom-codex"))
    adapter = CodexAdapter(home=tmp_path / "home", project_root=tmp_path / "proj")
    paths = [loc.path for loc in adapter.list_skill_locations()]
    assert tmp_path / "custom-codex" / "skills" in paths


def test_preview_install_never_writes(tmp_path: Path) -> None:
    source = _skill(tmp_path / "src")
    home = tmp_path / "home"
    (home / ".opencode" / "skills").mkdir(parents=True)
    adapter = OpenCodeAdapter(home=home, project_root=tmp_path / "proj")
    plan = adapter.preview_install(source, InstallScope.USER)
    assert plan.actions
    assert not plan.conflicts
    # target must NOT exist yet
    assert not list((home / ".opencode" / "skills").iterdir())


def test_install_requires_approval(tmp_path: Path) -> None:
    source = _skill(tmp_path / "src")
    home = tmp_path / "home"
    (home / ".opencode" / "skills").mkdir(parents=True)
    adapter = OpenCodeAdapter(home=home, project_root=tmp_path / "proj")
    plan = adapter.preview_install(source, InstallScope.USER)
    with pytest.raises(PermissionError):
        adapter.install(plan)


def test_install_and_sync_status(tmp_path: Path) -> None:
    source = _skill(tmp_path / "src")
    home = tmp_path / "home"
    (home / ".claude" / "skills").mkdir(parents=True)
    adapter = ClaudeCodeAdapter(home=home, project_root=tmp_path / "proj")
    plan = adapter.preview_install(source, InstallScope.USER)
    plan.approved = True
    record = adapter.install(plan)
    assert Path(record.target_path).exists()
    assert record.installed_hash
    assert adapter.sync_status(record).value == "up-to-date"

    # local modification detected
    skill_md = Path(record.target_path) / "SKILL.md"
    skill_md.write_text(skill_md.read_text() + "\nlocal edit\n", encoding="utf-8")
    assert adapter.sync_status(record).value == "locally-modified"


def test_conflict_is_reported_not_overwritten(tmp_path: Path) -> None:
    source = _skill(tmp_path / "src")
    home = tmp_path / "home"
    skills = home / ".claude" / "skills"
    skills.mkdir(parents=True)
    existing = _skill(skills, "demo-skill")
    (existing / "SKILL.md").write_text(
        "---\nname: demo-skill\ndescription: Different\n---\n", encoding="utf-8"
    )
    adapter = ClaudeCodeAdapter(home=home, project_root=tmp_path / "proj")
    plan = adapter.preview_install(source, InstallScope.USER)
    assert plan.conflicts
    assert adapter.check_conflicts("demo-skill")


def test_uninstall_only_removes_named_skill(tmp_path: Path) -> None:
    home = tmp_path / "home"
    skills = home / ".claude" / "skills"
    skills.mkdir(parents=True)
    _skill(skills, "keep-me")
    _skill(skills, "remove-me")
    adapter = ClaudeCodeAdapter(home=home, project_root=tmp_path / "proj")
    assert adapter.uninstall("remove-me", InstallScope.USER)
    assert not (skills / "remove-me").exists()
    assert (skills / "keep-me").exists()


def test_installed_skills_discovery(tmp_path: Path) -> None:
    home = tmp_path / "home"
    skills = home / ".claude" / "skills"
    skills.mkdir(parents=True)
    _skill(skills, "installed-one")
    adapter = ClaudeCodeAdapter(home=home, project_root=tmp_path / "proj")
    found = adapter.get_installed_skills()
    assert any(s.name == "installed-one" for s in found)
