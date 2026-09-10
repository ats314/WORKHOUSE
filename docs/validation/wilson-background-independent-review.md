# Independent review of the charged resolvent / finite-time derivative lemma

Reviewed 2026-09-09 against `C:/WORKHOUSE/tmp/signed-covariance-agent.md`. No shared repository edits. Result: the displayed all-coupling first/mixed-derivative bounds follow with the stated unit-S3 SU(2) normalization and geometry qualifications. This is analytical review, not Lean certification.

## Explicit Markov realization

At a cubic vertex x, write its six signed incident link generators as Z_i^a (outgoing left multiplication and incoming minus right multiplication), and G_x^a=sum_i Z_i^a. Then exactly

    Delta_star - (1/6) sum_a (G_x^a)^2
      = (1/6) sum_a sum_(i<j) (Z_i^a-Z_j^a)^2.

All vector fields are smooth. Add the outside-link Laplacian and the smooth drift `2 grad log Z_t . grad`. The negative of `K_t-epsilon C_x/6` is therefore a smooth sum-of-squares diffusion generator with no killing term on the compact finite lattice. This establishes its Markov evolution without assuming regularity of an abstract square root of a semidefinite matrix. At each finite time, Z_t is positive and smooth. The parabolic problem on each bounded time interval is standard, with compact state space and smooth time-dependent coefficients.

For distinct stars that overlap, the residual after subtracting `epsilon(C_x+C_y)/12` is half the sum of the two individual residual generators, hence is again a smooth diffusion. For disjoint stars, subtract both Casimirs with coefficient epsilon/6 directly.

The adjoint infinitesimal matrices with the unit-S3 basis are `J_a v=2 e_a cross v`, satisfying `-sum_a J_a^2=8 I`. A tail derivative of a gauge-invariant scalar is adjoint covariant at that tail and invariant at all other vertices. For different tails, its mixed derivatives are in `adjoint_x tensor adjoint_y`; the sum Casimir is 16. The scalar Markov evolution acts componentwise on Euclidean vectors/tensors, so Jensen gives contraction in their Euclidean/Hilbert-Schmidt supremum norm. It follows that charged damping is 4epsilon/3 for one charge or two arbitrary distinct charges, and 8epsilon/3 for two disjoint stars.

## Direct finite-time equations and constants

With Z_t=exp(-tH)1, p_e=X_e Z_t/Z_t and q_ef=X_e X_f Z_t/Z_t (different edges), the link Killing derivatives commute with Delta, and derivatives on different links commute. Direct differentiation gives exactly

    (partial_t+K_t)p_e = -V_e,
    (partial_t+K_t)q_ef = -V_ef-p_e tensor V_f-V_e tensor p_f.

Initial values are zero. The four plaquettes through a link each have gradient norm at most one, hence `||V_e||_infinity <=4k`. Charged damping gives

    ||p_e(t)||_infinity <=3 lambda (1-exp(-4epsilon*t/3)) <=3lambda.

For two distinct tails, the tensor source is bounded by `||V_ef||+24k^2/epsilon`, so

    ||q_ef|| <=3||V_ef||/(4epsilon)+18lambda^2.

Since `H_ef=X_e X_f log Z_t=q_ef-p_e tensor p_f`,

    ||H_ef|| <=3||V_ef||/(4epsilon)+27lambda^2.

For disjoint stars the improved result is

    ||H_ef|| <=3||V_ef||/(8epsilon)+18lambda^2.

Thus the claimed pure `18lambda^2` bound requires additionally `V_ef=0`, equivalently here no plaquette containing both links. All estimates are uniform in t, finite volume, and configurations. The fixed-finite-volume smooth ground limit then passes them to log Omega. No uniform ground-convergence assumption or physical-sector gap has been inserted.

## Geometric qualification

Disjoint stars alone do not imply V_ef=0. In a positive plaquette, the east link starting at (0,1) and the north link starting at (1,0) share head (1,1) and the plaquette. Their tails are nonadjacent, and their incident link stars are disjoint. The improvement by two in the resolvent bound applies, but the V_ef term remains. Sufficiently distant blocks satisfy both conditions.

## Useful extension

For any selected vertex set S, let n_e in {0,1,2} count selected endpoints of link e. Then

    Delta - (1/12)sum_(x in S)sum_a (G_x^a)^2
      = sum_e (1-n_e/2)Delta_e
        + (1/12)sum_(x in S)sum_a sum_(i<j)(Z_i^a-Z_j^a)^2.

This proves a Markov residual for arbitrary S. A tensor with one adjoint charge at each of n distinct vertices has damping `(2epsilon/3)n`. If S is an independent vertex set, coefficient1/6 is available and damping doubles. These are charged-sector facts; a same-vertex adjoint tensor product can contain singlets, and physical gauge-invariant states have Casimir zero.

## Exact remaining bound

For sufficiently separated links, write R_xy for the actual charged inverse. The remaining connected expression is

    H_ef = -R_xy(p_e tensor V_f+V_e tensor p_f)-p_e tensor p_f.

The new argument controls its supremum uniformly in time and volume but does not produce dependence on the distance between e and f. Separate norms yield a constant18lambda^2; a row sum over arbitrarily many blocks still grows with volume. The needed next proof is spatial decay of this precise connected combination, not invertibility of its charged resolvent. The latter is now established under the stated finite-lattice conventions.

