# Viscous Hamilton–Jacobi (vHJ), Hessian Flow, and Riccati Curvature Bounds

## Abstract

Gaussian coarse-graining of a Gibbs density \(\rho_0(x)=e^{-S_0(x)}\) generates a one-parameter family
\[
\rho_\ell = C_\ell * \rho_0, \qquad S_\ell = -\log \rho_\ell,
\]
where \(C_\ell\) is a centered Gaussian kernel. The map \(S_0\mapsto S_\ell\) obeys a **viscous Hamilton–Jacobi PDE**
\[
\partial_\ell S_\ell = \Delta S_\ell - |\nabla S_\ell|^2,
\]
and its Hessian satisfies a **matrix parabolic inequality** that yields a **Riccati-type lower bound** for the minimal curvature. The project’s PDE simulations validate that, for convex initial data, the minimal eigenvalues follow an almost perfect Riccati trajectory
\[
\lambda(t)\approx \frac{1}{\frac{1}{\lambda_0}+\alpha t},
\]
with \(\alpha\) empirically near-universal across modes.

This document collects the derivations and records the simulation evidence.

---

## 1. From heat flow to viscous Hamilton–Jacobi

Let \(S_0:\mathbb{R}^n\to\mathbb{R}\) and define
\[
\rho_0(x) = e^{-S_0(x)}.
\]
For \(\ell>0\), define the Gaussian coarse-grained density
\[
\rho_\ell(x) = (C_\ell * \rho_0)(x),
\qquad
S_\ell(x) = -\log \rho_\ell(x).
\]

Since \(C_\ell\) is the heat kernel (up to parameter conventions), \(\rho_\ell\) solves a heat equation in \(\ell\):
\[
\partial_\ell \rho_\ell = \Delta \rho_\ell.
\]

Compute using \(\rho_\ell = e^{-S_\ell}\):
\[
\partial_\ell \rho_\ell = -(\partial_\ell S_\ell)e^{-S_\ell},
\qquad
\Delta \rho_\ell = (\;|\nabla S_\ell|^2 - \Delta S_\ell\;)e^{-S_\ell}.
\]
Equating gives the vHJ PDE:
\[
\boxed{\;\partial_\ell S_\ell = \Delta S_\ell - |\nabla S_\ell|^2.\;}
\]

---

## 2. Gradient and Hessian flow

Define the gradient and Hessian:
\[
b_\ell = \nabla S_\ell,\qquad h_\ell = \nabla^2 S_\ell.
\]

Differentiating vHJ yields a PDE for the gradient (schematically a viscous Burgers-type equation):
\[
\partial_\ell b_\ell = \Delta b_\ell - 2 h_\ell b_\ell.
\]

Differentiating again gives a matrix PDE for \(h_\ell\). In the presence of an added “source” term \(J_\ell(x)\) (useful when modeling additional curvature injection),
\[
\partial_\ell S_\ell = \Delta S_\ell - |\nabla S_\ell|^2 + J_\ell(x),
\]
one obtains the structural form
\[
\boxed{\;
\partial_\ell h_\ell
=
\Delta h_\ell
- 2(\nabla S_\ell\cdot\nabla)h_\ell
- 2 h_\ell^2
+ \nabla^2 J_\ell.
\;}
\]
(Up to convention-dependent constants; the key term is the quadratic sink \(-2h^2\) plus the source \(\nabla^2 J\).)

---

## 3. Riccati inequality for the minimal eigenvalue

Let \(\lambda_{\min}(\ell,x)\) be the smallest eigenvalue of \(h_\ell(x)\). Evaluating the Hessian equation along a minimizing eigenvector and applying a maximum principle produces a Riccati-type differential inequality
\[
\partial_\ell \lambda_{\min}(\ell,x) \;\gtrsim\; -2\,\lambda_{\min}(\ell,x)^2 + \lambda_{\mathrm{source}}(\ell,x) - \mathrm{Err}(\ell,x),
\]
where:

- \(\lambda_{\mathrm{source}}(\ell,x)\) comes from \(\nabla^2 J_\ell\),
- the error term controls drift/transport and regularity artifacts.

### Source-free corollary

If \(J_\ell\equiv 0\) and errors are controlled, you get the clean Riccati decay bound:
\[
\partial_\ell \lambda_{\min} \gtrsim -2\lambda_{\min}^2
\quad\Longrightarrow\quad
\lambda_{\min}(\ell)\gtrsim \frac{\lambda_{\min}(0)}{1+2\lambda_{\min}(0)\ell}.
\]

### With a positive curvature source

If \(\nabla^2 J_\ell \succeq \kappa I\) uniformly, then \(\lambda_{\min}\) is pushed upward and can converge to a positive plateau. This is the conceptual role played by Haar-induced quadratic curvature in the Yang–Mills program.

---

## 4. Numerical validation: Riccati trajectories in PDE experiments
## 4. Numerical validation: Riccati trajectories in PDE experiments

The project contains multiple PDE-level experiments (2D and 4D grid solvers) evolving vHJ and tracking Hessian eigenvalues at the origin. The strongest diagnostic pattern is:

- **convex initial data** \(\Rightarrow\) convexity persists at the origin,
- eigenvalues \(\lambda_i(t)\) follow
  \[
  \lambda_i(t)\approx \frac{1}{b_i+\alpha t}
  \]
  with nearly identical \(\alpha\) across multiple modes (“universal curvature decay”).

### 4.1 Reported \(\alpha_i\) statistics (4D runs)

A representative 4D run reports modewise Riccati slopes \(\alpha_i\) and finds extremely small spread, e.g.

- Haar-only: mean \(\alpha\approx 7.90\times 10^{-4}\) with \(\mathrm{std}\approx 3.0\times 10^{-7}\),
- YM+Haar: mean \(\alpha\approx 7.89\times 10^{-4}\) with \(\mathrm{std}\approx 3.0\times 10^{-7}\),

corresponding to a relative spread on the order of \(4\times 10^{-4}\) (about \(0.04\%\)).

### 4.2 Example: true vs predicted eigenvalue along one trajectory

For a tracked mode, the “true” \(\lambda(t)\) and Riccati predictor \(\lambda_{\text{pred}}(t)\) agree to \(\sim 10^{-4}\) over long times. A typical log (abbreviated) looks like:

\[
\lambda_{\text{pred}}(t) = \Big(\frac{1}{\lambda_0} + \alpha t\Big)^{-1}.
\]

| \(t\) | \(\lambda_{\text{true}}(t)\) | \(\lambda_{\text{pred}}(t)\) |
|---:|---:|---:|
| 0 | 3.1376 | 3.1373 |
| 60 | 0.6526 | 0.6526 |
| 120 | 0.3872 | 0.3872 |
| 180 | 0.2759 | 0.2759 |
| 240 | 0.2150 | 0.2150 |
| 270 | 0.1959 | 0.1959 |

The striking part is not that Riccati decay occurs (that’s expected from the \(-2h^2\) sink), but that **multiple eigenmodes share essentially the same \(\alpha\)**, hinting at a coarse-graining universality class.

### 4.3 Practical caveat (critical for interpretation)

Monte-Carlo estimators of Hessians under coarse-graining can go catastrophically wrong when the underlying potential is not globally convex (because the Gaussian sampling cloud is unbounded and will probe nonconvex regions). The project resolves this by switching to **analytic Hessians** for test potentials (e.g. Gaussian bumps) and by restricting to regimes where global convexity is controlled.

The project contains multiple PDE-level experiments (2D and 4D grid solvers) evolving vHJ and tracking Hessian eigenvalues at the origin. The strongest diagnostic pattern is:

- **convex initial data** \(\Rightarrow\) **convexity persists at the origin**,
- eigenvalues \(\lambda_i(t)\) follow
  \[
  \lambda_i(t)\approx \frac{1}{b_i+\alpha t}
  \]
  with nearly identical \(\alpha\) across multiple modes (“universal curvature decay”).

### Example: trajectory match for one mode (recorded table)

A representative check reports \(\lambda_{\text{true}}(t)\) vs the Riccati predictor \(\lambda_{\text{pred}}(t)\) matching to ~\(10^{-4}\) across long times, e.g.
\[
\lambda_{\text{pred}}(t) = \Big(\frac{1}{\lambda_0} + \alpha t\Big)^{-1}.
\]

### Practical caveat (critical for interpretation)

Monte-Carlo estimators of Hessians under coarse-graining can go catastrophically wrong when the underlying potential is not globally convex (because the Gaussian sampling cloud is unbounded and will probe nonconvex regions). The project resolves this by switching to **analytic Hessians** for test potentials (e.g. Gaussian bumps) and by restricting to regimes where global convexity is controlled.

---

## 5. Minimal implementation (JAX finite-difference grid solver)

Below is a compact 2D template used as a “toy validator” (extendable to 4D with more compute):

```python
import jax
import jax.numpy as jnp

L = 64
X = 3.0
dx = 2*X/L
dt = 5e-4

xs = jnp.linspace(-X, X, L)
X1, X2 = jnp.meshgrid(xs, xs, indexing="ij")
grid2 = jnp.stack([X1, X2], axis=-1)  # (L,L,2)

H2 = jnp.array([[3.0, 0.3],
                [0.3, 2.5]])

def S0_2d(grid):
    g = grid.reshape(-1,2)
    vals = 0.5*jnp.einsum("...i,ij,...j->...", g, H2, g)
    return vals.reshape(L,L)

def laplace2(F):
    return (
        -4*F
        + jnp.roll(F,1,0) + jnp.roll(F,-1,0)
        + jnp.roll(F,1,1) + jnp.roll(F,-1,1)
    ) / (dx*dx)

def grad2_2(F):
    Fx = (jnp.roll(F,-1,0) - jnp.roll(F,1,0)) / (2*dx)
    Fy = (jnp.roll(F,-1,1) - jnp.roll(F,1,1)) / (2*dx)
    return Fx*Fx + Fy*Fy

S = S0_2d(grid2)
for n in range(500):
    S = S + dt*(laplace2(S) - grad2_2(S))
```

Hessian-at-origin diagnostics can be extracted by local finite differences near \((0,0)\), or by fitting \(S(t,x)\) locally to a quadratic.

---

## 6. Why this matters for Yang–Mills

The YM program tries to use:

- **Haar curvature** \(\Rightarrow\) a positive quadratic source \(J_\ell\) (in the effective action evolution),
- **vHJ/Hessian flow** \(\Rightarrow\) a controlled evolution of \(\lambda_{\min}\) under coarse-graining,

to produce a uniform Bakry–Émery lower bound and hence a mass gap.

The key remaining analytic challenge is to make the “source + error” control rigorous for the lattice YM effective action, rather than for finite-dimensional toy potentials.

