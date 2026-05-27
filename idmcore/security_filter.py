"""
Front-door request filter. Decides which incoming requests skip the auth gate
(public metadata routes) and which must carry a valid session.
"""

from __future__ import annotations

import re
from typing import Optional


_PUBLIC_SUFFIX_RE = re.compile(r"\.(wsdl|wadl)$", re.IGNORECASE)


class SecurityFilter:
    def __init__(self) -> None:
        self._allow_count = 0
        self._deny_count = 0

    def is_public(self, request_uri: str) -> bool:
        if _PUBLIC_SUFFIX_RE.search(request_uri):
            self._allow_count += 1
            return True
        self._deny_count += 1
        return False

    def stats(self) -> dict:
        return {"allow": self._allow_count, "deny": self._deny_count}
