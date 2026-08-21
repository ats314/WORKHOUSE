# G. Checklist of Analytic Tasks Remaining — With Frontier/Open Flags

This is the “engineering checklist” version of the program.
Each item is tagged:

- **[DONE-ish]**: essentially complete in finite dimension (up to polishing constants).
- **[TRACTABLE]**: hard but realistically attackable with careful analysis.
- **[FRONTIER]**: this is where current mathematics for 4D YM genuinely gets strained.

No fake victories.

---

## G0. One-line target

You want a **uniform spectral gap / mass scale** in the continuum limit of 4D SU(3) Yang–Mills.

Everything below is a subcomponent of that.

---

## G1. Local convexity / BE curvature in a small-field core (finite cutoff)

### G1.1 Haar Hessian lemma (chart, small field)
**Goal:** show
\[
\nabla^2 S_{\rm Haar}(A)\ \succeq\ (c_0 - C_H \|A\|^2)\,I
\quad\text{for }\|A\|\le r_0.
\]

Status: **[DONE-ish]**  
Mechanism is analytic (Jacobian is an even analytic function of \(\mathrm{ad}_A\)).

Remaining work:
- make constants explicit for a chosen SU(3) normalization,
- track the chart radius and norm equivalence constants.

### G1.2 Wilson Hessian increment bound (local analytic constant)
**Goal:** in an exponential chart,
\[
\|\nabla^2 S_W(A) - \nabla^2 S_W(0)\|_{\rm op}
\ \le\ C_W\,\|A\|^2
\quad\text{for }\|A\|\le r_0.
\]

Status: **[TRACTABLE]**  
Reason: \(S_W\) is analytic in \(A\); by Taylor’s theorem the Hessian increment is controlled by 4th derivatives, and odd terms vanish by symmetry (real part / anti-Hermitian structure), giving a natural \(\|A\|^2\) scaling.

Hard part:
- turning “analytic ⇒ bounded derivatives” into a usable constant \(C_W\) for SU(3) with lattice combinatorics.

Numerical calibration exists (effective constants \(\sim 14\)–\(17\) in the code’s normalization), which is a big help.

### G1.3 Combined convex core BE lemma (Haar + Wilson)
**Goal:** for \(A\) in the core \(\|A\|_\infty\le R\),
\[
\nabla^2 S_{\rm eff}(A)\ \succeq\ \rho_{\beta,R}\,I,
\qquad
\rho_{\beta,R}=c_0 - (C_H + \beta C_W)R^2.
\]

Status: **[TRACTABLE]** once G1.1 and G1.2 are in hand.

---

## G2. Outlier control (tails) and Lyapunov drift (finite cutoff)

### G2.1 Intrinsic (group-distance) tail bounds
**Goal:** show the measure of configurations with some link far from identity is small:
\[
\mu_{\beta,\Lambda}\bigl(\exists \ell:\ d(U_\ell,I)\ge \delta\bigr)
\ \lesssim\ |L|\,\mathrm{poly}(\beta)\,e^{-c\beta\delta^2}.
\]

Status: **[TRACTABLE]** in finite volume if done carefully.

Caveat:
- Single-link bounds are easy (compactness + local quadratic core + Laplace lower bound).
- Lattice-level bounds require control of how energy localizes and how marginals behave; crude union bounds may be too weak for sharp continuum scaling.

### G2.2 Lyapunov drift condition for the Langevin generator
**Goal:** find \(W\ge 1\) such that for generator \(L\),
\[
LW \le -\lambda W + b\,1_{\mathcal{C}_R}.
\]

Status: **[FRONTIER]** for “real” YM scaling.

Why hard:
- In algebra coordinates the Haar term is *not globally coercive*.
- The Wilson action is bounded on the compact group and does not automatically give a Euclidean quadratic drift.

So any Lyapunov argument must be geometric and multiscale.

---

## G3. Dynamic / multiscale mechanisms (the “race condition”)

### G3.1 Prove a smoothing/coarse-graining flow drives fields into the convex core
**Goal (prototype statement):**
starting from a typical configuration at scale \(a\),
a controlled RG/flow map \(\Phi_t\) satisfies
\[
\mu_{\beta(a)}\bigl(\Phi_t(A)\notin\mathcal{C}_{R_{\rm conv}(\beta(a))}\bigr)
\le e^{-c\,t/a^\alpha}
\]
for some scaling exponent \(\alpha>0\).

Status: **[FRONTIER]**

This is the heart of the continuum proof attempt: it is exactly the quantitative statement that makes “core convexity” useful when the core shrinks with \(\beta(a)\).

The project has **numerical evidence** that gradient-flow steps can increase \(\lambda_{\min}\), but not yet a uniform restoration theorem.

### G3.2 Matrix evolution inequalities for curvature along the flow
**Goal:** control the evolution of the Hessian or a curvature proxy along the coarse-graining.
Often formulated as a matrix Riccati-type inequality.

Status: **[FRONTIER]** (in the YM setting)

Even when the PDE is known (e.g. vHJ Hessian PDE), converting it into a *uniform-in-\(a\)* convexification mechanism is difficult.

---

## G4. Continuum limit and uniform functional inequalities

### G4.1 Uniform-in-\(a\) BE curvature (or a substitute)
**Goal:** a curvature-type lower bound that does not die as \(a\to 0\).

Status: **[FRONTIER]**

Because \(\beta(a)\to\infty\), any naive core radius shrinks.  
You need either:
- a genuinely uniform curvature mechanism, or
- a multiscale decomposition where each scale has its own controlled core.

### G4.2 Uniform LSI / spectral gap in the continuum limit
**Goal:** a Poincaré/LSI constant that survives \(a\to 0\), giving a real mass gap.

Status: **[FRONTIER]**

This is (morally) equivalent to the mass gap problem itself, but it can sometimes be attacked via constructive RG if all sub-lemmas are in place.

### G4.3 Constructive RG matching for 4D YM (actual renormalization, not vibes)
**Goal:** a rigorous flow from lattice YM to a continuum limit with controlled effective actions and preserved gap.

Status: **[FRONTIER]** (this is deep constructive field theory territory)

---

## G5. Geometry / gauge singularities (Gribov, reducibles)

### G5.1 Polarity/capacity approach
**Goal:** show Gribov/reducible strata are capacity-zero (polar) and can be ignored in Dirichlet-form arguments.

Status:  
- **[TRACTABLE]** in finite dimension under strong absolute continuity bounds,  
- **[FRONTIER]** in the continuum limit because constants may blow up.

---

## G6. What is “most promising next” (highest ROI)

1. **Get an honest numerical \(C_W\) estimator working** (Hessian increment norm), and check it matches the convexity-bound inferred constants.
2. **Prove the local Wilson Hessian increment bound** with a constant in the same ballpark.
3. **Replace all fake Euclidean tails** with **intrinsic group-distance tail/Lyapunov constructions**.
4. Use the q-Racah / \(T_q\) toy tower to prototype a **real multiscale outlier-exclusion proof** before trying to lift it to YM.

---
