"""Provider abstraction for uSkill Runtime.

Core code never binds to a specific model vendor: everything goes through
the :class:`Provider` protocol. Ships with a Mock provider (for tests, no
API key needed), an OpenAI Chat Completions provider, and an OpenAI
Responses API provider. Any OpenAI-compatible gateway works by passing a
custom ``base_url``.
"""

from __future__ import annotations

import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from ..errors import ProviderError


@dataclass
class ProviderCapabilities:
    """Declared capabilities of a provider."""

    json_mode: bool = True
    structured_output: bool = False
    function_calling: bool = False
    streaming: bool = False


@dataclass
class ProviderResponse:
    """Normalized provider response."""

    text: str
    model: str
    usage: dict[str, Any] = field(default_factory=dict)
    finish_reason: str | None = None


@dataclass
class Message:
    """Minimal chat message."""

    role: str
    content: str

    def to_dict(self) -> dict[str, str]:
        return {"role": self.role, "content": self.content}


@runtime_checkable
class Provider(Protocol):
    """Protocol every provider must implement."""

    name: str
    capabilities: ProviderCapabilities

    def complete(
        self,
        messages: Sequence[Message],
        *,
        model: str,
        temperature: float = 0.1,
        json_mode: bool = False,
        timeout: float = 30.0,
        json_schema: dict[str, Any] | None = None,
    ) -> ProviderResponse:
        """Run one completion. Must raise ProviderError on failure.

        When ``json_schema`` is given, providers should constrain output to
        that schema (structured outputs); ``json_mode`` is the weaker
        JSON-object fallback.
        """
        ...


class MockProvider:
    """Scripted provider for tests and offline evaluation.

    ``script`` may be a single string, a list of strings consumed in
    order, or a callable ``f(call_index) -> str``. Errors can be scripted
    with ``errors`` (exception raised on those call indices).
    """

    name = "mock"

    def __init__(
        self,
        script: str | Sequence[str] | Callable[[int], str] = "{}",
        errors: dict[int, Exception] | None = None,
        delay: float = 0.0,
        capabilities: ProviderCapabilities | None = None,
    ) -> None:
        self.script = script
        self.errors = errors or {}
        self.delay = delay
        self.capabilities = capabilities or ProviderCapabilities(json_mode=True)
        self.calls: list[dict[str, Any]] = []

    def complete(
        self,
        messages: Sequence[Message],
        *,
        model: str,
        temperature: float = 0.1,
        json_mode: bool = False,
        timeout: float = 30.0,
        json_schema: dict[str, Any] | None = None,
    ) -> ProviderResponse:
        idx = len(self.calls)
        self.calls.append(
            {
                "index": idx,
                "messages": [m.to_dict() for m in messages],
                "model": model,
                "temperature": temperature,
                "json_mode": json_mode,
                "json_schema": json_schema,
            }
        )
        if self.delay:
            time.sleep(self.delay)
        if idx in self.errors:
            raise self.errors[idx]

        if callable(self.script):
            text = self.script(idx)
        elif isinstance(self.script, str):
            text = self.script
        else:
            text = self.script[idx] if idx < len(self.script) else self.script[-1]

        return ProviderResponse(
            text=text,
            model=model,
            usage={
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            finish_reason="stop",
        )


class _OpenAIProviderBase:
    """Shared lazy-openai client handling."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        client: Any | None = None,
    ) -> None:
        if client is not None:
            self.client = client
            return
        from openai import OpenAI  # lazy import: keeps core openai-optional

        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def _classify(self, exc: Exception) -> ProviderError:
        try:
            from openai import (
                APIConnectionError,
                APITimeoutError,
                InternalServerError,
                RateLimitError,
            )

            retryable = isinstance(
                exc, (APITimeoutError, APIConnectionError, RateLimitError, InternalServerError)
            )
        except ImportError:  # pragma: no cover
            retryable = False
        return ProviderError(f"provider error: {exc}", retryable=retryable)


class OpenAIChatProvider(_OpenAIProviderBase):
    """OpenAI Chat Completions API (and compatible gateways)."""

    name = "openai-chat"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.capabilities = ProviderCapabilities(
            json_mode=True, structured_output=True, function_calling=True
        )

    def complete(
        self,
        messages: Sequence[Message],
        *,
        model: str,
        temperature: float = 0.1,
        json_mode: bool = False,
        timeout: float = 30.0,
        json_schema: dict[str, Any] | None = None,
    ) -> ProviderResponse:
        kwargs: dict[str, Any] = {
            "model": model,
            "messages": [m.to_dict() for m in messages],
            "temperature": temperature,
            "timeout": timeout,
        }
        if json_schema is not None:
            kwargs["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "uskills_output",
                    "schema": json_schema,
                    "strict": False,
                },
            }
        elif json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        try:
            response = self.client.chat.completions.create(**kwargs)
        except ProviderError:
            raise
        except Exception as exc:
            raise self._classify(exc) from exc

        usage = response.usage.model_dump() if getattr(response, "usage", None) else {}
        return ProviderResponse(
            text=response.choices[0].message.content or "",
            model=response.model,
            usage=usage,
            finish_reason=response.choices[0].finish_reason,
        )


class OpenAIResponsesProvider(_OpenAIProviderBase):
    """OpenAI Responses API adapter (the recommended modern interface)."""

    name = "openai-responses"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.capabilities = ProviderCapabilities(
            json_mode=True, structured_output=True, function_calling=True, streaming=True
        )

    def complete(
        self,
        messages: Sequence[Message],
        *,
        model: str,
        temperature: float = 0.1,
        json_mode: bool = False,
        timeout: float = 30.0,
        json_schema: dict[str, Any] | None = None,
    ) -> ProviderResponse:
        instructions = "\n\n".join(m.content for m in messages if m.role == "system")
        payload = [m.to_dict() for m in messages if m.role != "system"]
        kwargs: dict[str, Any] = {
            "model": model,
            "input": payload,
            "temperature": temperature,
            "timeout": timeout,
        }
        if instructions:
            kwargs["instructions"] = instructions
        if json_schema is not None:
            kwargs["text"] = {
                "format": {
                    "type": "json_schema",
                    "name": "uskills_output",
                    "schema": json_schema,
                    "strict": False,
                }
            }
        elif json_mode:
            kwargs["text"] = {"format": {"type": "json_object"}}
        try:
            response = self.client.responses.create(**kwargs)
        except ProviderError:
            raise
        except Exception as exc:
            raise self._classify(exc) from exc

        usage_obj = getattr(response, "usage", None)
        usage = usage_obj.model_dump() if usage_obj is not None else {}
        return ProviderResponse(
            text=getattr(response, "output_text", "") or "",
            model=getattr(response, "model", model),
            usage=usage,
            finish_reason=getattr(response, "status", None),
        )


def create_provider(kind: str, **kwargs: Any) -> Provider:
    """Factory for known providers.

    Args:
        kind: one of ``mock``, ``openai-chat``, ``openai-responses``.
    """
    if kind == "mock":
        return MockProvider(**kwargs)
    if kind == "openai-chat":
        return OpenAIChatProvider(**kwargs)
    if kind == "openai-responses":
        return OpenAIResponsesProvider(**kwargs)
    raise ValueError(f"Unknown provider kind: {kind!r}")


__all__ = [
    "Provider",
    "ProviderCapabilities",
    "ProviderResponse",
    "Message",
    "MockProvider",
    "OpenAIChatProvider",
    "OpenAIResponsesProvider",
    "create_provider",
]
