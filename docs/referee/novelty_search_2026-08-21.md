# Negative search: the cell-completion coefficient family in the strong-coupling literature

**2026-08-21.** Scope record for §7.4 of `cellular_completion_family.md`,
which states: "Novelty unverified. We have not established that this family
is absent from the strong-coupling literature." This document is the search
that establishes what has now been checked, exactly, and with what result.
It is a **negative search with stated scope**, not a novelty proof: the
family may still exist in sources listed below as unobtained.

## The target

```
c_prim(r) = (-1)^(r-1) · 2^(r-1) · C(2r-2, r-1) / (N (N²-1)^(r-1))
```

signed counts `S_r = 6, −20, 70, −252`; tetrahedron `−8/(N(N²−1))`;
SU(3) instances `−1/3, 1/8, 1/3, −5/48, 35/384, −21/256` — in the role of
completing closed 2-surfaces of plaquettes with Haar merges and
Rayleigh–Schrödinger resolvents. A random occurrence of a matching fraction
is not a hit; the geometry and role must match.

## Sources read in full and found NOT to contain the family

Each was retrieved from arXiv on 2026-08-21, digest-pinned (SHA-256 of the
copy read), and read page by page for series tables, completion geometries,
and the family's values. Digests are in `literature/index.yaml` for the
indexed papers and printed here for the rest.

| Source | What it is | Result |
|---|---|---|
| SZH_1997 (hep-lat/9603026) | coupled-cluster formalism, cites Hamer 1989 | no series coefficients at all; formalism only |
| HSB_2000 (hep-lat/0005009) | GFMC SU(3) 3+1D | no mass gaps computed, no series; comparison standard is HIP_1986's ELCE |
| MP_1999 (hep-lat/9901004v2) | anisotropic Euclidean spectrum | no strong-coupling expansion performed |
| LLL_2006 (hep-lat/0503038) | Hamiltonian-limit MC, cites Hamer 1989 | plots Hamer's β_H^7 series, reprints HIP ELCE tensions; no independent coefficients |
| CM_2003 (hep-lat/0303022) | variational SU(N) on a single cube | **nearest miss on record** — see below |
| MICHAEL_1992 (hep-lat/9209014, sha256 ebfc809ba743ed157b957811f9dd0a273a0160834fd1806a47fb541fe2e6e868) | review | qualitative only; no tables |
| KPS_1981 preprint (KEK scan 80-10-101, sha256 ffb45afde017a1f020e98adb8567a71cfe950f8a05406a4823a4a1717b521cab) | Hamiltonian SU(3) string tension, exact Table 2 | no completion coefficients; instead the exact tables that now validate SIGMA_2..SIGMA_5 |
| SMIT_1982 preprint ITFA-82-3 (KEK scan 82-08-005, sha256 4df455d689a9ce8d06dc3f0453285570547887eddcd0555248e5d6d369164c51) | Euclidean glueball series estimates | family absent; its Table 1 is the errata-resolved Münster–Seo 8th-order SU(3) series, the only open copy of the corrected Euclidean coefficients |
| SEO_UKAWA_1982 preprint EFI-82-05 (KEK scan 82-06-009) | off-axis plaquette-correlation formalism | family absent; cube-chain self-energy graphs, the Euclidean precedent for off-axis glueball series |
| Münster DESY 83-109 talk (KEK scan 83-12-084) | Münster's own review of his mass-gap expansions | inspected during the search; no family occurrence found |
| Nakayama UT-382 (KEK scan 82-06-116; = PRD 28, 922) | off-axis glueball masses, Euclidean | inspected during the search; no family occurrence found |

**The CM_2003 near-miss.** Its Eq. (14) is the single-cube link-to-plaquette
Jacobian `Σ_r (1/d_r⁴) Π_{i=1..6} χ_r(P_i)` — the six-plaquette closed-cube
character merge, i.e. exactly the geometry of the cube row `−5/48`, with the
`d_r^{2−6}` Haar weight. The paper never expands this object into
strong-coupling rationals: no `−5/48`, no `−8/(N(N²−1))`, no central-binomial
counts. The rationals it does contain (overlap-counting coefficients in
Eqs. (42)/(44); cycle-index fractions in the SU(6)–SU(8) Mandelstam
constraints, including an unrelated `1/48`) are all accounted for and none is
a completion coefficient. This is the closest published object to the
brief's Theorem 2 geometry found so far — the geometry without the
coefficients.

## Sources identified as the priority targets, not yet obtainable here

INSPIRE metadata verified 2026-08-21; every retrieval attempt through this
environment's proxy hit Elsevier's bot-block (HTTP 403), and the ScienceDirect
open archive serves these free to a browser. **A maintainer-supplied PDF of
any of these is directly useful** — the Hamer 1989 pass proved that works.

1. **Munster, Nucl. Phys. B190 (1981) 439** (recid 164289; preprint
   BUTP-2/81 Bern, no KEK scan) — the canonical Euclidean strong-coupling
   mass-gap expansion. Its diagrams are tubes of plaquettes capped into
   closed surfaces with character/Haar weights. *Update, later on
   2026-08-21: both errata were maintainer-supplied and read* — the
   erratum-and-addendum NPB 200 (1982) 536 (two overlooked graphs, SU(3)
   correction `12(3−2ε)u⁷ − 18(75−74ε)u⁸`) and the definitive second
   erratum NPB 205 (1982) 648 ("Murphy's sixth law"; thanks Ukawa and Seo),
   whose final table for every gauge group is now registered
   (`MUNSTER_ERR_MS`) and proved identical to Smit's open reprint in the
   published-comparisons suite. **Family check on the final corrected
   coefficients of all three channels: ABSENT** — SU(3) denominators are
   `2ᵃ·5ᵇ` and `2ᵃ·7ᵇ` forms (10240, 71680, 40960, 1280, 448), not
   `(N²−1)` powers, and no central binomials appear; the SU(∞) row
   (`−34, −164, −546`) is integer. What remains unread, and the only place
   the family could still hide in this line: NPB 190's per-diagram weights
   (Tables 1–2 internals, before summation).
2. **Seo, Nucl. Phys. B209 (1982) 200** (recid 184480, 28 citations;
   preprint EFI-82-10, no KEK scan recorded) — extends and cross-checks
   Munster's series, off-axis included; tabulates cluster-by-cluster
   contributions where cube- and prism-shaped plaquette clusters appear
   with explicit rational SU(3) weights. The most likely single table to
   contain `−5/48`-type entries per geometric cluster. Now indexed as
   `SEO_1982` with a `supplies-comparison → G5` edge saying exactly this.
3. **Kogut–Sinclair–Susskind, Nucl. Phys. B114 (1976) 199** (recid 3785;
   preprint CLNS-336, no KEK scan) — the founding Hamiltonian resolvent
   computation; the structure that would generate central-binomial
   intermediate-state counts.
4. **Hamer–Irving–Preece, Nucl. Phys. B270 (1986) 553** and
   **Irving–Hamer, Nucl. Phys. B230 (1984) 361** — the ELCE line; the linked
   subtraction G3's protocol names.
5. **Munster, Nucl. Phys. B180 (1981) 23** (DESY 80/44, recid 153653) —
   the cluster-machinery paper behind the mass-gap expansion, still unread.
   *(Its 1985 sibling NPB 256 (1985) 67 — the effective transfer matrix on
   the degenerate glueball eigenspace — was maintainer-supplied later on
   2026-08-21 and read in full: the completion family is ABSENT from its
   per-order effective-matrix pieces too (integer combinations of the
   momentum matrices A, B; 2ᵃ·5ᵇ scalar denominators), and its Table 1
   produced a bonus FINDING — it shifts the 1982 erratum's eighth orders by
   exact amounts (−96 for SU(3)) that no further erratum records. See
   `MUNSTER_1985_TM` in the index and the FINDING check in the published
   suite.)*

(Smit NPB 206 (1982) 309 stood on this list until its KEK preprint scan was
found, read, and recorded as clean — see the table above.)

## The closest published relative: O'Brien–Zuber 1985

The search's substantive find is not a prior source but the **occupied
role-space** any novelty claim must argue against. O'Brien–Zuber,
*Strong coupling expansion of large-N QCD and surfaces*, Nucl. Phys. B253
(1985) 621 (read here from the author's open self-archive, sha256
`972fdb855e5bc9555203d8c241a88414620f5e3238136ee2b44818b76d49a592`; now
indexed as `OBZ_1985` with a `supplies-comparison → G5` edge):

- Its eq. (2.5) attaches **signed central binomials** `(2k)!/(k!)²` as
  one-link cumulant weights to the cyclic contractions (Kazakov's saddles,
  PLB 128B (1983) 316) that sew closed plaquette surfaces in the large-N
  Euclidean free-energy expansion — with cube-based worked examples.
- The companion note (PLB 144B (1984) 407, also read, sha256
  `a8305b5ca46ea63f7df726eae2cbf97f1a6d238a9a4e17eb2d005f0ade6006ee`)
  derives those weights from an **inverse square root** of the one-link
  integral — the same mechanism class that generates a central-binomial
  series.
- The bridge, now a T1 check in the published-comparisons suite:
  `C(2n−2, n−1) = n·Cat(n−1)`, so the family's signed counts
  `S_n = 6, −20, 70, −252` are exactly **n times** the Catalan-class
  cyclic-contraction weights.

What the family has that O'Brien–Zuber does not, verified against the
primary: finite-N pure-power denominators `(N²−1)^(r−1)` (Drouffe–Zuber
Phys. Rep. 102 (1983), appendix (A.26), gives the finite-N coefficients
with *product* denominators `(N²−1)(N²−4)…`, and its closed-orientable
surface weights carry no such denominators at all), the `2^(r−1)` factor,
the prism-cap sector structure, and Rayleigh–Schrödinger resolvents —
theirs is Euclidean free energy at `N → ∞`, not Hamiltonian degenerate
perturbation theory. **The open adjudication: whether the finite-N
completion coefficients are derivable from these cumulant weights.** A
derivation would make the family a repackaging and strengthen the anchor
table; none is known, and nothing here decides it.

Modern relatives checked and clean (all retrieved and grepped):
Langelage–Münster–Philipsen JHEP 07 (2008) 036 (capped-tube mechanism
present, family fractions absent); Borga–Cao–Shogren-Knaak arXiv:2411.11676
and Lemoine arXiv:2606.28945 (signed *Catalan*, not central-binomial,
surface weights at large N); Chatterjee/Jafarov/Basu–Ganguly/Unger
master-loop and one-link Catalan structures.

## What was searched beyond full-text reading

- **INSPIRE-HEP API** (2026-08-21): author/title metadata queries across the
  Hamiltonian and Euclidean series lines — exact queries logged by the
  search run: Munster, Seo, Irving–Hamer, Kogut–Sinclair–Susskind,
  Kogut–Pearson–Shigemitsu, Kogut–Shigemitsu, Drouffe–Zuber,
  Balian–Drouffe–Itzykson, Banks–Sinclair, Smit, Hollenberg,
  Langelage, Falcioni–Marinari–Parisi — plus INSPIRE fulltext queries for
  the family's fractions ("35/384", "21/256", "5/48" with strong-coupling
  qualifiers; caveat: INSPIRE fulltext coverage is mainly arXiv-era, so the
  1974–1990 target literature is largely outside it, and phrase queries
  tokenize). Every openly retrievable candidate PDF was downloaded and
  grepped (~20 sources, including the Churcher–Moreau intermediate-coupling
  thesis, whose "5/48" fulltext hit proved a tokenization artifact).
- **Web, Exa, and arXiv search** for the family's SU(3) values and for
  central-binomial/Catalan structures in strong-coupling lattice contexts
  (queries logged in the run; arXiv all-fields `"central binomial" "lattice
  gauge"` returns zero results).
- **Open library scans** (KEK KISS, CERN CDS) for preprint copies of the
  unobtained targets; KEK KISS rejected automated queries during the run
  (503), so the scan route remains unexhausted.

## Outcome

**No prior source for the family has been found; the search is bounded by
the unobtained primary sources above (Munster ×3, Seo, KSS, HIP–IH) plus
Kazakov 1983 and Balian–Drouffe–Itzykson PRD 11 (1975) 2104.** Absence is
established for: everything on arXiv that cites Hamer 1989 (all four such
papers read in full), the eleven read sources in the table — including the
KEK preprint scans of Kogut–Pearson–Shigemitsu, Smit, and Seo–Ukawa — the
O'Brien–Zuber pair and Drouffe–Zuber review, the modern large-N surface-sum
literature (grepped), and the metadata/abstract layer of the candidate
lines. It is NOT established for Munster/Seo/KSS/HIP–IH, whose tables are
exactly where a 1980s series expansion would put such coefficients — Seo
NPB 209 (1982) 200 tabulates cluster-by-cluster contributions for cube- and
prism-shaped plaquette clusters and is the single most likely table. Per
§7.4 of the brief, a prior source would *strengthen* the anchor table —
finding one is a win, so obtaining those papers is the live continuation of
this search, and `workhouse lit` already ranks them among the top
acquisition targets on citation-web grounds alone.

A side payoff of the scan hunt dwarfed the search itself: the KPS scan's
exact Table 2 validates the certified `SIGMA_2..SIGMA_5` rational for
rational — see the KPS checks in the published-comparisons suite and the
`KPS_1981` entry in `literature/index.yaml`.
