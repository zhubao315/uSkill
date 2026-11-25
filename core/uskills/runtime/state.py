"""Execution state model for uSkill Runtime.

Every run gets a unique Run ID and every step keeps a full record:
input, output, status, timings, usage, error and retry history.
RunRecord is JSON serializable so long-running tasks are checkpointed on
disk rather than kept only in memory.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import re
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any


class RunRetentionPolicy(StrEnum):
    METADATA_ONLY = "metadata_only"
    REDACTED = "redacted"
    FULL = "full"
    DISABLED = "disabled"


_SENSITIVE_KEY = re.compile(
    r"token|secret|password|credential|api[_-]?key|authorization|cookie", re.I
)
_BULK_KEY = re.compile(r"input|output|prompt|text|body|result|content", re.I)


def _digest(value: Any) -> dict[str, Any]:
    text = (
        value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
    )
    return {"sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "length": len(text)}


def redact_run(data: dict[str, Any], policy: RunRetentionPolicy) -> dict[str, Any]:
    """Return a copy of a run record according to a retention policy."""
    if policy == RunRetentionPolicy.FULL:
        return data
    if policy == RunRetentionPolicy.DISABLED:
        return {
            "run_id": data.get("run_id", ""),
            "status": data.get("status", ""),
            "started_at": data.get("started_at"),
            "finished_at": data.get("finished_at"),
        }

    def walk(value: Any) -> Any:
        if isinstance(value, dict):
            out: dict[str, Any] = {}
            for k, v in value.items():
                if _SENSITIVE_KEY.search(k):
                    out[k] = "[REDACTED]"
                elif policy == RunRetentionPolicy.METADATA_ONLY and _BULK_KEY.search(k):
                    out[k] = _digest(v)
                else:
                    out[k] = walk(v)
            return out
        if isinstance(value, list):
            return [walk(v) for v in value]
        return value

    result: dict[str, Any] = walk(data)
    return result


class StepState(StrEnum):
    """Lifecycle states of a run or step."""

    PENDING = "PENDING"
    READY = "READY"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    RETRYING = "RETRYING"
    INTERRUPTED = "INTERRUPTED"
    CANCELLED = "CANCELLED"
    WAITING_APPROVAL = "WAITING_APPROVAL"


TERMINAL_STATES = {
    StepState.COMPLETED,
    StepState.FAILED,
    StepState.SKIPPED,
    StepState.INTERRUPTED,
    StepState.CANCELLED,
}


def _now() -> str:
    return datetime.now(UTC).isoformat()


def new_run_id() -> str:
    return f"run-{uuid.uuid4().hex[:12]}"


@dataclass
class StepRun:
    """Record of one executed step."""

    step_id: str
    kind: str  # "llm" | "subskill" | "tool"
    via: str = ""  # "tool" when a subskill-declared step resolved to a registered tool
    status: StepState = StepState.PENDING
    input: Any = None
    output: Any = None
    error: str | None = None
    started_at: str | None = None
    finished_at: str | None = None
    attempts: int = 0
    retry_errors: list[str] = field(default_factory=list)
    usage: dict[str, Any] | None = None
    execution_time: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "step_id": self.step_id,
            "kind": self.kind,
            "via": self.via,
            "status": self.status.value,
            "input": self.input,
            "output": self.output,
            "error": self.error,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "attempts": self.attempts,
            "retry_errors": self.retry_errors,
            "usage": self.usage,
            "execution_time": self.execution_time,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> StepRun:
        run = cls(step_id=data["step_id"], kind=data["kind"])
        run.via = data.get("via", "")
        run.status = StepState(data["status"])
        run.input = data.get("input")
        run.output = data.get("output")
        run.error = data.get("error")
        run.started_at = data.get("started_at")
        run.finished_at = data.get("finished_at")
        run.attempts = data.get("attempts", 0)
        run.retry_errors = data.get("retry_errors", [])
        run.usage = data.get("usage")
        run.execution_time = data.get("execution_time")
        return run


@dataclass
class RunRecord:
    """Full record of one skill execution."""

    run_id: str
    skill_id: str
    status: StepState = StepState.PENDING
    inputs: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, Any] = field(default_factory=dict)
    steps: list[StepRun] = field(default_factory=list)
    events: list[dict[str, Any]] = field(default_factory=list)
    error: str | None = None
    started_at: str | None = None
    finished_at: str | None = None
    usage: dict[str, Any] = field(default_factory=dict)
    execution_time: float | None = None
    result: Any = None

    def add_event(self, event: str, **data: Any) -> None:
        self.events.append({"time": _now(), "event": event, **data})

    @property
    def total_tokens(self) -> int:
        return int(self.usage.get("total_tokens", 0) or 0)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "skill_id": self.skill_id,
            "status": self.status.value,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "steps": [s.to_dict() for s in self.steps],
            "events": self.events,
            "error": self.error,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "usage": self.usage,
            "execution_time": self.execution_time,
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RunRecord:
        record = cls(run_id=data["run_id"], skill_id=data["skill_id"])
        record.status = StepState(data["status"])
        record.inputs = data.get("inputs", {})
        record.outputs = data.get("outputs", {})
        record.steps = [StepRun.from_dict(s) for s in data.get("steps", [])]
        record.events = data.get("events", [])
        record.error = data.get("error")
        record.started_at = data.get("started_at")
        record.finished_at = data.get("finished_at")
        record.usage = data.get("usage", {})
        record.execution_time = data.get("execution_time")
        record.result = data.get("result")
        return record


class RunStore:
    """Filesystem-backed checkpoint store for run records."""

    def __init__(
        self, root: str | Path, *, retention: RunRetentionPolicy = RunRetentionPolicy.FULL
    ):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.retention = retention

    def save(self, record: RunRecord) -> Path | None:
        if self.retention == RunRetentionPolicy.DISABLED:
            return None
        data = redact_run(record.to_dict(), self.retention)
        path = self.root / f"{record.run_id}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        with contextlib.suppress(OSError):
            os.chmod(path, 0o600)
        return path

    def load(self, run_id: str) -> RunRecord:
        path = self.root / f"{run_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"No run record for run_id: {run_id}")
        return RunRecord.from_dict(json.loads(path.read_text(encoding="utf-8")))

    def list_runs(self) -> list[str]:
        return sorted(p.stem for p in self.root.glob("run-*.json"))


class CancelToken:
    """Cooperative cancellation signal for in-flight runs.

    The runtime checks the token between steps and between attempts, and
    while waiting on a provider call. A long-blocking vendor request cannot
    be killed from this process; it is still bounded by ``control.timeout``.
    """

    def __init__(self) -> None:
        self._cancelled = False
        self._reason = ""

    def cancel(self, reason: str = "cancelled by caller") -> None:
        self._cancelled = True
        self._reason = reason

    @property
    def cancelled(self) -> bool:
        return self._cancelled

    @property
    def reason(self) -> str:
        return self._reason


__all__ = [
    "StepState",
    "TERMINAL_STATES",
    "StepRun",
    "RunRecord",
    "RunStore",
    "CancelToken",
    "new_run_id",
]
