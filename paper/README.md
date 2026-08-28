# The master paper

`master_paper_2026-08-28.tex` — *Nested-quotient temporal histories and
homological flat bands in strong-coupling SU(N) Hamiltonian lattice gauge
theory* — is the distillation of this repository's verified layer into one
derivation. It supersedes the 8-page `Homological flat bands...` manuscript
(reviewed 2026-08-28; see `docs/referee/final_paper_review_2026-08-28.md`):
the isotropy hypothesis behind the channel weights is now a derived theorem,
the Bloch and chain carrier counts are joined by a sum rule, the
vacuum-mediated selection rule is stated at every rank, and the fourth-order
non-identifiability is a certified obstruction.

## The `check:` convention

Every displayed result in the paper carries a `check:` line naming the machine
check that establishes it. Each name is a real check in
`src/workhouse/invariants.py`, re-runnable alone:

```bash
workhouse verify --only 'the shared-link weights are Weingarten, not an isotropy assumption'
```

The citation runs both ways: `ledger/documents.yaml` legends the paper as
`MASTER paper`, so check `section` strings can cite it and
`tests/test_documents.py` keeps the reference resolvable.

## Building

```bash
make paper      # runs verify_core.py, then pdflatex twice
```

`verify_core.py` is a portable standard-library verifier for the paper's core
claims — no dependencies, under a second. Two of its checks are deliberately
stronger than float tests: the incidence identity is *decided* in exact
Gaussian-rational arithmetic at rational torus points, and the finite-torus
kernel comes with an explicit spanning cycle basis.

## What the paper does not claim

The scope section is part of the result. No continuum mass gap, no glueball
identification, no convergence of the series, no adjudication of the
fourth-order off-axis dispute (C2) — the paper proves that the retained
Γ/axis corpus *cannot* adjudicate it, which is why G3 (the target-blind
marked-cluster run) is the decisive next computation.
