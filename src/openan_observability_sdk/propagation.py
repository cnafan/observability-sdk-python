from __future__ import annotations

from collections.abc import Mapping, MutableMapping
from contextlib import contextmanager
from typing import Iterator

from opentelemetry.context import Context, attach, detach
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator


class TraceContextPropagation:
    """W3C Trace Context helpers for caller-owned text carriers such as HTTP headers."""

    _propagator = TraceContextTextMapPropagator()

    @classmethod
    def inject(cls, carrier: MutableMapping[str, str]) -> MutableMapping[str, str]:
        """Write the current W3C trace context into ``carrier`` and return it."""

        if carrier is None:
            raise ValueError("carrier is required")
        cls._propagator.inject(carrier)
        return carrier

    @classmethod
    @contextmanager
    def extract_to_current(cls, carrier: Mapping[str, str]) -> Iterator[Context]:
        """Extract W3C headers and make the resulting context current in a ``with`` block."""

        if carrier is None:
            raise ValueError("carrier is required")
        extracted = cls._propagator.extract(carrier)
        token = attach(extracted)
        try:
            yield extracted
        finally:
            detach(token)
