# Synthesis — the O(y⁴) C-odd 1⁺⁻ glueball band meets the lattice spectrum

**2026-06-13.** Combining the *verified* O(y⁴) result (`y4_o3_flatband_verification/`) with the curated
lattice glueball data (`lattice_glueball_data/`). Every claim is tagged by its grounds:
**[V]** = derived-and-machine-verified, **[D]** = derived here (exact, re-runnable), **[H]** = heuristic,
**[C]** = conjecture. No continuum / all-orders / mass-gap claim is made.

## 0. The two inputs

- **[V]** Strong-coupling Hamiltonian series for the C-odd one-flux (1⁺⁻ = T1⁺⁻) branch:
  `m₋(k,y)·a = 8/3 + y + (11/306)y² − (109151/249696)y³ + y⁴·c₄(k) + O(y⁵)`,
  flat through O(y³); the O(y⁴) term `c₄(k)` comes from the Hermitian 189-entry kernel (verdict: **LIFT**).
- **[V/data]** Lattice 1⁺⁻ glueball mass: **2.944(42) GeV** (continuum, Athenodorou–Teper) ≡ **2940(165) MeV**
  (Kogut–Susskind Hamiltonian limit). The two agree — an independent cross-check of the state's identity.

## 1. New ground — the *exact full* band structure (beyond the verification)

The verification proved the lift with a **lower bound**: the parity witness `c₄(R)−c₄(X) = 17607806155349/275331901291200 ≈ 0.06395`. Mapping the whole Brillouin zone gives the complete picture:

| point | k | c₄ (exact) | ≈ |
|---|---|---|---|
| Γ (band **min**) | (0,0,0) | −20721577909065127111 / 7250590288602460800 | −2.857916 |
| X | (π,0,0) | −17700498622147435111 / 7250590288602460800 | −2.441249 |
| M | (π,π,0) | −4367164159624988707 / 1812647572150615200 | −2.409274 |
| R (band **max**) | (π,π,π) | −3447362930970494909 / 1450118057720492160 | −2.377298 |

- **[D] Exact O(y⁴) bandwidth** `ΔW₄ = c₄(R) − c₄(Γ) = 132329431693349 / 275331901291200 ≈ 0.48062`.
  This is **~7.5× the parity witness** — the witness only spanned X→R; the band actually reaches down to Γ.
- **[D]** At Γ the three coordinate planes are degenerate: `H₄(0) = c₄(Γ)·I` (the off-diagonal real-space
  blocks sum to zero). So the Γ "singularity" of the flat eigenvector is **removable** — c₄ has a clean,
  direction-independent minimum at zero momentum.
- **[D] Band-edge curvatures `d²c4/d|k|²` (corrected 2026-06-13, see `../y4_o3_flatband_verification/AUDIT_Y4_review_global_band_edge_certificate.md`):**
  the Γ minimum is **anisotropic** (cubic warping) — `5/24 ≈ 0.208` along [100], `≈0.112` along [110],
  `≈0.080` along [111] — so there is **no single effective mass at Γ**. The R maximum **is** isotropic,
  exactly `−132329431693349/1651991407747200 = −ΔW₄/6 ≈ −0.0801`. (An earlier draft wrongly called Γ
  isotropic `+0.104`; that was the [100]-only half-value.)
- Band shape (see `DATA_Y4_1pm_band_structure.png`): rises Γ→(local max near X), dips at M, up to R, back to Γ.

## 2. Mobility suppression (what the band *means*)

- **[D]** The 1⁺⁻ glueball's lattice **mobility first appears at O(y⁴)**. Its fractional dispersion is
  `ΔW₄·y⁴ / m₋(y) = 0.48062·y⁴ / (8/3 + y + …) ≈ 0.180·y⁴` (leading). At y = 0.5 that is ≈ 1.1%; at y = 1, ≈ 13%.
  The state is **nearly dispersionless** at strong coupling — an emergent low-mobility ("heavy-on-the-lattice")
  excitation.
- **[V]** Mechanism: the cube-boundary state is annihilated by H₄ up to a residual that leaks onto exactly
  6 plaquettes with weight **5/48** (closed-surface protection failing at 4th order). The dispersion is the
  Fourier transform of that small leakage — hence parametrically small.
- **[H]** The flatness through O(y³) is at least partly kinematic (translating a cube-surface state needs
  ~4 plaquette insertions); the *dynamical* new content is the near-total O(y⁴) cancellation that leaves only
  the 5/48 edge term. Disentangling kinematic vs dynamical suppression is a clean follow-up **[C]**.

## 3. A falsifiable prediction for strong-coupling Hamiltonian lattice gauge theory

A dedicated measurement of the 1⁺⁻ one-flux band at strong coupling (small y, Kogut–Susskind Hamiltonian,
e.g. tensor-network / exact-diagonalization on a 3D spatial lattice) should find, with **no free parameters**:

1. band **minimum at zero momentum (Γ)**, **maximum at the BZ corner R = (π,π,π)**;
2. the branch **flat through O(y³)**, first dispersing at **O(y⁴)**;
3. total bandwidth **`0.48062·y⁴`** (lattice units), i.e. fractional bandwidth **`≈ 0.180·y⁴`**;
4. band **anisotropic at Γ** (curvature `d²c4/d|k|²` runs `5/24` along [100] to `≈0.080` along [111]) and
   **isotropic at R** with curvature `−ΔW₄/6 ≈ −0.0801`; the global bandwidth `ΔW₄ = 0.4806…` is now *proved*;
5. the full intermediate shape of `DATA_Y4_1pm_band_structure.png` (X and M are interior points, not extrema).

Any deviation falsifies the O(y⁴) des-Cloizeaux kernel; agreement is a stringent, momentum-resolved test
that goes well beyond a single mass.

## 4. Honest boundary

- **[H, important]** The strong-coupling series is **asymptotic**; it is *not* a route to the continuum
  2.944 GeV (that lives at the opposite, weak-coupling end). The lattice number anchors *which* physical state
  this is and cross-validates the Hamiltonian-limit value — it does **not** get predicted by the y-series.
- Mass-ratio context **[D/H]**: lattice `m(1⁺⁻)/m(0⁺⁺) = 2.944/1.653 = 1.78`; in strong coupling both branches
  start at 8/3 (ratio → 1), so the physical splitting is a scaling-region effect, outside this expansion.
- Everything in §1 is exact and re-runnable (`band.py`/`edges.py` patterns over the verified kernel);
  §2–§3 are physics built on it; §4 marks where rigor stops.

## Sources
- O(y⁴) verification + kernel: `../y4_o3_flatband_verification/` (verdict LIFT, kernel SHA-256 635d40…).
- Lattice masses: arXiv:2007.06422 (Athenodorou–Teper, Tables 17/18); arXiv:hep-lat/0503038 (Hamiltonian limit).
