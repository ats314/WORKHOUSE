# Formal bridges from the Yang-Mills source collection

The new Lean layer proves the finite ground-state transform and transports a
weighted Poincare bound to the physical matrix form. It also proves the
mean-residual budget, the quartic Gaussian residual floor and global frequency
optimization, and finite algebra used by Simon's transverse confinement method.

The source is [Basic.lean](../../lean/Workhouse/Basic.lean); every theorem is
mapped in [theorems.yaml](../../ledger/theorems.yaml). No new axiom is introduced.
The theorem statements expose their hypotheses. The infinite-dimensional
Yang-Mills construction, global curvature estimate, and regulator-uniform
physical mass gap remain the open obligations recorded by G19, G20 and G23.

## Exact finite ground-state identification

Let `H` be any real symmetric matrix on a finite index set, and let `psi` and
`f` be real vectors. Define

\[
q_H(x)=\sum_{i,j}H_{ij}x_ix_j,\qquad
D_\psi(f)=\frac12\sum_{i,j}(-H_{ij})\psi_i\psi_j(f_i-f_j)^2.
\]

If `sum_j H_ij psi_j = R_i psi_i`, Lean proves

\[
q_H(\psi f)=D_\psi(f)+\sum_iR_i\psi_i^2f_i^2.
\tag{F-1}
\]

The proof expands the squared differences. Symmetry identifies the two
diagonal sums, and the row equation evaluates each. This works for every finite
index type, rather than only the three-dimensional symbolic check. The
`finite_ground_state_ratio_identity` corollary defines the residual by
`R_i=(H psi)_i/psi_i` and discharges the row equation when all `psi_i` are nonzero.
No positivity or exact-ground-state assumption is needed for this identity.

When `psi_i >= 0` and `H_ij <= 0` off the diagonal, every edge contribution is
nonnegative. Diagonal entries have no sign restriction because their squared
differences vanish. This sign condition is a property to verify in the chosen
Hamiltonian basis; it is not automatic for every real symmetric matrix.

For an exact eigenvector `H psi = E psi`, the residual is constant and (F-1)
becomes

\[
q_H(\psi f)-E\sum_i\psi_i^2f_i^2=D_\psi(f).
\tag{F-2}
\]

Suppose the weighted Poincare estimate

\[
\gamma\sum_i\psi_i^2f_i^2\le D_\psi(f),\qquad
\sum_i\psi_i^2 f_i=0
\]

holds. `finite_ground_state_gap_transfer` constructs `f_i=x_i/psi_i` and proves

\[
\gamma\sum_i x_i^2\le q_H(x)-E\sum_i x_i^2,
\qquad \sum_i\psi_ix_i=0.
\tag{F-3}
\]

Thus the transformed test vectors cover every physical vector orthogonal to
`psi`. The theorem does not conceal a completeness or surjectivity assumption.
The Poincare estimate is an explicit premise, and a positive gap follows only
when its constant is positive. There is no identification with an unrelated
sampling or Euclidean transfer generator.

This finite bridge is the algebraic counterpart of the source-normalized
conjugation discussed in
[the weighted-curvature derivation](yangmills-weighted-curvature.md), based on
MMM 2019, equations II.2, II.9 and II.16, and Mondal 2023, equations 4.1 and 4.9.
The differential identity and its physical prefactor are checked separately at
T1; Lean does not formalize those differential operators here.

## A trial residual needs a floor and a mean

Given energy comparisons `E1 >= gamma+rmin` and `E0 <= meanR`, Lean proves

\[
E_1-E_0\ge\gamma-(\mathrm{mean}R-r_{\min}).
\tag{F-4}
\]

Its exact defect is the sum of the two nonnegative comparison slacks:

\[
(E_1-E_0)-[\gamma-(\mathrm{mean}R-r_{\min})]
=[E_1-(\gamma+r_{\min})]+[\mathrm{mean}R-E_0].
\]

There is no upper-bound requirement on the residual itself. Applying this
arithmetic to a Schrödinger operator requires the common form domain, the
comparison operator and its gap, a lower residual bound, an admissible trial
vector with finite mean residual, and the min-max/Rayleigh comparisons.
Those analytic statements are supplied conditionally in GST-6; they are not
axioms added to Lean.

## The pure quartic Gaussian certificate

For the trial state with `S(x)=m omega x^2/2`, the residual of
`H=-(hbar^2/(2m)) d^2/dx^2 + lambda x^4` is

\[
R(x)=\frac{\hbar\omega}{2}-\frac{m\omega^2x^2}{2}+\lambda x^4.
\]

At `m^2 omega^3 = 6 lambda hbar`, Lean proves the exact square completion

\[
R(x)=\frac{\hbar\omega}{8}
+\lambda\left(x^2-\frac{m\omega^2}{4\lambda}\right)^2.
\tag{F-5}
\]

For `lambda>0` this is a global residual floor, including arbitrarily large
`x`. The Gaussian mean `3 hbar omega/8` is computed in the T1 derivation from
the Gaussian moment recurrence. It is not promoted to T0 by the square
completion. Given that mean and comparison gap `hbar omega`, the formal
budget arithmetic is `3 hbar omega/4`.

More strongly, for every positive frequency ratio `q=omega/omega_star`, Lean
proves

\[
\frac34-\left(\frac{5q}{4}-\frac1{8q^2}-\frac{3q^4}{8}\right)
=\frac{(q-1)^2(3q^4+6q^3+9q^2+2q+1)}{8q^2}\ge0.
\tag{F-6}
\]

Equality holds if and only if `q=1`. This proves the global and unique optimum
within this Gaussian residual-floor family. It does not identify the true
quartic spectral gap or optimize over all possible trial profiles.

## Algebra for Simon's transverse mechanism

For arbitrary finite real families `a_i,u_i`, Lean proves

\[
\left(\sum_i a_i^2\right)\left(\sum_i u_i^2\right)
-\left(\sum_i a_i u_i\right)^2
=\frac12\sum_{i,j}(a_i u_j-a_j u_i)^2.
\tag{F-7}
\]

This identity applies separately to each transverse coordinate in the
commuting-valley expansion. Lean additionally proves the slice remainder

\[
T+V-(T/2+cR)=\frac{n(T+2V)-2ncR}{2n},\qquad n>0,
\]

and its lower-bound implication. After a Hardy scale is established, the
radial algebra is certified by

\[
\frac1{2z^2}+z-\frac32
=\frac{(z-1)^2(2z+1)}{2z^2}\ge0,\qquad z>0.
\]

The analytic oscillator slice, Hardy inequality, form closure and compactness
arguments are described in
[the Simon derivation](yangmills-simon-flat-directions.md). These Lean lemmas
certify their finite algebra and normalization. A positive ground-energy
estimate before vacuum subtraction is distinct from a positive `E1-E0`.

## Verification and promotion boundary

Run `lake build --wfail` from `lean/`. The new theorems use only the existing
mathlib import and standard Lean axioms; there are no `sorry` placeholders.

Four exact checks have complete theorem mappings: the finite matrix residual
identity, mean-residual budget arithmetic, balanced slice aggregation, and
global Gaussian frequency optimization. The full quartic certificate remains
T1 because its Gaussian moment and differential checks extend beyond the Lean
polynomial lemmas. The finite valley identity does not promote the complete
Hessian-spectrum check, and the radial inequality does not promote the complete
Hardy or compactness argument.
