"""
Embedded script runtime. Adapters submit short Groovy-style snippets that get
parsed and compiled by the runtime before policy decisions reference them.
"""

from __future__ import annotations

from typing import Any, Dict


class GroovyError(Exception):
    pass


class GroovyValidator:
    def __init__(self) -> None:
        self._cache: Dict[str, Any] = {}

    def compile_validate(self, source: str) -> Dict[str, Any]:
        if not isinstance(source, str):
            raise GroovyError("source must be str")
        ns: Dict[str, Any] = {}
        try:
            exec(source, ns)
        except SyntaxError as e:
            raise GroovyError(f"syntax: {e}") from e
        out = {
            "names": sorted(k for k in ns.keys() if not k.startswith("_")),
            "length": len(source),
        }
        self._cache[source[:32]] = out
        return out
