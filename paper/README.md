# The manuscript of record

*Nested-quotient temporal histories and homological flat bands in
strong-coupling SU(N) Hamiltonian lattice gauge theory*, Alexander Smith —
the outward-facing statement of this program, and the artifact that cites this
repository by commit.

Manuscripts are pinned here for the same reason `runs/` is pinned: the checks
below refer to *these bytes*. `SHA256SUMS` records them and `tests/test_paper.py`
fails if any of them moves.

| File | What it is |
|---|---|
| `master_paper_2026-08-29.tex` | **the final edition, and the current artifact of record.** Source, pinned alongside its build. |
| `master_paper_2026-08-29.pdf` | its build. Byte-reproducible; see **Rebuilding**. 16 pages, zero overfull boxes, zero undefined references. |
| `master_paper_2026-08-28.tex` | the united edition. Superseded by the line above, kept as pinned evidence. |
| `master_paper_2026-08-28.pdf` | its build. |
| `homological_flat_bands_2026-08-28.pdf` | the flat-band manuscript, the first artifact to cite this repository by commit. Superseded, kept as the pinned original. |
| `nested_quotient_master_2026-08-28.pdf` | the master derivation, uniting it with the nested-quotient circuit theory. Same standing. |
| `*_2026-08-28.txt` | their extracted text, extracted once with `pypdf` 6.16.2 so checks can read them. Derived, never authority — where the two differ the PDF wins. |
| `verify_core.py` | the portable verifier: 29 checks, standard library only, no float constructed anywhere, matching the final edition's Reproducibility section. |
| `../verify_core.py` | the flat-band manuscript's, 16 checks. Root-level so *that* manuscript's printed `python3 verify_core.py` is true as printed. |

```bash
make paper      # both verifiers, then three reproducible pdflatex passes
```

## What the final edition adds

The 28 August united edition's four self-contained statements are unchanged in
substance: the Weingarten derivation of the channel weights, the all-rank
second-order law, the Bloch–chain bridge, and the fourth-order obstruction
certificate. Four things are new, and each carries its own check.

1. **What a link cutoff drops, exactly.** Retaining only the singlet and
   `Lambda2 F` routes projects the hopping to `w_Lambda2 - w_1 = -1/12` —
   opposite in sign to `t_3` and 10.2x larger — and what is dropped is
   `w_Sym2 - w_Adj = 14/153`, the two summing to `5/612`. This is arithmetic on
   the Weingarten weights alone, so a counterterm for a published `T1`
   Hamiltonian is `14/153` and never `5/612`. §5, Corollary 14.
2. **The two-cube census IS that ledger, channel by channel.** The
   1,590,462-state face-sharing `(3,2,2)` prism recovers `t_3 = 5/612`
   target-blind, and its six link-irrep coefficients are the four Weingarten
   fusion weights individually: `c_1 = -w_1`, `c_8 = -w_Adj`, and each
   like-family weight split evenly between an irrep and its conjugate. Summing
   to the right number is weak evidence; agreeing channel by channel is not.
   Reported rather than proved: the six coefficients are rational
   reconstructions of finite-precision contractions (residual 2.1e-14), the
   certificate declares `symbolic_exact_local_amplitudes: false`, and the build
   was not reproduced here. §5, Reported result 12.
3. **The charge-even sector gets a closed form.** Its Bloch spectrum is the
   cubic `mu(mu - p)^2 = 4 â1 â2 â3` with `p + q = 12`, so one zone function
   runs both sectors; the range `[-4, 12]` is exact, the top attained only at Γ
   and the floor on the three planes `k_j = pi` (triple only at R); and the
   charge-even Γ splitting is `12 t_(r,+)` exactly — which pins the
   charge-even hopping where the charge-odd rest frame has no analogue. §6.
4. **The open fourth-order coefficient gets a geography, not a verdict.** An
   explicit second witness `C_alt` exhibits the non-identifiability by
   construction; the shape fit's `C` row sums to zero, so no Γ-anchoring error
   can move `C_shp` at all; six of 189 records carry 81% of it; and the sealed
   609-cluster sweep is shown, by reading its engine, to be structurally
   incapable of deciding it. §9.

`C_shp` stays open. Nothing in the edition prefers a side, and
`verify_core.py` assumes no value for it.

## Every displayed result names its check

That is the edition's one device: 105 `\chk` labels over 98 distinct checks,
each printed beneath the equation it establishes, so any line re-runs in about
a second:

```bash
workhouse verify --only '<the name printed under the equation>'
```

The device is itself checked. `every \chk in every pinned edition names a check
that exists and passes` scans **every** `.tex` in this directory — not one
named file — and resolves all 137 printed labels across both editions against
the live registry. The first draft of that check hard-coded the 2026-08-28
edition, which would have left the successor's labels unverified; a device that
verifies only the edition nobody is editing any more is worse than none.

`ledger/documents.yaml` legends both editions, so a check's `section` string
can cite either and `tests/test_documents.py` keeps the reference resolvable —
the citation runs both ways.

Neither edition is in `PAPER_TEXTS`, so neither is scanned by the fourth-order
firewall check. Both discuss the fourth order on purpose, to state the
obstruction. The firewall is a property of the two original manuscripts and
remains measured for them.

## The claim-to-check map

Every displayed statement in the final edition, in printed order, with its
tier. Generated from the `.tex` against a live `workhouse verify`, so it cannot
disagree with the paper.

**Hamiltonian and projected sector**

- T1 `the printed towers are canonical-u: 4*Delta(3u/2) reproduces them verbatim`
- T1 `the 4**r rescaling breaks the bridge: order 2 off by 16, order 3 by 64`
- T1 `each channel gap is C_F + C_R/2, and the weights sum to one`
- T1 `at N = 2 the C-odd hopping vanishes and the C-even one does not`

**Oriented incidence and the exact carrier**

- T1 `B B^dagger = q I - d conj(d)^T for the curl incidence`
- T1 `dim Z_2 = L^3 + 2 by rank, not by re-arranging the formula`
- T1 `cube boundaries and three wrapping sheets SPAN Z_2`
- T1 `the L^3+2 count is chain-level, not the Bloch convention`
- T1 `the Bloch and chain routes to the carrier agree`

**The wrapping sheets are cycles, not harmonic**

- T1 `FINDING: the wrapping sheets are cycles but NOT harmonic`

**Exact all-rank dynamics at second order**

- (again) `each channel gap is C_F + C_R/2, and the weights sum to one`

**The channel weights are a theorem**

- T1 `the shared-link weights are Weingarten, not an isotropy assumption`
- T1 `the Weingarten route is independent of the corpus`
- T1 `the published dimension-ratio matrix element is this registry's weight formula`
- T1 `the four channel weights follow from dimension and Casimir`
- T1 `A_N and B_N are the channel sums, not transcriptions`

**The shared-link law**

- T1 `t_N = B_N - A_N`
- T1 `t_N > 0 for N >= 3`
- T1 `t_2 = 0 and t_3 = 5/612`
- T1 `large-N expansion of t_N through 1/N^9`

**The vacuum-mediated route**

- T1 `ell_N = A_N + B_N + 1/C_F, the vacuum-mediated route at every rank`

**Finite-volume width**

- T1 `the zone maximum of q is 12 only at even L`
- T1 `q_min on the L-torus grid is 4 sin^2(pi/L)`

**The orientation signs are essential**

- T1 `the two band spans ARE the two incidence spectra`

**The second-order coefficient on a two-cube space**

- T1 `the connected two-cube geometry has exactly four cross-cell pairs, each -1`
- T1 `the B=6 connected kernel is (5/612) G_conn + diag, with the certified spectrum`
- T2 `the certificate's own gates pass, target-blind, with the wrong-sign control rejected`
- T1 `the B=6 six-channel census sums to the registry's own t_3 = 5/612`
- T1 `the B=6 six-channel census IS the Weingarten four-channel ledger, channel by channel`

**One truncation, two constructions**

- T1 `B=6 retains every adjacent shared-link channel; B=4 provably cannot`
- (again) `the B=6 six-channel census IS the Weingarten four-channel ledger, channel by channel`
- T1 `FINDING: the T1 link cutoff reverses the sign of t_3, and 14/153 is what it omits`
- T2 `FINDING: a full T1 = B = 4 cube Hamiltonian reproduces -1/12 and the reversed shell`
- T2 `FINDING: the B = 6 cube flips the sign back to +5/612, closing the decisive test`
- T1 `the B = 6 scalar misses the bridge's by exactly the same-face sextet route`
- T1 `the certificate's finite-volume fingerprints, and 29 = L^3 + 2 is the Lean cycle count`

**The charge-even sector in closed form**

- T1 `the C-even characteristic polynomial is mu(mu - p)^2 = 4 a_1 a_2 a_3`
- T1 `p + q = 12: one zone function runs both sectors`
- T1 `the Bloch cubic IS the finite L = 3 and L = 4 plaquette spectrum, exactly`
- T1 `the C-even range is exact; the top is attained only at Gamma, the floor on three planes`
- T1 `the C-even band touches its floor exactly on the three planes k_j = pi`
- (again) `the C-even band touches its floor exactly on the three planes k_j = pi`
- T1 `the C-even spectra at the four high-symmetry momenta`

**One assembly, both sectors, both orders**

- T1 `one assembly formula gives every registered band value`
- T1 `one assembly formula gives every C-even value at both orders`
- T1 `the plaquette graph is 12-regular and two faces share at most one link`
- T1 `both declared coincidences, checked: one is ell_N at all ranks, the other is bare`

**Where the rest frame is not blind**

- T1 `the C-even Gamma point pins t_+, exactly where no C-odd Gamma datum can`
- T1 `the C-even curvature is (4/3)|t_+| at both orders, and isotropic`
- T1 `the C-even bandwidth is 16|t_+| at every order; the C-odd manifold width is 12|t_-|`

**SU(3) through third order**

- T1 `d_3 = 7/32 + 12*leak_3 - 4*b_3`
- T1 `leak_3 is assembled from the domino diagonal and the vacuum piece`
- T1 `E_flat and t(u) carry the ledger coefficients`
- T1 `d_- = 1/2 + 12*leak_2, and leak_2 = -11/306`
- T1 `FINDING: no Gamma-point datum can constrain the hopping`

**What the homology protects**

- (again) `B B^dagger = q I - d conj(d)^T for the curl incidence`
- T1 `the carrier projection is where the 1/q comes from`
- T1 `clearing the denominator reproduces the five-element numerator basis`

**The fourth-order boundary**

- T2 `v10a.26 A, B, D match the sealed rationals within 2.3e-13`
- T2 `FINDING: alpha_new falls outside the corpus's own 2.3e-13 bound`

**The obstruction is polynomial**

- T1 `FINDING: the retained Gamma/axis data cannot identify C_shp`
- T1 `Phi_C vanishes at Gamma along every direction`
- T1 `the crosswalk is exactly scalar on the momentum axes`
- T1 `on an axial cut the mixed invariants vanish and the norm divides`

**A second witness**

- T1 `FINDING: an explicit second witness C_alt exhibits the C2 non-identifiability`
- T2 `the C_alt witness IS the balanced eps-free continuation, and Delta_C/(A/2) = 15/32`

**Where the coefficient lives**

- T1 `checkpoint values at X, M, P, R`
- T1 `the four extraction formulas invert the ansatz`
- T1 `X is blind to B, C, D — it fixes A alone`
- T1 `the shape fit's C row sums to zero, so no Gamma-anchor error can move C_shp at all`
- T1 `a translation-local scalar shift changes nothing observable`
- T2 `FINDING: C_shp is carried by 6 of 189 records, not spread across the kernel`
- T2 `FINDING: A = 5/48 pins the normal sector's whole C4 contribution`
- T1 `C_normal = -A_normal/2: the agreed axial coefficient pins the normal channel`
- T2 `the two 189-record kernels agree everywhere except three amplitudes, and the on-site anchor swap moves C by exactly zero`

**What cannot decide it**

- T1 `FINDING: the marked-cluster engine emits the Gamma scalar only — a completed 609-sweep cannot decide C_shp`

**The tier collapse, as two integers**

- T1 `RETRACTED: the vertex count does NOT forbid B_shp and D_shp`
- T1 `FINDING: the tier collapse is two integer cancellations at record level`
- T1 `the vanishing coefficients are exactly the degree-3 ones`

**A near- statement that survives the dispute**

- T1 `Jordan bound q(k) >= (4/pi^2)|k|^2 holds on the whole zone`
- T2 `the criterion survives C2: K depends on the kernel only through sqrt(W_4)`
- T2 `the statement is non-vacuous only below an explicit coupling`

**External comparisons**

- T2 `Hamer's 1+- series matches the C-odd Gamma-point coefficients through x^3`
- T2 `Hamer's 0++ series matches the C-even Gamma-point coefficients through x^3`
- T1 `the m_n = 2^(n-1) a_n bridge is the x = 2u conversion`
- T2 `the Hamer table is pinned, and the a_4 agreement is primary-source`
- T1 `the KPS 1980 string-tension table equals the certified sigma series EXACTLY`
- T1 `sigma_n^phys = (-1)^n sigma_n^raw, and C5 is the n = 3 case`
- T1 `the ratio and sigma series reproduce E_flat exactly`
- T1 `the errata-resolved Euclidean series is doubly sourced, transcription for transcription`
- T1 `FINDING: Munster's 1985 table shifts his 1982 erratum at eighth order`
- T1 `the overlap obstruction was published in 1988, and it scales`
- T1 `a cross-regime paper never supplies a value`

**Scope**

- T1 `Delta_L = 4 tau(u) sin^2(pi/L) is positive and falls as L^-2`

**Channel weights in closed form**

- (again) `the four channel weights follow from dimension and Casimir`

**The Weingarten index sums**

- (again) `the shared-link weights are Weingarten, not an isotropy assumption`
- T1 `SU(3) Weingarten values follow from the general formula`
- T1 `the fourth moment integral |U_11|^4 = 1/6 at N = 3`

**The SU(3) coefficient ledger**

- T1 `the manuscript's SU(3) ledger is this registry, value by value`

**The charge-even ledger**

- (again) `one assembly formula gives every C-even value at both orders`
- T1 `FINDING: the certificate key 'bandmin' holds the band MAXIMUM, at both orders`

**Finite-volume chain calculation**

- T1 `d_2 d_3 = 0 on the built complex`
- T1 `rank d_3 = L^3 - 1 on the built complex`

**The two-cube geometry**

- T1 `the B=4 comparator on the same geometry gives -1/12 with the reversed spectrum`

## What is not checked, and what a referee should press on

Recorded because a claim-to-check map that hides its gaps is worse than none.

**Closed since the 28 August edition**, each by a named check:

- *eq. (18)'s isotropy premise*, which was the single unproved physical input
  of the whole second-order chain, is a theorem — `the shared-link weights are
  Weingarten, not an isotropy assumption` — and the derivation imports nothing
  from the corpus, which `the Weingarten route is independent of the corpus`
  measures.
- *"three harmonic sheets"* is corrected: the sheets are cycles and are not
  harmonic, with Rayleigh quotient exactly 2. `FINDING: the wrapping sheets are
  cycles but NOT harmonic`.
- *Theorem 3's missing clause* is stated as the vacuum-mediated route, as an
  all-rank formula rather than a one-rank erratum.
- *The `L >= 3` caveat* is confined to the twelve-neighbour Bloch adjacency.
- *Table 2's `u^1` row* is labelled `SU(3)`-only.
- *The unsigned-incidence "control"* is no longer a paragraph: it is §6.

**Still open against the final edition:**

- **The third-order lifter census is unchecked.** Three lifter classes over 32
  five-trace numerator patterns each, 96 contractions in total. Nothing in
  `src/`, `ledger/`, `lean/` or `tests/` checks any of them, and the edition
  says so in §1 item 7. Everything in §7 beyond second order rests on it.
- **`b_3`, `leak_3` and `d_3` are supplied-ledger values.** What is checked is
  the *assembly* — `d_3 = 7/32 + 12 leak_3 - 4 b_3` — not the contraction that
  produced the inputs.
- **There is no all-rank formula for `E_flat,N`.** The scalar is known only as
  "momentum independent"; the SU(3) expression is a specialization of nothing.
- **The two-cube construction was not re-run here.** Its builder needs
  `pyclebsch` and sealed NPZ inputs that did not travel, so the checks audit the
  delivered certificate's arithmetic against geometry rebuilt locally. Its
  diagonal `D_B6` is B6-truncated and not proved cutoff-stable, its finite-`u`
  validation is a 66-dimensional star rather than the full Hamiltonian, and no
  external group has reproduced the release.
- **Conjecture 13 (the all-rank even split) is a conjecture.** The channel
  identification of Reported result 12 is at `N = 3` only. Falsifying the
  conjecture needs a link-resolved census at some `N >= 4` in a truncation that
  still retains every adjacent shared-link channel; at `N = 4` the endpoint
  budgets make that `B >= 33/4`, and no such construction has been run.
- **Two premises are prose, not results, and both are load-bearing.** That the
  range of `P_-` is exactly the charge-odd one-plaquette span for `L >= 3`, and
  that the four fusion channels exhaust the second-order shared-link routes.
  The Weingarten theorem fixes each channel's weight; it does not establish
  that the list is complete. §11 now says so.
- **The two one-cube reconstructions are not an independent replication.** Both
  read the same pinned plaquette-matrix-element source, and the published
  table's `|M_rho|^2 = d_rho/N^2` is the very numerator of the weight formula.
  A cross-check of assembly, not a third confirmation of `t_3`.
- **The sector setup is asserted.** That the range of `P_-` is the charge-odd
  one-plaquette span for `L >= 3`, and that the four channels exhaust the
  shared-link routes, are arguments in prose. The published finite-rank matrix
  element corroborates the *weights*, not that premise.
- **C2 is open, and this edition does not narrow the interval.** It maps where
  the coefficient lives and rules out whole classes of instrument. The decisive
  move remains an off-axis contraction.
- **Nothing here crosses a regime boundary.** Infinite volume, the spectral
  bridge and the continuum limit are named in §11 as the unpaid debts they are.

## Rebuilding

```bash
cd paper
SOURCE_DATE_EPOCH=1787961600 FORCE_SOURCE_DATE=1 \
  pdflatex -interaction=nonstopmode master_paper_2026-08-29.tex   # x3
```

Three passes for the cross-references. `SOURCE_DATE_EPOCH` is what makes the
digest in `SHA256SUMS` reproducible — without it `pdflatex` stamps the build
time into the PDF and the pin fails on a rebuild that changed nothing. Needs
`texlive-latex-base` and `texlive-latex-recommended` (for `booktabs`). Zero
overfull boxes and zero undefined references is the accepted state; the build
is 16 pages.

`1787961600` is 2026-08-29 00:00 UTC, so the PDF's internal creation date
matches the date on its title page. The 28 August editions use `1756339200`,
which is 2025-08-28 — one year early. Their bytes are pinned evidence and stay
as they are; the discrepancy is recorded here rather than corrected, and the
new edition simply does not repeat it. Rebuilding *those* still needs their own
epoch:

```bash
SOURCE_DATE_EPOCH=1756339200 FORCE_SOURCE_DATE=1 \
  pdflatex -interaction=nonstopmode master_paper_2026-08-28.tex   # x3
```

## What the manuscripts say about this repository

The flat-band manuscript's §9 pins commit
`ca3d440a7f93c17569e12d0511847505b6b72c5a` and reports four counters for it:
119 exact-rational checks, 29 numerical cross-checks, 349 repository tests, 28
Lean theorems with no omitted proofs. All four were re-measured at that commit
and are correct there. They are **not** a description of HEAD and were never
meant to be — that is what pinning a commit is for.

The final edition pins commit `f25328f8d6658af63588fb3d30dbd3b7f6ede9c0` —
the commit immediately before this one, which carries every check the
edition names and none of the edition's own bytes — and reports its counters
there. `git checkout f25328f && make verify` reproduces them:

| Layer | Count |
|---|---|
| T0 — Lean 4 theorems, no `sorry` | 40 |
| T1 — exact re-derivations | 179 |
| T2 — numerical, within a stated tolerance | 46 |
| Repository tests | 472 |

All 40 T0 theorems were confirmed by `#print axioms` against the built oleans:
39 depend on `[propext, Classical.choice, Quot.sound]` and one, `dim_Z₂`, on
`[propext]` alone. Nothing else.

Those counters are provenance, not independent evidence, and the edition says
so. The live counts are in `FRONTIER.md` §1.

## verify_core.py

```bash
python3 paper/verify_core.py    # 29 checks, ~0.5 s
python3 verify_core.py          # the flat-band manuscript's 16
```

Standard library only, no arguments, no floats. It exists so a referee who will
install nothing can still check the arithmetic. Nine claim groups now, matching
the final edition's Reproducibility section: the coefficient ledger; the
Weingarten derivation by explicit index summation; the incidence identity,
*decided* in exact Gaussian-rational arithmetic at rational torus points rather
than checked to a residual; the chain condition and finite-torus ranks with an
explicit kernel basis; the sheets' Rayleigh quotient; the two-cube geometry,
spectra and channel identification; the charge-even cubic; the fourth-order
checkpoint algebra and the obstruction; and the coupling convention.

Every value in it is a `Fraction`. No float is constructed anywhere in the file,
so "agreement" there always means equality, never proximity — and
`tests/test_portability.py` and `tests/test_paper.py` join its hard-coded
ledger to `constants.py`, because two verifiers that drift apart certify two
different papers.

What it does not do, said plainly: it does not enumerate the third-order lifter
classes, it does not sum the cube histories or reproduce the microscopic axial
sweep, it does not re-run the 1,590,462-state two-cube construction, and it
decides nothing about the disputed fourth-order coefficient. Its fourth-order
group is the *obstruction* as arithmetic — the extraction formulas, the
blindness of `X`, and the identical vanishing of `e_2` on every axial cut.

## The referee trail

- `docs/referee/final_paper_review_2026-08-28.md` — the review that drove the
  united edition.
- `docs/referee/final_paper_2026-08-28.md` — this repository's own referee
  document on the flat-band manuscript.
- `docs/decisions/0014-a-manuscript-enters-as-pinned-evidence.md` — why `paper/`
  exists and the four rules that come with it. A future revision is a new pinned
  artifact plus a regenerated map, in one visible diff; this directory is the
  second time that has happened.
