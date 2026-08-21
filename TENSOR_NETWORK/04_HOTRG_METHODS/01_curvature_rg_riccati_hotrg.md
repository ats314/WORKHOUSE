# Curvature → RG → Riccati Stabilization (with HOTRG evidence)

## Executive summary

This note extracts a **research-program skeleton** that appears repeatedly in the project files:

1. **Curvature seed:** group geometry (and/or Haar measure) contributes a positive “mass-like” curvature term.
2. **Curvature transport:** under a viscous Hamilton–Jacobi (vHJ)–type flow, the *minimal curvature* appears to follow a Riccati law
   \[
   \frac{d\lambda}{dt} \approx -\alpha \lambda^2
   \quad\Longrightarrow\quad
   \frac{1}{\lambda(t)} \approx \frac{1}{\lambda(0)} + \alpha t .
   \]
3. **RG hazard:** HOTRG-style coarse-graining (linearized pushforward \(H\mapsto JHJ^\top\)) can generate **huge curvature anisotropy** (large \(\lambda_{\max}\)).
4. **Riccati “restoration”:** applying the explicit spectral map
   \[
   \lambda \mapsto \frac{\lambda}{1+\eta\lambda}
   \]
   (a discrete Riccati/Euler step) crushes the large eigenvalues back to \(O(1)\).

The files present *numerical evidence* for each link.  
None of this is a proof of a Yang–Mills mass gap; it is a plausible **control strategy** for keeping convexity from being annihilated by coarse-graining.

---

## 1. Haar curvature “seed” on a tiny lattice (SU(2) scan)

A direct scan over random configurations suggests that adding an explicit Haar-like quadratic curvature term can shift a Wilson-like Hessian upward.

In one experiment (periodic \(L=2\), \(d=4\), random configs scaled by \(0.1\), Haar coefficient \(c_0=0.25\)), the smallest Hessian eigenvalue behaved as follows:

- \(\beta=0.5\):
  - sample 0: \(\lambda_{\min}(W)\approx -0.0589\), \(\lambda_{\min}(W+\text{Haar})\approx +0.1911\)
  - sample 1: \(-0.0654 \to +0.1846\)
  - sample 2: \(-0.0823 \to +0.1677\)

- \(\beta=1.0\):
  - sample 0: \(-0.1374 \to +0.1126\)
  - sample 1: \(-0.1334 \to +0.1166\)
  - sample 2: \(-0.1440 \to +0.1060\)

- \(\beta=2.0\):
  - sample 0: \(-0.2701 \to -0.0201\)
  - sample 1: \(-0.2773 \to -0.0273\)
  - sample 2: \(-0.3110 \to -0.0610\)

So at fixed \(c_0\), the Haar-like term lifts the spectrum for moderate \(\beta\), but does not fully cure negativity at larger \(\beta\).  
This is *exactly* the kind of “curvature floor” tuning problem one expects if convexity is to be maintained across regimes.

---

## 2. Riccati law for minimal curvature under vHJ flow (PDE analogue)

The vHJ equation used as a geometric analogue is:

\[
\partial_t S = \Delta S - \|\nabla S\|^2,
\quad\text{equivalently}\quad
S = -\log u,\;\; \partial_t u=\Delta u.
\]

A 4D finite-difference experiment tracked the smallest eigenvalue of the Hessian at the origin, \(\lambda_{\min}(t)\), showing monotone decay with no sign change.

One sample trajectory:

| step (≈ time) | \(\lambda_{\min}\) |
|---:|---:|
| 0 | 1.846839 |
| 50 | 1.690464 |
| 100 | 1.558517 |
| 150 | 1.445689 |
| 200 | 1.348103 |
| 250 | 1.262871 |
| 300 | 1.187772 |
| 350 | 1.121113 |
| 400 | 1.061551 |
| 450 | 1.007987 |

The files then fit the **Riccati form**
\[
\frac{1}{\lambda(t)} \approx \alpha t + b,
\]
with an example estimate \(\alpha \approx 1.02\times 10^{-3}\).

Interpretation (as a working theory):
- The flow preserves convexity.
- The slow-down of decay at large \(t\) is consistent with \(\lambda(t)\sim 1/t\), i.e., a Riccati mechanism.

---

## 3. Micro-ground-truth: SU(3) plaquette Hessian has rank-8 curvature block

A particularly clean “sanity anchor” appears in the SU(3) plaquette Hessian spectrum (right-invariant coordinates, projected to a physical subspace):

- 32 total eigenvalues (4 links × 8 generators).
- 24 eigenvalues \(\approx 0\) (gauge/redundancies at this micro level).
- 8 eigenvalues exactly \(8/3 \approx 2.6666667\).

So the Wilson plaquette curvature “lives” on an 8D gauge-invariant quotient, consistent with the idea that a single plaquette really only cares about one SU(3) loop variable.

This is important because it provides an **autodiff-derived “correct micro Hessian”** that can be used as a trusted input to downstream RG diagnostics.

---

## 4. HOTRG curvature explosion + Riccati damping (numerical evidence)

A HOTRG-linearization experiment constructs a Jacobian \(J\) from a tensor merge and measures the coarse Hessian by pushforward:

\[
H_{\text{coarse}} = J H J^\top.
\]

### 4.1 One-step HOTRG pushforward

Reported spectrum behavior:

- Before Riccati:  
  \(\lambda_{\min}\approx -6\times 10^{-11}\) (numerical ~0),  
  \(\lambda_{\max}\approx 2.65\times 10^{5}\).

- After repeated Riccati steps \(\lambda\mapsto \lambda/(1+\eta\lambda)\) with \(\eta=0.1\):

| step | \(\lambda_{\max}\) |
|---:|---:|
| 1 | 9.999623 |
| 2 | 4.999906 |
| 3 | 3.333291 |
| 4 | 2.499976 |
| 5 | 1.999985 |
| 6 | 1.666656 |
| 7 | 1.428564 |

The pattern is exactly what the map predicts: large eigenvalues get squashed toward \(O(1/\eta)\), while near-zero modes are nearly unchanged.

### 4.2 Multi-step RG + Riccati

A 5-step loop repeats:

1. pushforward \(H\mapsto J H J^\top\),
2. (identity) projector in tensor space,
3. Riccati smoothing.

One run:

- Initial expanded \(H\): \(\lambda_{\min}=+2.278651\times 10^{-1}\), \(\lambda_{\max}=+8.823058\).
- RG step 1: before Riccati \(\lambda_{\max}\approx 2.789805\times 10^5\), after Riccati \(\lambda_{\max}\approx 9.999642\).
- RG steps 2–5: before Riccati \(\lambda_{\max}\approx 1.6383\times 10^5\), after Riccati \(\lambda_{\max}\approx 9.999390\).

So the coarse-graining repeatedly creates a huge \(\lambda_{\max}\), and the Riccati map repeatedly brings it back.

**Caution:** the HOTRG Jacobian here is linearized around a trivial tensor, and the Hessian used in tensor space is a proxy embedding of a smaller “physical Hessian” into the HOTRG input dimension. So treat this as a *diagnostic* — not a final physics statement.

---

## 5. Why this is potentially interesting

The Riccati map is a very explicit spectral control tool:

- It prevents “curvature blow-up” at the top end.
- It has a simple continuous-time interpretation: \(\dot\lambda=-\eta \lambda^2\).

A plausible strategic goal (still speculative):
- Maintain a **uniform convexity window** across RG steps: keep \(\lambda_{\min}\ge \kappa>0\) and \(\lambda_{\max}\le K\).
- Then apply functional inequality machinery (Bakry–Émery, LSI/Poincaré) to get a **scale-uniform spectral gap**, and then a mass scale.

This is a “convexity-first” approach to spectral gaps, and it is not the standard QFT route — which is why it’s interesting.

---

## 6. Next work that would most upgrade this from “cool numerics” to “research-grade”

1. **Replace proxy embeddings with a real mapping** from link degrees of freedom to tensor degrees of freedom (and back), so that \(H\) and \(J\) genuinely act on the same physical object.
2. **Project out gauge zero modes correctly** at each scale (Hodge projector / Coulomb gauge, plus torons/harmonics).
3. Track not just \(\lambda_{\max}\), but **\(\lambda_{\min}\)** in the *physical* subspace under RG + smoothing.
4. Derive a **rigorous inequality** showing that the Riccati map corresponds to integrating out a convex Gaussian “noise” (or some controlled coarse-graining) rather than an ad hoc spectral clamp.
5. Connect the resulting uniform convexity to a **uniform LSI constant** and then to exponential decay of correlators in a transfer-matrix setting.

---

## Sources used

- `Simulations_and_Results_Summary.txt` (vHJ curvature flow + Riccati fit; Haar scan summary).
- `12-3-25 FINAL CODE RUN.pdf` (Haar scan numbers; SU(2) setup).
- `GPT CODE PRODCUTIOPN TEST.txt` (SU(3) plaquette Hessian spectrum; HOTRG pushforward + Riccati tables; multi-step RG+Riccati).
- `CHAT YANG SIMULATION 4x4.txt` (high-level dependency graph and framing).
