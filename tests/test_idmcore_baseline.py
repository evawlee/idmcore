"""
Baseline behavior tests for the idmcore package.
"""

from __future__ import annotations

from idmcore.audit_log import AuditLog
from idmcore.policy_cache import PolicyCache
from idmcore.tenant import Tenant


def test_audit_log_records_and_counts():
    log = AuditLog()
    log.record("alice", "login_ok")
    log.record("bob", "policy_read")
    assert log.count() == 2
    dump = log.dump()
    assert "alice" in dump
    assert "policy_read" in dump


def test_tenant_counters():
    t = Tenant("tnt-1", "Acme")
    assert t.counter("logins") == 0
    assert t.bump("logins") == 1
    assert t.bump("logins") == 2
    assert t.counter("logins") == 2
    assert t.counter("other") == 0


def test_policy_cache_basic_put_and_get():
    cache = PolicyCache()
    cache.clear()
    cache.put_policy("policy_a", {"effect": "allow", "rule": "r1"})
    got = cache.get_policy("policy_a")
    assert got is not None
    assert got["effect"] == "allow"
    assert "policy_a" in cache.list_policy_keys()
    cache.clear()


def test_policy_cache_session_lookup_and_token_redaction():
    cache = PolicyCache()
    cache.clear()
    cache.open_session("sid-7", {"user": "carol", "session_token": "secret-tok"})
    blob = cache.lookup_session("sid-7")
    assert blob is not None
    assert blob["user"] == "carol"
    redacted = cache.list_sessions(include_tokens=False)
    found = [r for r in redacted if r["sid"] == "sid-7"]
    assert found
    assert "session_token" not in found[0]
    full = cache.list_sessions(include_tokens=True)
    found_full = [r for r in full if r["sid"] == "sid-7"]
    assert found_full
    assert found_full[0]["session_token"] == "secret-tok"
    cache.clear()
