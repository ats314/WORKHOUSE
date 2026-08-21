# Diffusion gaps vs OS mass gaps: a quadratic-form comparison program

## Executive summary

The project files propose an attractive bridge:

\[
\text{(configuration-space diffusion spectral gap)}
\quad\Longrightarrow\quad
\text{(Osterwalder--Schrader Hamiltonian gap / mass gap)}.
\]

The idea is simple: if *somehow* the Euclidean-time correlators can be dominated by diffusion mixing at rate $\lambda_*$, then the OS spectral representation forces the physical gap $\Delta$ to satisfy $\Delta\ge\lambda_*$.

This note extracts the cleanest form of the argument and, crucially, isolates the **missing analytic step**: diffusion time and Euclidean time are not automatically comparable. The comparison must be justified via an explicit operator/semigroup inequality.

---

## 1. Two semigroups, two inner products

### (A) Diffusion semigroup on configuration space

Let $(M_\Lambda,g_\Lambda)$ be the finite lattice configuration manifold and $\mu_\Lambda$ the Gibbs measure. The reversible diffusion generator is
\[
L_\Lambda f = \Delta_{g_\Lambda} f - \langle \nabla S_\Lambda,\nabla f\rangle,
\qquad P_t^\Lambda := e^{tL_\Lambda}.
\]

A global Poincaré inequality on the gauge-invariant sector gives
\[
\|P_t^\Lambda f - \mu_\Lambda(f)\|_{L^2(\mu_\Lambda)}
\le e^{-\lambda_* t}\, \|f-\mu_\Lambda(f)\|_{L^2(\mu_\Lambda)}.
\]
Equivalently, the diffusion spectral gap on invariants satisfies $\lambda_1^{\rm inv}\ge\lambda_*$.

### (B) OS transfer matrix and physical Hilbert space

If the lattice measure is reflection positive, the OS construction produces a Hilbert space $\mathcal H_{\rm OS}$, a cyclic vacuum $\Omega$, and a positive transfer matrix $T_a$ (time-lattice spacing $a$). The Hamiltonian is
\[
H_a := -\frac{1}{a}\log T_a,
\]
with physical spectral gap
\[
\Delta_\Lambda(a) := \inf\bigl(\sigma(H_a)\setminus\{0\}\bigr).
\]

For an OS-positive observable $F$ supported at positive times, the Euclidean-time two-point function admits the spectral representation
\[
C_F(t)
:=
\langle \Omega,\, F\, e^{-tH_a}\, F\, \Omega\rangle
=
\int_{\Delta_\Lambda(a)}^\infty e^{-t\lambda}\, d\nu_F(\lambda),
\]
for a positive measure $\nu_F$.

---

## 2. The tempting inequality and what it would imply

Suppose one could prove a uniform (in $\Lambda$) bound of the form
\[
C_F(t)
\;\le\;
\|F\|_{L^2(\mu_\Lambda)}^2\, e^{-\lambda_* t}
\quad\text{for all }t\ge0,
\]
for a sufficiently rich class of OS-positive observables $F$.

Then, since
\[
C_F(t)\le e^{-\Delta_\Lambda(a)t}\int d\nu_F,
\]
comparison of exponential decay rates forces
\[
\boxed{\Delta_\Lambda(a)\ge \lambda_* .}
\]

This is the "diffusion gap bounds mass gap" punchline.

---

## 3. The missing bridge: diffusion time $\neq$ Euclidean time

The inequality above is *not automatic*, because:

- $P_t^\Lambda$ is a Markov semigroup on **configuration space** with respect to $\mu_\Lambda$.
- $e^{-tH_a}$ is a semigroup on the **OS Hilbert space** implementing **time translations** of fields.

These are different objects. To make the comparison honest, one needs a statement like:

> There exists a map $\mathfrak J$ from OS-positive time-slice observables into $L^2(\mu_\Lambda)$ such that
> \[
> \langle \Omega, F\, e^{-tH_a} F\,\Omega\rangle
> \le
> \langle \mathfrak JF,\, P_{ct}^\Lambda\,\mathfrak JF\rangle_{L^2(\mu_\Lambda)}
> \]
> for some $c>0$ independent of $\Lambda$ (and ideally $a$).

Equivalently, one seeks a **quadratic-form comparison** (one-step is enough):
\[
\boxed{
\langle \psi, H_a \psi\rangle_{\mathcal H_{\rm OS}}
\;\ge\;
c\, \mathcal E_\Lambda(f,f)
\quad\text{for }\psi=[F],\;f=\mathfrak JF,
}
\]
where $\mathcal E_\Lambda$ is the diffusion Dirichlet form
\[
\mathcal E_\Lambda(f,f)=\int_{M_\Lambda}\|\nabla f\|^2\, d\mu_\Lambda.
\]

If this held on a dense domain, then spectral gaps would compare:
\[
\Delta_\Lambda(a)\ge c\,\lambda_1^{\rm inv}(\Lambda)\ge c\,\lambda_*.
\]

---

## 4. Why the comparison might be plausible here

The project files implicitly lean on two structural facts:

1. **Reflection positivity gives a transfer matrix** and a controlled time translation.
2. **Gauge invariance makes diffusion curvature relevant**, because gradients of gauge-invariant functions lie in the horizontal bundle where curvature bounds are available.

The hope is that, on time-slice observables, both the OS form and the diffusion form reduce (after coarse-graining / integration over half-lattices) to comparable quadratic functionals.

---

## 5. What a rigorous route would likely require

A realistic rigorous program looks like this:

1. **Work at fixed lattice spacing $a$** and finite volume.
2. Prove a **one-step comparison** between:
   - the transfer matrix $T_a$ (or its generator $H_a$),
   - and a suitable Markov generator acting on the same time-slice algebra.
3. Use the SAFE-region curvature/LSI machinery to get a **uniform diffusion gap** $\lambda_*$.
4. Transfer to a **uniform OS gap** via the quadratic-form comparison.
5. Only then attempt to pass to the continuum.

The key difficulty is Step 2.

---

## 6. Provenance in this project

This program is extracted primarily from:

- `Full Proof Attempt at 12-10-25 Many holes.txt` (the proposed decay-rate comparison and the statement $\Delta_\Lambda\ge\lambda_*$),
- `Comparing Diffusion and OS Gaps.txt` (the idea of a one-step OS/Dirichlet comparison and the physical-sector curvature input).

This note intentionally sharpens the logic by isolating the extra inequality that must be proven for the implication to be valid.

