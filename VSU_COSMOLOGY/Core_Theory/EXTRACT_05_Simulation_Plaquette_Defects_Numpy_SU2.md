---
title: "Simulation Note: Gauge-Invariant 'Small-Field' Defects via SU(2) Plaquette Angles (NumPy)"
author: "Project extraction + verification run"
date: "2025-12-29"
---

# Why a simulation note belongs in this extraction

The project includes a full 4D SU(2) Monte Carlo prototype in JAX, designed to measure a “defect density” defined by a **radius**
\[
r(U)=\arccos\!\Big(\tfrac12\operatorname{ReTr}(U)\Big),
\]
and then counting links with \(r(U)>r_{\mathrm{crit}}\). 【235:1†UNIFIED_4D_Lattice_YangMills_Simulation_and_Scaling_Analysis_JAX.md†L3-L7】【235:6†UNIFIED_4D_Lattice_YangMills_Simulation_and_Scaling_Analysis_JAX.md†L31-L38】

That’s a reasonable *local coordinate diagnostic*, but in a gauge theory **link variables are gauge-dependent**. So a link-based defect density can fail to show the weak-coupling trend unless one gauge-fixes.

To connect more cleanly to the project’s “small-field region” philosophy, the natural gauge-invariant diagnostic is a **plaquette-angle defect density**:
\[
U_p = U_\mu(x)\,U_\nu(x+\hat\mu)\,U_\mu(x+\hat\nu)^\dagger\,U_\nu(x)^\dagger,
\qquad
r(U_p)=\arccos\!\Big(\tfrac12\operatorname{ReTr}(U_p)\Big),
\]
and then count plaquettes with \(r(U_p)>r_{\mathrm{crit}}\).

---

# 1. What the project’s JAX prototype does (and what it outputs)

The JAX code defines \(r(U)\) via \(\arccos(\tfrac12\operatorname{ReTr}(U))\) and a defect density \(\rho(\beta)\) by counting links with \(r(U)>r_{\mathrm{crit}}\). 【235:6†UNIFIED_4D_Lattice_YangMills_Simulation_and_Scaling_Analysis_JAX.md†L31-L45】

It then reports an example scan (with \(r_{\mathrm{crit}}=1.0\)):

- defect densities around \(0.78\)–\(0.87\) across \(\beta\in[2,10]\). 【235:1†UNIFIED_4D_Lattice_YangMills_Simulation_and_Scaling_Analysis_JAX.md†L46-L60】

The same file also includes a “full lattice simulation” example at \(L=8\), \(\beta=5.0\), \(r_{\mathrm{crit}}=1.9248\) reporting **zero** defects. 【235:8†UNIFIED_4D_Lattice_YangMills_Simulation_and_Scaling_Analysis_JAX.md†L52-L69】

These outputs are useful as sanity checks of code plumbing and the staple-based local action implementation, but the link-based defect statistic should be interpreted cautiously unless a gauge-fixing prescription is included.

---

# 2. A small CPU-verifiable variant: SU(2) Metropolis with plaquette defects (NumPy)

Because JAX with CUDA is not available in this environment, I implemented a minimal SU(2) Metropolis sampler in **NumPy** using the unit-quaternion representation of SU(2). The goal is not precision physics; it is a *trend check*:

> As \(\beta\) increases, plaquette holonomies should concentrate closer to the identity, and the plaquette-angle defect density should decrease.

Below is the runnable code (single file) used for the measurement.

```python
import numpy as np, math

# ---------- SU(2) as unit quaternions q = (w,x,y,z) ----------
def quat_mul(a, b):
    aw, ax, ay, az = np.moveaxis(a, -1, 0)
    bw, bx, by, bz = np.moveaxis(b, -1, 0)
    w = aw*bw - ax*bx - ay*by - az*bz
    x = aw*bx + ax*bw + ay*bz - az*by
    y = aw*by - ax*bz + ay*bw + az*bx
    z = aw*bz + ax*by - ay*bx + az*bw
    return np.stack([w,x,y,z], axis=-1)

def quat_conj(a):
    out = np.array(a, copy=True)
    out[...,1:] *= -1.0
    return out

def quat_trace_re(a):
    # For SU(2) in this representation: ReTr(U) = 2*w
    return 2.0 * a[...,0]

def quat_radius(a):
    w = np.clip(a[...,0], -1.0, 1.0)
    return np.arccos(w)

def su2_random(rng):
    v = rng.normal(size=(4,))
    return v / np.linalg.norm(v)

def su2_near_id(rng, eps=0.2):
    alpha = rng.normal(scale=eps, size=(3,))
    theta = np.linalg.norm(alpha)
    if theta < 1e-12:
        return np.array([1.0, 0.0, 0.0, 0.0])
    axis = alpha/theta
    return np.array([math.cos(theta), *(math.sin(theta)*axis)])

# ---------- 4D periodic lattice neighbors ----------
def make_neighbor_tables(L):
    Vol = L**4
    def lin(c):
        x,y,z,t = c
        return (((x*L + y)*L + z)*L + t)

    up = np.empty((4,Vol), dtype=np.int32)
    down = np.empty((4,Vol), dtype=np.int32)

    idx = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for t in range(L):
                    for mu,(dx,dy,dz,dt) in enumerate([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]):
                        up[mu,idx]   = lin(((x+dx)%L,(y+dy)%L,(z+dz)%L,(t+dt)%L))
                        down[mu,idx] = lin(((x-dx)%L,(y-dy)%L,(z-dz)%L,(t-dt)%L))
                    idx += 1
    return up, down

# ---------- Local Metropolis update using staple terms ----------
def metropolis_update_link(U_flat, site, mu, beta, up, down, rng, eps=0.2):
    U_old = U_flat[site, mu]
    U_new = quat_mul(su2_near_id(rng, eps=eps), U_old)

    old_retr = 0.0
    new_retr = 0.0
    for nu in range(4):
        if nu == mu:
            continue

        x_plus_mu = up[mu, site]
        x_plus_nu = up[nu, site]
        # forward term: U_nu(x+mu) * U_mu(x+nu)^† * U_nu(x)^†
        term_fwd = quat_mul(
            quat_mul(U_flat[x_plus_mu, nu], quat_conj(U_flat[x_plus_nu, mu])),
            quat_conj(U_flat[site, nu])
        )

        x_minus_nu = down[nu, site]
        x_plus_mu_minus_nu = down[nu, x_plus_mu]
        # backward term: U_nu(x-nu) * U_mu(x-nu)^† * U_nu(x+mu-nu)^†
        term_bwd = quat_mul(
            quat_mul(U_flat[x_minus_nu, nu], quat_conj(U_flat[x_minus_nu, mu])),
            quat_conj(U_flat[x_plus_mu_minus_nu, nu])
        )

        old_retr += quat_trace_re(quat_mul(U_old, term_fwd)) + quat_trace_re(quat_mul(U_old, term_bwd))
        new_retr += quat_trace_re(quat_mul(U_new, term_fwd)) + quat_trace_re(quat_mul(U_new, term_bwd))

    # accept if log u < 0.5*beta*(new-old)
    if math.log(rng.random()) < 0.5 * beta * (new_retr - old_retr):
        U_flat[site, mu] = U_new
        return 1
    return 0

def sweep(U_flat, beta, up, down, rng, eps=0.2):
    Vol = U_flat.shape[0]
    acc = 0
    for site in range(Vol):
        for mu in range(4):
            acc += metropolis_update_link(U_flat, site, mu, beta, up, down, rng, eps=eps)
    return acc / (Vol*4)

# ---------- Gauge-invariant observables ----------
def measure_avg_plaquette(U_flat, L, up):
    Vol = L**4
    total = 0.0
    count = 0
    for site in range(Vol):
        for mu in range(4):
            for nu in range(mu+1,4):
                x_plus_mu = up[mu, site]
                x_plus_nu = up[nu, site]
                U_p = quat_mul(
                    quat_mul(
                        quat_mul(U_flat[site,mu], U_flat[x_plus_mu,nu]),
                        quat_conj(U_flat[x_plus_nu,mu])
                    ),
                    quat_conj(U_flat[site,nu])
                )
                total += 0.5 * quat_trace_re(U_p)  # = w_p
                count += 1
    return total / count

def measure_plaquette_defect_density(U_flat, L, up, r_crit=1.9):
    Vol = L**4
    defects = 0
    count = 0
    for site in range(Vol):
        for mu in range(4):
            for nu in range(mu+1,4):
                x_plus_mu = up[mu, site]
                x_plus_nu = up[nu, site]
                U_p = quat_mul(
                    quat_mul(
                        quat_mul(U_flat[site,mu], U_flat[x_plus_mu,nu]),
                        quat_conj(U_flat[x_plus_nu,mu])
                    ),
                    quat_conj(U_flat[site,nu])
                )
                defects += int(quat_radius(U_p) > r_crit)
                count += 1
    return defects / count

# ---------- Run ----------
def run(L=3, betas=(1.5,3.0,6.0), n_therm=20, n_meas=20, eps=0.2, r_crit=1.9, seed=2025):
    rng = np.random.default_rng(seed)
    up, down = make_neighbor_tables(L)
    Vol = L**4
    U_flat = np.zeros((Vol,4,4))
    for s in range(Vol):
        for mu in range(4):
            U_flat[s,mu] = su2_random(rng)

    out = []
    for beta in betas:
        for _ in range(n_therm):
            sweep(U_flat, beta, up, down, rng, eps=eps)

        accs, ps, rhos = [], [], []
        for _ in range(n_meas):
            accs.append(sweep(U_flat, beta, up, down, rng, eps=eps))
            ps.append(measure_avg_plaquette(U_flat, L, up))
            rhos.append(measure_plaquette_defect_density(U_flat, L, up, r_crit=r_crit))

        out.append((beta, float(np.mean(accs)), float(np.mean(ps)), float(np.mean(rhos))))
    return out
```

---

# 3. Results from an actual run (toy scale, but trend visible)

Parameters:

- lattice \(L=3\) (so \(3^4=81\) sites, periodic),
- proposal size \(\varepsilon=0.2\),
- thermalization 20 sweeps, measurement 20 sweeps,
- defect threshold \(r_{\mathrm{crit}}=1.9\) on **plaquette angles**,
- \(\beta\in\{1.5,3.0,6.0\}\).

Observed averages:

| β | acceptance | ⟨½ReTr(U_p)⟩ | defect density ρ_def (r(U_p)>1.9) |
|---:|---:|---:|---:|
| 1.5 | 0.804 | 0.192 | 0.175 |
| 3.0 | 0.685 | 0.340 | 0.099 |
| 6.0 | 0.522 | 0.469 | 0.054 |

**Interpretation:**

- \(\langle \tfrac12\mathrm{ReTr}(U_p)\rangle\) increases with \(\beta\), as it should.
- The plaquette-defect density \(\rho_{\mathrm{def}}\) drops with \(\beta\), consistent with increasing concentration in a gauge-invariant small-field regime.

Again: this is a *tiny lattice* with *short runs*; it is not meant as precision scaling physics—just a sanity check that the “small-field region becomes typical” story is at least numerically visible when the statistic is gauge invariant.

---

# 4. Connection back to the project’s theory pipeline

This simulation supports the *qualitative* assumption behind the Part III Lyapunov strategy:

> For sufficiently large \(\beta\), the Gibbs measure should spend most of its mass in a region where plaquettes are close to the identity (and therefore where the local horizontal curvature theorem can plausibly be applied after appropriate coordinate/gauge choices).

Quantifying this uniformly in \(\Lambda\) is the hard analytic step—exactly what the Lyapunov drift condition is meant to certify.
