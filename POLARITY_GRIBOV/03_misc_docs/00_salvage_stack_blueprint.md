# Salvage Stack Blueprint: Curvature Seeds, Hessian Flow, and “Convex Cores” for Lattice Yang–Mills

*Status:* research program with several **rigorous finite-dimensional** lemmas + **numerical evidence** on small lattices.

## 1. The one-line idea

On a finite lattice, a spectral gap for the Langevin generator (hence exponential mixing and clustering) is guaranteed if the effective action is uniformly convex:
\[
\nabla^2 S_{\mathrm{eff}} \succeq \rho I \quad \Longrightarrow \quad \text{LSI}(\rho)\;\Longrightarrow\; \text{spectral gap}\;\gtrsim \rho .
\]
The core strategy in this project is to **engineer and propagate** such a convexity bound across coarse-graining by combining:

1. **A geometric “seed curvature”** coming from the **Haar Jacobian** in exponential coordinates on compact groups.
2. A **stability-preserving nonlinear smoothing** (viscous Hamilton–Jacobi / log-heat semigroup) whose Hessian evolution obeys a **matrix Riccati inequality**.
3. A measure-theoretic removal of gauge singular strata: **reducibles are polar (capacity zero)**, so they do not obstruct Dirichlet-form / functional-inequality arguments.
4. A “q-deformation sanity check” pillar: controlled classical limits of q-6j data + a q-Racah Doob toy model where a spectral gap can be tracked explicitly.

This is not yet a proof of the YM mass gap in the continuum limit. It is a coherent attempt to replace “Gaussian RG smoothing kills convexity” with a flow that can *in principle* preserve a curvature floor.

## 2. The convex-core mechanism (why Haar matters)

Using exponential coordinates \(U=\exp(A)\) with \(A\in\mathfrak{g}\), the Haar measure contributes a Jacobian \(J(A)\). Writing the effective action as
\[
S_{\mathrm{eff}}(A) \;=\; S_{\mathrm{Wilson}}(A) \;-\;\sum_{\ell}\log J(A_\ell),
\]
the **Haar term contributes a positive quadratic form** near \(A=0\), behaving like a mass term:
\[
-\log J(A) \;=\; \frac{1}{24}\big\langle A,\; \mathcal{M} A \big\rangle \;+\; O(\|A\|^4),
\]
with \(\mathcal{M}\) proportional to the adjoint Casimir (precise normalization depends on conventions).  

This suggests the existence of a **convex core**:
\[
\|A\|\le \sigma_\star(\beta)\quad \Rightarrow\quad \nabla^2 S_{\mathrm{eff}}(A)\succeq \rho(\beta)\,I,
\]
where \(\rho(\beta)\) stays positive for fixed lattice spacing and the “radius” \(\sigma_\star(\beta)\) shrinks with \(\beta\) (as the Wilson term stiffens).

Small-lattice Hessian scans in the project strongly support the presence of such a \(\sigma_\star(\beta)\) window.

## 3. The propagation mechanism (why vHJ matters)

If \(\rho_t = e^{-S_t}/Z_t\) solves the heat equation, then \(S_t\) solves the viscous Hamilton–Jacobi equation
\[
\partial_t S_t = \Delta S_t - |\nabla S_t|^2 + J_t.
\]
In finite dimension, differentiating yields a Hessian evolution of the form
\[
\partial_t H_t
= \Delta H_t - 2(\nabla S_t\cdot \nabla)H_t - 2H_t^2 + \nabla^2 J_t,
\]
so the “bad term” is the **Riccati sink** \(-2H_t^2\). If \(J_t\) contains a positive mass piece (Haar-like curvature), one can hope to obtain:
\[
\lambda_{\min}(H_t)\;\ge\; \underline\lambda(t)\quad\text{via a scalar Riccati inequality.}
\]
That gives a *template* for “convexity survives flow”.

## 4. Why polarity matters (removing the Gribov bogeyman)

The set of reducible connections is a singular stratum for gauge orbits. In an infinite-dimensional Gaussian reference setting, the project argues this set is **polar** (capacity zero). For Dirichlet-form arguments, polar sets can be removed without changing the form domain: heuristically, they are “almost never hit” by the relevant diffusion.  

This is the analytic move that lets one hope to treat the gauge quotient as essentially smooth “for free”.

## 5. Where the q-stuff plugs in (not decoration)

Two q-based modules serve as *numerical/structural sanity checks*:

- **q-6j classical limit:** on a small “safe region” in spin and deformation angle, the q-6j symbol differs from the classical 6j by a controlled \(O(\theta^2)\) error, with an empirically small constant. This is a candidate for a **computer-assisted theorem** once interval arithmetic is used.
- **q-Racah Doob toy model:** a tridiagonal q-Racah Hamiltonian admits a Doob transform to a Markov generator, whose spectral gap can be tracked as \(q\to 1\). A fitted scaling exponent \(\nu\approx 0.97\) appears in the data.

## 6. What would count as “the next proof step”

The blueprint becomes a rigorous mass-gap proof only if you can establish a uniform-in-volume, uniform-in-scale lower bound on BE curvature (or LSI constant) after the full RG / coarse-graining flow. A plausible proof path is:

1. **Local convexity:** prove the Haar-induced quadratic term dominates negative Wilson Hessian contributions inside \(\|A\|\le \sigma_\star(\beta)\).
2. **Concentration / metastability:** show the measure at the scales of interest spends overwhelming probability inside the convex core (or that excursions can be controlled).
3. **Flow stability:** show the chosen flow (vHJ / log-heat / some modified semigroup) propagates a curvature floor rather than destroying it.
4. **Thermodynamic + continuum limits:** extract uniform LSI/gap → clustering → Osterwalder–Schrader mass gap.

That is still a hard mountain. But the pieces collected in this repository are the *interesting footholds*.
