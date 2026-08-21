# SU(N) fourth-order band-shape theorem — campaign intake (2026-06-14)

**What this is.** The fourth-order projected lifting of the one-flux \(T_1^{+-}\) glueball
band, solved in closed form for **every non-pseudoreal integer SU(N), N ≥ 3**. This is the
general-N extension of the one-plaquette flat-band spectroscopy (the SU(3) case lives in the
flat-band paper); v0.8 of that paper now embeds this theorem. Deposited here from the
2026-06-14 ZIP-ARCHIVES drop after independent cold verification.

## The result

With \(X_i = 1-\cos k_i\), the symmetry + displacement gates force the projected
fourth-order shape to

\[
D_N(k) = A_N \sum_i X_i^2 + B_N \sum_{i<j} X_i X_j .
\]

Closed forms (canonical):

- \(A_N = \dfrac{640}{N(N^2-1)^3}\) for every integer \(N\ge 4\); \(A_3 = 5/12\).
- \(B_N = P_{402}(N)/D_{409}(N)\) (canonical) \(= P_{17}(N^2)/(N\,R_{20}(N^2))\) (reduced, paper v0.8).
- \(q_N = -\dfrac{2}{3N}\,Q_{32}(N^2)/D_{34}(N^2)\) (the common offset).

Large-N (paper v0.8 / `ENGINE_Y4_sun_largen_asymptotic_verify.py`):
\(q_N=-227/N^5+O(N^{-7})\), \(A_N=640/N^7+O(N^{-9})\),
\(B_N=\tfrac{6170}{9}N^{-7}+O(N^{-9})\), \(\Delta c_{4,N}=\tfrac{11930}{9}N^{-7}+O(N^{-9})\).

**Theorem.** For every integer \(N\ge 3\): \(A_N>0\) and \(B_N>0\). Therefore **Γ is the unique
global minimum, R the unique global maximum, and the bandwidth \(\Delta c_{4,N}=A_N+B_N>0\).**
Positivity for \(N\ge 7\) is by the 403 strictly positive Newton coefficients of \(P_{402}\)
about \(N=7\) plus denominator positivity; \(N=4,5,6\) are checked exactly (with determinant-sector
handling). SU(2) remains a separate case; the offsets \(q_4,q_6\) still need their determinant-sector
corrections (these do **not** affect the extrema or the bandwidth theorem).

Exceptional-rank determinant analysis: **SU(4):** ΔA₄ = ΔB₄ = 0 (40 exceptional words; +8/−8 coefficients
cancel by equal multiplicity in every B-class); **SU(5):** no determinant sector occurs; **SU(6):** the
sole determinant orbit is absent from the A/B target.

## Verification done this session (grounds: T1 machine-gated + independent cross-check)

Cold-run in a clean sandbox (Python 3.10, sympy 1.14.0), no precomputed cache:

| script | result |
|---|---|
| `ENGINE_Y4_sun_all_n_ge3_band_shape_verify.py` | **ALL GATES PASS** (SU4 census +312/+156; ΔA₄=ΔB₄=0; SU5 none; SU6 absent-from-target; A_N,B_N>0 at N=3..6 and symbolic N≥7) |
| `ENGINE_Y4_sun_symbolic_qab_verify.py` | **ALL GATES PASS** (q_N degrees (32,34); A_N=640/[N(N²−1)³]; B_N denom degree 409 + 403 positive Newton coeffs; N=7..18 stored matches; q_N<0,A_N>0,B_N>0 ∀N≥7) |
| `ENGINE_Y4_sun_largen_asymptotic_verify.py` | **ALL GATES PASS** (the four asymptotic series above) |

**Independent cross-check (my own, not the bundle's scripts).** I loaded the raw per-N kernels from
the *separate* `Y4_SUN_FULL_SYMBOLIC_INDEPENDENT_RERUN` bundle (`independent_rerun_kernels/`) and verified,
in exact rational arithmetic, for **N = 7…18**: \(A_N = 640/(N(N^2-1)^3)\) exactly, \(B_N>0\), and
\(A_N+B_N>0\). All 12 pass. (E.g. \(A_7 = 5/6048 = 640/(7\cdot 48^3)\).) This is a reimplementation of the
positivity/closed-form check independent of both the bundle verifier and the certificate.

**Scope honesty.** T1 (machine-gated, cold-reproduced) + an independent finite-N cross-check to N=18.
The all-N≥7 positivity is the scripts' Newton-coefficient argument (I confirmed it holds and exhausted
N≤18 directly). NOT yet T2 (line-by-line human review of the walled-Brauer construction) or T3 (external
referee). Status in STATE is recorded accordingly; not promoted to "established."

## Provenance (source bundles in `C:\ALL THEORY\ZIP ARCHIVES\`, MD5 of the .zip)

- `Y4_SUN_ALL_N_GE_3_BAND_SHAPE_BUNDLE_2026-06-14.zip` — md5 `44dd0908799455baf158f1b8303b2643` (certificate + all-N verifier + SU4/5/6 determinant analysis)
- `Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14_V2.zip` — md5 `cb9f01f12dd35f71c29ae248f1aff0a0` (symbolic q/A/B verifier + large-N + closed-form expressions; the canonical construction)
- `Y4_SUN_FULL_SYMBOLIC_INDEPENDENT_RERUN_2026-06-14.zip` — md5 `161450c47125b38ef19ba08f41cbcd23` (independent recomputation, N=7..18 kernels — the cross-check source)

Per-file MD5 of this directory: `MAN_SUN_md5sums.txt`. The bulk walled-Brauer construction scripts and
`*.json.gz` word/topology data are **not** copied here (they stay in the source bundles) — only the
theorem, certificates, closed-form expressions, the three verifier scripts, and the independent-rerun
kernels are distilled in.

## Completion layer (2026-06-14) — see `completion_2026-06-14/`
Later-same-day uploads that complete/consolidate this theorem (machine-checked this session):
- **SU(2) is now CLOSED, not a gap:** `SU2_CODD_SECTOR_EXCLUSION_THEOREM` proves C is a gauge transformation in
  SU(2) (U\*=εUε⁻¹ ⟹ C=I, P_{C=−}=0) ⟹ **no SU(2) T₁⁺⁻ branch exists**; the N≥3 domain is **maximal**. (Verified: U\*=εUε⁻¹ exact, TrX³=0.)
- **Unified N-ality theorem (audited V2):** consolidates the all-N statement with exact exceptional offsets —
  B₃=B₃^bal−25/64 (verified), Δq₄=−304746539168/160249753125, Δq₆=6/343, SU5 none; exact q₃..q₆.
- **Closed-surface Stage-1:** universal 2nd-order flatness for all N≥3 (t_N>0, t₃=5/612 verified); a cleaner
  structural route. 4th-order reduction is conditional; Stage-2 obligations open.

## Open / next
- **q₄, q₆ offsets are now GIVEN** (unified theorem above); the SU(2) "gap" is **closed** (excluded, N≥3 maximal).
- Closed-surface **Stage-2** (generic-N three-orbit support lemma + closed forms + all-N positivity) — open.
- A T2 line-by-line review of the walled-Brauer fixed-rank construction would raise the tier.
