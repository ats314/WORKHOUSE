# Spectral Gap Pipeline: Curvature → Covariance → Kernel Decay → Clustering → OS Mass Gap

## Scope

This document isolates a closed analytic pipeline that turns **local geometric coercivity** into a **spectral gap** statement for a reconstructed Hamiltonian, via:

1. Helffer–Sjöstrand covariance representation on a compact manifold / configuration space.
2. Operator-order comparison (curvature/hinge → deterministic inverse).
3. Deterministic inverse **off-diagonal decay** (Combes–Thomas / Davies).
4. Conditional-to-unconditional upgrade (localization algebra + typicality).
5. OS reconstruction and Euclidean decay ⇒ Hamiltonian gap.
6. Gap permanence interfaces for limits (forms / projective limits).

Only statements already present in the project corpus are used.

---

## 1. Helffer–Sjöstrand (HS) covariance representation

### 1.1 Diffusion / generator setup

Let \((M,g)\) be compact Riemannian, \(S\in C^2(M)\), and \(d\mu = Z^{-1} e^{-S}\,d\mathrm{vol}_g\). Let \(L\) be the \(\mu\)-symmetric generator (Appendix E interface, used in Appendix F).

External Input **F.2**: Poisson solvability on the mean-zero subspace: for \(G\) with \(\mu(G)=0\), solve \(-Lu=G\) with \(\mu(u)=0\).

### 1.2 HS operator on vector fields

Define the drifted connection Laplacian on vector fields \(((-L)\otimes I)\Xi\) and the HS/Witten operator
\[
\mathcal L^{(1)}\Xi := ((-L)\otimes I)\Xi + \mathrm{Ric}_\mu(\Xi),
\qquad \mathrm{Ric}_\mu := \mathrm{Ric}_g+\nabla^2 S.
\]

Key commutation:
\[
\nabla(-Lu) = \mathcal L^{(1)}(\nabla u).
\]

External Input **F.12**: invertibility of \(\mathcal L^{(1)}\) on the relevant sector.

### 1.3 HS covariance identity (Appendix F, Theorem F.13)

For smooth \(F,G\) with \(\mu(G)=0\),
\[
\boxed{
\mathrm{Cov}_\mu(F,G)
=
\int_M \left\langle \nabla F, \big(\mathcal L^{(1)}\big)^{-1}\nabla G \right\rangle_g\,d\mu.
}
\]

---

## 2. Curvature/hinge → deterministic inverse

If a pointwise endomorphism lower bound holds on a domain \(\mathcal D\subset M\),
\[
\mathrm{Ric}_\mu(U)\succeq M \succeq m^2 I \quad \forall U\in\mathcal D,
\]
then (Appendix F, Proposition F.15)
\[
\mathcal L^{(1)} \succeq M,\qquad (\mathcal L^{(1)})^{-1}\preceq M^{-1}
\]
(as quadratic forms on vector fields supported in \(\mathcal D\)).

Corollary (Appendix F, Corollary F.16): matrix Brascamp–Lieb type bound
\[
|\mathrm{Cov}_\mu(F,G)|
\le
\Big(\int \langle \nabla F, M^{-1}\nabla F\rangle\,d\mu\Big)^{1/2}
\Big(\int \langle \nabla G, M^{-1}\nabla G\rangle\,d\mu\Big)^{1/2}.
\]

---

## 3. Deterministic inverse kernel decay

### 3.1 Combes–Thomas inverse decay (Appendix G)

For a uniformly positive self-adjoint finite-range operator \(A\) on a finite graph with fiber, Appendix G proves:
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}
\le \frac{2}{a_0(A)}\exp(-\eta_{\mathrm{CT}}(A)\,\mathrm{dist}(x,y)).
\]

Specialization (Appendix G, Proposition G.4.1): massive Maxwell operator \(M_{\Lambda_L}\) on links satisfies
\[
\|(M_{\Lambda_L}^{-1})_{bb'}\|_{\mathrm{op}}
\le \frac{2}{m_H^2}\exp(-\eta_{\mathrm{CT}}(M_{\Lambda_L})\,\mathrm{dist}_E(b,b')).
\]

### 3.2 Davies semigroup method (Appendix H)

Appendix H proves an alternative decay bound using Laplace transform of the semigroup and Davies conjugation:
\[
M^{-1}=\int_0^\infty e^{-m_H^2 t}\,e^{-tL}\,dt,
\]
with a conjugated semigroup norm bound yielding
\[
\|(M^{-1})_{bb'}\|_{\mathrm{op}}
\le C(\lambda)\,e^{-\lambda\,\mathrm{dist}_E(b,b')},
\]
under an explicit admissibility condition on \(\lambda\).

### 3.3 Riccati-flux CT derivation (12-23-25 PULSE)

The PULSE note supplies a CT-style exponential resolvent decay derived from a Riccati inequality after exponential conjugation (continuous/discrete variants). It is compatible with the deterministic kernel-decay role of Appendix G/H.

---

## 4. Conditional → unconditional: localization + typicality

### 4.1 Localization algebra (Appendix I)

For an event \(K\) with \(0<\mu(K)<1\), Appendix I gives the exact covariance decomposition
\[
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,\Delta_K F\,\Delta_K G,
\]
and a universal bound
\[
|\mathrm{Cov}_\mu(F,G)| \le |\mathrm{Cov}_{\mu_K}(F,G)| + 8\|F\|_\infty\|G\|_\infty\,\mu(K^c).
\]

### 4.2 Typicality mechanism for a canonical good set (Appendix J)

Appendix J constructs a canonical good set \(K_{\Lambda_L}(\varepsilon)\) based on the average plaquette potential and proves a volume-scale bound
\[
\mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)\le \exp(-c_{\mathrm{typ}}|P(\Lambda_L)|)
\]
under explicit conditions. This supplies the smallness of \(\mu(K^c)\) needed to upgrade conditional bounds to unconditional ones.

---

## 5. Reflection positivity and OS gap extraction

### 5.1 Reflection positivity (Appendix K)

Appendix K proves finite-volume OS reflection positivity for the Wilson measure \(\mu_{\Lambda_L,\beta}\) w.r.t. a time reflection, for all positive-time observables \(F\):
\[
\mathbb E_{\Lambda_L,\beta}[(\theta F)F]\ge 0.
\]

### 5.2 OS reconstruction and spectral lemma (Appendix L)

Appendix L isolates the OS interface:

- External Input **L.2.6**: OS reconstruction (Hilbert space \(\mathcal H_{\mathrm{OS}}\), contraction \(T\), transfer identity).
- Proposition: \(T=e^{-aH}\) defines \(H\ge0\).
- Lemma L.3.2: discrete-time decay of \(\langle\psi,e^{-naH}\psi\rangle\) implies a spectral gap on the spectral measure of \(H\).
- Theorem L.4.7: Euclidean exponential decay of centered OS correlations implies \(\mathrm{gap}(H)\ge \eta/a\).

---

## 6. Permanence interfaces (Appendix M) + external inputs ledger (Appendix N)

Appendix M proves:

- reflection positivity is preserved under reflection-equivariant coarse-graining pushforward;
- gap inequalities persist under monotone supremum limits of quadratic forms (Proposition M.2.6), with operator representation isolated as External Input **M.2.7**.

Appendix N is the global registry enforcing “no hidden imports,” listing external inputs F.2, F.7, F.12, F.20, L.2.6, M.2.7.

---

## 7. What is novel/high-leverage here

This pipeline is structurally “complete”: it provides a modular route from local curvature/coercivity to a spectral gap claim, with interfaces (typicality/localization, RP/OS, kernel decay) that are normally scattered across disparate literatures.

The highest-leverage extension targets are:

- make the hinge/curvature lower bound \( \mathrm{Ric}_\mu \succeq M\) explicit on the canonical good set \(K_{\Lambda_L}\) (the missing local dragon);
- certify deterministic inverse decay constants uniformly in volume (Appendix G/H constants are structured for this);
- connect the resulting Euclidean decay rate to OS gap extraction with explicit constants.

