"""Run the local Workbench service: `uskills workbench`."""

from __future__ import annotations

import contextlib
import os
import socket
import webbrowser
from pathlib import Path

from .app import create_app
from .security import issue_token


def free_port(start: int = 8765) -> int:
    for port in range(start, start + 20):
        with socket.socket() as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise RuntimeError("no free loopback port found")


def run(
    *,
    skills: str = "skills",
    runs_dir: str = ".uskills/runs",
    static: str | None = None,
    open_browser: bool = True,
) -> int:
    import uvicorn

    token = issue_token()
    os.environ["USKILL_WORKBENCH_TOKEN"] = token
    port = free_port()
    web_dir = Path(static) if static else Path(__file__).resolve().parents[1] / "web" / "dist"
    app = create_app(
        skills_root=skills,
        runs_dir=runs_dir,
        static_dir=web_dir if web_dir.is_dir() else None,
        token=token,
    )
    url = f"http://127.0.0.1:{port}/?token={token}"
    print(f"uSkill Workbench  ->  {url}")
    print("Loopback only. Press Ctrl+C to stop.")
    if open_browser and web_dir.is_dir():
        with contextlib.suppress(Exception):
            webbrowser.open(url)
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")
    return 0
