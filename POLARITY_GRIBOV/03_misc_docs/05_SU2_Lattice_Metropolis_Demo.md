# Minimal 4D SU(2) Wilson Metropolis demo (NumPy): plaquette statistics and “large-angle” rarity

The repository contains JAX-based Monte Carlo scripts (e.g. `analysis_mc_defects.py`, `analysis_lattice_mc.py`). fileciteturn1file8 fileciteturn2file0  
Those scripts do not run in this environment because `jaxlib` is unavailable, so I wrote a small **NumPy** Metropolis implementation to extract at least a sanity-check dataset.

This is not a production lattice code. It’s a tiny pedagogical simulator:
- lattice size \(L=3\) in \(d=4\) (so \(3^4=81\) sites),
- local Metropolis updates with small SU(2) rotations,
- measurements of the **average plaquette** and the fraction of plaquettes with “large” group angle.

---

## 1. Observable definitions

### Wilson action (standard)
\[
S = -\frac{\beta}{2}\sum_{p}\mathrm{Re}\,\mathrm{Tr}(U_p).
\]

### Average plaquette
\[
\langle P\rangle := \left\langle \frac{1}{2}\mathrm{Re}\,\mathrm{Tr}(U_p)\right\rangle.
\]

### “Large-angle plaquette” rate
For each plaquette matrix \(U_p\in SU(2)\), define its group angle by
\[
\frac{1}{2}\mathrm{Re}\,\mathrm{Tr}(U_p)=\cos\theta_p,\qquad \theta_p\in[0,\pi].
\]
Then define a crude “defect” indicator
\[
\mathbf{1}\{\theta_p>\pi/2\}.
\]
This is a simple proxy for “plaquette far from identity.”

(Important: link angles are gauge dependent; plaquette angles are gauge invariant. For convexity-in-exponential-coordinates arguments, gauge fixing probably matters, but plaquettes are the safe first diagnostic.)

---

## 2. Results (L=3 demo)

Each row below used:
- 30 thermalization sweeps,
- 30 measurement sweeps,
- cold start,
- a proposal scale `eps` tuned by hand.

| beta | eps | accept | plaquette_mean | plaquette_std | defect_mean | defect_std |
|---|---|---|---|---|---|---|
| 1 | 0.6 | 0.600412 | 0.233191 | 0.01483 | 0.303841 | 0.016012 |
| 2 | 0.55 | 0.326543 | 0.514484 | 0.022442 | 0.098834 | 0.016241 |
| 3 | 0.45 | 0.25 | 0.727257 | 0.010414 | 0.008848 | 0.003609 |
| 4 | 0.35 | 0.276029 | 0.804068 | 0.009706 | 0.001166 | 0.001653 |

Interpretation:
- the average plaquette increases with \(\beta\), as expected.
- the fraction of plaquettes with \(\theta_p>\pi/2\) drops rapidly (roughly exponentially) with \(\beta\).

This is qualitatively consistent with the **concentration-of-measure** calculation in the one-link model (see the concentration note). fileciteturn2file3

---

## 3. Code (self-contained)

```python
import numpy as np, math

# Pauli matrices
sx = np.array([[0,1],[1,0]], dtype=np.complex128)
sy = np.array([[0,-1j],[1j,0]], dtype=np.complex128)
sz = np.array([[1,0],[0,-1]], dtype=np.complex128)
I2 = np.eye(2, dtype=np.complex128)

def su2_exp(alpha):
    "Return exp(i alpha·sigma) for alpha in R^3."
    theta = np.linalg.norm(alpha)
    if theta < 1e-12:
        return I2 + 1j*(alpha[0]*sx + alpha[1]*sy + alpha[2]*sz)
    aS = alpha[0]*sx + alpha[1]*sy + alpha[2]*sz
    return math.cos(theta)*I2 + 1j*math.sin(theta)/theta * aS

def dagger(M):
    return M.conj().T

def shift(coord, mu, delta, L):
    c = list(coord)
    c[mu] = (c[mu] + delta) % L
    return tuple(c)

def su2_retr(U):
    return float(np.real(np.trace(U)))

def su2_angle(U):
    c = max(-1.0, min(1.0, su2_retr(U)/2.0))
    return math.acos(c)

def staple_sum(U, coord, mu, L):
    S = np.zeros((2,2), dtype=np.complex128)
    for nu in range(4):
        if nu == mu:
            continue
        x_mu = shift(coord, mu, +1, L)
        x_nu = shift(coord, nu, +1, L)

        # forward staple
        S_up = U[x_mu][nu] @ dagger(U[x_nu][mu]) @ dagger(U[coord][nu])

        # backward staple
        x_minus_nu = shift(coord, nu, -1, L)
        x_mu_minus_nu = shift(x_minus_nu, mu, +1, L)
        S_dn = dagger(U[x_mu_minus_nu][nu]) @ dagger(U[x_minus_nu][mu]) @ U[x_minus_nu][nu]

        S += S_up + S_dn
    return S

def metropolis_sweep(U, beta, eps, rng):
    L = U.shape[0]
    accept = 0
    total = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    coord = (x0,x1,x2,x3)
                    for mu in range(4):
                        A = staple_sum(U, coord, mu, L)
                        U_old = U[coord][mu]
                        R = su2_exp(eps * rng.normal(size=3))
                        U_new = R @ U_old
                        tr_old = su2_retr(U_old @ A)
                        tr_new = su2_retr(U_new @ A)
                        dS = -0.5*beta*(tr_new - tr_old)
                        if dS <= 0 or rng.random() < math.exp(-dS):
                            U[coord][mu] = U_new
                            accept += 1
                        total += 1
    return accept/total

def average_plaquette(U):
    L = U.shape[0]
    s = 0.0
    n = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    coord=(x0,x1,x2,x3)
                    for mu in range(4):
                        for nu in range(mu+1,4):
                            x_mu = shift(coord, mu, +1, L)
                            x_nu = shift(coord, nu, +1, L)
                            U_p = (
                                U[coord][mu]
                                @ U[x_mu][nu]
                                @ dagger(U[x_nu][mu])
                                @ dagger(U[coord][nu])
                            )
                            s += su2_retr(U_p)/2.0
                            n += 1
    return s/n

def plaquette_defect_density(U, theta_thresh):
    L = U.shape[0]
    n = 0
    d = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    coord=(x0,x1,x2,x3)
                    for mu in range(4):
                        for nu in range(mu+1,4):
                            x_mu = shift(coord, mu, +1, L)
                            x_nu = shift(coord, nu, +1, L)
                            U_p = (
                                U[coord][mu]
                                @ U[x_mu][nu]
                                @ dagger(U[x_nu][mu])
                                @ dagger(U[coord][nu])
                            )
                            if su2_angle(U_p) > theta_thresh:
                                d += 1
                            n += 1
    return d/n
```

---

## 4. What would make this more useful (next steps)

1. **Gauge fixing** (Landau / Coulomb) so that link-angle “defects” are meaningful in exponential coordinates.  
2. Larger lattices and longer runs to estimate the defect rate in the weak-coupling regime, where convexity breakdown is relevant.  
3. Compare measured “bad set” densities against the one-link prediction \(\sim e^{-\beta}\) and against any block-spin/RG effective theory.

