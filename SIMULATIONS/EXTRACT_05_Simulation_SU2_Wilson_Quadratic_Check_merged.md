---
title: "Simulation Note: SU(2) Wilson Action Matches the Discrete Curl Quadratic Form at Small Field"
date: "2025-12-29"
---

# Simulation note: SU(2) Wilson action $\approx$ quadratic curl energy

## Goal

The linearized analysis of the Wilson action near the identity predicts that, for small Lie-algebra fields,
the Wilson action is well-approximated by a quadratic form built from the discrete exterior derivative $d_1$:
\[
S_W(U)\ \approx\ \frac{\beta}{2}\sum_{p}\| (d_1 X)_p\|^2.
\]
This note provides a quick numerical check in the simplest setting:

- gauge group $SU(2)$,
- $2$d periodic lattice of size $L\times L$ (so plaquettes are well-defined and small),
- link variables parameterized as $U_{x,\mu} = \exp(i\,a_{x,\mu}\cdot\sigma)$ with $a_{x,\mu}\in\mathbb R^3$,
- Wilson action
\[
S_W = \beta\sum_{p}\Bigl(1-\tfrac12\mathrm{Tr}(U_p)\Bigr).
\]

We verify that $S_W/S_{\mathrm{quad}}\to 1$ as the field amplitude $\varepsilon\to 0$.

---

## Code (pure Python / NumPy)

```python
import numpy as np, math

# Pauli matrices
sigma = [
    np.array([[0,1],[1,0]], dtype=complex),
    np.array([[0,-1j],[1j,0]], dtype=complex),
    np.array([[1,0],[0,-1]], dtype=complex)
]
I2 = np.eye(2, dtype=complex)

def su2_exp(v):
    # Return SU(2) matrix exp(i v·sigma) for v in R^3.
    v = np.asarray(v, dtype=float)
    a = np.linalg.norm(v)
    if a < 1e-12:
        return I2.copy()
    n = v / a
    n_dot = n[0]*sigma[0] + n[1]*sigma[1] + n[2]*sigma[2]
    return math.cos(a)*I2 + 1j*math.sin(a)*n_dot

def su2_dag(U):
    return U.conj().T

def wilson_action_2d(Ulinks, beta=1.0, L=3):
    # Periodic LxL lattice, mu=0,1. Wilson action beta sum_p (1 - 1/2 Tr(U_p)).
    S=0.0
    for x in range(L):
        for y in range(L):
            U1 = Ulinks[(x,y,0)]
            U2 = Ulinks[((x+1)%L,y,1)]
            U3 = Ulinks[(x,(y+1)%L,0)]
            U4 = Ulinks[(x,y,1)]
            Up = U1 @ U2 @ su2_dag(U3) @ su2_dag(U4)
            tr = np.trace(Up).real
            S += beta*(1.0 - 0.5*tr)
    return float(S)

def quadratic_curl_action_2d(alinks, beta=1.0, L=3):
    # alinks are R^3 vectors a_{x,mu}; curl is a1+a2-a3-a4 at each plaquette.
    S=0.0
    for x in range(L):
        for y in range(L):
            a1 = alinks[(x,y,0)]
            a2 = alinks[((x+1)%L,y,1)]
            a3 = alinks[(x,(y+1)%L,0)]
            a4 = alinks[(x,y,1)]
            f = a1 + a2 - a3 - a4
            S += beta*0.5*np.dot(f,f)
    return float(S)

def random_alinks(L=3, scale=1.0, rng=None):
    if rng is None:
        rng = np.random.default_rng()
    alinks={}
    for x in range(L):
        for y in range(L):
            for mu in [0,1]:
                alinks[(x,y,mu)] = scale*rng.normal(size=3)
    return alinks

def build_Ulinks_from_alinks(alinks):
    return {k: su2_exp(v) for k,v in alinks.items()}

def experiment_ratios(eps_list, n_samples=500, L=3, beta=1.0, seed=2):
    rng=np.random.default_rng(seed)
    rows=[]
    for eps in eps_list:
        ratios=[]
        for _ in range(n_samples):
            base = random_alinks(L=L, scale=1.0, rng=rng)
            alinks = {k: eps*v for k,v in base.items()}
            Ulinks = build_Ulinks_from_alinks(alinks)
            S_exact = wilson_action_2d(Ulinks, beta=beta, L=L)
            S_quad  = quadratic_curl_action_2d(alinks, beta=beta, L=L)
            ratios.append(S_exact/S_quad)
        rows.append((eps, float(np.mean(ratios)), float(np.std(ratios))))
    return rows

print(experiment_ratios([0.2,0.1,0.05,0.02,0.01]))
```

---

## Results

For $L=3$, $\beta=1$, and $500$ random samples at each amplitude $\varepsilon$, the output is:

| $\varepsilon$ | mean $S_W/S_{\mathrm{quad}}$ | std |
|---:|---:|---:|
| 0.20 | 0.909 | 0.061 |
| 0.10 | 0.977 | 0.028 |
| 0.05 | 0.993 | 0.014 |
| 0.02 | 0.999 | 0.006 |
| 0.01 | 1.000 | 0.003 |

As expected, the ratio tends to $1$ as $\varepsilon\to 0$, consistent with the claim that
the quadratic part of the Wilson action is governed by the discrete curl $d_1$.

---

## Bonus: eigenvalues of $d_1^\ast d_1$ on a 2D torus

If one builds the matrix $D$ implementing $d_1$ on scalar cochains, then $D^T D$ is positive semidefinite.
On an $L\times L$ torus one finds:

- $\dim\ker(D)=L^2+1$ (one global constraint makes $\mathrm{rank}(D)=L^2-1$),
- the smallest positive eigenvalue scales like $4\sin^2(\pi/L)\sim (2\pi/L)^2$.

This is a useful reminder: **the Wilson Hessian alone does not give a volume-independent positive constant**.
In the curvature program, the volume-independent floor comes from Haar geometry (Ricci), not from $d_1^\ast d_1$.
