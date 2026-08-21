---
file: Core_1__Lattice_Gauge_Model_at_Fixed_Cutoff.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_C__Configuration_Geometry.md
feeds_into:
  - Core-2 (Configuration geometry and differential calculus)
  - Core-3 (OS framework at fixed cutoff)
  - Core-4 (Vacuum linearization and the discrete Maxwell structure)
  - Core-7 (Fixed-cutoff exponential clustering)
  - Core-8 (Thermodynamic limit at fixed cutoff)
---

# Core-1 — Lattice gauge model at fixed cutoff

## Core-1.0 Interface

**Definition (Core-1.0.1: scope).**  
Fix dimension `d=4` and a finite periodic lattice `\Lambda_L` as in Definition **A.1.3**.  
All objects in this file live at **fixed cutoff** (fixed lattice spacing, suppressed in the notation) and at **finite periodic volume**.

**Definition (Core-1.0.2: imported primitives).**  
The following primitives are used without redefinition:
- cell sets and orientations: Definitions **A.2.1–A.2.6** (with detailed cellular bookkeeping in Appendix **B**);
- configuration manifold and product Haar/Riemannian volume: Definitions **A.4.1–A.4.7** and Lemma **C.3.3**;
- plaquette holonomy and Wilson action: Definitions **A.6.1–A.6.3**;
- Gibbs measure, expectation, covariance: Definitions **A.6.5–A.6.6**;
- lattice gauge group and gauge action: Definitions **C.3.1–C.3.2**.

**Definition (Core-1.0.3: output of this file).**  
This file introduces:
1. path and loop holonomy as products of link variables (Definitions Core-1.1.1–Core-1.1.4);
2. the conjugation-covariance of holonomy under gauge transformations (Lemma Core-1.2.1);
3. a canonical family of gauge-invariant “loop class observables” (Proposition Core-1.2.2);
4. gauge invariance of the Wilson action and Gibbs measure (Proposition Core-1.3.1).

---

## Core-1.1 Paths and holonomy

**Definition (Core-1.1.1: oriented link symbols with reversal).**  
Let `E(\Lambda_L)` be the positively oriented link set (Definition **A.2.2**).  
Write `E^{\pm}(\Lambda_L)` for the set of oriented link symbols obtained by adjoining formal reversals `b^{-1}` for `b\in E(\Lambda_L)`.  
Reversal of link variables is always interpreted by Definition **A.2.4**:
`U_{b^{-1}} := U_b^{-1}`.

**Definition (Core-1.1.2: head and tail of an oriented link symbol).**  
For an oriented link `b=(x,\mu)\in E(\Lambda_L)`, its tail and head are
`\partial_- b := x` and `\partial_+ b := x+\hat e_\mu` (Definitions **A.2.2** and **A.1.4**).  
For the reversed symbol `b^{-1}`, set
`\partial_- (b^{-1}) := \partial_+ b` and `\partial_+ (b^{-1}) := \partial_- b`.

**Definition (Core-1.1.3: (nearest-neighbor) path).**  
A (nearest-neighbor) path in `\Lambda_L` is a finite sequence of oriented link symbols
`\gamma=(b_1,\dots,b_m)` with each `b_i\in E^{\pm}(\Lambda_L)` such that
`\partial_+ b_i = \partial_- b_{i+1}` for every `i\in\{1,\dots,m-1\}`.

The initial vertex and terminal vertex of `\gamma` are
`\partial_-\gamma := \partial_- b_1` and `\partial_+\gamma := \partial_+ b_m`.

**Definition (Core-1.1.4: path holonomy).**  
Let `U\in M_{\Lambda_L}`. The holonomy of `U` along a path `\gamma=(b_1,\dots,b_m)` is the group element
\[
U_{\gamma}(U) := U_{b_1}\,U_{b_2}\cdots U_{b_m}\in G,
\]
where each factor is interpreted using the reversal convention `U_{b^{-1}}:=U_b^{-1}`.

**Definition (Core-1.1.5: loop).**  
A path `\gamma` is a loop if `\partial_-\gamma=\partial_+\gamma`.  
In that case, `U_{\gamma}(U)` is called the loop holonomy.

---

## Core-1.2 Gauge covariance and gauge-invariant loop observables

**Lemma (Core-1.2.1: gauge covariance of path holonomy).**  
Let `g\in\mathcal G_{\Lambda_L}` act on configurations by Definition **C.3.2**, and let `\gamma=(b_1,\dots,b_m)` be a path.
Then for every configuration `U\in M_{\Lambda_L}`,
\[
U_{\gamma}(g\cdot U) = g_{\partial_-\gamma}\,U_{\gamma}(U)\,g_{\partial_+\gamma}^{-1}.
\]

*Proof.*  
Write `x_0:=\partial_-\gamma` and for `i\ge 1` set `x_i:=\partial_+ b_i=\partial_- b_{i+1}` (so `x_m=\partial_+\gamma`).  
For each positively oriented link `b=(x,\mu)\in E(\Lambda_L)`, Definition **C.3.2** gives
`(g\cdot U)_b = g_x\,U_b\,g_{x+\hat e_\mu}^{-1}`; for the reversed symbol `b^{-1}` this implies
`(g\cdot U)_{b^{-1}} = ((g\cdot U)_b)^{-1} = g_{\partial_+ b}\,U_{b^{-1}}\,g_{\partial_- b}^{-1}`.
Thus, for every oriented symbol `b\in E^{\pm}(\Lambda_L)` one has the uniform identity
\[
(g\cdot U)_b = g_{\partial_- b}\,U_b\,g_{\partial_+ b}^{-1}.
\]
Multiplying this identity along `\gamma=(b_1,\dots,b_m)` and using the path-adjacency constraints
`\partial_+ b_i=\partial_- b_{i+1}`, the intermediate factors telescope:
\[
\begin{aligned}
U_{\gamma}(g\cdot U)
&= \prod_{i=1}^m (g\cdot U)_{b_i}
 = \prod_{i=1}^m \big(g_{\partial_- b_i}\,U_{b_i}\,g_{\partial_+ b_i}^{-1}\big) \\
&= g_{x_0}\,\Big(\prod_{i=1}^m U_{b_i}\Big)\,g_{x_m}^{-1}
 = g_{\partial_-\gamma}\,U_{\gamma}(U)\,g_{\partial_+\gamma}^{-1}.
\end{aligned}
\]
∎

**Definition (Core-1.2.2: class functions and loop class observables).**  
A function `\Psi:G\to\mathbb C` is a class function if
`\Psi(h V h^{-1})=\Psi(V)` for all `h,V\in G`.

Given a loop `\gamma`, define the associated loop class observable
\[
F_{\gamma,\Psi}(U) := \Psi\big(U_{\gamma}(U)\big),
\qquad U\in M_{\Lambda_L}.
\]

**Proposition (Core-1.2.3: loop class observables are gauge invariant).**  
If `\gamma` is a loop and `\Psi` is a class function, then
\[
F_{\gamma,\Psi}(g\cdot U)=F_{\gamma,\Psi}(U)
\qquad\text{for all }g\in\mathcal G_{\Lambda_L},\ U\in M_{\Lambda_L}.
\]

*Proof.*  
Since `\gamma` is a loop, `\partial_-\gamma=\partial_+\gamma`. By Lemma Core-1.2.1,
`U_{\gamma}(g\cdot U)=g_{\partial_-\gamma}\,U_{\gamma}(U)\,g_{\partial_-\gamma}^{-1}`.
Apply the class-function identity for `\Psi` to conclude
\[
F_{\gamma,\Psi}(g\cdot U)
=\Psi\big(U_{\gamma}(g\cdot U)\big)
=\Psi\big(g_{\partial_-\gamma}U_{\gamma}(U)g_{\partial_-\gamma}^{-1}\big)
=\Psi\big(U_{\gamma}(U)\big)
=F_{\gamma,\Psi}(U).
\]
∎

---

## Core-1.3 Wilson action and Gibbs measure: gauge invariance

**Proposition (Core-1.3.1: gauge invariance of the Wilson action).**  
The Wilson action `S_{\Lambda_L,\beta}` (Definition **A.6.3**) is gauge invariant:
\[
S_{\Lambda_L,\beta}(g\cdot U)=S_{\Lambda_L,\beta}(U)
\qquad\text{for all }g\in\mathcal G_{\Lambda_L},\ U\in M_{\Lambda_L}.
\]

*Proof.*  
By Definition **A.6.3**, the action is a sum over plaquettes `p\in P(\Lambda_L)` of the single-plaquette potential
`\Phi_\beta(U_p(U))`, where `U_p(U)` is the plaquette holonomy (Definition **A.6.1**) and `\Phi_\beta` is defined in **A.6.2**.

Each plaquette boundary is a loop in the sense of Definition Core-1.1.5 (with the same ordered product as in Definition **A.6.1**),
so Lemma Core-1.2.1 applies with `\gamma=\partial p` to give
`U_p(g\cdot U)=g_x\,U_p(U)\,g_x^{-1}` for the plaquette basepoint `x` (the initial vertex of the loop, determined by the convention in **A.6.1**).

Finally, `\Phi_\beta(V)=\beta\big(1-\frac1n\Re\mathrm{Tr}(V)\big)` is a class function because `\Re\mathrm{Tr}(h V h^{-1})=\Re\mathrm{Tr}(V)` for all `h,V\in G`. Thus
`\Phi_\beta(U_p(g\cdot U))=\Phi_\beta(U_p(U))` for each plaquette `p`. Summing over plaquettes yields the claim. ∎

**Proposition (Core-1.3.2: gauge invariance of the Gibbs measure).**  
The Gibbs measure `\mu_{\Lambda_L,\beta}` (Definition **A.6.5**) is invariant under the gauge action:
for every bounded measurable `F:M_{\Lambda_L}\to\mathbb C` and every `g\in\mathcal G_{\Lambda_L}`,
\[
\mathbb E_{\Lambda_L,\beta}[F\circ\Phi_g] = \mathbb E_{\Lambda_L,\beta}[F],
\qquad \Phi_g(U):=g\cdot U.
\]

*Proof.*  
By Definition **A.6.5**,
`\mu_{\Lambda_L,\beta}(dU) = Z_{\Lambda_L,\beta}^{-1} e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(dU)`.

1. By Lemma **C.3.3**, the gauge map `\Phi_g` is volume preserving:
`(\Phi_g)_*\mathrm{vol}_{g_{\Lambda_L}}=\mathrm{vol}_{g_{\Lambda_L}}`.

2. By Proposition Core-1.3.1, the density is gauge invariant:
`S_{\Lambda_L,\beta}(\Phi_g(U))=S_{\Lambda_L,\beta}(U)`.

Therefore the pushforward measure satisfies `(\Phi_g)_*\mu_{\Lambda_L,\beta}=\mu_{\Lambda_L,\beta}`.
Equivalently, for bounded measurable `F`,
\[
\mathbb E_{\Lambda_L,\beta}[F\circ\Phi_g]
=\int F(\Phi_g(U))\,d\mu_{\Lambda_L,\beta}(U)
=\int F(U)\,d\mu_{\Lambda_L,\beta}(U)
=\mathbb E_{\Lambda_L,\beta}[F].
\]
∎

---

## Core-1.4 Dependency notes (non-normative)

**Definition (Core-1.4.1: direct uses downstream).**  
The only results from this file used downstream are:
- Lemma Core-1.2.1 and Proposition Core-1.2.3 (to justify gauge invariance of the admissible observable class);
- Proposition Core-1.3.1–Core-1.3.2 (to justify gauge invariance of the Gibbs law, and later gauge-equivariance of derived operators).

No other statement in later files may cite Core-1 unless it cites one of the numbered items above.
