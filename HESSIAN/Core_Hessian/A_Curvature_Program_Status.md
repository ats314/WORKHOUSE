# A. Curvature–Convexity Program: What’s Solid, What’s Conjectural, What’s Next

This document is the “blueprint layer”: a cleaned version of the program that keeps **proven statements** separate from **assumptions** and **numerical evidence**.

The core idea is to turn *local* convexity into a *global* spectral gap (mass scale) using:
1. **Local Bakry–Émery (BE) curvature** on a convex core,
2. **Tail/outlier control + Lyapunov drift** to patch local → global inequalities,
3. A **coarse-graining / smoothing flow** that drives typical configurations into the core quickly enough.

That combination is the conceptual engine. The hard part is making the steps uniform in lattice spacing \(a\) (continuum limit).

---

## A1. Static finite-cutoff chain (rigorous if assumptions verified)

Work on a finite lattice \(\Lambda\) with link variables \(U_\ell \in SU(3)\).  
In an exponential chart around the identity,
\[
U_\ell = \exp(A_\ell),\qquad A_\ell \in \mathfrak{su}(3),
\]
the (local) chart density is
\[
dU_\ell = J(A_\ell)\,dA_\ell,\qquad S_{\rm Haar}(A_\ell) := -\log J(A_\ell).
\]

Define the effective action in chart coordinates:
\[
S_{\rm eff}(A) \;=\; \sum_{\ell\in L} S_{\rm Haar}(A_\ell)\;+\;\beta\sum_{p} S_W(U_p(A)),
\]
where \(S_W(U_p)=1-\frac{1}{3}\Re\operatorname{Tr}(U_p)\) is the Wilson plaquette action.

### Step 1: Local BE curvature on a convex core
If on a domain (“convex core”)
\[
\mathcal{C}_R := \{A:\ \|A_\ell\|\le R\ \forall \ell\},
\]
we can prove
\[
\nabla^2 S_{\rm eff}(A)\ \succeq\ \rho_{\beta,R}\, I\qquad \forall A\in\mathcal{C}_R,
\]
then the restricted Gibbs measure
\[
d\mu_{\beta,R}(A)\ \propto\ e^{-S_{\rm eff}(A)}\,1_{\mathcal{C}_R}(A)\,dA
\]
satisfies local functional inequalities (Poincaré / LSI) with constants controlled by \(\rho_{\beta,R}\).

This part is standard (Brascamp–Lieb / Bakry–Émery), but **verifying \(\rho_{\beta,R}>0\)** for SU(3) Wilson+Haar is nontrivial.

### Step 2: Patch local → global
To get global Poincaré/LSI for the full measure \(d\mu_\beta \propto e^{-S_{\rm eff}}dA\), one typically needs something like:

- a **Lyapunov drift condition** for the Langevin generator \(L\), and/or
- a **measure decomposition**: “good core + exponentially small outliers”.

This is where Haar compactness geometry matters: there is no globally quadratic drift in algebra coordinates, so any global argument must be genuinely geometric (group-distance tails, not fake Euclidean tails).

### Step 3: Gap \(\Rightarrow\) mass scale (at fixed cutoff)
On a finite lattice, a global Poincaré inequality implies a **spectral gap** for the Langevin generator / transfer operator, hence exponential decay of correlations and a mass scale in the reconstructed theory (at fixed cutoff).

---

## A2. Where numerics enter: mapping the convexity window

A useful numerical proxy for “local BE curvature on a core” is to measure the smallest Hessian eigenvalue \(\lambda_{\min}\) of the effective action at configurations with controlled amplitude.

The project implemented a fast SU(3) scanner:

- Parameterize \(A_\ell\in\mathfrak{su}(3)\) by 8 real coordinates per link.
- Use a stable **Padé(2,2)** approximation for \(\exp(A)\) in FP32.
- Estimate \(\lambda_{\min}\) via **Hessian-vector products + Lanczos** (no explicit Hessian).

This produces the empirical convexity boundary:
\[
\lambda_{\min}(\beta, {\rm scale};L)\ \gtrless\ 0
\quad\Rightarrow\quad
\text{“convex” vs “non-convex” region}.
\]

The main outcome: across \(L=4,6,8\), the boundary is highly consistent and roughly fits
\[
R_{\rm conv}(\beta)\ \sim\ \frac{\text{const}}{\sqrt{\beta}},
\]
with an inferred constant consistent with an “effective Wilson Hessian constant” of order \(\sim 10\)–\(20\) under the project’s normalization.

(Details and the full tables are in **E\_SU3\_Convexity\_Engine\_and\_Results.md**.)

---

## A3. The real bottleneck: continuum scaling (“race condition”)

The continuum limit requires \(a\to 0\) and typically \(\beta(a)\to\infty\).

Even if at each fixed \(a\) there is a core radius \(R_{\rm conv}(\beta)\) where
\[
\nabla^2 S_{\rm eff}\ \succeq\ \rho_{\beta} I,
\]
that radius usually shrinks as \(\beta\) grows (in the scan it scales \(\sim \beta^{-1/2}\)).

The *race condition* is:

- Typical UV fluctuations become rougher as \(a\to 0\),
- The convexity core shrinks as \(\beta(a)\to\infty\),
- You need a multi-scale argument showing typical configurations are driven into the core quickly enough (by RG/flow) **uniformly in \(a\)**.

This is exactly the kind of statement that currently looks **frontier-level**: it blends
constructive RG, functional inequalities, and nonlinear geometric tails.

---

## A4. What this export treats as “high potential”

The pieces most likely to scale into something bigger (with real work) are:

1. **The convexity scanner** + empirical scaling collapse across \(L\)  
   (valuable for calibrating constants and testing conjectures).

2. **Haar small-field Hessian lemma** (clean, local, analytic, and essential).

3. **Capacity/polarity handling of Gribov / reducible strata**  
   (removes an entire class of gauge-fixing singularity worries—*if* the comparison step is nailed).

4. **q-Racah / Doob and composite \(T_q\)**  
   (exactly solvable spectral-gap toy model that mimics multiscale coarse-graining; useful as a “laboratory” for the race condition).

---

## A5. What this export does *not* claim

- It does **not** claim: “Uniform-in-\(a\) BE curvature is proven for SU(3) Wilson+Haar.”
- It does **not** claim: “Continuum Yang–Mills mass gap is proven.”
- It does **not** claim: “The RG/flow always restores convexity from arbitrary unstable configurations.”

Instead it gives a **clean set of fragments** that can be carried into a new chat / new workspace without memory overflow.

---
