# Entropic Gribov Spark Conjecture a plausible IR “Spark” not tied to the cutoff

This is the most *conceptually novel* mechanism in the notes: the idea that **gauge fixing + boundary entropy** can generate a *quadratic* effective potential for infrared modes, i.e. a genuine Spark for the Spark–Flow–Gap engine.

It is explicitly **conjectural**. The value is that it turns “Gribov geometry” into a concrete quantitative target: a lower bound on the Hessian of an IR effective potential.

---

## 1. Why we need an IR Spark at all

A global Bakry–Émery curvature lower bound cannot hold as \(\beta\to\infty\) because the Wilson action has negative Hessian directions somewhere in configuration space (see **RECOMMENDED_02**).

The finite-cutoff Haar-vs-Wilson convexity window (see **RECOMMENDED_01**) produces convexity at very strong coupling, but it scales like \(a^2 g(a)^2\) and dies in the continuum limit.

So any continuum-relevant convexity mechanism must be either:

- **localized** (convexity only on a high-probability region), and/or
- **sparked** at a physical scale (not proportional to \(a^2\)).

This conjecture is a candidate for the second route.

---

## 2. The geometric picture working model

Work in a Landau-type gauge fixing where gauge fields are represented as a vector \(A\) in a huge-dimensional linear space (lattice gauge potential variables, after gauge fixing).

Heuristically, gauge fixing restricts you to a **fundamental domain** \(\mathcal F\) (think “Fundamental Modular Region”, FMR), whose boundary touches the **Gribov horizon** (where the Faddeev–Popov operator develops a zero mode).

Working assumptions (not proven in full generality, but standard as a heuristic model):

- \(\mathcal F\subset \mathbb R^D\) is **convex** and **bounded** (a convex body) in the gauge-fixed coordinates.
- The Gibbs weight is \(e^{-S(A)}\) with \(S\) not necessarily strongly convex globally.
- Entropy is enormous: \(D\) is of order \(\#\text{links}\times (N^2-1)\).

Now split variables into “IR” and “UV” parts:
\[
A = A_{\mathrm{IR}} \oplus A_{\mathrm{UV}},
\qquad 
A_{\mathrm{IR}}\in \mathbb R^k,\; k\ll D.
\]
Let \(P:\mathbb R^D\to\mathbb R^k\) be the projection onto IR coordinates, \(Y:=P(A)\).

Define the marginal density of \(Y\) by integrating out all other directions *within the domain*:
\[
\rho_{\mathrm{IR}}(y)
=
\int_{\{A\in\mathcal F:\;P(A)=y\}} e^{-S(A)}\, dA_{\mathrm{UV}}.
\]
Equivalently,
\[
\rho_{\mathrm{IR}}(y)=\int_{\mathbb R^{D-k}} e^{-S(y,z)}\mathbf 1_{\mathcal F}(y,z)\,dz.
\]

Define the IR effective potential:
\[
V_{\mathrm{eff}}(y):= -\log \rho_{\mathrm{IR}}(y).
\]

If \(V_{\mathrm{eff}}\) is **uniformly strongly convex** near the origin, that’s an IR Spark.

---

## 3. The conjecture a precise target

### Conjecture 3.1 Entropic Gribov Spark
There exists a fixed \(k\) (number of IR modes) and a scale \(m_*^2>0\), independent of the UV dimension \(D\), such that for the gauge-fixed fundamental domain \(\mathcal F\) and the induced IR effective potential \(V_{\mathrm{eff}}\),
\[
\nabla^2 V_{\mathrm{eff}}(0)\succeq m_*^2\,I_k.
\]

A stronger (and more useful) version would be: there is a neighborhood \(U\ni 0\) such that
\[
\nabla^2 V_{\mathrm{eff}}(y)\succeq m_*^2\,I_k
\quad \text{for all }y\in U.
\]

Interpretation: the IR marginal is approximately Gaussian near \(0\),
\[
\rho_{\mathrm{IR}}(y)\approx \exp\!\left(-\frac{m_*^2}{2}\|y\|^2\right),
\]
not because the *action* is quadratic, but because the **available volume in the fiber shrinks quadratically** as you move in IR directions (a boundary-entropy effect).

---

## 4. Why this is not crazy heuristics from high-dimensional convexity

Even with \(S\equiv 0\), the uniform measure on a high-dimensional convex body has a famous phenomenon:

> **Low-dimensional marginals often look Gaussian.**

There are several “central limit” results for isotropic log-concave measures / convex bodies that say: for fixed \(k\), a random \(k\)-dimensional projection looks close to a standard Gaussian when the ambient dimension is huge (under suitable regularity and position assumptions).

If \(\rho_{\mathrm{IR}}\) is close to a Gaussian in distribution, then \(-\log\rho_{\mathrm{IR}}\) should have a quadratic Taylor expansion near \(0\), i.e. a positive definite Hessian at the origin.

The Gribov horizon provides additional geometric structure: it is a boundary defined by a spectral constraint (a smallest eigenvalue hitting zero). Boundaries defined by spectral constraints can be *very* curved in high dimension, which is exactly what you want for an entropic quadratic term.

This is the “entropy does the confining” idea.

---

## 5. How it plugs into Spark–Flow–Gap

If Conjecture 3.1 holds, then the IR effective action has a curvature floor \(m_*^2\).
That’s precisely the Spark you need.

Then:

- Use the **block convexity engine** (RECOMMENDED_03) to show this convexity survives further integration/coarse-graining (Flow).
- Use standard “strong convexity \(\Rightarrow\) Poincaré/log-Sobolev \(\Rightarrow\) spectral gap” to get a mass gap in the IR effective theory (Gap).
- Use the localization bridge (RECOMMENDED_02) to control the parts of configuration space where gauge fixing is singular or where the domain geometry is not well behaved.

---

## 6. What to do next concrete and falsifiable

This conjecture is great because it can be *attacked*.

### 6.1. Numerical prototype on small lattices
Pick a small lattice (say \(4^4\), \(6^4\)), do a practical Landau-gauge fixing procedure, approximate restriction to a Gribov region proxy, and:

1. Compute a few lowest Fourier modes of \(A\) (your \(y\)).
2. Empirically estimate \(\rho_{\mathrm{IR}}(y)\).
3. Fit \(-\log\rho_{\mathrm{IR}}(y)\) near \(y=0\) and estimate the Hessian.

If the Hessian does *not* appear bounded below away from \(0\) as volume increases, that’s strong evidence against the spark.

### 6.2. Analytic toy model
Replace \(\mathcal F\) by a tractable convex body (e.g., a zonotope, a spectrahedron, or an intersection of half-spaces), pick a projection \(P\), and compute/estimate the fiber volume function
\[
y\mapsto \mathrm{Vol}\big(\mathcal F\cap P^{-1}(y)\big).
\]
Look for a robust quadratic lower bound on \(-\log\) of that volume near \(y=0\).

### 6.3. A “soft theorem” approach
Try to prove something like:

- If \(\mu\) is log-concave on \(\mathbb R^D\) and isotropic, then for typical \(k\)-dimensional projections the marginal density has a strictly positive Hessian at the origin with probability \(\to 1\) as \(D\to\infty\).

Even a *weak* version would be enough to justify a spark-like term.

---

## 7. Why I’m recommending this despite it being conjectural

Because it’s doing the right kind of weird:

- It directly targets the **one missing ingredient** in the continuum story (a non-vanishing Spark).
- It converts a famously slippery physical idea (“Gribov horizon affects IR physics”) into a sharp analytic object (\(\nabla^2 V_{\mathrm{eff}}\)).
- It’s falsifiable by computation and approachable through convex geometry.

That’s exactly the kind of conjecture that deserves to be sharpened rather than buried.
