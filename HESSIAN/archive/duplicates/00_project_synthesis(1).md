# SIMULATION REVIEW — Extracted Proofs & High-Value Results

This folder collects the *highest signal* derivations/proofs found across the chat logs and project files (Dec 2025).  
The goal is to turn scattered simulation output into a small set of coherent, falsifiable mathematical statements.

## What made the cut

1. **SU(2) drift–Laplacian–gradient identity and its consequences.**  
   The simulations strongly support an Ito/Langevin-generator decomposition
   \[
     \mathcal L V \;=\; \Delta V \;-\;\langle \nabla S,\nabla V\rangle,
   \]
   together with an *exact* affine Laplacian law for the plaquette-defect observable
   \[
     \Delta B_{\rm avg} \;=\; 12 - 12\,B_{\rm avg}.
   \]
   Empirically, the constant \(12\) is *volume-stable* across \(L\in\{8,12,16\}\) and the drift certificate strengthens with \(\beta\).

2. **Viscous Hamilton–Jacobi curvature-flow Riccati law and the “Haar α-band”.**  
   In a PDE surrogate model, the minimal curvature \(\lambda(t)\) follows a Riccati decay
   \[
     \frac{d\lambda}{dt}\approx -\alpha\lambda^2
     \quad\Longrightarrow\quad
     \lambda(t)\approx \frac{1}{b+\alpha t},
   \]
   with measured \(\alpha\approx 0.00102\) for quadratic-only initial data and a striking clustering
   \(\alpha\in (7.8,8.0)\times 10^{-4}\) once Haar-like measure curvature is included.

3. **SU(3) convex core (volume-stable) from Hessian minimum-eigenvalue scans.**  
   A multi-volume scan (L=4,6,8) of the minimum Hessian eigenvalue of a 4D SU(3) Wilson action
   shows an apparently volume-stable “convex core” for sufficiently small field amplitude.

4. **SU(3) plaquette Hessian quantization at the identity.**  
   A corrected right-invariant, gauge-projected Hessian micro-test at the identity yields
   *exact plateaus* at \(8/3\) and (on larger micro-lattices) multiples of \(8/3\),
   consistent with an “overlap number” \(k\) of plaquettes touched by a mode.

## How to use these notes

Each document is self-contained and follows the same pattern:

- Definitions \(\to\) statement \(\to\) derivation/proof sketch \(\to\) numerical evidence \(\to\) next steps.

The pieces can be combined into a broader program: **build explicit Foster–Lyapunov / Bakry–Émery-style coercivity bounds for lattice gauge dynamics** that survive volume increase and strengthen with \(\beta\).  
That’s a plausible bridge from “local convexity” to “mixing/spectral gap style statements” (not a proof yet, but a tractable direction).

---

**Documents in this set**

- `01_su2_generator_laplacian_drift.md`
- `02_vhj_riccati_alpha_band.md`
- `03_su3_convexity_window.md`
- `04_su3_plaquette_hessian_quantization.md`
