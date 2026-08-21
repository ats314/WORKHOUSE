# One‑Step RG Stability of Convexity via a Block Hessian (Schur‑Complement) Inequality

## 0. Executive idea

Suppose an action \(S(x,y)\) is uniformly convex jointly in coarse variables \(x\) and fine variables \(y\).  
After integrating out \(y\), the coarse effective action
\[
  S_{\mathrm{eff}}(x) := -\log\int e^{-S(x,y)}\,dy
\]
need **not** stay convex: the \(-\log\) generates a covariance term that subtracts curvature.

This note isolates a clean inequality showing that convexity *does* survive **one RG step** provided the mixed \(x\)–\(y\) couplings are sufficiently small compared to the fine‑scale curvature.

The application to lattice Yang–Mills is: Haar gives a “mass curvature” \(\rho_*(a)\), Wilson couplings give a mixed‑block size \(M\), and one obtains a stricter “very strong coupling” window
\[
  g^4>\frac{24}{c_0 a^2}
\]
in which coarse‑grained convexity persists.

---

## 1. Differentiating the log‑integral: curvature = mean Hessian − covariance

Fix \(x\) and define the conditional (fine) Gibbs measure
\[
  d\mu_x(y)
  := Z(x)^{-1}e^{-S(x,y)}\,dy,\qquad
  Z(x)=\int e^{-S(x,y)}dy.
\]
Then
\[
  S_{\mathrm{eff}}(x)=-\log Z(x).
\]

A standard computation yields

\[
  \nabla_x S_{\mathrm{eff}}(x) = \mathbb{E}_{\mu_x}\big[\nabla_x S(x,y)\big],
\]
and
\[
  \nabla_x^2 S_{\mathrm{eff}}(x)
  = \mathbb{E}_{\mu_x}\big[\nabla_{xx}^2 S(x,y)\big]
    \;-\;
    \mathrm{Cov}_{\mu_x}\!\big(\nabla_x S(x,y)\big).
\]

So convexity survives if we can control the covariance term.

---

## 2. Bounding the covariance using a Poincaré inequality in \(y\)

Assume that for each fixed \(x\), the conditional measure \(\mu_x\) satisfies a Poincaré inequality with constant \(\gamma>0\):
\[
  \mathrm{Var}_{\mu_x}(f)
  \le \frac{1}{\gamma}\int \|\nabla_y f\|^2\,d\mu_x.
\]
A sufficient condition is a uniform lower bound on the \(yy\)-block Hessian:
\[
  \nabla_{yy}^2 S(x,y)\ \succeq\ \gamma I.
\]

Now fix any unit vector \(v\in\mathbb{R}^{\dim x}\) and consider the scalar function
\[
  f_v(y):= v\cdot \nabla_x S(x,y).
\]
Then
\[
  \mathrm{Var}_{\mu_x}(f_v)
  \le \frac{1}{\gamma}\int \|\nabla_y f_v\|^2\,d\mu_x
  =  \frac{1}{\gamma}\int \|(\nabla_{yx}^2 S)\,v\|^2\,d\mu_x.
\]

Assume a uniform mixed‑block bound
\[
  \|\nabla_{yx}^2 S(x,y)\|\ \le\ M
  \quad\text{(operator norm)}.
\]
Then \(\|(\nabla_{yx}^2 S)\,v\|\le M\|v\|=M\), and therefore
\[
  \mathrm{Var}_{\mu_x}(f_v)\ \le\ \frac{M^2}{\gamma}.
\]

But \(\mathrm{Var}_{\mu_x}(f_v)\) is exactly \(v^\top \mathrm{Cov}_{\mu_x}(\nabla_x S)\,v\). Hence
\[
  v^\top \mathrm{Cov}_{\mu_x}(\nabla_x S)\,v\ \le\ \frac{M^2}{\gamma}
  \quad\Longrightarrow\quad
  \mathrm{Cov}_{\mu_x}(\nabla_x S)\ \preceq\ \frac{M^2}{\gamma}\,I.
\]

---

## 3. The block convexity bound

Assume additionally
\[
  \nabla_{xx}^2 S(x,y)\ \succeq\ \alpha I.
\]
Then, combining with the covariance estimate,
\[
  \nabla_x^2 S_{\mathrm{eff}}(x)
  \succeq
  \left(\alpha-\frac{M^2}{\gamma}\right)I.
\]

### Proposition (one‑step convexity stability)
If
\[
  \alpha\gamma > M^2,
\]
then the coarse effective action \(S_{\mathrm{eff}}(x)\) is uniformly convex with curvature at least \(\alpha-M^2/\gamma\).

This is essentially a Schur‑complement idea expressed through the log‑integral identity.

---

## 4. Plug‑in to lattice Yang–Mills: the “very strong coupling” window

In the lattice YM extraction:

- the strong‑coupling convexity from Haar\(+\)Wilson gives a curvature lower bound
  \[
    \rho_*(a)=c_0 a^2 g^2-\frac{12}{g^2},
  \]
- the size of mixed couplings is controlled by the Wilson Hessian scale
  \[
    M=\beta C_V(N)=\frac{12}{g^2},
  \]
- and one applies the proposition with \(\alpha=\gamma=\rho_*(a)\).

Then the condition \(\alpha\gamma>M^2\) becomes
\[
  \rho_*(a)^2 > \left(\frac{12}{g^2}\right)^2
  \quad\Longleftrightarrow\quad
  \rho_*(a)>\frac{12}{g^2}.
\]
Using \(\rho_*(a)=c_0 a^2 g^2-\frac{12}{g^2}\), this is equivalent to
\[
  c_0 a^2 g^2-\frac{12}{g^2} > \frac{12}{g^2}
  \quad\Longleftrightarrow\quad
  c_0 a^2 g^4 > 24.
\]

### Conclusion
A sufficient “one‑step RG stability” condition is
\[
  g^4>\frac{24}{c_0 a^2}.
\]

Inside this subwindow, coarse‑graining cannot destroy convexity at first order; instead it preserves a positive curvature margin.

---

## 5. What this buys you

This inequality is not a full RG theorem. But it provides a **quantitative bridge**:

- *static convexity at one scale* \(\Rightarrow\) *convexity at the next scale*,  
- with an explicit gap between the mere convexity window (\(12/(c_0 a^2)\)) and the “RG‑stable” window (\(24/(c_0 a^2)\)).

That gap is where the interesting work lives: either tighten the estimates, or introduce better multiscale functional inequalities (MFIP‑style) to propagate curvature beyond a single step.

