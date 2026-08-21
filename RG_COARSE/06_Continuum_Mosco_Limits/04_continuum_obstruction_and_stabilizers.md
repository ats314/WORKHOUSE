# Continuum Obstruction and Candidate Stabilizers (Riccati Flow, Curvature/Anomaly, and “Log-Forest” UV Control)

This note extracts the **continuum-limit diagnosis** from the project notes, and reorganizes it into a crisp statement:

- the finite-cutoff Haar-convexity mechanism is real but **cannot** survive naive continuum scaling,
- therefore a continuum mass-gap proof needs an **\(a\)-independent convexity source** (“spark”) plus **RG-stable control** of how convexity evolves.

---

## 1. The basic obstruction: Haar convexity dies as \(a\to 0\)

In the finite-cutoff argument, the convexity lower bound has the schematic form
\[
\mathrm{Hess}_{\mathrm{hor}}\,S_{\mathrm{eff}}
\;\succeq\;
\underbrace{c_0 a^2 g^2}_{\text{Haar spark}}
\;-\;
\underbrace{\beta\,(\text{Wilson curvature size})}_{\text{interaction / nonconvexity}}.
\]

Along a continuum/asymptotically free scaling trajectory,
\[
a\to 0,
\qquad
g(a)\to 0,
\qquad
\beta(a)\sim \frac{1}{g(a)^2}\to\infty.
\]

So the Haar piece \(a^2 g(a)^2\to 0\), while Wilson contributions are multiplied by \(\beta\to\infty\).  
No amount of wishful algebra rescues a **global** uniform convexity estimate of that finite-cutoff type.

**Conclusion:** A continuum proof must use a different convexity source that does not vanish with \(a\).

---

## 2. Hessian flow under coarse-graining: why convexity can decay

A recurring theme in the notes is to model coarse-graining by heat-flow smoothing of densities:
\[
\partial_t \rho_t=\Delta \rho_t,
\qquad \rho_t=e^{-S_t}.
\]

This yields the viscous Hamilton–Jacobi equation
\[
\partial_t S_t=\Delta S_t-|\nabla S_t|^2.
\]

Differentiating twice gives a matrix Riccati-type evolution for the Hessian \(H_t=\nabla^2 S_t\):
\[
\partial_t H_t = \Delta H_t - 2H_t^2 + R_t,
\]
where \(R_t\) is a remainder term involving third derivatives.

### Gaussian warning shot

For a Gaussian initial condition, \(R_t\equiv 0\) and the eigenvalues solve
\[
\dot\lambda=-2\lambda^2
\quad\Rightarrow\quad
\lambda(t)\sim \frac{1}{2t}\to 0.
\]

So **without a positive source term**, convexity typically decays under smoothing.

---

## 3. Candidate stabilizer A: intrinsic geometry as a source term

On compact group manifolds (and products of them), there is positive Ricci curvature coming from the bi-invariant metric.  
The notes suggest that, after gauge fixing and restricting to physical directions, this can act as a background stabilizer.

At the level of a toy eigenvalue inequality, one imagines
\[
\dot\lambda \gtrsim -2\lambda^2 + \sigma_{\mathrm{geom}},
\qquad \sigma_{\mathrm{geom}}>0,
\]
whose ODE fixed point is
\[
\lambda_*=\sqrt{\sigma_{\mathrm{geom}}/2}.
\]

This is not yet a proof (one must control the projection to “physical” directions), but it motivates searching for a **scale-independent positive source** \(\sigma_*\).

---

## 4. Candidate stabilizer B: trace anomaly as effective curvature (conjectural)

The project proposes an “anomaly-curvature” identification, in words:

- the trace anomaly measures the breaking of scale invariance,
- it should manifest as an effective stabilizing curvature pressure in the RG/Hessian evolution.

A schematic conjectural relation (as extracted from the notes) is:
\[
\sigma_{\mathrm{anom}}(t)
=
\mathcal{K}\,\frac{\beta(g(t))}{g(t)}\,\left\langle \mathrm{Tr}\,F_{\mu\nu}^2\right\rangle_t.
\]

For asymptotically free YM, \(\beta(g)<0\) and \(\langle \mathrm{Tr}F^2\rangle>0\), so the sign of \(\mathcal{K}\) determines whether \(\sigma_{\mathrm{anom}}\) is stabilizing.

This idea is **not proved** in the notes; it is a proposed bridge between:
- QFT renormalization data (\(\beta(g)\), condensates),
- geometric/functional inequality data (Bakry–Émery curvature bounds).

If a rigorous version existed, it would be a major conceptual unifier.

---

## 5. Candidate stabilizer C: “log-forest” UV control as Log–Sobolev scaling (speculative)

Another striking proposal is to reinterpret “UV control” as a statement about **Log–Sobolev constants** \(C_{LS}(a)\) on the gauge-orbit metric-measure space:
\[
\mathrm{Ent}_{\mu_a}(f^2)\le C_{LS}(a)\int |\nabla f|^2\,d\mu_a.
\]

The project’s conjectural improvement is that for gauge-invariant observables, one might have only polylog growth:
\[
C_{LS}(a)\lesssim \left(\log\frac{1}{a}\right)^{p},
\]
instead of power-law blowup.

In the notes this is motivated by an information-compression metaphor (“gauge redundancy prunes a forest of UV noise”), but the *mathematical content* is: UV fluctuations are controlled sufficiently well to make multiscale error terms summable.

---

## 6. A multiscale recursion picture

The notes repeatedly circle a recursion of the form
\[
\rho_{j+1}\;\ge\; K\,\rho_j - \varepsilon_j + \sigma_*,
\]
where
- \(\rho_j\) is an effective convexity/gap parameter at scale \(j\),
- \(\varepsilon_j\) is an “entropy cost” of coarse-graining (to be controlled),
- \(\sigma_*\) is a scale-independent positive source (geometry/anomaly/horizon spark).

If \(\sum_j \varepsilon_j<\infty\) and \(\sigma_*>0\), the recursion can converge to a strictly positive fixed point, yielding a nonzero continuum gap.

This is a **blueprint**, not a proof; but it cleanly decomposes the continuum problem into two tasks:
1. prove \(\sigma_*>0\) from a genuine YM spark mechanism,
2. prove \(\varepsilon_j\) is summably small (LSI/UV control).

---

## 7. Where to push next (high-value technical tasks)

1. Put the “physical configuration space” on firm footing as a **metric-measure space** (orbifold/RCD-like) where \(\Gamma_2\), BE curvature, and LSI make sense despite singularities (Gribov copies).
2. Replace “global convexity” by a **localized curvature** notion on a high-probability core subset, and quantify how diffusion interacts with the boundary.
3. Make the Gribov/FMR entropic spark precise in a finite-cutoff model, then show it survives \(a\to 0\).
4. Sharpen the Wilson Hessian constant and isolate the exact horizontal subspace estimate, to widen the provable finite-cutoff window (useful as a controlled starting point for RG induction).

