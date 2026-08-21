# UNIFY PROOFS — Curated Extracts (Markdown + LaTeX)

This folder contains a **curated, cleaned-up extraction** of the most promising mathematical/physical ideas found in the project notes.

The underlying project has two distinct layers:

1. **Proven / standard-derivation layer (finite cutoff):**  
   At fixed lattice spacing \(a>0\), one can obtain **uniform convexity windows** (at strong enough bare coupling) for the *effective action* and hence a **spectral gap** for the associated Langevin generator via Bakry–Émery/Poincaré machinery.

2. **Speculative / “new theory” layer (continuum mechanism candidates):**  
   The finite-cutoff convexity mechanism cannot survive the \(a\to 0\) continuum scaling *by itself*. The notes propose candidate “sparks” that could replace it, notably:
   - **entropic convexity** induced by Gribov/FMR hard-wall geometry in gauge-fixed configuration space,
   - **anomaly/geometry source terms** stabilizing convexity in a Riccati-type Hessian flow,
   - an **information-theoretic** rephrasing of UV control as (poly)logarithmic Log–Sobolev constants (“log-forest” idea).

## File map

1. `01_block_convexity_engine.md`  
   The reusable abstract engine: convexity \(\Rightarrow\) functional inequalities \(\Rightarrow\) spectral gap, plus block-RG convexity stability bounds.

2. `02_finite_cutoff_gap_lattice_YM.md`  
   The strongest rigorous core: Haar Jacobian expansion (positive “mass” term), conservative Wilson Hessian bounds, finite-cutoff convexity windows, Bakry–Émery gap, and an RG-stable subwindow.

3. `03_sparks_compact_QED3_and_4D_YM.md`  
   “Spark” mechanisms: a verified spark in compact QED\(_3\) (Polyakov duality) and a conjectural spark in 4D YM from Gribov/FMR entropic effects.

4. `04_continuum_obstruction_and_stabilizers.md`  
   Why the finite-cutoff mechanism cannot naively survive the continuum limit, and what additional stabilizers would be needed (Riccati flow + curvature/anomaly/LSI ideas).

## Conventions (used consistently in these extracts)

- Lie algebra \(\mathfrak{su}(N)\): **skew-Hermitian** traceless matrices.  
- Inner product on each link tangent space:
  \[
  \langle X,Y\rangle = -\mathrm{Tr}(XY),
  \qquad \|X\|^2=-\mathrm{Tr}(X^2).
  \]
- Link coordinate near identity: \(U=\exp(X)\) with \(X=agA\in\mathfrak{su}(N)\).

Where the original notes disagree on constants (notably the Wilson Hessian constant), these extracts adopt **conservative** bounds and flag possible sharpenings.

