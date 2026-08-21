# Extended Derivations for Constructive Lattice Yang–Mills

**Document:** YM_MassGap_DocD_ConstructiveLatticeYM – Extended  
**Role:** Technical companion to Doc D, expanding the constructive lattice Yang–Mills module with more detailed derivations and LLM-ready tasks.

This document is organized to be readable in isolation, but it assumes familiarity with:

- Finite-volume Euclidean lattice gauge theory.
- Basic representation theory of compact Lie groups (especially SU(N)).
- Osterwalder–Schrader (OS) reconstruction.

---

## 1. Lattice Setup and Haar/Wilson Measure

### 1.1. Lattice and configuration space

Let \(\Lambda\) be a finite hypercubic lattice in \(\mathbb{Z}^4\) with periodic boundary conditions. Its elements are sites \(x\in\Lambda\), oriented bonds \(b=(x,\mu)\) with \(\mu\in\{1,2,3,4\}\), and oriented plaquettes \(p\).

- Gauge group: \(G=SU(N)\).
- Link variables: for each oriented bond \(b\), a group element \(U_b\in G\).
- Configuration space: \(\Omega = G^{\mathcal{B}}\), where \(\mathcal{B}\) is the set of bonds.

### 1.2. Haar measure and Wilson action

The product Haar measure is
\[
d\mu_H(U) = \prod_{b\in\mathcal{B}} dU_b
\]
with each \(dU_b\) the normalized Haar measure on \(G\).

For a plaquette \(p\), the ordered product of links around \(p\) is denoted \(U_p\). The Wilson action is
\[
S_W(U) = \frac{1}{g^2}\sum_{p} \Re\operatorname{Tr}(I - U_p)
= \frac{1}{g^2}\sum_p \big( N - \Re\operatorname{Tr} U_p\big).
\]

The Boltzmann weight is \(e^{-S_W(U)} = e^{-\frac{1}{g^2}\sum_p (N-\Re\operatorname{Tr} U_p)}\). The partition function is
\[
Z_\Lambda = \int_\Omega e^{-S_W(U)}\,d\mu_H(U).
\]

The normalized Gibbs measure is
\[
d\mu_\Lambda(U) = Z_\Lambda^{-1}e^{-S_W(U)}\,d\mu_H(U).
\]

---

## 2. OS Reconstruction and Transfer Matrix (Sketch)

### 2.1. Time-slicing

Pick one lattice direction (say \(\mu=4\)) as Euclidean time. Decompose the lattice into spatial slices \(\Lambda_t\), each corresponding to fixed time coordinate.

Define:

- Spatial link variables \(U_{\mathbf{x},i}(t)\) with \(i=1,2,3\).
- Temporal link variables \(U_{\mathbf{x},4}(t)\) connecting slices \(t\) and \(t+1\).

The Gibbs weight can be factorized as
\[
e^{-S_W(U)} = \prod_t W_t(U_t,U_{t+1}),
\]
where \(U_t\) denotes all spatial links at time \(t\) and \(W_t\) is a “transfer kernel” depending on spatial links at times \(t\) and \(t+1\) and the temporal links between them.

### 2.2. Hilbert space and transfer matrix

Define the Hilbert space
\[
\mathcal{H} = L^2(\mathcal{C}, d\mu_{\text{slice}}),
\]
where:

- \(\mathcal{C}=G^{\mathcal{B}_{\text{space}}}\) is the set of spatial link configurations on a time slice.
- \(\mu_{\text{slice}}\) is the product Haar measure on the spatial links (or a gauge-invariant version if spatial gauge fixing is imposed).

The transfer matrix \(T\) is a positive self-adjoint operator on \(\mathcal{H}\) defined by
\[
(T\psi)(U') = \int_{\mathcal{C}} K(U',U)\,\psi(U)\,d\mu_{\text{slice}}(U),
\]
where \(K\) is derived from the Boltzmann factors involving time-like plaquettes between slices \(t\) and \(t+1\).

The basic OS reconstruction result is:

- The lattice Gibbs measure can be written as matrix elements of \(T^n\) between appropriate boundary vectors.
- The Hamiltonian is defined by \(H = -\frac{1}{a}\log T\) up to additive constants (here \(a\) is the lattice spacing).
- The Hilbert space \(\mathcal{H}\) is the “one-time-slice” state space, and \(\Omega\) (the vacuum) corresponds to the constant function \(1\) (or its gauge-invariant projection).

This establishes a correspondence:
\[
\text{correlation decay in Euclidean time} \quad\leftrightarrow\quad \text{spectral gap of } H.
\]

---

## 3. Charge Conjugation and “Polarity Sectors”

### 3.1. Charge conjugation on the lattice

Define the lattice charge conjugation operator \(\mathcal{C}\) on configurations by
\[
(\mathcal{C}U)_b := U_b^*,
\]
where \(*\) is complex conjugation (Hermitian adjoint) in the fundamental representation.

Properties:

- \(\mathcal{C}\) is an involution: \(\mathcal{C}^2 = \mathrm{id}\).
- Haar measure is invariant: \(d\mu_H(\mathcal{C}U)=d\mu_H(U)\).
- Wilson action is invariant: \(\Re\operatorname{Tr}(I-U_p) = \Re\operatorname{Tr}(I-U_p^*)\).

Therefore, the Gibbs measure \(\mu_\Lambda\) is invariant under \(\mathcal{C}\), and \(\mathcal{C}\) induces a unitary involution on the OS Hilbert space \(\mathcal{H}\).

### 3.2. Decomposition of \(\mathcal{H}\) into \(\mathcal{H}^+\oplus\mathcal{H}^-\)

Define
\[
\mathcal{H}^\pm := \{\psi\in\mathcal{H} : \mathcal{C}\psi = \pm\psi\}.
\]
These are closed subspaces, and
\[
\mathcal{H} = \mathcal{H}^+\oplus\mathcal{H}^-.
\]

- \(\mathcal{H}^+\) contains the vacuum vector (constant function), so it is nontrivial.
- For \(SU(N>2)\), there exist \(\mathcal{C}\)-odd observables, e.g. suitable combinations of Wilson loops in the fundamental representation, so \(\mathcal{H}^-\neq\{0\}\).

**Representation-theoretic argument for nontrivial \(\mathcal{H}^-\):**

Consider a Wilson loop in the fundamental representation:
\[
W(C) = \frac{1}{N}\operatorname{Tr}\,\mathcal{P}\prod_{\ell\in C} U_\ell.
\]
Under \(\mathcal{C}\),
\[
\mathcal{C}W(C) = \frac{1}{N}\operatorname{Tr}\, \big(\mathcal{P}\prod_{\ell\in C}U_\ell\big)^* = \overline{W(C)}.
\]
For generic configurations, \(W(C)\) is not real; thus its imaginary part
\[
W^-(C) := \frac{1}{2i}(W(C) - \overline{W(C)})
\]
is \(\mathcal{C}\)-odd and nontrivial. Its OS-class in \(\mathcal{H}\) lies in \(\mathcal{H}^-\) and is nonzero.

### 3.3. Sector-preserving Hamiltonian

Because \(\mathcal{C}\) leaves the action and Haar measure invariant, it commutes with the transfer matrix \(T\) and Hamiltonian \(H\). Therefore, \(H\) preserves \(\mathcal{H}^\pm\), and its spectrum splits as
\[
\operatorname{spec}(H) = \{0\}\cup[\Delta^+,\infty) \cup [\Delta^-,\infty),
\]
where \(\Delta^\pm\) are the lowest positive eigenvalues on \(\mathcal{H}^\pm\). The physical mass gap at lattice spacing \(a\) is
\[
m_{\text{gap}}(a) = \min(\Delta^+(a),\Delta^-(a)).
\]

These are the “polarity sectors” in the sense used in Doc D. They are unrelated to “polar sets” in the capacity sense of Doc C.

---

## 4. Mass from Haar Measure: Extended Derivation

### 4.1. Exponential coordinates and Jacobian

Locally around the identity of \(G\), write
\[
U = \exp(iag A),
\]
where \(A\in\mathfrak{g}=\mathfrak{su}(N)\), \(g\) is the gauge coupling, and \(a\) is the lattice spacing. In these coordinates, the Haar measure is
\[
d\mu_H(U) = J(A)\,dA,
\]
with Jacobian
\[
J(A) = \det_{\mathfrak{g}}\!\left(\frac{\sinh(\frac{\mathrm{ad}_{iag A}}{2})}{\frac{\mathrm{ad}_{iag A}}{2}}\right).
\]

Define the measure action
\[
S_{\mathrm{measure}}(A) := -\log J(A).
\]

We expand near \(A=0\). Let \(X = \frac{\mathrm{ad}_{iag A}}{2}\). Then
\[
\frac{\sinh X}{X} = 1 + \frac{X^2}{6} + O(X^4).
\]
Thus,
\[
\log\left(\frac{\sinh X}{X}\right)
= \frac{X^2}{6} + O(X^4).
\]
Taking the trace over \(\mathfrak{g}\),
\[
S_{\mathrm{measure}}(A)
= -\operatorname{Tr}\log\left(\frac{\sinh X}{X}\right)
= -\frac{1}{6}\operatorname{Tr}(X^2) + O(\|X\|^4).
\]

Now \(X = \frac{\mathrm{ad}_{iag A}}{2} = \frac{iag}{2}\mathrm{ad}_A\). Therefore
\[
X^2 = -\frac{a^2g^2}{4}\,\mathrm{ad}_A^2,
\]
and
\[
\operatorname{Tr}(X^2)
= -\frac{a^2g^2}{4}\operatorname{Tr}(\mathrm{ad}_A^2)
= -\frac{a^2g^2}{4}C_2(\text{ad})\,\langle A,A\rangle,
\]
where \(C_2(\text{ad})\) is the quadratic Casimir in the adjoint representation and \(\langle\cdot,\cdot\rangle\) is the Killing form (or an equivalent Ad-invariant inner product).

Plugging in,
\[
S_{\mathrm{measure}}(A)
= \frac{1}{6}\cdot\frac{a^2g^2}{4}C_2(\text{ad})\langle A,A\rangle + O(a^4\|A\|^4)
= c_N a^2 g^2 \langle A,A\rangle + O(a^4\|A\|^4),
\]
with
\[
c_N := \frac{C_2(\text{ad})}{24}.
\]

Thus the Haar measure induces an **effective quadratic term** in the action:
\[
S_{\mathrm{measure}}(A) \approx c_N a^2 g^2 \sum_b \operatorname{Tr}(A_b^2),
\]
which looks like a mass term \(m_{\mathrm{Haar}}^2\sim c_N a^2 g^2\) in the Gaussian approximation.

When this contribution is combined with the Wilson plaquette action expanded around the identity, the total quadratic part of the action picks up a strictly positive mass term, which acts as a **geometric mass** even at strong coupling.

---

## 5. Strong-Coupling Polymer Expansion and Mass Gap

### 5.1. Idea of the expansion

At strong coupling (small \(\beta = 1/g^2\)), expectation values of Wilson loops and plaquette operators can be expressed as convergent series over polymers (connected clusters of plaquettes and links). For a plaquette operator \(P_x = \Re\operatorname{Tr} U_{p(x)}\), its two-point function
\[
\langle P_x P_y\rangle
\]
has contributions from polymers that connect plaquettes near \(x\) and \(y\).

A standard argument shows that:

- Each “connected” polymer contributing to \(\langle P_x P_y\rangle_c\) must span the region between \(x\) and \(y\).
- The weight of a polymer of size \(|\Gamma|\) is proportional to \(\beta^{|\Gamma|}\).
- The number of polymers of a given size is exponentially bounded.

Therefore
\[
|\langle P_x P_y\rangle_c|\le C e^{-m(\beta)\,|x-y|},
\]
with
\[
m(\beta) \sim -\log(\kappa\beta)
\]
for some model-dependent \(\kappa\). This defines a finite correlation length and hence a mass gap in the OS-reconstructed theory.

### 5.2. C-sector specific gaps

If one uses C-even and C-odd plaquette operators \(P_x^\pm\), constructed e.g. by combining a plaquette with its complex conjugate appropriately, one can similarly analyze their correlators and obtain two mass scales \(m^\pm(\beta)\) corresponding to the lowest excitations in \(\mathcal{H}^\pm\).

Formally,
\[
\langle P_x^\pm P_y^\pm\rangle_c \sim e^{-m^\pm(\beta)|x-y|},
\]
leading to lattice mass gaps \(\Delta^\pm(a) = m^\pm(\beta)/a\).

---

## 6. LLM-Friendly Task Decomposition (Doc D)

To make this extended Doc D maximally useful for LLM-based work, here are explicit tasks:

1. **Task D1 (Exact Haar Jacobian coefficient).**  
   For \(G=SU(N)\), compute \(C_2(\text{ad})\) explicitly and derive the exact coefficient \(c_N\) in the small-\(A\) expansion of \(S_{\mathrm{measure}}(A)\).

2. **Task D2 (OS reconstruction step-by-step).**  
   Starting from the factorization of the Gibbs weight into time-slices, derive the transfer matrix \(T\) explicitly and verify its positivity, self-adjointness, and normalization. Then show how the Hamiltonian \(H=-\frac{1}{a}\log T\) is obtained.

3. **Task D3 (Explicit polymer expansion in 2D).**  
   In a simpler 2D SU(N) lattice gauge theory, perform an explicit polymer expansion for the plaquette–plaquette correlator and identify the leading exponential decay rate.

4. **Task D4 (C-sector projections).**  
   For a specific small lattice (e.g., \(2^4\)), construct the projectors onto \(\mathcal{H}^\pm\) and compute the first few eigenvalues of \(H\) numerically (in principle) in each sector, illustrating the sector splitting \(\Delta^+\neq\Delta^-\).

5. **Task D5 (Strong-coupling bound on \(\Delta^\pm(a)\)).**  
   Prove a rigorous lower bound \(\Delta^\pm(a)\ge c(\beta)\) in the strong-coupling regime, following the structure of Faria da Veiga–O’Carroll arguments, and identify explicitly how Haar-induced mass contributes.

These tasks can be dispatched individually to a model with this document as context to deepen or check specific constructive steps.

