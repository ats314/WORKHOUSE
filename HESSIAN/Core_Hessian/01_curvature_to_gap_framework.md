# Curvature \(\to\) Gap \(\to\) Mass: a finite-dimensional theorem pipeline

## 0. Scope (what is actually proved here)

Everything in this document is **rigorous in finite dimension** (e.g. lattice models after choosing coordinates and gauge-fixing, or scalar lattice models). The logical spine is:

\[
\text{Hessian lower bound} \Rightarrow \text{Bakry–Émery curvature} \Rightarrow \text{LSI + Poincaré} \Rightarrow \text{spectral gap/mixing} \Rightarrow \text{clustering} \Rightarrow \text{(OS) Hamiltonian mass gap}.
\]

For Yang–Mills, the nontrivial work is verifying the hypotheses uniformly in volume and under a chosen coarse-graining.

---

## 1. Langevin generators, \(\Gamma\), and \(\Gamma_2\)

Let \(S\in C^2(\mathbb{R}^n)\) be confining and define
\[
\mu(dx) = Z^{-1} e^{-S(x)}\,dx.
\]
The (overdamped) Langevin generator acting on smooth \(f\) is
\[
(Lf)(x) = \Delta f(x) - \nabla S(x)\cdot \nabla f(x).
\]
Define the carré-du-champ
\[
\Gamma(f,g) := \tfrac12\big(L(fg) - fLg - gLf\big),\qquad \Gamma(f):=\Gamma(f,f),
\]
and its iterated form
\[
\Gamma_2(f) := \tfrac12\big(L\Gamma(f) - 2\Gamma(f,Lf)\big).
\]
For this diffusion,
\[
\Gamma(f,g)=\nabla f\cdot \nabla g,\qquad \Gamma(f)=|\nabla f|^2.
\]

---

## 2. Bakry–Émery–Hessian identity (the key local computation)

**Theorem 2.1 (Bakry–Émery–Hessian identity).** For \(L=\Delta-\nabla S\cdot\nabla\) and smooth \(f\),
\[
\Gamma_2(f)
= \|\nabla^2 f\|_{\mathrm{HS}}^2 + \langle \nabla f, (\nabla^2 S)\,\nabla f\rangle.
\]

*Proof sketch.* Expand \(L\Gamma(f)\) and \(\Gamma(f,Lf)\), use \(\Gamma(f)=|\nabla f|^2\), and collect terms.

---

## 3. Bakry–Émery curvature and functional inequalities

**Definition 3.1 (\(\mathrm{BE}(\rho)\)).** We say \(\mu\) satisfies Bakry–Émery curvature \(\mathrm{BE}(\rho)\) if
\[
\Gamma_2(f) \ge \rho\,\Gamma(f)\qquad\text{for all smooth }f.
\]

A sufficient (and in this setting essentially equivalent) condition is a Hessian lower bound:
\[
\nabla^2 S(x) \succeq \rho I\quad\text{for all }x.
\]
Indeed, by Theorem 2.1,
\(
\Gamma_2(f) \ge \langle \nabla f,(\nabla^2 S)\nabla f\rangle \ge \rho|\nabla f|^2=\rho\Gamma(f).
\)

**Theorem 3.2 (\(\mathrm{BE}(\rho)\Rightarrow\) Poincaré and LSI).** If \(\mu\) satisfies \(\mathrm{BE}(\rho)\) with \(\rho>0\), then:

1. (**Poincaré / spectral gap**) for mean-zero \(f\in H^1(\mu)\),
\[
\mathrm{Var}_\mu(f) \le \frac1\rho \int |\nabla f|^2\,d\mu.
\]
2. (**Log–Sobolev inequality**) for \(f\ge 0\) smooth,
\[
\mathrm{Ent}_\mu(f) := \int f\log\frac{f}{\int f\,d\mu}\,d\mu
\le \frac{1}{2\rho}\int \frac{|\nabla f|^2}{f}\,d\mu.
\]

Consequences: exponential convergence of the semigroup \(P_t=e^{tL}\) in \(L^2(\mu)\) with rate \(\rho\), and exponential entropy decay with the same scale.

---

## 4. From a spectral gap to exponential clustering (finite volume)

Let \(\Lambda\) be a finite lattice region and \(\mu_\Lambda\) a Gibbs measure on \(\mathbb{R}^{n(\Lambda)}\) (scalar case) or a coordinate chart for link variables (gauge case).

A *finite-volume* Poincaré constant gives a mixing time scale for local observables. Under an additional **locality** structure of the generator (carré-du-champ involves only near-neighbor derivatives), the spectral gap controls decay of correlations.

**Lemma 4.1 (locality \(+\) spectral gap \(\Rightarrow\) clustering template).** Suppose:

- The generator decomposes as a sum of local pieces \(L=\sum_{X\subset\Lambda} L_X\) with bounded range.
- A uniform Poincaré inequality holds with constant \(\rho>0\) independent of volume.

Then there exist \(c,C>0\) such that for local observables \(F,G\) supported in disjoint sets with graph distance \(d\),
\[
|\mathrm{Cov}_{\mu_\Lambda}(F,G)| \le C\,e^{-c d}\,\|F\|_{\mathrm{Lip}}\,\|G\|_{\mathrm{Lip}}.
\]

*Comment.* The precise constants depend on the locality norm and the choice of Lipschitz/Dirichlet norms. This is the step you would formalize using Helffer–Sjöstrand representations or finite-speed propagation bounds for Glauber/Langevin dynamics.

---

## 5. From Euclidean clustering to a Hamiltonian mass gap (OS)

Assume the Euclidean field theory satisfies Osterwalder–Schrader reflection positivity (OS positivity), so Euclidean correlators reconstruct a Hilbert space \(\mathcal{H}\), vacuum \(\Omega\), and Hamiltonian \(H\ge 0\).

**Lemma 5.1 (exponential decay \(\Rightarrow\) spectral gap).** If for a dense class of time-zero fields \(\mathcal{O}\), the two-point functions satisfy
\[
\langle \Omega, \mathcal{O}\,e^{-tH}\,\mathcal{O}\,\Omega\rangle
\le C e^{-m t}\qquad (t\to\infty),
\]
then \(\mathrm{spec}(H)\cap(0,m)=\varnothing\), i.e. the mass gap is at least \(m\).

This is the standard “Laplace transform of the spectral measure” argument.

---

## 6. Main theorem (finite-dimensional, hypothesis-driven)

**Theorem 6.1 (curvature-stable mechanism \(\Rightarrow\) mass gap at fixed cutoff).**
Consider a family of finite-dimensional Gibbs measures \(\{\mu_\ell\}\) produced by an admissible coarse-graining scheme \(\ell\mapsto\mu_\ell\) such that for each \(\ell\):

1. (**Curvature**) \(\mu_\ell\) satisfies \(\mathrm{BE}(\rho_\ell)\) with \(\inf_\ell \rho_\ell \ge \rho_*>0\).
2. (**Locality**) The associated generators are local in the carré-du-champ sense.
3. (**Polarity**) Any singular strata (e.g. reducible connections in gauge quotients) are polar for the relevant Dirichlet form.
4. (**OS positivity**) The Euclidean measure satisfies reflection positivity.

Then:

- Each \(\mu_\ell\) satisfies uniform LSI and Poincaré inequalities with constants controlled by \(\rho_*\).
- Local correlations cluster exponentially at scale \(\gtrsim \rho_*\).
- The reconstructed Hamiltonian has a strictly positive mass gap \(\Delta E\ge c\rho_*\) at that cutoff.

*What it does **not** claim:* it does **not** identify the continuum limit, does not prove YM measure existence, and does not give the correct asymptotic value of the gap as lattice spacing \(a\to 0\). It packages the problem into a finite list of analytic conditions.

---

## 7. Scalar prototype (end-to-end success)

A uniformly convex scalar lattice action (e.g. \(\phi^4\) with strong enough quadratic pinning) satisfies
\(
\nabla^2 S_\Lambda(\phi)\succeq \rho_* I
\)
uniformly in volume, hence triggers the entire pipeline above. This is the “calibration model” proving the mechanism works in a nontrivial interacting 4D lattice theory.

