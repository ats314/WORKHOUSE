# Complete first-order cancellation on every finite open strip

The actual three-plaquette strip has nonzero electric and true source
first jets. Their complete transported sum nevertheless annihilates
every physical state. The operator identity extends to every finite
open strip length by an exact index calculation.

For n based plaquette vectors, put D_ij=grad_i cross grad_j and
G=sum_j X_j cross grad_j. The actual original-edge electric first jet is

\[
H_1=\frac12\sum_{i=0}^{n-2}(X_i+X_{i+1})\cdot D_{i,i+1}
+\sum_{i<j}X_j\cdot D_{ij}.
\]

The source-compatible, divergence-free complete coordinate generator is

\[
K_n=-\frac12\sum_{i<j}(X_i\times X_j)\cdot\nabla_i.
\]

It preserves every radius. Its first ground action matches the exact
cubic quantum ground correction, and its action on the literal outer
observation matches that observation's first jet. The true first
marginal correction is zero. Including the magnetic commutator gives

\[
\boxed{H_1+[H_0,K_n]
=-\left(\sum_{i=0}^{n-1}\nabla_i+\frac12\nabla_{n-1}\right)
\cdot G=0\quad\text{on physical states}.}
\]

Therefore the complete first force and first fast defect vanish on this
family. For n=3 the reference retained source is nonreducing, but the
identity holds on its full Gaussian graph image as well. `graph.md`
derives that graph explicitly, including its all-chaos resolvent formula.

The analytic all-n index proof is in `geometry.md`; the matching true
ground and source proof is in `source.md`. The executable controls cover
the original-edge differentiation, exact n=3 coefficients, general-n
identity on additional finite lengths and the nonreducing graph. The
general theorem follows from the index proof, not an extrapolation of
those finite examples.

This result directs the next nonzero first-order calculation to the
actual 2x2 square. That calculation, including its nonzero complete force
and sharp all-source inverse-energy bound, is recorded in
`../w6_square_block_20260909/SQUARE_BLOCK_RESULT.md`.
