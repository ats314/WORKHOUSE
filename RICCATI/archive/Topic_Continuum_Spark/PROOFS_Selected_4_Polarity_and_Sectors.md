# Selected Proof 4: Cleaning the State Space — Polarity of Reducibles and Charge-Conjugation Sector Decomposition

**Source backbone:**  
- `Lattice_Polarity_Proof_Complete.md` (reducibles are polar / negligible)  
- `Charge_Conjugation_Sector_Decomposition_Proof.md` (Hilbert-space splitting \( \mathcal{H}=\mathcal{H}^+\oplus\mathcal{H}^-\))

This document extracts two structural results that are not “the mass gap” per se, but are *foundational* for making the mass gap problem well-posed and decomposable.

---

## Part I. Polarity of reducible configurations (lattice version)

### 1. Configuration space and reducibles

On a finite lattice \(\Lambda\), the configuration space is
\[
\mathcal{C} = \prod_{b\in B(\Lambda)} SU(N),
\]
and the gauge group is
\[
\mathcal{G} = \prod_{x\in\Lambda} SU(N),
\]
acting by \((U^g)_b = g_{x(b)}^{-1} U_b g_{y(b)}\).

A configuration \(U\in\mathcal{C}\) is **reducible** if its stabilizer
\[
\mathrm{Stab}(U)=\{g\in\mathcal{G}:U^g=U\}
\]
is strictly larger than the center (equivalently: the gauge orbit has lower-than-generic dimension).

Let \(\Sigma\subset\mathcal{C}\) be the set of reducibles.

---

### 2. Algebraic structure: \(\Sigma\) has positive codimension

The project proves that \(\Sigma\) is an algebraic subset of \(\mathcal{C}\) of positive codimension. Intuitively, reducibility forces all link variables to preserve a common nontrivial decomposition of \(\mathbb{C}^N\), which is an algebraic constraint.

A representative codimension estimate is:

\[
\boxed{
\mathrm{codim}(\Sigma)\ge 1
\quad\text{for }N\ge 2 \text{ and }|\Lambda|\ge 2,
}
\]
and for “generic” lattices and \(N\ge 3\), codimension is typically much larger (on the order of \(N^2-1\)).

---

### 3. Measure-theoretic consequence: reducibles are negligible

Let \(d\mu(U)=Z^{-1}e^{-S_W(U)}\,d\mu_{\mathrm{Haar}}(U)\) be the lattice Yang–Mills measure (or any gauge-invariant Gibbs measure with a smooth density relative to Haar measure).

Since \(\mathcal{C}\) is a compact real-analytic manifold and \(\Sigma\) is a strict algebraic subset of positive codimension, one has:
\[
\mu(\Sigma)=0.
\]

The project goes further: it argues \(\Sigma\) is **polar** (zero capacity) for the relevant Dirichlet form, which is stronger than measure zero and is exactly what one wants for analysis of diffusion operators and maximum principles.

---

### 4. Why polarity matters (not just “measure zero”)

In infinite-dimensional gauge theory, reducibles create analytic singularities: the quotient is stratified and not a smooth manifold globally. The lattice polarity statement is a rigorous finite-dimensional proxy for the claim:

> **“Almost surely, the theory lives on the regular stratum.”**

This justifies (at finite cutoff) doing Riemannian geometry on \(\mathcal{M}_{\mathrm{reg}}=\mathcal{C}_{\mathrm{reg}}/\mathcal{G}\) without constantly tripping over singular orbits.

---

## Part II. Charge-conjugation sector decomposition (lattice version)

### 5. Charge conjugation on configurations and measure invariance

Define charge conjugation on configurations by
\[
(\mathcal{C}U)_b := U_b^*.
\]
The Wilson action is invariant:
\[
S_W(\mathcal{C}U)=S_W(U),
\]
hence the lattice measure is \(\mathcal{C}\)-invariant.

---

### 6. The induced operator on the physical Hilbert space

Let the physical Hilbert space be
\[
\mathcal{H}=L^2(\mathcal{C}/\mathcal{G},\mu).
\]
Define \((\mathcal{C}f)(U)=f(\mathcal{C}U)\). Then:

- \(\mathcal{C}\) is a unitary involution: \(\mathcal{C}^\dagger=\mathcal{C}\), \(\mathcal{C}^2=I\).
- Therefore \(\mathrm{Spec}(\mathcal{C})\subset\{+1,-1\}\) and \(\mathcal{H}\) splits orthogonally:
\[
\boxed{
\mathcal{H}=\mathcal{H}^+\oplus\mathcal{H}^-,
\qquad
\mathcal{H}^\pm=\{f:\mathcal{C}f=\pm f\}.
}
\]

A crucial representation-theoretic refinement is:

- For \(SU(2)\), all irreps are (pseudo-)real, which forces \(\mathcal{H}^-=\{0\}\).
- For \(SU(N>2)\), the fundamental representation is complex and \(\mathcal{H}^-\neq\{0\}\).

---

### 7. Dynamical consequence: the Hamiltonian preserves sectors

Let \(T=e^{-aH}\) be the transfer matrix and \(H\) the Hamiltonian. Since the action is charge-conjugation invariant, one has
\[
[\mathcal{C},T]=0,
\qquad\Rightarrow\qquad
[\mathcal{C},H]=0.
\]
Thus
\[
H\mathcal{H}^\pm \subset \mathcal{H}^\pm.
\]

Define sector gaps (with ground state in \(\mathcal{H}^+\) by reflection positivity):
\[
\Delta^\pm := \inf\{E-E_0: E\in\mathrm{Spec}(H|_{\mathcal{H}^\pm}),\ E>E_0\},
\qquad
\Delta=\min(\Delta^+,\Delta^-).
\]

So the mass gap problem naturally **factorizes into two independent spectral problems** in the \(C\)-even and \(C\)-odd sectors.

---

## 8. Synthesis: two clean reductions

These two results combine into a structural “cleanup” lemma for the broader program:

1. **Regularity almost surely:** reducible orbits are negligible (polar / measure zero), so one can work on \(\mathcal{M}_{\mathrm{reg}}\) without losing probability mass.

2. **Symmetry decomposition:** dynamics preserves a \(\pm\) splitting, so the mass gap can be pursued sector-by-sector.

Both reductions are general-purpose tools for turning an infinite-dimensional, stratified quotient into something analyzable at finite cutoff.

---

## References within the project

- `Lattice_Polarity_Proof_Complete.md`  
- `Charge_Conjugation_Sector_Decomposition_Proof.md`
