"""
Lightweight in-memory audit log. Other modules call it for trace plumbing.
"""

from __future__ import annotations

import io
import time
from typing import List


class AuditLog:
    def __init__(self) -> None:
        self._sink = io.StringIO()
        self._lines: List[str] = []

    def record(self, who: str, what: str) -> None:
        ts = int(time.time())
        line = f"{ts}|{who}|{what}\n"
        self._sink.write(line)
        self._lines.append(line)

    def dump(self) -> str:
        return self._sink.getvalue()

    def count(self) -> int:
        return len(self._lines)
