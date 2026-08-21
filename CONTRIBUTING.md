# Contributing

## Setup

```bash
make bootstrap
make check
```

## The one rule

Do not make a failing check pass by weakening it. In this repository a failing
check is usually information, not a defect. See `CLAUDE.md` for the full
working agreement — it applies to humans equally.

## Pull requests

- Every new invariant cites the corpus section it re-derives.
- Every change to a number in `src/workhouse/constants.py` cites its source
  document and section, and states its status and evidence level.
- Changes to `theory/` require regenerating `theory/SHA256SUMS` (`make manifest`)
  and saying in the PR body why the evidence changed.
- Dependency changes go through `make lock` so `uv.lock` stays in step with
  `pyproject.toml`. The lockfile is what makes a result reproducible rather than
  merely recorded — the same distinction the corpus draws between
  *cold-reproduced* and *record-backed* evidence.
- `make check` passes locally before you push.

## Commit style

Short imperative subject, body explaining *why*. Reference contradiction and
gap ids (`C1`, `G3`) where relevant — they are the shared vocabulary here.
