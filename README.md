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

## Anchoring vs. the real dispute

Two independent computations of the SU(3) `O(u⁴)` kernel exist. They agree
exactly on the sealed core (`A_shp = 5/48`, `B_shp = D_shp = 0`,
`α_pen = 5/12`). Where they appear to differ splits into two very different
situations.

**The scalar is not a dispute.** `q_band⁽⁴⁾` and `m_Γ⁽⁴⁾` are *not* two
competing estimates of one coordinate:

| | | |
|---|---|---|
| `q_band⁽⁴⁾` | `−20721577909065127111/7250590288602460800` | band-kernel anchor (exact) |
| `m_Γ⁽⁴⁾` | `−0.7751458630189173` | vacuum-subtracted physical Γ-point coefficient |

They are differently anchored coordinates related by a translation-local scalar
shift `Δ_Γ = 2.0827701250956417`. Since
`H_mass − m_Γ⁽⁴⁾·I ≡ H_band − q_band⁽⁴⁾·I`, that shift cannot change the
centered operator, its eigenvectors, the SOS factorization, the mobility
coefficients, or the bandwidth. **Never call these "two `m_4` values"** — that
phrasing is what manufactured the contradiction, and a test enforces the
register keeps saying so.

`m_Γ⁽⁴⁾` reproduces Hamer's axial coefficient through `mₙ = 2ⁿ⁻¹·aₙ`
(`8·a₄ = −0.7751458630184`, agreeing to `5.2e-13`) from a run with the
historical target disabled — substantive external validation. Note the separate
caveat: the final assembled rest value is *forced* to equal that oracle by
`local_shift = M4_ORACLE − ax_rest`, which is true by construction and
validates neither the off-axis C-row nor the 189-entry ledger.

**The off-axis coefficient is the real dispute**, and structurally so:

```
c₄_new(k) = c₄_old(k) + Δ_Γ + Δ_C·Φ_C(k),    Φ_C(k) = 4e₂(k)/Q(k)
```

With `e₂ = O(|k|⁴)` and `Q = O(|k|²)`, `Φ_C = O(|k|²)` and `Φ_C(0) = 0`. So a
Γ-point scalar pins `Δ_Γ` and constrains `Δ_C` **not at all** — which is exactly
why the scalar match can be right while the off-axis kernel stays unresolved.
`Φ_C` vanishes on every axial cut too, so axial data agree exactly while
`Φ_C(M) = 8` and `Φ_C(R) = 16` split those points by `8Δ_C` and `16Δ_C`, with
`C_old = −0.04808638318135875` against `C_new = −0.020213328886166577` and
`Δ_C = 0.027873054295192174`.

Scalar re-anchoring alone leaves the centered structure unchanged; only the
`Δ_C·Φ_C` term can move the dispersion. The crosswalk preserves bandwidth only
if `Δ_C` vanishes or is absorbed by an exact operator identity, and neither is
established.

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
settlement/ received artifacts: two cold-rerun transcripts and the adjudication harness
ledger/     contradictions.yaml (C1–C22) and gaps.yaml (G1–G19), machine-readable
src/        constants registry, invariant checks, ledger validation, CLI
tests/      every invariant as an individual test case
scripts/    stack detection, bootstrap, check — one source of truth for CI and hooks
```

## What the verifier found

52 invariants currently re-derive cleanly. Six are recorded as **findings**.
Three are places where the corpus's own wording is slightly tighter than its
numbers:

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

- **`Δ_Γ` is printed one ulp low.** The register gives `2.0827701250956414`.
  In high precision the difference is `2.082770125095641678…`, which correctly
  rounds to `…417`; the printed value comes from rounding `q_band⁽⁴⁾` to a
  double *before* subtracting. Cosmetic, but the printed digit is not the
  correctly rounded one.

None changes any physics. All three are exactly the class of drift that a prose
corpus cannot catch on its own.

Three more concern the adjudication harness in `settlement/`, which is the tool
that would actually decide C2:

- **The target-blindness scan cannot see two scalar-determining targets.**
  `m_Γ = q_band + Δ_Γ` exactly, and Hamer's `8·a₄` *is* the scalar to 13
  digits — so an engine carrying either constant is seeded with the answer it
  is supposed to reconstruct blind. The scan covers the 16-digit oracle form
  `7751458630189173`, but that string does **not** contain `7751458630184`;
  they diverge at index 12. Both would pass `[PASS] target-contamination scan`.
- **The scan reads only the engine file.** An engine that imports a helper
  module, loads a data file, or restores from the sqlite checkpoint carries
  that content past it untouched.
- **The verdict can never be `COMPLETE`.** Protocol item 10 (the W22 toggle) is
  hardcoded `OPEN` and the completeness predicate rejects any `OPEN` value, so
  even a certificate discharging items 8 and 9 with a full shape block yields
  `PARTIAL`.

The quarantine *architecture* is sound — targets stay module-local and the
engine is launched with a clean environment. The gap is in detecting a target
already inside the engine, which is exactly the case the scan exists to rule
out.

## Status

Pre-1.0. The verifier covers the second-order rank law, the SU(3) second- and
third-order ledgers, the fourth-order sealed core and axial law, the dispute
arithmetic, the generalized Hodge pencil, checkpoint extraction, and the
homology count. The fourth-order adjudication itself (gap **G3**) is not
implemented — see [`ledger/gaps.yaml`](ledger/gaps.yaml) for the 11-item frozen
protocol it must follow. Its scope narrowed once C1 was dissolved: what G3 must
settle is `C_shp`, since `Φ_C(0) = 0` makes Γ-point data structurally incapable
of constraining `Δ_C`.
