"""Sprint 5 governance: derived risk levels, static script scan, audit redaction."""

from __future__ import annotations

import json
from pathlib import Path

from core.uskills.agentskills import import_agent_skill
from core.uskills.builder.scan import scan_risk_level, scan_scripts
from core.uskills.governance import Permission
from core.uskills.governance.audit import AuditLogger
from core.uskills.governance.risk import (
    RiskLevel,
    assess_skill_risk,
    skill_directory_flags,
    tool_permissions_for,
)
from core.uskills.runtime.tools import ToolDef, ToolRegistry
from core.uskills.schema import USkill


def skill(with_approval: bool = False) -> USkill:
    return USkill(
        **{
            "skill_id": "uskill-atomic-risk-v1-0-0",
            "meta": {"name": "risk", "category": "atomic", "description": "d"},
            "input": {"params": []},
            "execute": {
                "prompt_template": "just text",
                "model": "m",
                "tools": ["read-tool", "ghost-tool"],
                "requires_approval": with_approval,
            },
            "output": {"format": "text"},
            "control": {"timeout": 5, "retry": 0},
        }
    )


def registry_with(permission: Permission) -> ToolRegistry:
    reg = ToolRegistry()
    reg.register(ToolDef(id="read-tool", description="", func=lambda p: None,
                         permission=permission))
    return reg


class TestRiskDerivation:
    def test_pure_text_is_L0(self) -> None:
        assessment = assess_skill_risk(skill())
        assert assessment.level is RiskLevel.L0
        assert "pure text" in assessment.factors[0]

    def test_registered_read_tool_is_L2(self) -> None:
        reg = registry_with(Permission.read)
        assessment = assess_skill_risk(skill(), tool_permissions=tool_permissions_for(skill(), reg))
        assert assessment.level is RiskLevel.L2

    def test_write_tool_is_L3_network_is_L4(self) -> None:
        for perm, level in (
            (Permission.write, RiskLevel.L3),
            (Permission.shell, RiskLevel.L3),
            (Permission.network, RiskLevel.L4),
            (Permission.sensitive_data, RiskLevel.L4),
        ):
            reg = registry_with(perm)
            assessment = assess_skill_risk(
                skill(), tool_permissions=tool_permissions_for(skill(), reg)
            )
            assert assessment.level is level, perm

    def test_scripts_raise_L3(self) -> None:
        assessment = assess_skill_risk(skill(), has_scripts=True)
        assert assessment.level is RiskLevel.L3

    def test_unregistered_tools_do_not_raise_risk(self) -> None:
        # "ghost-tool" is declared but unresolvable: the runtime cannot invoke it
        assessment = assess_skill_risk(skill(), tool_permissions=[])
        assert assessment.level is RiskLevel.L0

    def test_approval_recorded_as_mitigation(self) -> None:
        assessment = assess_skill_risk(skill(with_approval=True))
        assert any("mitigation" in f for f in assessment.factors)
        json.dumps(assessment.to_dict())

    def test_directory_flags(self, tmp_path: Path) -> None:
        (tmp_path / "scripts").mkdir()
        (tmp_path / "scripts" / "run.py").write_text("print(1)")
        flags = skill_directory_flags(tmp_path)
        assert flags["has_scripts"] and flags["scripts"] == ["run.py"]


class TestStaticScan:
    def test_detects_dangerous_patterns(self, tmp_path: Path) -> None:
        scripts = tmp_path / "scripts"
        scripts.mkdir()
        (scripts / "evil.py").write_text(
            "import subprocess\nsubprocess.run(['rm', '-rf', '/'])\n", encoding="utf-8"
        )
        (scripts / "net.py").write_text("import requests\n", encoding="utf-8")
        findings = scan_scripts(scripts)
        ids = {f.pattern_id for f in findings}
        assert {"process-exec", "network"} <= ids
        assert scan_risk_level(findings) is RiskLevel.L4

    def test_clean_script_no_findings(self, tmp_path: Path) -> None:
        scripts = tmp_path / "scripts"
        scripts.mkdir()
        (scripts / "calc.py").write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")
        assert scan_scripts(scripts) == []

    def test_comments_are_not_capability(self, tmp_path: Path) -> None:
        scripts = tmp_path / "scripts"
        scripts.mkdir()
        (scripts / "doc.py").write_text("# subprocess is documented here\nx = 1\n", encoding="utf-8")
        assert scan_scripts(scripts) == []

    def test_missing_dir_is_empty(self, tmp_path: Path) -> None:
        assert scan_scripts(tmp_path / "nope") == []


class TestAuditRedaction:
    def test_sensitive_keys_masked(self) -> None:
        audit = AuditLogger()
        audit.log("tool_invoked", api_key="sk-live-123", nested={"user_token": "t"})
        entry = audit.read()[0]
        assert entry["api_key"] == "***REDACTED***"
        assert entry["nested"]["user_token"] == "***REDACTED***"

    def test_bulk_values_stored_as_digest(self) -> None:
        audit = AuditLogger()
        audit.log("debug", input={"secret_text": "hello world"})
        entry = audit.read()[0]["input"]
        assert entry["length"] > 0 and "sha256" in entry
        assert "hello world" not in json.dumps(entry)

    def test_non_sensitive_passthrough(self) -> None:
        audit = AuditLogger()
        audit.log("run_completed", duration_ms=12, tool="grep")
        entry = audit.read()[0]
        assert entry["duration_ms"] == 12 and entry["tool"] == "grep"

    def test_file_log_is_redacted_too(self, tmp_path: Path) -> None:
        path = tmp_path / "audit.jsonl"
        audit = AuditLogger(path)
        audit.log("x", password="hunter2", ok_field="fine")
        raw = path.read_text(encoding="utf-8")
        assert "hunter2" not in raw and "fine" in raw


class TestImportScanIntegration:
    @staticmethod
    def _make_skill(root: Path, scripts_text: str | None) -> Path:
        d = root / "ext-skill"
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(
            "---\nname: ext-skill\ndescription: external skill\n---\n\nBody\n", encoding="utf-8"
        )
        if scripts_text is not None:
            scripts = d / "scripts"
            scripts.mkdir(exist_ok=True)
            (scripts / "tool.py").write_text(scripts_text, encoding="utf-8")
        return d

    def test_import_reports_findings_and_sets_risk(self, tmp_path: Path) -> None:
        d = self._make_skill(tmp_path, "import os\nos.system('whoami')\n")
        _target, manifest, notes = import_agent_skill(d)
        joined = "\n".join(notes)
        assert "SECURITY SCAN" in joined
        assert manifest.security.risk_level == "L3"
        assert manifest.security.untrusted_source is True

    def test_clean_import_still_L3_floor_for_scripts(self, tmp_path: Path) -> None:
        d = self._make_skill(tmp_path, "x = 1\n")
        _target, manifest, notes = import_agent_skill(d)
        # presence of executable scripts raises the floor regardless of scan luck
        assert manifest.security.risk_level == "L3"
        assert any("floor risk to L3" in n for n in notes)

    def test_text_only_import(self, tmp_path: Path) -> None:
        d = self._make_skill(tmp_path, None)
        _target, manifest, _notes = import_agent_skill(d)
        assert manifest.security.risk_level == "L0"
