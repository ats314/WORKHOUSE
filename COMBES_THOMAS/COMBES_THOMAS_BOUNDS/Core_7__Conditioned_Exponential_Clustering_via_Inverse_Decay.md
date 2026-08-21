---
file: Core_7__Conditioned_Exponential_Clustering_via_Inverse_Decay.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md
  - Core_2__Configuration_Geometry_and_Differential_Calculus.md
  - Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set.md
  - Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md
feeds_into:
  - Core_8__Localization_and_Transfer_to_Infinite_Volume.md
---

# Core-7 — Conditioned exponential clustering via inverse decay

## Core-7.0 Output of this file

**Definition Core-7.0.1 (scope).**  
Fix a periodic box `\Lambda_L` (Definition **A.1.3**) and a coupling `\beta>0`.  
Let `\mathcal K_{\Lambda_L,\beta}` be the canonical good set (Definition **Core-5.1.2**) and let
`\mu_{\Lambda_L,\beta}^{\mathcal K}` be the conditioned law on `\mathcal K_{\Lambda_L,\beta}` (Definition **Core-6.1.1**).

**Definition Core-7.0.2 (goal).**  
This file proves the implication
\[
\text{(conditional HS/hinge covariance bound)}\ +\ \text{(inverse kernel exponential decay)}
\Longrightarrow
\text{(conditional exponential clustering on }\mathcal K_{\Lambda_L,\beta}\text{)}.
\]

**Definition Core-7.0.3 (exported statements).**  
The file exports:

1. an explicit exponential decay bound for the inverse-kernel blocks of the deterministic hinge operator `M_{\Lambda_L}^{\mathrm{hinge}}` (Proposition **Core-7.1.3**);
2. a conditional exponential clustering bound for smooth cylinder observables under `\mu_{\Lambda_L,\beta}^{\mathcal K}` (Proposition **Core-7.2.2** and Corollary **Core-7.2.3**).

**Definition Core-7.0.4 (constants).**  
This file introduces no new *universal* constants.
All quantitative parameters are those already fixed in Appendix A (e.g. `m_H^2`, `\alpha_W`, `\nu_P`) together with the Combes–Thomas rate functional `\eta_{\mathrm{CT}}(\cdot)` (Definition **A.10.2**).

---

## Core-7.1 Exponential decay of the hinge Green kernel

### Definition Core-7.1.1 (hinge operator; recall)
Let `M_{\Lambda_L}^{\mathrm{hinge}}` be the deterministic hinge operator from Definition **Core-5.2.3**:
\[
M_{\Lambda_L}^{\mathrm{hinge}}
:= m_H^2\,\mathrm{Id} + \tfrac12\,\alpha_W\,d_1^*d_1
\qquad\text{acting on }\mathcal C^1(\Lambda_L;\mathfrak g)\cong \ell^2(E(\Lambda_L);\mathfrak g).
\]
Distance on the link index set `E(\Lambda_L)` is measured by the link graph distance `\mathrm{dist}_E` (Definition **A.2.9**).

### Lemma Core-7.1.2 (Combes–Thomas parameters for `M_{\Lambda_L}^{\mathrm{hinge}}`)
Let `a_0(\cdot),R(\cdot),B_0(\cdot)` be the Combes–Thomas parameters from Definition **A.10.1**, defined on self-adjoint operators on `\ell^2(E(\Lambda_L);\mathfrak g)`.
Then:

1. **Positivity:**
   \[
   a_0\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)=m_H^2.
   \]
2. **Finite range in `\mathrm{dist}_E`:**
   \[
   R\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)=1.
   \]
3. **Off-diagonal row-sum constant:** with `\mathsf M_1:=d_1^*d_1` and `C_0(\mathsf M_1)` as in Definition **A.9.3**,
   \[
   B_0\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)
   = \tfrac12\,\alpha_W\,C_0(\mathsf M_1)
   \le \tfrac12\,\alpha_W\,(3\nu_P).
   \]

**Proof.**

(1) By Lemma **B.4.1**, `\mathsf M_1=d_1^*d_1\succeq 0` as a quadratic form on `\mathcal C^1(\Lambda_L;\mathfrak g)`. Hence
\[
M_{\Lambda_L}^{\mathrm{hinge}}=m_H^2\,\mathrm{Id}+\tfrac12\alpha_W\,\mathsf M_1\succeq m_H^2\,\mathrm{Id}.
\]
By maximality in Definition **A.10.1**, `a_0(M_{\Lambda_L}^{\mathrm{hinge}})=m_H^2`.

(2) The mass term is diagonal in the link index. The off-diagonal coupling is that of `\mathsf M_1` multiplied by `\tfrac12\alpha_W`. Proposition **B.4.5** states that `\mathsf M_1` has interaction range one in the link graph `\mathrm{dist}_E`, i.e. `(\mathsf M_1)_{bb'}=0` when `\mathrm{dist}_E(b,b')>1` and `b\neq b'`. Therefore the same holds for `M_{\Lambda_L}^{\mathrm{hinge}}`, and the smallest such range is `R(M_{\Lambda_L}^{\mathrm{hinge}})=1`.

(3) For `b\neq b'`, one has `(M_{\Lambda_L}^{\mathrm{hinge}})_{bb'}=\tfrac12\alpha_W\,(\mathsf M_1)_{bb'}`.
Thus
\[
\sum_{b'\neq b}\big\|\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)_{bb'}\big\|_{\mathrm{op}}
=\tfrac12\alpha_W\sum_{b'\neq b}\big\|(\mathsf M_1)_{bb'}\big\|_{\mathrm{op}}.
\]
Taking the supremum over `b` gives
\[
B_0\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)=\tfrac12\alpha_W\,C_0(\mathsf M_1).
\]
The bound `C_0(\mathsf M_1)\le 3\nu_P` is Lemma **B.4.6**.
\(\square\)

### Proposition Core-7.1.3 (exponential inverse-kernel decay for `\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)^{-1}`)
For all links `b,b'\in E(\Lambda_L)`, the inverse kernel blocks of `M_{\Lambda_L}^{\mathrm{hinge}}` satisfy
\[
\big\|\big((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\big)_{bb'}\big\|_{\mathrm{op}}
\le
\frac{2}{m_H^2}\,\exp\!\Big(-\eta_{\mathrm{CT}}\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)\,\mathrm{dist}_E(b,b')\Big),
\tag{7.1}
\]
where `\eta_{\mathrm{CT}}(\cdot)` is the Combes–Thomas decay rate from Definition **A.10.2**.

Moreover, since `R(M_{\Lambda_L}^{\mathrm{hinge}})=1`, one has the explicit identity
\[
\eta_{\mathrm{CT}}\big(M_{\Lambda_L}^{\mathrm{hinge}}\big)
=
\log\Bigl(1+\frac{m_H^2}{2B_0(M_{\Lambda_L}^{\mathrm{hinge}})}\Bigr)
=
\log\Bigl(1+\frac{m_H^2}{\alpha_W\,C_0(\mathsf M_1)}\Bigr)
\ge
\log\Bigl(1+\frac{m_H^2}{\alpha_W\,(3\nu_P)}\Bigr).
\tag{7.2}
\]

**Proof.**
By Lemma **Core-7.1.2**, the operator `M_{\Lambda_L}^{\mathrm{hinge}}` is self-adjoint and satisfies
`a_0(M_{\Lambda_L}^{\mathrm{hinge}})>0`, `R(M_{\Lambda_L}^{\mathrm{hinge}})<\infty`, and `B_0(M_{\Lambda_L}^{\mathrm{hinge}})<\infty`.
Therefore Proposition **G.3.1** applies (with `V=E(\Lambda_L)` and distance `\mathrm{dist}_E`), giving (7.1).

The explicit formula (7.2) is Definition **A.10.2** together with Lemma **Core-7.1.2** and the bound of Lemma **B.4.6**.
\(\square\)

**Remark Core-7.1.4 (volume-uniformity).**  
The bound (7.1) holds for each finite volume `\Lambda_L` with the decay rate `\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})` computed from Definition **A.10.2**.

For later uniform-in-volume uses, it suffices to retain the explicit lower bound in (7.2): by Lemma **B.4.6**, `C_0(\mathsf M_1)\le 3\nu_P` with `\nu_P` depending only on the dimension. Consequently,
\[
\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})
\ge
\log\Bigl(1+\frac{m_H^2}{\alpha_W\,(3\nu_P)}\Bigr),
\]
and therefore (7.1) implies the weaker but volume-uniform kernel decay estimate
\[
\big\|\big((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\big)_{bb'}\big\|_{\mathrm{op}}
\le
\frac{2}{m_H^2}\,\exp\!\Big(-\log\bigl(1+\frac{m_H^2}{\alpha_W\,(3\nu_P)}\bigr)\,\mathrm{dist}_E(b,b')\Big).
\]
Here `m_H^2` and `\alpha_W` are defined in Appendix A and are independent of `L`.

---

## Core-7.2 Conditional exponential clustering on the good set

### Definition Core-7.2.1 (linkwise gradient envelopes for cylinder observables)
Let `F\in C^\infty(\mathcal M_{\Lambda_L})` and write its right-trivialized gradient as `\nabla^R F` (Definition **Core-6.4.1**, originally Definition **Core-2.2.1**).

For each link `b\in E(\Lambda_L)`, define the uniform envelope
\[
\mathsf L_b(F)
:=
\sup_{U\in \mathcal M_{\Lambda_L}}\big| (\nabla^R F(U))_b\big|_{\mathfrak g}\ \in [0,\infty).
\]
If `F` is a cylinder observable with finite link support `A=\mathrm{supp}_E(F)` (Definition **Core-2.1.4**), then by Corollary **Core-2.2.5** one has `(\nabla^R F(U))_b\equiv 0` for all `b\notin A`, hence `\mathsf L_b(F)=0` for `b\notin A`.

Define the finite quantity
\[
\mathsf L_E(F)
:=
\sum_{b\in E(\Lambda_L)} \mathsf L_b(F)
=
\sum_{b\in \mathrm{supp}_E(F)} \mathsf L_b(F)
\tag{7.3}
\]
for cylinder observables.

### Proposition Core-7.2.2 (conditional exponential clustering; kernel form)
Let `F,G\in C^\infty(\overline{\mathcal K_{\Lambda_L,\beta}})` be smooth cylinder observables with finite link supports
`A:=\mathrm{supp}_E(F)` and `B:=\mathrm{supp}_E(G)`.
Let `\mathrm{dist}_E(A,B)` be the support distance from Definition **Core-2.3.1**.

Assume the hypotheses of Proposition **Core-6.4.3** (conditional HS/hinge covariance bound on `\mathcal K_{\Lambda_L,\beta}`).
Then
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}^{\mathcal K}(F,G)\big|
\le
\frac{2}{m_H^2}\,e^{-\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})\,\mathrm{dist}_E(A,B)}
\Big(\sum_{b\in A}\big(\mathbb E_{\Lambda_L,\beta}^{\mathcal K}[| (\nabla^R F)_b |_{\mathfrak g}^2]\big)^{1/2}\Big)
\Big(\sum_{b'\in B}\big(\mathbb E_{\Lambda_L,\beta}^{\mathcal K}[| (\nabla^R G)_{b'} |_{\mathfrak g}^2]\big)^{1/2}\Big).
\tag{7.4}
\]

**Proof.**
Start from Proposition **Core-6.4.3**, which states
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}^{\mathcal K}(F,G)\big|
\le
\sum_{b\in A}\sum_{b'\in B}
\Big(\mathbb E^{\mathcal K}[| (\nabla^R F)_b |^2]\Big)^{1/2}
\,\Big\|\big((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\big)_{b,b'}\Big\|_{\mathrm{op}}
\,\Big(\mathbb E^{\mathcal K}[| (\nabla^R G)_{b'} |^2]\Big)^{1/2}.
\tag{7.5}
\]
Insert the inverse-kernel bound from Proposition **Core-7.1.3**:
\[
\Big\|\big((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\big)_{b,b'}\Big\|_{\mathrm{op}}
\le \frac{2}{m_H^2}\exp\big(-\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})\,\mathrm{dist}_E(b,b')\big).
\tag{7.6}
\]
By definition of `\mathrm{dist}_E(A,B)` (Definition **Core-2.3.1**), every pair `(b,b')\in A\times B` satisfies
`\mathrm{dist}_E(b,b')\ge \mathrm{dist}_E(A,B)`.
Hence for all such pairs,
\[
\exp\big(-\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})\,\mathrm{dist}_E(b,b')\big)
\le
\exp\big(-\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})\,\mathrm{dist}_E(A,B)\big).
\tag{7.7}
\]
Factor the right-hand side of (7.7) out of the double sum in (7.5), and then separate the product as
\(
\sum_{b\in A}\sum_{b'\in B} a_b c_{b'} = (\sum_{b\in A} a_b)(\sum_{b'\in B} c_{b'})
\)
with
\(a_b=(\mathbb E^{\mathcal K}[| (\nabla^R F)_b |^2])^{1/2}\) and
\(c_{b'}=(\mathbb E^{\mathcal K}[| (\nabla^R G)_{b'} |^2])^{1/2}\).
This yields (7.4). \(\square\)

### Corollary Core-7.2.3 (deterministic conditional clustering bound)
In the setting of Proposition **Core-7.2.2**,
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}^{\mathcal K}(F,G)\big|
\le
\frac{2}{m_H^2}\,e^{-\eta_{\mathrm{CT}}(M_{\Lambda_L}^{\mathrm{hinge}})\,\mathrm{dist}_E(A,B)}\,\mathsf L_E(F)\,\mathsf L_E(G),
\tag{7.8}
\]
where `\mathsf L_E(\cdot)` is defined in (7.3).

**Proof.**
For each `b\in A`,
\[
\big(\mathbb E^{\mathcal K}[| (\nabla^R F)_b |^2]\big)^{1/2}
\le
\sup_{U\in \mathcal K_{\Lambda_L,\beta}} |(\nabla^R F(U))_b|
\le
\sup_{U\in \mathcal M_{\Lambda_L}} |(\nabla^R F(U))_b|
=\mathsf L_b(F).
\]
Summing over `b\in A` yields
\(
\sum_{b\in A}(\mathbb E^{\mathcal K}[| (\nabla^R F)_b |^2])^{1/2}\le \sum_{b\in A}\mathsf L_b(F)=\mathsf L_E(F)
\)
(using `\mathsf L_b(F)=0` outside `A`).
The same holds for `G`. Substituting these bounds into (7.4) gives (7.8). \(\square\)

---

## Core-7.3 Dependency and conditionality ledger

**Definition Core-7.3.1 (proved vs. conditional content in this file).**  
- Propositions **Core-7.1.3** and **Core-7.2.2** are proved given the upstream statements cited in their proofs.
- Proposition **Core-7.2.2** is conditional on the hypotheses of Proposition **Core-6.4.3**, which (by Core 6) are conditional on:
  - **External Input Core-6.EI.1** (reflecting diffusion / conditioned HS identity on `\mathcal K_{\Lambda_L,\beta}`), and
  - the hinge input Proposition **Core-5.2.4**, itself conditional on **External Input Core-5.EI.1**.

No other assumptions are introduced in this file.
