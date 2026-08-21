# Reflection positivity stress test (numerical): a practical experiment design

## Goal

The lattice Wilson gauge action is known to be reflection positive, but in this project the reflection-positivity (RP) property is also used as a conceptual bridge toward OS reconstruction and mass-gap statements.

A practical way to de-risk the analytic program is to implement a **numerical RP stress test**:

> Sample gauge fields from the lattice Yang--Mills measure and empirically check that the RP Gram matrix
> \[
> G_{ij} := \langle \Theta F_i \cdot F_j\rangle
> \]
> is positive semidefinite for a reasonably rich set of test observables $\{F_i\}$ supported in the positive-time half-lattice.

This does *not* prove RP (which is exact), but it can catch implementation errors in:
- coordinate conventions,
- reflection map conventions,
- time-slice factorization,
- transfer matrix reconstruction,
- and gauge-fixing / projector choices.

---

## 1. The RP Gram matrix

Fix a reflection hyperplane (e.g. time reflection $t\mapsto 1-t$ across a midplane). Let $\Theta$ act on gauge fields by:

1. reflecting the lattice sites $x=(t,\vec x)\mapsto \theta x$,
2. mapping each link variable $U_{x,\mu}$ to the corresponding reflected link,
3. inverting time-like links appropriately so that oriented Wilson loops reflect to oriented Wilson loops,
4. complex conjugation if needed.

For an observable $F$ supported in the positive half-space, RP says:
\[
\langle \Theta F \cdot F\rangle_{\mu} \ge 0.
\]

Equivalently, for any finite set $\{F_i\}$ supported in the positive half-space, the matrix
\[
G_{ij} := \langle \Theta F_i \cdot F_j\rangle_\mu
\]
is positive semidefinite.

---

## 2. Choice of test observables

Good stress-test observables should be:

- gauge invariant,
- localized near the reflection plane (to probe subtle sign conventions),
- nontrivial (not all commuting / redundant),
- low-cost to evaluate.

Examples:

1. **Spatial plaquettes** at a fixed positive time slice:
   \[
   F_p(U) := \Re\Tr(U_{p}),
   \]
   with $p$ a plaquette lying entirely in the $t=1$ slice.

2. **Short rectangles / chair loops** in the positive half.

3. **Polyakov lines** restricted to half-time extent (careful: not fully gauge invariant unless closed appropriately).

4. **Characters** $\chi_j(U_p)$ (for $SU(2)$, use spin-$j$ characters) to probe nonlinear combinations.

Pragmatically: start with 5--20 observables.

---

## 3. Sampling gauge fields

Two acceptable samplers for a small-lattice stress test:

- **Metropolis updates** on each link with local staple recomputation.
- **SU(2) heatbath** (faster / more standard, but more code).

For $SU(2)$, representing group elements as unit quaternions is convenient.

---

## 4. What to check empirically

Given $N$ sampled configurations $U^{(k)}$:

1. Estimate Gram entries
   \[
   \widehat G_{ij} = \frac{1}{N}\sum_{k=1}^N \bigl(\Theta F_i\bigr)\!\left(U^{(k)}\right)\, F_j\!\left(U^{(k)}\right).
   \]
2. Compute eigenvalues of $\widehat G$.
3. RP predicts all eigenvalues $\ge 0$; finite-sample noise produces small negative eigenvalues with magnitude shrinking like $N^{-1/2}$.

A practical diagnostic:
- repeat for increasing $N$ and confirm the most-negative eigenvalue drifts upward toward $0$.

---

## 5. Minimal Python skeleton (SU(2), Metropolis)

Below is a deliberately minimal (not optimized) skeleton illustrating the structure. It omits many performance improvements but is useful as a correctness scaffold.

```python
import numpy as np

# --- SU(2) as unit quaternions q=(a0,a1,a2,a3), |q|=1
def su2_random(rng):
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    return v

def su2_mul(q, r):
    a0,a1,a2,a3 = q
    b0,b1,b2,b3 = r
    return np.array([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ])

def su2_inv(q):
    a0,a1,a2,a3 = q
    return np.array([a0,-a1,-a2,-a3])

def su2_retr(q):
    # Re Tr(U) for SU(2) matrix is 2*a0 for quaternion convention
    return 2.0*q[0]

# --- Lattice indexing utilities omitted for brevity ---
# You need:
#   - neighbor(x,mu)
#   - list of plaquettes containing a link
#   - compute_plaquette(U, x, mu, nu) -> SU(2) element

def metropolis_sweep(U, beta, eps, rng):
    # For each link ℓ:
    #  - compute staple S(ℓ)
    #  - propose U' = R * U with R near identity
    #  - accept with prob min(1, exp(-(ΔS)))
    pass

def reflect_config(U):
    # Implement Θ acting on link fields (time reflection + inversion of time links)
    pass

def observable_F_i(U):
    # e.g. list of spatial plaquette traces at t=1
    pass

def stress_test(U_samples, F_list):
    # build Gram matrix G_ij = < ΘF_i * F_j >
    pass
```

---

## 6. Interpretation and failure modes

If you see persistent negative eigenvalues well below the sampling noise floor, likely causes are:

- reflection map $\Theta$ is implemented incorrectly (orientation/inversion of time links is the classic gotcha),
- observables are not actually supported strictly in the positive half,
- gauge fixing / projection is breaking RP,
- numerical sampler not equilibrated (bad burn-in).

---

## Provenance in this project

This experiment design is extracted from:

- `Reflection Positivity Stress Test.txt` (the proposed Gram-matrix stress test and small-lattice plan).

No Monte Carlo results are included here; the only executed numerics in this project snapshot are the $SU(3)$ Haar Hessian scans in `su3_haar_hessian_scan.py`.

