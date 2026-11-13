"""Tests for the legacy SkillExecutor shim and the AI converter report."""

from __future__ import annotations

import json

import pytest

from core.uskills.ai_converter import AIConverter
from core.uskills.errors import ExecutionFailedError
from core.uskills.executor import SkillExecutor
from core.uskills.runtime import MockProvider
from core.uskills.validator import load_skill


class TestLegacyExecutor:
    def test_legacy_result_envelope(self) -> None:
        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        provider = MockProvider('{"keywords": ["a"], "summary": "s"}')
        ex = SkillExecutor(provider=provider)
        result = ex.execute(skill, {"text": "some text"})
        assert result["skill_id"] == skill.skill_id
        assert result["result"] == {"keywords": ["a"], "summary": "s"}
        assert "execution_time" in result["meta"]
        assert result["status"] == "COMPLETED"

    def test_failed_run_raises_instead_of_fake_success(self) -> None:
        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        ex = SkillExecutor(provider=MockProvider("not json at all"))
        with pytest.raises(ExecutionFailedError):
            ex.execute(skill, {"text": "x"})


def _valid_skill_payload(i: int) -> dict:
    return {
        "skill_id": f"uskill-atomic-ai-skill-{i}-v1-0-0",
        "meta": {"name": f"AI Skill {i}", "category": "atomic", "description": "d"},
        "input": {"params": [{"name": "text", "type": "string", "required": True}]},
        "execute": {"prompt_template": "do {{text}}"},
        "output": {"format": "text"},
        "control": {},
    }


class TestAIConverterReport:
    def test_valid_items_and_structured_errors(self) -> None:
        payload = json.dumps(
            {
                "skills": [
                    _valid_skill_payload(1),
                    {"skill_id": "garbage", "meta": {}},  # invalid
                    _valid_skill_payload(2),
                ]
            }
        )
        provider = MockProvider(payload)
        conv = AIConverter(provider=provider)
        report = conv.convert_sop_with_report("sop text", "SOP")
        assert len(report.skills) == 2
        assert len(report.errors) == 1
        assert report.errors[0].index == 1
        assert not report.ok
        d = report.to_dict()
        assert d["skill_count"] == 2 and len(d["errors"]) == 1

    def test_non_json_output_reported(self) -> None:
        provider = MockProvider("oops not json")
        conv = AIConverter(provider=provider)
        report = conv.convert_sop_with_report("sop", "SOP")
        assert not report.ok
        assert "not JSON" in report.errors[0].message

    def test_back_compat_convert_sop(self) -> None:
        provider = MockProvider(json.dumps({"skills": [_valid_skill_payload(1)]}))
        conv = AIConverter(provider=provider)
        skills = conv.convert_sop("sop", "SOP")
        assert len(skills) == 1
        assert conv.last_report is not None and conv.last_report.ok

    def test_requires_provider(self) -> None:
        from core.uskills.errors import ProviderError

        conv = AIConverter(provider=None)
        conv.provider = None
        with pytest.raises(ProviderError):
            conv.convert_sop_with_report("x", "SOP")
