"""Sprint 5 distribution: SkillRegistry search, packaging, MCP bridge."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

import pytest

from adapters.mcp_bridge import register_mcp_tool, register_mcp_tools
from core.uskills.errors import PermissionDeniedError
from core.uskills.governance import Permission, PermissionPolicy
from core.uskills.packaging import package_skill
from core.uskills.registry import SkillRegistry
from core.uskills.runtime import ToolRegistry

REPO = Path(__file__).resolve().parent.parent


class TestSkillRegistry:
    @pytest.fixture
    def registry(self) -> SkillRegistry:
        return SkillRegistry(REPO / "skills")

    def test_loads_repo_skills(self, registry: SkillRegistry) -> None:
        assert len(registry.all()) >= 8  # all legacy assets load
        assert registry.get("uskill-atomic-text-summarize-v1-1-0") is not None

    def test_health_clean(self, registry: SkillRegistry) -> None:
        health = registry.health()
        assert health["ok"], health
        assert health["broken"] == [] and health["duplicate_ids"] == []

    def test_name_search(self, registry: SkillRegistry) -> None:
        hits = registry.search("text-summarize", mode="name")
        assert any(h.skill_id.startswith("uskill-atomic-text-summarize") for h in hits)

    def test_tag_search(self, registry: SkillRegistry) -> None:
        hits = registry.search("nlp", mode="tag")
        assert len(hits) >= 2

    def test_domain_search(self, registry: SkillRegistry) -> None:
        hits = registry.search("nlp", mode="domain")
        assert all(h.domain == "nlp" for h in hits) and hits

    def test_keyword_search(self, registry: SkillRegistry) -> None:
        hits = registry.search("流水线", mode="keyword")
        assert any("content-pipeline" in h.skill_id for h in hits)

    def test_dependency_search(self, registry: SkillRegistry) -> None:
        # who declares text_summarize as a sub-skill/tool?
        hits = registry.search("text_summarize", mode="dependency")
        assert any(h.category == "composite" for h in hits)

    def test_auto_mode_dedupes(self, registry: SkillRegistry) -> None:
        hits = registry.search("translate", mode="auto")
        ids = [h.skill_id for h in hits]
        assert len(ids) == len(set(ids)) and ids

    def test_broken_file_reported(self, tmp_path: Path) -> None:
        (tmp_path / "bad.yaml").write_text("skill_id: 123\nnot: a-skill\n", encoding="utf-8")
        reg = SkillRegistry(tmp_path)
        assert reg.all() == []
        assert reg.health()["broken"]
        assert not reg.health()["ok"]


class TestPackaging:
    def test_package_agent_skill_dir(self, tmp_path: Path) -> None:
        src = REPO / "skills/agent-skills/code-review"
        result = package_skill(src, tmp_path / "dist")
        assert result.path.exists()
        assert result.sha256 == hashlib.sha256(result.path.read_bytes()).hexdigest()
        with zipfile.ZipFile(result.path) as zf:
            names = zf.namelist()
            assert "package.json" in names
            assert any(n.endswith("SKILL.md") for n in names)
            manifest = json.loads(zf.read("package.json"))
        assert manifest["format"] == "agent-skill"
        assert {"path", "sha256"} <= set(manifest["files"][0].keys())
        assert "governance layer" in " ".join(manifest["compatibility_layers"])

    def test_package_legacy_file(self, tmp_path: Path) -> None:
        result = package_skill(REPO / "skills/atomic/text_summarize.yaml", tmp_path / "d")
        with zipfile.ZipFile(result.path) as zf:
            manifest = json.loads(zf.read("package.json"))
        assert manifest["format"] == "skill-v1"
        assert len(manifest["files"]) == 1

    def test_no_silent_overwrite(self, tmp_path: Path) -> None:
        src = REPO / "skills/agent-skills/code-review"
        package_skill(src, tmp_path / "d")
        with pytest.raises(ValueError, match="exists"):
            package_skill(src, tmp_path / "d")
        package_skill(src, tmp_path / "d", force=True)

    def test_rejects_unknown_format(self, tmp_path: Path) -> None:
        p = tmp_path / "x.txt"
        p.write_text("hi")
        with pytest.raises(ValueError, match="unsupported"):
            package_skill(p, tmp_path / "d")

    def test_checksums_verifiable(self, tmp_path: Path) -> None:
        src = REPO / "skills/agent-skills/code-review"
        result = package_skill(src, tmp_path / "d")
        with zipfile.ZipFile(result.path) as zf:
            for entry in json.loads(zf.read("package.json"))["files"]:
                assert hashlib.sha256(zf.read(entry["path"])).hexdigest() == entry["sha256"]


class TestMcpBridge:
    @staticmethod
    def _spec(name: str = "fetch_url") -> dict:
        return {
            "name": name,
            "description": "fetch a URL",
            "inputSchema": {"type": "object", "properties": {"url": {"type": "string"}}},
        }

    def test_registration_and_dispatch(self) -> None:
        calls: list[tuple[str, dict]] = []
        registry = ToolRegistry(policy=PermissionPolicy(allow={Permission.network}))
        tool = register_mcp_tool(
            registry, self._spec(), dispatch=lambda n, a: calls.append((n, a)) or "ok"
        )
        assert tool.id == "mcp:fetch_url"
        assert tool.input_schema is not None
        out = registry.invoke("mcp:fetch_url", {"url": "https://x"})
        assert out == "ok"
        assert calls == [("fetch_url", {"url": "https://x"})]

    def test_default_denied_by_least_privilege(self) -> None:
        registry = ToolRegistry()  # default policy: read only
        register_mcp_tool(registry, self._spec(), dispatch=lambda n, a: None)
        with pytest.raises(PermissionDeniedError):
            registry.invoke("mcp:fetch_url", {})

    def test_mcp_tools_default_non_idempotent(self) -> None:
        registry = ToolRegistry()
        tool = register_mcp_tool(registry, self._spec("pay_bill"), dispatch=lambda n, a: None)
        assert tool.idempotent is False

    def test_batch_registration(self) -> None:
        registry = ToolRegistry(policy=PermissionPolicy(allow={Permission.network}))
        tools = register_mcp_tools(
            registry, [self._spec("a"), self._spec("b")], dispatch=lambda n, a: n
        )
        assert [t.id for t in tools] == ["mcp:a", "mcp:b"]
        assert registry.invoke("mcp:b", {}) == "b"

    def test_spec_requires_name(self) -> None:
        with pytest.raises(ValueError, match="name"):
            register_mcp_tool(ToolRegistry(), {"description": "x"}, dispatch=lambda n, a: None)

    def test_mcp_tool_resolves_as_composite_substep(self) -> None:
        # end-to-end: composite declares mcp:fetch_url; runtime invokes it
        import core.uskills.runtime as rt

        registry = ToolRegistry(policy=PermissionPolicy(allow={Permission.network}))
        register_mcp_tool(registry, self._spec(), dispatch=lambda n, a: "fetched")
        from core.uskills.schema import USkill

        composite = USkill(
            **{
                "skill_id": "uskill-composite-mcp-v1-0-0",
                "meta": {"name": "mcp", "category": "composite", "description": "d"},
                "input": {"params": [{"name": "text", "type": "string", "required": True}]},
                "execute": {
                    "prompt_template": "fetch {{mcp:fetch_url}}",
                    "model": "m",
                    "tools": ["mcp:fetch_url"],
                },
                "output": {"format": "json", "params": ["result"]},
                "control": {"timeout": 5, "retry": 0},
            }
        )
        runtime = rt.SkillRuntime(rt.MockProvider('{"result": "r"}'), registry=registry)
        record = runtime.run(composite, {"text": "x"})
        assert record.status is rt.StepState.COMPLETED
        step = next(s for s in record.steps if s.step_id == "subskill:mcp:fetch_url")
        assert step.output == "fetched"
