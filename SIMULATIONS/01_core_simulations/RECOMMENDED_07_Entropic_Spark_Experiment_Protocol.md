# Entropic Spark Lattice Experiment Protocol

This note translates the **Entropic Gribov Spark Conjecture** into a doable numerical experiment.

**Goal.** On a small 4D lattice, with a practical proxy for “FMR / Gribov restriction”, estimate the **Hessian at the origin**
\[
\nabla^2 V_{\mathrm{eff}}(0)
\quad\text{where}\quad
V_{\mathrm{eff}}(Y):=-\log \rho(Y)
\]
and \(\rho(Y)\) is the marginal density of a chosen **IR mode vector** \(Y\) under the gauge-fixed measure.

If the smallest eigenvalue of \(\nabla^2 V_{\mathrm{eff}}(0)\) looks **positive** and **volume-stable** (does not drift to \(0\) as \(L\) grows), that is serious evidence for a non-UV “Spark”.

---

## 0. What this *does not* prove

Even a perfect positive signal here is not a proof: finite volume and algorithmic gauge fixing are approximations to the FMR story.

But this experiment can do something valuable: **rule out** the conjecture quickly, or give a **strong calibration target** (the actual size of the curvature floor) for later analysis.

---

## 1. Choose the minimal testbed

Pick a first target that is cheap but meaningful:

- Gauge group: \(SU(2)\) (cheapest) or \(SU(3)\).
- Lattice: \(L^4\) with \(L\in\{4,6,8,10\}\) (start at \(L=4,6\)).
- Action: Wilson action at several \(\beta\) values (include a moderately weak-coupling regime and a “not too weak” regime).

You are not chasing continuum scaling here; you are chasing **a qualitative yes/no** on “is there an effective quadratic well for the lowest modes after gauge fixing?”.

---

## 2. Generate gauge configurations

Use a standard Markov chain Monte Carlo sampler:

- Heatbath + overrelaxation for \(SU(2)\).
- Cabibbo–Marinari for \(SU(3)\).
- Ensure thermalization and decorrelation (binning / integrated autocorrelation time).

Store \(N_{\mathrm{cfg}}\) configurations per \((L,\beta)\) (even \(10^3\) can be informative at tiny \(L\)).

---

## 3. Gauge-fixing proxy: approximate “FMR” by multi-start minimal Landau gauge

### Landau gauge functional
For each configuration \(U\), define the Landau gauge functional
\[
F[g;U] := \sum_{x,\mu} \Re \mathrm{Tr}\big(g(x)\,U_{x,\mu}\,g(x+\hat\mu)^{-1}\big).
\]
Landau gauge fixing corresponds to **maximizing** \(F[g;U]\) over gauge transformations \(g(\cdot)\).

### Practical proxy for being closer to the FMR
The true FMR requires the *global* maximizer; you cannot get it cheaply.

A standard proxy:
1. Run a fast Landau gauge fixer (overrelaxation / steepest ascent) from many random starts \(g_0\).
2. Keep the gauge copy with the **largest** final \(F\) value.

Call this “multi-start minimal Landau gauge”.  
It is not the FMR, but it pushes you toward it.

**Key experimental dial:** number of random restarts \(R\).  
Do runs with \(R\in\{1,5,20,100\}\). If the measured Hessian increases with \(R\), that is consistent with an entropic/FMR mechanism.

---

## 4. Define the IR observable \(Y\)

You need a low-dimensional vector \(Y\) that captures “the lowest modes”.

### Option A simplest choice
Convert gauge-fixed links to a Lie-algebra field \(A_{x,\mu}\) via a standard map (e.g. the anti-Hermitian traceless part of \(\log U_{x,\mu}\), or a small-field approximation when \(\beta\) is large).

Then Fourier transform:
\[
\tilde A_\mu(k) := \frac{1}{L^4}\sum_x e^{-ik\cdot x} A_{x,\mu}.
\]

Pick the smallest nonzero lattice momenta, e.g.
\[
k = \left(\tfrac{2\pi}{L},0,0,0\right),\ \left(0,\tfrac{2\pi}{L},0,0\right),\dots
\]
and define \(Y\) as the real vector formed by the independent components of \(\tilde A_\mu(k)\) for those \(k\) and \(\mu\).

This makes \(Y\) finite-dimensional and “IR”.

### Option B more geometric choice
Pick a block size \(b\) and define a block-averaged field \(Y\) (coarse mode) on the blocked lattice.  
This is closer to the RG language used in the theory notes, but costs a bit more code.

---

## 5. Estimate \(\nabla^2 V_{\mathrm{eff}}0\)

Let \(Y^{(1)},\dots,Y^{(n)}\) be the sampled IR vectors.

The marginal density is \(\rho(Y)\) (unknown analytically).  
The effective potential is \(V_{\mathrm{eff}}(Y)=-\log\rho(Y)+\mathrm{const}\).

You want the Hessian at the origin, i.e. the local quadratic curvature.

### Method 1 local Gaussian fit
Assume near \(0\),
\[
\rho(Y)\approx \exp\!\left(-\tfrac12 Y^\top H Y\right),
\quad\Rightarrow\quad
\nabla^2 V_{\mathrm{eff}}(0)\approx H.
\]
Then \(H\approx \Sigma^{-1}\) where \(\Sigma\) is the covariance of \(Y\) *restricted to a small ball* \(\|Y\|\le r\).

Protocol:
1. Choose a radius \(r\) so that you keep (say) 10–30% of samples (tune \(r\)).
2. Compute the sample covariance \(\widehat \Sigma(r)\).
3. Estimate \(H(r)=\widehat \Sigma(r)^{-1}\) (with regularization if needed).
4. Check stability as \(r\to 0\) (shrinking radii).

Output:
- smallest eigenvalue \(\lambda_{\min}(H(r))\),
- its dependence on \(r\), \(R\), \(L\), and \(\beta\).

### Method 2: quadratic fit to \(-\log\widehat\rhoY\) more direct, noisier
Estimate \(\widehat\rho\) via a KDE or histogram in low dimension, then fit
\[
V_{\mathrm{eff}}(Y)\approx V_0+\tfrac12 Y^\top H Y
\]
on a neighborhood of \(0\).

This is good in 1–3 dimensions; it becomes unreliable in higher dimension.

### Method 3 score matching and Stein estimators
If you can estimate \(\nabla \log\rho(Y)\), then near \(0\),
\[
\nabla \log\rho(Y)\approx -H Y,
\]
so you can regress the estimated score against \(Y\) to get \(H\).

---

## 6. Key stress tests

You are looking for **three convergences**:

1. **Restart convergence:** as \(R\) increases (better FMR proxy), \(\lambda_{\min}(\nabla^2 V_{\mathrm{eff}}(0))\) should *not* decrease.  
   Ideally it increases and stabilizes.

2. **Volume stability:** as \(L\) grows at fixed \(\beta\), the smallest eigenvalue should remain bounded away from \(0\) (or drift slowly).  
   A clean signal would be a stable positive plateau.

3. **Mode choice robustness:** the positive curvature should persist if you swap “which lowest modes” you track (e.g. choose a different set of minimal momentum vectors).

If all three occur, the conjecture has teeth.

---

## 7. Bonus diagnostic for distance to the Gribov horizon

If feasible, compute the smallest eigenvalue of the lattice Faddeev–Popov operator \(\mathcal M_A\) in Landau gauge (using Lanczos).

Track:
- \(\lambda_{\min}(\mathcal M_A)\) vs gauge-copy quality (restart count \(R\)),
- correlation between \(\lambda_{\min}(\mathcal M_A)\) and the inferred \(\lambda_{\min}(\nabla^2 V_{\mathrm{eff}}(0))\).

A strong correlation would support the “Gribov-geometry induces IR curvature” story.

---

## 8. Suggested minimal deliverable

- \(SU(2)\), \(L=4,6,8\), a couple of \(\beta\) values.
- \(R\in\{1,20\}\) random restarts.
- \(Y\) = smallest nonzero Fourier modes of \(A_\mu\).
- Estimate \(H(r)\) by local covariance inversion with two radii.

Plot:
- \(\lambda_{\min}(H)\) vs \(L\),
- \(\lambda_{\min}(H)\) vs \(R\),
- and (if available) \(\lambda_{\min}(\mathcal M_A)\) vs \(R\).

This already answers: “does the entropic Spark look even vaguely plausible?”

---

## 9. How to report results back into the theory stack

If you get a stable positive \(\lambda_{\min}\), translate it into a “Spark constant”:

- define \(m_*^2 := \lambda_{\min}(\nabla^2 V_{\mathrm{eff}}(0))\),
- treat \(m_*\) as the candidate IR curvature scale.

Then the next mathematical task becomes: prove a lower bound \(\nabla^2 V_{\mathrm{eff}}(0)\succeq m_*^2 I\) on a typical set, and feed it into the **Block-Convexity Engine**.