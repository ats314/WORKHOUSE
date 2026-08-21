# Exact Star-Level Wilson Hessian and the Curvature-Defect Functional \(\Phi(a)\)

*This note packages the star-level Wilson Hessian mechanism (the “rank-one defect” structure) and the resulting geometric invariant \(\Phi(a)\), specialized for \(G=\mathrm{SU}(3)\) but stated in a group-agnostic way.*

---

## 1. The star configuration space at one link

Fix a link \(\ell\) in a \(4\)D lattice.

Let \(\mathrm{Star}(\ell)\) denote the six plaquettes incident to \(\ell\).  
Gauge-fix so that \(U_\ell=\mathbf 1\). Let \(\mathcal C_\ell\) denote the resulting finite-dimensional compact manifold of remaining star link variables.

Define the star-restricted Wilson action
\[
S_W^{(\ell)}(U):=\sum_{p\in \mathrm{Star}(\ell)}\Phi_\beta(U_p(U)),
\qquad
\Phi_\beta(g)=\beta\Bigl(1-\tfrac13\Re\operatorname{Tr}(g)\Bigr).
\]

Let \(\Pi_{\mathrm{phys}}^{(\ell)}\) be the orthogonal projection onto the physical subspace after removing the infinitesimal gauge directions that remain after fixing \(U_\ell=\mathbf 1\).

The **exact physical star Hessian** is
\[
\mathsf H_W^{(\ell)}(U)
:=
\Pi_{\mathrm{phys}}^{(\ell)}\;\nabla^2 S_W^{(\ell)}(U)\;\Pi_{\mathrm{phys}}^{(\ell)}.
\]

---

## 2. Vacuum reference stiffness \(\kappa_\*\)

At the vacuum configuration \(U^{(0)}\) (all links \(\mathbf 1\)), the project establishes an exact vacuum Hessian identity of the form
\[
\nabla^2 S_W(U^{(0)})=\alpha\,d_1^\*d_1
\quad(\alpha\asymp \beta),
\]
in right-trivialized coordinates.

Restricting to one star and projecting to physical directions yields a finite-dimensional positive operator. Define
\[
\kappa_\* := \lambda_{\min}\!\Big(\mathsf H_W^{(\ell)}(U^{(0)})\Big) \;>\;0.
\]

---

## 3. Star-level rank-one defect mechanism (conceptual form)

The user’s Appendix X.Z draft in this chat proposes (and motivates) the following *exact* conceptual structure:

- Each incident plaquette contributes a “stiff” isotropic part comparable to \(\kappa_\*\mathrm{Id}\),
- plus a **rank-one negative defect** along a transported “flux direction”
  \[
  X_p(U)\in \mathfrak{su}(3)\cong \mathbb R^8,
  \]
- plus a remainder that is quadratically small in the plaquette logarithms near the vacuum.

In schematic form,
\[
\mathsf H_W^{(\ell)}(U)
=
\kappa_\*\,\mathrm{Id}
\;-\;
\sum_{p\in\mathrm{Star}(\ell)}
c_p(U)\,
\Pi_{\mathrm{phys}}^{(\ell)}\bigl(X_p(U)\otimes X_p(U)\bigr)\Pi_{\mathrm{phys}}^{(\ell)}
\;+\;\mathcal R^{(\ell)}(U),
\]
with \(c_p(U)>0\) and \(\|\mathcal R^{(\ell)}(U)\|\lesssim \sum_p \|A_p(U)\|^2\) near the vacuum.

**The key geometric point:** stiffness can be destroyed only if these defect directions \(X_p(U)\) span “enough” of \(\mathfrak{su}(3)\) inside the physical subspace. Conversely, if \(\lambda_{\min}(\mathsf H_W^{(\ell)}(U))\) is close to \(\kappa_\*\), then the rank-one defects must be jointly ineffective — which forces a strong alignment/commutation structure (a “Cartan-type exceptional set”).

---

## 4. Finite-dimensional Cartan rigidity lemma (standalone proposition)

Let \(\mathcal C_\ell\) be compact and \(U\mapsto \mathsf H_W^{(\ell)}(U)\) continuous in operator norm.

Let \(\mathcal E_\ell\subset \mathcal C_\ell\) be the **exceptional set** of star configurations where the transported defect vectors fail to generate enough noncommuting directions in \(\mathfrak{su}(3)\) (e.g., configurations where all \(X_p(U)\) lie in a common Cartan subalgebra and transports preserve it).

> **Proposition (Exact star-level Cartan rigidity).**  
> Assume:
> 1. (Compactness) \(\mathcal C_\ell\) is compact.  
> 2. (Continuity) \(U\mapsto \mathsf H_W^{(\ell)}(U)\) is continuous.  
> 3. (Strict stiffness loss away from \(\mathcal E_\ell\)) For all \(U\notin \mathcal E_\ell\),
>    \[
>    \lambda_{\min}\!\big(\mathsf H_W^{(\ell)}(U)\big)\ <\ \kappa_\*.
>    \]
> Then for every \(\varepsilon>0\) there exists \(\delta>0\) such that
> \[
> \lambda_{\min}\!\big(\mathsf H_W^{(\ell)}(U)\big)\ \ge\ \kappa_\*-\varepsilon
> \quad\Longrightarrow\quad
> \mathrm{dist}(U,\mathcal E_\ell)\le \delta.
> \]

*Proof (compactness + continuity).*  
Fix \(\varepsilon>0\). Consider the closed set
\[
A_\varepsilon:=\left\{U\in\mathcal C_\ell:\ \mathrm{dist}(U,\mathcal E_\ell)\ge \tfrac1n\right\}
\]
for any \(n\in\mathbb N\). Since \(\mathcal C_\ell\) is compact and \(\mathcal E_\ell\) is closed, \(A_\varepsilon\) is compact.

Define the continuous function
\[
f(U):=\kappa_\*-\lambda_{\min}(\mathsf H_W^{(\ell)}(U))\ \ge 0.
\]
By assumption (3), \(f(U)>0\) for all \(U\in A:=\mathcal C_\ell\setminus \mathcal E_\ell\). Hence for each \(n\), the minimum
\[
m_n:=\min_{U\in A_n} f(U)
\]
exists and satisfies \(m_n>0\).

Choose \(n\) large enough so that \(m_n>\varepsilon\), and set \(\delta:=1/n\). Then if \(\mathrm{dist}(U,\mathcal E_\ell)\ge\delta\), we have \(U\in A_n\) hence \(f(U)\ge m_n>\varepsilon\), i.e.
\[
\lambda_{\min}(\mathsf H_W^{(\ell)}(U))\ \le\ \kappa_\*-\varepsilon.
\]
Contraposition gives the claim. \(\square\)

**What this buys you:** you never need to solve for the minimizer explicitly. You only need:
- an explicit characterization of \(\mathcal E_\ell\),
- and a proof that outside \(\mathcal E_\ell\) stiffness loss is strict.

---

## 5. The curvature-defect functional \(\Phi(a)\)

Given a lattice spacing \(a\), define the star curvature defect observable at a link \(\ell\):
\[
\Delta_\ell(U) := \bigl(\kappa_\*-\lambda_{\min}(\mathsf H_W^{(\ell)}(U))\bigr)_+.
\]

Define the average curvature defect
\[
\Phi(a) := \mathbb E_{\mu_{a}}\Big[\Delta_\ell(U)\Big],
\]
where \(\mu_a\) is the Wilson Gibbs measure at spacing \(a\), and the expectation is translation-invariant so \(\Phi(a)\) does not depend on \(\ell\).

Heuristic but testable implication in the project’s framework:
- \(\Phi(a)\) is a scale-stable “order parameter” for nonabelian roughness,
- and \(\Phi(a)\) controls (up to order-one constants) the Euclidean correlation length at fixed cutoff.

---

## 6. “Geometric characterization of the \(\mathrm{SU}(3)\) Yang–Mills vacuum” (what to say)

If the mechanism is correct, lattice practitioners should be able to verify a statement of the form:

> In the \(\mathrm{SU}(3)\) Wilson ensemble at physically relevant \(\beta\), typical link stars exhibit an order-one curvature defect \(\Delta_\ell\) and an order-one Cartan misalignment; configurations near the Cartan-aligned exceptional set \(\mathcal E_\ell\) are rare. The continuum limit (if it exists) inherits a nonzero limiting defect density \(\liminf_{a\downarrow 0}\Phi(a)>0\).

This is not “predicting the glueball mass directly.” It is *characterizing the vacuum* by a measurable geometric statistic that the analytic proof naturally consumes.

---

## 7. Next steps that would make this completely referee-proof

1. **Write \(\mathcal E_\ell\) explicitly for SU(3).**  
   E.g. “all six transported plaquette logs lie in a common Cartan and the transport holonomies normalize that Cartan.”

2. **Prove strict stiffness loss away from \(\mathcal E_\ell\).**  
   This is a finite-dimensional linear-algebra statement about rank-one (or low-rank) defects spanning \(\mathfrak{su}(3)\) in the physical subspace.

3. **Show the remainder \(\mathcal R^{(\ell)}(U)\) cannot restore stiffness** on the complement, at least on the typical region of the star ensemble.

---

## Sources inside this project

- Star geometry and bounded overlap constants: `### 3.1 Product Lie-group manifold.txt`  
- Vacuum Hessian identity and stiffness constants: `## 5.1 Vacuum configuration and linearization.txt`  
- The “Cartan alignment is the only cancellation mechanism” route isolate: `02_Assumption_A_and_LocalCancellation_SU2.docx`, `PROJECT_GAP_MAP.md`

(Parts of the star-level decomposition are currently written in the user’s Appendix X.Z draft in this chat.)
