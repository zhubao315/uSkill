"""Tests for 3.0 publish gate and package verification."""

from __future__ import annotations

import json
import zipfile

from core.uskills.governance.release import check_publish_gate, content_hash, verify_package


def _skill(tmp_path, *, reviewed: bool = True, license_declared: bool = True, scripts: bool = False):
    d = tmp_path / "skill"
    d.mkdir(exist_ok=True)
    license_line = "license: MIT\n" if license_declared else ""
    (d / "SKILL.md").write_text(
        f"---\nname: demo\ndescription: Demo skill\n{license_line}---\n\n# Body\n",
        encoding="utf-8",
    )
    gov = 'governance:\n  status: reviewed\n  reviewer: alice\n' if reviewed else 'governance:\n  status: draft\n'
    (d / "uskill.yaml").write_text(
        f"apiVersion: uskills/v2\nkind: Skill\nmetadata:\n  name: demo\n{gov}", encoding="utf-8"
    )
    if scripts:
        (d / "scripts").mkdir(exist_ok=True)
        (d / "scripts" / "run.py").write_text("print('never auto-run')\n", encoding="utf-8")
    return d


def test_publish_gate_blocks_draft(tmp_path) -> None:  # noqa: ANN001
    d = _skill(tmp_path, reviewed=False)
    problems = check_publish_gate(d, evaluation_report={"metrics": {}, "regressions": []})
    assert any("lifecycle" in p for p in problems)


def test_publish_gate_passes_reviewed(tmp_path) -> None:  # noqa: ANN001
    d = _skill(tmp_path)
    problems = check_publish_gate(d, evaluation_report={"metrics": {}, "regressions": []})
    assert problems == []


def test_publish_gate_flags_scripts_without_executing(tmp_path) -> None:  # noqa: ANN001
    d = _skill(tmp_path, scripts=True)
    problems = check_publish_gate(d, evaluation_report={"metrics": {}, "regressions": []})
    assert any("executable script" in p for p in problems)
    assert (d / "scripts" / "run.py").exists()


def test_publish_gate_requires_evaluation(tmp_path) -> None:  # noqa: ANN001
    d = _skill(tmp_path)
    problems = check_publish_gate(d)
    assert any("evaluation" in p for p in problems)


def test_content_hash(tmp_path) -> None:  # noqa: ANN001
    d = _skill(tmp_path)
    h = content_hash(d)
    assert len(h) == 64
    assert h == content_hash(d / "SKILL.md")


def test_verify_package_good(tmp_path) -> None:  # noqa: ANN001
    archive = tmp_path / "skill.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("SKILL.md", "---\nname: demo\n---\n")
        z.writestr("package.json", json.dumps({"files": {"SKILL.md": {"sha256": "x"}}}))
    problems = verify_package(archive)
    assert any("checksum mismatch" in p for p in problems)


def test_verify_package_traversal(tmp_path) -> None:  # noqa: ANN001
    archive = tmp_path / "bad.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("../escape.txt", "bad")
    problems = verify_package(archive)
    assert any("unsafe path" in p for p in problems)
