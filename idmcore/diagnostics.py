"""
Diagnostic state dump. Used by operations dashboards to summarize current
runtime. Ops normally wants device counts and policy keys; secrets only on
explicit opt-in.
"""

from __future__ import annotations

from typing import Any, Dict


class DiagState:
    def __init__(self, store, role_enforcer) -> None:
        self._store = store
        self._role_enforcer = role_enforcer

    def dump(self, include_session_tokens: bool = True) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        out["policy_keys"] = self._store.list_policy_keys()
        out["sessions"] = self._store.list_sessions(include_tokens=include_session_tokens)
        out["roles_checked"] = self._role_enforcer.how_many_checked()
        return out
