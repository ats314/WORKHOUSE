---
title: "EXTRACT 06 — Toy Numerical Check: Riccati Lower-Bound Dynamics"
project: "SWIM2"
source_files:
  - "SYNTH_P06_riccati_hessian_flow.md"
status: "toy simulation (reproducible)"
---

# Toy Numerical Check: Riccati Lower-Bound Dynamics

## Purpose

Several project arguments reduce a tensor flow to a scalar Riccati-type inequality for a minimum eigenvalue:

\[
\dot\lambda(t)\;\ge\; -2\lambda(t)^2 + \sigma(t).
\]

This note provides a **reproducible toy simulation** for the model ODE

\[
\dot\lambda(t)= -2\lambda(t)^2 + \sigma(t),
\]

to illustrate:

- convergence to a positive fixed point when \(\sigma(t)\equiv\sigma>0\) and the initial value is not too negative,
- finite-time blow-down for overly negative initial data (an important caveat for any comparison argument).

---

## 1. Constant forcing \(\sigma(t)\equiv 1\)

### Fixed point and analytic solution

For \(\sigma\equiv 1\), the stable fixed point is:

\[
\lambda_\ast = \sqrt{\frac{1}{2}} \approx 0.707106781186548.
\]

If \(|\lambda_0|<\lambda_\ast\), the solution can be written explicitly using \(\tanh\):

\[
\lambda(t)=\lambda_\ast \tanh\Big(\sqrt{2}\,t + \operatorname{arctanh}\big(\lambda_0/\lambda_\ast\big)\Big).
\]

If \(\lambda_0<-\lambda_\ast\), the solution blows down to \(-\infty\) in finite time:

\[
t_{\mathrm{blow}}=\frac{1}{\sqrt{2}}\operatorname{arccoth}\Big(\frac{|\lambda_0|}{\lambda_\ast}\Big).
\]

---

### Numerical results at \(t=10\)

Using an adaptive Runge–Kutta solver:

| initial \(\lambda_0\) | \(\lambda(10)\) |
|---:|---:|
|  -0.6 | 0.707106781177567 |
|   0.0 | 0.707106781185812 |
|   1.0 | 0.707106781186674 |
|   2.0 | 0.707106781186899 |

All converge extremely close to \(\lambda_\ast\), as expected.

---

### Blow-down example (\(\lambda_0=-1\))

Here \(\lambda_0=-1<-\lambda_\ast\), so the solution decreases without bound.

Analytic blow-down time:

\[
t_{\mathrm{blow}} \approx 0.623225240.
\]

Numerically, the trajectory reaches \(\lambda(t)=-10^6\) at approximately:

\[
t \approx 0.623224740.
\]

This matters because any PBH/Riccati comparison argument must ensure the relevant eigenvalue lower bound does **not** start too negative (or that diffusion/geometry prevents the global minimum from following this blow-down).

---

## 2. Time-dependent forcing example \(\sigma(t)=1+0.5\sin t\)

For \(\lambda(0)=0\), the same ODE produces a bounded, oscillatory solution that tracks the moving instantaneous fixed point \(\sqrt{\sigma(t)/2}\) with lag.

Numerically:

| \(t\) | \(\lambda(t)\) |
|---:|---:|
|    0 | 0.000000000 |
|    2 | 0.856302983 |
|    5 | 0.521816015 |
|   10 | 0.666649469 |
|   20 | 0.822637635 |

---

## 3. Minimal Python code (copy/paste)

```python
import numpy as np
from scipy.integrate import solve_ivp

def rhs_const(t, y, sigma=1.0):
    lam = y[0]
    return [-2.0*lam**2 + sigma]

def rhs_time(t, y):
    lam = y[0]
    sigma = 1.0 + 0.5*np.sin(t)
    return [-2.0*lam**2 + sigma]

# constant sigma example
lam0 = 0.0
sol = solve_ivp(lambda t,y: rhs_const(t,y,1.0), (0,10), [lam0], t_eval=[10],
                rtol=1e-10, atol=1e-12, max_step=0.01)
print(sol.y[0,-1])

# time-dependent sigma example
t_points = [0,2,5,10,20]
sol2 = solve_ivp(rhs_time, (0,max(t_points)), [0.0], t_eval=t_points,
                 rtol=1e-10, atol=1e-12, max_step=0.01)
print(list(zip(sol2.t, sol2.y[0])))
```

