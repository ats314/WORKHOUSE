# Quantitative use of the proved positive-reference Schur step

The finite-step theorem in `compact_residual.md` now applies to the actual
compact square, with its true source algebra and nonreducing graph. This
note identifies exactly which scale bounds would make its error budget
summable; it does not assert those bounds for the coupled Wilson family.

## Relative coupling increments

Suppose the actual transported derivative constants on a step based at
s obey M_k(s)<=c_k s^(-k), k=1,2,3. Set r=|t-s|/s and require c1 r<1.
Substituting these bounds into the proved cubic Schur remainder gives

\[
\frac{|\mathcal E_{s,t}[p]|}{b_s[p]}
\le\beta r^3\left[
\frac{c_3}{6}+
\frac{c_1c_2+r c_2^2/4+c_1^3}{1-c_1r}\right].
\tag{B1}
\]

This concerns the complete actual compact step. No reference at g=0,
Gaussian form comparison, or classical conditional measure occurs in
the substitution.

For the illustrative running sequence
\(g_j=\sqrt{\kappa/(j+n_0)}\), write n=j+n0. Then

\[
r_j=1-\sqrt{\frac n{n+1}}\le\frac1{2n}.
\]

If n0>=max(1,c1), the fast comparison loss is at most one half. Equation
(B1) therefore yields

\[
\frac{|\mathcal E_j[p]|}{b_{g_j}[p]}
\le\frac{C_*}{n^3},
\quad
C_*=\frac\beta8\left[
\frac{c_3}{6}+2c_1c_2+2c_1^3+\frac{c_2^2}{4n_0}\right].
\tag{B2}
\]

Thus the local relative remainder budget is summable under the stated
derivative scaling. Establishing that scaling is substantive: compact
positive-coupling smoothness alone does not bound c_k as s tends to zero.

## Do not discard the changing source energy

The actual source comparison in the finite-step theorem also gives

\[
b_{g_{j+1}}[R_jp]\le(1+c_1r_j)b_{g_j}[p].
\]

Consequently a source transported through j steps can have energy at
most

\[
b_{g_j}[R_{j-1}\cdots R_0p]
\le e^{c_1/(2n_0)}
\left(\frac{n_0+j}{n_0}\right)^{c_1/2} b_{g_0}[p].
\tag{B3}
\]

When errors are expressed in the initial source norm, the bound supplied
by (B2)-(B3) is summable if c1<4. More generally, any independently proved
upper source-energy growth O(n^alpha) with alpha<2 suffices. If this
condition fails, these particular bounds do not settle the accumulated
error; one needs a better one-sided source comparison or a correctly
renormalized norm budget.

These are coupling comparisons on the fixed square. Changes of lattice
spacing, coarse operator identification, physical clock and interacting
volume-uniformity are additional operations. The present estimate does
not identify them with a change of the coupling parameter.
