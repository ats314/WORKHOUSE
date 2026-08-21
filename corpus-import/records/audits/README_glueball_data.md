# Lattice glueball data for the T1(+-) / 1(+-) flat-band program

**Compiled:** 2026-06-13 (lead math agent). **Purpose:** replace the topological-susceptibility
table (`lattice_qcd_data_suN.csv`, which has only the 0++ scalar) with lattice data that actually
contains the channel our work is about — the **lightest C-odd glueball, J^{PC}=1^{+-}** (lattice
T1^{+-}).

## Files
- `DATA_FLUX_glueball_spectrum_lattice_1pm_relevant.csv` — continuum SU(3) glueball spectrum, full J^{PC},
  from **Morningstar & Peardon 1999** (arXiv:hep-lat/9901004, Table VII), with the 1^{+-} row
  flagged. Includes r0·m, mass in MeV, a derived m/√σ, ratios to the 0++, and continuum spin J.
- `lattice_qcd_data_suN.csv` (already in the project) — the SU(N) 0++ mass and topological
  susceptibility vs N; this is the **Athenodorou–Teper SU(N)** data (arXiv:2106.00364). Keep it
  for the large-N context; its `mass_ratio_0pp` for N=3 is 3.405(21), the AT continuum 0++/√σ.

## The one number that matters for our work
The paper's object is the **lowest one-flux C-odd band in the T1^{+-} representation**. In the
real (continuum) glueball spectrum, the lightest C-odd state *is* the 1^{+-}:

> **m(1^{+-}) = 2940(30)(140) MeV,  r0·m = 7.18(4)(7)**  (Morningstar–Peardon 1999)
> ≈ 2989(30)(140) MeV in the alternative scale convention used by some reviews.

So the channel is real, well-measured, and sits where our work places it: it is the **lightest
glueball with C = −**, well above the C = + ground states.

## Ordering (real spectrum), and how it compares to the paper
0++ < 2++ < 0−+ < 0*++ < **1+−** < 2−+ < 3+− < …

The paper's stated "0++ < 2++ < 1+−" is correct but incomplete: the 0−+ (and the excited 0*++)
sit between the 2++ and the 1+−. The robust, scale-independent facts the lattice supports are:
- the 1+− is the **lightest C-odd** glueball (ratio m(1+−)/m(0++) = 7.18/4.21 = **1.71**);
- it is heavier than the 0++, 2++, and 0−+.

## HONEST SCOPE — read before quoting any of this as a "prediction"
This data is **continuum** lattice Yang–Mills. The paper's flat band is an **exact strong-coupling
(small-β) lattice** statement that the paper itself shows **breaks at O(y⁴)**. The two are connected
only by quantum numbers, not by a quantitative mass relation:
- The strong-coupling series `m_-(k,y) = 8/3 + y + (11/306)y² − (109151/249696)y³ + …` is a
  lattice-scale energy in the strong-coupling regime; it is **not** converged at the coupling where
  these continuum masses live, and it does not predict 2940 MeV or m/√σ.
- What the work *does* connect to the real world is **qualitative/structural**: the existence and
  lattice quantum numbers of a 1+− (lightest C-odd) glueball, and the ordering above. That is a
  legitimate real-world-facing statement; a continuum mass from 3 strong-coupling terms is not.
- Do not convert the strong-coupling band energy into GeV. The defensible comparison is the
  **quantum-number assignment** and, at most, the **ordering** — both of which the lattice confirms.

## Provenance / scale conventions
- **MP1999** (arXiv:hep-lat/9901004): anisotropic, quenched SU(3); r0^{-1} = 410(20) MeV; the two
  uncertainties are (continuum-extrapolation, anisotropy) and the MeV column adds the r0^{-1} scale
  error. In the CSV the per-row uncertainty is the quadrature combination; originals are in the paper.
- **AT2020** SU(3) (arXiv:2007.06422) and **AT2021** SU(N) (arXiv:2106.00364): finer lattices, masses
  in m/√σ. Continuum 0++/√σ = 3.405(21). Full per-channel √σ tables (incl. 1+−) are in those papers
  (Sec. 5.5–5.6); only the 0++ anchor is filled in the CSV's `m_over_sqrtsigma_AT` column.
- `m_over_sqrtsigma_derived` converts MP's r0·m with r0√σ = 1.19 (Necco–Sommer / Lucini–Teper); it is
  flagged DERIVED and differs from AT at the ~4% level (different actions/lattices), as expected.

## Next layer (not yet pulled — offer)
The **SU(N) dependence of the 1+−** (m(1+−)/√σ for N = 2…12 and N=∞) lives in arXiv:2106.00364,
Sec. 5.5–5.6 tables. That is the dataset most relevant to the paper's **SU(N) generalization** and
would let you test the 1+− large-N trend directly. Say the word and I'll extract that table too.
