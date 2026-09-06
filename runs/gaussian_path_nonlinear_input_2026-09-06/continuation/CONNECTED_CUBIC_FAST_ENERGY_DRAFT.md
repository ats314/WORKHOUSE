# Pending connected Lie-cubic calculation

6 September 2026. Outputs-only draft preserved when publication was
prioritized. The formulas below have been derived but this continuation
has not received its complete independent finite controls or final audit.
It is not a registered result and is not part of the completed package.

## Inputs and conditional moment

The current graph already contains the literal Gaussian source and local
covariant path results. The newly reviewed covariance source is
`../next_gaussian_fast_covariance/CONDITIONAL_QUANTUM_PATH_COVARIANCE.md`.
Its C_fast is twice the probability covariance. Set sigma=C_fast/2.
At fixed L its spatial block kernel is summable uniformly in torus volume
and bounded rho/v, with constants depending on L. The root first-jet note
`../next_cubic_ground_transfer/CUBIC_GROUND_TRANSFER_DRAFT.md` establishes
the alternating color structure of the actual first Wilson ground forcing.

Let D_ijk and E_lrs be real alternating spatial tensors, summing over all
ordered triples, and f_abc an orthonormal compact-simple Lie tensor with
sum_bc f_abc f_dbc=C_A delta_ad. Let d=dim Lie(G). For a color-diagonal
Gaussian Z of probability covariance delta_ab sigma_ij and retained mean
m_i in Lie(G), write

```text
P_D(x)=sum_ijk,abc D_ijk f_abc x_i^a x_j^b x_k^c,
F_D=P_D(m+Z)-P_D(m).
```

Every internal contraction repeats two colors of f and vanishes. Thus
F_D has exactly the following mutually orthogonal conditional Wick degrees:

```text
degree 1: 3 sum_ijk D_ijk <[m_i,m_j],Z_k>,
degree 2: 3 sum_ijk,abc D_ijk f_abc m_i^a :Z_j^b Z_k^c:,
degree 3: sum_ijk,abc D_ijk f_abc :Z_i^a Z_j^b Z_k^c:.
```

Wick pairing gives the complete candidate connected second moment

```text
E(F_D F_E)
 =9 sum_ijk,lrs D_ijk E_lrs sigma_ks
       <[m_i,m_j],[m_l,m_r]>
 +18 C_A sum_ijk,lrs D_ijk E_lrs sigma_jr sigma_ks <m_i,m_l>
 +6 C_A d sum_ijk,lrs D_ijk E_lrs sigma_il sigma_jr sigma_ks.
```

The factors are respectively 3^2, 3^2 2!, and 3!. The middle color
contraction is C_A delta; the last is sum f^2=C_A d. No Gaussian
independence of distinct spatial sites is assumed.

## Proposed rooted estimate

For local vertices D_v define

```text
a_v=sum_ijk |D_v,ijk|,
a_star=sup_k sum_v,ij |D_v,ijk|,
S=sup_i sum_j |sigma_ij|,
sigma_star=sup_ij |sigma_ij|,
beta_G=sup_(|x|=|y|=1) |[x,y]| <=sqrt(C_A).
```

For |m_i|<=M on the two supports in a covariance, the preceding expression
and one summable cross-propagator give

```text
sum_w |E(F_Dv F_Dw)|
 <=a_v a_star S [9 beta_G^2 M^4
                   +18 C_A M^2 sigma_star
                   +6 C_A d sigma_star^2].
```

One bounds all other propagators by sigma_star, then sums the remaining
cross propagator against the pointed coefficient incidence a_star. This
is independent of the number of vertices when the local coefficient norms
are uniform. The probability covariance convention supplies the factor
one half in S and sigma_star. Converting the predecessor block operator
row norm to individual spatial-component row sums costs at most
sqrt(3L^3), not a color dimension factor. Color factors are already explicit.

Local retained cutoffs chi_v(y), vanishing unless |m_i(y)|<=M on the
vertex support, preserve conditional centering. The same pointwise Schur
matrix bound applies to arbitrary superpositions sum_v c_v(y)chi_v F_Dv.
If A=sup_v a_v and the bracketed rooted constant is kappa, this proposes
an L2 synthesis bound by kappa sum_v ||c_v||^2, without an any-bad-site
probability or a total-volume factor in the operator norm.

## Energy scope and unresolved step

For the exact literal P and Q=I-P, these centered forces lie in Q. An
established whole Gaussian inequality h0>=cQ gives F0=Qh0Q>=c on Q, hence

```text
<B c,F0^(-1)B c> <= (kappa/c) sum_v ||c_v||^2.
```

This bounds a selected second-order fast exchange contribution. It does
not identify an equal-time covariance with the actual time-integrated
resolvent kernel, and an operator bound on that kernel does not imply
an absolute rooted row bound. That stronger locality requires a dynamic
or resolvent kernel argument. For a nonreducing Gaussian source the
baseline Qh0P is already nonzero: the full second derivative of a static
Schur map also contains changes in its fast operator and baseline cross
term. Endpoint coefficients similarly involve time ordering. Neither is
computed by the equal-time moment alone.

Actual local magnetic cubic coefficients fit the stated local tensor
input. Locality of all ground-forcing or resolvent-corrector spatial
coefficients cannot be inferred merely from their exterior-three-form
color structure. Their norms and the other order-two Wilson, metric,
Haar and moving-source contributions remain to be controlled. There is
no all-orders convergence or continuum conclusion here.
