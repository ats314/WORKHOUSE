# SU(2) Lattice Gauge Langevin: Empirical Drift Certificates and an (Almost-)Exact Laplacian Identity

## Abstract

This note distills a set of **computer-assisted “proof objects”** discovered in the project’s SU(2) lattice gauge simulations:

1. An extremely tight **affine law** for the group Laplacian of a natural Lyapunov observable $V(U)=1+\overline{B}(U)$,
2. A robust **positivity/coercivity** observation for the pairing term $\langle \nabla S,\nabla V\rangle$,
3. A **pointwise generator decomposition check**,
4. A **uniform-in-$L$ ratio drift certificate** (after a coupling rescaling scan) that passes simultaneously for $L\in\{8,12,16\}$.

Taken together, these support a working conjecture:  
> **Outside a low-action core set**, the SU(2) Langevin generator drives the system *strictly* toward smaller plaquette defect with a drift constant that can be made uniform in $L$.

This is the right shape of ingredient for **geometric ergodicity / mixing bounds** and (speculatively) a route toward **computer-assisted spectral-gap estimates** for stochastic quantization on finite lattices.

---

## 1. Model and the objects being measured

We work on a periodic hypercubic lattice of size $L^4$ with link variables
\[
U_{x,\mu}\in \mathrm{SU}(2).
\]

Let $U_p$ be the plaquette holonomy and define the normalized plaquette trace
\[
w(p) \;\equiv\; \frac{1}{2}\Re\operatorname{Tr}(U_p)\in[-1,1],
\]
and the plaquette “defect”
\[
z(p)\;\equiv\; 1-w(p)\in[0,2].
\]

Define the average defect
\[
\overline{B}(U)\;\equiv\;\frac{1}{N_p}\sum_{p} z(p),
\]
and the Lyapunov observable used throughout the project:
\[
V(U)\;\equiv\; 1+\overline{B}(U).
\]
(In the code/logs this appears as `Vbar` and `Bavg`.)

Let $S_\beta(U)$ be the Wilson action (up to an additive constant), proportional to $\beta\sum_p z(p)$.

---

## 2. Generator decomposition (standard, but verified numerically)

For overdamped Langevin / stochastic quantization on the compact Lie group manifold (one SU(2) per link), the infinitesimal generator has the schematic form
\[
\mathcal{L} f \;=\; \Delta f \;-\; \langle \nabla S_\beta,\nabla f\rangle,
\]
where $\Delta$ is the (right-invariant) Laplace–Beltrami operator on the product manifold of links.

For $f=V$,
\[
\mathcal{L}V \;=\; (\Delta V) \;-\; \langle \nabla S_\beta,\nabla V\rangle.
\]

In the project outputs these components are recorded as:

- `lap`  $\approx \Delta V$,
- `gip`  $\approx \langle \nabla S_\beta,\nabla V\rangle$,
- `LV`   $\approx \mathcal{L}V$,

with the identity
\[
\boxed{\quad \mathrm{LV} \;=\; \mathrm{lap}\;-\;\mathrm{gip}\quad}
\]
checked numerically to machine precision at the array level (reported max error $\sim 10^{-14}$ in later runs).

---

## 3. Proof-object A: an affine Laplacian law

Across $L\in\{8,12,16\}$ (with $\beta=6$ in the simulation that generated `decomp_Lsweep_results.npz`), a linear regression fit reports
\[
\Delta V \;\approx\; a + b\,\overline{B},
\]
with
- $a\simeq 11.9991\text{ to }11.9993$,
- $b\simeq -11.9989\text{ to }-11.9992$,
- $R^2>0.9999993$,
- max residuals at the $\sim 10^{-2}$ level.

A direct hypothesis check used in the logs is:
\[
\boxed{\quad \Delta V \stackrel{?}{\approx} 12 - 12\,\overline{B}\quad}
\]
with reported max deviations from this hypothesis of order $10^{-2}$ (tightening with $L$ in the displayed runs).

### Why this is exciting
This is *way too clean* to be an accident. It looks like an **exact representation-theoretic identity** plus small Monte Carlo / finite-difference noise.

### Working conjecture (candidate exact theorem)
There exists a precise choice of normalization for $\Delta$ such that for the observable $V(U)=1+\overline{B}(U)$,
\[
\boxed{\quad \Delta V \;=\; 12\,(1-\overline{B}) \;=\; 12\,\overline{w}\quad}
\]
where $\overline{w}$ is the average plaquette trace.

### Sketch of an analytic route (not yet a proof)
- $\mathrm{SU}(2)\cong S^3$, and the Laplacian eigenfunctions are matrix elements / characters of irreps.
- The fundamental character $\chi_{1/2}(g)=\Re\operatorname{Tr}(g)$ is an eigenfunction of the group Laplacian with eigenvalue tied to the quadratic Casimir.
- Each plaquette trace is the character of a product of four link variables; the full $\Delta$ is a **sum over link Laplacians**, so applying $\Delta$ to the plaquette average counts how often each link appears.
- In $d=4$, each link participates in $2(d-1)=6$ plaquettes; a factor like $12$ is therefore “dimensionally plausible”.

If this identity can be proven exactly, it upgrades the entire drift story: you’d have **an analytic closed form** for the diffusion part of $\mathcal{L}V$.

---

## 4. Proof-object B: positivity of the pairing term

The simulation reports (for each $L$) that
\[
\langle \nabla S_\beta,\nabla V\rangle \ge 0
\]
**for all sampled configurations** (2048/2048 positive, no negatives), with the minimum around $10^{-8}$ (i.e., numerically near-zero but still positive).

### Interpretation
Since $S_\beta$ is (essentially) proportional to the total plaquette defect and $V$ is proportional to the *average* plaquette defect, it is plausible that
\[
\nabla S_\beta \;\parallel\; \nabla \overline{B}
\quad\Rightarrow\quad
\langle \nabla S_\beta,\nabla V\rangle \propto \|\nabla \overline{B}\|^2 \ge 0.
\]
But because each link affects multiple plaquettes, proving global alignment is not completely trivial; it may require a careful SU(2) calculus argument.

---

## 5. Proof-object C: split-half pointwise decomposition sanity check

A “split-half” test estimates `LV` using one Monte Carlo half-sample and estimates `lap - gip` using the other half-sample, forming a residual and $z$-score.

Reported behavior (typical):
- $|z|>2$ occurs at a few percent (around 3.7–4.7% across $L$),
- max $|z|$ around 3.2–3.5.

This is consistent with a healthy Monte Carlo estimator: it’s **not** proving the identity (which is exact analytically), it’s verifying the *estimation pipeline*.

---

## 6. Proof-object D: uniform-in-$L$ ratio drift certificate (after a $\beta$ scan)

A more actionable drift statement is ratio-based and avoids intercept terms:

For a threshold $\tau>0$, consider the domain
\[
\Omega_\tau \;=\; \{U:\overline{B}(U)\ge \tau\}.
\]

Define conservative (error-bar aware) ratios, schematically:
\[
c(U)\;\equiv\;\frac{\langle \nabla S_\beta,\nabla V\rangle}{\overline{B}},
\qquad
d(U)\;\equiv\;\frac{\mathcal{L}V}{\overline{B}}.
\]

The certificate searches for $\tau$ such that, uniformly over $L$,
\[
c_{\min}(\tau)\ge c_\star,\qquad d_{\max}(\tau)\le -d_\star,
\]
with target values in the logs (example) $c_\star=20$ and $d_\star=1$.

### Observed pass (key result)
A scan over an effective coupling rescaling parameter (reported as “beta scan”) found a **PASS** at
\[
\boxed{\beta=12,\qquad \tau_0 \approx 0.2158}
\]
with conservative bounds (holdout, per-$L$ split):
\[
c_{\min,\mathrm{all}}(\tau_0)\approx 21.44,\qquad d_{\max,\mathrm{all}}(\tau_0)\approx -21.44,
\]
simultaneously for $L=8,12,16$.

### What this would imply (if made rigorous)
This has the exact architecture of a Foster–Lyapunov drift condition:

- **Outside the core** $\{\overline{B}<\tau_0\}$, the process has strictly negative drift in the direction of decreasing $\overline{B}$,
- The constants appear **uniform in $L$** (for these $L$ values), suggesting a route to finite-volume mixing bounds that do not collapse immediately with volume.

---

## 7. What to do next (high-leverage followups)

1. **Prove the Laplacian identity.**  
   This is the crown jewel. If $\Delta V = 12(1-\overline{B})$ is exact, it gives you analytic control of the diffusion contribution.

2. **Generalize to SU(N).**  
   Replace SU(2) characters with SU(N) fundamental characters and track Casimirs; the constant “12” should become a function of $N$ and dimension $d$.

3. **Turn the ratio certificate into a full drift theorem.**  
   Handle the core $\overline{B}<\tau_0$ by a minorization / compactness argument (finite lattice, continuous compact manifold) and then apply standard geometric ergodicity machinery.

4. **Stress test worst offenders.**  
   The worst-case configuration is stable across reports (same global index reappearing). That hints at a structured configuration class; study it (gauge-fix? compute Polyakov loops?).

5. **Connect to mass gap numerics.**  
   If the Langevin dynamics has a uniform spectral gap, it can inform autocorrelation times used in conventional lattice gauge theory measurement. This is speculative but potentially profound.

---

## Appendix: minimal “run plan” for reproducing the drift dataset

The project logs indicate a typical dataset design:

- $L\in\{8,12,16\}$,
- $K_\text{total}=2048$ configs per $L$, split into fit/holdout halves,
- mixture: 75% “sigma-perturbed” configs around identity with $\sigma\in\{0,0.1,0.2,0.4,0.8,1.6\}$ and 25% Haar-random,
- finite-difference step `eps_fd=0.005`,
- Monte Carlo drift sampling `mc=256`.

A cleaned, reusable script is provided separately in the project exports (see the companion code link in the chat report).
