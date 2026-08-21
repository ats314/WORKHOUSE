# Simulation Certificates for the Analytic Engine
## Drift decomposition, affine Laplacian law, ratio certificates, and spectral obstructions under blocking

This document extracts the most valuable simulation artifacts in the project: those that probe the same operator
that appears in the analytic pipeline (Hessian / Witten / Green kernel).

---

## 1. A pointwise generator decomposition check

Across the SU(2) 4D drift runs the dataset records three per-configuration estimates:

- `LV`  : the drift $LV$,
- `lap` : the Laplacian contribution $\Delta V$,
- `gip` : the pairing $\langle\nabla S,\nabla V\rangle$.

The target identity is

\[
LV \stackrel{?}{=} \mathrm{lap} - \mathrm{gip}.
\]

### Code skeleton (NPZ-based)

```python
import numpy as np
d = np.load("decomp_Lsweep_results.npz", allow_pickle=True)
LV  = np.asarray(d["LV"],  dtype=np.float64).reshape(-1)
lap = np.asarray(d["lap"], dtype=np.float64).reshape(-1)
gip = np.asarray(d["gip"], dtype=np.float64).reshape(-1)

print("max|lap - gip - LV| =", np.max(np.abs(lap - gip - LV)))
print("rms|.|            =", np.sqrt(np.mean((lap - gip - LV)**2)))
```

### Reported result

The run output reports essentially machine-precision agreement:

\[
\max|\mathrm{lap}-\mathrm{gip}-LV| \approx 3.197\times 10^{-14},
\quad
\mathrm{rms}\approx 5.498\times 10^{-15}.
\]

That is strong evidence that the computed components are internally consistent and can be treated as a reliable numerical proxy
for the analytic decomposition.

---

## 2. PROOF A: the “affine Laplacian law”

A striking empirical finding is that the Laplacian term is almost perfectly linear in the averaged plaquette badness $B_{\mathrm{avg}}$:

\[
\mathrm{lap}\ \approx\ a + b\,B_{\mathrm{avg}},
\qquad a\approx 12,\ b\approx -12.
\]

The reported fit is:

- $\hat a = 11.999259$,
- $\hat b = -11.999253$,
- $R^2 = 0.999999871795$.

This is not merely “nice”; it is **structurally useful** because the analytic proof uses the good set
$K=\{B_{\mathrm{avg}}\le \varepsilon\}$, and an identity/estimate linking $\mathbb E[B_{\mathrm{avg}}]$
to Laplacian terms would be a plausible route to proving typicality inputs.

---

## 3. PROOF C: drift inequality fit + holdout (per volume)

A holdout-style certificate attempts to find constants $(\lambda,b)$ such that on a domain (core complement)

\[
LV \le -\lambda\,V + b.
\]

One representative “best certified (t,lam)” report (format varies by run) shows per-volume outputs like:

- $L=8$ : $\tau_0=0.1$, best $\lambda_\*\approx 13.2173$ (holdout violations and slack reported),
- $L=12$: $\tau_0=0.1$, best $\lambda_\*\approx 14.1018$ (holdout coverage reported).

These are not yet *the* final constants needed for the full analytic chain (because they are per-$L$ and rely on the specific $V$ chosen),
but they are meaningful evidence that the Foster–Lyapunov mechanism is numerically present with an order-one drift rate.

---

## 4. UNIFORM-IN-$L$ ratio certificate (and what it says is still missing)

A more “lemma-shaped” certificate (designed to avoid intercept artifacts) tries to control ratios on holdout, per $L$:

- coercivity: $\mathrm{gip}\ge c_{\min}(\tau_0)\,B_{\mathrm{avg}}$ on $\{B_{\mathrm{avg}}\ge\tau_0\}$,
- negative drift: $LV\le d_{\max}(\tau_0)\,B_{\mathrm{avg}}$ on $\{B_{\mathrm{avg}}\ge\tau_0\}$ with $d_{\max}<0$.

The scan reports:

- **no** $\tau_0$ on the grid meets the target $c_{\min}\ge 20$,
- the best-margin choice is $\tau_0\approx 0.215793$,
- at that $\tau_0$:
  \[
  c_{\min,\mathrm{all}}(\tau_0)\approx 10.718741,
  \qquad
  d_{\max,\mathrm{all}}(\tau_0)\approx -10.723010,
  \]
  with counts-by-volume (holdout domain size) roughly
  \[
  \{L=8:704,\ L=12:713,\ L=16:741\}.
  \]

So the **negative drift** part looks robust ($d_{\max}$ comfortably negative), but the **coercivity target** is not yet met uniformly.

The “worst offender” responsible for both bottlenecks is explicitly identified (example):
\[
\text{global\_idx}=3573,\quad L=12,\quad B_{\mathrm{avg}}\approx 1.00069,\quad LV\approx -13.4795.
\]

This is excellent information: it turns an abstract missing constant into a concrete configuration classification problem.

---

## 5. Maxwell Green-kernel verification (FFT) and anisotropy tuning

Separate simulation code computes a massive (vector/Maxwell) Green kernel by FFT, computes a constant $C_0(\Delta_1)$,
and checks the exponential bound by verifying that the ratio
\[
e^{+\eta\,d}\,|G(d)|
\]
is uniformly $\le 1$ (up to normalization).

One recorded run (L=16, $m^2=0.3$) reports:

- geometry: $D_E=18$, $C_0(\Delta_1)\approx 43.9077$,
- exponents:
  \[
  \eta_{\mathrm{DG}}(D_E)\approx 0.1290,\qquad
  \eta_{\mathrm{DG}}(C_0)\approx 0.0826,\qquad
  \eta_{\mathrm{CT}}(C_0)\approx 0.00341,
  \]
- max ratio $\approx 0.1412$ at distance $d=0$ (so the bound holds).

There is also a separate scalar-propagator “geometry tuning” experiment, adding a $c\,p^4$ hypercubic correction term to reduce lattice anisotropy.

---

## 6. Spectral obstruction signals under blocking

The run PDFs include computations of a **physical projected Hessian** minimum eigenvalue before and after blocking.

Representative printed diagnostics include:

- case A:
  \[
  \lambda_{\min}^{\rm phys}\approx 16.2075,\qquad
  \lambda_{\min}^{\rm blocked}\approx 11.5870,
  \]
- case B:
  \[
  \lambda_{\min}^{\rm phys}\approx 16.6728,\qquad
  \lambda_{\min}^{\rm blocked}\approx -47.5770,
  \]
  i.e. **large negative physical modes appear after blocking**.

This is a genuinely important signal for theory-building: it indicates coarse graining can destroy positivity in the physical sector
unless a renormalization/counterterm mechanism is in play.

---

## 7. What this suggests, theory-wise

A plausible “bigger theory” thread is:

- The analytic proofs seek a *matrix hinge* lower bound $\mathrm{Ric}_\mu\succeq m^2I+\alpha d_1^\*d_1$ on the good set.
- The simulations show:
  - the generator decomposition that feeds HS is numerically exact at dataset precision,
  - drift negativity outside a core set is robust,
  - but coercivity constants may be limited by rare offenders,
  - and blocking can create negative physical modes.

Put together, this suggests the continuum limit is not just “take $a\to0$” but “take $a\to0$ **while maintaining the hinge**,”
and the hinge may require explicit scale-dependent tuning.

---

## Primary sources inside the project

- Drift and Laplacian law: `127.pdf`, `12-21-25 GEMINI CODE.txt`.
- Ratio certificate outputs and offender audit: `127.pdf`.
- Maxwell kernel verification: `MAXWELL SIMS.txt`.
- Blocking spectral diagnostics: `RUN 124.pdf` (and related run PDFs).
