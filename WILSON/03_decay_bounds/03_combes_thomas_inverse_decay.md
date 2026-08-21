# Combes–Thomas conjugation: exponential decay of the massive Maxwell inverse

This note extracts the project’s **finite-range inverse decay lemma** (Combes–Thomas style)
and explains how it produces **explicit exponential clustering rates** once we reduce
covariances to a massive Maxwell inverse.

---

## 1. Abstract setup: a positive finite-range operator on a graph

Let \(V\) be the vertex set of a graph with distance \(d(\cdot,\cdot)\).
Let \(A\) be a self-adjoint operator on \(\ell^2(V;\mathsf H_0)\)
(\(\mathsf H_0\) a fixed finite-dimensional Hilbert space, e.g. \(\mathfrak g\)).

Assume:

1. **Finite range**: there exists \(R\in\mathbb N\) such that \(A_{xy}=0\) whenever \(d(x,y)>R\).
2. **Spectral gap (positivity)**: there exists \(a_0>0\) with \(A\succeq a_0 I\).
3. **Off-diagonal row-sum control**:
   \[
   B:=\sup_{x\in V}\sum_{y\neq x}\|A_{xy}\|_{\mathrm{op}} < \infty.
   \]

---

## 2. The Combes–Thomas decay rate

Define the Combes–Thomas rate
\[
\eta := \frac{1}{R}\log\!\Bigl(1+\frac{a_0}{2B}\Bigr).
\]

The abstract lemma then yields an exponential off-diagonal bound of the form
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\;\le\;
C(a_0,B)\,e^{-\eta\,d(x,y)}.
\]

### Proof idea (compressed but explicit)
The “one-line” engine is conjugation by a weight:
for a fixed \(x_0\in V\), define the multiplication operator
\[
(W_\gamma f)(x) := e^{\gamma\,d(x,x_0)} f(x).
\]
Then analyze
\[
A_\gamma := W_\gamma A W_{-\gamma}.
\]
Finite range implies that \(A_\gamma-A\) is controlled by \((e^{\gamma R}-1)\) times the off-diagonal row sums.
Choosing \(\gamma\) so that this perturbation is \(\le a_0/2\) preserves invertibility and gives
\(\|A_\gamma^{-1}\|\le 2/a_0\).
Finally,
\[
(A^{-1})_{xy}
=
e^{-\gamma(d(x,x_0)-d(y,x_0))}\,(A_\gamma^{-1})_{xy},
\]
and selecting \(x_0=x\) turns the exponent into \(e^{-\gamma d(x,y)}\),
yielding the bound with \(\gamma=\eta\).

---

## 3. Specialization: the massive Maxwell operator on the link graph

The project’s key application is
\[
M := m^2 I + \alpha\,d_1^\*d_1,
\qquad
m^2=\frac{c_H}{2},\quad \alpha=\frac{\beta}{n\lambda_\rho}.
\]

Restrict to the horizontal sector \(M_H:=M|_{\ker(d_0^\*)}\).
This is a finite-range operator on the **link graph** (links as vertices, adjacency given by shared plaquettes).

- Positivity gap: \(a_0=m^2\).
- Range: typically \(R=1\) in the link-adjacency metric.
- Off-diagonal row-sum:
  since \(d_1^\*d_1\) has bounded degree \(D\),
  one expects
  \[
  B \;\lesssim\; \alpha\,D.
  \]

Therefore,
\[
\eta \approx \log\!\Bigl(1+\frac{m^2}{2\alpha D}\Bigr),
\qquad (R=1).
\]

---

## 4. From kernel decay to an explicit OS mass lower bound

Once covariances are bounded by the massive Maxwell kernel,
the decay rate \(\eta(a)\) transfers to Euclidean-time correlation decay, and then to an OS Hamiltonian gap.

The project packages an explicit formula:
\[
m_{\mathrm{Euc}}(a)=\frac{\eta(a)}{a},
\qquad
\eta(a) = \frac1R\log\!\Bigl(1+\frac{a_0}{2B}\Bigr),
\]
and in a representative specialization,
\[
m_{\mathrm{OS}}(\Lambda)
\ \ge\
\frac{1}{a}\log\Big(1+\frac{m^2}{2\alpha D}\Big).
\]

This is a strikingly explicit “physics-facing” bridge: it gives a quantitative spectral gap bound in terms of
the curvature mass \(m^2\) and stiffness \(\alpha\).

---

## 5. Further work that could expand this

1. **Sharper geometry in \(B\)**: improve the row-sum bound by exploiting cancellations or block structure in \(d_1^\*d_1\).

2. **Multiscale Combes–Thomas**: combine with RG coarse-graining to track how \(\eta(a)\) behaves across scales.

3. **Better distance choices**: pick a metric that matches physical separation of observables more directly (e.g. plaquette graph vs link graph), potentially improving constants.

