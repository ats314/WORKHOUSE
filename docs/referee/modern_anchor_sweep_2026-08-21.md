# The 2020–2026 anchor sweep

**Date:** 2026-08-21.
**Charge:** find the strongest papers from 2020–present related to this
program, work backwards from them, and see where they meet the citation web —
"if newer papers are still citing the same work we are, that's a sign, but if
citations are on a new level now, we need to catch up."

This document records the method, the measurement, and the verdict, so the
conclusion "the roots are current" is checkable rather than asserted.

## Method

Sixteen INSPIRE-HEP queries, retrieved 2026-08-21 (all re-runnable from the
descriptions below; the anchors' recids are in `literature/index.yaml`):

- **Nine citer queries** — `refersto:recid:<anchor> and de 2020->2026`, most
  cited first, over the web's anchors (KS_1975, KSS_1976, MUNSTER_1981,
  HIP_1986, HAMER_1989, SCHIERHOLZ_1988, MP_1999, CS_2006, KRS_2023).
- **Seven topic queries** — glueball spectrum, SU(N) glueballs, Hamiltonian
  lattice gauge theory, strong coupling, tensor-network LGT, quantum
  simulation of LGT, Teper glueball.

125 hits, 116 distinct papers. Ranking was by *relevance to indexed claims*,
not raw citation count — the raw top of the pool is the Review of Particle
Physics, which bears on nothing here. Candidates' own INSPIRE reference lists
were then intersected against the 34 recids of the citation web: a modern
paper "meets the web" where its references land in it.

## The four winners

| id | paper | INSPIRE cites | meets the web at |
|---|---|---|---|
| `CKS_2021` | Ciavarella–Klco–Savage, PRD 103, 094501 — SU(3) Yang–Mills in the local multiplet basis, run on IBM hardware | 285 | KS_1975, WILSON_1974 |
| `AT_2020_SU3` | Athenodorou–Teper, JHEP 11 (2020) 172 — the SU(3) continuum glueball spectrum | 184 | MP_1999, MT_1989 |
| `DRS_2021` | Davoudi–Raychowdhury–Shaw, PRD 104, 074505 — formulation cost comparison for Hamiltonian simulation | 163 | KS_1975, WILSON_1974 |
| `AT_2021_SUN` | Athenodorou–Teper, JHEP 12 (2021) 082 — glueball spectra, string tensions and topology for SU(N), N = 2..12 | 115 | MP_1999, MT_1989 |

All four were read in full (reading agents over the actual PDFs), every number
quoted in their index entries was verified against the pinned copy, and all
four are indexed with INSPIRE-verified metadata. Three are stored under
redistribution-permitting licences — `AT_2021_SUN` and `CKS_2021` are CC BY
4.0 on arXiv itself, `AT_2020_SU3`'s published JHEP PDF is CC BY 4.0 — which
triples the stored-fulltext count (previously KRS_2023 alone qualified).
`DRS_2021` (arXiv nonexclusive licence) is pinned, not stored.

## The verdict: the roots are current

The user's question had two possible answers, and the measurement gives the
first one cleanly:

**The moderns still stand on exactly the papers this web pins.** The 2020s
literature relevant to this program splits into two branches, and each
branch's reference lists meet the web at its oldest anchors:

- The **continuum spectroscopy branch** (Athenodorou–Teper) anchors on
  MP_1999 (its explicit comparison standard, ref [4] of AT_2020) and MT_1989
  — the same two Euclidean spectra this index already carried for G18.
- The **quantum-simulation branch** (CKS_2021, DRS_2021, and KRS_2023 already
  indexed) anchors on KS_1975 and WILSON_1974 directly — the same two
  foundations at the root of this web's tree. The sole 2020s citer of
  HIP_1986 in the sweep window is the 2023 spin-network algorithms paper
  (INSPIRE 2649260), also from this branch.

No new-level replacement anchor exists: nothing in the 116-candidate pool
supersedes the web's roots, and the sweep found no post-2020 paper this
program should be anchored on that it was not already connected to within one
edge. Catch-up was needed at the *leaves*, not the roots — which is what the
four entries are.

## The bibliographic split, and why it matters here

The sharpest structural fact the sweep measured: **the modern Euclidean
spectroscopy line cites zero Hamiltonian strong-coupling work.** AT_2020 and
AT_2021 have, between them, no reference to KS_1975, KSS_1976, HIP_1986,
HAMER_1989, or any series paper. Meanwhile the quantum-simulation line cites
KS_1975 as its formulation but *none of the 1976–89 series program* — CKS_2021
has no strong-coupling series expansion anywhere in it (its coupling g is a
plot parameter), and its 140 references contain no series literature.

Consequences recorded:

1. **The Hamiltonian strong-coupling series corpus has no modern
   recomputation.** Nobody in the 2020s pool re-derives, extends, or checks
   the KSS/Hamer/HIP series this repository certifies. Its certified exact
   values (D_3, m_Gamma^(4), the sigma series) are, as far as this sweep can
   see, the only machine-checked form of that program's results anywhere.
   The 2020s strong-coupling remnant is Euclidean and thermodynamic (the
   Philipsen school, INSPIRE 1856750), not Hamiltonian-spectral.
2. **The two modern branches do not cite each other's foundations** — the
   spectroscopy branch never mentions the Hamiltonian, the simulation branch
   never compares against the continuum spectrum. The citation web now holds
   both branches *and* the 1975–89 trunk they forked from, which is a view
   neither branch's own bibliography provides.
3. **The quantum-simulation line is heading back toward exactly the regime
   this program certifies.** CKS_2021's truncation analysis shows the
   electric (strong-coupling) basis converging fastest at large g, and its
   initial states are the electric vacua whose perturbations the certified
   series coefficients describe. If any modern line eventually needs the
   Hamiltonian strong-coupling series, it is this one.

## What entered the index

- Four paper entries (`AT_2020_SU3`, `CKS_2021`, `DRS_2021`, `AT_2021_SUN`),
  every quoted number verified against the pinned copy.
- Twelve new citation edges from primary sources, including the mutual
  CKS_2021 ↔ DRS_2021 edge (concurrent preprints) and a retro-edge
  KRS_2023 → DRS_2021 confirmed in KRS's INSPIRE reference list.
- The wanted slot "a modern continuum SU(N) glueball spectrum at several N"
  is **filled** by AT_2021_SUN — the second wanted entry ever discharged
  (KPS_1981 was the first).
- A scope firewall on DRS_2021 (1+1D, SU(2), with matter), same rule as
  KRS_2023: comparison, never input.

## Scope and negatives

- The sweep window is 2020-01 → 2026-08 and the pool is INSPIRE; a paper
  outside INSPIRE's coverage (pure math, quant-ph without hep cross-list)
  can be missed. The Catalan/Weingarten adjudication line (OBZ, Collins–
  Sniady) was not re-swept here; its modern condition is recorded in
  docs/referee/novelty_search_2026-08-21.md.
- `citers:HAMER_1989 and de 2020->2026` returns **zero** papers, and
  `citers:SCHIERHOLZ_1988` likewise: the two tables this program's strongest
  external agreements rest on are uncited in the 2020s. That is the
  bibliographic-split point in its starkest form.
- Nothing in this document promotes anything. Every new edge is
  `supplies-comparison`; the Euclidean/hardware numbers quoted in the
  entries are targets and context, and none enters a Hamiltonian claim.
