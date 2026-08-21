# The Block-Convexity Engine Spark–Flow–Gap in one reusable lemma

This is the most “portable” piece of the project: a quantitative statement that convexity can survive integrating out variables *if* cross-couplings are controlled.

It’s the mathematical core behind the slogan

\[
\textbf{Spark} \;\Longrightarrow\; \textbf{Flow} \;\Longrightarrow\; \textbf{Gap}.
\]

- **Spark:** produce a positive curvature lower bound \(\rho>0\) at some scale.
- **Flow:** show \(\rho\) does not collapse when you integrate out degrees of freedom.
- **Gap:** \(\rho>0\) yields Poincaré/log-Sobolev \(\Rightarrow\) spectral gap/exponential mixing.

---

## 1. Coarse/fine split and the problem

Let \((x,y)\in\mathbb R^m\times\mathbb R^n\) and \(S(x,y)\in C^2\).
Define the coarse-grained effective action by marginalizing the \(y\)-variables:
\[
e^{-S_{\mathrm{eff}}(x)} := \int_{\mathbb R^n} e^{-S(x,y)}\,dy.
\]

Question: under what assumptions does **uniform convexity in \((x,y)\)** imply **uniform convexity in \(x\)** after integrating out \(y\)?

---

## 2. The block Hessian RG inequality

Write the Hessian of \(S\) in block form:
\[
\nabla^2 S(x,y)=
\begin{pmatrix}
A(x,y) & B(x,y)\\
B(x,y)^\top & C(x,y)
\end{pmatrix},
\]
where \(A\in\mathbb R^{m\times m}\), \(C\in\mathbb R^{n\times n}\), \(B\in\mathbb R^{m\times n}\).

Assume uniform bounds (for all \((x,y)\)):

- coarse curvature: \(A(x,y)\succeq \alpha I_m\),
- fine curvature: \(C(x,y)\succeq \gamma I_n\) with \(\gamma>0\),
- cross coupling: \(\|B(x,y)\|_{\mathrm{op}}\le M\).

### Theorem 2.1 block convexity survives marginalization
Under the three bounds above, the coarse effective action satisfies
\[
\nabla_x^2 S_{\mathrm{eff}}(x)\succeq \left(\alpha-\frac{M^2}{\gamma}\right)I_m.
\]
In particular, if \(M^2<\alpha\gamma\), then \(S_{\mathrm{eff}}\) is uniformly convex in \(x\) with curvature
\[
\rho_{\mathrm{new}}=\alpha-\frac{M^2}{\gamma}>0.
\]

#### Proof clean and explicit
Let \(\mu_x(dy)\propto e^{-S(x,y)}dy\) be the conditional measure at fixed \(x\).
A standard differentiation-under-the-integral identity gives
\[
\nabla_x^2 S_{\mathrm{eff}}(x)
=
\mathbb E_x[A(x,Y)] - \mathrm{Cov}_x(\nabla_x S(x,Y)).
\]
Test against a unit vector \(v\in\mathbb R^m\):
\[
v^\top \nabla_x^2 S_{\mathrm{eff}}(x)v
=
\mathbb E_x[v^\top A(x,Y)v]
-
\mathrm{Var}_x\!\big(v^\top \nabla_x S(x,Y)\big).
\]

- Since \(A\succeq \alpha I\), we have \(\mathbb E_x[v^\top A v]\ge \alpha\).

- For the variance term, apply a Poincaré/Brascamp–Lieb inequality in \(y\):
  if \(C(x,y)\succeq \gamma I\) (uniform strong log-concavity in \(y\)), then
  \[
  \mathrm{Var}_x(f(Y))\le \frac{1}{\gamma}\,\mathbb E_x\big[\|\nabla_y f(Y)\|^2\big].
  \]
  Take \(f(y)=v^\top \nabla_x S(x,y)\). Then \(\nabla_y f = B(x,y)^\top v\), so
  \[
  \|\nabla_y f\|^2=\|B^\top v\|^2\le \|B\|_{\mathrm{op}}^2\|v\|^2\le M^2.
  \]
  Hence \(\mathrm{Var}_x(f(Y))\le M^2/\gamma\).

Putting these together gives
\[
v^\top \nabla_x^2 S_{\mathrm{eff}}(x)v \ge \alpha-\frac{M^2}{\gamma}.
\]
Since this holds for all unit \(v\), the matrix inequality follows. \(\square\)

---

## 3. Two useful corollaries

### 3.1. A curvature recursion multi-step RG
If at “scale \(k\)” you can take \(\alpha=\gamma=\rho_k\) and \(M\le M_k\), then after integrating out a block you get
\[
\rho_{k+1}\;\ge\;\rho_k-\frac{M_k^2}{\rho_k}.
\]
A sufficient condition for \(\rho_{k+1}>0\) is \(\rho_k>M_k\).

This is exactly the inequality used to define “RG-stable strong-coupling subwindows”.

### 3.2. A no-loss theorem when you have *full* strong log-concavity
If the full Hessian satisfies \(\nabla^2_{(x,y)}S(x,y)\succeq \rho I_{m+n}\), then the marginal is \(\rho\)-strongly log-concave:
\[
\nabla_x^2 S_{\mathrm{eff}}(x)\succeq \rho I_m.
\]
This is a Prékopa-type stability phenomenon: **true strong convexity does not degrade under marginalization.**

The block inequality above is what you use when you *don’t* have full strong log-concavity and need to pay for cross-couplings.

---

## 4. Where this plugs into lattice gauge theory

In the lattice application, \(x\) and \(y\) represent coarse and fine subsets of links (after gauge-fixing, i.e. restricting to horizontal directions).  

- \(\alpha,\gamma\) come from whatever convexity you can prove at the current scale.
- \(M\) is controlled by operator-norm bounds on mixed second derivatives (typically coming from the Wilson term).

The finite-cutoff Haar-vs-Wilson window gives one way to produce a Spark at the UV scale (see **RECOMMENDED_01**), but it dies in the continuum.
So the real game is: **find a Spark at a physical scale**, then use the block inequality to make it flow.

That’s why the conjectural “entropic Gribov spark” (see **RECOMMENDED_04**) is so central: it’s a candidate Spark that isn’t proportional to \(a^2 g(a)^2\).

---

## 5. What would strengthen this engine

The inequality is already sharp in spirit, but applications depend on estimates:

- Make \(M\) smaller by proving mixed derivatives are smaller on *typical* configurations (localization), or on horizontals.
- Make \(\gamma\) larger by identifying genuinely convex “fast modes” (e.g., gauge-fixed directions with strong quadratic confinement).
- Replace the crude uniform bounds by a probabilistic version: \(A,C,B\) random under \(\mu\), and you control the *tail* of bad events.

Those upgrades are where the project becomes genuinely interesting (and genuinely hard).
