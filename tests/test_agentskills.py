"""Tests for Agent Skills open-standard compatibility and Manifest V2."""

from __future__ import annotations

from pathlib import Path

import pytest

from core.uskills.agentskills import (
    export_agent_skill,
    import_agent_skill,
    inspect_agent_skill,
    validate_agent_skill,
)
from core.uskills.manifest import (
    USkillManifest,
    manifest_from_legacy_skill,
    validate_manifest_file,
)


def make_skill_dir(
    tmp_path: Path,
    name: str = "code-review",
    *,
    frontmatter: str | None = None,
    body: str = "Review the diff and report risks.",
    extra_files: dict[str, str] | None = None,
) -> Path:
    root = tmp_path / name
    root.mkdir(parents=True, exist_ok=True)
    if frontmatter is None:
        frontmatter = f"---\nname: {name}\ndescription: Reviews code diffs for risks.\n---\n"
    (root / "SKILL.md").write_text(frontmatter + "\n" + body, encoding="utf-8")
    for rel, content in (extra_files or {}).items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return root


class TestValidateAgentSkill:
    def test_valid_skill(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path, extra_files={"references/policy.md": "policy"})
        ok, issues = validate_agent_skill(root)
        assert ok, issues

    def test_missing_skill_md(self, tmp_path: Path) -> None:
        (tmp_path / "empty-skill").mkdir()
        ok, issues = validate_agent_skill(tmp_path / "empty-skill")
        assert not ok
        assert any("SKILL.md" in i for i in issues)

    def test_invalid_name_case(self, tmp_path: Path) -> None:
        root = make_skill_dir(
            tmp_path,
            frontmatter="---\nname: CodeReview\ndescription: bad name\n---\n",
        )
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("lowercase" in i for i in issues)

    def test_name_dir_mismatch(self, tmp_path: Path) -> None:
        root = make_skill_dir(
            tmp_path,
            frontmatter="---\nname: other-name\ndescription: mismatch\n---\n",
        )
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("parent directory" in i for i in issues)

    def test_missing_description(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path, frontmatter="---\nname: code-review\n---\n")
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("description" in i for i in issues)

    def test_description_too_long(self, tmp_path: Path) -> None:
        root = make_skill_dir(
            tmp_path,
            frontmatter=f"---\nname: code-review\ndescription: {'x' * 1100}\n---\n",
        )
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("1024" in i for i in issues)

    def test_unsupported_frontmatter_key(self, tmp_path: Path) -> None:
        root = make_skill_dir(
            tmp_path,
            frontmatter=("---\nname: code-review\ndescription: d\nuskill_extra: true\n---\n"),
        )
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("uskill_extra" in i for i in issues)

    def test_missing_referenced_file(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path, body="See references/guidelines.md for the rules.")
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("references/guidelines.md" in i for i in issues)

    def test_body_too_long(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path, body="\n".join(f"line {i}" for i in range(502)))
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("500" in i for i in issues)

    def test_no_frontmatter(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path, frontmatter="")
        ok, issues = validate_agent_skill(root)
        assert not ok
        assert any("frontmatter" in i for i in issues)


class TestImportExport:
    def test_import_generates_manifest_besides_skill_md(self, tmp_path: Path) -> None:
        root = make_skill_dir(
            tmp_path,
            extra_files={
                "references/policy.md": "p",
                "scripts/check.py": "print(1)",
                "assets/logo.svg": "<svg/>",
            },
        )
        target, manifest, notes = import_agent_skill(root)
        assert (root / "uskill.yaml").exists()
        assert manifest.metadata.name == "code-review"
        assert manifest.provenance.source == "imported"
        assert manifest.provenance.content_sha256  # hash recorded
        assert notes
        # SKILL.md untouched
        assert (root / "SKILL.md").read_text(encoding="utf-8").startswith("---")
        assert target == root

    def test_import_invalid_refuses(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path, frontmatter="---\nname: BadName\ndescription: d\n---\n")
        with pytest.raises(ValueError, match="invalid Agent Skill"):
            import_agent_skill(root)

    def test_export_roundtrip(self, tmp_path: Path) -> None:
        manifest = USkillManifest(
            metadata={
                "name": "text-summarize",
                "description": "Summarize long documents.",
                "version": "1.0.0",
            }
        )
        out = export_agent_skill(manifest, "Summarize the given document.", tmp_path / "out")
        ok, issues = validate_agent_skill(out)
        assert ok, issues
        assert (out / "uskill.yaml").exists()

    def test_export_does_not_overwrite_without_force(self, tmp_path: Path) -> None:
        manifest = USkillManifest(metadata={"name": "dup", "description": "d"})
        export_agent_skill(manifest, "body", tmp_path)
        with pytest.raises(FileExistsError):
            export_agent_skill(manifest, "body", tmp_path)
        export_agent_skill(manifest, "body", tmp_path, force=True)

    def test_inspect_reports(self, tmp_path: Path) -> None:
        root = make_skill_dir(tmp_path)
        pkg = inspect_agent_skill(root)
        assert pkg.name == "code-review"
        assert pkg.sha256


class TestManifest:
    def test_valid_manifest_file(self, tmp_path: Path) -> None:
        manifest = USkillManifest(
            metadata={"name": "demo-skill", "description": "demo"},
            execution={"mode": "llm", "timeout": 10},
            tools=[{"id": "fs.read", "permission": "read"}],
        )
        path = tmp_path / "uskill.yaml"
        from core.uskills.manifest import dump_manifest

        dump_manifest(manifest, path)
        ok, msg = validate_manifest_file(path)
        assert ok, msg

    def test_rejects_bad_api_version(self, tmp_path: Path) -> None:
        path = tmp_path / "uskill.yaml"
        path.write_text(
            "apiVersion: uskill/v1\nkind: Skill\nmetadata:\n  name: a\n  description: d\n",
            encoding="utf-8",
        )
        ok, _ = validate_manifest_file(path)
        assert not ok

    def test_from_legacy_skill(self) -> None:
        from core.uskills.validator import load_skill

        skill = load_skill("skills/composite/content_pipeline.yaml")
        manifest = manifest_from_legacy_skill(skill)
        assert manifest.metadata.name == "content-pipeline"
        assert manifest.execution.mode.value == "workflow"
        assert {t.id for t in manifest.tools} == {
            "text_keyword_extract",
            "text_summarize",
            "text_translate",
        }

    def test_compatibility_report(self) -> None:
        from core.uskills.agentskills import inspect_compatibility

        manifest = USkillManifest(
            metadata={"name": "x", "description": "d"},
            execution={"mode": "workflow"},
            inputs={"type": "object"},
        )
        notes = inspect_compatibility(manifest)
        assert any("workflow" in n for n in notes)
        assert any("JSON Schema" in n for n in notes)
