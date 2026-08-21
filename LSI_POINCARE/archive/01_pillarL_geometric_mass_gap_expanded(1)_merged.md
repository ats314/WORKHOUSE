---
title: "Pillar L++: Geometric Convexity, Riccati Stabilisation, and a Continuum Handoff (Expanded Notes)"
date: "2025-12-28"
project: "SIMULATIONS"
---

> **Status.** These are *working notes* expanding “Pillar L” (geometric mass-gap mechanism) into a more explicit PDE/flow picture.  
> They are not a proof of the 4D continuum Yang–Mills mass gap; rather they aim to isolate a plausible *mechanism* that could be sharpened.

## 0. The elevator pitch (what changes vs the original Pillar L note)

The original Pillar L sketch emphasized:

1. **Haar measure $\Rightarrow$ an “entropic” quadratic term** in exponential coordinates.
2. **Irreducible sector $\Rightarrow$ global horizontal Hessian gap** by compactness + exclusion of reducibles.
3. **Bakry–Émery $\Rightarrow$ functional inequalities $\Rightarrow$ spectral gap** for the Langevin generator.

The new “enlightening” piece is the *flow/renormalisation bridge*:

- When one evolves the effective action $S_t$ under a smoothing flow (modelled by heat-kernel convolution of the density), the **smallest horizontal Hessian eigenvalue** $\lambda(t,U)$ satisfies a **parabolic Riccati-type inequality**  
  \[
    \partial_t \lambda \;\gtrsim\; -\alpha \lambda^2 + c_0
  \]
  (up to diffusion/advection terms that do not decrease the minimum), so it is driven **toward a strictly positive fixed point**
  \[
    \lambda_* \;=\; \sqrt{c_0/\alpha}.
  \]
In other words: once you can identify a strictly positive, *scale-independent* source term, convexity becomes a **stable attractor** rather than a fragile UV artifact.

This “Riccati stabilisation” is explicitly stated in the project’s derivations: a viscosity/maximum-principle argument yields a matrix-parabolic inequality and reduces it to a scalar Riccati ODE with a positive fixed point.【87:10†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L1-L69】

---

## 1. Geometry of configuration space and the horizontal Hessian

Let
\[
C_\Lambda \;=\; SU(N)^{N_b}
\]
be the link configuration manifold for a finite lattice $\Lambda$, with $N_b$ links, equipped with the product of the bi-invariant metrics.

Gauge transformations act by conjugation at vertices; at each $U\in C_\Lambda$ the tangent space splits orthogonally as
\[
T_U C_\Lambda \;=\; V_U \oplus H_U,
\]
where $V_U$ are **vertical** (gauge-orbit) directions and $H_U$ are **horizontal** (physical/orbit-space) directions.

For a gauge-invariant effective action $S_{\mathrm{eff}}$, vertical directions are “flat” by redundancy, so the meaningful convexity object is the **horizontal Hessian**
\[
\mathrm{Hess}^{\perp} S_{\mathrm{eff}}(U)
\;:=\;
\mathrm{Hess}\,S_{\mathrm{eff}}(U)\big|_{H_U\times H_U},
\qquad
\lambda_{\min}(U):=\lambda_{\min}\!\big(\mathrm{Hess}^{\perp}S_{\mathrm{eff}}(U)\big).
\]

A key finite-cutoff theorem in the project is:

> **Global horizontal Hessian gap.** There exists $c_*>0$ (depending on $N,a,\beta$ but **not** on volume) such that  
> \[
> \lambda_{\min}(U)\ge c_*
> \quad\text{for all }U\in C^{\mathrm{irr}}_\Lambda,
> \]
> i.e. on the irreducible sector.【87:9†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L28-L65】

The proof idea uses: local convexity near the identity + compactness + the fact that irreducibility forbids horizontal eigenvalues from hitting $0$ away from the reducible set (whose degeneracies are made irrelevant by polarity arguments in “Pillar M”).【87:9†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L55-L65】

---

## 2. Haar measure as an entropic potential (and why it is not just “a tiny $a^2$ term”)

### 2.1 General $SU(N)$ Jacobian in exponential coordinates

Write a single-link variable in exponential coordinates,
\[
U=\exp(iagA),\qquad A\in\mathfrak{su}(N).
\]
The Haar measure transforms as
\[
d\mu_H(U)=J(A)\,dA,
\]
with Jacobian (in adjoint form)
\[
J(A)=\det_{\mathfrak g}\!\left(\frac{\sinh(\mathrm{ad}_{iagA}/2)}{\mathrm{ad}_{iagA}/2}\right),
\]
and one defines the **Haar measure action**
\[
S_{\mathrm{Haar}}(A)=-\log J(A),
\]
additive over links.【97:3†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L30-L63】

A small-field expansion yields a **positive quadratic term**:
\[
S_{\mathrm{Haar}}(A)
=
c_0\,a^2 g^2\,\mathrm{Tr}(A^2)+O(a^4\|A\|^4),
\qquad
c_0=\frac{N^2-1}{2N},
\]
and therefore
\[
\mathrm{Hess}\,S_{\mathrm{Haar}}(0)=c_0 a^2 g^2\,\mathrm{Id}.
\]【97:3†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L66-L85】

This is the “Haar mass” seed.

### 2.2 The *global* part: SU(2) makes the intuition painfully clear

For $SU(2)$, parameterize
\[
U=\exp(i\,r\,\hat n\cdot \sigma),\qquad r\in[0,\pi],\;\hat n\in S^2.
\]
The Haar measure is (up to normalization)
\[
d\mu_H \propto \sin^2 r\;dr\,d\Omega,
\]
while flat Euclidean coordinates would contribute $r^2\,dr\,d\Omega$.  
Hence the Jacobian ratio is
\[
J(r)=\left(\frac{\sin r}{r}\right)^2,
\qquad
S_{\mathrm{Haar}}(r)=-\log J(r)=-2\log\!\left(\frac{\sin r}{r}\right).
\]

Now the “enlightening” observation:

- $S_{\mathrm{Haar}}(r)$ is not only quadratic near $r=0$,
  \[
  S_{\mathrm{Haar}}(r)=\frac{r^2}{3}+O(r^4),
  \]
  it is **globally repulsive** because it diverges at the cut locus $r\to\pi$.
- Moreover it is **convex** in the radial direction:
  \[
  S_{\mathrm{Haar}}'(r)=-2\cot r + \frac{2}{r},\qquad
  S_{\mathrm{Haar}}''(r)=2\left(\csc^2 r-\frac{1}{r^2}\right)\;>\;0
  \quad (0<r<\pi),
  \]
  since $\sin r < r$ for $r\in(0,\pi)$.

So even before adding the Wilson action, the Haar term behaves like an **entropic confining wall** on each link variable: it penalizes the exponential-map boundary and prevents “flat measure” wandering.

Why this matters conceptually: the naive statement “the Haar mass scales like $a^2$ and vanishes” is a **local** statement around $U\approx I$. Globally the Haar term is a *geometry-enforcing* potential tied to compactness; it can contribute to nonperturbative convexity control when combined with a flow argument.

---

## 3. From convexity to a *volume-independent* spectral gap (Bakry–Émery)

On a Riemannian manifold $(M,g)$ with potential $S$, the Langevin generator is
\[
Lf=\Delta f-\langle \nabla S,\nabla f\rangle.
\]
Bakry–Émery $\Gamma$-calculus gives
\[
\Gamma_2(f)=\|\nabla^2 f\|_{HS}^2
+
\langle (\mathrm{Ric}+\nabla^2 S)\nabla f,\nabla f\rangle,
\]
so a uniform lower bound
\[
\mathrm{Ric}+\nabla^2 S\ge \rho\,g\quad (\rho>0)
\]
implies Poincaré/log-Sobolev inequalities and a spectral gap at least $\rho$ for $-L$.【87:0†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L61-L114】

Two geometric facts in the project are crucial:

1. The product manifold $C_\Lambda=SU(N)^{N_b}$ has **Ricci curvature bounded below** by a constant $\rho_0>0$ depending only on $N$ (not volume).【87:4†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L7-L12】
2. Combining this with the horizontal Hessian gap yields a Bakry–Émery bound on the irreducible sector and thus a **finite-volume spectral gap independent of volume** for the Langevin generator.【87:4†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L16-L48】

So at fixed cutoff $a>0$, there is a very clean “curvature $\Rightarrow$ gap” route.

---

## 4. The Riccati-stabilisation mechanism (the “bridge”)

### 4.1 Modelling coarse-graining as heat flow on densities

A canonical smoothing model is: let $\rho_t$ evolve by a heat equation on configuration space, and write
\[
\rho_t \propto e^{-S_t}.
\]
Then $S_t$ satisfies a **viscous Hamilton–Jacobi** equation (Euclidean prototype):
\[
\partial_t S_t=\Delta S_t-|\nabla S_t|^2.
\]
This is attractive because it provides an explicit PDE controlling how *convexity* evolves.

### 4.2 Hessian evolution and a parabolic Riccati inequality

Let $H_t=\nabla^2_{\!\perp} S_t$ be the horizontal Hessian matrix-field, and let $\lambda(t,U)$ be its smallest horizontal eigenvalue at configuration $U$.

The project derives (via maximum principle for matrix parabolic equations) an inequality of the form
\[
\partial_t \lambda
\;\ge\;
\Delta \lambda -2(\nabla S_t\cdot\nabla)\lambda
-\alpha\,\lambda^2
+c_0,
\]
where:

- $c_0>0$ is a **positive source term** tied to the Haar contribution,
- $\alpha>0$ is geometric (controls the quadratic term coming from $H_t^2$).

Neglecting the diffusion/advection terms (which do **not** decrease the minimum under comparison principles) yields the scalar Riccati inequality
\[
\dot\ell=-\alpha \ell^2+c_0,
\qquad
\ell(0)\le \lambda(0,U).
\]

This ODE has a stable positive fixed point
\[
\ell_*=\sqrt{c_0/\alpha},
\]
and one gets a uniform-in-time lower bound $\lambda(t,U)\ge \ell(t)\ge \min\{\ell(0),\ell_*\}>0$.  
The document even writes an explicit solution in terms of $\tanh$.【87:10†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L1-L69】

### 4.3 Why this is “enlightening”

This mechanism reframes the continuum problem:

- The finite-cutoff convexity constant $\rho_*(a)$ may degrade as $a\to 0$ because the **explicit** Haar mass seed scales like $a^2$.
- But if the *flow itself* injects a positive source term $\sigma_{\mathrm{geom}}$ that does **not** vanish with $a$, then convexity becomes an **attractor**:
  even if $\rho_*(a)$ starts tiny, the flow pushes it up toward $\sqrt{\sigma_{\mathrm{geom}}/\alpha}$.

This idea is precisely articulated as a conjectural continuum handoff in the project: one assumes a Riccati-type bound with a source term from intrinsic curvature that is independent of $a$, so the limit retains a strictly positive horizontal Hessian bound.【87:2†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L23-L61】

---

## 5. Concrete next steps (how to sharpen this into something publishable)

Here are the “non-handwavy” steps that would turn this from a compelling story into a serious theorem program.

### Step A — Make the smoothing flow *the* renormalisation map

Pick a specific flow that is:

- gauge-invariant,
- local or quasi-local,
- compatible with Osterwalder–Schrader positivity (so spectral interpretations survive),
- and has a tractable PDE (or inequality) for $\nabla^2_{\!\perp} S_t$.

Candidates: heat-kernel convolution on $SU(N)$ links (a “heat RG”), or Wilson/gradient flow with controlled Jacobian terms.

### Step B — Prove the parabolic comparison argument on the **irreducible orbit space**

The inequality for $\lambda(t,U)$ should be stated on the quotient/orbit space, not on $C_\Lambda$ with gauge directions.  
This is where polarity of reducibles matters: one wants to ignore singular strata rigorously (capacity zero) and apply maximum principles on the regular stratum.

### Step C — Identify a truly scale-independent source term

At finite cutoff, $c_0$ is literally the Haar piece.  
For a continuum limit, one needs an $a$-independent geometric $\sigma_{\mathrm{geom}}$.

A plausible route: isolate the piece coming from **intrinsic positive curvature** (Ricci lower bound) of the compact group factors and show it contributes additively to the eigenvalue lower bound, uniformly under the chosen flow.

### Step D — Connect Langevin spectral gap to the **physical** mass gap in gauge theory

For scalar convex models, there is a relatively direct OS/stochastic-quantisation bridge between the generator gap and Euclidean time decay (the project includes this as a calibration example).【87:6†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L13-L47】

For gauge theory, one must incorporate:

- gauge-invariant observable algebras,
- reconstruction of the physical Hilbert space,
- relation between diffusion-time and Euclidean time (or a comparison with the transfer matrix).

The project pairs this with a second mechanism: a strong-coupling transfer-matrix gap, which one then hopes “flows” to continuum under RG.【87:5†2025-11-27_FiniteCutoffYangMillsMassGap_Yang-Mills-MassGap-MathematicalDerivations.pdf†L52-L63】

---

## 6. The one-sentence thesis

> **Mass gap as a stable fixed point of convexity under geometric RG:**  
> seed convexity at finite cutoff (Haar), prevent singular orbit-space degeneracies from mattering (polarity of reducibles), and use a Riccati-stabilised flow with an $a$-independent geometric source term to keep a positive horizontal curvature scale as $a\to 0$.

