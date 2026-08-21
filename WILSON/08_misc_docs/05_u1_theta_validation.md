# 2D $U(1)$ $\theta$-physics as a validation harness

**Source notebooks:** `gauge_theory_theta_scan.ipynb`, `U1_2D_Genuine_ChiTop.ipynb`

## Why this note exists

The 4D $SU(2)$ construction in this project is ambitious and uses nontrivial algebraic machinery (quantum $6j$ symbols, rank-8 tensors, HOTRG truncations). A good scientific habit is to keep a nearby “toy universe” where:

- topological charge is unambiguous,
- $\theta$-dependence is well understood,
- and multiple numerical methods can be cross-checked.

2D $U(1)$ lattice gauge theory is exactly such a universe.

---

## 1. Sector decomposition and $\theta$ dependence

For an integer topological charge $Q\in\mathbb{Z}$, the canonical identity is:
\[
Z(\theta) = \sum_{Q\in\mathbb{Z}} P(Q)\,e^{i\theta Q}.
\]

If $P(Q)=P(-Q)$, then
\[
Z(\theta) = P(0) + 2\sum_{Q>0} P(Q)\cos(\theta Q),
\]
so $Z(\theta)$ is real and even.

Define
\[
F(\theta) = -\Re\log Z(\theta).
\]

The topological susceptibility is
\[
\chi_{\rm top} = \frac{1}{V}\left.\frac{\partial^2 F}{\partial\theta^2}\right|_{\theta=0}
= \frac{1}{V}\bigl(\langle Q^2\rangle - \langle Q\rangle^2\bigr).
\]

In CP-symmetric sampling, $\langle Q\rangle\approx 0$, hence $\chi_{\rm top}\approx \langle Q^2\rangle/V$.

---

## 2. The TRG-style tensor construction used in the notebook

The TRG notebook uses a flux-integer formulation (Villain-like), with integer flux labels $n\in[-N_{\max},N_{\max}]$ and a constraint implementing flux conservation (a Bianchi identity):

\[
n_i + n_j - n_k - n_l = 0.
\]

This constraint defines the nonzero tensor entries. A (real, positive) weight is then assigned, e.g. of Villain form:
\[
w(n)\propto \exp\!\left(-\beta \frac{(2\pi n)^2}{2}\right),
\]
and a “charge tensor” is tracked in parallel so that $\theta$-dependence can be reconstructed.

This is a concrete example of how one can avoid sampling a complex action directly.

---

## 3. The Monte Carlo sector-measurement approach

The second notebook implements a direct Monte Carlo sampler for $U(1)$ link angles, then estimates topological charge per configuration from plaquette angles. From the empirical sector histogram $P(Q)$ one reconstructs:

\[
Z(\theta) \approx \sum_Q P(Q)e^{i\theta Q}.
\]

This provides an independent route to $F(\theta)$ and $\chi_{\rm top}$.

---

## 4. How to use this as a “unit test” for the 4D pipeline

1. Run 2D $U(1)$ TRG and MC at the same parameters.
2. Compare:
   - periodicity of $F(\theta)$,
   - evenness of $F(\theta)$,
   - $\chi_{\rm top}$ from Fourier fits vs $\langle Q^2\rangle/V$.
3. Only once these agree within expected truncation/MC error should the same extraction pipeline be trusted for the harder 4D model.

---

## 5. Why this matters for the $SU(2)$ project

In a nonabelian 4D theory, defining and measuring $Q$ is hard, and a naive $\theta$-term introduces a severe sign problem. The $U(1)$ toy model is the place where your data-analysis and tensor-contraction logic can be tested without that complexity.

If the $U(1)$ harness is solid, and the $SU(2)$ model produces stable, symmetry-consistent $F(\theta)$ with positive $\chi_{\rm top}$, you have a much stronger case that the quantum-group deformation approach is capturing genuine $\theta$-dependent physics (whether or not it is exactly Yang–Mills).

