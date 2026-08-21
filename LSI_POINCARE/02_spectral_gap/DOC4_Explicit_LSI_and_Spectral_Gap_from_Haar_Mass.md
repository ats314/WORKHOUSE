# Explicit Log–Sobolev Constant on Finite Lattice Yang–Mills via Bakry–Émery

## Abstract

A central payoff of the Bakry–Émery viewpoint is that a uniform curvature lower bound implies *dimension-free* functional inequalities with explicit constants.  
This note records the project’s finite-lattice claim:

\[
\operatorname{Ent}_\mu(f^2)\;\le\;\frac{2}{c_0}\int |\nabla f|^2\,d\mu,
\qquad
c_0=\frac{N^2-1}{2N},
\]
for the lattice Yang–Mills measure \(\mu\) on \(SU(N)^{\text{bonds}}\).

The novelty is not the Bakry–Émery theorem (classical), but the appearance of an **explicit group-theoretic constant** \(c_0\) for a non-Abelian lattice gauge measure, packaged in a way that plugs into tightness and continuum-limit arguments.

---

## 1. Setting: Gibbs measure on a compact manifold

Let \(M=SU(N)^{E}\) with the product Haar metric \(g\) and Haar volume \(d\mathrm{vol}_g\).  
Let \(S:M\to\mathbb R\) be an effective lattice action and
\[
d\mu = Z^{-1}e^{-S}\,d\mathrm{vol}_g.
\]
The symmetric diffusion generator is
\[
L=\Delta_g-\nabla S\cdot\nabla.
\]

The Bakry–Émery tensor is
\[
\mathrm{Ric}_\mu := \mathrm{Ric}_g+\nabla^2 S.
\]

---

## 2. The curvature-dimension condition \(CD(\rho,\infty)\)

The curvature-dimension condition is
\[
\mathrm{Ric}_\mu\ge \rho\,g
\qquad(\rho>0),
\]
equivalently \(\Gamma_2(f)\ge \rho\,\Gamma(f)\) for the carré du champ \(\Gamma\).

---

## 3. Bakry–Émery \(\Rightarrow\) log–Sobolev with explicit constant

### Theorem (Classical Bakry–Émery LSI)

If \(\mathrm{Ric}_\mu\ge \rho g\) with \(\rho>0\), then for all smooth \(f\),
\[
\operatorname{Ent}_\mu(f^2)
\le \frac{2}{\rho}\int |\nabla f|^2\,d\mu.
\]

Consequences include Poincaré inequality with constant \(1/\rho\) and spectral gap \(\lambda_1\ge \rho\).

---

## 4. The project’s lattice constant \(c_0\)

The project asserts a finite-lattice lower bound of the form
\[
\mathrm{Ric}_\mu \big|_{\text{physical}} \ge c_0\,g,
\qquad
c_0=\frac{N^2-1}{2N},
\]
as a synthesis of:

- a Haar-geometry (“Haar mass”) contribution, and
- Wilson-Hessian positivity on physical (horizontal) directions.

Given this \(\rho=c_0\), Bakry–Émery yields the explicit log–Sobolev inequality:

### Theorem (Finite-lattice LSI with explicit \(c_0\))

For the lattice YM measure \(\mu\) on \(SU(N)^{\text{bonds}}\),
\[
\boxed{
\operatorname{Ent}_\mu(f^2)
\;\le\;
\frac{2}{c_0}\int |\nabla f|^2\,d\mu,
\qquad c_0=\frac{N^2-1}{2N}.
}
\]

### Corollaries

- Poincaré:
  \[
  \operatorname{Var}_\mu(f)\le \frac{1}{c_0}\int|\nabla f|^2\,d\mu.
  \]
- Spectral gap:
  \[
  \lambda_1\ge c_0>0.
  \]
- Exponential \(L^2\) relaxation:
  \[
  \|P_t f-\mu(f)\|_{L^2(\mu)}\le e^{-c_0 t}\|f-\mu(f)\|_{L^2(\mu)}.
  \]

---

## 5. Why this matters for the broader program

An explicit LSI constant is a rare kind of “hard currency” in constructive QFT programs:

- It gives quantitative concentration of measure and mixing rates.
- It is stable under products/tensorization and often under controlled perturbations.
- It feeds directly into tightness/compactness arguments (e.g., embedding into negative Sobolev spaces) used for continuum limits.

The remaining mathematical work is to ensure that the curvature lower bound leading to \(c_0\) is:
1. genuinely global (not just in a small-angle tube),
2. compatible with gauge projection issues (horizontals vs full space),
3. uniform in the scaling limits required for a continuum theory.
