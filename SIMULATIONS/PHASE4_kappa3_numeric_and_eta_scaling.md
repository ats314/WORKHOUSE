---
title: "SU(3) strip parameters, numeric $\kappa_3(\varepsilon)$, and the $\eta^4$ tube law"
date: "2025-12-31"
---

## 0. Parameter choices (strip-consistent)

We work with the smooth plaquette defect (fundamental character proxy)
\[
\widetilde z(U)\;=\;1-\frac13\Re\operatorname{Tr}(U)\in[0,2].
\]

**Strip (average defect):** choose
\[
\Sigma \;=\;\{\varepsilon_B < B(U) < \varepsilon_B+\delta\},
\qquad
B(U):=\frac{1}{|P|}\sum_{p}\widetilde z(U_p).
\]

A concrete choice that matches the combinatorics in the outside-core argument is:
\[
\boxed{\varepsilon_B=0.20,\qquad \delta=0.05.}
\]

Then on the event \(B\ge \varepsilon_B\), at least an \(\varepsilon_B/4\) fraction of plaquettes satisfy
\[
\widetilde z(U_p)\ge \varepsilon:=\varepsilon_B/2=0.10,
\]
so the one-plaquette force lower bound only needs to hold for
\[
\boxed{\varepsilon = 0.10.}
\]

**Eigen-gap floor:** to stay away from Weyl walls, pick
\[
\boxed{\gamma_0 = 0.50\ \text{rad}.}
\]
(For the minimizer of \(\kappa_3(0.1)\) found below, the actual gap is \(\approx 0.555\), so this \(\gamma_0\) does not degrade the constant.)

---

## 1. What is $\kappa_3(\varepsilon)$?

Define the class-function force size floor
\[
\kappa_3(\varepsilon;\gamma_0)
:=
\inf\Big\{|\nabla \widetilde z(U)|:\ \widetilde z(U)\in[\varepsilon,1],\ \mathrm{gap}(U)\ge \gamma_0\Big\}.
\]

Here \(\mathrm{gap}(U)\) is the minimal pairwise eigenangle separation:
if \(U\) has eigenangles \(\theta_1,\theta_2,\theta_3\) (mod \(2\pi\)),
\[
\mathrm{gap}(U):=\min_{i<j} \mathrm{dist}_{S^1}(\theta_i,\theta_j).
\]

### Metric normalization

We use the project normalization fixed by SU(2):
\[
\Delta_{\mathrm{SU}(2)}\Big(\tfrac12\Re\mathrm{Tr}(U)\Big)=-3\Big(\tfrac12\Re\mathrm{Tr}(U)\Big).
\]
Under this convention the SU(3) fundamental Laplacian eigenvalue is \(16/3\), and gradient norms scale accordingly.

---

## 2. Weyl-alcove formula (2D)

Every conjugacy class in SU(3) has a representative
\[
U(\phi,\psi)=\mathrm{diag}(e^{i\phi},\,e^{i\psi},\,e^{-i(\phi+\psi)}),
\qquad \phi,\psi\in[-\pi,\pi].
\]

Then
\[
\widetilde z(\phi,\psi)=1-\frac13\Big(\cos\phi+\cos\psi+\cos(\phi+\psi)\Big).
\]

For the project normalization, a convenient closed form for the **gradient norm** (depending only on the class) is:
\[
|\nabla \widetilde z|(\phi,\psi)
=
\frac{\sqrt2}{3}\sqrt{
\sum_{k=1}^3\Big(\sin\theta_k-\overline s\Big)^2
},
\qquad
(\theta_1,\theta_2,\theta_3)=(\phi,\psi,-\phi-\psi),
\quad
\overline s:=\frac{\sin\theta_1+\sin\theta_2+\sin\theta_3}{3}.
\]

This follows from the right-trivialized gradient identity
\[
\nabla \widetilde z(U)
=\frac{1}{6}\Big(U-U^\dagger-\tfrac13\mathrm{Tr}(U-U^\dagger)\,I\Big),
\]
together with the metric scaling that matches \(\Delta_{\mathrm{SU}(2)}w=-3w\).

---

## 3. Numerical minimization (SciPy, constrained 2D)

We solve:
\[
\min_{\phi,\psi\in[-\pi,\pi]}|\nabla \widetilde z|(\phi,\psi)
\quad\text{s.t.}\quad
\widetilde z(\phi,\psi)\ge \varepsilon,\;\widetilde z(\phi,\psi)\le 1,\;\mathrm{gap}(\phi,\psi)\ge\gamma_0.
\]

### Result

For \(\varepsilon=0.10\), \(\gamma_0=0.50\ \mathrm{rad}\):
\[
\boxed{\kappa_3(0.10;\,0.50)\ \approx\ 0.3511884584.}
\]

A minimizer (up to Weyl permutations) is approximately
\[
(\theta_1,\theta_2,\theta_3)\approx(0.55481,\,0,\,-0.55481),
\]
which has
\[
\widetilde z \approx 0.10,\qquad \mathrm{gap}\approx 0.5548.
\]

### Reproducible code

```python
import numpy as np, math
from scipy.optimize import minimize

TWOPI=2*math.pi

def wrap(a):
    return ((a+math.pi) % (2*math.pi)) - math.pi

def ang_diff(a,b):
    return abs(wrap(a-b))

def gap_angles(phi,psi):
    th=[wrap(phi), wrap(psi), wrap(-phi-psi)]
    return min(ang_diff(th[i],th[j]) for i in range(3) for j in range(i+1,3))

def ztilde(phi,psi):
    th1, th2, th3 = phi, psi, -phi-psi
    return 1 - (1/3)*(math.cos(th1)+math.cos(th2)+math.cos(th3))

def grad_norm_project(phi,psi):
    th1, th2, th3 = phi, psi, -phi-psi
    s1, s2, s3 = math.sin(th1), math.sin(th2), math.sin(th3)
    sbar=(s1+s2+s3)/3.0
    # project normalization (SU(2): Δ w = -3 w)
    return (math.sqrt(2)/3.0)*math.sqrt((s1-sbar)**2+(s2-sbar)**2+(s3-sbar)**2)

def solve_kappa(eps=0.10, gamma0=0.50, zmax=1.0, nstarts=40, seed=0):
    rng=np.random.default_rng(seed)
    bounds=[(-math.pi,math.pi),(-math.pi,math.pi)]
    best=float('inf'); bestx=None

    def obj(x): return grad_norm_project(x[0],x[1])
    cons=[
        {'type':'ineq','fun':lambda x,eps=eps: ztilde(x[0],x[1]) - eps},
        {'type':'ineq','fun':lambda x,zmax=zmax: zmax - ztilde(x[0],x[1])},
        {'type':'ineq','fun':lambda x,gamma0=gamma0: gap_angles(x[0],x[1]) - gamma0},
    ]

    for _ in range(nstarts):
        x0=rng.uniform(-math.pi, math.pi, size=2)
        res=minimize(obj, x0, method='SLSQP', bounds=bounds, constraints=cons,
                     options={'ftol':1e-12,'maxiter':1000})
        if res.success and res.fun < best:
            best, bestx = res.fun, res.x

    return best, bestx, ztilde(bestx[0],bestx[1]), gap_angles(bestx[0],bestx[1])

kappa, x, z, gap = solve_kappa()
print("kappa =", kappa)
print("phi,psi =", x)
print("z =", z, "gap =", gap)
```

---

## 4. Why you should see an $\eta^4$ law (and you can test it cleanly)

For the root-normalizer tube test at a link, a convenient proxy for
\(\mathrm{dist}(g,N(K_{12}))\) is the amount by which \(g\) mixes the invariant axis:
\[
d_{12}(g):=\sqrt{|g_{13}|^2+|g_{23}|^2}.
\]
Then \(d_{12}(g)=0\) iff \(g\) preserves the splitting \(\mathbb C^3=\mathrm{span}(e_1,e_2)\oplus\mathrm{span}(e_3)\),
i.e. \(g\in S(U(2)\times U(1))\), the normalizer of the embedded \(SU(2)\) in the \((1,2)\) plane.

**Haar fact (exact):** if \(g\) is Haar-uniform in \(SU(3)\) (or \(U(3)\)),
its third column is uniform on the complex unit sphere \(S^{5}\subset\mathbb C^3\).
Hence \(s:=|g_{13}|^2+|g_{23}|^2\) is Beta\((2,1)\) with density \(2s\) on \([0,1]\),
so
\[
\boxed{\mathbb P\big(d_{12}(g)\le \eta\big)=\eta^4\quad (0\le\eta\le 1).}
\]
This is the cleanest way to validate the codimension-4 tube scaling numerically.

---

## 5. What to measure in lattice data

With \(\varepsilon=0.10\) and \(\gamma_0=0.50\):

1. For each link \(\ell\), enumerate its 6 plaquettes \(p\ni\ell\).
2. Form staples \(S_{\ell,p}\) and relative staples \(R_{pq}=S_{\ell,q}S_{\ell,p}^{-1}\).
3. Define the near-normalizer score
   \[
   d_{ij}(R_{pq}) \le \eta
   \]
   using the appropriate column entries for the chosen root plane.
4. Define the “two-root-plane conspiracy precursor” event:
   - \(\widetilde z(U_p)\ge \varepsilon,\ \widetilde z(U_q)\ge \varepsilon\),
   - \(\mathrm{gap}(U_p),\mathrm{gap}(U_q)\ge \gamma_0\),
   - \(d_{ij}(R_{pq})\le \eta\).
5. Sweep:
   - fixed \(\beta\), vary \(\eta\): expect \(\sim \eta^4\) in the small-\(\eta\) regime;
   - fixed \(\eta\), vary \(\beta\): expect a roughly \(\sim e^{-2\beta\varepsilon}\) decay once \(\beta\) is large enough that rough plaquettes are rare and weakly dependent.

