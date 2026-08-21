# Outside-core coercivity and drift certificates for 4D SU(2) Langevin dynamics

## Overview

This note extracts the most *proof-shaped* object present in the project files: a **uniform-in-volume outside-core certificate** for (i) coercivity of the pairing term $\langle\nabla S,\nabla V\rangle$ and (ii) negativity of the drift $LV$, for a natural bounded observable $V$ built from the plaquette defect.

The key idea is to turn raw Monte‑Carlo generator estimates into a **holdout-validated lemma candidate** of the form:

\[
\boxed{
\text{On the domain } \{B_{\mathrm{avg}}\ge \tau\}:\quad
\langle\nabla S,\nabla V\rangle \;\ge\; c(\tau)\,B_{\mathrm{avg}},\qquad
LV \;\le\; d(\tau)\,B_{\mathrm{avg}}
}
\]

with $c(\tau)>0$ and $d(\tau)<0$ once $\tau$ is large enough, and with constants that appear stable across lattice sizes $L\in\{8,12,16\}$.

---

## Definitions and generator decomposition

### Lattice and variables
- Lattice: 4D periodic hypercubic lattice of linear size $L$.
- Gauge group: $SU(2)$.
- Link field: $U(x,\mu)\in SU(2)$ for $\mu\in\{0,1,2,3\}$.

### Wilson action and plaquette defect
Let $U_p$ denote the oriented plaquette matrix and define the **plaquette defect**
\[
z_p \;=\; 1-\frac{1}{2}\mathrm{Re}\,\mathrm{Tr}(U_p)\in[0,2].
\]
Let $B_{\mathrm{avg}}$ be the mean of $z_p$ over all plaquettes and sites.

Define the bounded observable
\[
V \equiv V_{\mathrm{bar}} \;=\; 1 + B_{\mathrm{avg}}.
\]

### Langevin generator shape (overdamped)
For a Langevin-type diffusion on the group manifold with invariant measure proportional to $e^{-S}$, the generator has the schematic form
\[
Lf \;=\; \Delta f \; -\;\langle\nabla S,\nabla f\rangle,
\]
where $\Delta$ is the Laplace–Beltrami operator (sum of second derivatives along an orthonormal basis of the Lie algebra directions on each link).

Applying to $V$ yields the decomposition
\[
LV \;=\; \underbrace{\Delta V}_{\texttt{lap}} \; -\; \underbrace{\langle\nabla S,\nabla V\rangle}_{\texttt{gip}}.
\]

---

## Monte‑Carlo finite-difference estimator (directional)

The code implements a directional finite-difference estimate in random Lie-algebra directions $\Xi$ per configuration:

\[
\Delta V \approx \frac{V(U e^{+\varepsilon\Xi}) + V(U e^{-\varepsilon\Xi}) - 2 V(U)}{\varepsilon^2},
\]
\[
D_\Xi S \approx \frac{S(U e^{+\varepsilon\Xi}) - S(U e^{-\varepsilon\Xi})}{2\varepsilon},\qquad
D_\Xi V \approx \frac{V(U e^{+\varepsilon\Xi}) - V(U e^{-\varepsilon\Xi})}{2\varepsilon},
\]
\[
\langle\nabla S,\nabla V\rangle \approx (D_\Xi S)(D_\Xi V),
\qquad
LV \approx \Delta V - (D_\Xi S)(D_\Xi V),
\]
followed by averaging over many random directions (`mc=256`) to get a mean and standard error for each configuration.

---

## Structural checks that look like lemmas

### 1) Affine Laplacian law for $V_{\mathrm{bar}}$

A striking near-identity appears numerically across volumes:
\[
\Delta V_{\mathrm{bar}} \approx 12 - 12\,B_{\mathrm{avg}}.
\]
The reported residuals for the hypothesis $\Delta V_{\mathrm{bar}}\stackrel{?}{\approx}12-12B_{\mathrm{avg}}$ are small (max absolute errors $\sim 10^{-2}$ and decreasing with $L$).

This is a plausible candidate for an *analytic identity* (or a perturbatively exact relation) tied to the geometry of $SU(2)$ and the specific form of $V_{\mathrm{bar}}$.

### 2) Sign of the pairing term
For the samples reported, the pairing term $\langle\nabla S,\nabla V\rangle$ is nonnegative for every tested configuration, with an extreme sign-test p-value reported in the logs.

If provable, that is a clean inequality:
\[
\langle\nabla S,\nabla V\rangle \ge 0.
\]

---

## Drift inequality: global affine bound (baseline)

A simple one-sided affine drift upper bound was fit on half the samples and tested on holdout:

\[
LV \le -\lambda V + b.
\]

With a $5\sigma$ safety margin, the reported fit found $\lambda=0$ and $b\approx 12.0183$ with **0/1024 holdout violations** at the same $5\sigma$ margin in the logged run.

Interpretation: this is a safe *global ceiling* but not the proof-shape Foster–Lyapunov condition you really want (it does not show negative drift away from a core).

---

## The genuinely proof-shaped object: ratio certificates and a uniform $\tau_0$

### Ratio certificates on a tail domain
Define (with an $n\sigma$ safety margin on holdout)

\[
c_{\mathrm{gip}}(\tau)
=\inf_{B_{\mathrm{avg}}\ge\tau}\frac{\texttt{gip}-n\sigma\,\texttt{gip\_se}}{B_{\mathrm{avg}}},
\qquad
d_{LV}(\tau)
=\sup_{B_{\mathrm{avg}}\ge\tau}\frac{\texttt{LV}+n\sigma\,\texttt{LV\_se}}{B_{\mathrm{avg}}}.
\]

Then for $B_{\mathrm{avg}}\ge \tau$ we have certified (numerically):

\[
\texttt{gip} \ge c_{\mathrm{gip}}(\tau)\,B_{\mathrm{avg}},\qquad
\texttt{LV} \le d_{LV}(\tau)\,B_{\mathrm{avg}}.
\]

### Uniform-in-$L$ summary and the selected threshold
The project output gives a pooled, uniform-in-$L$ summary (holdout, $n\sigma=2$) over $L=8,12,16$ and identifies the first $\tau$ meeting targets
\[
c_{\min}(\tau)\ge 20,\qquad d_{\max}(\tau)\le -1,
\]
as
\[
\boxed{\tau_0 = 0.3883,\quad c_{\min}(\tau_0)=20.9510,\quad d_{\max}(\tau_0)=-2.6909.}
\]

This is exactly the sort of “one-line lemma statement” that can be attacked analytically:
> *Outside the small-defect core set $\{B_{\mathrm{avg}}<\tau_0\}$, the pairing term is coercive and the drift is negative, with constants stable across tested volumes.*

---

## Why this is exciting (and what to do next)

### Why it matters
A Foster–Lyapunov condition typically looks like:
\[
LV \le -\alpha V + \beta\,\mathbf{1}_{\mathcal{C}},
\]
i.e. negative drift outside a “core” set $\mathcal{C}$, plus a bounded compensation inside $\mathcal{C}$.

The ratio-certificate output is already in that shape, except phrased in units of $B_{\mathrm{avg}}$ rather than $V$.

### Next analytic targets
1. **Prove the Laplacian law** (exactly or with a uniform error) for $V_{\mathrm{bar}}=1+B_{\mathrm{avg}}$.
2. **Prove positivity/coercivity** of $\langle\nabla S,\nabla V\rangle$ on $\{B_{\mathrm{avg}}\ge\tau\}$ with an explicit $c(\tau)$.
3. **Control the core set** $\{B_{\mathrm{avg}}<\tau_0\}$ by either:
   - proving boundedness of $LV$ there, or
   - switching to a different $V$ that is small near the core but grows in the tail (increasing-volume setting).
4. **Scaling program:** check whether $(\tau_0,c_{\min},d_{\max})$ remain stable as $L$ increases beyond 16, and how they behave as $\beta$ varies.

---

## Reproducible code fragment: uniform-in-$L$ $\tau_0$ picker

Below is the essential “uniform-in-$L$ $\tau_0$ picker” extracted/adapted from the project log.

```python
import numpy as np

NSIGMA = 2.0

def per_L_fit_hold_indices(L, Lval):
    idx = np.where(L == Lval)[0]
    n = idx.size
    n_fit = n // 2
    return idx[:n_fit], idx[n_fit:]

def c_gip(L, Bavg, gip, gip_se, Lval, tau):
    _, hold = per_L_fit_hold_indices(L, Lval)
    dom = hold[Bavg[hold] >= tau]
    if dom.size == 0:
        return None
    val = (gip[dom] - NSIGMA*gip_se[dom]) / Bavg[dom]
    return float(np.min(val))

def d_LV(L, Bavg, LV, LV_se, Lval, tau):
    _, hold = per_L_fit_hold_indices(L, Lval)
    dom = hold[Bavg[hold] >= tau]
    if dom.size == 0:
        return None
    val = (LV[dom] + NSIGMA*LV_se[dom]) / Bavg[dom]
    return float(np.max(val))

# choose tau grid from pooled fit quantiles (more stable)
QS = [0.20,0.25,0.30,0.35,0.38,0.40,0.42,0.45,0.50,0.55,0.60,0.67,0.75,0.80,0.90]
taus = sorted(set([max(1e-6, float(np.quantile(Bavg_fit, q))) for q in QS]))

C_TARGET, D_TARGET = 20.0, 1.0
tau0 = None
for tau in taus:
    cs, ds = [], []
    ok = True
    for Lval in np.unique(L):
        c = c_gip(L, Bavg, gip, gip_se, Lval, tau)
        d = d_LV(L, Bavg, LV, LV_se, Lval, tau)
        if c is None or d is None:
            ok = False
            break
        cs.append(c); ds.append(d)
    if not ok:
        continue
    cmin, dmax = min(cs), max(ds)
    if (cmin >= C_TARGET) and (dmax <= -D_TARGET):
        tau0 = (tau, cmin, dmax)
        break

print("tau0 =", tau0)
```

---

## Notes on scope

All statements above are **numerical certificates** extracted from the project logs. They are not analytic proofs yet; they are intended to serve as a precise target for analytic lemmas.
