# What is still missing for a Yang–Mills mass-gap proof (and the clean next steps)

## 0. Keep your map honest

The salvage stack gives a rigorous *mechanism*:

> If you can maintain a uniform Bakry–Émery curvature lower bound under coarse-graining, then LSI + spectral gap + clustering + OS reconstruction give a mass gap.

Yang–Mills is hard because the hypotheses are hard—not because the mechanism is vague.

Below is the smallest set of missing statements that would turn the current project into an actual Yang–Mills theorem.

---

## 1. The three missing pillars

### (P1) A **correct coordinate chart** where convexity is meaningful

The Haar Jacobian computation is local in exponential coordinates. For a theorem you need a globally correct formulation:

- Either restrict to a principal branch of $\log:SU(N)\to\mathfrak{su}(N)$ and prove measure concentration in that chart,
- or formulate everything directly on $G^{\mathcal{B}}$ using Riemannian geometry (no global $A$-coordinates).

**Deliverable:** a clean lemma specifying the coordinate domain and proving it captures the relevant measure with high probability.

### (P2) **Measure concentration in the convex core**, uniformly in volume

Your SU(3) Hessian scans map where the action is locally convex as a function of $(\beta,\text{scale},L)$.
That is not enough.

You need a statement of the form:

> There exists a window $\beta\in[\beta_-,\beta_+]$ and constants $c,\varepsilon>0$ such that for all volumes,
> $$\mu_{\beta}^{(L)}\big(\mathcal{C}_\beta\big)\ge \varepsilon,$$
> where $\mathcal{C}_\beta$ is a region on which $\nabla^2 S_{\rm eff}\succeq cI$.

Even a weaker “overwhelming probability” statement would be gold.

**Clean next computation:** sample in **$U$-space** (true Haar + Wilson weight), map to a principal $A(U)$, and estimate
$$\mathbb{P}(A(U)\in\mathcal{C}_\beta)$$
for multiple $L$.

### (P3) A **coarse-graining map** for YM that preserves the curvature bound

The vHJ/Hessian-flow Riccati story is rigorously true for certain finite-dimensional PDE models. For Yang–Mills you need a coarse-graining scheme that fits into that template.

Two realistic targets:

1. **Restricted sector RG:** prove the effective action remains in a convex family for a finite number of RG steps in a strong-coupling window.
2. **Inequality-based RG:** avoid an explicit RG equation; instead prove a *curvature comparison inequality* between scales.

**Deliverable:** a theorem of the form
$$\rho_{\ell'} \ge F(\rho_\ell, \ell,\ell')$$
for Bakry–Émery constants $\rho_\ell$ along the chosen coarse-graining.

---

## 2. The “one clean next step” (do this before writing more theorems)

Your best immediate move is to **separate modeling artifacts from physics**:

1. Sample $U$ with a standard lattice algorithm (even naive link Metropolis is fine for a first pass).
2. Compute a consistent principal-log $A(U)$ per link.
3. Measure both:
   - the norm distribution of $A(U)$,
   - and the fraction of samples with $\lambda_{\min}(\nabla^2 S_{\rm eff})>0$.

If the convex-core probability collapses with $L$, you learn exactly what must be fixed.
If it stays stable, you have a real bridge from the convexity engine to the curvature-to-gap theorem.

---

## 3. How the q-Racah pillar fits (and what it does *not* claim)

The q-Racah Doob model shows a tunable, nontrivial spectral gap that closes as $q\to 1$ with clean scaling. It does not prove YM.

What it **does** provide is a reusable template:

- a deformation parameter controlling gap stability,
- a transfer-operator embedding where a boundary observable tracks a bulk gap,
- a controlled failure mode when the construction leaves the “safe region.”

That template is exactly what you want when you later define YM-inspired transfer operators and ask whether their subleading eigenvalues remain separated.

---

## 4. A sanity rule (prevents 90% of self-inflicted pain)

Never mix these three claims:

1. “The action is locally convex in a region.”  
2. “The measure spends most of its time in that region.”  
3. “Curvature bounds persist under coarse-graining.”

Your current project has (1) numerically and (2)/(3) partially as a program.
The next step is to nail (2) decisively with correct sampling, then (3) with a precise coarse-graining inequality.
