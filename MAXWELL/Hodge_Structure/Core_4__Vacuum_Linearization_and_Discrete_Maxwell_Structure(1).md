---
file: Core_4__Vacuum_Linearization_and_Discrete_Maxwell_Structure.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_C__Configuration_Geometry.md
  - Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md
feeds_into:
  - Core-5 (Local coercivity / matrix hinge: identifies the Maxwell term and its coefficient)
  - Core-6 (Helffer–Sjöstrand covariance comparison: identifies the comparison operator)
  - Core-7 (Finite-range inverse decay: supplies the specific massive operator to invert)
---

# Core-4 — Vacuum linearization and the discrete Maxwell structure

## Core-4.0 Interface

**Definition (Core-4.0.1: scope).**  
Fix dimension `d=4` (Definition **A.1.1**) and a finite periodic lattice `\Lambda_L` (Definition **A.1.3**).  
All objects in this file are at **fixed cutoff** and **finite periodic volume**.

**Definition (Core-4.0.2: imported primitives).**  
The following objects and identities are used without redefinition.

- Plaquette holonomy `U_p(U)` and Wilson action `S_{\Lambda_L,\beta}`: Definitions **A.6.1–A.6.3**.
- Vacuum configuration `U^{(0)}`: Definition **A.6.4**.
- Right-trivialization at the vacuum and cochain identification: Definitions **A.4.3–A.4.4**.
- Cochain operators `d_0,d_1,d_0^*,d_1^*` and the Maxwell operator `\mathsf M_1=d_1^*d_1`: Definitions **A.5.3–A.5.6**.
- Horizontal subspace `H^{(0)}=\ker(d_0^*)` and its invariance under `\mathsf M_1`: Definition **B.3.4** and Lemma **B.4.3**.
- Vacuum holonomy linearization and vacuum Hessian identity: Propositions **D.2.2** and **D.4.3**.

**Definition (Core-4.0.3: outputs of this file).**  
This file exports exactly the following items for downstream use.

1. linearization of plaquette holonomy at the vacuum equals the discrete coboundary `d_1` (Proposition **Core-4.1.1**);
2. operator identity for the Wilson-action Hessian at the vacuum (Proposition **Core-4.2.2**);
3. the definition and basic structural properties of the **horizontal restriction** of the massive Maxwell operator (Definitions/Lemmas **Core-4.3.1–Core-4.3.4**).

**Definition (Core-4.0.4: constants).**  
This file introduces no named constants.
It references only the constants defined in Appendix **A**, in particular:
- `\alpha_W=\beta/n` (Definition **A.9.1**);
- `m_H^2` (Definition **A.8.3**);
- the massive Maxwell operator `M_{\Lambda_L}` (Definition **A.9.2**).

---

## Core-4.1 Linearization of plaquette holonomy at the vacuum

**Proposition (Core-4.1.1: plaquette holonomy linearization equals `d_1`).**  
Fix a plaquette `p\in P(\Lambda_L)` (Definition **A.2.3**) and consider the smooth map
\[
\mathrm{Hol}_p: M_{\Lambda_L}\to G,\qquad \mathrm{Hol}_p(U):=U_p(U)
\quad\text{(Definition **A.6.1**).}
\]
Identify the tangent space `T_{U^{(0)}}M_{\Lambda_L}` with the cochain space `\mathcal C^1(\Lambda_L;\mathfrak g)` by right-trivialization at `U^{(0)}` (Definitions **A.4.3–A.4.4**).

Then the differential at the vacuum is the discrete coboundary `d_1` evaluated at `p`:
\[
(d\,\mathrm{Hol}_p)_{U^{(0)}}(X)\;=\;(d_1X)_p\in\mathfrak g\cong T_{\mathbf 1}G
\qquad\text{for every }X\in\mathcal C^1(\Lambda_L;\mathfrak g).
\]

*Proof.* This is Proposition **D.2.2**. ∎

---

## Core-4.2 Vacuum Hessian of the Wilson action: Maxwell structure

**Lemma (Core-4.2.1: the vacuum is a critical point of the Wilson action).**  
\[
\nabla S_{\Lambda_L,\beta}(U^{(0)})=0.
\]

*Proof.* This is Lemma **D.4.1**. ∎

**Proposition (Core-4.2.2: vacuum Hessian identity `\nabla^2S(U^{(0)})=\alpha_W d_1^*d_1`).**  
Identify `T_{U^{(0)}}M_{\Lambda_L}` with `\mathcal C^1(\Lambda_L;\mathfrak g)` by right-trivialization (Definitions **A.4.3–A.4.4**).
Then the Riemannian Hessian of the Wilson action at the vacuum satisfies the operator identity
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})\;=\;\alpha_W\,d_1^*d_1
\qquad\text{as self-adjoint operators on }\mathcal C^1(\Lambda_L;\mathfrak g),
\]
where `\alpha_W` is the vacuum Wilson–Maxwell coefficient (Definition **A.9.1**).

Equivalently, for all `X,Z\in\mathcal C^1(\Lambda_L;\mathfrak g)`,
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,Z]
\;=\;\alpha_W\,\langle d_1X, d_1Z\rangle_{\mathcal C^2}
\;=\;\alpha_W\,\langle X, d_1^*d_1 Z\rangle_{\mathcal C^1}.
\]

*Proof.* This is Proposition **D.4.3**. ∎

---

## Core-4.3 Massive Maxwell operator and its horizontal restriction

### Core-4.3.1 The relevant cochain subspace at the vacuum

**Definition (Core-4.3.1: horizontal subspace at the vacuum; reference).**  
Let
\[
H^{(0)}:=\ker(d_0^*)\subset \mathcal C^1(\Lambda_L;\mathfrak g)
\quad\text{(Definition **B.3.4**).}
\]
This is the orthogonal complement of exact 1-cochains `\mathrm{im}(d_0)` by Lemma **B.3.3**.

### Core-4.3.2 Restricting operators to horizontals

**Definition (Core-4.3.2: horizontal restriction of an operator).**  
Let `A` be a linear operator on `\mathcal C^1(\Lambda_L;\mathfrak g)`.
Assume
\[
A\big(H^{(0)}\big)\subset H^{(0)}.
\]
Define the **horizontal restriction** of `A` to be the induced operator
\[
A_H := A\big|_{H^{(0)}}: H^{(0)}\to H^{(0)}.
\]

### Core-4.3.3 The massive Maxwell operator preserves horizontals

**Lemma (Core-4.3.3: invariance of `H^{(0)}` under the massive Maxwell operator).**  
Let `M_{\Lambda_L}` be the massive Maxwell operator (Definition **A.9.2**):
\[
M_{\Lambda_L} := m_H^2\,\mathrm{Id} + \alpha_W\,d_1^*d_1.
\]
Then
\[
M_{\Lambda_L}\big(H^{(0)}\big)\subset H^{(0)}.
\]
Consequently, the horizontal restriction `(M_{\Lambda_L})_H` is well-defined by Definition **Core-4.3.2**.

*Proof.* The identity operator preserves every subspace. By Lemma **B.4.3**, `d_1^*d_1` preserves `H^{(0)}`.
Therefore any linear combination of these two operators, in particular `M_{\Lambda_L}`, preserves `H^{(0)}`. ∎

**Definition (Core-4.3.4: horizontal massive Maxwell operator).**  
Define
\[
M_{\Lambda_L,H} := (M_{\Lambda_L})_H = M_{\Lambda_L}\big|_{H^{(0)}}.
\]

### Core-4.3.4 Positivity gap and inverse existence

**Lemma (Core-4.3.5: positivity gap).**  
The operator `M_{\Lambda_L}` satisfies the quadratic-form bound
\[
M_{\Lambda_L}\succeq m_H^2\,\mathrm{Id}
\quad\text{on }\mathcal C^1(\Lambda_L;\mathfrak g),
\]
and similarly
\[
M_{\Lambda_L,H}\succeq m_H^2\,\mathrm{Id}
\quad\text{on }H^{(0)}.
\]

*Proof.* By Lemma **B.4.1**, `d_1^*d_1\succeq 0`. Hence
\[
\langle X, M_{\Lambda_L}X\rangle_{\mathcal C^1}
= m_H^2|X|_{\mathcal C^1}^2 + \alpha_W\langle X, d_1^*d_1 X\rangle_{\mathcal C^1}
\ge m_H^2|X|_{\mathcal C^1}^2
\quad\text{for all }X\in\mathcal C^1.
\]
Restricting the inequality to `X\in H^{(0)}` yields the second bound.
(The constant `m_H^2` is strictly positive by Definition **A.8.3** together with Assumption **A.3.8**.) ∎

**Lemma (Core-4.3.6: invertibility and operator-norm bound).**  
The operators `M_{\Lambda_L}` on `\mathcal C^1(\Lambda_L;\mathfrak g)` and `M_{\Lambda_L,H}` on `H^{(0)}` are invertible. Moreover,
\[
\|M_{\Lambda_L}^{-1}\|_{\mathrm{op}}\le \frac{1}{m_H^2},
\qquad
\|M_{\Lambda_L,H}^{-1}\|_{\mathrm{op}}\le \frac{1}{m_H^2}.
\]

*Proof.* If a self-adjoint operator `A` satisfies `A\succeq c\,\mathrm{Id}` with `c>0`, then `A` is invertible and `\|A^{-1}\|_{\mathrm{op}}\le c^{-1}` (finite-dimensional spectral theorem).
Apply this to `A=M_{\Lambda_L}` and `A=M_{\Lambda_L,H}` with `c=m_H^2` using Lemma **Core-4.3.5**. ∎

---

## Core-4.4 Dependency notes (non-normative)

**Definition (Core-4.4.1: “feeds into” map at statement level).**

- Proposition **Core-4.1.1** feeds into Proposition **Core-4.2.2** via Appendix **D** and is used implicitly whenever the Maxwell operator is identified as the vacuum linearization of plaquette holonomy.

- Proposition **Core-4.2.2** feeds into Core-5 (coercivity/curvature lower bounds), where the Maxwell term appears as the “stiff” part of the curvature matrix.

- Definitions/Lemmas **Core-4.3.1–Core-4.3.6** feed into Core-6 and Core-7, where the inverse `M_{\Lambda_L,H}^{-1}` is compared to covariance and its kernel is estimated.

No other statement in later files may cite Core-4 unless it cites one of the numbered items in this file.
