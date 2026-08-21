# 2D U(1) Villain Gauge Theory: Non-Negative Site Tensor, Gaussian Flux Truncation, and a θ-Sector Design Sketch
*(Extracted from the validated 2D U(1) TRG work + the proposed “strict θ sector” extension.)*

## 0. Why this is in the “keep and develop” pile

Two things here are genuinely valuable:

1. A **validated, strictly non-negative** tensor network for the \(\theta=0\) 2D U(1) Villain theory (already run with TRG successfully at large volume).
2. A clearly stated, *still-open but highly plausible* extension: a **strict \(Q\)-sector decomposition** for \(\theta\neq 0\) that would keep all local tensors non-negative and push the complex phase into a final global sum.

That second point is the 2D analogue of the rotor’s boundary-phase trick, and it looks like a gateway to “general theory” territory.

---

## 1. Villain flux representation (θ = 0)

Start from the Villain form on a square lattice with link variables \(U_\ell=e^{iA_\ell}\) and plaquette angles \(\vartheta_p\) (oriented sum of link angles around plaquette \(p\)):

\[
Z(\beta)
=
\int \prod_\ell dU_\ell
\prod_p \sum_{n_p\in\mathbb Z}
\exp\left[-\frac{\beta}{2}\big(\vartheta_p-2\pi n_p\big)^2\right].
\]

Integrating out the link variables yields a pure integer-flux model:

\[
Z(\beta)
=
\sum_{\{n_p\in\mathbb Z\}}
\left[\prod_x \delta(\text{Bianchi constraint at }x)\right]
\exp\left[-2\pi^2\beta\sum_p n_p^2\right].
\]

Everything is real and non-negative.

---

## 2. Site-tensor construction (θ = 0)

Place a tensor on each site \(x\), with four indices corresponding to the integer fluxes on the four plaquettes adjacent to \(x\): \(n_1,n_2,n_3,n_4\).

A consistent orientation gives the local constraint

\[
n_1-n_2+n_3-n_4 = 0.
\]

Define the site tensor

\[
T^{(x)}_{n_1 n_2 n_3 n_4}
=
\delta_{n_1-n_2+n_3-n_4,\,0}
\prod_{j=1}^{4}\exp\left[-\frac{2\pi^2\beta}{4}\,n_j^2\right].
\]

- Each tensor element is **non-negative**.
- Contracting these tensors over shared plaquette indices reproduces the flux partition function.

This construction is reported as “proven/validated” on a \(2\times 2\) lattice and used successfully in a large-scale TRG simulation.

---

## 3. Flux truncation bound (Gaussian tail)

Truncate each plaquette flux to \(|n_p|\le N_{\max}\).  
For a single plaquette weight \(w(n)=\exp(-2\pi^2\beta n^2)\), the tail beyond \(N_{\max}\) is

\[
S_{\text{tail}}(N_{\max})
=
2\sum_{n=N_{\max}+1}^\infty e^{-2\pi^2\beta n^2}.
\]

Bound the discrete sum by an integral with \(\alpha=2\pi^2\beta\):

\[
\sum_{n=N_{\max}+1}^\infty e^{-\alpha n^2}
\le
\int_{N_{\max}}^\infty e^{-\alpha x^2}\,dx
\le
\frac{1}{2\alpha N_{\max}}e^{-\alpha N_{\max}^2}.
\]

Hence:

\[
S_{\text{tail}}(N_{\max})
\lesssim
\frac{1}{2\pi^2\beta N_{\max}}\,e^{-2\pi^2\beta N_{\max}^2}.
\]

A union bound over \(N_{\text{plaq}}=L_xL_t\) plaquettes yields a global error bound of the form

\[
|Z-Z_{\text{TN}}(N_{\max})|
\le
C(\beta,L_x,L_t)\,e^{-c(\beta)N_{\max}^2},
\qquad c(\beta)=2\pi^2\beta,
\]

i.e. **Gaussian decay in \(N_{\max}^2\)** with only polynomial volume dependence in the prefactor.

Practical takeaway recorded in the archive: for \(\beta\approx 1\), \(N_{\max}=2\) or \(3\) is already extremely accurate.

---

## 4. θ ≠ 0: what exists vs what would be “strictly sign-free”

### 4.1 Existing working implementation: local phase factors + complex TRG

A prototype modifies local weights with phases like \(e^{i\theta n_{\text{plaq}}}\), producing a complex-valued tensor that TRG can still contract deterministically. This sidesteps Monte Carlo’s sign problem in practice, but local tensors are no longer non-negative.

### 4.2 Proposed strict sector decomposition (open engineering task)

The 2D U(1) archive proposes a strict analogue of the rotor trick:

1. Introduce an auxiliary index that tracks the **total topological charge** \(Q\in\mathbb Z\).
2. Build a TN that computes sector weights \(Z_Q^{(0)}(\beta)\ge 0\).
3. Form
   \[
   Z(\beta,\theta)=\sum_{Q\in\mathbb Z} e^{i\theta Q}\,Z_Q^{(0)}(\beta).
   \]

This would keep every local tensor non-negative and confine all phases to a final global sum.

---

## 5. A concrete design sketch for the strict sector TN

Here is the most direct design that fits the “Phase-Isolation Principle”:

### 5.1 Polynomial trick

Attach a formal variable \(z\) to each plaquette flux contribution:

\[
w(n_p)\quad\longrightarrow\quad w(n_p)\,z^{n_p}.
\]

Then the full contraction yields a Laurent polynomial

\[
P(z)=\sum_{Q\in\mathbb Z} Z_Q^{(0)}(\beta)\,z^Q,
\qquad Z_Q^{(0)}(\beta)\ge 0.
\]

Finally,
\[
Z(\beta,\theta)=P(e^{i\theta}).
\]

### 5.2 Implementing the accumulator efficiently

Naively tracking \(Q\) globally increases bond dimension by a factor \(\sim (2Q_{\max}+1)\).  
But because the coefficients are non-negative, one can:

- truncate \(Q\) using Gaussian tail estimates,
- contract while periodically compressing the \(Q\)-index (e.g., SVD truncation on the accumulator legs),
- evaluate \(P(z)\) at many \(z\) values on the unit circle and use FFT to reconstruct coefficients.

This is the natural 2D “next step” for turning the current working complex-\(\theta\) TRG into a strictly non-negative \(\theta\)-free TN plus a final phase sum.

---

## 6. What further work unlocks (in escalating order of ambition)

1. **Engineering proof-of-concept:** implement the \(Q\)-accumulator on small lattices and verify \(Z(\theta)\) matches the complex-phase implementation.
2. **Scaling study:** measure how \(Q_{\max}\) grows with volume and \(\beta\) in the Villain theory; test whether Gaussian tail bounds remain sharp in practice.
3. **Big-theory connection:** generalize the accumulator idea to other Abelian topological terms (e.g. higher-form gauge theories) where the charge is a cohomology class and still \(\mathbb Z\)-valued.
4. **Bridge attempt to non-Abelian:** identify whether a dual formulation exists where the relevant topological invariant becomes an additive integer label that can be accumulated similarly.

---

## Sources in the project

This document is distilled primarily from `TN_2D_U1_Detail_v2.md` and the simulation analysis note confirming the non-negative TRG pipeline.

