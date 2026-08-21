# Curvature semigroup diagnostics: Riccati law, phase diagram, and obstruction proxies

This note collects (i) the *curvature–Riccati* identity used as a diagnostic for viscous Hamilton–Jacobi (vHJ) flow in 4D toy models, and (ii) the measured curvature–decay constants across multiple “phases” (choices of potential terms).

---

## vHJ flow and the Riccati diagnostic

We evolve an effective action (potential) \(S(t,x)\) by the viscous Hamilton–Jacobi semigroup
\begin{equation}
\partial_t S \;=\; \Delta S \;-\; \|\nabla S\|^2.
\end{equation}

The diagnostic observable is the *minimal curvature* (smallest Hessian eigenvalue) at a chosen reference point \(x_\star\) (often the origin):
\begin{equation}
\lambda_{\min}(t) \;=\; \lambda_{\min}\!\big(\nabla^2 S(t,x_\star)\big).
\end{equation}

A Riccati-type law is used as a closed-form model:
\begin{equation}
\frac{d\lambda}{dt}\;\approx\; -\alpha\,\lambda^2
\qquad\Longrightarrow\qquad
\frac{1}{\lambda(t)} \;\approx\; \frac{1}{\lambda(0)}+\alpha t.
\end{equation}

The check is purely linear regression of \(1/\lambda(t)\) vs. \(t\).

---

## Explicit regression primitive (data → \(\alpha\))

Given sampled times \(t_k\) and curvatures \(\lambda_k>0\), define \(y_k = 1/\lambda_k\) and solve
\(
y_k \approx \alpha\,t_k + b
\)
by least squares:

```python
import numpy as np

t_vals = np.array([...], dtype=float)
lam    = np.array([...], dtype=float)   # lam[k] > 0

inv = 1.0 / lam
A   = np.vstack([t_vals, np.ones_like(t_vals)]).T

alpha, b = np.linalg.lstsq(A, inv, rcond=None)[0]
lam_pred = 1.0/(b + alpha*t_vals)
```

---

## Example: Riccati fit data (4D run)

The sampled data used for one explicit fit is:

\begin{align}
t:&\quad 0,\; 50,\;100,\;150,\;200,\;250,\;300,\;350,\;400,\;450,\\
\lambda_{\mathrm{true}}:&\quad
1.846839,\;1.690464,\;1.558517,\;1.445689,\;1.348103,\\
&\quad 1.262871,\;1.187772,\;1.121113,\;1.061551,\;1.007987.
\end{align}

A linear regression on \(1/\lambda(t)\) yields representative parameters
\(\alpha \approx 0.00102145\), \(b\approx 0.238785\), and the predicted curve
\(
\lambda_{\mathrm{pred}}(t)=1/(b+\alpha t)
\)
tracks the measured values closely.

---

## Phase diagram: measured \(\alpha\)-bands across potentials

A single script aggregates per-mode \(\alpha_i\) values for several “phases” (different combinations of terms in \(S_0\)), then plots bars/lines.

The recorded per-phase arrays (four modes) include:

\begin{align}
\alpha_{\mathrm{quad}} &= (0.001002,\;0.001002,\;0.001002,\;0.001002),\\
\alpha_{\mathrm{haar}} &= (0.000788,\;0.000788,\;0.000788,\;0.000788),\\
\alpha_{\mathrm{haar+YM}} &= (0.000780,\;0.000781,\;0.000782,\;0.000782),\\
\alpha_{\mathrm{haar+SU2}} &\approx (0.0007875071,\;0.0007932955,\;0.0007627501,\;0.0007980805),\\
\alpha_{\mathrm{haar+SU3\ mass}} &\approx (0.0007973450,\;0.0007992039,\;0.0008004338,\;0.0008011904),\\
\alpha_{\mathrm{SU3\ comm}} &\approx (0.0007966843,\;0.0007976923,\;0.0007861267,\;0.0008002392).
\end{align}

For the SU(3)-commutator phase, the *per-mode* linear fits (slope/intercept for \(1/\lambda_i(t)\)) were printed explicitly:
\begin{align}
\alpha_1 &\approx 0.0007966843,\quad b_1 \approx 0.1165916863,\\
\alpha_2 &\approx 0.0007976923,\quad b_2 \approx 0.0990026600,\\
\alpha_3 &\approx 0.0007861267,\quad b_3 \approx 0.0892911905,\\
\alpha_4 &\approx 0.0008002392,\quad b_4 \approx 0.0807821716.
\end{align}

The key empirical “band” in these datasets is that once a Haar-like quadratic mass is present, \(\alpha_i\) cluster near \(\sim 7.8\times 10^{-4}\) across many distinct nonlinear add-ons, while a pure quadratic phase sits higher near \(\sim 1.0\times 10^{-3}\).

---

## Obstruction proxy based on a curvature threshold

Define a curvature threshold \(\kappa_\star>0\) and per-sample “defect”
\begin{equation}
\mathrm{defect} \;=\; \max(0,\;\kappa_\star-\lambda_{\min}).
\end{equation}

A Monte Carlo diagnostic then reports
\begin{equation}
\Phi_{\mathrm{proxy}} \;=\; \mathbb{E}\big[\max(0,\kappa_\star-\lambda_{\min})\big].
\end{equation}

One printed example used \(\kappa_\star=0.5\) and reported \(\Phi_{\mathrm{proxy}}\approx 0.193333\) together with \(E[\lambda_{\min}]\approx 7.53948\).

---

## Where this can go (theory-development hooks)

1. **Turn the Riccati diagnostic into a lemma**: identify hypotheses on \(S(t,\cdot)\) under which a mode-wise inequality
\(
\frac{d}{dt}\lambda_i \le -\alpha_i \lambda_i^2
\)
can be derived (even if \(\alpha_i\) is crude), then integrate to get a deterministic \(1/\lambda\) bound.

2. **Connect curvature bounds → functional inequalities**: if the evolved effective action stays uniformly convex in a suitable sense, one can aim for a Poincaré / log-Sobolev inequality (LSI), and therefore a spectral gap for the associated Langevin/Fokker–Planck operator. (This is the bridge from “curvature program” to “mass gap proxy”.)

3. **Explain the \(\alpha\)-band universality**: the empirical near-constancy of \(\alpha\) across a family of nonlinearities suggests the dominant driver is the quadratic (Haar-like) mass term and the grid/Laplacian discretization, with other terms subleading in the curvature decay rate in this regime.
