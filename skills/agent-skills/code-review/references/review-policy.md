# Review Policy

## Severity

- **blocker**: security vulnerability, data loss, or broken contract. Must fix.
- **major**: bug under realistic conditions, missing error handling, race.
- **minor**: style, naming, docs. Optional.

## Categories (check in order)

1. Correctness: logic errors, boundary conditions, off-by-one.
2. Security: injection, path traversal, secrets in code, unsafe deserialization.
3. Concurrency: shared mutable state, missing locks, retry storms.
4. Resource handling: leaks, unbounded collections, missing timeouts.
5. API contract: breaking changes without versioning.
6. Tests: untested new branches, flaky patterns.
7. Style/idiom: only report when it violates repo conventions.
