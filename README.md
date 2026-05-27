# idmcore

idmcore is an identity governance core: front-door request filter, embedded validator, role
enforcement, diagnostic dump, and tenant cache for an internal IAM plane.

## Modules

- `idmcore.security_filter` — public-route gate at the front of the request flow
- `idmcore.script_runtime` — embedded validator for adapter snippets
- `idmcore.governance` — role enforcement on governance and admin paths
- `idmcore.diagnostics` — runtime state dump for the operations dashboard
- `idmcore.policy_cache` — per-tenant policy and session cache
- `idmcore.path_norm` — public-route prefix matcher
- `idmcore.audit_log` — in-memory audit trail
- `idmcore.tenant` — tenant metadata holder

## Layout

```
idmcore/                # package
tests/                  # baseline behavior tests
pyproject.toml          # build + test config
```

## Tests

```bash
pip install -e ".[dev]"
pytest tests/
```

