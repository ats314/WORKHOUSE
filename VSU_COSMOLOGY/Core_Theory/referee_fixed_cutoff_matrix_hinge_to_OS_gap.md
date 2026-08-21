# Fixed-cutoff analytic spine: matrix-hinge coercivity \(\Rightarrow\) clustering \(\Rightarrow\) OS/transfer-matrix gap

## What this document establishes

It isolates the *load-bearing* analytic chain in the HAAR project that turns a **matrix lower bound on the Witten Laplacian on 1-forms** (“matrix hinge”) into:

1. exponential decay of covariances of local gauge-invariant observables (Euclidean clustering), and  
2. a corresponding Osterwalder–Schrader / transfer-matrix spectral gap at **fixed lattice cutoff**.

Everything is stated so a referee can check which steps are standard, which are proved in-project, and which are still assumptions.

---

## 0. Setup and notation

- Finite lattice \(\Lambda\) with vertex set \(V\), oriented edge (bond) set \(B\), plaquette set \(P\).
- Gauge group \(G=SU(N)\). Configuration manifold
  \[
  \mathcal C_\Lambda := G^{|B|},
  \]
  with product bi-invariant Riemannian metric and volume \(d\mathrm{vol}\).
- Gauge group \(\mathcal G_\Lambda := G^{|V|}\) acts by \((g\cdot U)_{xy}=g_x U_{xy} g_y^{-1}\).
- “Physical” (gauge-invariant) observables are functions \(F:\mathcal C_\Lambda\to\mathbb R\) constant on orbits.

Let \(S:\mathcal C_\Lambda\to\mathbb R\) be an effective action (typically Wilson plus a Haar/Jacobian term on each link). Define the Gibbs measure
\[
d\mu(U) := Z^{-1} e^{-S(U)}\,d\mathrm{vol}(U).
\]

**Langevin generator.** On functions,
\[
L f := \Delta f - \langle \nabla S,\nabla f\rangle.
\]
On 1-forms \(\omega\) (identified with vector fields via the metric), let \(L^{(1)}\) denote the corresponding Witten Laplacian (the Helffer–Sjöstrand operator):
\[
L^{(1)} := \nabla^*\nabla + (\mathrm{Ric} + \nabla^2 S),
\]
acting on 1-forms (precise conventions vary by a factor 2; only operator inequalities matter below).

---

## 1. Standard bridge: Helffer–Sjöstrand covariance representation

For sufficiently regular \(F,G\),
\[
\mathrm{Cov}_\mu(F,G)
:= \int (F-\mu F)(G-\mu G)\,d\mu
= \left\langle dF,\ (L^{(1)})^{-1}\, dG\right\rangle_{L^2(\mu)}.
\]

**Status.** Standard (Helffer–Sjöstrand). In-project this is treated as an input and used repeatedly.

**Consequence.** Any *operator lower bound* \(L^{(1)}\succeq \mathcal A\) implies
\[
|\mathrm{Cov}_\mu(F,G)| \le \left\langle dF,\ \mathcal A^{-1}\, dF\right\rangle^{1/2}
\left\langle dG,\ \mathcal A^{-1}\, dG\right\rangle^{1/2}.
\]

---

## 2. Discrete Hodge structure on links (the “Maxwell piece”)

Let \(d_0\) be the (linearized) lattice coboundary \(0\to 1\) and \(d_1\) the coboundary \(1\to 2\) (curl):
\[
d_0:\ \text{site fields}\to \text{edge fields},\qquad
d_1:\ \text{edge fields}\to \text{plaquette fields},\qquad d_1 d_0 = 0.
\]

Define the **Maxwell operator on edges**
\[
\mathcal M := d_1^* d_1.
\]

- \(\ker \mathcal M\) contains \(\mathrm{im}(d_0)\) (pure gauge gradients).
- On the orthogonal complement (co-closed / “horizontal” subspace), \(\mathcal M\) is elliptic and has a spectral gap depending on the lattice size unless a mass is added.

A **massive Maxwell operator** is
\[
\mathcal A_M := m_H^2 I + \alpha \mathcal M,
\]
with \(m_H^2>0\) (“Haar mass / curvature mass”) and \(\alpha>0\) (stiffness coefficient).

**Status.** Linear algebra / discrete Hodge theory: standard. The project uses this to keep track of gauge directions and make \(\mathcal A_M\) invertible on physical/horizontal modes.

---

## 3. The project’s analytic core inequality: the matrix hinge

### 3.1 Statement (as used)

There exist constants \(m_H^2>0\), \(\alpha>0\) such that, on the *horizontal* (physical) 1-form sector,
\[
L^{(1)}\ \succeq\ \mathcal A_M
:= m_H^2 I + \alpha\, d_1^* d_1.
\tag{MH}
\]

Interpretation: the Bakry–Émery tensor \(\mathrm{Ric}+\nabla^2 S\) does not just dominate a constant mass;
it dominates a **mass plus a discrete elliptic operator** tied to plaquettes/curls.

### 3.2 What is actually proved vs assumed in-project

- The decomposition of the Wilson Hessian into “Laplacian minus bounded potential” form is treated as structural; the *boundedness* part is proved (uniform Hessian bound per link/plaquette).
- The explicit emergence of \(d_1^*d_1\) as the correct elliptic operator is justified by the discrete complex and horizontality computations.
- The inequality (MH) in full generality is **not shown as a complete proof** for the interacting measure; it is used as a target coercivity statement and then localized (SAFE core vs complement).

So: (MH) should be read as a *conditional inequality* which, if established on a set of configurations, yields quantitative clustering on that set.

---

## 4. Standard bridge: Combes–Thomas resolvent decay

Let \(\mathcal A_M = m_H^2 I + \alpha d_1^*d_1\) act on edge fields (with adjoint indices suppressed).
Then its Green’s function \(G=\mathcal A_M^{-1}\) has exponential off-diagonal decay:
\[
\|G_{b,b'}\|\ \le\ C \exp\bigl(-\mathfrak m\,\mathrm{dist}(b,b')\bigr),
\]
with \(\mathfrak m\) comparable to \(m_H/\sqrt{\alpha}\) (precise formula depends on lattice geometry and norm choice).

**Status.** Standard (Combes–Thomas for massive discrete elliptic operators).

---

## 5. Consequence: Euclidean clustering of local observables

If \(F,G\) are local gauge-invariant observables supported near disjoint regions,
and if the matrix hinge (MH) holds on the relevant sector, then the HS formula plus Combes–Thomas implies
\[
|\mathrm{Cov}_\mu(F,G)|
\ \lesssim\ \|\nabla F\|_{L^2(\mu)}\,\|\nabla G\|_{L^2(\mu)}\,
e^{-\mathfrak m\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}.
\]

**Status.** Standard once (MH) is available.

---

## 6. Fixed-cutoff OS/transfer-matrix gap

Assume:
1. reflection positivity of the Euclidean lattice measure, and
2. exponential clustering of suitable local observables at rate \(\mathfrak m>0\).

Then, by standard Osterwalder–Schrader reconstruction / transfer-matrix arguments, the Hamiltonian (or transfer matrix) has a spectral gap bounded below in terms of \(\mathfrak m\).

**Status.** Standard, but requires the correct reflection structure and careful choice of observable class.

**Project status.** Treated as a downstream step contingent on establishing global clustering.

---

## 7. Where the project adds structure: localization (core + complement) to globalize (MH)

The project does **not** claim a global proof of (MH) across all of \(\mathcal C_\Lambda\).
Instead it uses a three-region strategy:

- \(\mathcal K\) (“core” / SAFE region): prove/verify strong convexity and hence (MH) with explicit \(m_H^2,\alpha\).
- \(A=\mathcal C_\Lambda\setminus\mathcal K\) (complement): use a Lyapunov/drift inequality to control exit times / Dirichlet eigenvalues.
- \(\Sigma\) (boundary strip): control cutoffs and gradient of the partition of unity used to glue the inequalities.

This is encoded in the fixed-cutoff module as hypotheses of the form:
- **(core Poincaré)** on \(\mathcal K\),
- **(Dirichlet / exit-time control)** on \(A\),
- **(gluing lemma)** combining them into a global Poincaré inequality.

Once a global Poincaré (or stronger) inequality is obtained, HS + hinge yields global clustering.

**Status.**
- Gluing and Lyapunov-function techniques: standard in principle.
- The particular choices of \(\mathcal K\), the drift function, and the link between drift and a *uniform* Dirichlet bound: not proved in the project; supported by numerical exploration and local geometric lemmas.

---

## 8. Referee assessment: what survives as solid, and what remains missing

### Solid (as mathematics)
- HS representation \(\Rightarrow\) reduce covariance control to coercivity of \(L^{(1)}\).
- Combes–Thomas \(\Rightarrow\) resolvent decay for \(m_H^2I+\alpha d_1^*d_1\).
- Discrete Hodge decomposition \(\Rightarrow\) why horizontality matters (avoid gauge kernel).

### Conditional / incomplete
- A global, uniform (in volume) matrix hinge bound (MH) for the interacting Yang–Mills measure.
- The complement control: a proof that the chosen “bad set” \(A\) has a Dirichlet eigenvalue bounded below uniformly in volume.

### Numerically suggested (not proof)
- SAFE-region convexity constants for \(SU(3)\) and drift inequalities for \(SU(2)\) outside the core.

---

## Internal sources in this project

Primary modules feeding this spine:
- `doc01_matrix_hinge_mass_gap.md`
- `Extract_09_Gauge_Horizontality_and_Massive_Maxwell.md`
- `CURATED_03_HS_to_Clustering_OSGap.md`
- `3_fixed_cutoff_mass_gap_su2.md`
