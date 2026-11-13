"""Indexer: grouping, error surfacing, duplicate detection, stats."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from core.uskills.indexer import (
    STANDALONE_GROUP,
    _anchor,
    build_skills_index,
    get_skill_stats,
)

REPO = Path(__file__).resolve().parent.parent


def _skill(
    name: str,
    *,
    sop_name: str | None = None,
    category: str = "atomic",
    domain: str = "test",
    version: str = "1.0.0",
) -> dict:
    data = {
        "skill_id": f"uskill-{category}-{name}-v1-0-0",
        "meta": {"name": name, "category": category, "description": f"{name} skill"},
        "input": {"params": []},
        "execute": {"prompt_template": "do it"},
        "output": {"format": "text"},
        "control": {"timeout": 5, "retry": 0},
    }
    data["meta"]["version"] = version
    data["meta"]["domain"] = domain
    if sop_name:
        data["source"] = {
            "sop_name": sop_name,
            "sop_path": "x.md",
            "step_index": 1,
            "raw_step": name,
        }
    return data


def _write(root: Path, filename: str, data: dict) -> Path:
    path = root / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".json":
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    else:
        path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    return path


class TestBuildSkillsIndex:
    def test_groups_by_sop_name_and_standalone(self, tmp_path: Path) -> None:
        skills = tmp_path / "skills"
        _write(skills, "a.yaml", _skill("alpha", sop_name="NLP 技能集"))
        _write(skills, "b.yaml", _skill("beta", sop_name="NLP 技能集"))
        _write(skills, "sub/c.json", _skill("gamma"))  # standalone, nested, json

        out = build_skills_index(skills, tmp_path / "docs/generated/index.md")
        text = out.read_text(encoding="utf-8")
        assert out.exists()
        assert "共收录 **3** 个技能，来源于 **2** 个" in text
        assert "## NLP 技能集" in text
        assert f"## {STANDALONE_GROUP}" in text
        assert "| `uskill-atomic-alpha-v1-0-0` | alpha | atomic | test | 1.0.0 |" in text
        assert "- **atomic**: 3 个技能" in text

    def test_broken_file_reported_not_silently_skipped(self, tmp_path: Path) -> None:
        skills = tmp_path / "skills"
        _write(skills, "good.yaml", _skill("good"))
        (skills / "broken.yaml").write_text(
            "skill_id: 123\nmeta: {}\nnot-a-skill: true", encoding="utf-8"
        )
        out = build_skills_index(skills, tmp_path / "idx.md")
        text = out.read_text(encoding="utf-8")
        assert '!!! warning "加载警告"' in text
        assert "broken.yaml" in text
        assert "good" in text  # valid skill still indexed

    def test_duplicate_skill_ids_surfaced(self, tmp_path: Path) -> None:
        skills = tmp_path / "skills"
        _write(skills, "one.yaml", _skill("dup"))
        _write(skills, "two.yaml", _skill("dup"))  # same skill_id
        out = build_skills_index(skills, tmp_path / "idx.md")
        text = out.read_text(encoding="utf-8")
        assert '!!! danger "重复 Skill ID"' in text
        assert "uskill-atomic-dup-v1-0-0" in text

    def test_skips_manifest_and_evals_files(self, tmp_path: Path) -> None:
        skills = tmp_path / "skills"
        _write(skills, "keep.yaml", _skill("keep"))
        # uskill.* manifests use a different schema and must be skipped
        (skills / "uskill.yaml").write_text(
            "apiVersion: uskills/v2\nkind: USkillManifest", encoding="utf-8"
        )
        suite = {"skill": "x", "version": "1", "cases": []}
        (skills / "evals").mkdir()
        (skills / "evals" / "x.suite.json").write_text(json.dumps(suite), encoding="utf-8")

        stats = get_skill_stats(skills)
        assert stats["total_skills"] == 1
        assert stats["invalid_files"] == 0  # skipped, not broken

    def test_empty_dir(self, tmp_path: Path) -> None:
        out = build_skills_index(tmp_path / "nothing", tmp_path / "idx.md")
        text = out.read_text(encoding="utf-8")
        assert "共收录 **0** 个技能" in text


class TestStats:
    def test_stats_shape_over_repo_skills(self) -> None:
        stats = get_skill_stats(REPO / "skills")
        assert stats["total_skills"] >= 8
        assert stats["total_sources"] >= 1
        assert set(stats["categories"]) >= {"atomic", "composite"}
        assert stats["invalid_files"] == 0
        assert stats["duplicate_ids"] == 0

    def test_counts_broken_and_duplicates(self, tmp_path: Path) -> None:
        _write(tmp_path, "d1.yaml", _skill("d"))
        _write(tmp_path, "d2.yaml", _skill("d"))
        (tmp_path / "bad.yaml").write_text("nope: true", encoding="utf-8")
        stats = get_skill_stats(tmp_path)
        assert stats["total_skills"] == 2
        assert stats["duplicate_ids"] == 1
        assert stats["invalid_files"] == 1


class TestAnchor:
    def test_anchor_rules(self) -> None:
        # exact contract: mirrors markdown.extensions.toc.slugify_unicode
        # (configured in mkdocs.yml), so generated nav links always resolve
        assert _anchor("NLP Skills") == "nlp-skills"
        assert _anchor("  Weird__Chars!! Here ") == "weird__chars-here"
        assert _anchor("a - b -- c") == "a-b-c"  # hyphen/space runs collapse
        assert _anchor("技能仓库") == "技能仓库"
        assert _anchor("!!!") == "section"
