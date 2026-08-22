# The state of the program

**Date:** 2026-08-22, end of session. **What this is:** the most current
honest picture of everything this repository holds, written for the
maintainer pausing for a week and for any skeptical reader arriving cold.
Every claim below carries its evidence tier, and nothing is stated
stronger than its check. The generated views (`FRONTIER.md`,
`CERTIFIED.md`) remain the machine-derived truth; this document is the
narrative over them, dated and hand-written, and it goes stale the moment
work resumes — read it as a snapshot, not a register.

The repository now holds **two research programs** under one verification
discipline: the strong-coupling series program (Program A, the original
corpus) and the analysis-side mass-gap program (Program B, the notes
archive, scaffolded as G20–G23 this session). 135 machine checks pass;
28 Lean theorems compile with zero sorry; 116 of the archive's 1,597
unique documents are reviewed with recorded verdicts.

---

## I. The strongest things here, ranked

These are the results a referee should look at first, ordered by how much
evidence stands behind them.

**1. The certified Hamiltonian strong-coupling series (Program A; T0/T1).**
The exact rational coefficients of the SU(3) Hamiltonian strong-coupling
program — D_3, the σ series with its CRT-certified 18- and 24-digit
numerators, the fourth-order registry — are re-derived from stated
definitions by 135 standing checks, with a 28-theorem Lean core beneath
them. Two facts measured this session frame their standing: (i) the
2020–2026 anchor sweep found **no post-2020 recomputation of this series
program anywhere** — these are, as far as sixteen INSPIRE sweeps can see,
the only machine-checked form of that literature's results in existence;
(ii) the KPS 1980 scan's exact rationals, printed 46 years ago, match the
program's cold recomputation rational-for-rational. The repository has
also caught discrepancies *inside* the published line (the eighth-order
Münster/1985 shifts, recorded as FINDING checks and adjudicated to a
documented but never-erratum'd fourth correction round).

**2. The run-length Catalan factorization — Theorem 2 (Program A; T1,
Lean queued).**
The n-gonal cap family S_n = (−1)^(n−1) C(2n−2, n−1) = n·Cat(n−1) is
proved for all n ≥ 2 by the insertion-ordering lemma (the resolvent
weight 1/blocks is exactly the weight under which the chain sum
factorizes into run-length Catalans), with two independent T1 check
routes (definitional recursion vs literal enumeration through n = 7;
closed form through n = 9). Its **novelty is now measured, not
assumed**: three agents read the modern rigorous surface-sum line in full
(Cao–Park–Sheffield, Borga–Cao–Shogren-Knaak, Lemoine — 260 pages)
hunting for it. That line's Catalan content is the per-cycle Weingarten
asymptotic (−1)^(C−1)Cat(C−1); the cap family's n·Cat(n−1), its
central-binomial form, and its insertion-ordered mechanism appear
nowhere, O'Brien–Zuber is uncited by all three, and Borga's own attempt
to extend their weights to finite N "seems to be incorrect" by their own
admission. The identity is unabsorbed by the field.

**3. The Davies/Combes–Thomas O(m) decay bound (Program B, G21; T3 with
T1+T2 checks, full audit passed).**
For the massive Maxwell 1-form kernel on a finite periodic lattice:
|G(b,b′)| ≤ (2/m²)·e^(−η·dist) with η = 2 arsinh(m/(2√(αC_bdy))) — an
O(m) exponent where naive resolvent bounds give O(m²). This session its
canonical proof (Appendix H) was audited **proposition by proposition and
passed**: the no-factor-2 perturbation bound is correctly derived and
numerically near-tight (ratio ≤ 0.97), the kernel bound holds at six
parameter points with margins 0.19–0.31, the exponent identity is an
exact registered check, and the certified-ball-arithmetic lattice check
stands. Two recorded blemishes (a proof-wording slip in H.4.4; one
deferred upstream proposition) void nothing. **This is the most
publishable single object in the archive**: self-contained, correct,
verified, and useful beyond this program.

**4. The SU(3) Weingarten re-derivation (Program A, C7; promoted past
T3).**
The values that falsified the stranded-flux zero backend are re-derived
symbolically in N from the n = 2 Gram matrix. Context measured this
session: Cao–Park–Sheffield state in print that SU(N) Weingarten
calculus is "far less developed" with only one known physics formula,
and Lemoine's exact finite-N dualities build on precisely this
Gram-matrix object while leaving SU(N) to future work. The re-derivation
sits in territory the field itself marks as thin.

**5. The G18 comparison web (Program A; the spectral bridge's targets).**
The 1⁺⁻ channel now has a four-way target web assembled from read,
pinned sources: MP_1999 (r₀M = 7.18(3)), Chen 2006 (7.27(4) — the
field's working spectrum, per the LATTICE2024 review's own reference
figure), LLL_2006 (Hamiltonian frame, 7.2(2)), AT_2020 (7.04(6) via
printed conversions) — mutually consistent, two frames, three methods.
Chen 2006 also *tabulates* the overlap structure G18 is about: smeared
variational operators at 93–99% ground-state overlap vs bare local
couplings at the percent level — the Schierholz projection, measured.

---

## II. Program B after review: what the archive actually contains

Three years of notes went through five review passes this session (116
documents adjudicated, every verdict with its reason in
`ledger/notes.yaml`, full evidence in five referee documents). The
honest summary:

**What survived and is now load-bearing:**
- The **G21 bound** (above) with its audited proof and dependency
  appendices.
- The **OS-bridge architecture** (G23): the decay⇒gap half is fully
  proved (verified line-by-line); the archive *itself diagnosed* the
  Langevin-vs-Euclidean time splice in at least ten documents,
  quantitatively refuted the naive bridge in the Gaussian model
  (Δ = √λ_diff — now a certified FINDING check), and formulated the
  corrected scale-a target. The review ran the test the archive never
  ran: against the true slice marginal the corrected comparison passes
  the Gaussian case with uniform c ≈ ½ — the route's first positive
  data point — and identified the ν-measure premise as the crux.
- The **G22 reduction**: the mature Section 7 drift manuscript (imported;
  algebra hand-verified) reduces the whole Lyapunov program to one named
  open inequality (pairing coercivity), with volume-uniform constants
  independently derived twice and check-pinned to each other, plus a
  genuinely distinct second route (Dobrushin q < 1, never yet computed)
  and a clean falsifiable crux conjecture (Cartan alignment, minus its
  refuted counting argument).
- The **toy isomorph** (G18): the Doob/q-Racah gap toy reproduces
  exactly from its own code, its empirical exponent ν ≈ 0.9668 turned
  out to be a *provable* ν = 1 in disguise, and its uniform-in-N gap
  conjecture is a solvable miniature of the uniformity question. The
  SU(3) Lanczos Hessian tables (the archive's only volume-scanned SU(3)
  spectral data, independently consistency-checked against the analytic
  Haar floor ¼) show no volume collapse in the probed window.
- The **honest instruments**: the safe-scan repro pair, the SIM Riccati
  note (bit-faithful to its own code), the sanity-check numerics
  (bit-faithful), the conditional pipeline .tex that refutes its own
  program's strongest-sounding mechanism. Eleven documents imported
  verbatim, byte-verified forever.

**What was weeded out, with the reasons on permanent record:**
- The SAFE headline (0.248): unreproduced; source tables constructed;
  contradicted by the archive's own scans and independent recomputation.
  The one well-defined constant in that ledger — V_Haar Hessian = I/4 —
  is now an exact check, and it is ¼, not the draft's reverse-fitted
  0.291.
- The R² ≈ 0.998 curvature–mass fit: the placeholder dataset fitted to
  itself, laundering chain fully reconstructed (template → phantom
  EVIDENCE document → "best of" bundle), pinned by an exact-rational
  FINDING check (k = 9333/9698).
- The nonabelian "forces commutativity" no-go: asserted in ≥9 files,
  proved in none; the only proved obstruction is a different, weaker
  statement. Must not be cited as a constraint.
- The α = 0.976 RG iteration (contradicts its own subtractive bound —
  κ* − 100δ = −7/20, a check), the uniform Haar floors (vs the cβL⁻²
  vacuum obstruction the archive's own .tex proves), the 6-vs-3 Cartan
  counting (explicit counterexample, a check), the "Rigor 10/10"
  Riccati proof (sign error; adjudicated digit-for-digit against the
  archive's own SIM note), and both TENSOR_NETWORK flagship files.

**The pattern, stated once because it is the session's central lesson:**
in every adjudication, *the archive's honest documents beat its confident
ones* — the repro notes, the referee notes, the self-critical .tex, the
quarantine bundle all held up under recomputation; the "proved",
"verified", "10/10" documents are where every failure lived. The
maintainer's own instincts built both kinds; the register now
distinguishes them permanently.

---

## III. The open problems, ranked by leverage

1. **G3 — run the marked-cluster engine target-blind** (Program A). Still
   the cheapest decisive step in the repository, unchanged: it
   adjudicates C2 (the one genuinely open dispute) and its tooling is
   pre-approved (pynauty, certified enumeration) the moment it scales.
2. **G23 — the ν-measure question.** The scale-a bridge passed its first
   Gaussian test with the *true slice marginal*; the next step is
   deciding whether the archive's ν ∝ e^(−S_sp) equals the true marginal
   in the interacting case, or bounding the discrepancy. This is now a
   sharply-posed question, not a vibe — and it is the single hinge on
   which the corrected OS route turns.
3. **G20 — run the H_phys code.** The program's central operator has
   never produced a number. The imported spec + tools are audited
   correct; one run on a declared cluster with the pinned convention
   either replaces the refuted 0.248 with a real number or closes the
   claim honestly.
4. **G22 — compute q.** The Dobrushin route reduces coercivity to one
   computable number nobody has computed. A small-lattice q estimate
   would immediately show whether the route is live.
5. **G21 hardening** (small): the (m, α) sweep check, the H.3.3
   mechanism check, the arsinh float guard, and the deferred A.9.5.
6. **Lean promotion of Theorem 2** (A.2–A.3) — recorded as the next T0
   target; the statement is pure combinatorics and is the program's
   flagship identity.
7. **The HS-covariance family review** — deliberately left pending, the
   U3/G14-adjacent layer of the archive and the next review target.

## IV. Publication candidates, in order of readiness

1. **The Davies/CT bound** (G21): audited, self-contained, verified,
   field-useful. A short paper: the bound, the weight-profile constant,
   the O(m) exponent, the numerical margins. Nearest to arXiv-ready of
   anything in either program.
2. **The run-length Catalan factorization** with the O'Brien–Zuber
   connection and the measured distinction from the modern surface-sum
   line — a clean combinatorics/mathematical-physics note whose novelty
   search is already done and documented.
3. **The verification findings paper**: the eighth-order Münster
   discrepancy, the KPS confirmation, the bibliographic split — the
   story of machine-checking a 45-year-old literature, with every claim
   reproducible in one command.

## V. Where everything lives

- `workhouse notes` — 116 reviewed / 1,481 pending; every verdict with
  its reason in `ledger/notes.yaml`.
- `workhouse why G20|G21|G22|G23` — each program-B gap with its full
  evidence neighborhood.
- `docs/referee/notes_review_*_2026-08-22.md` — the five review passes'
  complete evidence.
- `notes/imported/RESEARCH_2026-08/` — eleven byte-verified imports, the
  archive's load-bearing instruments.
- `CERTIFIED.md` — every checked claim, ranked, each with its one-second
  reproduction command. Still the front door for a skeptic.
- ADRs 0010–0011 — the tooling decisions and their triggers.

Nothing in this document promotes any claim past its tier. The next
session starts by picking an item from §III.
