# Review — Global O(y⁴) band-edge certificate (+ curvature audit)

**2026-06-13.** Independent review of the uploaded `y4_global_band_edge_certificate_final.py` /
`CERT_Y4_global_band_edge_certificate.md` / `AUDIT_Y4_curvature.log`. Grounds: **[V]** verified here.

## Verdict: SOUND, and a genuine strengthening. [V]

The certificate **rigorously proves** that `c4(k)` attains its global minimum at Γ and global maximum at
R over the whole Brillouin zone — upgrading my earlier grid-scan ("≈0.48, min near Γ") to an exact,
**proved global bandwidth**:

> **ΔW₄ = c4(R) − c4(Γ) = 132329431693349 / 275331901291200 ≈ 0.4806186** (global, exact).

### Method (sound)
- Division-free reduction: since `D(k)=‖ψ(k)‖² ≥ 0`, `c4 ≥ c4(Γ) ⇔ Qmin = N − c4(Γ)D ≥ 0` (and dually for R).
  Both `Q` are exact trigonometric polynomials — no division near Γ.
- Reduction to `[0,π]³` justified by reflection + permutation symmetry of `N,D`.
- Zero-neighborhoods (Γ for both, R for the max) handled by **exact rational Taylor lower bounds**
  (positive quartic/quadratic minus a bounded remainder, valid in an explicit ball).
- The rest by **interval branch-and-bound** (rigorous mpmath interval arithmetic).

### What I verified independently [V]
1. **Reproduced the proof** on my own copy of the kernel: `PROVED`, **0 unresolved boxes**
   (min: 1590 boxes, max: 76), bandwidth as above.
2. **The load-bearing symmetry reduction is real:** I rebuilt `N` (25 terms) and `D` (7 terms) myself and
   confirmed both are invariant under all **8 reflections** and **6 coordinate permutations** ⇒ `[0,π]³` is
   a valid fundamental domain. (Without this the "global" claim would only cover 1/8 of the BZ; it holds.)
3. **Curvatures match exactly** (next section).

The interval-arithmetic core is rigorous; I did not re-implement it, I re-ran it and independently checked
its two assumptions (D ≥ 0 and the symmetry domain). No gaps found.

## The curvature audit corrects my synthesis. [V]

`AUDIT_Y4_curvature.log` reports the band-edge curvatures `d²c4/d|k|²`, which I independently reproduced to
the digit:

| point / direction | exact | decimal |
|---|---|---|
| Γ, [100] | `5/24` | 0.208333 |
| Γ, [110] | `247051057231349/2202655210329600` | 0.112161 |
| Γ, [111] | `132329431693349/1651991407747200` | 0.080103 |
| R (all dirs) | `−132329431693349/1651991407747200` = **−ΔW₄/6** | −0.080103 |

**Correction to `../lattice_glueball_data/NOTE_Y4_synthesis_band_vs_lattice.md`:** I had written the Γ band-bottom
curvature as "isotropic +0.104." That is **wrong**. The Γ minimum is **anisotropic (cubic warping)** — the
curvature runs from `5/24` along the cube axis down to `≈0.080` along the body diagonal, so **there is no
single effective mass at Γ**. (My "0.104" was half of `5/24`, computed from the [100] axis alone with an
incorrect isotropy assumption.) The **R** maximum *is* isotropic, exactly `−ΔW₄/6 ≈ −0.0801` (my earlier
`−0.036` was an inaccurate finite difference; the synthesis is corrected accordingly).

## Net
The uploaded certificate is correct, rigorous, and strengthens the result (global edges now proved, not
scanned). It also fixed a real mistake of mine (anisotropic Γ curvature). Both my reproduction and the
two independent assumption-checks are in `ENGINE_Y4_indep_cert_check.py`. The exact `−ΔW₄/6` R-curvature relation is
a clean bonus.
