"""Backward-compatible executor shim over the new runtime.

``SkillExecutor`` keeps its historic API (``execute(skill, inputs)``
returning a legacy-shaped dict) but now delegates to the governed
:class:`~core.uskills.runtime.engine.SkillRuntime`, so ``control.timeout``
and ``control.retry`` are genuinely enforced. New code should use
``SkillRuntime`` directly.
"""

from __future__ import annotations

import os
from typing import Any

from .errors import ExecutionFailedError
from .runtime import (
    MockProvider,
    OpenAIChatProvider,
    Provider,
    SkillRuntime,
    StepState,
)
from .schema import USkill


class SkillExecutor:
    """Legacy facade over the governed runtime."""

    def __init__(
        self,
        api_key: str | None = None,
        default_model: str = "gpt-4o-mini",
        base_url: str | None = None,
        provider: Provider | None = None,
    ) -> None:
        self.default_model = default_model
        if provider is not None:
            self._runtime = SkillRuntime(provider)
        elif api_key is not None or os.getenv("OPENAI_API_KEY"):
            self._runtime = SkillRuntime(OpenAIChatProvider(api_key=api_key, base_url=base_url))
        else:
            self._runtime = SkillRuntime(MockProvider())
        self.provider = self._runtime.provider

    def execute(self, skill: USkill, inputs: dict[str, Any]) -> dict[str, Any]:
        """Execute a skill and return the legacy result envelope.

        Raises ExecutionFailedError when the governed run fails (the old
        shim used to print a warning and return unparsed text instead).
        """
        if isinstance(self.provider, MockProvider) and not skill.control.mockable:
            raise ExecutionFailedError(
                f"skill {skill.skill_id} is not mockable and no real provider is configured"
            )
        record = self._runtime.run(skill, inputs)
        if record.status is not StepState.COMPLETED:
            raise ExecutionFailedError(
                f"run {record.run_id} ended in {record.status.value}: {record.error}"
            )
        return {
            "skill_id": skill.skill_id,
            "result": record.result,
            "run_id": record.run_id,
            "status": record.status.value,
            "steps": [s.step_id for s in record.steps],
            "events": record.events,
            "meta": {
                "execution_time": record.execution_time,
                "model": skill.execute.model,
                "usage": record.usage,
            },
        }


__all__ = ["SkillExecutor"]
