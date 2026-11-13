"""Audit logging: append-only JSONL trail of runtime actions."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class AuditLogger:
    """Append-only audit trail.

    Every permission check, tool invocation, approval decision and run
    transition should be recorded so execution is traceable after the fact.
    """

    def __init__(self, path: str | Path | None = None):
        self.path = Path(path) if path else None
        self.memory: list[dict[str, Any]] = []
        if self.path:
            self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, action: str, *, run_id: str = "", skill_id: str = "", **detail: Any) -> None:
        entry = {
            "time": datetime.now(UTC).isoformat(),
            "action": action,
            "run_id": run_id,
            "skill_id": skill_id,
            **detail,
        }
        self.memory.append(entry)
        if self.path:
            with self.path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def read(self) -> list[dict[str, Any]]:
        if self.path and self.path.exists():
            return [
                json.loads(line)
                for line in self.path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
        return list(self.memory)


__all__ = ["AuditLogger"]
