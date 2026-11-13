"""MCP bridge: register MCP-provided tools into the uSkill ToolRegistry.

MCP ≠ Skill. MCP supplies *connections* (external tools/data); a Skill
captures *how to work*. This bridge is the single integration point: it
maps MCP tool declarations (name / description / inputSchema) into
governed ``ToolDef`` entries. Transport stays with the caller's MCP
client session (e.g. the ``mcp`` SDK) — this module deliberately has no
network behaviour and no MCP SDK dependency, so it is fully testable
offline.

Security posture: MCP tools are EXTERNAL side effects. They default to
the ``network`` permission (least-privilege runtimes deny them until
explicitly granted) and ``idempotent=False`` unless the caller declares
idempotency, so retries can never duplicate them.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Any

from core.uskills.governance.policy import Permission
from core.uskills.runtime.tools import ToolDef, ToolRegistry

Dispatch = Callable[[str, dict[str, Any]], Any]


def mcp_tool_id(name: str) -> str:
    return f"mcp:{name}"


def register_mcp_tool(
    registry: ToolRegistry,
    tool_spec: dict[str, Any],
    *,
    dispatch: Dispatch,
    permission: Permission = Permission.network,
    idempotent: bool = False,
    timeout: float | None = 30.0,
    prefix: str = "mcp",
) -> ToolDef:
    """Register one MCP tool declaration: {name, description, inputSchema}.

    ``dispatch(name, arguments)`` is the caller's bridge to the MCP client
    session (e.g. ``session.call_tool``).
    """
    name = str(tool_spec.get("name", "")).strip()
    if not name:
        raise ValueError("MCP tool spec requires a non-empty 'name'")
    input_schema = tool_spec.get("inputSchema") or tool_spec.get("input_schema")

    def handler(payload: dict[str, Any]) -> Any:
        return dispatch(name, dict(payload))

    tool = ToolDef(
        id=f"{prefix}:{name}",
        description=str(tool_spec.get("description", ""))[:500],
        func=handler,
        permission=permission,
        input_schema=input_schema if isinstance(input_schema, dict) else None,
        timeout=timeout,
        idempotent=idempotent,
        metadata={"source": "mcp", "mcp_name": name},
    )
    registry.register(tool)
    return tool


def register_mcp_tools(
    registry: ToolRegistry,
    tools: Sequence[dict[str, Any]],
    *,
    dispatch: Dispatch,
    permission: Permission = Permission.network,
    idempotent: bool = False,
) -> list[ToolDef]:
    """Register a whole MCP ``tools/list`` result."""
    return [
        register_mcp_tool(
            registry, spec, dispatch=dispatch,
            permission=permission, idempotent=idempotent,
        )
        for spec in tools
    ]


__all__ = ["mcp_tool_id", "register_mcp_tool", "register_mcp_tools"]
