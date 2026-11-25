"""Audit logging: append-only JSONL trail of runtime actions.

Privacy by default (SECURITY.md policy): values under sensitive keys
(``*token*``, ``*secret*``, ``*key*``, ``*password*``, ``*credential*``)
are masked, and large free-form values (``input``/``prompt``/``output``)
are stored as ``{sha256, length}`` digests, not raw text. Full inputs live
in RunRecords under operator-controlled paths, never in the audit trail.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

_SENSITIVE_KEY = re.compile(r"token|secret|key|password|credential|api[-_]?hdr", re.I)
_BULK_KEYS = re.compile(r"^(input|inputs|prompt|output|outputs|text|body)$", re.I)
_MASK = "***REDACTED***"


def redact(value: Any, *, key: str = "") -> Any:
    """Recursively mask sensitive values for audit storage."""
    if key and _SENSITIVE_KEY.search(key):
        return _MASK
    if key and _BULK_KEYS.match(key) and isinstance(value, str | dict | list):
        text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
        return {
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
            "length": len(text),
            "note": "bulk value stored as digest",
        }
    if isinstance(value, dict):
        return {k: redact(v, key=str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    return value


class AuditLogger:
    """Append-only audit trail.

    Every permission check, tool invocation, approval decision and run
    transition should be recorded so execution is traceable after the fact.
    Detail payloads pass through :func:`redact` before storage.
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
            **{k: redact(v, key=k) for k, v in detail.items()},
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


__all__ = ["AuditLogger", "redact"]
