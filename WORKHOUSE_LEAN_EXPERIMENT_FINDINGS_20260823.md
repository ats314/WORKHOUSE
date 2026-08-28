# Self-designed experiment on the five carrier→continuum Lean files — findings

**Date:** 2026-08-23
**Scope:** the five uploaded files — `Incidence.lean`, `Spectrum.lean`, `Flatness.lean`,
`FiberGap.lean`, `CarrierAtomGap.lean` (+ the `AtomLemma.lean` core they depend on).
**Provenance / posture:** files are external uploads, not the repo clone. The experiment
was run entirely in the session scratchpad against the repo venv's `sympy` (1.14) + native
Python. **No repo file was written, no `git`/GitHub action was taken.** Read-only throughout.

---

## 0. What the experiment was

A **degeneracy-and-transcription adversarial audit**. The question was *not* "do the proofs
compile" (the Lean kernel already answers that) but the one the kernel cannot answer:

> Does each theorem's **statement** carry the weight its name and docstring imply, or is it
> true-but-hollow — vacuous, coefficient-inert, or internally consistent among
> mis-transcribed objects?

Five engines, an independent oracle (`sympy` exact + native-complex stress at scale), and —
deliberately — a test of whether *I* would cry "bug" on an artifact of my own check.

Everything below is reproducible from three scratch scripts (`exp_engineA.py`,
`exp_engineA_diag.py`, `exp_rest.py`, `exp_E.py`).

---

## 1. The honest headline

I set out to find hollow statements. The audit surfaced exactly **one** genuine hollowness
(the disputed `fiber_gap` coefficient is logically inert), confirmed the atom bound is not
just sound but **tight**, and otherwise re-confirmed the files. **The only outright "breaks"
the whole experiment produced were in my own two checks, not in the Lean.** Then an
independent adversarial pass corrected **two overclaims in my own write-up**. Net: run
against a real oracle, the files held; my prose needed the oracle more than they did.

---

## 2. Findings by engine (all quantified)

### Engine A — transcription / definition audit
Rebuilt `Bmat`, `psi`, `qa` from the physics (`dᵢ = e^{ikᵢ}−1`) *independently of the file*
and checked every incidence/spectrum statement **exactly** (symbolic):

| Check | Statement | Result |
|---|---|---|
| A1 | `Bᴴ ψ = 0` (`carrier_in_kernel`) | exact 0 |
| A2 | `BBᴴ = qa·I − ψψᴴ` (`incidence_gram`) | exact match |
| A3 | `‖ψ‖² = qa` (`carrier_normSq`) | exact match |
| A4 | `Sψ = −4ψ` (`Smat_carrier_eigen`) | exact match |
| A5 | `Sv = (−4+qa)v` on ψ^⊥ (`Smat_perp_eigen`) | exact, 3 vecs |
| A6 | `qa = Σ 4sin²(kᵢ/2)` (`qa_dispersion_sum`) | exact identity |
| A7 | `spec S = {−4, −4+qa, −4+qa}` | exact (char poly, §5 below) |

**Self-test caught here:** my first pass flagged A6 and A7 as FAIL. Both were bugs in *my
check* — `sympy.simplify` under-reduced A6 (both sides are `6 − 2Σcos kᵢ`), and I had set a
`1e-25` tolerance against a *floating* eigensolver in A7. Reproduced in isolation → both
dissolved. This is the CLAUDE.md decision tree ("bug in the check / transcription slip / real
discrepancy") landing on **bug in the check**, twice.

### Engine C — coefficient inertness of `fiber_gap`  ← sharpest finding
Replace the C2-disputed `2861009/8438730300` with a **free symbol `c`**:
`LHS − RHS ≡ 0`. The theorem holds for **any** `c`; it is `cos_gap` scaled by `c·u⁴`.
**Machine-checking `fiber_gap` gives zero bits of support to the correctness of that specific
number.** (Refined by verification — see §3, V1.)

### Engine D — does the atom bound have teeth?
Worked in the eigenbasis (`H=diag(λ)`, `ε=‖(H−m0)ψ‖`, window `|λ−m0|≤g/2`):

- **Soundness:** 20,000 random instances → **0** violations of `bound ≤ true window mass`.
- **Non-vacuity:** `1−(2ε/g)² > 0 ⟺ ε < g/2` (4366/20000 non-vacuous; min slack `5.8e-4 ≥ 0`).
- **Tightness:** explicit 2-level state, weight at `g/2+η` just outside the window →
  `truemass − bound → 0` as `η→0` (`1.2e-6` at `η=1e-6`). The Chebyshev bound is
  **best-possible of the form `f(ε/g)`** — no slack to reclaim. (Refined — see §3, V2.)
- **Collapse:** `g(b)=gapfun` at `u=0.1` shrinks `6.8e-8 → 6.5e-10` as `b: 2→32`; admissible
  `ε` shrinks like `u⁴/b²`. A clean atom needs `ε_mix = o(u⁴/b²)` — an **unproven** input.

### Engine B — is `B†ψ=0` load-bearing?
- Carrier eigenvalue is `E`, **k-independent** (exact); the other two eigenvalues are
  `E+t·qa` and **do** move with k (`5.02` vs `5.43` at two momenta).
- Generic perturbation breaks it: residual `‖(H−R)ψ‖ = 4.01 ≠ 0`. Hypothesis does real work.
  (Refined — see §3, V4.)

### Engine E — "try random shit, see if it breaks"
200,000 random `k`: worst `|Bᴴψ| = 0` exactly; worst `|Sψ−(−4)ψ| = 3.97e-15` (roundoff).
Nothing broke where the theorems make a claim.

---

## 3. Adversarial verification — where it corrected *me*

Five independent agents were each told to **refute** one headline claim. All that returned a
verdict returned **"upheld-with-refinement"** — the files held, but my *framing* was
sharpened or corrected in four places. These corrections are the most valuable output.

- **V1 (coefficient inertness) — upheld, two sharpenings.**
  (1) `fiber_gap` is *not* fully number-blind: its `hc` step machine-checks the **1:2 ratio**
  between the two printed coefficients (`2861009/4219365150 = 2·(2861009/8438730300)`), so it
  *would* catch a doubling-transcription slip. "Zero support" is exact for the **absolute
  magnitude's correctness**; the one checked fact touching the literals is the ratio.
  (2) The coefficient's **sign is never proved either** — positivity enters only as the
  hypothesis `0 < gapfun`. So even the sign gets 0 machine-check bits; it is load-bearing for
  *what the user must supply* to make the theorem non-vacuous, not something Lean verifies.
  *(This corrects my earlier "the sign is load-bearing downstream" — precisely: as a required
  hypothesis, not a verified fact.)*

- **V2 (atom bound) — upheld, tier conflation flagged.**
  Soundness and non-vacuity are **T0** (compiled, no `sorry`). **Tightness/best-possible is
  NOT formalized anywhere** in the Lean — it is my hand/numeric derivation, so **T2/T3, not
  T0**. Bundling them under one label hid that. Boundary is correct: the window is inclusive
  (`≤ g/2`), so the extremal weight sits *strictly* outside (`g/2+η`) and tightness is a
  **supremum approached as η→0, never attained**.

- **V3 (transcription/spectrum) — upheld, one overclaim caught.**
  The definitions are faithful and the spectrum is exactly `{−4, −4+qa, −4+qa}` — **true and
  machine-checked**, but *via* `Smat_carrier_eigen` + `Smat_perp_eigen` + `carrier_perp_finrank`
  (dim ψ^⊥ = 2), **not** via a characteristic polynomial. There is **no `charpoly`/`det`
  theorem in the Lean.** My `det(S−xI) = −(x+4)(x+4−qa)²` is an *independent T1 `sympy` check*,
  not a machine-checked route in the tree — I must not cite it as the Lean's verification.
  **Scope:** pinning needs `ψ ≠ 0`, i.e. `k ≠ Γ`; the Lean guards this (`d1≠0 ∨ d2≠0 ∨ d3≠0`).
  At Γ all `dᵢ=0`, `ψ=0`, and the multiplicity-2 refinement degenerates (spectrum → `{−4,−4,−4}`).

- **V4 (flatness load-bearing) — upheld, sharper witness.**
  `hker : Bᴴψ=0` is the literal rewrite that annihilates the perturbation term — used, not
  decorative; the theorem is false for general `ψ`, so it genuinely constrains. **Refinement:**
  the theorem's matrix is `Bk·Bkᴴ` (a PSD Gram), *not* a generic Hermitian; my
  generic-Hermitian residual (`4.01`) is a valid but *looser* witness. The precise thing that
  breaks without `hker` is the **eigenvalue value `E` (k-independence)** — a generic Hermitian
  could still have `ψ` as an eigenvector, but at `E+tμ ≠ E`.

- **V5 (novelty) — upheld, one overclaim caught.**
  (a) No genuinely new mathematics: `incidence_gram` is `fin_cases`+`ring`; `carrier_in_kernel`
  is `∂²=0`; `carrier_eigenvector` is one-line linear algebra; `qa_dispersion` and the
  spectrum/finrank lemmas are textbook. (c) None of the three inputs is secretly discharged:
  the `H_eff = E·I+t·BB†+O(u³)` **form** is the *supplied* operator (never derived), the C2
  coefficient is a hard-coded literal, and `ε_mix/g→0` enters `carrier_atom_clean_limit` as a
  **hypothesis, never bounded**. (b) "Davis–Kahan-free" is accurate (Parseval + second-moment
  + Chebyshev only). **Overclaim caught:** item (iii), "the explicit `o(u⁴/b²)` reduction,"
  overstates what is formalized. `carrier_atom_clean_limit` is a **decoupled limit-arithmetic
  lemma** over arbitrary sequences (`ε/g→0 ⟹ 1−(2ε/g)²→1`); it never references spectral mass,
  `gapfun`, or `carrier_atom_fiber_gap`, and `gap_asymptotic` is a standalone sinc limit.
  **Nowhere are they chained to conclude "window mass → 1."** What *is* formalized (T0) is the
  substitution `g = gapfun` into the bound (`carrier_atom_fiber_gap`); the "clean atom in the
  limit" is a wrapper, **not a formalized reduction**.

---

## 4. Consolidated tier table (what is actually established)

| Content | Tier | Note |
|---|---|---|
| `incidence_gram`, `Bᴴψ=0`, `Sψ=−4ψ`, `Sv=(−4+qa)v`, `dim ψ^⊥=2` (k≠Γ) | **T0** | Lean, no `sorry`, std axioms; independently reproduced exactly (Engine A) |
| `qa = Σ4sin²(kᵢ/2)` | **T0** | Lean; exact (Engine A6) |
| carrier eigenvalue `E` k-independent (`carrier_eigenvector`) | **T0** | Lean; `B†ψ=0` load-bearing (Engine B / V4) |
| atom bound soundness + non-vacuity (`window_weight_ge`) | **T0** | Lean; 0/20000 empirical violations (Engine D) |
| `carrier_atom_clean_limit` (`ε/g→0 ⟹ bound→1`) | **T0** | Lean; limit-arithmetic wrapper |
| `spec S = {−4,−4+qa,−4+qa}` via char poly | **T1** | *my* `sympy`; **not** in Lean (V3) |
| atom bound **tightness / best-possible** | **T2/T3** | hand+numeric only; **not** formalized (V2) |
| `fiber_gap` **coefficient value** `2861009/8438730300` | **inert** | 0 bits from the proof; only the 1:2 ratio is checked (Engine C / V1) |
| C2 coefficient correctness; O(u³) `H_eff` **form**; `ε_mix=o(u⁴/b²)` rate | **unproven** | the three inputs the physics conclusion actually needs |

---

## 5. Bottom line

The five files are **faithful, machine-checked (T0) formalizations** of a linear-algebra /
analysis skeleton that the corpus already asserted, plus one genuinely clean elementary
(Davis–Kahan-free) atom bound. The audit adds three things the compiler could not:

1. an **independent (non-Lean) exact reconstruction** confirming the definitions match the
   physics and the spectrum is exactly `{−4, −4+qa, −4+qa}`;
2. a **quantified quality read** on the atom bound — sound, and **tight** (best-possible of
   its form), with teeth only when `ε < g/2 ~ u⁴/b²`;
3. a **precise inertness result**: the C2-disputed coefficient carries **zero** machine-checked
   evidential weight in `fiber_gap` (only its 1:2 ratio is checked; its sign is assumed).

And it leaves the load-bearing physics exactly where it was: the O(u³) `H_eff` **form**, the
`ε_mix = o(u⁴/b²)` mixing rate, and the C2 coefficient are **all still unproven here**. So the
T0 status is real, the proof is clean — and none of it yet bears on the mass gap.

*All numbers reproduce from the scratchpad scripts; nothing in this document is authority — only the checks are.*
