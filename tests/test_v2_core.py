"""Tests for V2 additions: schema dialect, semantics, converter context."""

from __future__ import annotations

from pathlib import Path

import yaml

from core.uskills.converter import convert_sop_text, parse_sop
from core.uskills.schema import JSON_SCHEMA_DIALECT, ParamType, exported_json_schema
from core.uskills.validator import load_skill, validate_skill_data


class TestSchemaDialect:
    def test_exported_schema_declares_2020_12(self) -> None:
        schema = exported_json_schema()
        assert schema["$schema"] == JSON_SCHEMA_DIALECT
        assert "$defs" in schema
        # $id follows the canonical uSkill docs domain
        assert "github.io/uSkill/" in schema["$id"]

    def test_param_type_is_enum(self) -> None:
        schema = exported_json_schema()
        param = schema["$defs"]["SkillParam"]["properties"]["type"]
        # Pydantic emits enums as a $ref into $defs
        ref = param.get("$ref", "")
        target = schema["$defs"][ref.rsplit("/", 1)[-1]] if ref else param
        assert "enum" in target

    def test_bad_param_type_rejected(self) -> None:
        data = {
            "skill_id": "uskill-atomic-t-v1-0-0",
            "meta": {"name": "t", "category": "atomic", "description": "d"},
            "input": {"params": [{"name": "a", "type": "strin"}]},  # typo
            "execute": {"prompt_template": "x {{a}}"},
            "output": {"format": "text"},
            "control": {},
        }
        ok, msg = validate_skill_data(data)
        assert not ok and "strin" in msg

    def test_source_now_optional(self) -> None:
        data = {
            "skill_id": "uskill-atomic-standalone-v1-0-0",
            "meta": {"name": "standalone", "category": "atomic", "description": "d"},
            "input": {"params": []},
            "execute": {"prompt_template": "hello"},
            "output": {"format": "text"},
            "control": {},
        }
        ok, _ = validate_skill_data(data)
        assert ok

    def test_param_type_enum_values(self) -> None:
        assert {t.value for t in ParamType} == {
            "string",
            "number",
            "integer",
            "boolean",
            "object",
            "array",
        }


class TestSemanticValidation:
    def _base(self, **overrides):
        data = {
            "skill_id": "uskill-atomic-sem-v1-0-0",
            "meta": {"name": "sem", "category": "atomic", "description": "d"},
            "input": {"params": [{"name": "text", "type": "string", "required": True}]},
            "execute": {"prompt_template": "work on {{text}}"},
            "output": {"format": "text"},
            "control": {},
        }
        data.update(overrides)
        return data

    def test_undefined_template_var_is_error(self) -> None:
        data = self._base(execute={"prompt_template": "work on {{ghost}}"})
        ok, msg = validate_skill_data(data)
        assert not ok
        assert "undefined input params" in msg and "ghost" in msg

    def test_optional_without_default_is_warning_only(self) -> None:
        data = self._base(
            input={
                "params": [
                    {"name": "text", "type": "string", "required": True},
                    {"name": "extra", "type": "string", "required": False},
                ]
            }
        )
        ok, msg = validate_skill_data(data)
        assert ok
        assert "warnings" in msg

    def test_composite_without_tools_is_error(self) -> None:
        data = self._base(
            skill_id="uskill-composite-sem-v1-0-0",
            meta={"name": "sem", "category": "composite", "description": "d"},
        )
        ok, msg = validate_skill_data(data)
        assert not ok and "no tools" in msg


class TestConverterContext:
    SOP = """处理客户投诉时，首先应确认客户的诉求和订单状态。

1. 查询订单
   - 核对订单号
2. 判断问题类型
3. 给出处理方案

特别注意：涉及退款时需要主管审批。
"""

    def test_parse_sop_keeps_everything(self) -> None:
        doc = parse_sop(self.SOP)
        kinds = {b.kind for b in doc.blocks}
        assert "list_item" in kinds
        assert "paragraph" in kinds
        texts = " ".join(b.text for b in doc.blocks)
        assert "特别注意：涉及退款时需要主管审批" in texts
        assert "首先应确认客户的诉求和订单状态" in texts
        assert "核对订单号" in texts

    def test_nested_items_depth(self) -> None:
        doc = parse_sop(self.SOP)
        nested = [b for b in doc.blocks if b.kind == "list_item" and b.depth > 0]
        assert len(nested) == 1
        assert nested[0].text == "核对订单号"

    def test_conversion_preserves_preamble_and_constraints(self) -> None:
        skills = convert_sop_text(self.SOP, "客户投诉")
        assert len(skills) == 3  # top-level steps only
        ctx = skills[0].source.context or ""
        assert "主管审批" in ctx  # trailing constraint preserved
        assert "确认客户的诉求" in ctx  # leading paragraph preserved
        assert "特别注意" in skills[0].execute.prompt_template

    def test_nested_detail_attached_to_step(self) -> None:
        skills = convert_sop_text(self.SOP, "客户投诉")
        assert "核对订单号" in skills[0].source.context
        assert "核对订单号" in skills[0].execute.prompt_template

    def test_context_roundtrips_through_yaml(self, tmp_path: Path) -> None:
        from core.uskills.converter import convert_sop_file

        src = tmp_path / "sop.md"
        src.write_text(self.SOP, encoding="utf-8")
        written = convert_sop_file(src, tmp_path / "out")
        skill = load_skill(written[0])
        assert "主管审批" in (skill.source.context or "")
        data = yaml.safe_load(written[0].read_text(encoding="utf-8"))
        assert data["source"]["context"]

    def test_legacy_paragraph_fallback_still_works(self) -> None:
        skills = convert_sop_text("Para one.\n\nPara two.", "fallback")
        assert len(skills) == 2
