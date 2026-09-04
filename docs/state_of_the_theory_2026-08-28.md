# The SU(N) Cubic Flux-Band Program: What Stands

**2026-08-28.** Four years of research, 950 corpus files, five generations of
models — distilled to what is actually established, what is genuinely open,
and what would decide it. Every claim below is machine-checked (the tier says
how) or explicitly labeled asserted. Nothing here is confidence of phrasing.

---

## I. The bedrock

**Proved (T0).** 28 Lean 4 theorems compile from explicit definitions with no
`sorry` and standard axioms only: the incidence factorization ledger
(`S + 4I = BB†` as algebra), the third-order coefficient ledger, the axial
laws (`alphaPen_three: α₃ = 5/12`, cube/pentagonal/prism/tetra completions),
the blind holdout `λ_R = 2λ_M − λ_X`, the rank-law numerator, `dim Z₂`.
A further **27 theorems** — the carrier→continuum chain (PR #30) — **build
clean and depend on exactly `[propext, Classical.choice, Quot.sound]`**,
verified from scratch this session for the first time anywhere. They await
one repair before merge: the O(u⁴) literal they carry is the *pentagonal
cap-band* value (`DELTA_E_CAP_4`, a separate geometry the corpus explicitly
firewalls out of the cubic kernel), mislabeled "C2-disputed" when it is
neither C2 side. The proofs are coefficient-generic; the fix is a relabel,
not a teardown.

**Exactly re-derived (T1/T2).** 148 checks pass, from the stated corpus
definitions, in exact rationals or certified 128-bit enclosures. The spine:

- The C-odd series: `m₋(u) = 8/3 + u + (11/306)u² − (109151/249696)u³ + O(u⁴)`,
  with the drift-constant closure derived two independent ways.
- **U1 (supported):** protection, flat band, Betti count and spectrum all
  follow from the chain complex via `S(k) + 4I = B(k)B(k)†`, fixing
  `spec S = {−4, −4+q_a, −4+q_a}` and the carrier `ψ` with `‖ψ‖² = q_a`
  before any Hamiltonian.
- **U2 (supported):** every fourth-order shape coefficient is a symmetric
  function of Bloch scalars: `ε₄ = c₀ + A·q_a + B·e₂ + C·(4e₂/q_a) + D·(e₃/q_a)`.
- The sealed axial data: `A = 5/48`, `α = 4A = 5/12` — certified by **both**
  rival fourth-order kernels. The dispute never touches the axis.

## II. The one open question, and its new geography

**C2 — the off-axis coefficient C_shp** is the program's single genuinely
open contradiction: historical `−211835444920651/4405310420659200 ≈ −0.048086`
versus v10a.26 `−0.020213328886166577`, gap `0.027873…`. Both sides stay
recorded; neither is promoted. What this week's work added is *checked
geography* — where the dispute lives:

- The 189-record historical kernel now decomposes **exactly, over the whole
  Brillouin zone**, into physical transfer channels (this was previously
  known only at four parity points). Totals: `c₀ = q_band⁽⁴⁾`, `A = 5/48`,
  `B = D = 0`, `C = C_shp^historical` — and the numerator's constant and
  `q³` coefficients are exactly zero, so disconnected products cannot move
  the shape.
- **`C_normal = −A_normal/2` exactly.** The channel pinned by the axial
  coefficient both kernels share carries −0.052101 of C; *everything in
  dispute is the non-normal remainder* (+0.004015 historical vs +0.031888
  v10a.26 — a factor 7.94). Zeroing the entire 120-record rotation sector
  recovers only 14.6% of the required shift: the disagreement is a different
  in-plane amplitude, not a re-weighting.
- **Γ-point data cannot decide it** — `Φ_C = 4e₂/q_a` vanishes at Γ and on
  every axial cut. This is structural (machine-checked), which is why the
  externally-validated Γ-point scalar helps nothing.
- **G3's 609-cluster sweep cannot decide it either** (PR #29, pending
  merge): the Stage-3H contraction is *unwritten, not unrun* — the sweep
  yields a scalar-only certificate. Compute spent there does not reach C_shp.

**What would decide it**, ranked by cost:

1. **Extend `workhouse.cellular` to the in-plane and rotation channels.**
   The axial channel is already independently re-derived at symbolic N and
   T1-checked; the rotation-channel geometry (14 histories, S = −11) is
   cheap; the two channels carry the dispute, and three channels fix C to
   within 2.7×10⁻⁵ — 0.10% of the disputed gap. Engine-free, target-blind
   by construction.
2. **Near-Γ level ratios** (proposed, unexecuted): `ρ₂ = 2 + (96/5)C_shp`
   with built-in holdout `ρ₃ = 2ρ₂ − 1`. The two sides predict 1.077 vs
   1.612 — far apart. Any such run goes through the sealed-protocol
   discipline, never around it.
3. **The acceptance gate** for any future exact C_shp: support ⊆ S4 and
   `den | QBOUND` — a necessary condition that provably cannot prefer a
   side, ready to be registered as a harness stage.

## III. The tier collapse has become two integers

**G14** asked why `B_shp = D_shp = 0` when the two-hop enumeration generates
both. Now checked, at record level, over the whole zone: every degree-3
channel amplitude is an integer multiple of one raw record weight
`x = 360421351/40327601932800`, and the collapse is

```
B = 0 :  (+1, +1, −2) · x   over  {IN-PLANE(0,0,2), MIXED(0,1,1), ROTATION}
D = 0 :  (−3, +6, −3) · x   over  {IN-PLANE(0,0,2), IN-PLANE(0,1,1), MIXED(0,1,1)}
```

The kernel *does* populate the forbidden tier; the dynamics cancels it with
small integers, and the B-cancellation couples translations to the
120-record rotation sector — whose six displacement shells are individually
*outside* the shape span and cancel only as a sum. A mechanism (U3's
Feshbach-Q candidate) no longer explains a vague vanishing; it must
reproduce two specific integer vectors.

## IV. The balanced continuation is real arithmetic

The all-rank shape formula `β_N = P17(N²)/(N·R20(N²))` and the pinned
80-line structured walled-Brauer expression are **the same rational
function** — verified as an identity, not a sample. Evaluated at the
forbidden rank: `β₃^bal − β₃^hist = 25/64` **exactly** (the recorded C10
shift), with two corollaries recorded nowhere before this week:

```
Δβ₃ = −(15/16)·α₃          ΔC₃/(A/2) = −15/32
```

And the prohibition against continuation is now understood as a
*scalar-family* fact: the scalar denominator `D34` carries factors
`(z−4)(z−9)³(z−16)` — singular at exactly the ranks with ε-sectors, failing
loudly, never wrongly — while `R20`'s largest real root is `25/9` (N = 5/3):
the shape continuation is regular at every integer rank. Below its stated
scope the scalar formula reproduces the recorded `q₅` and `q₆^bal` exactly.

## V. The carrier → particle program, honestly

The fixed-spacing chain (electric shell → Yarotsky localization → CMP(1–4))
claims an isolated infinite-volume lattice quasiparticle band at small
coupling — explicitly *not* a continuum particle. Its own stopping point is
stated with unusual honesty: small `u` is strong coupling, the continuum is
the opposite end of the axis, and the missing uniform source-carrying
invariant-mass-island theorem "is essentially the particle-resolved
constructive 4D Yang–Mills problem."

**Evidence status (finding, recorded):** the chain's own manifest pins eight
documents; four are delivered and byte-match; four — the foundations F1–F3 —
are **cited, never delivered** (the maintainer confirms the delivery is
complete). Every "Proved" resting on them is claim-only. The delivered half
(CMP(2–4), the stopping point, and three audits that *refute* parts of the
chain's own earlier drafts) is imported and citable. The strongest survivors
are the refutations: the printed finite-time residue bound is false as
written (counterexample `μ = δ_M + 9δ_{M+Δ}`); PMBSF-type upper bounds can
never yield the needed lower residue bound; the one-ratio reduction dies on
two explicit counterexamples.

What remains live and sharp: the whole continuum carrier-atom question
reduces to **one bound** — `ε_mix(b) = o(u⁴/b²)` on block-induced alias
mixing — with the finite-dimensional atom lemma already formalized (the
verified Lean layer above), and the corrected cubic gap constant
`(5/12)π² ≈ 4.11·u⁴/b²` making the clean-atom budget ~615× less demanding
than the transplanted figure suggested.

## VI. Instruments and data in hand

- **G3:** the marked-cluster engine is located in-repo, behaviorally
  verified (freeze passes; self-test 47/47), and its first run fail-closed
  exactly as physics demands: the inherited cap (100) sits below the first
  cluster's measured demand (216). The cap-216 revision is specified and
  hash-pinned; a readiness notebook additionally defines the output
  contract a production engine must satisfy. The fix belongs upstream, as a
  deliberate hash change.
- **G18:** the NB_FLUX instrument is repaired (the original reunitarization
  was gauge non-covariant, defect 0.43 → 1.7×10⁻⁷ after the polar/SVD fix,
  16/16 gates, AT-2020 regression reproduced) and **1024 spin-resolved
  configurations at β = 6.0625 sit delivered and unanalyzed**. The shared
  correlated analysis is the single largest piece of unprocessed data in
  the program.
- **The certificate stack** (QBOUND, exact-Haar, modular-CRT) delivered its
  most important result by *failing correctly*: an external package landed
  byte-exactly on the C1 quarantined scalar while passing every
  denominator, divisibility, and Lean gate — because it skipped the
  anchoring step that is the open dispute. **Certificates are provenance,
  not physics: necessary, never sufficient.** That episode is now the
  program's canonical epistemic lesson, recorded as such.

## VII. The path, ranked

1. **Cellular channel extension** — the engine-free C2 decision (weeks).
2. **NB_FLUX correlated analysis** — G18's data exists; analyze it.
3. **PR #30 repair + merge** — 55 T0 theorems with the coefficient
   corrected; the spectral-bridge algebra becomes bedrock.
4. **G3 upstream revision** — cap + output contract, then the scalar
   certificate (C3/C22 close; C2 does not).
5. **G17/G18** remain the open infinite-volume problems. Nothing this week
   changed that; several things sharpened what they must contain.

---

*Provenance: 148/148 checks (`make verify`), 28 T0 theorems (`make lean`),
suite "off-axis channel ledger (C2 geography, G14)" for §II–§IV, the notes
register (`workhouse notes`) for every archive verdict, and
`docs/referee/wsls_triage_2026-08-28.md` for the week's evidence trail.
Each claim above re-checks in about a second:
`workhouse verify --only '<check name>'`.*
