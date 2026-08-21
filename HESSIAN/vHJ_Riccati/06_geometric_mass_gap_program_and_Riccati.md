# Program-level synthesis: geometric mass generation + Riccati-stabilized scale uniformity (with explicit lemmas)

## Scope

This note is the only one in the bundle that is partly *programmatic*. It still only uses mechanisms and lemmas that appear explicitly in the project files, but it reframes them as a coherent “geometric mass-generation principle” with a plausible route to scale-uniform control.

Any speculative extrapolation is explicitly marked as such.

---

## 1. Geometric mass generation principle (non-speculative statement)

A recurring pattern in the project is that the effective operator controlling covariances has the form
\[
M \;=\; m^2 I + t\,d_1^*d_1
\quad\text{on}\quad
H_{U^{(0)}}=\ker(d_0^*),
\tag{1.1}
\]
where:

* \(t\) comes from the Wilson quadratic form around the vacuum.
* \(m^2\) comes from **Haar geometry**, i.e. from \(\mathrm{Ric}_{g_\Lambda}\) inside \(\mathrm{Ric}_{\mu_\Lambda}=\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda\).

Two features are structural and volume-independent:

1. \(m^2>0\) depends only on the group geometry (Ricci floor), not on \(|\Lambda|\).
2. On \(\ker d_0^*\), the symbol of \(d_1^*d_1\) collapses to the scalar lattice Laplacian symbol, yielding explicit exponential decay bounds for \(M^{-1}\).

This provides a technically sharp “birthplace” of a lattice mass scale: the exponential-decay exponent of \(M^{-1}\).

---

## 2. The role of horizontality is not cosmetic

The explicit Green’s-function decay lemma uses the fact that on \(\ker d_0^*\),
\[
\widehat{d_1^*d_1}(k)=\lambda(k)\,\mathrm{Id}
\quad \text{(scalar)}.
\tag{2.1}
\]
Off \(\ker d_0^*\), the Maxwell symbol contains the non-scalar projector piece \(q\otimes\overline q\), and the decay proof becomes less clean.

Thus the gauge-theoretic ingredient “gradients of gauge-invariant observables are horizontal” is not just for removing gauge directions: it is what makes the Fourier-symbol argument usable *without losing constants*.

---

## 3. Fixing the Lyapunov bottleneck by a character-based global proxy

The analytic engine’s bottleneck was identified precisely:

* If \(z_p=d_G(U_p,\mathbf 1)^2\), then \(X_\ell^a X_\ell^a z_p\) is not uniformly controlled globally (cut locus).
* Replace \(z_p\) by a smooth class function such as
  \[
  \widetilde z(U)=1-\frac{1}{N}\Re\operatorname{Tr}(U),
  \tag{3.1}
  \]
  and drift computations can be closed with uniform second-derivative bounds.

An additional sharp fact (proved in the companion note in this bundle) is that for the averaged \(\overline V_\Lambda=1+\frac{1}{|P|}\sum_p \widetilde z(U_p)\), the pure Laplacian obeys an **exact** affine drift identity
\[
\Delta_\Lambda \overline V_\Lambda = -\lambda \overline V_\Lambda + b,
\qquad b=2\lambda,
\tag{3.2}
\]
with \(\lambda\) determined purely by the fundamental Laplacian eigenvalue under the chosen metric convention.

This is a rare situation: a globally smooth Lyapunov candidate with explicit uniform constants.

---

## 4. Discrete Riccati stabilization as an RG “convexity floor protector”

The project includes a general stabilization lemma intended to prevent curvature/convexity constants from collapsing under repeated RG steps.

### Lemma 4.1 (Discrete Riccati stabilization)

Let \((\lambda_n)_{n\ge 0}\subset(0,\infty)\) satisfy
\[
\lambda_{n+1}\ \ge\ \lambda_n - a\lambda_n^2 + b,
\qquad a>0,\ b>0.
\tag{4.1}
\]
Define the fixed point floor
\[
\lambda_*:=\sqrt{b/a}.
\tag{4.2}
\]

Then:

1. If \(0<\lambda_0\le \lambda_*\), then \(\lambda_n\) is nondecreasing and \(\lambda_n\le \lambda_*\) for all \(n\).
2. If \(\lambda_0\ge \lambda_*\), then \(\lambda_n\ge \lambda_*\) for all \(n\).
3. In either case, \(\lambda_n\to\lambda_*\) with an explicit exponential rate after the change of variables
   \[
   y_n:=\operatorname{arctanh}(\lambda_n/\lambda_*).
   \]

#### Proof sketch

Write \(f(x)=x-a x^2+b\). Then \(f\) is concave on \(\mathbb R_+\) with fixed points at \(x=\lambda_*\) and \(x=-\lambda_*\). On \([0,\infty)\), \(f(x)\ge x\) for \(x\in[0,\lambda_*]\) and \(f(x)\le x\) for \(x\ge \lambda_*\), while \(f(x)\ge \lambda_*\) for all \(x\ge \lambda_*\). Iterating these monotonicity relations yields (1)–(2).

For the quantitative rate, set \(x_n=\lambda_n/\lambda_*\in(0,\infty)\). Then (4.1) becomes
\[
x_{n+1}\ \ge\ x_n + \gamma(1-x_n^2),
\qquad \gamma:=\sqrt{ab}>0.
\tag{4.3}
\]
The map \(x\mapsto \operatorname{arctanh}(x)\) converts the logistic-type increment into an additive step:
\[
\operatorname{arctanh}(x+\gamma(1-x^2)) \approx \operatorname{arctanh}(x)+\gamma,
\]
and a careful inequality (the project’s note supplies it explicitly) yields an exponential approach of \(x_n\) to \(1\), hence of \(\lambda_n\) to \(\lambda_*\). \(\square\)

### Why this matters here

If \(\lambda_n\) is interpreted as “the minimal curvature/convexity constant on SAFE at RG scale \(n\)”, and the RG map perturbs it by a negative quadratic term (due to interactions) plus a positive constant reinjection (due to Haar mass / block averaging), then (4.1) is the correct schematic inequality. The lemma guarantees a **scale-uniform positive floor** \(\lambda_*\) once the recursion is verified.

---

## 5. A concrete “larger theory” direction (explicitly speculative)

**Working hypothesis (speculative):** There is a general geometric principle for compact-group lattice gauge systems:

> *Positive Ricci curvature of the single-site group manifold provides a universal on-site confining term (“mass”), and gauge invariance forces relevant gradients to lie in a transverse sector where the Maxwell operator scalarizes. Together these effects can drive uniform exponential clustering once a Lyapunov globalization mechanism is installed.*

If true, this is not specific to Yang–Mills; it would be a template for:
* compact nonabelian lattice gauge models,
* certain constrained sigma models with gauge redundancy,
* possibly discrete higher-form gauge theories where the relevant cochain Laplacians also scalarize on transverse sectors.

The hypothesis is credible only insofar as the project can prove the missing globalization and continuum-scaling steps. It is not a claim of a solved Clay problem.

---

## 6. What further work would actually test the hypothesis inside this project

1. **Upgrade the Lyapunov drift from \(\Delta\) to the full generator \(L\).**  
   The exact affine identity (3.2) is for \(\Delta\). One must prove a *deterministic* inequality for
   \[
   L\overline V_\Lambda = \Delta \overline V_\Lambda - \langle\nabla S_W,\nabla \overline V_\Lambda\rangle
   \]
   with uniform constants (or else switch to a different \(W_\Lambda\) where the cross term is controllable).

2. **Make the localization/globalization step quantitative without degrading the exponent.**  
   The matrix Green’s-function exponent \(\nu\) is only useful if the localization error can be made small in a way that does not destroy exponential decay. The project has a clean localization identity; it needs a uniform tail bound (Lyapunov or capacity) that is compatible with it.

3. **Continuum scaling: show \(\eta(a)\sim m_{\mathrm{gap}}a\).**  
   Even a perfect fixed-\(a\) engine can yield only \(m(a)\gtrsim 1/a\) unless the \(\beta(a)\) trajectory and normalization are controlled. This is the nonnegotiable constructive-YM barrier.

