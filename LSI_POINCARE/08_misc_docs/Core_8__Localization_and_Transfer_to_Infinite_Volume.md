---
file: Core_8__Localization_and_Transfer_to_Infinite_Volume.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_I__Localization_Algebra.md
  - Core_2__Configuration_Geometry_and_Differential_Calculus.md
  - Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set.md
  - Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md
  - Core_7__Conditioned_Exponential_Clustering_via_Inverse_Decay.md
feeds_into:
  - Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md
---

# Core-8 — Localization: from conditioned clustering to full clustering (finite volume)

## Core-8.0 Output of this file

**Definition Core-8.0.1 (scope).**  
Fix a finite periodic lattice `\Lambda_L` (Definition **A.1.3**) and coupling `\beta>0`.  
Let `\mathcal K_{\Lambda_L,\beta}` be the canonical good set from Definition **Core-5.1.2**, and let
`\mu_{\Lambda_L,\beta}^{\mathcal K}` denote the conditioned Gibbs law on `\mathcal K_{\Lambda_L,\beta}` (Definition **Core-6.1.1**).

This file proves the implication
\[
\text{(conditional exponential clustering on }\mathcal K_{\Lambda_L,\beta})
\ +\ 
\text{(typicality of }\mathcal K_{\Lambda_L,\beta})
\Longrightarrow
\text{(unconditional exponential clustering under }\mu_{\Lambda_L,\beta}).
\]

**Definition Core-8.0.2 (exported statement).**  
The main exported statement is **Theorem Core-8.3.1**, which gives an explicit exponential clustering bound for covariances under the *full* finite-volume Gibbs law `\mu_{\Lambda_L,\beta}`.

**Definition Core-8.0.3 (constants).**  
This file introduces no new named constants.  
All quantitative parameters are those from Appendix A (in particular `m_H^2`, `\alpha_W`, `\nu_P`, `m_\partial`, and the typicality exponent `c_{\mathrm{typ}}` from Assumption **A.11.2**) and the deterministic derived expression
\(
\log\bigl(1+\tfrac{m_H^2}{\alpha_W(3\nu_P)}\bigr)
\)
from Proposition **Core-7.1.3**.

---

## Core-8.1 Localization algebra: covariance decomposition across an event

**Definition Core-8.1.1 (localization event).**  
In the identities of Appendix I, we take the probability space
\((\Omega,\mathcal F,\mu) := (\mathcal M_{\Lambda_L},\mathcal B(\mathcal M_{\Lambda_L}),\mu_{\Lambda_L,\beta})\)
(Definitions **A.4.1**, **A.6.5**) and the event
\(
K := \mathcal K_{\Lambda_L,\beta}\in\mathcal F
\)
(Definition **Core-5.1.2**).

**Proposition Core-8.1.2 (localization inequality; imported).**  
For bounded measurable observables `F,G: \mathcal M_{\Lambda_L}\to\mathbb R`, Appendix **I**, Proposition **I.3.2** yields
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|
\le
\big|\mathrm{Cov}^{\mathcal K}_{\Lambda_L,\beta}(F,G)\big|
+
8\,\|F\|_\infty\,\|G\|_\infty\,\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L,\beta}^c).
\tag{8.1}
\]
No further measure-theoretic input beyond Appendix I is used in this file.

*Proof.* This is Appendix **I**, Proposition **I.3.2** with `\mu=\mu_{\Lambda_L,\beta}` and `K=\mathcal K_{\Lambda_L,\beta}`. \(\square\)

---

## Core-8.2 Typicality input and a distance conversion lemma

### Core-8.2.1 Typicality (assumed at this stage)

**Assumption Core-8.2.1 (typicality of the canonical good set).**  
Assume that the event family `K_{\Lambda_L}` from Assumption **A.11.1** is instantiated by
\(
K_{\Lambda_L}:=\mathcal K_{\Lambda_L,\beta}
\)
and that the volume-scale bound in Assumption **A.11.2** holds, i.e. there exists `c_{\mathrm{typ}}>0` such that for all sufficiently large volumes,
\[
\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L,\beta}^c)
\le
\exp\big(-c_{\mathrm{typ}}\,|P(\Lambda_L)|\big).
\tag{8.2}
\]

**Remark Core-8.2.2 (status).**  
Assumption **Core-8.2.1** is the only new hypothesis introduced in Core-8.  
It is explicitly tracked as the unique fixed-cutoff bottleneck for converting conditioned estimates into unconditional ones.

### Core-8.2.2 Converting a plaquette-count exponent to a link-distance exponent

The localization error term in (8.1) is controlled by `\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L,\beta}^c)`, which Assumption **Core-8.2.1** bounds in terms of `|P(\Lambda_L)|`.  
To combine this with the distance-dependent conditional clustering term from Core 7, we use the following deterministic comparison between `|P(\Lambda_L)|` and the link-distance `\mathrm{dist}_E`.

**Lemma Core-8.2.3 (distance is at most linear in `|P|`).**  
Let `A,B\subset E(\Lambda_L)` be finite nonempty sets of links, and let `\mathrm{dist}_E(A,B)` denote the link-graph support distance (Definition **Core-2.3.1**, built from Definition **A.2.9**). Then
\[
\mathrm{dist}_E(A,B)
\le
|E(\Lambda_L)|
\le
m_\partial\,|P(\Lambda_L)|.
\tag{8.3}
\]
In particular, for any `c>0`,
\[
\exp\big(-c\,|P(\Lambda_L)|\big)
\le
\exp\Big(-\frac{c}{m_\partial}\,\mathrm{dist}_E(A,B)\Big).
\tag{8.4}
\]

*Proof.*

**Step 1 (graph diameter bound).**  
`E(\Lambda_L)` is a finite set of vertices for the link adjacency graph (Definition **A.2.8**). Any path in a finite graph visits at most `|E(\Lambda_L)|` distinct vertices. Therefore, the graph distance between any two links is at most `|E(\Lambda_L)|-1`, and hence
\(
\mathrm{dist}_E(A,B)\le |E(\Lambda_L)|.
\)

**Step 2 (each link participates in at least one plaquette).**  
Fix a link `b=(x,\mu)\in E(\Lambda_L)`. Since `d=4` (Definition **A.1.1**), there exists some direction `\nu\in\{0,1,2,3\}` with `\nu\neq\mu`. Consider the plaquette `p=(x;\min\{\mu,\nu\},\max\{\mu,\nu\})\in P(\Lambda_L)` (Definition **A.2.3**). By the boundary convention (Definition **A.2.4**), the oriented boundary `\partial p` contains either `b` or its reversal with a nonzero incidence coefficient. In particular, every link appears in the boundary of at least one plaquette.

**Step 3 (incidence counting).**  
Each plaquette boundary consists of exactly `m_\partial` links (Definition **A.2.5**), hence the total number of (plaquette, link) incidences is exactly `m_\partial\,|P(\Lambda_L)|`. Since Step 2 shows that each link contributes at least one incidence, it follows that
\(
|E(\Lambda_L)|\le m_\partial\,|P(\Lambda_L)|.
\)
This completes (8.3).

**Step 4 (exponential consequence).**  
From (8.3),
\(
\frac{c}{m_\partial}\,\mathrm{dist}_E(A,B)\le c\,|P(\Lambda_L)|
\),
which implies (8.4) by monotonicity of the exponential. \(\square\)

---

## Core-8.3 Unconditional exponential clustering in finite volume

### Theorem Core-8.3.1 (finite-volume exponential clustering under `\mu_{\Lambda_L,\beta}`)

Let `F,G\in C^\infty(\mathcal M_{\Lambda_L})` be smooth cylinder observables with finite link supports
\(
A:=\mathrm{supp}_E(F),\ B:=\mathrm{supp}_E(G)
\)
(Definition **Core-2.1.4**).

Assume:
1. the conditional clustering bound of **Corollary Core-7.2.3** holds on `\mathcal K_{\Lambda_L,\beta}` (this is proved in Core 7, conditional only on the upstream hinge/HS inputs recorded there);
2. the typicality input **Assumption Core-8.2.1** holds.

Then the *unconditioned* covariance under `\mu_{\Lambda_L,\beta}` satisfies
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|
\le
\Big[\frac{2}{m_H^2}\,\mathsf L_E(F)\,\mathsf L_E(G)
\; +\; 8\,\|F\|_\infty\,\|G\|_\infty\Big]
\exp\Big(-\min\Big\{\log\Big(1+\frac{m_H^2}{\alpha_W(3\nu_P)}\Big),\ \frac{c_{\mathrm{typ}}}{m_\partial}\Big\}\,\mathrm{dist}_E(A,B)\Big).
\tag{8.5}
\]
Here:
- `\mathsf L_E(\cdot)` is the linkwise gradient envelope from Definition **Core-7.2.1**;
- `m_H^2`, `\alpha_W`, `\nu_P`, and `m_\partial` are from Appendix A (Definitions **A.8.3**, **A.9.1**, **A.2.6**, **A.2.5**);
- `c_{\mathrm{typ}}` is the typicality exponent from Assumption **A.11.2**.

In particular, the decay exponent in (8.5) is **uniform in the volume** (independent of `L`) once `\beta` and the typicality exponent are fixed.

*Proof.*

**Step 1 (localization inequality).**  
Apply Proposition **Core-8.1.2** to obtain
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|
\le
\big|\mathrm{Cov}^{\mathcal K}_{\Lambda_L,\beta}(F,G)\big|
+
8\,\|F\|_\infty\,\|G\|_\infty\,\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L,\beta}^c).
\tag{8.6}
\]

**Step 2 (conditional clustering bound on `\mathcal K_{\Lambda_L,\beta}`).**  
By Corollary **Core-7.2.3** and the uniform lower bound in Proposition **Core-7.1.3**–(7.2),
\[
\big|\mathrm{Cov}^{\mathcal K}_{\Lambda_L,\beta}(F,G)\big|
\le
\frac{2}{m_H^2}\,\mathsf L_E(F)\,\mathsf L_E(G)
\exp\Big(-\log\Big(1+\frac{m_H^2}{\alpha_W(3\nu_P)}\Big)\,\mathrm{dist}_E(A,B)\Big).
\tag{8.7}
\]

**Step 3 (typicality bound on `\mu(\mathcal K^c)` and distance conversion).**  
Assumption **Core-8.2.1** gives
\(
\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L,\beta}^c)\le \exp(-c_{\mathrm{typ}}|P(\Lambda_L)|)
\)
for all sufficiently large volumes.  
Lemma **Core-8.2.3**, applied to the same supports `A,B`, yields
\[
\exp(-c_{\mathrm{typ}}|P(\Lambda_L)|)
\le
\exp\Big(-\frac{c_{\mathrm{typ}}}{m_\partial}\,\mathrm{dist}_E(A,B)\Big).
\tag{8.8}
\]
Combining (8.8) with the error term in (8.6) gives
\[
8\,\|F\|_\infty\,\|G\|_\infty\,\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L,\beta}^c)
\le
8\,\|F\|_\infty\,\|G\|_\infty\,\exp\Big(-\frac{c_{\mathrm{typ}}}{m_\partial}\,\mathrm{dist}_E(A,B)\Big).
\tag{8.9}
\]

**Step 4 (combine and unify the exponent).**  
Insert (8.7) and (8.9) into (8.6). Each of the two terms has the form `C_i\,e^{-\eta_i\,\mathrm{dist}_E(A,B)}` with
\(
\eta_1=\log\big(1+\tfrac{m_H^2}{\alpha_W(3\nu_P)}\big)
\)
and
\(
\eta_2=\tfrac{c_{\mathrm{typ}}}{m_\partial}.
\)
Since
\(
\exp(-\eta_i r)\le \exp(-\min\{\eta_1,\eta_2\}\,r)
\)
for all `r\ge 0` and `i\in\{1,2\}`, the sum is bounded by the bracketed prefactor times the unified exponential, yielding (8.5). \(\square\)

---

## Core-8.4 Dependency and conditionality ledger

**Definition Core-8.4.1 (proved vs. assumed content in this file).**  
- Lemma **Core-8.2.3** and Theorem **Core-8.3.1** are proved within this file.
- Theorem **Core-8.3.1** is conditional on **Assumption Core-8.2.1** (typicality of `\mathcal K_{\Lambda_L,\beta}` in the sense of Assumption **A.11.2**).
- Theorem **Core-8.3.1** also depends on the *conditional* clustering bound **Corollary Core-7.2.3**, which is proved in Core 7 under the upstream hinge/HS inputs explicitly listed in Core 6–7.

No additional assumptions or external inputs are introduced in this file.
