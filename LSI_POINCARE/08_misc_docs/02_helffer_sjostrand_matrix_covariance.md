# Helffer--Sj"ostrand covariance representation (matrix form) and the “no scalarization” payoff

\begin{abstract}
For the reversible diffusion generator associated with a Gibbs measure on a Riemannian configuration manifold, the Helffer--Sj"ostrand representation expresses covariances of observables as an $L^2$ pairing of gradients through the inverse of a positive operator $\mathcal L^{(1)}$. Combined with a *matrix* lower bound on the Bakry--\'{E}mery curvature matrix (the “hinge”), this yields a Brascamp--Lieb-type covariance inequality in which the inverse of the **massive Maxwell operator** appears explicitly.
\end{abstract}

## 1. Setting: reversible diffusion on the configuration manifold

Let $M_\Lambda = G^{E(\Lambda)}$ be the configuration manifold with product metric and let
\[
\nu_\Lambda(dU) := Z_\Lambda^{-1} e^{-S_\Lambda(U)}\, d\mathrm{vol}_{g_\Lambda}(U)
\]
be a Gibbs measure with $S_\Lambda\in C^2(M_\Lambda)$. Let
\[
L f := \Delta f - \langle \nabla S_\Lambda, \nabla f\rangle
\]
be the symmetric generator on $L^2(\nu_\Lambda)$, with carré du champ
\[
\Gamma(f,g)=\langle\nabla f,\nabla g\rangle,
\qquad \Gamma(f)=|\nabla f|^2,
\]
and Dirichlet form
\[
\mathcal E_\Lambda(f,g) := \int \Gamma(f,g)\, d\nu_\Lambda = -\int f\,L g\, d\nu_\Lambda.
\]

## 2. The first-order lifted operator $\mathcal L^{(1)}$

Let $\nabla f$ be a (vector-valued) $1$-form on $M_\Lambda$.
Define the Bochner/Helffer--Sj"ostrand operator on $1$-forms
\[
\mathcal L^{(1)} := (-L)\otimes I + \mathrm{Ric}_{\nu_\Lambda},
\]
where the Bakry--\'{E}mery curvature matrix is
\[
\mathrm{Ric}_{\nu_\Lambda}(U) := \mathrm{Ric}_{g_\Lambda}(U) + \nabla^2 S_\Lambda(U),
\]
viewed as a self-adjoint endomorphism of the tangent space (or of the right-trivialized fiber).
Since $-L\succeq 0$ on $L^2(\nu_\Lambda)$, we always have
\[
\mathcal L^{(1)} \succeq \mathrm{Ric}_{\nu_\Lambda}.
\]

## 3. Helffer--Sj"ostrand representation

A standard HS identity gives, for sufficiently smooth $F,G$,
\[
\mathrm{Cov}_{\nu_\Lambda}(F,G)
:= \nu_\Lambda(FG)-\nu_\Lambda(F)\nu_\Lambda(G)
= \int \left\langle \nabla F, (\mathcal L^{(1)})^{-1}\nabla G\right\rangle\, d\nu_\Lambda.
\tag{HS}
\]

This is an identity, not a bound.

## 4. From HS to a **matrix covariance bound** using the hinge

Assume that on a region $K\subset M_\Lambda$ (a “good/small-field set”) one has the pointwise operator lower bound
\[
\mathrm{Ric}_{\nu_\Lambda}(U)\ \succeq\ M\qquad (U\in K),
\]
for some positive operator $M$ on the appropriate sector (typically the horizontal sector for gauge-invariant observables).
Then on $K$,
\[
(\mathcal L^{(1)})^{-1} \preceq M^{-1}
\quad\text{(monotonicity of inverse on positive operators)}.
\]
Plugging into (HS) yields the localized Brascamp--Lieb-type inequality
\[
|\mathrm{Cov}_{\nu_{\Lambda,K}}(F,G)|
\le
\int \left\langle \nabla F, M^{-1}\nabla G\right\rangle\, d\nu_{\Lambda,K},
\]
where $\nu_{\Lambda,K}$ denotes the conditional measure $\nu_\Lambda(\cdot\mid K)$.

### The “massive Maxwell” specialization

In the Wilson--Haar setting, the hinge from the companion note gives on $K_\Lambda(r)$ (after choosing $r$ so the remainder is absorbed)
\[
M
:= \frac{c_H}{2} I + t\, d_1^*d_1,
\]
restricted to horizontals (so gradients of gauge-invariant observables live in the form domain of $M$).

## 5. Why this is potentially publishable even if the global program stalls

Two pieces here are “structurally strong”:

1. **No scalarization.** The HS identity is naturally matrix-valued. Keeping $d_1^*d_1$ intact preserves geometric sparsity and enables finite-range Green function bounds.
2. **Modularity.** This covariance representation can be reused in other lattice gauge or constrained manifold Gibbs measures, whenever a Bakry--\'{E}mery lower bound is available on a suitable set.

## 6. What remains to complete a fixed-cutoff clustering theorem

To turn the localized HS bound into an unconditional bound under $\nu_\Lambda$:

- control the Green kernel $(M^{-1})_{\ell\ell'}$ (finite-range Combes--Thomas / Fourier methods),
- control the localization error $\nu_\Lambda(K^c)$ and its effect on covariances (see the localization lemma note).
