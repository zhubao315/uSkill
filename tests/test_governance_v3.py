"""Tests for 3.0 governance: lifecycle persistence and run retention."""

from __future__ import annotations

import json

from core.uskills.governance.lifecycle import (
    LifecycleError,
    SkillLifecycle,
    assert_transition,
)
from core.uskills.manifest import USkillManifest
from core.uskills.runtime.state import (
    RunRecord,
    RunRetentionPolicy,
    RunStore,
    redact_run,
)


def _manifest() -> USkillManifest:
    return USkillManifest(
        metadata={"name": "demo", "description": "Demo skill", "version": "1.0.0"},
    )


def test_manifest_persists_lifecycle_status() -> None:
    m = _manifest()
    assert m.governance.status == SkillLifecycle.DRAFT
    assert "governance" in m.model_dump()
    m.governance.status = SkillLifecycle.VALIDATED
    assert m.governance.status == SkillLifecycle.VALIDATED
    restored = USkillManifest.model_validate_json(m.model_dump_json())
    assert restored.governance.status == SkillLifecycle.VALIDATED


def test_lifecycle_transition_guard() -> None:
    assert_transition(SkillLifecycle.DRAFT, SkillLifecycle.VALIDATED)
    try:
        assert_transition(SkillLifecycle.DRAFT, SkillLifecycle.PUBLISHED)
    except LifecycleError:
        pass
    else:
        raise AssertionError("illegal transition should fail")


def test_redaction_masks_sensitive_keys() -> None:
    data = {"api_key": "secret", "inputs": {"text": "hello"}, "status": "ok"}
    out = redact_run(data, RunRetentionPolicy.REDACTED)
    assert out["api_key"] == "[REDACTED]"
    assert out["inputs"]["text"] == "hello"
    assert out["status"] == "ok"


def test_metadata_only_digests_bulk_fields() -> None:
    data = {"inputs": {"text": "hello"}, "outputs": {"result": "world"}}
    out = redact_run(data, RunRetentionPolicy.METADATA_ONLY)
    assert "sha256" in out["inputs"]
    assert "sha256" in out["outputs"]
    assert "hello" not in json.dumps(out)


def test_disabled_policy_minimal_record() -> None:
    out = redact_run({"run_id": "r1", "inputs": {"x": 1}}, RunRetentionPolicy.DISABLED)
    assert out == {"run_id": "r1", "status": "", "started_at": None, "finished_at": None}


def test_runstore_full_default_backward_compatible(tmp_path) -> None:  # noqa: ANN001
    store = RunStore(tmp_path)
    rec = RunRecord(run_id="run-x", skill_id="s", inputs={"text": "hello"})
    path = store.save(rec)
    assert path is not None
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["inputs"]["text"] == "hello"


def test_runstore_redacted_policy(tmp_path) -> None:  # noqa: ANN001
    store = RunStore(tmp_path, retention=RunRetentionPolicy.REDACTED)
    rec = RunRecord(run_id="run-y", skill_id="s")
    rec.inputs = {"api_key": "secret", "text": "hello"}
    path = store.save(rec)
    assert path is not None
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["inputs"]["api_key"] == "[REDACTED]"
    assert data["inputs"]["text"] == "hello"
