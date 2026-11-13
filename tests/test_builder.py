"""Sprint 2: Skill Builder — importer, task IR, quality scoring, pipeline."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from core.uskills.builder.importer import import_source
from core.uskills.builder.ir import StepKind, build_ir, classify_step
from core.uskills.builder.pipeline import build_skills
from core.uskills.builder.quality import score_skill
from core.uskills.evaluation import EvalSuite
from core.uskills.schema import USkill
from core.uskills.validator import load_skill

SOP_TEXT = """# 发布流程 SOP

仅当变更通过 CI 后执行；不适用于紧急安全修复。

- 提交变更说明
  - 包含影响范围与回滚方案
- 如果风险等级为高则升级评审
- 由主管审批发布窗口
- 重复巡检监控直到稳定
"""

MINIMAL_SKILL = {
    "skill_id": "uskill-atomic-low-quality-v1-0-0",
    "meta": {"name": "Low Quality", "category": "atomic", "description": "x", "version": "1.0.0"},
    "input": {"params": [{"name": "text", "type": "string", "required": True}]},
    "execute": {"prompt_template": "do {{text}}"},
    "output": {"format": "text"},
    "control": {"timeout": 5},
}


class TestImporter:
    def test_inline_prompt(self) -> None:
        doc = import_source("把这段话翻译成英文")
        assert doc.kind == "prompt"
        assert "翻译" in doc.text

    def test_markdown_file(self, tmp_path: Path) -> None:
        p = tmp_path / "sop.md"
        p.write_text(SOP_TEXT, encoding="utf-8")
        doc = import_source(p)
        assert doc.kind == "markdown"
        assert doc.name == "sop"

    def test_legacy_skill_v1_file(self, tmp_path: Path) -> None:
        p = tmp_path / "skill.yaml"
        p.write_text(yaml.safe_dump(MINIMAL_SKILL), encoding="utf-8")
        assert import_source(p).kind == "skill-v1"

    def test_agent_skill_dir(self, tmp_path: Path) -> None:
        d = tmp_path / "my-skill"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: my-skill\ndescription: does things\n---\n\nBody text\n", encoding="utf-8"
        )
        doc = import_source(d)
        assert doc.kind == "agent-skill"
        assert doc.metadata["frontmatter"]["name"] == "my-skill"

    def test_missing_path_raises(self, tmp_path: Path) -> None:
        import pytest

        with pytest.raises(FileNotFoundError):
            import_source(tmp_path / "nowhere.md")


class TestStepClassification:
    def test_approval_markers(self) -> None:
        for text in ("由主管审批发布窗口", "转人工复核", "get manager approval"):
            kind, evidence = classify_step(text)
            assert kind is StepKind.APPROVAL, text
            assert evidence

    def test_decision_marker(self) -> None:
        kind, _ = classify_step("如果风险等级为高则升级评审")
        assert kind is StepKind.DECISION

    def test_loop_marker(self) -> None:
        kind, _ = classify_step("重复巡检监控直到稳定")
        assert kind is StepKind.LOOP

    def test_atomic_default(self) -> None:
        kind, evidence = classify_step("从知识库中检索最相关的处理方案")
        assert kind is StepKind.ATOMIC
        assert "no decision" in evidence


class TestBuildIR:
    def test_structure_and_kinds(self) -> None:
        ir = build_ir(SOP_TEXT, "release")
        assert ir.goal == "发布流程 SOP"
        assert len(ir.steps) == 4
        kinds = [s.kind for s in ir.steps]
        assert kinds == [StepKind.ATOMIC, StepKind.DECISION, StepKind.APPROVAL, StepKind.LOOP]
        assert ir.has_approval
        assert ir.steps[0].nested_details == ["包含影响范围与回滚方案"]
        summary = ir.kind_summary()
        assert summary == {"atomic": 1, "decision": 1, "approval": 1, "loop": 1}

    def test_constraints_and_serialization(self) -> None:
        _constraints()

    def test_empty_document(self) -> None:
        ir = build_ir("纯文本，没有步骤列表。", "plain")
        assert ir.steps == []
        assert not ir.has_approval


def _constraints() -> None:
    ir = build_ir(SOP_TEXT, "release")
    assert any("仅当" in c or "不适用" in c for c in ir.constraints)
    data = ir.to_dict()
    assert data["step_kind_summary"]["approval"] == 1
    assert json.dumps(data, ensure_ascii=False)


class TestQualityScore:
    def test_low_quality_requires_review(self) -> None:
        score = score_skill(USkill(**MINIMAL_SKILL))
        assert score.total < 70
        assert score.review_required
        by_name = {d.name: d for d in score.dimensions}
        assert by_name["traceability"].score == 0
        assert by_name["output_verifiability"].score == 0
        # every dimension carries evidence for every point awarded or lost
        assert all(d.evidence for d in score.dimensions)

    def test_better_artifact_scores_higher(self, tmp_path: Path) -> None:
        p = tmp_path / "sop.md"
        p.write_text(SOP_TEXT, encoding="utf-8")
        report = build_skills(p, tmp_path / "out")
        best = max(report.candidates, key=lambda c: c.score.total)
        assert best.score.total > score_skill(USkill(**MINIMAL_SKILL)).total
        assert best.score.total <= 100

    def test_secret_like_literal_loses_safety_points(self) -> None:
        data = dict(json.loads(json.dumps(MINIMAL_SKILL)))
        data["execute"]["prompt_template"] = "use api_key=sk-abc123 for {{text}}"
        data["output"] = {"format": "json", "params": ["result"]}
        data["meta"]["description"] = "a description that is definitely long enough to pass"
        dims = {d.name: d for d in score_skill(USkill(**data)).dimensions}
        safety = dims["safety_discoverability"]
        assert any("secret" in e for e in safety.evidence)
        assert safety.score == 0  # secret blocks the safety points entirely


class TestBuildPipeline:
    def test_end_to_end_drafts_and_report(self, tmp_path: Path) -> None:
        p = tmp_path / "sop.md"
        p.write_text(SOP_TEXT, encoding="utf-8")
        out = tmp_path / "build"
        report = build_skills(p, out)

        assert report.candidates, "SOP should yield candidates"
        # drafts are loadable skills, tagged draft, approval propagated
        drafts = sorted((out / "drafts").glob("*.json"))
        assert len(drafts) == len(report.candidates)
        for path in drafts:
            skill = load_skill(path)
            assert "draft" in skill.meta.tags
            assert skill.execute.requires_approval  # SOP contains an approval step
        # eval drafts are loadable suites bound to their skill
        suites = sorted((out / "evals-draft").glob("*.suite.json"))
        assert len(suites) == len(report.candidates)
        suite = EvalSuite.load(suites[0])
        assert suite.skill
        assert suite.cases and suite.cases[0].task_id == "normal-001"
        # machine-readable report, explicit no-auto-publish policy
        raw = json.loads((out / "build-report.json").read_text(encoding="utf-8"))
        assert raw["policy"].count("review") >= 1
        assert raw["ir"]["step_kind_summary"]["approval"] == 1
        assert any("approval" in n for n in report.notes)

    def test_source_without_steps_yields_no_drafts(self, tmp_path: Path) -> None:
        report = build_skills("# 只有标题和一段话\n\n没有结构化步骤。", tmp_path / "out")
        assert report.candidates == []
        assert any("manual authoring" in n for n in report.notes)

    def test_drafts_are_never_marked_published(self, tmp_path: Path) -> None:
        p = tmp_path / "sop.md"
        p.write_text(SOP_TEXT, encoding="utf-8")
        report = build_skills(p, tmp_path / "out")
        assert all(c.lifecycle.value == "draft" for c in report.candidates)
        for path in (tmp_path / "out" / "drafts").glob("*.json"):
            assert "draft" in load_skill(path).meta.tags
