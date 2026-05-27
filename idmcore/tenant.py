"""
Tenant metadata holder used by the cache and the diagnostics dump.
"""

from __future__ import annotations

from typing import Dict


class Tenant:
    def __init__(self, tenant_id: str, label: str) -> None:
        self.tenant_id = tenant_id
        self.label = label
        self._counters: Dict[str, int] = {}

    def bump(self, name: str) -> int:
        self._counters[name] = self._counters.get(name, 0) + 1
        return self._counters[name]

    def counter(self, name: str) -> int:
        return self._counters.get(name, 0)

    def __repr__(self) -> str:
        return f"Tenant({self.tenant_id!r}, {self.label!r})"
