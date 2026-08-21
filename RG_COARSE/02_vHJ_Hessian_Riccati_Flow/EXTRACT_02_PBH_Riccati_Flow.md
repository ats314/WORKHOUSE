---
title: "EXTRACT 02 — PBH / Riccati Hessian Flow: A Comparison Principle that Turns Curvature into a Gap"
date: "2025-12-31"
---

# Executive summary

A core engine in the archive is the observation that a “Projected Bochner–Hessian” evolution
drives Hessians by a **Riccati‑type** mechanism:
\[
  \dot H \approx -H^2 + \Sigma_{\mathrm{eff}},
\]
where $\Sigma_{\mathrm{eff}}$ collects curvature and “source/anomaly” contributions.

If one can prove $\Sigma_{\mathrm{eff}}\ge\sigma_\*>0$ on the physical (horizontal) directions,
then the smallest eigenvalue of $H$ satisfies a scalar Riccati inequality
\[
  \dot h \ \ge\ -h^2 + \sigma_\*,
\]
which has an explicit, globally stable lower bound.
That is the algebraic heart of “gap persistence”.

This extract is based on:

- `SYNTH_P06_riccati_hessian_flow.md`
- `SYNTH_P17_trace_bound.md`
- (linked motivation) `SYNTH_P20_stratified_parabolic_principle.md`

# 1. Scalar Riccati comparison lemma

Consider the scalar ODE
\[
  \dot h(t) = -h(t)^2 + \sigma(t).
\]

A theorem in the archive (in “primed” form) states that if
\[
  \sigma(t)\ge \sigma_\*>0 \quad\text{for all }t,
\]
then the solution satisfies:

- **Uniform positivity / stabilization**: $h(t)$ is pushed toward $+\sqrt{\sigma_\*}$,
  and cannot drift to $0$ once it is positive.
- **Explicit bound**: for constant $\sigma(t)=\sigma_\*$,
  \[
    h(t)=\sqrt{\sigma_\*}\,\tanh\!\left(\sqrt{\sigma_\*}\,t+\operatorname{arctanh}\frac{h_0}{\sqrt{\sigma_\*}}\right)
    \quad\text{if }h_0<\sqrt{\sigma_\*},
  \]
  and a corresponding $\coth$ formula if $h_0>\sqrt{\sigma_\*}$.

The point is not the hyperbolic functions; the point is that the Riccati nonlinearity
converts a **positive source** into a **positive fixed point**.

# 2. Matrix version: smallest eigenvalue inequality

Suppose $H(t)$ is a symmetric matrix solving
\[
  \dot H = -H^2 + S(t),
\qquad S(t)=S(t)^\top,
\]
and define $h(t)=\lambda_{\min}(H(t))$ and $\sigma(t)=\lambda_{\min}(S(t))$.
Then (under mild nondegeneracy assumptions, or in viscosity/min–max form)
\[
  \dot h(t)\ \ge\ -h(t)^2 + \sigma(t).
\]

So a lower bound $S(t)\ge \sigma_\*\mathrm{Id}$ implies $h(t)$ obeys the scalar Riccati lower bound,
hence $H(t)$ remains uniformly positive definite and stabilizes.

# 3. Why this matters in the SWIM2 chain

The earlier “geometric mass” result (Extract 01) is precisely the kind of statement
that would supply a *uniform positive lower bound* for a source term:
\[
  \mathrm{Ric}_g + \beta \nabla^2 S_W \ \ge\ (\kappa+\beta c_W)\,g
\]
on horizontals.

If $\Sigma_{\mathrm{eff}}$ in the PBH evolution can be identified with that Bakry–Émery tensor
(or controlled below by it), then the Riccati mechanism produces a hard analytic floor for the Hessian.
That floor is the functional‑analytic cousin of a “mass gap”.

# 4. Toy numerics: noncommuting source $S$

The following numerical experiment is not a claim about Yang–Mills;
it is a sanity check of the **comparison inequality** in a genuinely noncommuting matrix flow.

We integrate, for $n=6$,
\[
  \dot H = -H^2 + S,
\]
with $S>0$ symmetric but chosen so that $[H(0),S]\neq 0$.

## 4.1 Code (Python)

```python
import numpy as np, math

np.random.seed(0)

def random_orthonormal(n):
    A = np.random.randn(n, n)
    Q, R = np.linalg.qr(A)
    if np.linalg.det(Q) < 0:
        Q[:,0] *= -1
    return Q

n = 6
Q = random_orthonormal(n)
diag = np.linspace(1.5, 3.0, n)     # min eigenvalue = 1.5
S = Q @ np.diag(diag) @ Q.T

A = np.random.randn(n, n)
H = A.T @ A
H = H / np.linalg.norm(H, ord=2)
H += 0.3*np.eye(n)

sigma_star = np.linalg.eigvalsh(S)[0]
h0 = np.linalg.eigvalsh(H)[0]

def rhs(H):
    return -(H @ H) + S

def rk4_step(H, dt):
    k1 = rhs(H)
    k2 = rhs(H + 0.5*dt*k1)
    k3 = rhs(H + 0.5*dt*k2)
    k4 = rhs(H + dt*k3)
    Hn = H + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
    return 0.5*(Hn + Hn.T)

sqrt_sigma = math.sqrt(sigma_star)

def scalar_lower(t):
    return sqrt_sigma*math.tanh(sqrt_sigma*t + math.atanh(h0/sqrt_sigma))

dt = 1e-3
T  = 2.0
steps = int(T/dt)

rows = []
for i in range(steps+1):
    t = i*dt
    if i % 200 == 0:                  # every 0.2
        h = np.linalg.eigvalsh(H)[0]
        rows.append((t, h, scalar_lower(t), h-scalar_lower(t)))
    if i < steps:
        H = rk4_step(H, dt)

for r in rows:
    print(r)
```

## 4.2 Output (selected times)

|   t |   lambda_min(H(t)) |   scalar_lower_bound |      gap |
|----:|-------------------:|---------------------:|---------:|
| 0   |           0.300541 |             0.300541 | 0        |
| 0.2 |           0.657124 |             0.561585 | 0.095539 |
| 0.4 |           0.873585 |             0.770838 | 0.102747 |
| 0.6 |           1.01439  |             0.925138 | 0.089248 |
| 0.8 |           1.10051  |             1.03205  | 0.068464 |
| 1   |           1.15129  |             1.10297  | 0.048319 |
| 1.2 |           1.18094  |             1.14867  | 0.032268 |
| 1.4 |           1.19838  |             1.17757  | 0.020814 |
| 1.6 |           1.20877  |             1.19562  | 0.013147 |
| 1.8 |           1.21502  |             1.20682  | 0.008201 |
| 2   |           1.21881  |             1.21373  | 0.005078 |

As expected, $\lambda_{\min}(H(t))$ stays **above** the scalar Riccati lower bound built from
$\sigma_\*=\lambda_{\min}(S)$ and the initial value $h(0)$.

# 5. What remains hard

1. **Identify $\Sigma_{\mathrm{eff}}$ correctly**  
   In the project, $\Sigma_{\mathrm{eff}}$ is a combination of horizontal curvature,
   measure Jacobians, and RG/flow anomalies.  
   The Riccati mechanism only needs a lower bound, but it must be the *right* object.

2. **Upgrade from ODE to PDE on configuration space**  
   The matrix ODE is a cartoon. The real PBH evolution is a parabolic inequality on
   a stratified infinite‑dimensional space, which is why the archive develops
   a stratified maximum principle (Extract 04).

3. **Uniformity across scales**  
   For a mass gap, $\sigma_\*$ must not decay as lattice spacing goes to zero.

