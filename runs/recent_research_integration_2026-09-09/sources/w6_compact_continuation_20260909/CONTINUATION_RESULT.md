# Next W6 steps: compact interacting residual and coupled Gaussian floor

The continuation now goes beyond the first square-block coefficients.
It establishes a complete finite-coupling comparison at positive compact
references, a size-independent Gaussian fast floor on shared-edge grids,
and actual quantum ground remainder estimates at small coupling.

## Complete finite-coupling residual at a positive compact reference

For the actual square, let s>0 be a reference coupling and t a nearby
positive coupling. A fully specified source-range and vacuum transport
preserves the physical H1 form domain and is norm smooth there. It
retains the exact nonreducing graph J_s. The actual derivative constants
M1,M2,M3 are constructed from the compact Wilson forms and true quantum
ground/projection derivatives.

Writing Delta=t-s and epsilon=M1|Delta|<1, the complete selected residual
rho_(s,t)=Q(l_t-l_s)G_s t_s satisfies

\[
\boxed{\langle\rho_{s,t}p,G_t\rho_{s,t}p\rangle
\le\frac{\beta M_1^2\epsilon^2}{1-\epsilon}\,b_s[p],}
\]
\[
\boxed{|(l_t-l_s)[G_st_sp,G_tt_sp]|
\le\frac{\beta M_1^3|t-s|}{1-\epsilon}\,b_s[p].}
\]

These bounds cover every actual retained finite-energy source. The
operator difference is the full finite difference, not its first jet.
The same proof establishes a cubic Schur remainder and comparison of
the actual source energies. Details and constants: `compact_residual.md`.
The reference and source chart differ from the Gaussian zero-coupling
reference; their identification is not assumed.

## Shared-edge grid floor without a reduction assumption

For every open 2m by 2n planar face rectangle, retaining each 2x2 block's
full summed flux vector and then imposing physical invariance, the
actual tangent electric matrix is C=4I-Adjacency. Let E be the blockwise
constant subspace. The exact edge decomposition gives

\[
2Q_E\le C\le8I.
\]

The Gaussian retained one-particle directions are R=C^(1/4)E, not E.
A positive-form transfer lemma and second quantization give

\[
\boxed{F_{0,\Lambda}\ge\frac1{\sqrt2}I,\qquad
\|F_{0,\Lambda}^{-1}\|\le\sqrt2.}
\]

This includes shared edges, all oscillator levels, the generally
nonreducing source, and physical invariants. The constants are independent
of m,n. Details: `grid_gaussian_floor.md`. The result is Gaussian;
the actual finite-g uniform-volume transfer remains to be proved.

## Actual quantum ground estimates toward zero coupling

The exact original-edge identities
\(\Delta_E V=48-3V\) and \(\sum|EV|^2\le16V\) give quantum ground
moment bounds and exponential concentration, including

\[
\mathbb E_{\mu_g}\exp(V/(2g^2))\le2e^{2E}
\quad\text{when }e_g\le E.
\]

An explicit compact dilation D preserves the entire outer-trace source
algebra. The actual differentiated ground equation and weighted elliptic
estimates prove

\[
\boxed{\|\partial_g\Psi_g+D\Psi_g/g\|
+\|(H_g-e_g)^{1/2}(\partial_g\Psi_g+D\Psi_g/g)\|\le C.}
\]

This removes the singular dilation of the true ground, rather than
assuming a differentiated Gaussian expansion. See `quantile_scale.md`.
Independently, the explicit first-corrected Gaussian quasimode v_g obeys

\[
\boxed{\|\Psi_g-v_g\|
+\|(H_g-e_g)^{1/2}(\Psi_g-v_g)\|=O(g^2),
\qquad |e_g-e_0|=O(g^2).}
\]

The original operator Taylor remainder and the actual physical gap prove
this estimate in `ground_first_jet_remainder.md`.

## Precise next uniform estimate

The positive-reference theorem's constants are finite and explicit in
actual conditional quantum scores. After removing dilation, the averaged
conditional score variance is uniformly bounded. Controlling its action
on arbitrary retained sources, with the correct source energy weight,
is stronger than that average and weaker than demanding an unweighted
essential supremum. The proved criterion in `quantile_source_weight.md`
is

\[
\int K_g|f-\nu_g f|^2d\nu_g
\le\left(8B_g+\frac{4\overline K_g}{\gamma}\right)b_g[f],
\]

where K_g is the actual conditional variance of the ground score after
subtracting dilation, overline(K_g) is its already bounded average, and
B_g is an explicit variance tail times a coarse resistance integral.
The uniform bound on B_g is not yet proved. This criterion avoids an
unnecessary uniform essential-supremum requirement; the example K(a)=a
has unbounded supremum but a proved all-source energy bound.

The remaining quantitative transfer is an all-source, small-coupling
bound for these complete transported residuals and their derivative
constants, together with the actual interacting analogue of the grid
floor. `positive_reference_budget.md` states how derivative scaling would
enter an accumulated error budget while keeping source-energy growth.

The supporting scripts check exact finite algebra. The operator-domain,
all-energy, localization and parameter-uniformity arguments are analytic
proofs and are not claimed as new Lean formalizations.

The three executable checks were run together and passed: 50 compact
finite-step controls, 50 coupled-grid controls, and 15 quantum transport
controls. `provenance.json` pins their records and all supporting files.
