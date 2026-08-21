# Convexification by the chord: oscillation bounds and the Holley–Stroock factor (toy model)

This note explores a practical question that appears implicitly in the repository:

> If the potential is “almost convex” but has a concave dip on an interval, can we bound the *price* of convexifying it?

In one dimension, a clean way to convexify is to replace the concave interval by the chord connecting its endpoints (the convex envelope along that axis).

The original repository script testing this numerically is `analysis_perturbation.py` (JAX-based). fileciteturn1file0

---

## 1. The toy potential

Use the same one-link effective potential
\[
S_\beta(\theta) = -2\log\left(\frac{\sin\theta}{\theta}\right) - \beta\cos\theta,
\qquad \theta\in(0,\pi).
\]

For \(\beta>\beta_c\), the radial Hessian becomes negative on \((\theta_-,\theta_+)\), giving a concave “dip”.

---

## 2. Chord convexification and oscillation

Define the chord between \(\theta_-\) and \(\theta_+\):
\[
\mathrm{Chord}_\beta(\theta)
=
S_\beta(\theta_-)
+
\frac{S_\beta(\theta_+)-S_\beta(\theta_-)}{\theta_+-\theta_-}(\theta-\theta_-).
\]

Then define a convexified proxy potential
\[
\widetilde S_\beta(\theta)
=
\begin{cases}
S_\beta(\theta), & \theta\notin[\theta_-,\theta_+],\\[4pt]
\mathrm{Chord}_\beta(\theta), & \theta\in[\theta_-,\theta_+].
\end{cases}
\]

The **oscillation** (max deviation from convexified envelope) is
\[
\mathrm{osc}(\beta) = \sup_{\theta\in[\theta_-,\theta_+]}\bigl(S_\beta(\theta) - \mathrm{Chord}_\beta(\theta)\bigr).
\]

This quantity controls a classical Holley–Stroock comparison:
if two measures satisfy \(d\mu \propto e^{-S}\), \(d\tilde\mu\propto e^{-\tilde S}\) and
\[
\|S-\tilde S\|_\infty \le \mathrm{osc},
\]
then log-Sobolev and Poincaré constants differ by factors \(\lesssim e^{\mathrm{osc}}\).

---

## 3. Numerical values

Computing \(\theta_\pm\) from the Hessian-root condition, then scanning \([\theta_-,\theta_+]\) for the max deviation gives:

| beta | r_start | r_end | osc | HS_factor |
|---|---|---|---|---|
| 5 | 1.92482 | 2.33232 | 0.00539456 | 1.00541 |
| 10 | 1.70622 | 2.65422 | 0.310291 | 1.36382 |
| 20 | 1.63377 | 2.8128 | 1.46296 | 4.31872 |
| 50 | 1.5951 | 2.93859 | 6.05786 | 427.458 |

So:
- Around \(\beta=5\), the convexification penalty is tiny (∼0.5%).
- At \(\beta=10\), it is already a \(\sim 1.36\times\) factor.
- At \(\beta=50\), it is enormous (\(\sim 4\times 10^2\)).

---

## 4. The big warning label: volume blow-up

For a *single* degree of freedom, Holley–Stroock can be useful.

For a **lattice** measure, the total action is a **sum** over many local terms. If you convexify each local term and take a sup norm, the total oscillation generically scales like
\[
\mathrm{osc}_{\rm total} \sim (\text{volume})\times (\text{per-term oscillation}),
\]
so the Holley–Stroock factor \(e^{\mathrm{osc}_{\rm total}}\) becomes useless in the thermodynamic limit.

This is precisely why the repository’s proof plan treats “perturbative convexification” as an idea that needs a more sophisticated multi-scale implementation (or a different functional inequality).

---

## 5. What might fix it (research directions)

To prevent volume blow-up you likely need one of:

- **Two-scale / block decomposition** log-Sobolev inequalities: show strong convexity at the block level and treat defects as sparse.
- **Restricted LSI** on a high-probability “good set” + control of the complement (rare-event functional inequalities).
- **Cluster expansion for defects**: if defects behave like a dilute polymer gas, one can sometimes show uniform mixing/spectral gap for the “sea” with controlled corrections.
- **Gauge fixing**: the worst concavity may be a coordinate artifact amplified by gauge orbits; a gauge-fixed representative might reduce the effective oscillation per block.

---

## 6. Reproducible code snippet (no JAX)

```python
import math
import numpy as np
from scipy.optimize import brentq

def S(theta, beta):
    if theta < 1e-12:
        haar = theta**2/3 + theta**4/90
    else:
        haar = -2*math.log(math.sin(theta)/theta)
    return haar - beta*math.cos(theta)

def lam_rad_scaled(theta, beta):
    return 0.5*(1/math.sin(theta)**2 - 1/theta**2) + (beta/4)*math.cos(theta)

def roots(beta, nscan=200000):
    thetas = np.linspace(1e-6, math.pi-1e-6, nscan)
    vals = 0.5*(1/np.sin(thetas)**2 - 1/thetas**2) + (beta/4)*np.cos(thetas)
    s = np.sign(vals)
    idx = np.where(s[:-1]*s[1:] < 0)[0]
    a,b = thetas[idx[0]], thetas[idx[0]+1]
    c,d = thetas[idx[1]], thetas[idx[1]+1]
    t1 = brentq(lambda x: lam_rad_scaled(x,beta), a,b)
    t2 = brentq(lambda x: lam_rad_scaled(x,beta), c,d)
    return t1,t2

def oscillation(beta, n=4000):
    t1,t2 = roots(beta)
    S1,S2 = S(t1,beta), S(t2,beta)
    slope = (S2-S1)/(t2-t1)
    grid = np.linspace(t1,t2,n)
    chord = S1 + slope*(grid - t1)
    diffs = np.array([S(t,beta) for t in grid]) - chord
    return diffs.max()

```

