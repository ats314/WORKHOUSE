# Block-Convexity Engine: Spark \(\to\) Flow \(\to\) Gap

This note isolates the **abstract mechanism** repeatedly used across the project:

- **Spark:** obtain a *strictly positive* convexity/Hessian lower bound at some scale (or on some “coarse” degrees of freedom).
- **Flow:** prove that convexity is **stable under coarse-graining** (RG steps, marginalization, integrating out UV variables), perhaps with quantitative degradation.
- **Gap:** use Bakry–Émery / Poincaré / log-Sobolev technology to convert convexity into a **spectral gap** and exponential mixing/clustering.

The point of writing this as an “engine” is that it applies beyond lattice Yang–Mills: any Gibbs measure with a robust convexity source plus controlled interactions can be fed into it.

---

## 1. Convexity and functional inequalities

Consider a compact Riemannian manifold \((M,g)\) with probability measure
\[
d\mu(x)=Z^{-1}e^{-S(x)}\,d\mathrm{vol}(x),
\]
and Langevin generator
\[
L f=\Delta f-\langle \nabla S,\nabla f\rangle.
\]

If the action is uniformly convex,
\[
\nabla^2 S(x)\succeq \rho I
\quad\text{for all }x\in M,
\]
then (in the Euclidean case and in many manifold settings with appropriate curvature control) one gets a **Bakry–Émery curvature-dimension condition**
\[
\Gamma_2(f)\ge \rho\,\Gamma(f),
\]
which implies a **Poincaré inequality**
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\rho}\int |\nabla f|^2\,d\mu,
\]
and therefore a **spectral gap**
\[
\lambda_1(-L)\ge \rho.
\]

Interpretation: uniform convexity of \(S\) acts like a “mass” term that suppresses long-wavelength wandering of the diffusion.

---

## 2. Marginalization preserves strong log-concavity

Let \((x,y)\in\mathbb{R}^{m}\times \mathbb{R}^{n}\), and \(f(x,y)=e^{-S(x,y)}\) with
\[
\nabla^2_{(x,y)} S(x,y)\succeq \rho I_{m+n}.
\]
Define the marginal
\[
f_{\mathrm{eff}}(x)=\int_{\mathbb{R}^n} e^{-S(x,y)}\,dy = e^{-S_{\mathrm{eff}}(x)}.
\]
Then \(S_{\mathrm{eff}}\) is also \(\rho\)-convex:
\[
\nabla^2_x S_{\mathrm{eff}}(x)\succeq \rho I_m.
\]

This is a high-level convex-geometry statement (Prékopa-type arguments): **global strong convexity survives integration**.

---

## 3. Quantitative block-RG convexity inequality with cross couplings

In practice, one often only has **blockwise** convexity and must control cross terms.

Write the Hessian in blocks:
\[
\nabla^2 S(x,y)=
\begin{pmatrix}
A(x,y) & B(x,y)\\
B(x,y)^\top & C(x,y)
\end{pmatrix}.
\]
Assume uniform bounds:
\[
A\succeq \alpha I_m,\qquad
C\succeq \gamma I_n,\qquad
\|B\|_{\mathrm{op}}\le M,
\]
with \(\gamma>0\).

Define coarse graining by integrating out \(y\):
\[
e^{-S_{\mathrm{eff}}(x)}=\int_{\mathbb{R}^n}e^{-S(x,y)}\,dy.
\]

A standard identity gives
\[
\nabla_x^2 S_{\mathrm{eff}}(x)=\mathbb{E}_x[A(x,Y)]-\mathrm{Cov}_x(\nabla_x S(x,Y)).
\]

Using a Brascamp–Lieb/Poincaré bound on the covariance term (coming from the \(\gamma\)-convexity in \(y\)), one obtains:

\[
\nabla_x^2 S_{\mathrm{eff}}(x)\succeq \left(\alpha-\frac{M^2}{\gamma}\right)I_m.
\]

So convexity is preserved if
\[
M^2<\alpha\gamma.
\]

**Interpretation:** coarse convexity is not automatic; it survives if the “UV stiffness” \(\gamma\) beats the mixed coupling strength \(M\).

---

## 4. Spark–Flow–Gap as a reusable template

A pragmatic “engineering” version:

1. **Spark:** show that at some scale (or for some effective action) you have
   \[
   \nabla^2 S \succeq \rho_* I
   \quad\text{on physically relevant directions.}
   \]
2. **Flow:** show that a coarse-graining step produces
   \[
   \rho_{\mathrm{new}} \ge \rho_* - \frac{M^2}{\rho_*}
   \quad\text{(or better)}.
   \]
   If \(\rho_*>M\) you get \(\rho_{\mathrm{new}}>0\).
3. **Gap:** apply Bakry–Émery \(\Rightarrow\) Poincaré \(\Rightarrow\) spectral gap.

The nontrivial work in applications is almost always step (1): finding a real, \(a\)-independent spark in the continuum limit.

