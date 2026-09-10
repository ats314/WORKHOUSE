# Reconstruction, observable completeness, and a quantitative localization interface

This derivation uses the physical-time semigroup in Osterwalder–Schrader (OS), not an identification of physical time with an auxiliary diffusion parameter. The exact finite examples and optimization identities are checked by `ym_reconstruction.py`. The spectral theorem, measure limits, and the full OS reconstruction theorem below are analytic inputs; they have not been formalized in Lean in this file.

## 1. Source statements and the operator to be bounded

- [OS 1975](https://doi.org/10.1007/BF01608978), printed p. 291 (PDF p. 11), equations (5.2)–(5.3), constructs the Hilbert space from reflection positivity and its weakly continuous self-adjoint contraction semigroup `exp(-tH)`, with `H >= 0`. The paragraph immediately before (5.3) asserts totality of the field-generated vectors. This **totality**, as well as positivity, is essential for the full-space gap implication.
- OS 1975, pp. 282 and 287–288, repairs the regularity step of the 1973 paper using strengthened distribution or linear-growth assumptions. Its p. 291 semigroup statement is usable without repeating the failed multivariable continuation argument.
- [OS 1973](https://doi.org/10.1007/BF01645738), p. 89, remark 2 after (3.1), relates exponential clustering to a mass gap. Apply this within a reconstruction framework with its corrected hypotheses.
- [Jaffe–Witten](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), p. 6, sections 4–5, specifies a gap for the physical Hamiltonian and the resulting clustering. The full positive-energy spectrum is the target, beyond one carrier correlator.

Assume a reconstructed nonnegative self-adjoint `H`, a vacuum `Omega`, and a centered vector `F` in its physical Hilbert space. The spectral theorem gives a finite positive measure

\[
 C_F(t)=\langle F,e^{-tH}F\rangle
       =\int_{[0,\infty)}e^{-tE}\,d\nu_F(E),\qquad
 \nu_F(B)=\|P_H(B)F\|^2.
\]

For every `0 <= E < eta` and `t >= 0`, positivity gives

\[
 \nu_F([0,E])\le e^{Et}C_F(t). \tag{R1}
\]

If `C_F(t) <= A_F exp(-eta t)` for every `t`, (R1) and `t -> infinity` force `P_H([0,E])F=0`. If this holds with **one common eta > 0** for a dense linear set of centered physical vectors, boundedness of the spectral projection extends it to the whole vacuum orthocomplement. Taking a countable sequence `E` increasing to `eta` excludes spectrum in `(0,eta)`. The prefactor `A_F` may depend on `F`. Neither an upper bound on one correlator nor finitely many observables without a completeness argument supplies this density step.

## 2. A finite reflection-positive model one can inspect exactly

For positive weights `w_j` and transfer eigenvalues `0 < r_j <= 1`, set `C_n=sum_j w_j r_j^n`. Then

\[
 \sum_{k,l=0}^m\bar c_k c_l C_{k+l}
 =\sum_j w_j\left|\sum_{k=0}^m c_k r_j^k\right|^2\ge0. \tag{R2}
\]

This is reflection positivity of the finite-time kernel, not a reconstruction of a spacetime field theory. The check factors the four-by-four kernel exactly as `V diag(w1,w2) V^T`; its leading two-by-two determinant is `w1*w2*(r1-r2)^2`. The physical energies, when one step has duration `a`, are `E_j=-log(r_j)/a`. A rescaling of `a` changes the inferred gap. No diffusion eigenvalue appears in this definition.

## 3. Observable completeness is a testable interface

Let the two excited eigenvectors have observable-amplitude matrix

\[
 A=\begin{pmatrix}1&1\\1&-1\\0&1\end{pmatrix},\qquad
 A^*A=\operatorname{diag}(2,3)\succeq2I. \tag{R3}
\]

The summed correlator is `2 r1^n + 3 r2^n`. Each mode has a strictly positive weight. The exact identity `||Av||^2-2||v||^2=y^2` certifies the lower frame bound. Removing all but the row `(0,1)` makes the first sector invisible. Thus the finite version of OS totality is an explicit rank/lower-frame-bound computation. A finite carrier frame controls its own carrier subspace.

The existing G18 record already contains the fixed-spacing physical carrier frame, coefficient-to-GNS transport, and the no-dark-carrier result on momentum patches separated from Gamma. Those results are inputs to preserve. The two-dimensional example here is a calibration of the completeness mechanism, not a replacement for that stronger carrier construction. The remaining use of OS totality concerns the full vacuum complement and the continuum observable family; the existing carrier restriction does not by itself identify the isotropic Wilson transfer matrix.

## 4. What a localization plateau actually proves

Suppose only

\[
 C_F(t)\le A e^{-\eta t}+\varepsilon,\quad A,\eta,\varepsilon>0.
\]

Write `theta=E/eta` with `0<theta<1` and `x=exp(eta t)>=1`. Equation (R1) yields

\[
 \nu_F([0,E])\le\inf_{x\ge1}
       \left[A x^{\theta-1}+\varepsilon x^\theta\right]. \tag{R4}
\]

After multiplication by the positive `x^(2-theta)`, the derivative is the affine function `-A(1-theta)+epsilon*theta*x`. Its slope is positive; the minimizer is

\[
 x_* = \max\{1,A(1-\theta)/(\varepsilon\theta)\}.
\]

If the second argument exceeds one, the exact minimum is

\[
 \frac{A^\theta\varepsilon^{1-\theta}}
 {\theta^\theta(1-\theta)^{1-\theta}}. \tag{R5}
\]

Otherwise the minimum is `A+epsilon`. At `E=0`, letting `t` increase gives `nu_F({0})<=epsilon`. For `E>0`, (R5) generally scales as `epsilon^(1-E/eta)`, **not** linearly in epsilon. This sharpens the older note's informal small-spectral-weight description. A fixed nonzero error does not exclude any interval of low energies.

An exact falsifier is `T=diag(1,15/16,3/4)`, `Omega=(1,0,0)`, `F=(0,u,1)`. The centered physical correlator is

\[
 C_n=u^2(15/16)^n+(3/4)^n\le(3/4)^n+u^2.
\]

For arbitrarily small nonzero `u`, its slow mode still has energy `-log(15/16)/a`, strictly below `-log(3/4)/a`. At `u=0` the slow mode persists in the physical space but disappears from this correlator. This combines the plateau and incomplete-observable obstructions in one positive transfer model.

## 5. A precise sufficient repair, with its remaining hypothesis exposed

Here is a conditional route that can actually remove the plateau. Suppose, for every `R,t>=0`, an estimate has been established on the same physical correlation function:

\[
 C_F(t)\le A_F e^{-\eta t+\alpha R}+B_F e^{-\beta R},
 \quad \eta,\beta>0,\quad\alpha\ge0. \tag{R6}
\]

Choose `R=eta*t/(alpha+beta)`. Both exponents are exactly `-delta*t`, where

\[
 \delta=\frac{\eta\beta}{\alpha+\beta}>0. \tag{R7}
\]

Consequently `C_F(t)<=(A_F+B_F)exp(-delta*t)`. Section 1 now supplies the gap implication if the rate is common on a dense centered set. If `R` must be an integer, choosing its ceiling changes the prefactor by at most `exp(alpha)` and preserves the rate. Constants must also have the required cutoff and volume control.

The checked algebra is (R7), not the Yang-Mills estimate (R6). To use (R6), define the localization family, prove its bad-event tail `exp(-beta R)`, and bound the growth of the conditioned prefactor by `exp(alpha R)` while retaining the same decay rate `eta`. A family where `eta` deteriorates with `R` does not meet this hypothesis. A direct estimate with a time-decaying error would serve equally well.

The old unfixed **all-links-near-identity** good set is not a candidate for such a tail. The preserved repository extraction `notes/imported/EXTRACT_2026-09-01/EX-006-obstruction-haar-marginal.md`, items 1–2, derives Haar link marginals and product Haar on spanning trees for gauge-invariant measures. Its volume-small good set cannot be made overwhelmingly probable by a coupling argument. A new candidate must use a gauge-invariant or rigorously gauge-fixed localization with its own measure and Jacobian.

Falsifier for applying this route: a single allowed `(R,t,a,volume)` violating (R6), a vanishing uniform rate, or a nonzero spectral projection invisible to the proposed observable class. These are separate, measurable obligations. The route leaves G18/G19/G23 open while replacing a vague implication by exact interfaces.
