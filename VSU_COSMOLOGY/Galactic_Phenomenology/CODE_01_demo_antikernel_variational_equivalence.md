# CODE_01 — Anti-kernel Hankel rule from a local operator inverse (toy numeric check)

Generated: 2026-01-01 01:41:14 UTC

## Purpose

Numerical sanity check (toy model): demonstrate that the Hankel-space multiplier

\[
\widehat g_{\mu}(k) = \left(1 + \frac{\mu^2}{k^2}\right)\widehat g_b(k)
\]

(order-1 Hankel channel) is equivalent (modulo IR regularization and boundary conditions) to a local real-space representation

\[
g_\mu(r)=g_b(r)+\mu^2\,\chi(r),
\qquad
\mathcal L_1\chi = g_b,
\]

with the order-1 Bessel operator

\[
\mathcal L_1 := -\left(\frac{d^2}{dr^2}+\frac{1}{r}\frac{d}{dr}-\frac{1}{r^2}\right).
\]

This file embeds the exact Python script used for the check and the default run output.

## Dependencies

- `numpy`
- `scipy` (`scipy.special`, `scipy.sparse`, `scipy.sparse.linalg`)

## Code

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CODE_demo_antikernel_variational_equivalence.py

Toy numerical sanity check:

Hankel-space rule (order-1):
    ghat_mu(k) = (1 + mu^2/k^2) ghat_b(k)

is equivalent (up to boundary conditions / IR regularization) to the local real-space form:
    g_mu(r) = g_b(r) + mu^2 * chi(r),
where chi solves the order-1 Bessel operator equation
    L1 chi = g_b
with
    L1 := - (d^2/dr^2 + (1/r) d/dr - (1/r^2)).

This is not a SPARC run; it is a toy demonstration of operator equivalence.
"""

import numpy as np
from scipy.special import j1
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


def hankel1_forward(f_r: np.ndarray, r: np.ndarray, k: np.ndarray) -> np.ndarray:
    """F(k) = integral dr * r * f(r) * J1(k r) (truncated, trapezoid)."""
    dr = r[1] - r[0]
    rr = r[:, None]
    kk = k[None, :]
    J = j1(rr * kk)
    return ((r * f_r)[:, None] * J).sum(axis=0) * dr


def hankel1_inverse(F_k: np.ndarray, k: np.ndarray, r: np.ndarray) -> np.ndarray:
    """f(r) = integral dk * k * F(k) * J1(k r) (truncated, trapezoid)."""
    dk = k[1] - k[0]
    rr = r[:, None]
    kk = k[None, :]
    J = j1(rr * kk)
    return ((k * F_k)[None, :] * J).sum(axis=1) * dk


def solve_L1_inverse(gb: np.ndarray, r: np.ndarray) -> np.ndarray:
    """
    Solve L1 chi = gb on r in [0, R] with chi(0)=0, chi(R)=0 (toy BCs).

    L1 = - (d2 + (1/r)d - (1/r^2)).
    """
    dr = r[1] - r[0]

    # interior points
    ri = r[1:-1]
    n = len(ri)

    lower = -(1.0 / dr**2) + 1.0 / (2.0 * dr * ri)
    main  =  (2.0 / dr**2) + 1.0 / (ri**2)
    upper = -(1.0 / dr**2) - 1.0 / (2.0 * dr * ri)

    A = diags([lower[1:], main, upper[:-1]], offsets=[-1, 0, 1], format="csc")
    b = gb[1:-1].copy()

    chi_int = spsolve(A, b)

    chi = np.zeros_like(gb)
    chi[1:-1] = chi_int
    chi[0] = 0.0
    chi[-1] = 0.0
    return chi


def main():
    # Toy baryonic acceleration profile
    Rmax = 50.0
    Nr = 4096
    r = np.linspace(1e-6, Rmax, Nr)
    r0 = 3.0
    gb = np.exp(-r / r0)  # arbitrary smooth test function

    # Hankel grids
    Kmax = 25.0
    Nk = 4096
    k = np.linspace(0.0, Kmax, Nk)
    k_ir = np.pi / Rmax  # geometry-motivated IR regulator

    mu = 0.10  # toy value, in same units as k (1/length)

    # Hankel anti-kernel computation (with IR-regulated pole)
    gb_hat = hankel1_forward(gb, r, k)
    M = 1.0 + (mu**2) / (k**2 + k_ir**2)
    gmu_h = hankel1_inverse(gb_hat * M, k, r)

    # Local PDE form: g_mu = g_b + mu^2 * L1^{{-1}} g_b
    chi = solve_L1_inverse(gb, r)
    gmu_p = gb + (mu**2) * chi

    # Compare on the domain away from the boundaries
    mask = (r > 0.5) & (r < 0.9 * Rmax)
    num = np.linalg.norm((gmu_h - gmu_p)[mask])
    den = np.linalg.norm(gmu_h[mask])
    rel = num / (den + 1e-30)

    print("Toy anti-kernel equivalence check")
    print(f"mu = {{mu:.4f}}, Rmax = {{Rmax}}, k_ir = pi/Rmax = {{k_ir:.6f}}")
    print(f"Relative L2 error (interior region): {{rel:.3e}}")
    print(f"Max abs diff (interior region): {{np.max(np.abs(gmu_h - gmu_p)[mask]):.3e}}")


if __name__ == "__main__":
    main()
```

## Default run output (this environment)

```text
Toy anti-kernel equivalence check
mu = 0.1000, Rmax = 50.0, k_ir = pi/Rmax = 0.062832
Relative L2 error (interior region): 2.054e-02
Max abs diff (interior region): 1.639e-02
```
