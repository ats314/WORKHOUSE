# UNIFY 04 — From Configuration-Space Spectral Gaps to OS Mass Gaps: A Dirichlet-Form Comparison Program

## Purpose of this extract

The project draws a careful distinction:

- \(\lambda_1^{\mathrm{conf}}(\Lambda)\): the spectral gap of the **configuration-space diffusion** generator \(-L_\Lambda^{\mathrm{inv}}\) on \(L^2(\mu_\Lambda)\), for gauge-invariant observables.
- \(\Delta_\Lambda\): the spectral gap of the **Osterwalder–Schrader Hamiltonian** \(H_\Lambda\) on the OS Hilbert space \(\mathcal H_\Lambda\); this is the finite-volume “mass gap”.

This note isolates the conjectural bridge (Conjecture D\(_\Lambda\)) and frames it as a **Dirichlet-form comparison problem**.

---

## 1. Two operators, two gaps, two Dirichlet forms

### 1.1 Configuration-space diffusion (Euclidean “mixing time”)

On the configuration manifold \(M_\Lambda\) with Gibbs measure \(\mu_\Lambda\),
\[
L_\Lambda f = \Delta_{g_\Lambda}f - \langle \nabla S_\Lambda,\nabla f\rangle.
\]
Restricting to gauge-invariant functions (and taking closures as needed) yields \(L_\Lambda^{\mathrm{inv}}\).

Its Dirichlet form is
\[
\mathcal E_\Lambda^{\mathrm{conf}}(f,f)
:= \int_{M_\Lambda} |\nabla f(U)|_{g_\Lambda}^2\,d\mu_\Lambda(U).
\]
The gap \(\lambda_1^{\mathrm{conf}}(\Lambda)\) is the best constant in the Poincaré inequality:
\[
\mathrm{Var}_{\mu_\Lambda}(f) \le \frac{1}{\lambda_1^{\mathrm{conf}}(\Lambda)}\,\mathcal E_\Lambda^{\mathrm{conf}}(f,f).
\]

### 1.2 OS Hamiltonian (Euclidean-time correlations)

Reflection positivity and OS reconstruction yield a Hilbert space \(\mathcal H_\Lambda\), a cyclic vacuum \(\Omega_\Lambda\), and a positive self-adjoint Hamiltonian \(H_\Lambda\ge 0\).

The OS Dirichlet form is
\[
\mathcal E_\Lambda^{\mathrm{OS}}(\Psi,\Psi)
:= \langle \Psi, H_\Lambda \Psi\rangle_{\mathcal H_\Lambda}.
\]

The mass gap is
\[
\Delta_\Lambda := \inf\big(\sigma(H_\Lambda)\setminus\{0\}\big) = E_1(\Lambda).
\]

---

## 2. Conjecture D\(_\Lambda\): a finite-volume spectral-to-mass comparison

A clean finite-volume version is:

> **Conjecture D\(_\Lambda\)** (spectral-to-mass).  
> There exists a constant \(c>0\), independent of \(\Lambda\), such that
> \[
> \Delta_\Lambda \ \ge\ c\,\lambda_1^{\mathrm{conf}}(\Lambda),
> \]
> (up to harmless dimensionless factors depending on normalization conventions).

This is *not* a tautology: \(e^{tL_\Lambda}\) and \(e^{-tH_\Lambda}\) are different semigroups living on different spaces.

---

## 3. Why a Dirichlet-form comparison is the right target

The spectral gap of a positive operator is, variationally, an infimum of Rayleigh quotients. Thus a comparison of gaps typically comes from a comparison of forms.

A schematic path to Conjecture D\(_\Lambda\):

1. Construct a linear map (“time-zero embedding”)
   \[
   \iota_\Lambda: L^2(\mu_\Lambda)\supset \mathcal A_\Lambda^{\mathrm{inv}} \longrightarrow \mathcal H_\Lambda
   \]
   sending a gauge-invariant observable \(f\) (supported on a time slice) to a vector in OS space, e.g.
   \(\iota_\Lambda(f)=f^{\mathrm{OS}}\Omega_\Lambda\).

2. Prove **two-sided norm control**:
   \[
   \| \iota_\Lambda(f)\|_{\mathcal H_\Lambda}^2 \asymp \|f\|_{L^2(\mu_\Lambda)}^2
   \quad \text{on a suitable dense subclass.}
   \]

3. Prove a **Dirichlet-form inequality**
   \[
   \mathcal E_\Lambda^{\mathrm{OS}}(\iota_\Lambda(f),\iota_\Lambda(f))
   \ \ge\ c\,
   \mathcal E_\Lambda^{\mathrm{conf}}(f,f).
   \]

If steps (2)–(3) hold with \(\Lambda\)-uniform constants, then (by Rayleigh quotient comparison) one gets
\(\Delta_\Lambda \ge c\,\lambda_1^{\mathrm{conf}}(\Lambda)\).

So Conjecture D\(_\Lambda\) is “just” a comparison principle—but “just” in the same way climbing Everest is “just walking”.

---

## 4. Where the difficulty lives

Several obstructions/unknowns are real:

- **Different dynamics.**  
  \(L_\Lambda\) is a reversible Markov generator in configuration space; \(H_\Lambda\) is the generator of Euclidean time translations after OS reconstruction. There is no algebraic reason the gaps must match or compare.

- **Domain and range issues.**  
  The map \(f\mapsto f^{\mathrm{OS}}\Omega_\Lambda\) is natural for time-slice observables, but its range may miss low-energy states relevant to the mass gap (or include only a non-closed subspace).

- **Locality vs gauge constraints.**  
  Gauge invariance and Gauss constraints affect the OS Hilbert space structure, potentially complicating simple comparisons.

- **Normalization and scaling.**  
  Any comparison constant \(c\) must be stable under changes in lattice spacing and volume along the desired scaling trajectory.

---

## 5. Concrete research directions suggested by the framework

This is where “new theory” could genuinely be born.

### 5.1 Compare semigroups via a Markov–transfer operator interpolation

One possible route is to build an intermediate operator that shares structure with both:

- \(P_t^\Lambda = e^{tL_\Lambda}\) is a Markov semigroup on \(L^2(\mu_\Lambda)\).
- \(T_\Lambda = e^{-aH_\Lambda}\) is a transfer matrix/OS semigroup on \(\mathcal H_\Lambda\).

If one can represent \(T_\Lambda\) as an integral operator on a time slice with kernel \(K\) built from the action, then compare \(K\) to the heat-kernel-like operator \(P_t^\Lambda\) via domination or log-Sobolev transport inequalities, one might be able to extract spectral comparisons.

### 5.2 A “Brascamp–Lieb on the quotient” philosophy

The curvature-driven results yield strong concentration and convexity *on the quotient/or horizontal directions*. If the OS Hamiltonian can be expressed in a form where its low-energy behavior is governed by the same convexity structure, then one can hope to compare gaps by a generalized Brascamp–Lieb inequality on the quotient space of gauge fields.

### 5.3 Identify a common Dirichlet form on a shared core

Another tactic: find a dense set of observables \(\mathcal C\) such that

- \(\mathcal C\subset L^2(\mu_\Lambda)\) is a core for the configuration diffusion form,
- \(\iota_\Lambda(\mathcal C)\) is a form core in \(\mathcal H_\Lambda\),
- both forms can be expressed via a common quadratic functional (e.g. gradients vs discrete time-shifts).

Then form comparison becomes a computable inequality on \(\mathcal C\), not an abstract statement.

---

## 6. Why this extract is worth isolating

The earlier curvature/FI work is *actionable* mathematics: it produces explicit constants and uniformity claims (conditional on Lyapunov/local-FI inputs).
Conjecture D\(_\Lambda\) is the missing conceptual hinge that would convert those analytic controls into the physically correct mass-gap statement.

Framing it as a Dirichlet-form comparison clarifies what needs to be built:

- a precise “dictionary” between time-slice observables and OS states,
- a quantitative inequality between two quadratic forms.

If that dictionary can be made sharp, the project’s curvature machinery becomes directly relevant to the Clay mass-gap goal.

