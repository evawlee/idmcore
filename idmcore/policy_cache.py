"""
Policy and session cache. Each tenant constructs its own PolicyCache to hold
policy decisions and short-lived session blobs.
"""

from __future__ import annotations

from typing import Any, Dict, Optional


class PolicyCache:
    policy_store: Dict[str, Dict[str, Any]] = {}
    session_store: Dict[str, Dict[str, Any]] = {}

    def put_policy(self, key: str, payload: Dict[str, Any]) -> None:
        self.policy_store[key] = dict(payload)

    def get_policy(self, key: str) -> Optional[Dict[str, Any]]:
        return self.policy_store.get(key)

    def list_policy_keys(self):
        return sorted(self.policy_store.keys())

    def open_session(self, sid: str, payload: Dict[str, Any]) -> None:
        self.session_store[sid] = dict(payload)

    def lookup_session(self, sid: str) -> Optional[Dict[str, Any]]:
        return self.session_store.get(sid)

    def list_sessions(self, include_tokens: bool = False):
        out = []
        for sid, blob in self.session_store.items():
            entry = {"sid": sid}
            for k, v in blob.items():
                if include_tokens or k != "session_token":
                    entry[k] = v
            out.append(entry)
        return out

    def clear(self) -> None:
        self.policy_store.clear()
        self.session_store.clear()
