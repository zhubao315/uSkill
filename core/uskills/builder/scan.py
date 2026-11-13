"""Static security scan for skill directories (import-time gate signal).

Scanning is a *signal*, not a sandbox: findings never block an import
silently — they surface in the import report, raise the derived risk
level, and mark the manifest as untrusted so deployment policy (not this
module) decides isolation. Scripts in imported skills are NEVER executed
by uSkill; they are only inspected here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from ..governance.risk import RiskLevel

# (id, pattern, human description, min risk when found)
_PATTERNS: list[tuple[str, re.Pattern[str], str, RiskLevel]] = [
    (
        "process-exec",
        re.compile(r"\bsubprocess\b|\bos\.system\b|\bpopen\b|child_process", re.I),
        "spawns processes",
        RiskLevel.L3,
    ),
    (
        "dynamic-code",
        re.compile(r"\beval\(|\bexec\(|Function\(|\|\s*import\(", re.I),
        "dynamic code execution",
        RiskLevel.L3,
    ),
    (
        "file-write",
        re.compile(r"\bopen\([^)]*['\"][wax]|writeFile|shutil\.rmtree|\brm\s+-rf\b", re.I),
        "writes or deletes files",
        RiskLevel.L3,
    ),
    (
        "network",
        re.compile(
            r"\brequests\b|urllib|httpx|socket\.|fetch\(|axios|http\.client", re.I
        ),
        "network access",
        RiskLevel.L4,
    ),
    (
        "env-secrets",
        re.compile(r"os\.environ|getenv|process\.env", re.I),
        "reads environment (may touch secrets)",
        RiskLevel.L4,
    ),
]

_SCAN_SUFFIXES = {".py", ".sh", ".bash", ".js", ".ts", ".mjs", ".rb", ".pl"}


@dataclass
class ScanFinding:
    file: str
    pattern_id: str
    description: str
    line_no: int
    line: str
    min_risk: RiskLevel

    def to_dict(self) -> dict[str, object]:
        return {
            "file": self.file,
            "pattern": self.pattern_id,
            "description": self.description,
            "line": self.line_no,
            "snippet": self.line.strip()[:120],
            "min_risk": f"L{int(self.min_risk)}",
        }


def scan_scripts(scripts_dir: str | Path, *, max_bytes: int = 200_000) -> list[ScanFinding]:
    """Statically scan every script file for high-risk capability patterns."""
    root = Path(scripts_dir)
    findings: list[ScanFinding] = []
    if not root.is_dir():
        return findings
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in _SCAN_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")[:max_bytes]
        except OSError:  # pragma: no cover
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("#"):
                continue  # comments are not capability
            for pid, pattern, desc, risk in _PATTERNS:
                if pattern.search(line):
                    findings.append(
                        ScanFinding(
                            file=str(path.relative_to(root)),
                            pattern_id=pid,
                            description=desc,
                            line_no=line_no,
                            line=line,
                            min_risk=risk,
                        )
                    )
    return findings


def scan_risk_level(findings: list[ScanFinding]) -> RiskLevel:
    """Derived floor risk implied by the findings."""
    if not findings:
        return RiskLevel.L0
    return max(f.min_risk for f in findings)


__all__ = ["ScanFinding", "scan_scripts", "scan_risk_level"]
