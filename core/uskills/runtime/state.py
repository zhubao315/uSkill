"""Execution state model for uSkill Runtime.

Every run gets a unique Run ID and every step keeps a full record:
input, output, status, timings, usage, error and retry history.
RunRecord is JSON serializable so long-running tasks are checkpointed on
disk rather than kept only in memory.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any


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
    WAITING_APPROVAL = "WAITING_APPROVAL"


TERMINAL_STATES = {
    StepState.COMPLETED,
    StepState.FAILED,
    StepState.SKIPPED,
    StepState.INTERRUPTED,
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

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, record: RunRecord) -> Path:
        path = self.root / f"{record.run_id}.json"
        path.write_text(
            json.dumps(record.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return path

    def load(self, run_id: str) -> RunRecord:
        path = self.root / f"{run_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"No run record for run_id: {run_id}")
        return RunRecord.from_dict(json.loads(path.read_text(encoding="utf-8")))

    def list_runs(self) -> list[str]:
        return sorted(p.stem for p in self.root.glob("run-*.json"))


__all__ = [
    "StepState",
    "TERMINAL_STATES",
    "StepRun",
    "RunRecord",
    "RunStore",
    "new_run_id",
]
