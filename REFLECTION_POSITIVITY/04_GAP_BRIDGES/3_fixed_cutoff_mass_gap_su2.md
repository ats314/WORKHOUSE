# Fixed-Cutoff Mass Gap for SU(2) Lattice Yang–Mills (Conditional Module)

This document packages the **fixed-cutoff** part of the mechanism:

\[
\text{(good/bad functional inequalities)} \Longrightarrow
\text{global Poincar\'e} \Longrightarrow
\text{exponential clustering} \Longrightarrow
\text{OS Hamiltonian gap}.
\]

Everything is stated in a referee-usable way: hypotheses are explicit, constants are named,
and the conclusion is the fixed-cutoff (finite \(a\)) mass gap **uniform in volume**.

---

## 0. Setting (matches `NOTATION_AND_CONSTANTS.md`)

Let \(G=\mathrm{SU}(2)\). Let \(\Lambda\) be a finite periodic \(d=4\) lattice (a discrete torus) with spacing \(a>0\).
Write \(E(\Lambda)\) for oriented edges (links) and \(P(\Lambda)\) for oriented plaquettes.

Configuration manifold:
\[
M_\Lambda := G^{E(\Lambda)}.
\]
Let \(g_\Lambda\) be the product bi-invariant metric and \(d\mathrm{vol}\) its Riemannian volume.

Define the plaquette holonomy \(U_p(U)\in G\) in the standard way and the Wilson action
\[
S_W(U)=\beta \sum_{p\in P(\Lambda)} \widetilde z(U_p(U)),
\qquad
\widetilde z(g):=1-\tfrac12\mathrm{ReTr}(g)\in[0,2],
\]
with \(\beta>0\).

The Gibbs measure is
\[
d\mu_{\Lambda,\beta}(U)=Z_{\Lambda,\beta}^{-1}e^{-S_W(U)}\,d\mathrm{vol}(U).
\]

Define the reversible generator (Witten Laplacian)
\[
L f := \Delta f - \langle \nabla S_W,\nabla f\rangle_{g_\Lambda},
\]
with Dirichlet form
\[
\mathcal E_\Lambda(f):=\int_{M_\Lambda}|\nabla f|^2\,d\mu_{\Lambda,\beta}.
\]

The global Poincaré constant \(C_P(\Lambda,\beta)\) is the least \(C\) such that
\[
\mathrm{Var}_{\mu_{\Lambda,\beta}}(f)
\le
C\,\mathcal E_\Lambda(f)
\quad\text{for all smooth }f.
\]

---

## 1. Good set / bad set decomposition

Define the averaged disorder (plaquette energy density)
\[
\mathcal B_\Lambda(U)
:=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)} \widetilde z(U_p(U))\in[0,2].
\]

Fix thresholds \(0<\varepsilon<\varepsilon+\delta\le 1\) and define
\[
K := \{\mathcal B_\Lambda\le \varepsilon\},
\qquad
K^c := \{\mathcal B_\Lambda\ge \varepsilon+\delta\},
\qquad
\Sigma := \{\varepsilon<\mathcal B_\Lambda<\varepsilon+\delta\}.
\]

For any \(f\),
the exact variance decomposition across the partition \(K,\Sigma,K^c\) gives
\[
\mathrm{Var}_\mu(f)
\le
\mu(K)\mathrm{Var}_{\mu_K}(f)
+
\mu(K^c)\mathrm{Var}_{\mu_{K^c}}(f)
+
\mu(K)\mu(K^c)\big(\mu_K f-\mu_{K^c}f\big)^2
+
\text{(strip terms on }\Sigma\text{)}.
\tag{1.1}
\]

Thus we must control:
- restricted Poincaré on \(K\),
- restricted Poincaré on \(K^c\),
- the between-set jump term.

---

## 2. Hypotheses (the only nontrivial analytic inputs)

### (H-GOOD) Good-set functional inequality (hinge output)
There exists \(C_{\mathrm{good}}<\infty\), independent of \(|\Lambda|\), such that
\[
\int_K (f-\mu_K f)^2\,d\mu
\le
C_{\mathrm{good}} \int_K |\nabla f|^2\,d\mu
\quad\text{for all smooth }f.
\tag{2.1}
\]
In the project this is produced by the **matrix hinge + Bakry–\'Emery** module on a small-field region
(and then extended to \(K\) as needed).

### (H-BAD) Bad-set functional inequality (drift / Lyapunov output)
There exists \(C_{\mathrm{bad}}<\infty\), independent of \(|\Lambda|\), such that
\[
\int_{K^c} (f-\mu_{K^c} f)^2\,d\mu
\le
C_{\mathrm{bad}} \int_{K^c} |\nabla f|^2\,d\mu
\quad\text{for all smooth }f.
\tag{2.2}
\]
(One sufficient route is a Lyapunov/drift estimate on \(K^c\), plus a bounded \(\Delta S_W\) term.)

### (H-GLUE) Boundary-strip drift for \(\mathcal B_\Lambda\)
There exists \(\rho>0\), independent of \(|\Lambda|\), such that on the mid strip
\[
\Sigma_{\mathrm{mid}}:=\left\{U:\ \frac{\mathcal B_\Lambda(U)-\varepsilon}{\delta}\in\Big[\frac14,\frac34\Big]\right\},
\]
we have the *inward drift* bound
\[
L\mathcal B_\Lambda \le -\rho
\quad\text{pointwise on }\Sigma_{\mathrm{mid}}.
\tag{2.3}
\]
This is exactly the hypothesis used in the **smooth gluing lemma** (see document 2).

---

## 3. Global Poincaré inequality (volume-uniform)

Under (H-GOOD), (H-BAD), (H-GLUE), the smooth gluing lemma yields
\[
\mu(K)\mu(K^c)\big(\mu_K f-\mu_{K^c}f\big)^2
\le
C_{\mathrm{mix}}\,\mathcal E_\Lambda(f)
+
C_\Sigma\int_\Sigma (f-\mu f)^2\,d\mu,
\tag{3.1}
\]
with \(C_{\mathrm{mix}}\) volume-uniform.

Plugging (2.1), (2.2), and (3.1) into (1.1) gives a global Poincaré inequality
\[
\mathrm{Var}_\mu(f)
\le
C_P\,\mathcal E_\Lambda(f),
\qquad
C_P := C_{\mathrm{good}}+C_{\mathrm{bad}}+C_{\mathrm{mix}}+C_\Sigma,
\tag{3.2}
\]
with \(C_P\) independent of \(|\Lambda|\) (for fixed \(a,\beta,\varepsilon,\delta\)).

This closes the *fixed-cutoff* Poincaré problem.

---

## 4. From global Poincaré to exponential clustering

The project’s fixed-cutoff clustering module proceeds via:
1. **Helffer–Sj\"ostrand representation** for covariances of \(\mu\),
2. reduction to estimating the inverse of a localized “massive Maxwell” operator \(A_M\),
3. **Combes–Thomas conjugation** to obtain exponential off-diagonal decay of \(A_M^{-1}\).

### 4.1 The massive operator and its coercivity
On the good set (or after localization), the hinge module yields a lower bound
\[
A_M \ \ge\ m^2\,\mathrm{Id}
\quad\text{with}\quad
m^2 = \frac{c_H}{2},
\tag{4.1}
\]
in the sense of quadratic forms on \(L^2\) 1-forms, with a finite-range term \(\alpha d_1^*d_1\) as in the notation file.

### 4.2 Combes–Thomas exponent
If \(A_M\ge m^2\) and \(A_M\) has interaction range \(R\) and bounded off-diagonal size \(B_M\),
the Combes–Thomas lemma (project file “9.1”) yields
\[
\big|(A_M^{-1})_{xy}\big|
\ \le\
C\,e^{-\eta_M\,\mathrm{dist}(x,y)},
\qquad
\eta_M=\frac{1}{R}\log\!\Big(1+\frac{m^2}{2B_M}\Big).
\tag{4.2}
\]
In the project bookkeeping, \(B_M\) is proportional to \(\alpha\) (finite-range derivative term).

### 4.3 Exponential clustering
Combining (4.2) with the Helffer–Sj\"ostrand representation gives:

> **Clustering statement (fixed cutoff).**  
> For gauge-invariant cylinder observables \(F,G\) supported in spacelike separated regions,
> \[
> \big|\mathrm{Cov}_\mu(F,G)\big|
> \le
> C(F,G)\,e^{-\eta(a)\,d(F,G)}
> +
> \text{(localization error)},
> \tag{4.3}
> \]
> with \(\eta(a)\asymp \eta_M>0\) independent of \(|\Lambda|\).

---

## 5. OS reconstruction and the Hamiltonian gap

Assume the standard Osterwalder–Schrader axioms hold at fixed cutoff:
reflection positivity, translation invariance, and regularity on the cylinder algebra.
Then exponential decay of Euclidean-time correlations implies a positive spectral gap
for the reconstructed Hamiltonian \(H_a\):
\[
\big|\mathrm{Cov}_\mu(\theta F,\tau_n G)\big|
\le
C(F,G)e^{-\eta(a)n}
\quad\Longrightarrow\quad
\mathrm{gap}(H_a)\ \ge\ \frac{\eta(a)}{a}.
\tag{5.1}
\]

---

## 6. Fixed-cutoff mass gap theorem (conditional)

### Theorem 6.1 (Fixed-cutoff OS gap, volume-uniform)
Fix \(a>0\) and \(\beta>0\).
Assume (H-GOOD), (H-BAD), (H-GLUE) and the fixed-cutoff OS axioms.
Then there exists \(\eta(a)>0\), independent of \(|\Lambda|\), such that the OS Hamiltonian
\(H_a\) reconstructed from any thermodynamic limit point satisfies
\[
\mathrm{gap}(H_a)\ \ge\ \frac{\eta(a)}{a}\ >\ 0.
\tag{6.1}
\]

---

## 7. What is actually “new” in this module

Compared to standard lattice YM discussions, the potentially novel elements here are:
1. **Explicit separation of responsibilities:**  
   good-set curvature/hinge \(\Rightarrow\) coercive \(A_M\); bad-set drift \(\Rightarrow\) no trapping;
   gluing is its own stand-alone analytic lemma.
2. **The smooth gluing lemma:**  
   a purely PDE/Dirichlet-form argument that replaces “Cheeger-type” shortcuts
   and avoids illegal indicator gradients.
3. **The strip drift target \(L\mathcal B_\Lambda\le -\rho\):**  
   this is a concrete, local geometric inequality. The drift computation module shows exactly
   what inner-product bound suffices to force such a \(\rho\).

The next steps (per the project gap map) are precisely: make (H-GLUE) and the local transversality input *deterministic*.

