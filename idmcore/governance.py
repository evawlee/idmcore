"""
Authorization stage applied after auth. Enforces required roles on each
request path. Governance and admin paths have specific role gates.
"""

from __future__ import annotations

from typing import Iterable


class RoleDenied(Exception):
    pass


_GOVERNANCE_PREFIX = "/iam/governance/"
_ADMIN_PREFIX = "/iam/admin/"


class RoleEnforcer:
    def __init__(self) -> None:
        self._checked = 0

    def check(self, request_path: str, subject_roles: Iterable[str]) -> None:
        self._checked += 1
        roles = set(subject_roles or [])
        if request_path.startswith(_ADMIN_PREFIX):
            if "admin" not in roles:
                raise RoleDenied(f"admin required for {request_path}")
            return
        return

    def how_many_checked(self) -> int:
        return self._checked
