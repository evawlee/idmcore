"""
Public-route prefix matcher. The gateway calls match_public(path) for every
incoming request to decide if the request can skip the auth gate. Returns True
when the request is on a published, unauthenticated route.
"""

from __future__ import annotations


_PUBLIC_PREFIXES = (
    "/iam/metadata",
    "/iam/login",
    "/iam/health",
    "/services/wsdl",
)


def match_public(request_path: str) -> bool:
    if not isinstance(request_path, str):
        return False
    for prefix in _PUBLIC_PREFIXES:
        if request_path.startswith(prefix):
            return True
    return False
