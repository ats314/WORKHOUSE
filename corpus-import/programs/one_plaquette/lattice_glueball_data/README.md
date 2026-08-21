# Lattice glueball data relevant to the O(y⁴) C-odd flat-band work

**Curated 2026-06-13.** Reference lattice data for the SU(3) Kogut–Susskind strong-coupling
glueball program — specifically the C-odd `T1^{+-}` (= 1⁺⁻) state whose one-flux band the
O(y⁴) computation found to be flat through O(y³) and lifting at O(y⁴). Every number here is
either **verbatim** from the cited source or an explicitly-flagged **derived** quantity; no
values were guessed. Where a full table sat past the web-fetch limit, that is stated rather
than filled in.

## 1. Glueball masses (see `DATA_FLUX_glueball_masses.csv` / `.json`)

**Hamiltonian-limit Monte Carlo — same Kogut–Susskind formalism as our work** (arXiv:hep-lat/0503038, abstract, verbatim):

| state | cubic rep | mass |
|---|---|---|
| 0⁺⁺ (scalar) | A1⁺⁺ | **1654 ± 83 MeV** |
| 2⁺⁺ (tensor) | E⁺⁺/T2⁺⁺ | **2272 ± 115 MeV** |
| **1⁺⁻ (axial vector, C-odd)** | **T1⁺⁻** | **2940 ± 165 MeV** |

The 1⁺⁻ row is the physical glueball our flat-band band describes. `m(1⁺⁻)/√σ ≈ 2940/485 ≈ 6.06`.

**Continuum (Euclidean → a→0) anchor** (arXiv:2007.06422, Athenodorou–Teper, verbatim):

- `M(0⁺⁺)/√σ = 3.405(21)`
- scale: `r0 = 0.472(5) fm = 1/418(5) MeV`, `√σ = 1.160(6)/r0 = 485(6) MeV`
- ⇒ derived `M(0⁺⁺) = 3.405(21) × 485(6) = 1651(23) MeV`.

**Cross-check:** Hamiltonian-limit 0⁺⁺ = 1654(83) MeV vs AT continuum 1651(23) MeV — agree within
errors, which validates comparing our Hamiltonian strong-coupling result to the continuum spectrum.

**Full AT continuum spectrum by J^{PC}** — now retrieved verbatim from Tables 17 (M/√σ) and 18 (GeV)
of arXiv:2007.06422 (rendered in-browser; web-fetch had stripped the table bodies). Full 20-state
tower in `DATA_FLUX_at_continuum_spectrum.csv` and the `AT continuum (J^PC)` sheet of the workbook. The C-odd
sector our O(y⁴) work concerns:

| J^PC | level | M/√σ | M [GeV] |
|---|---|---|---|
| **1⁺⁻** | gs | 6.065(40) | **2.944(42)** |
| 1⁺⁻ | excited | 7.82(6) | 3.80(6) |
| 2⁺⁻ | gs | 8.74(12)* | 4.24(8)* |
| 3⁺⁻ | gs | 7.27(12) | 3.53(8) |
| 4⁺⁻ | gs | 9.02(10)** | 4.38(8)** |
| 1⁻⁻ | gs | 8.31(10) | 4.03(7) |
| 2⁻⁻ | gs | 8.08(15) | 3.92(9) |

`1⁺⁻ gs = 2.944(42) GeV` equals the Hamiltonian-limit `2940(165) MeV` — independent cross-validation
of both the value and the table's column mapping. Flags: `*` poor fit / hesitant spin, `**` speculative.
Cross-check: `M/√σ × 0.485 GeV` reproduces every GeV entry (e.g. 6.065×0.485 = 2.94).

## 2. Hamiltonian strong-coupling series (sources)

Directly comparable to our O(y⁴) expansion (the lightest glueball = minimal-plaquette flux loop;
the mass gap is its excitation energy, strictly positive in strong coupling):

- **Pavel, arXiv:1611.06542** — SU(3) YM Hamiltonian in the "flux-tube gauge"; systematic strong-coupling
  expansion in `λ ≡ g^{-2/3}` (= expansion in spatial derivatives); low-energy glueball spectrum.
- **arXiv:0912.5465** — expansion of the YM Hamiltonian in spatial derivatives and the glueball spectrum.
- Classic: Kogut–Susskind (1975); Münster strong-coupling series for glueball masses; Hamiltonian
  strong-coupling reviews (e.g. World Scientific *Lattice Gauge Theories: The Strong Coupling…*).

Note: exact series coefficients live inside these papers' bodies (not extractable cleanly via web
fetch); the arXiv IDs above are the retrieval pointers. **Our own O(y⁴) C-odd `T1^{+-}` result is itself
a new datum in this strong-coupling-series line** — flat through O(y³), first nonzero bandwidth at O(y⁴),
coefficient ≥ `17607806155349/275331901291200`.

## 3. Raw gauge configurations (access, not bundled)

Direct download isn't feasible from here (large binaries / accounts), so these are access pointers:

- **ILDG — International Lattice Data Grid:** https://hpc.desy.de/ildg/ (metadata catalogue + markup;
  SU(3) ensembles in ILDG format).
- **OpenLat (Open Lattice Initiative):** arXiv:2212.07314 — Nf=2+1 Stabilized-Wilson-Fermion ensembles,
  ILDG-compatible, public after each stage's publication, no embargo.
- Historical: MILC ensembles; the NERSC "Gauge Connection". For pure-SU(3) glueball spectroscopy these
  configs are not actually the relevant comparison — the *spectra* in §1 are.

## 4. Sources

- Athenodorou, Teper, *The glueball spectrum of SU(3) gauge theory in 3+1 dimensions*, JHEP 11(2020)172 — [arXiv:2007.06422](https://arxiv.org/abs/2007.06422)
- *Monte Carlo study of glueball masses in the Hamiltonian limit of SU(3) lattice gauge theory* — [arXiv:hep-lat/0503038](https://arxiv.org/abs/hep-lat/0503038)
- Pavel, *SU(3) Yang-Mills Hamiltonian in the flux-tube gauge…* — [arXiv:1611.06542](https://arxiv.org/abs/1611.06542)
- *Expansion of the Yang-Mills Hamiltonian in spatial derivatives and glueball spectrum* — [arXiv:0912.5465](https://arxiv.org/abs/0912.5465)
- ILDG portal — https://hpc.desy.de/ildg/ ; OpenLat — [arXiv:2212.07314](https://arxiv.org/abs/2212.07314)
