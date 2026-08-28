# The manuscript of record

*Homological flat bands in strongly coupled SU(N) Hamiltonian lattice gauge
theory*, Alexander Smith, 28 August 2026 — the first piece of this program
written for outside readers, and the first artifact that cites this repository
by commit.

It is pinned here for the same reason `runs/` is pinned: the checks below refer
to *these bytes*. `SHA256SUMS` records them and `tests/test_paper.py` fails if
any of them moves.

| File | What it is |
|---|---|
| `homological_flat_bands_2026-08-28.pdf` | the flat-band manuscript, the one that cites this repository by commit. |
| `nested_quotient_master_2026-08-28.pdf` | the master derivation, uniting it with the nested-quotient circuit theory. **The current artifact of record.** |
| `nested_quotient_master_2026-08-28.txt` | its extracted text, same provenance and standing as the line below. |
| `homological_flat_bands_2026-08-28.txt` | its text, extracted once with `pypdf` 6.16.2 so checks can read it. Derived, never authority — where the two differ the PDF wins. |
| `../verify_core.py` | the portable verifier §9 promises. Root-level so the manuscript's printed `python3 verify_core.py` is true as printed. |

## What the manuscript says about this repository

§9 pins commit `ca3d440a7f93c17569e12d0511847505b6b72c5a` and reports four
counters for it. All four were re-measured at that commit, before anything in
this directory existed:

| §9 says | measured at `ca3d440` |
|---|---|
| 119 exact-rational checks | 119 T1 checks |
| 29 numerical cross-checks | 29 T2 checks |
| 349 repository tests | 349 collected, 349 passed |
| 28 Lean theorems, no omitted proofs | 28 theorems, 0 `sorry` |

Those numbers describe `ca3d440` and stay true there; `git checkout ca3d440 &&
make verify` reproduces them. They are **not** a description of HEAD and were
never meant to be — this session's own work moves them, which is what pinning a
commit is for. The current counts are in `FRONTIER.md` §1.

One thing §9 promised that did not exist at that commit: `verify_core.py`.
It exists now — and it proves more than either manuscript claims for it (below).

The master document states the same counters and adds the right qualification
itself: "the counts are provenance information rather than independent evidence
here". That is correct, and it is what this directory exists to fix.

## The claim-to-check map

Every displayed statement, and the command that re-establishes it here in about
a second. A reader who does not believe a line should not have to read code to
find out who checks it.

```bash
workhouse verify --only '<check name>'
```

| Manuscript | Check | Tier |
|---|---|---|
| eq. (4) `E_F,N = 2 C_F` | `each channel gap is C_F + C_R/2, and the weights sum to one` | T1 |
| eq. (7)–(12) Thm 1, factorization and spectrum | `B B^dagger = q I - d conj(d)^T for the curl incidence` | T1 |
| eq. (13)–(15) Thm 2, the carrier | `dim Z_2 = L^3 + 2 by rank, not by re-arranging the formula` · `rank d_3 = L^3 - 1 on the built complex` · `cube boundaries and three wrapping sheets SPAN Z_2` | T1 |
| eq. (6), App. B, `d_2 d_3 = 0` | `d_2 d_3 = 0 on the built complex` | T1 |
| Thm 1 ↔ Thm 2, the missing bridge | `the Bloch and chain routes to the carrier agree` | T1 |
| eq. (16) `q_min = 4 sin^2(pi/L)` | `q_min on the L-torus grid is 4 sin^2(pi/L)` | T1 |
| eq. (17)–(19) fusion, dimensions, Casimirs | `the four channel weights follow from dimension and Casimir` | T1 |
| eq. (18) the resolvent weight | `each channel gap is C_F + C_R/2, and the weights sum to one` | T1 |
| eq. (20)–(21), App. A eq. (40) | `A_N and B_N are the channel sums, not transcriptions` | T1 |
| eq. (23) Thm 3, `t_N` | `t_N = B_N - A_N` · `t_2 = 0 and t_3 = 5/612` · `t_N > 0 for N >= 3` | T1 |
| eq. (25) large-N expansion | `large-N expansion of t_N through 1/N^9` | T1 |
| eq. (26) `W_N = 12 t_N u^2` | `the two band spans ARE the two incidence spectra` | T1 |
| §4 unsigned-incidence control | `the two band spans ARE the two incidence spectra` | T1 |
| eq. (27)–(28) the second-order assembly | `d_- = 1/2 + 12*leak_2, and leak_2 = -11/306` · `d_- - 4 t_- = 11/306` | T1 |
| eq. (29)–(30) `b_3`, `leak_3`, `d_3` | `d_3 = 7/32 + 12*leak_3 - 4*b_3` · `leak_3 is assembled from the domino diagonal and the vacuum piece` | T1 |
| eq. (31)–(34) Thm 6 | `E_flat and t(u) carry the ledger coefficients` · `one assembly formula gives every registered band value` | T1 |
| eq. (35) `Delta_L` | `Delta_L = 4 tau(u) sin^2(pi/L) is positive and falls as L^-2` | T1 |
| eq. (39) the fourth-order shape basis | `Phi_C vanishes at Gamma along every direction` · `the carrier projection is where the 1/q comes from` | T1 |
| §5 Hamer cross-check | `Hamer's 1+- series matches the C-odd Gamma-point coefficients through x^3` | T2 |
| §6 the fourth-order firewall | `no fourth-order coefficient enters the manuscript` | T1 |
| Table 2, the SU(3) ledger | `the manuscript's SU(3) ledger is this registry, value by value` | T1 |
| Table 1, evidence map | see **What is not checked**, below | — |
| MASTER eq. (18) the isotropy premise | `the shared-link weights are Weingarten, not an isotropy assumption` | T1 |
| MASTER eq. (34) `q_max(L)` parity | `the zone maximum of q is 12 only at even L` | T1 |
| MASTER Fig. 2 | `q at the four high-symmetry points is 0, 4, 8, 12` | T1 |
| MASTER §9 eq. (60)–(64) axial datum | `on an axial cut the mixed invariants vanish and the norm divides` | T1 |
| MASTER closure audit, the C2 obstruction | `FINDING: the retained Gamma/axis data cannot identify C_shp` | T1 |

## What is not checked, and what a referee should press on

Recorded because a claim-to-check map that hides its gaps is worse than none.

- **eq. (18)'s "isotropy" is the single unproved physical input of the whole
  second-order chain.** The arithmetic consequence is exact — `d_R/N^2` sums to
  1 per family, and that is checked — but the premise that the six free-link
  Haar integrations leave the shared-link tensor maximally mixed is asserted in
  one word. The corpus source states the clause that earns it
  (`corpus-import/papers/flat_band/PAPER_FLUX_glueball_flat_band_v1_1.tex`);
  the manuscript compresses it. Independent support exists at N = 3 only.
  The decisive and cheap test: an orientation-resolved Weingarten evaluation at
  N = 3 and N = 4 returning `A_N` and `B_N` separately.
- **Theorem 3's proof needs one more clause.** "Every second-order
  inter-plaquette process uses one shared link" is false in general and true in
  the charge-odd sector only, because `V` is C-even and `<0|V|p,-> = 0`. This
  repository's C13 is the record of what omitting that costs: `A_3 + B_3 =
  -481/612` is exactly the superseded C-even value. The check
  `ell_N = A_N + B_N + 1/C_F, the vacuum-mediated route at every rank` pins
  the size of the omitted route at every rank.
- **Lemma 4's "unmatched" must mean multiplicity exactly one.** A link carrying
  three fundamental indices does *not* integrate to zero for SU(3) — the
  manuscript's own `+u` in eq. (32) is that epsilon channel. The corpus engine
  states the correct hypothesis ("at least 2 links private to it"); an
  independent re-derivation of the geometry gives minimum 2, so the paper's
  "at least one" is true and understated.
- **Table 1 row 5's "32 lifter classes" misdescribes its source.** The
  enumeration has three lifter classes evaluated over 32 five-trace numerator
  patterns each, 96 in total. Nothing in `src/`, `ledger/`, `lean/` or `tests/`
  checks any of it.
- **§9's "The analytic proof in this paper is self-contained"** is jointly
  refuted by the three items above: eq. (18) is asserted, Lemma 4 carries no
  proof environment, and Remark 5's enumeration was performed elsewhere.
- **The abstract attaches "For L >= 3" to the carrier count; Theorem 2 does
  not, and does not need it.** The caveat belongs to the twelve-neighbour Bloch
  adjacency. `the L^3+2 count is chain-level, not the Bloch convention` pins
  L = 1 and L = 2.
- **§6's "three harmonic sheets" are not harmonic.** The sheets Theorem 2
  exhibits are cycles but are not in `ker d_3*`; `L_up` moves them with
  Rayleigh quotient exactly 2 at every size. Nothing downstream breaks —
  Proposition 7 rests on `B* w = 0`, which covers all of `ker d_2` — but §6's
  real-space restatement does not cover the objects Theorem 2 constructs.
  Recorded as `FINDING: the wrapping sheets are cycles but NOT harmonic`.
- **There is no all-rank formula for `E_flat,N`.** Theorem 3 gives the scalar
  only as "momentum independent"; eq. (32) is SU(3). So "exact all-rank
  coefficient" covers `t_N` alone, and there is no all-rank analogue of
  eq. (35).
- **Table 2's `u^1` row is SU(3)-only**, not an SU(3) specialization: it is
  `-<p,-|V|p,-> = 1`, which needs the epsilon channel and vanishes at N >= 4.
  Table 2 carries no scope column saying so.
- **Hamer cannot see the hopping.** `q(0) = 0`, so no rest-frame series
  constrains `tau(u)`; the agreement pins `12 leak_3 - 4 b_3` and neither
  coefficient alone. Recorded as `FINDING: no Gamma-point datum can constrain
  the hopping`. This does not weaken `b_3`, which the abstract-domino engine
  computes directly and which the `lambda = 8` band top separates.

## verify_core.py

```bash
python3 verify_core.py        # or: make paper
```

Standard library only, no arguments, no floats, about a fifth of a second. It
exists so a referee who will install nothing can still check the arithmetic,
and so §9's reproducibility sentence names something real.

Two of its checks are stronger than the manuscript claims for them:

- **the incidence identity is exact, not residual.** §9 promises a check "at
  deterministic generic momenta", which in floating point means a small
  residual. A torus point with rational `tan(k_j/2)` has `exp(i k_j)` a
  Gaussian rational, so `B B* = q I - w w*`, `B* w = 0` and the characteristic
  polynomial `x (x - q)^2` are all *decided* in exact arithmetic at five
  hard-coded points.
- **the torus ranks come with a basis.** Rank over `F_p` bounds the kernel from
  below; the exhibited cycles — every elementary cube boundary plus the three
  wrapping sheets — bound it from above. The two bounds meeting is the
  manuscript's own proof, `ker d_2 = im d_3 (+) H_2`, carried out rather than
  cited.

It now also **derives the manuscripts' central input**: the shared-link channel
weights follow from the order-2 Weingarten values, computed from the `S_2` Gram
inverse in exact `Fraction` arithmetic with explicit index sums. A referee who
installs nothing can check that eq. (18)'s one asserted word is a theorem.

What it does not do, said plainly: it does not enumerate the third-order lifter
classes, it does not sum the cube histories or reproduce the microscopic axial
sweep, and it decides nothing about the disputed fourth-order coefficient.
