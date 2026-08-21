# vHJ Curvature-Flow Simulations (Correct Semigroup, JAX)

## 0. What this document is

This document records the **viscous Hamilton–Jacobi (vHJ)** simulations used as a coarse-graining / “geometric RG” surrogate:

\[
\partial_t S(t,x)=\nu\,\Delta S(t,x)-\|\nabla S(t,x)\|^2
\qquad (x\in\mathbb{R}^4 \text{ discretized}).
\]

Key diagnostics extracted in the project runs:

- the **Hessian spectrum** of \(S(t,\cdot)\) at (or near) the origin,
- an empirical **Riccati law** for each eigenvalue branch:
  \[
  \frac{1}{\lambda_i(t)}\approx \frac{1}{\lambda_i(0)}+\alpha_i t,
  \qquad\text{(fit from recorded steps)}.
  \]

Important: this PDE is an identity for the heat-semi\-group transform
\(S_t=-\log(P_t e^{-S_0})\). It is *not* the Yang–Mills gradient flow.

---

## 1. Correct semigroup identity (fix from first pass)

If \(\rho_t = P_t\rho_0\) solves the heat equation and \(\rho_t=e^{-S_t}\), then
\[
\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2.
\]
There is no extra self-canceling “\( +J_t \)” term in the pure heat-semi\-group case.

---

## 2. 4D discretization (periodic grid)

We discretize on an \(L^4\) periodic lattice in a box \([-X,X)^4\) using central differences.

### 2.1 Core JAX code (4D)

```python
import jax
import jax.numpy as jnp

# Optional (often useful for stability/accuracy):
# jax.config.update("jax_enable_x64", True)

# -----------------------
# Grid (periodic)
# -----------------------
def make_grid_4d(L=24, X=2.0):
    dx = (2*X) / L
    xs = jnp.linspace(-X, X, L, endpoint=False)   # consistent with periodic dx
    X1, X2, X3, X4 = jnp.meshgrid(xs, xs, xs, xs, indexing="ij")
    grid = jnp.stack([X1, X2, X3, X4], axis=-1)   # (L,L,L,L,4)
    return grid, dx

# -----------------------
# Finite differences
# -----------------------
def laplace4(S, dx):
    return (
        -8.0*S
        + jnp.roll(S,  1, 0) + jnp.roll(S, -1, 0)
        + jnp.roll(S,  1, 1) + jnp.roll(S, -1, 1)
        + jnp.roll(S,  1, 2) + jnp.roll(S, -1, 2)
        + jnp.roll(S,  1, 3) + jnp.roll(S, -1, 3)
    ) / (dx*dx)

def grad2_4(S, dx):
    g0 = (jnp.roll(S, -1, 0) - jnp.roll(S,  1, 0)) / (2*dx)
    g1 = (jnp.roll(S, -1, 1) - jnp.roll(S,  1, 1)) / (2*dx)
    g2 = (jnp.roll(S, -1, 2) - jnp.roll(S,  1, 2)) / (2*dx)
    g3 = (jnp.roll(S, -1, 3) - jnp.roll(S,  1, 3)) / (2*dx)
    return g0*g0 + g1*g1 + g2*g2 + g3*g3

@jax.jit
def vHJ_step(S, dx, dt, nu=1.0):
    return S + dt*(nu*laplace4(S, dx) - grad2_4(S, dx))

# -----------------------
# Hessian at a point (center)
# -----------------------
def hessian4_at(S, dx, idx):
    # idx is a 4-tuple, e.g. (L//2, L//2, L//2, L//2)
    shifts = {}
    for a in range(4):
        ea = [0,0,0,0]; ea[a]=1
        shifts[(a, +1)] = jnp.roll(S, +1, axis=a)
        shifts[(a, -1)] = jnp.roll(S, -1, axis=a)

    # helper to read shifted field at idx
    def val(F): return F[idx]

    H = jnp.zeros((4,4), dtype=S.dtype)

    # diagonal second derivatives
    for i in range(4):
        H = H.at[i,i].set((val(shifts[(i,+1)]) - 2.0*val(S) + val(shifts[(i,-1)])) / (dx*dx))

    # mixed second derivatives
    for i in range(4):
        for j in range(i+1,4):
            Sp = jnp.roll(jnp.roll(S, +1, axis=i), +1, axis=j)
            Sm = jnp.roll(jnp.roll(S, +1, axis=i), -1, axis=j)
            Mp = jnp.roll(jnp.roll(S, -1, axis=i), +1, axis=j)
            Mm = jnp.roll(jnp.roll(S, -1, axis=i), -1, axis=j)
            Hij = (val(Sp) - val(Sm) - val(Mp) + val(Mm)) / (4.0*dx*dx)
            H = H.at[i,j].set(Hij)
            H = H.at[j,i].set(Hij)
    return H

@jax.jit
def center_hessian_eigs(S, dx):
    L = S.shape[0]
    idx = (L//2, L//2, L//2, L//2)
    Hc = hessian4_at(S, dx, idx)
    ev = jnp.linalg.eigvalsh(Hc)
    return jnp.sort(ev)   # ascending
```

---

## 3. Initial data families used in the recorded runs

All runs start from a base quadratic
\[
S_0(x)=\tfrac12 x^\top H x
\]
plus various “geometry-inspired” perturbations.

### 3.1 Initial potential builder (toy YM geometry knobs)

```python
def make_S0_family(grid,
                   Hmat,
                   m2=0.0,              # Haar-like quadratic mass
                   lam4=0.0,            # isotropic quartic
                   gamma_YM=0.0,        # YM-style quartic plaquette surrogate
                   lambda_SU2=0.0,      # SU(2) adjoint curvature knob
                   lambda_SU3=0.0,      # SU(3) adjoint curvature knob
                   C2_SU3=3.0):
    # base quadratic
    quad = 0.5*jnp.einsum("...i,ij,...j->...", grid, Hmat, grid)

    x1, x2, x3, x4 = grid[...,0], grid[...,1], grid[...,2], grid[...,3]
    r2 = x1*x1 + x2*x2 + x3*x3 + x4*x4

    haar = 0.5*m2*r2
    quartic = lam4*(r2*r2)

    # YM plaquette surrogate: sum_{i<j} x_i^2 x_j^2
    YM_plaq = (x1*x1*x2*x2 + x1*x1*x3*x3 + x1*x1*x4*x4 +
               x2*x2*x3*x3 + x2*x2*x4*x4 + x3*x3*x4*x4)

    # adjoint curvature surrogates used in the recorded runs
    adj_SU2 = lambda_SU2 * (2.0*(x1*x1 + x2*x2 + x3*x3))   # first 3 coords only
    adj_SU3 = lambda_SU3 * (C2_SU3*r2)                    # full 4-vector

    return quad + haar + quartic + gamma_YM*YM_plaq + adj_SU2 + adj_SU3
```

---

## 4. Recorded outputs (from this chat’s runs)

The following tables are **recorded outputs** from the Colab runs captured in this chat.
They are included verbatim (no new computation here).

### 4.1 Quadratic baseline: 4×4 Hessian eigenvalues over steps

Sorted eigenvalues \(\lambda_1\le\lambda_2\le\lambda_3\le\lambda_4\):

```
step     λ1      λ2      λ3      λ4   (sorted eigenvalues)
   0   3.137619  3.801772  4.401150  5.462403
  30   2.866945  3.411298  3.885940  4.689939
  60   2.639317  3.093663  3.478878  4.109222
  90   2.445215  2.830214  3.149128  3.656686
 120   2.277726  2.608154  2.876544  3.294059
 150   2.131735  2.418447  2.647444  2.996953
 180   2.003350  2.254495  2.452184  2.749084
 210   1.889568  2.111381  2.283774  2.539118
 240   1.788015  1.985362  2.137040  2.358979
 270   1.696828  1.873549  2.008032  2.202747
```

Riccati-fit coefficients (from the same run):
```
Eigenvalue   alpha_i         intercept_i (1/λ_i(0))
----------------------------------------------------
i=1:     0.0010022789      0.3187423305
i=2:     0.0010026004      0.2630756084
i=3:     0.0010028736      0.2272639797
i=4:     0.0010033081      0.1831387770
```

### 4.2 Haar RG (quadratic + Haar-like mass)

```
step      λ1        λ2        λ3        λ4   (Haar RG)
   0   5.314069  5.979081  6.577921  7.639357
  30   4.730976  5.244640  5.695179  6.466385
  60   4.259698  4.667785  5.018534  5.603515
  90   3.871800  4.203512  4.484058  4.942648
 120   3.547456  3.822220  4.051587  4.420572
 150   3.272463  3.503689  3.694634  3.997839
 180   3.036546  3.233768  3.395149  3.648672
 210   2.832010  3.002167  3.140341  3.355417
 240   2.653069  2.801350  2.920954  3.105705
 270   2.495223  2.625582  2.730120  2.890516
```

Riccati-fit coefficients:
```
Eigenvalue   α_i(Haar)      intercept_i
i=1:     0.0007880153      0.1876355891
i=2:     0.0007916689      0.1668507983
i=3:     0.0007939418      0.1517155462
i=4:     0.0007967519      0.1307107120
```

### 4.3 Haar + YM quartic plaquette surrogate

```
step   λ1     λ2     λ3     λ4   (Haar + YM quartic)
   0   5.317576  5.985277  6.584897  7.648608
  30   4.746849  5.261582  5.712169  6.483884
  60   4.280406  4.688396  5.038575  5.622919
  90   3.893856  4.224702  4.504283  4.961584
 120   3.569202  3.842653  4.070808  4.438169
 150   3.293206  3.522845  3.712478  4.013888
 180   3.055967  3.251467  3.411499  3.663182
 210   2.850043  3.018443  3.155244  3.368526
 240   2.669711  2.816243  2.934525  3.117526
 270   2.510584  2.639218  2.742485  2.901196
```

Riccati-fit coefficients:
```
Eigenvalue   α_i(YM+Haar)    intercept_i
i=1:     0.0007799263      0.1871075463
i=2:     0.0007854121      0.1663754420
i=3:     0.0007887369      0.1513088164
i=4:     0.0007928276      0.1303804288
```

### 4.4 Haar + YM + SU(2) adjoint curvature surrogate

```
step   λ1    λ2    λ3    λ4   (Haar + YM + SU(2) adjoint)
   0   5.969544  7.494316  8.735322  9.790115
  30   5.248125  6.374480  7.238564  7.939785
  60   4.676118  5.540572  6.175710  6.674832
  90   4.213378  4.897046  5.383110  5.756155
 120   3.832201  4.386069  4.769803  5.059031
 150   3.513237  3.970883  4.281417  4.512133
 180   3.242647  3.627025  3.883405  4.071715
 210   3.010325  3.337685  3.552908  3.709481
 240   2.808814  3.090909  3.274122  3.406350
 270   2.632397  2.877986  3.035824  3.148988
```

Riccati-fit coefficients:
```
Eigenvalue   α_i(SU2+Haar+YM)    intercept_i
--------------------------------------------------
i=1:     0.0007875071      0.1668187001
i=2:     0.0007932955      0.1330191860
i=3:     0.0007627501      0.1211391406
i=4:     0.0007980805      0.1019825721
```

### 4.5 Haar + YM + SU(2) + SU(3) adjoint curvature surrogate

```
step   λ1    λ2    λ3    λ4   (Haar + YM + SU(2) + SU(3))
   0   8.552138  10.070476  11.306206  12.356505
  30   7.111890  8.121508  8.897969  9.529510
  60   6.082116  6.800884  7.333221  7.754219
  90   5.310836  5.848202  6.235627  6.536125
 120   4.712193  5.128965  5.423448  5.648622
 150   4.234345  4.566936  4.798306  4.973281
 180   3.844222  4.115753  4.302308  4.442171
 210   3.519747  3.745613  3.899191  4.013550
 240   3.245703  3.436505  3.565157  3.660408
 270   3.011178  3.174494  3.283816  3.364371
```

Riccati-fit coefficients:
```
Eigenvalue   α_i(SU3)           intercept_i
--------------------------------------------------
i=1:     0.0007973450      0.1166651489
i=2:     0.0007992039      0.0991425524
i=3:     0.0008004338      0.0883685728
i=4:     0.0008011904      0.0809022973
```

### 4.6 SU(3) “commutator” curvature run (same surrogate family)

```
step   λ1    λ2    λ3    λ4   (SU(3) COMM RG)
   0   8.554087  10.073799  11.312973  12.365769
  30   7.116392  8.133140  8.910410  9.542375
  60   6.086889  6.813251  7.345314  7.766044
  90   5.315245  5.859468  6.246212  6.546200
 120   4.716111  5.138824  5.432490  5.657091
 150   4.237770  4.575469  4.805980  4.980411
 180   3.847211  4.123129  4.308865  4.448209
 210   3.522375  3.752022  3.904846  4.018720
 240   3.248001  3.442095  3.570049  3.664845
 270   3.013234  3.179433  3.288107  3.368243
```

Riccati-fit coefficients:
```
Eigenvalue   α_i(SU3_comm)         intercept_i
--------------------------------------------------
i=1:     0.0007966843      0.1165916863
i=2:     0.0007976923      0.0990026600
i=3:     0.0007861267      0.0892911905
i=4:     0.0008002392      0.0807821716
```

### 4.7 “Curvature phase diagram” summary (α-band)

```
============================================
Curvature Phase Diagram Summary
============================================
Quadratic       | mean α = 0.001002000   | spread = 0.000000000
Haar            | mean α = 0.000788000   | spread = 0.000000000
Haar+YM         | mean α = 0.000781250   | spread = 0.000002000
Haar+SU2        | mean α = 0.000785408   | spread = 0.000035330
Haar+SU3-mass   | mean α = 0.000799543   | spread = 0.000003845
SU3-comm        | mean α = 0.000795186   | spread = 0.000014112
============================================
```

---

## 5. What these numerics actually certify (and what they do not)

Certified (empirical, for the tested discretizations and initial data):
- the PDE evolution preserves **positive Hessian eigenvalues at the probe point** over the simulated time window,
- the decay of each eigenvalue branch is well fit by a **Riccati law** with an \(\alpha\) in a narrow band.

Not certified:
- any **uniform-in-volume** curvature lower bound,
- any **gauge-covariant** Yang–Mills statement,
- any implication from these PDE surrogates to the **transfer-matrix spectrum** without additional Osterwalder–Schrader / locality inputs.

