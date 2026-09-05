# Research results and manuscript editions

For the current mathematical state, start with
[Current research](../docs/current_research.md),
[FRONTIER.md](../FRONTIER.md), and the claim graph through
`workhouse why G18`. The manuscript editions below preserve the arguments and
verification coverage recorded when they were written; they are not the
current status register for the September results.

The [rooted Wilson contraction theorem](research_notes/G18_ROOTED_WILSON_CONTRACTION_20260905.md)
establishes convergent nonunitary vacuum creator coordinates on an explicit
coupling disk uniform in spatial volume and temporal mesh. Its
[infinite-lattice continuation](research_notes/G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md)
constructs an analytic creator family with a quantitative local convergence
bound. The [sealed verification run](../runs/wilson_rooted_contraction_2026-09-05/README.md)
distinguishes these analytic proofs from finite exact controls and the scalar
Lean theorem. Controlled physical operator realization and the complete
excited-space identification remain open.

The current research guide also connects the September C2 resolution,
symbolic all-rank assembly, and fixed-spacing construction to their proofs
and downstream questions. Older disputes and proposed next steps in pinned
editions remain part of the research history; use the live ledger for their
present verdicts.

## The manuscript of record

*Volume-uniform electric-shell isolation, exact shared-link hopping, and a
homological carrier in strong-coupling SU(N) Hamiltonian lattice gauge
theory* — master edition, Alexander Smith, 30 August 2026. It merges the two
lineages this directory had been carrying in parallel: the 29 August master
paper (two-column, 22 pages) and the 30 August publication edition rev. 4
(40 pages). Where they overlap, the later text governs; where only one carries
something, it is kept.

The lineage begins with *Homological flat bands in strongly coupled SU(N)
Hamiltonian lattice gauge theory*, 28 August 2026 — the first piece of this
program written for outside readers, and the first artifact that cites this
repository by commit.

It is pinned here for the same reason `runs/` is pinned: the checks below refer
to *these bytes*. `SHA256SUMS` records them and `tests/test_paper.py` fails if
any of them moves.

| File | What it is |
|---|---|
| `workhouse_publication_edition_rev5_2026-08-30.tex` | **publication edition, revision 5** — the maintainer's latest single-column article, pinned verbatim on 2026-09-01 (source only; no build, see **Revision 5** below). Same lineage as v2, rewritten around the volume-uniform electric window (Thm. 1), the periodic Yarotsky descent and the SU(3) Riesz island, the small-support two-cycle and reduced same-face lemmas that make second-order process completeness a theorem, the fixed-momentum carrier, the radius-two Ritz extension, the exact G17 reduction, and a new external-comparisons section that places Schor, O'Carroll–Dantas Barbosa, Bricmont–Fröhlich, Münster and Yarotsky against the paper's own claim boundary. |
| `master_paper_2026-08-30.tex` | **the master edition, the current artifact of record.** The two lineages merged. From the publication edition rev. 4: the volume-uniform electric window `spec(H_E) ∩ [0, 5C_F/2) = {0, 2C_F}` with an external margin ≥ `C_F/2` (Thm. 1, which proves more than the retained-shell premise asked for); the SU(3) all-orders finite-volume Riesz island from Yarotsky's local spectral enclosure (Thm. 2); the fixed-momentum carrier and the exact locality/sharp-momentum tradeoff (Prop. 10); the centre-charge process-completeness lemma and the explicit projector cross matrix element, which make the global order-u² assembly a corollary with no completeness hypothesis; the detached-replayed radius-two Ritz extension with its onset proposition; and the exact G17 free-energy reduction. From the 29 August master paper: the **retraction** of the Bloch–chain "coincidence" reading (the Γ block *is* `b_2(T^3)`) and the harmonic representatives that follow; the executed `B = 7` six-face probe; the sharp zone minimum `min_{|k|≥r} q = 4 sin²(r/2)`, which corrects the crossover constants from 17.04/23.66 to 10.85/15.06; the weak-inequality retention rule and what it does *not* confirm; the Weingarten `SU(N)`-vs-`U(N)` rank argument; the tier counter table and the Lean paragraph, including the retraction of "nothing that bears on `C_shp` appears there". Kept from v2 and dropped by both uploads: the planar closed form `1 - 4N^3 t_N = (2N^4+31N^2-9)/((N^2-1)(2N^2-1)(4N^2-9))` and the coverage appendix. |
| `master_paper_2026-08-30.pdf` | its build (Tectonic 0.15.0, 46 pages, clean log: zero undefined references, zero overfull boxes). Rebuild: `python3 make_coverage.py && tectonic master_paper_2026-08-30.tex`. |
| `coverage_master.tex` | its generated coverage appendix: all 126 inline `\chk` markers, verbatim, under the section that carries each. |
| `workhouse_publication_edition_v2_2026-08-30.tex` | the publication edition v2, superseded by the master edition above and kept pinned. Built from the 29 August publication edition plus, most importantly: proofs of the two formerly load-bearing prose premises — the retained shell and second-order process exhaustion — so the global order-u² torus assembly is now a theorem (new, flagged as not yet externally refereed; the combinatorial cores are machine-enumerated and the two classical representation inputs named). Also: the planar closed form `1 - 4N^3 t_N = (2N^4+31N^2-9)/((N^2-1)(2N^2-1)(4N^2-9))` with checked positivity and monotonicity; the per-channel resolvent matrix-element equation closing the projector-norm-to-hopping step; torus rank/kernel checks extended through L = 5; a subsection reporting the sealed cutoff-free radius-two delivery, whose second-order block contains a rational sub-block with straddle exactly `2 t_3 = 5/306`; and a generated appendix printing all 119 inline `\chk` markers so coverage is auditable. |
| `workhouse_publication_edition_v2_2026-08-30.pdf` | its build (Tectonic 0.15.0, 38 pages, clean log). Rebuilt on 2026-08-30 after eleven of its `\chk` labels were corrected — see **Label drift**, below. |
| `coverage_generated.tex` | its coverage appendix, 118 markers. |
| `verify_publication_core.py` | the exact verifier both the master edition and v2 name: 38 checks, standard library only, every value a `Fraction`, no float constructed anywhere in the file. It does **not** cover the arithmetic new in the master edition — the Casimir shelf, the Riesz-contour arithmetic, the cycle censuses, the fixed-momentum carrier, the harmonic representatives, the sharp zone minimum — and the master edition's §12 says so rather than implying otherwise. Those live in the registry, under `workhouse verify`. |
| `verify_radius2_report.py` | the float half, kept in a separate file so the exact one stays float-free: 6 checks at stated tolerances against the sealed radius-two artifact (stdlib npz reader + Jacobi diagonalisation, no numpy). |
| `two_cube_cutoff_free_radius2_finite_u_spectrum.npz` | the sealed 29 August cutoff-free radius-two delivery, pinned; `verify_radius2_report.py` refuses any other bytes. Its certificate sits beside it. |
| `make_coverage.py` | the coverage-appendix generator. It regenerates the appendix of **every** edition that prints one — `coverage_master.tex` and `coverage_generated.tex` — because a single hard-coded source is how one edition's appendix ends up describing another. Run it before rebuilding either tex. |
| `make_figures.py`, `figure_*.pdf` | the three vector figures and their generator (NumPy + Matplotlib). |
| `master_paper_2026-08-28.tex` | the united edition of 28 August, superseded, kept pinned. The two manuscripts below merged into one, with the four results this repository added on 2026-08-28 folded in. Source, not just output — the `.tex` is pinned alongside the `.pdf`. |
| `master_paper_2026-08-28.pdf` | its build. Byte-reproducible; see **Rebuilding** below. |
| `homological_flat_bands_2026-08-28.pdf` | the flat-band manuscript, the one that cites this repository by commit. Superseded by the united edition, kept as the pinned original. |
| `nested_quotient_master_2026-08-28.pdf` | the master derivation, uniting it with the nested-quotient circuit theory. Superseded by the united edition, kept the same way. |
| `nested_quotient_master_2026-08-28.txt` | its extracted text, same provenance and standing as the line below. |
| `homological_flat_bands_2026-08-28.txt` | its text, extracted once with `pypdf` 6.16.2 so checks can read it. Derived, never authority — where the two differ the PDF wins. |
| `verify_core.py` | the master paper's portable verifier: 12 checks, standard library only, matching its Reproducibility section; finite-volume ranks through L = 5. |
| `../verify_core.py` | the flat-band manuscript's, 16 checks. Root-level so *that* manuscript's printed `python3 verify_core.py` is true as printed. |

Two verifiers because there are two papers. They overlap on the ledger and
diverge where the documents do: the root one follows the flat-band
manuscript's equation numbers, the one here follows the master paper's
Reproducibility section and adds the assembly formula, the band spans and the
torus ranks with a spanning cycle basis. Both are exact, stdlib-only, and
carry no floats.

```bash
make paper      # both verifiers, then three reproducible pdflatex passes
```

The review that drove the united edition is
`docs/referee/final_paper_review_2026-08-28.md`; this repository's own referee
document on the flat-band manuscript is `docs/referee/final_paper_2026-08-28.md`.

## Revision 5 (2026-09-01 pin)

`workhouse_publication_edition_rev5_2026-08-30.tex` is the maintainer's
revision 5 of the publication edition, pinned exactly as uploaded — CRLF line
endings included, which is why `.gitattributes` now marks `paper/**` as
`-text` like every other byte-pinned tree. It is not edited here, and the master edition remains the merged artifact of record;
rev. 5 is the article lineage carried forward. The guard `every \chk in the
united paper names a check that exists and passes` reads it like every other
edition, and on arrival seven of its 107 distinct labels resolved to nothing.
None of the seven was fixed by editing the paper:

- **Three became real checks**, in `electric_shell.py`, because the theorem
  and lemma they sit under delegate to finite arithmetic nobody had carried
  out: the window assembly (`below 5 C_F/2 the trivial-flux electric spectrum
  is exactly 0 and 2 C_F` — the support bound, the centre-neutral Casimir
  floor `C_2 ≥ N` by enumeration over su(3..7), the two winding energies as
  rational functions of `N`, and the fundamental-only face), the retained-shell
  count (`3L^3` from the built complex, and the 96 once-winding lines at
  `L = 4` that trivial flux removes), and the process-completeness lemma
  (`second-order off-diagonal processes are exactly the adjacent shared-link
  channels` — every centre-charge match `∂(εp+ηq) = ∂(ε'p'+η'r) mod N` at
  `L = 3, 4`, `N = 3, 4, 5` is the same-face route or the exchange route and
  nothing else, with the `L = 2` wrapping sheet as the lemma's sharpness).
- **Four are rescoped restatements of existing checks**, and each got a check
  of its own carrying the fact the new wording turns on rather than an alias:
  the `N = 2` zero located channel by channel (`Λ²F` is the singlet and
  `Sym²F` the adjoint there); the cubic built for the *unsigned-incidence
  comparison operator* from `B(k)` by dropping signs; the range statement with
  the floor on the three planes `k_j = π` — which also records that the older
  title `each edge is attained at one point only` overstates the floor; and
  the Hamer marker, now checked as a claim about the document (`a_4` and
  `m_Γ^(4)` appear nowhere in the source).

Recorded, not corrected, because the file is pinned as delivered:

- two missing backslashes inside math, `,qquad` (line 514) and `+overline{`
  (line 560), typeset as stray text rather than failing the build;
- "arithmetic and a the cited periodic-boundary version" (line 2949);
- the source includes `figure_radius_two_spectrum.pdf` and names
  `audit_radius2_attachment.py` and the detached two-cube release verifier;
  none of the three is in this directory, so the edition is pinned as source
  and not built here. `verify_publication_core.py` is present and passes its
  38/38 as printed;
- the hostile-scope audit commit it pins, `ff9a5976…`, is not reachable from
  this repository's history.

## The master edition (2026-08-30)

Two lineages had been running in parallel in this directory, both descended
from the 28 August united edition below: a two-column *master paper*
(29 August, 22 pages) and the single-column *publication edition* (rev. 4,
30 August, 40 pages). `master_paper_2026-08-30.tex` is the single document.

Merging them was not concatenation, and three of the decisions are worth
stating because a reader will otherwise wonder which text won:

1. **Later text governs where they overlap.** The publication edition rev. 4
   is the spine: its Theorem 1 (the volume-uniform electric window), Theorem 2
   (the SU(3) Riesz island), the process-completeness lemma and the explicit
   projector matrix element together retire the two prose premises that
   earlier editions carried, so the global order-u² assembly is a corollary
   with no completeness hypothesis at all.
2. **Where only one carries something, it is kept** — including one place
   where the older text is *right and the newer one is not*. Rev. 4 still
   reads the Bloch–chain agreement as a coincidence worth checking ("the 3 is
   the triple degeneracy of B(0) = 0, not b₂(T³)"). The 29 August master
   retracts that: under the DFT all of `im ∂₃` sits at nonzero momenta, so the
   Γ block *is* H₂ and the 3 *is* b₂(T³). The merged edition carries the
   retraction, and `the sheets average to harmonic representatives, and the
   Gamma block IS b_2` now checks it. Same for the near-Γ criterion: the
   master's sharp zone minimum `min_{|k|≥r} q = 4 sin²(r/2)` replaces the
   Jordan bound, which is tight only at the zone corner and loose by `π²/4`
   where the criterion is actually used — the crossover constants drop from
   17.04/23.66 to 10.85/15.06.
3. **Nothing was dropped because both uploads dropped it.** The planar closed
   form and the coverage appendix exist only in the repository's own v2 and
   are kept: losing an established exact result to a merge would be a
   regression the merge has no reason to make.

The merged edition is 46 pages against 40 and 22, and its build carries zero
undefined references and zero overfull boxes.

## The united edition (2026-08-28)

The two pinned manuscripts overlap heavily and disagree in emphasis: the
flat-band paper carries the homology and the second-order chain, the master
derivation carries the nested-quotient circuit theory and the fourth-order
material. `master_paper_2026-08-28.tex` is the single document, and it differs
from a concatenation in four places, each one a result this repository
established after both were written:

1. **The isotropy premise is derived, not assumed.** The flat-band paper's
   eq. (18) asserts isotropy in one word, and it was the single unproved
   physical input of the entire second-order chain. It is now a Weingarten
   computation: the six non-shared links integrate independently, collapsing
   the pair moment to degree $(2,2)$ on the shared link, and all four channel
   weights come out $d_R/N^2$. §4, Theorem 4.
2. **Theorem 1 and Theorem 2 are joined.** Both manuscripts state a $3\times3$
   Bloch spectrum and an $(L^3+2)$-dimensional chain-level carrier without
   remarking that the two agree. §3, Theorem 3.
3. **The vacuum-mediated route is stated as a rank formula.** "Every
   second-order inter-plaquette process uses one shared link" is false in
   general; the route $p\to|0\rangle\to p'$ connects any pair and is worth
   $1/C_F$. It vanishes in the charge-odd sector by C-parity, which is *why*
   the result stands. §4, Proposition 2.
4. **The fourth-order disagreement gets an obstruction certificate.** Not an
   adjudication — the two records differ by $4\Delta_C e_2$, and $e_2$ is the
   zero polynomial on every axial cut, so no $\Gamma$-point or axial datum
   separates them at any precision. §7, Theorem 7.

Every displayed result carries the name of the machine check that establishes
it, printed beneath the equation, so any line can be re-run in about a second:

```bash
workhouse verify --only '<the name printed under the equation>'
```

`ledger/documents.yaml` legends the 28 August edition as `MASTER paper` and
the 30 August one as `MASTER edition`, so a check's `section` string can cite
either and `tests/test_documents.py` keeps the reference resolvable — the
citation runs both ways. The two aliases exist because section numbers are not
portable between editions: the numbers in the existing citations are the
28 August edition's, and repointing one alias at a later document would
silently invalidate every one of them.

That device is itself checked. `every \chk in the united paper names a check
that exists and passes` resolves every printed label in **every** pinned
edition against the live registry and fails if one is renamed or deleted —
otherwise the paper would go on printing a command that no longer resolves,
which is the same drift `FRONTIER.md`'s staleness test exists to catch.

Since 2026-09-01 the same labels are graph edges: every legended edition emits
one `labels` edge per distinct `\chk` label, through the parser the guard uses,
so `workhouse why 'PUBLICATION rev5'` lists the checks that edition rests on
and `workhouse why <check>` says which editions print it. The claim-to-check
map is computed from the source rather than maintained here (ADR 0015).

### Label drift

The guard read *one* edition until 2026-08-30, and the editions written after
it drifted unwatched. When it was made to read them all, nineteen labels in the
publication editions named no registered check at all — some renamed out from
under the paper, some never registered. That is the failure the guard exists to
catch, reported green for as long as it covered a third of the artifact.

The resolution was not to widen anything:

- **Seven were renames.** The check existed under a different name; the label
  now points at it.
- **Eight became real checks.** The statements were checkable and nobody had
  checked them: the torus cycle census (short cycles, four-cycles), the
  one-cube shell, the orbit-constant connected diagonal, the census read
  channel by channel rather than only in the sum, the per-channel
  proportionality on all 56 adjacent pairs, boundary-factorised rigidity for a
  generic `M`, and the connected first-order cover count.
- **Four radius-two labels collapse onto one.** Those statements are checked
  by `verify_radius2_report.py`, a float program kept out of the exact layer on
  purpose. A registered T2 check now runs it, so the labels resolve and name
  what actually establishes the sentences.

Six further checks were written for material the merge itself brought in — the
`5C_F/4` Casimir shelf and the SU(3) additive spectrum behind Theorems 1 and 2,
the Fourier carrier and its locality price, the harmonic representatives, the
sharp zone minimum, and the weak retention rule — so the merged edition prints
no marker it cannot back. Fifteen new checks in total; see
`src/workhouse/invariants/electric_shell.py` and the additions to
`homology.py`, `uniformity.py` and `two_cube.py`.

Nothing was dropped to make the guard green, and no tolerance moved.

**2026-09-01, one rename with a correction.** The master edition's §9 label
`PREDICTION: the eps-sector at N=3 is Delta(rho + pi) = -25/512 and nothing
else` now points at `CORRECTED PREDICTION: the eps-sector at N=3 is
Delta(rho + pi~) = -25/512; u is NOT constrained`, and a one-paragraph
correction follows it in the source: the step `Δν = 0 ⇒ Δu = 0` was wrong
(ADR 0019). The 30 August prose is kept as written and the PDF is the 30
August build; `coverage_master.tex` and the manifest were regenerated.

The master edition is deliberately **not** in `PAPER_TEXTS`, and so is not
scanned by the fourth-order firewall check. It discusses the fourth order on
purpose, in §9, to state the obstruction. The firewall is a property of the two
original manuscripts and remains measured for them.

## Rebuilding

```bash
cd paper
python3 make_coverage.py                       # regenerate both appendices
tectonic master_paper_2026-08-30.tex           # 46 pages
```

Tectonic 0.15.0. Zero overfull boxes and zero undefined references is the
accepted state. `make_coverage.py` regenerates the coverage appendix of every
edition that prints one, and must run before the build: the appendix is what
makes the coverage claim auditable, and a stale one describes a paper that no
longer exists.

The 28 August edition builds the older way, and its pinned digest depends on it:

```bash
SOURCE_DATE_EPOCH=1756339200 FORCE_SOURCE_DATE=1 \
  pdflatex -interaction=nonstopmode master_paper_2026-08-28.tex   # x3
```

Three passes for the cross-references. `SOURCE_DATE_EPOCH` is what makes the
digest in `SHA256SUMS` reproducible — without it `pdflatex` stamps the build
time into the PDF and the pin fails on a rebuild that changed nothing. Needs
`texlive-latex-base` and `texlive-latex-recommended` (for `booktabs`); that
build is 7 pages.

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

This list is against the **two pinned originals**, which are immutable evidence
and stay as they are. The united edition is ours to write, so it carries six of
these corrected: eq. (18)'s isotropy is now proved (§4, Thm 4); Theorem 3's
missing clause is stated as the vacuum route (§4, Prop 2); the `L >= 3` caveat
is confined to the Bloch adjacency (§3, remark); the `u^1` row is labelled
`SU(3)`-only (App. C); the lifter census is given as three classes over 32
patterns each, 96 in total, with "nothing here checks any of them" said out
loud (§1, item 5); and the sheets are called cycles, never harmonic (§3).
Lemma 4's imprecise "unmatched" is moot there — the lemma is gone, replaced by
the Weingarten proof that made it unnecessary. The remaining items below are
open against the united edition too.

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

Standard library only, no arguments, no floats, about ten seconds — nearly
all of it the exact `Fraction` elimination of the L = 4 and L = 5 torus
boundary maps, which the finite-volume checks now cover through L = 5. It
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
