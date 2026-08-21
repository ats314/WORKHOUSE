# Selection Report: Novel/High-Leverage Derivations in the Project Files

## Executive summary

After reading the project files, **five** clusters stood out as both (i) high leverage for the overall mass-gap program and (ii) structurally *novel* in how they combine established mathematics into a new pipeline:

1. **Haar–Wilson Bakry–Émery Mass Mechanism (lattice, horizontal)**  
   A geometric inequality: Haar Ricci curvature \(\kappa>0\) plus Wilson-Hessian positivity on horizontals \(\beta c_W\) yields a Bakry–Émery lower bound \(\kappa+\beta c_W\), giving local Poincaré/log-Sobolev constants and a “mass-like” scale.【152:0†SYNTH_P04_haar_geometry_supplement.md†L5-L36】

2. **Explicit finite-lattice Log–Sobolev inequality with group-theoretic constant \(c_0\)**  
   The project spells out an explicit LSI
   \[
   \operatorname{Ent}_\mu(f^2)\le \frac{2}{c_0}\int|\nabla f|^2\,d\mu,\qquad c_0=\frac{N^2-1}{2N},
   \]
   for lattice YM on \(SU(N)^{\text{bonds}}\), derived from a curvature estimate \(\rho=c_0\).【211:0†SYNTH_P10_log_sobolev.md†L13-L20】

3. **Projected Bochner–Hessian (PBH) flow and Riccati comparison (RG stability engine)**  
   A bespoke flow equation for the *projected horizontal Hessian* along RG time:
   \[
   \partial_t h_t=\Delta_H h_t-2\nabla_{V_t}h_t-2h_t^2+S_{\mathrm{anom}}(t)+\mathfrak G(S_t,h_t),
   \]
   enabling Hamilton-style tensor maximum principles and reduction to a Riccati inequality for the minimum eigenvalue.【156:8†SYNTH_P14_rg_flow_stability.md†L10-L20】

4. **Polarity of reducibles + stratified parabolic maximum principle (singularity removal mechanism)**  
   If the reducible locus \(\Sigma\) has capacity zero (is polar), then supersolution positivity propagates on the regular stratum as if \(\Sigma\) were absent.【152:10†SYNTH_P20_stratified_parabolic_principle.md†L23-L27】  
   Supporting geometry: tangent to reducibles has infinite codimension (via an infinite-rank commutator map).【152:1†SYNTH_P18_gaussian_polarity.md†L31-L41】

5. **Conjecture A “Log-Forest UV Control” reframed as Dirichlet-form well-posedness**  
   A proposed interface between perturbative renormalization (BPHZ forests) and diffusion/Dirichlet-form analysis: after renormalization, energy/gradient norms of gauge-invariant observables have at worst polylog UV divergences, making the continuum Dirichlet form meaningful.【201:0†SYNTH_CONJ_A_log_forest_uv.md†L57-L65】

I extracted these into standalone Markdown+LaTeX notes (Docs 1–5) plus this report. Most other files are either:

- standard supporting machinery (Bakry–Émery \(\Rightarrow\) Poincaré/LSI, Riccati ODE comparison, tightness-from-LSI), or
- program scaffolding for the continuum limit (important, but not where the new technical “gear trains” are).

---

## What I selected and why

### 1) Haar–Wilson Bakry–Émery mass mechanism

**What it is.**  
The project isolates a concrete geometric inequality on lattice configuration space that looks and behaves like a “mass term” for physical modes:
\[
\mathrm{Ric}_{\mu_\beta}\big|_{\mathrm{horizontal}}
=
\mathrm{Ric}_g+\nabla^2 S_\beta
\;\ge\;
(\kappa+\beta c_W)\,g.
\]
This appears explicitly in the Haar-geometry supplement: Haar Ricci gives \(\kappa g\) and Wilson Hessian gives \(\beta c_W\) on horizontals, so the Bakry–Émery tensor is bounded below by \(\kappa+\beta c_W\).【152:0†SYNTH_P04_haar_geometry_supplement.md†L5-L36】

**Why it’s exciting.**  
This is a tidy “mass-from-curvature” mechanism: you get a positive functional-inequality constant (hence a spectral gap/mixing rate) from *intrinsic geometry + action convexity on physical directions*, rather than from a delicate long-distance argument.

**Why it’s plausibly novel.**  
All ingredients are classical (Ricci of compact Lie groups, Wilson action expansion, Bakry–Émery calculus), but the *assembly* into a gauge-invariant horizontal Bakry–Émery curvature bound interpreted as “effective mass” is not a standard viewpoint in lattice YM proof strategies.

---

### 2) Explicit finite-lattice Log–Sobolev inequality with \(c_0=(N^2-1)/(2N)\)

**What it is.**  
In `SYNTH_P10_log_sobolev.md`, the project specializes the standard Bakry–Émery LSI to the lattice YM setting using a curvature estimate \(\rho=c_0\), yielding the explicit inequality
\[
\operatorname{Ent}_\mu(f^2) \le \frac{2}{c_0} \int |\nabla f|^2 d\mu,
\qquad c_0=\frac{N^2-1}{2N}.
\]【211:0†SYNTH_P10_log_sobolev.md†L13-L20】

**Why it’s exciting.**  
An explicit LSI constant is “hard currency” for:
- concentration bounds,
- mixing/exponential decay,
- and tightness/compactness arguments used in continuum limits.

Even if the constant ultimately needs qualifications (e.g., horizontals-only, local tube, dependence on gauge-fixing), the *form* of the result is extremely valuable.

---

### 3) PBH flow and Riccati reduction (RG stability engine)

**What it is.**  
PBH is explicitly written as
\[
\partial_t h_t
=
\Delta_H h_t
-2\nabla_{V_t}h_t
-2h_t^2
+S_{\mathrm{anom}}(t)
+\mathfrak G(S_t,h_t),
\tag{PBH}
\]
where \(h_t=\nabla_H^2S_t\) is the projected horizontal Hessian.【156:8†SYNTH_P14_rg_flow_stability.md†L10-L20】

From this, the project derives a conditional persistence theorem: under (Curv)+(Trace bound)+(Anom)+(Asymptotic freedom)+(Initial gap), the minimum eigenvalue stays bounded below by a positive constant for large RG times.【156:12†SYNTH_P14_rg_flow_stability.md†L47-L53】

**Why it’s exciting.**  
PBH is a translation layer between RG and geometric analysis: it turns the gap problem into a parabolic-tensor maximum principle problem plus ODE comparison. That is an unusually clean reduction.

**Why it’s plausibly novel.**  
`SYNTH_P17_trace_bound.md` itself flags PBH as appearing to be original and not standard in YM/RG literature.【156:15†SYNTH_P17_trace_bound.md†L31-L32】

---

### 4) Polarity + stratified parabolic maximum principle (singularity removal)

**What it is.**  
The key P20 positivity statement is: for a supersolution \(\partial_t u\ge Lu+F(u)\) on the regular stratum, assuming \(\Sigma\) is polar (capacity zero), one has positivity propagation \(u(0)\ge 0\Rightarrow u(t)\ge 0\).【152:10†SYNTH_P20_stratified_parabolic_principle.md†L23-L27】

Supporting geometry comes from P18’s infinite codimension argument: the commutator map \(T_\xi(a)=[a,\xi]\) has infinite rank, so \(\ker T_\xi\) (tangent to reducibles) has infinite codimension.【152:1†SYNTH_P18_gaussian_polarity.md†L31-L41】

**Why it’s exciting.**  
This is a clever way to neutralize a notorious gauge-theory headache: singular strata don’t cooperate with classical PDE maximum principles. Capacity/polarity gives a principled criterion for when you can ignore them.

---

### 5) Conjecture A “Log-Forest UV Control” as a Dirichlet-form well-posedness principle

**What it is.**  
Conjecture A asserts a UV bound on renormalized gradients (at worst polylog) for gauge-invariant observables, organized by forest/BPHZ combinatorics.【201:0†SYNTH_CONJ_A_log_forest_uv.md†L57-L65】  

**Why it’s exciting.**  
It reframes “UV renormalization” in a language that directly serves the diffusion/functional-inequality program: it’s a conjecture about whether the *energy* \(\int\|\nabla O\|^2\,d\mu\) exists after renormalization, i.e. whether the continuum Dirichlet form is even well-posed on a rich observable algebra.

This interface between perturbative QFT (forests) and Dirichlet forms is a genuine “new theory seed”: even partial results here would clarify what a Bakry–Émery/semigroup approach can reasonably demand from renormalization.

---

## How the pieces connect into a larger theory

The project’s emerging “big picture” can be read as a five-part mechanism:

1. **Geometric seed positivity at the cutoff scale**  
   Haar geometry and Wilson Hessian generate a positive Bakry–Émery curvature lower bound on physical directions near the identity sector.

2. **Functional-inequality conversion**  
   Curvature bounds convert into explicit Poincaré/LSI constants, giving quantitative spectral gaps/mixing on the cutoff theory.

3. **RG-time propagation/stabilization of a spectral lower bound**  
   PBH gives a parabolic evolution equation for the Hessian. Under positive anomaly forcing and \(O(g^2)\) control of geometric corrections, the minimum eigenvalue satisfies a Riccati inequality driven to a positive equilibrium.

4. **Stratified-space safety**  
   If reducibles are polar/capacity-zero, maximum principles apply on the regular stratum without boundary terms, letting the PBH/maximum-principle reasoning survive the quotient singularities.

5. **Continuum well-posedness via UV control**  
   Conjecture A is the missing “renormalization-to-Dirichlet-form” interface: it is meant to guarantee that the diffusion/functional-inequality machinery is meaningful at all in 4D.

This package is “curvature-flow mass generation”: **curvature gives the seed; flow gives persistence; polarity removes singularities; UV control makes the continuum analytic objects exist.**

---

## What further work would most effectively expand the theory

Highest-payoff next steps (ordered by how much they upgrade conditional pieces to rigorous ones):

1. **Make Conjecture B (anomaly source positivity) precise and prove it in at least one RG scheme.**  
   The conjectural decomposition appears as
   \[
   \frac{dH_{\mathrm{phys}}}{dt}=-H_{\mathrm{phys}}^2+S_{\mathrm{Haar}}+S_{\mathrm{anom}}+O(g^4).
   \]【156:0†SYNTH_CONJ_B_anomaly_source.md†L36-L40】

2. **Turn “infinite codimension” into an actual capacity-zero (polarity) theorem.**  
   P18 supplies a robust infinite-codimension mechanism; the missing step is a direct capacity bound or a countable decomposition into known polar sets in an abstract Wiener space/Dirichlet-form framework.

3. **Derive PBH with full control of \(\mathfrak G(S_t,h_t)\) and verify (Curv)+(Trace) quantitatively.**  
   P14 states a bound of \(\mathfrak G\) by \(g(t)^2\|h_t\|_{\mathrm{Tr}}\) as the key control knob.【156:8†SYNTH_P14_rg_flow_stability.md†L22-L30】

4. **Upgrade “local/horizontal” curvature bounds to global/uniform ones.**  
   This is where large-angle configurations, gauge-fixing, and potential Gribov obstructions enter.

5. **Uniformity across volume and the continuum limit.**  
   `SYNTH_P11_continuum_limit.md` makes clear that Conjectures B/C/D are the main blockers for the full constructive program, even given the lattice achievements.【156:7†SYNTH_P11_continuum_limit.md†L57-L64】

6. **Bridge from “local-sector spectral gap” to physical mass gap** (OS reconstruction).  
   This is the Conjecture D-style step: turning Euclidean spectral/mixing statements into a Minkowski mass gap.

---

## Deliverables produced

Standalone Markdown+LaTeX notes capturing the extracted “best and most exciting” material:

1. `DOC1_Haar_Wilson_Bakry_Emery_Mass_Mechanism.md`  
2. `DOC2_PBH_Flow_Riccati_Comparison_Gap_Persistence.md`  
3. `DOC3_Polarity_and_Stratified_Parabolic_Max_Principle.md`  
4. `DOC4_Explicit_LSI_and_Spectral_Gap_from_Haar_Mass.md`  
5. `DOC5_Conjecture_A_Log_Forest_UV_Control.md`  

These are designed to be reusable as paper backbones: each isolates a mechanism with clean assumptions, derivations, and a short list of missing steps needed for full rigor.
