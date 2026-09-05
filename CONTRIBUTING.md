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
- Record each new result's hypotheses, conclusion, status, evidence, and
  provenance in the ledger. Connect it to its established inputs and the
  consequences it enables in the theory graph; update affected gap routes.
  Finite checks and Lean statements must describe exactly what they verify.
- Update the relevant current documentation, including
  [Current research](docs/current_research.md) and the README when the next
  research target changes. Preserve sealed proofs, manuscripts, and runs;
  link their later resolutions from current navigation.
- Every change to a number in `src/workhouse/constants.py` cites its source
  document and section, and states its status and evidence level.
- Changes to `theory/` require regenerating `theory/SHA256SUMS` (`make manifest`)
  and saying in the PR body why the evidence changed.
- Dependency changes go through `make lock` so `uv.lock` stays in step with
  `pyproject.toml`. The lockfile is what makes a result reproducible rather than
  merely recorded — the same distinction the corpus draws between
  *cold-reproduced* and *record-backed* evidence.
- Regenerate `index/`, `FRONTIER.md`, and `CERTIFIED.md` with `make catalogue`,
  `make frontier`, and `make certified`. Inspect `workhouse why <id>` for
  each affected claim so the new dependency and route information is usable.
- `make verify` and `make check` pass locally before you push. Run `make lean`
  when Lean statements change, and complete the required CI checks.

## Landing verified work

Follow [CLAUDE.md](CLAUDE.md#complete-the-result-then-land-your-own-green-work): when the PR is green,
has no conflict, and has no unaddressed review comment, mark it ready and merge
it. Verified research is not integrated until the result, graph, and current
documentation reach `main`. Report the merged commit and verify the remote
branch; distinguish local work, pushed work, and merged work in status updates.

## Commit style

Short imperative subject, body explaining *why*. Reference contradiction and
gap ids (`C1`, `G3`) where relevant — they are the shared vocabulary here.
