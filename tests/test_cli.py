"""CLI-level tests: every command through main() with real exit codes.

In-process (monkeypatched argv) so the whole CLI surface is covered fast.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cli.uskills_cli import main
from core.uskills.governance.audit import AuditLogger

REPO = Path(__file__).resolve().parent.parent

GOOD_SKILL = {
    "skill_id": "uskill-atomic-cli-fixture-v1-0-0",
    "meta": {"name": "cli fixture", "category": "atomic", "description": "d"},
    "input": {"params": []},
    "execute": {"prompt_template": "hello", "model": "mock"},
    "output": {"format": "json", "params": []},
    "control": {"timeout": 5, "retry": 0},
}


def run_cli(monkeypatch: pytest.MonkeyPatch, *argv: str) -> int:
    monkeypatch.setattr("sys.argv", ["uskills", *argv])
    return main()


@pytest.fixture
def skill_file(tmp_path: Path) -> Path:
    path = tmp_path / "fixture.yaml"
    import yaml

    path.write_text(yaml.safe_dump(GOOD_SKILL, allow_unicode=True), encoding="utf-8")
    return path


class TestBasics:
    def test_no_command_exits_2(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("sys.argv", ["uskills"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 2

    def test_version(self, monkeypatch: pytest.MonkeyPatch, capsys) -> None:
        monkeypatch.setattr("sys.argv", ["uskills", "--version"])
        with pytest.raises(SystemExit):
            main()
        assert capsys.readouterr().out

    def test_doctor(self, monkeypatch: pytest.MonkeyPatch) -> None:
        assert run_cli(monkeypatch, "doctor") == 0

    def test_validate_ok_and_bad(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        assert run_cli(monkeypatch, "validate", "skills/") == 0
        bad = tmp_path / "bad.yaml"
        bad.write_text("skill_id: nope\nmeta: {}", encoding="utf-8")
        assert run_cli(monkeypatch, "validate", str(bad)) == 1

    def test_stats(self, monkeypatch: pytest.MonkeyPatch, capsys) -> None:
        assert run_cli(monkeypatch, "stats", "skills") == 0
        assert "total_skills" in capsys.readouterr().out

    def test_index(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        out = tmp_path / "idx.md"
        assert run_cli(monkeypatch, "index", "skills", "--output", str(out)) == 0
        assert out.exists() and out.read_text(encoding="utf-8")


class TestStandardsCommands:
    def test_schema_both(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        a, b = tmp_path / "s.json", tmp_path / "m.json"
        rc = run_cli(
            monkeypatch,
            "schema",
            "--target",
            "both",
            "--output",
            str(a),
            "--manifest-output",
            str(b),
        )
        assert rc == 0
        assert json.loads(a.read_text())["$schema"].endswith("2020-12/schema")
        assert json.loads(b.read_text())["properties"]["apiVersion"]["const"] == "uskills/v2"

    def test_migrate_dry_run_and_real(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        assert (
            run_cli(
                monkeypatch,
                "migrate",
                "skills/atomic",
                "--output",
                str(tmp_path / "m"),
                "--dry-run",
            )
            == 0
        )
        assert not (tmp_path / "m").exists()
        assert (
            run_cli(
                monkeypatch,
                "migrate",
                "skills/atomic/text_summarize.yaml",
                "--output",
                str(tmp_path / "m"),
            )
            == 0
        )
        assert (tmp_path / "m").exists()

    def test_init_and_conflict(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        assert run_cli(monkeypatch, "init", "demo-skill", "--output", str(tmp_path)) == 0
        assert (tmp_path / "demo-skill" / "SKILL.md").exists()
        assert run_cli(monkeypatch, "init", "demo-skill", "--output", str(tmp_path)) == 1
        assert run_cli(monkeypatch, "init", "demo-skill", "--output", str(tmp_path), "--force") == 0

    def test_inspect_export_import(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        assert run_cli(monkeypatch, "inspect", "skills/agent-skills/code-review") == 0
        assert (
            run_cli(
                monkeypatch,
                "export-skill",
                "skills/atomic/text_summarize.yaml",
                "--output",
                str(tmp_path),
            )
            == 0
        )
        exported = tmp_path / "文本摘要"
        assert not exported.exists()  # name is slugified
        dirs = [p for p in tmp_path.iterdir() if (p / "SKILL.md").exists()]
        assert dirs
        assert run_cli(monkeypatch, "import-skill", str(dirs[0])) == 0


class TestBuildRunEval:
    def test_convert(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        assert (
            run_cli(
                monkeypatch,
                "convert",
                "examples/customer_service_sop.md",
                "--output",
                str(tmp_path / "gen"),
            )
            == 0
        )
        assert list((tmp_path / "gen").glob("*.yaml"))

    def test_build_success_and_empty(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        assert (
            run_cli(
                monkeypatch,
                "build",
                "examples/customer_service_sop.md",
                "--output",
                str(tmp_path / "b"),
            )
            == 0
        )
        assert (tmp_path / "b" / "build-report.json").exists()
        empty = tmp_path / "empty.md"
        empty.write_text("# 标题\n\n没有步骤。", encoding="utf-8")
        assert run_cli(monkeypatch, "build", str(empty), "--output", str(tmp_path / "b2")) == 1

    def test_run_success_and_unknown(
        self, monkeypatch: pytest.MonkeyPatch, skill_file: Path, tmp_path: Path
    ) -> None:
        rc = run_cli(monkeypatch, "run", str(skill_file), "--runs-dir", str(tmp_path / "runs"))
        assert rc == 0
        assert (
            run_cli(
                monkeypatch,
                "run",
                "ghost-skill-xyz",
                "--library",
                "skills",
                "--runs-dir",
                str(tmp_path / "runs"),
            )
            == 1
        )

    def test_run_with_audit_trail_written(
        self, monkeypatch: pytest.MonkeyPatch, skill_file: Path, tmp_path: Path
    ) -> None:
        audit_path = tmp_path / "audit.jsonl"
        rc = run_cli(
            monkeypatch,
            "run",
            str(skill_file),
            "--runs-dir",
            str(tmp_path / "runs"),
            "--audit",
            str(audit_path),
        )
        assert rc == 0
        assert audit_path.exists()
        # and readable via the audit command
        assert run_cli(monkeypatch, "audit", str(audit_path)) == 0

    def test_eval_markdown_and_json(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        out = tmp_path / "report.json"
        rc = run_cli(
            monkeypatch,
            "eval",
            "--skill",
            "skills/atomic/text_summarize.yaml",
            "--suite",
            "evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json",
            "--format",
            "json",
            "--output",
            str(out),
        )
        assert rc == 0 and json.loads(out.read_text())["metrics"]

    def test_eval_mock_response_deterministic_pass(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        out = tmp_path / "r.json"
        rc = run_cli(
            monkeypatch,
            "eval",
            "--skill",
            "skills/atomic/text_summarize.yaml",
            "--suite",
            "evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json",
            "--mock-response",
            '{"summary": "s", "key_points": ["k"]}',
            "--format",
            "json",
            "--output",
            str(out),
        )
        assert rc == 0
        data = json.loads(out.read_text())
        assert data["assisted_success_rate"] == 1.0
        assert data["metrics"]["security_probe_pass_rate"] == 1.0

    def test_eval_models_matrix(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rc = run_cli(
            monkeypatch,
            "eval",
            "--skill",
            "skills/atomic/text_summarize.yaml",
            "--suite",
            "evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json",
            "--models",
            "model-a,model-b",
            "--format",
            "json",
        )
        assert rc == 0

    def test_eval_gate_blocks_regression(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        previous = {
            "assisted_detail": {
                "normal-001": {"passed": True},
                "boundary-empty-001": {"passed": True},
                "security-injection-001": {"passed": True},
            },
            "assisted_success_rate": 1.0,
        }
        prev_path = tmp_path / "prev.json"
        prev_path.write_text(json.dumps(previous), encoding="utf-8")
        # mock default returns "{}" -> all cases now fail -> gate must exit 1
        rc = run_cli(
            monkeypatch,
            "eval",
            "--skill",
            "skills/atomic/text_summarize.yaml",
            "--suite",
            "evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json",
            "--compare",
            str(prev_path),
            "--gate",
        )
        assert rc == 1

    def test_gate_requires_compare(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rc = run_cli(
            monkeypatch,
            "eval",
            "--skill",
            "skills/atomic/text_summarize.yaml",
            "--suite",
            "evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json",
            "--gate",
        )
        assert rc == 2

    def test_test_command(
        self, monkeypatch: pytest.MonkeyPatch, skill_file: Path, tmp_path: Path
    ) -> None:
        suite = {
            "skill": "uskill-atomic-cli-fixture-v1-0-0",
            "version": "1.0.0",
            "cases": [{"task_id": "t1", "user_input": {}, "assertions": []}],
        }
        suite_path = tmp_path / "s.json"
        suite_path.write_text(json.dumps(suite), encoding="utf-8")
        assert (
            run_cli(monkeypatch, "test", "--skill", str(skill_file), "--suite", str(suite_path))
            == 0
        )
        suite["cases"][0]["assertions"] = [{"type": "json_key", "key": "never"}]
        suite_path.write_text(json.dumps(suite), encoding="utf-8")
        assert (
            run_cli(monkeypatch, "test", "--skill", str(skill_file), "--suite", str(suite_path))
            == 1
        )
        # scripted mock response satisfies the assertion (deterministic CI path)
        assert (
            run_cli(
                monkeypatch,
                "test",
                "--skill",
                str(skill_file),
                "--suite",
                str(suite_path),
                "--mock-response",
                '{"never": 1}',
            )
            == 0
        )


class TestGovernanceCommands:
    def test_search_found_and_not_found(self, monkeypatch: pytest.MonkeyPatch) -> None:
        assert run_cli(monkeypatch, "search", "nlp", "--mode", "tag") == 0
        assert run_cli(monkeypatch, "search", "zzz-nothing-matches", "--json") == 1

    def test_list(self, monkeypatch: pytest.MonkeyPatch, capsys) -> None:
        assert run_cli(monkeypatch, "list", "skills") == 0
        assert "uskill-atomic-text-summarize" in capsys.readouterr().out

    def test_list_json_filtered(self, monkeypatch: pytest.MonkeyPatch, capsys) -> None:
        assert run_cli(monkeypatch, "list", "skills", "--filter", "translate", "--json") == 0
        data = json.loads(capsys.readouterr().out)
        assert any("translate" in d["skill_id"] for d in data)

    def test_risk_and_package(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        assert run_cli(monkeypatch, "risk", "skills/", "--json") == 0
        assert (
            run_cli(
                monkeypatch,
                "package",
                "skills/agent-skills/code-review",
                "--output",
                str(tmp_path / "dist"),
            )
            == 0
        )
        zips = list((tmp_path / "dist").glob("*.zip"))
        assert zips
        assert (
            run_cli(
                monkeypatch,
                "package",
                "skills/agent-skills/code-review",
                "--output",
                str(tmp_path / "dist"),
            )
            == 1
        )  # no overwrite

    def test_audit_displays_redacted(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys
    ) -> None:
        path = tmp_path / "audit.jsonl"
        audit = AuditLogger(path)
        audit.log("run_started", run_id="run-1", api_key="sk-secret-999")
        assert run_cli(monkeypatch, "audit", str(path), "--json") == 0
        out = capsys.readouterr().out
        assert "sk-secret-999" not in out and "REDACTED" in out
        assert run_cli(monkeypatch, "audit", str(tmp_path / "missing.jsonl")) == 1
