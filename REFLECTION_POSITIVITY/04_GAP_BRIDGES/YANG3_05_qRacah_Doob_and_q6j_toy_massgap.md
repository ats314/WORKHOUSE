# q-Racah Doob-Transformed Toy Mass Gap + q-6j Error Control (Numerical Pillar)

## Abstract

The YANG 3 project includes a self-contained “toy pillar” designed to mimic a **nonperturbative gap** in a mathematically explicit setting:

- Start with a **q-Racah Jacobi matrix** (tridiagonal, parameterized by \(q\in(0,1)\) and finite size \(N\)).
- Use the ground state to build a **Doob \(h\)-transform**, producing a valid Markov generator \(Q\) (row sums zero, nonnegative off-diagonals).
- Define the toy “mass gap” as the **spectral gap** \(m_q(N)\) of \(Q\).
- Study the approach \(q\to 1\) and extract a critical exponent \(\nu\) from finite-size scaling.
- In parallel, control the classical limit of the quantum-group \(6j\) symbol via a concrete error bound.

The project’s key numerical outputs are:
\[
m(q)\sim C(1-q)^\nu,\qquad \nu\approx 0.97,
\]
and an empirical error law for \(q\)-\(6j\):
\[
\big|\{6j\}_q-\{6j\}\big|\;\lesssim\; C\,\theta^2\, J_{\max}^{5/2}.
\]

---

## 1. q-Racah \(\to\) Doob transform \(\to\) Markov generator

### 1.1 Jacobi matrix from q-Racah recurrences

q-Racah polynomials satisfy a three-term recurrence with coefficients that define a symmetric tridiagonal Jacobi matrix \(H\). In finite size \(N\), \(H\in\mathbb{R}^{(N+1)\times(N+1)}\).

### 1.2 Doob transform

Let \(\psi>0\) be the ground state of \(H\) with eigenvalue \(E_0\). The Doob transform produces a Markov generator \(Q\) (in a standard discrete-state setting) by
\[
Q = \mathrm{diag}(\psi)^{-1}(H-E_0 I)\,\mathrm{diag}(\psi),
\]
followed by a sign convention ensuring nonnegative off-diagonals and zero row sums.

The toy “mass gap” is then
\[
m_q(N)=\lambda_1(Q)-\lambda_0(Q)=\lambda_1(Q),
\]
since \(\lambda_0(Q)=0\).

---

## 2. Numerical results: gap scaling and exponent

The project’s finite-size scaling analysis reports:

- a **safe region** where the Doob construction remains well-conditioned and the Markov constraints hold (notably \(\alpha=\beta=\gamma=\delta=1\), \(q\in(0,1)\), and moderate \(N\), e.g. \(N\le 12\)),
- a gap that stays positive for all \(q<1\),
- a critical approach as \(q\to 1\) with exponent
  \[
  \nu \approx 0.9668,
  \]
  extracted from a log–log fit of \(m(q)\) vs \(1-q\).

Heuristically, this is consistent with a “linear” critical scaling \(m(q)\propto 1-q\) (i.e. \(\nu\approx 1\)).

---

## 3. Composite transfer operator \(T_q\) (boundary-to-bulk construction)

A companion development defines a composite transfer operator \(T_q\) built from boundary data and a bulk projection (details in the project files). The intended interpretation is:

- \(T_q\) acts like a discrete transfer matrix capturing propagation in a q-deformed setting,
- the gap of \(T_q\) is another proxy for a mass scale,
- the construction is designed to be compatible with explicit error control in the \(q\to 1\) limit.

---

## 4. q-6j classical limit: empirical \(\theta^2 J^{5/2}\) error law

The project also includes a numerical exploration of the error between the q-deformed \(6j\) symbol and its classical value as \(q=e^{i\theta}\to 1\).

A reported error envelope is:
\[
\boxed{
\big|\{6j\}_q-\{6j\}\big|
\le C\,\theta^2\, J_{\max}^{5/2}
}
\]
with an experimentally estimated \(C\) on the order of \(10^{-1}\) (e.g. \(C_{\mathrm{global}}\approx 0.183\) in one sweep).

A practical “safe region” heuristic for a target tolerance \(\varepsilon\) is:
\[
\theta \lesssim \frac{\mathrm{const}(\varepsilon)}{J_{\max}^{5/4}}.
\]

This provides a rare commodity in toy-model regularizations: an explicit knob with an explicit error budget.

---

## 5. Minimal code sketch (Python/Numpy)

Below is a schematic (non-optimized) outline of the finite-size scaling workflow:

```python
import numpy as np

def spectral_gap(Q):
    evals = np.linalg.eigvalsh(Q)
    evals.sort()
    return float(evals[1] - evals[0])  # evals[0] ~ 0

def fit_exponent(q_vals, gaps):
    x = np.log(1 - np.array(q_vals))
    y = np.log(np.array(gaps))
    A = np.vstack([x, np.ones_like(x)]).T
    nu, logC = np.linalg.lstsq(A, y, rcond=None)[0]
    return nu, np.exp(logC)
```

The project files include additional structural projectors (Jacobi and parametric q-Racah projections) to keep the generator in a physically meaningful “safe manifold” during perturbations.

---

## 6. Why keep this pillar?

Even though it is not Yang–Mills, it supplies:

- an explicit discrete transfer operator with a tunable parameter \(q\),
- a demonstrably positive gap for \(q<1\),
- controlled approach to a critical limit,
- and an explicit error budget for q-deformed group-theoretic data (the \(6j\) symbols).

This makes it a valuable sandbox for testing “gap survival under deformation” ideas that are otherwise brutally nonconstructive in 4D gauge theory.

---

## Next directions

1. Push \(N\) larger and improve conditioning diagnostics (to verify stability beyond \(N\le 12\)).
2. Connect the \(q\)-deformation knob to a lattice-spacing-like parameter and study scaling-collapse more systematically.
3. Tighten the \(q\)-\(6j\) error law into a true theorem (replace empirical \(C\) with proven constants).

