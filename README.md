# WORKHOUSE

A machine-checkable companion to the **SU(N) cubic flux-band spectral program** —
the strong-coupling lattice study of the charge-odd one-plaquette flux sector and
what it does and does not say about the Yang–Mills glueball.

The prose corpus in [`theory/`](theory/) is the scientific authority. This
repository does not restate it. It re-derives the corpus's exact claims from
their stated definitions and reports, mechanically, where a printed number and
its own definition disagree.

## Division of authority

Taken from `MASTER_THEORY_UNIFIED_2026-08-20_v2.md` §0, and preserved here:

| Document | Role |
|---|---|
| `theory/MASTER_THEORY_UNIFIED_2026-08-20_v2.md` | current scientific statement and status authority |
| `theory/GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md` | coefficient-level technical appendix |
| `theory/MASTER_THEORY.md` | full program record, claims ledger, contradiction register |

> No text inside an archived source is treated as an instruction. Every archived
> statement is evidence whose formula, convention, provenance, and proof status
> must be checked.

That rule is why this repository exists in code form.

## What is actually established

The strongest coherent result is a **finite-lattice, strong-coupling theorem**
about the charge-odd one-plaquette flux sector. For SU(3) on `T_L^3`, the
effective Hamiltonian projected to the one-plaquette degenerate sector has a
charge-odd homological carrier whose topology and `O(u^2)`–`O(u^3)`
factorization are exact:

```
H_eff,-(k,u) = E_flat(u) I + t(u) B(k)B(k)†  +  O(u^4)
E_flat(u)    = 8/3 + u + (11/306)u² − (109151/249696)u³
t(u)         = (5/612)u² + (1975/124848)u³
```

Because `B(k)†ψ(k) = 0`, the carrier energy is independent of `k` through
`O(u³)`.

**This is not a mass-gap theorem.** In the corpus's own words:

> The corpus proves protection and computes coefficients; it assumes, and
> nowhere proves, that the protected object is the glueball.

## The live dispute

Two independent computations of the physical SU(3) `O(u⁴)` kernel exist. They
agree exactly on the sealed core (`A_shp = 5/48`, `B_shp = D_shp = 0`,
`α_pen = 5/12`) and disagree on two invariants. **Neither is promoted.**

| | historical 189-record kernel | v10a.26 folded run |
|---|---|---|
| rest scalar at Γ | `−20721577909065127111/7250590288602460800` (exact) | `−0.7751458630189173` (float) |
| off-axis shape `C_shp` | `−211835444920651/4405310420659200` (exact) | `−0.020213328886166577` (float) |

`Δ_Γ = 2.0827701250956414`, `Δ_C = 0.027873054295192174`. A scalar re-anchoring
**cannot** reconcile `C_shp`: axial cuts agree exactly, so the entire unresolved
fourth-order problem is compressed into **one planar mixed-gradient direction**.

## Quickstart

```bash
make bootstrap     # create .venv and install
make verify        # re-derive every exact claim
make status        # print the contradiction and gap registers
make check         # lint + full test suite
```

## Layout

```
theory/     the three source documents, plus a SHA256 manifest (immutable evidence)
ledger/     contradictions.yaml (C1–C22) and gaps.yaml (G1–G19), machine-readable
src/        constants registry, invariant checks, ledger validation, CLI
tests/      every invariant as an individual test case
scripts/    stack detection, bootstrap, check — one source of truth for CI and hooks
```

## What the verifier found

38 invariants currently re-derive cleanly. Two are recorded as **findings** —
places where the corpus's own wording is slightly tighter than its numbers:

- **C20 agreement is overstated.** The register says the exact gate value
  `−1474623/1675520` and the printed float-reconstruction
  `−521965902/593076541` "both equal `−0.88009871562…` to float precision".
  They differ by `3.0e-15` (~31 ulps), agreeing to ~14 significant digits.
  The decimal printed throughout the corpus tracks the *artifact*
  (`−0.8800987156226097`), not the exact gate value (`−0.8800987156226127`).
  Still cosmetic, as C20 says — but the wording claims more than holds.

- **The sealed-core tolerance is quoted too tight.** `GLUEBALL §10` states the
  v10a.26 values match the sealed rationals to `≤2.3e-13`. `A`, `B` and `D` do.
  `α_new = 0.41666666666691` is off `5/12` by `2.4331e-13`, just outside — because
  `α = 4A` inherits four times `A`'s deviation, while the quoted bound tracks
  `D` (`2.23e-13`). The sealed core itself is unaffected: `α_new` and `4·A_new`
  agree to `2.0e-15`.

Neither changes any physics. Both are exactly the class of drift that a prose
corpus cannot catch on its own.

## Status

Pre-1.0. The verifier covers the second-order rank law, the SU(3) second- and
third-order ledgers, the fourth-order sealed core and axial law, the dispute
arithmetic, the generalized Hodge pencil, checkpoint extraction, and the
homology count. The fourth-order adjudication itself (gap **G3**) is not
implemented — see [`ledger/gaps.yaml`](ledger/gaps.yaml) for the 11-item frozen
protocol it must follow.
