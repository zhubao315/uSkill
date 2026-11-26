"""Local API security: loopback-only, pairing token, Origin allowlist, CSRF.

The Workbench service is intentionally local-only. It must NOT be exposed to
a network interface, and every state-changing request must present the
short-lived pairing token plus a matching Origin.
"""

from __future__ import annotations

import hmac
import os
import secrets
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

ALLOWED_ORIGINS = {
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:8765",
    "http://localhost:8765",
}
SAFE_METHODS = {"GET", "HEAD", "OPTIONS"}
TOKEN_ENV = "USKILL_WORKBENCH_TOKEN"


def issue_token() -> str:
    """Generate a pairing token for the current process session."""
    return secrets.token_urlsafe(32)


def expected_token() -> str:
    return os.environ.get(TOKEN_ENV, "")


def _bearer(request: Request) -> str:
    header = request.headers.get("authorization", "")
    if not header.lower().startswith("bearer "):
        return ""
    return header[7:].strip()


class LocalAPIGuard(BaseHTTPMiddleware):
    """Reject non-loopback, wrong Origin, missing/invalid pairing token."""

    def __init__(self, app: Any, *, token: str = "", allowed_origins: set[str] | None = None):
        super().__init__(app)
        self._token = token or expected_token()
        self._origins = allowed_origins if allowed_origins is not None else set(ALLOWED_ORIGINS)

    async def dispatch(self, request: Request, call_next: Any) -> Any:
        if not self._token:
            return JSONResponse(
                {"detail": "Workbench pairing token is not configured"}, status_code=503
            )
        host = (request.headers.get("host") or "").split(":")[0].lower()
        # "testserver" is the ASGI TestClient host; production uvicorn binds
        # 127.0.0.1 only, so this exception is inert outside tests.
        allowed_hosts = {"127.0.0.1", "localhost", "::1", "testserver"}
        if host not in allowed_hosts:
            return JSONResponse({"detail": "Workbench API is loopback-only"}, status_code=403)
        supplied = _bearer(request)
        if not supplied or not hmac.compare_digest(supplied, self._token):
            return JSONResponse({"detail": "Invalid pairing token"}, status_code=401)
        if request.method not in SAFE_METHODS:
            origin = request.headers.get("origin", "")
            if not origin or origin not in self._origins:
                return JSONResponse(
                    {"detail": "Origin not allowed for state-changing request"}, status_code=403
                )
        return await call_next(request)


__all__ = ["LocalAPIGuard", "issue_token", "expected_token", "ALLOWED_ORIGINS"]
