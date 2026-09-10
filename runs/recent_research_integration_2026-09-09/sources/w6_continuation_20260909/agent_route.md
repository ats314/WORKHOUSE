# Selected inverse continuation: residual certificate and one-sided exclusion

9 September 2026. Independent analytic note for the W6 continuation. The
definitions and normalizations are those in
`ALL THEORY/WORKHOUSE/docs/derivations/wilson-selected-inverse-wall.md`.
This note does not prove the interacting Wilson estimate. It derives a
conditional certificate, checks a finite counterexample, and excludes one
additional proposed global Gaussian comparison.

## 1. An exact residual identity that removes the interacting inverse vector

Write `A_0=F_0-z`, `A_g=F_g-z`, with positive closed forms, and let
`u=A_0^{-1}t`. Require that `u` belongs to the interacting form domain.
The residual is the functional

    rho[q] = a_g[q,u] - <q,t>.

It must extend continuously to the interacting energy space. These domain
conditions are real hypotheses when the Gaussian and compact realizations
have different form domains. The expression `rho=(A_g-A_0)u` is shorthand
valid on their admissible common core.

Let `v=A_g^{-1}t` and `w=A_g^{-1}rho=u-v`. Completion of the positive
quadratic form gives the exact identity

    <t,(A_g^{-1}-A_0^{-1})t>
      = -d_g[u,u] + ||rho||_{A_g^{-1}}^2,                         (R1)

where `d_g=a_g-a_0` on the chosen graph vectors. One proof starts from

    <t,A_g^{-1}t>
      = 2 Re<t,u> - a_g[u] + a_g[u-v]

and uses `<t,u>=a_0[u]`. Equivalently, `rho` is the Riesz representative
of `u-v` in the `a_g` energy inner product. This proves (R1) for forms,
including a residual in the form dual rather than in the Hilbert space.

Suppose an independently specified positive comparison form `ell` obeys

    a_g >= kappa ell,                 kappa>0,
    |d_g[u_p,u_p]| <= a |g| b[p],
    ||rho_p||_{ell^*} <= c sqrt(|g|) sqrt(b[p]),
    u_p=A_0^{-1}t_1 p.                                            (R2)

Here `ell^*` means the energy-dual norm, conventionally denoted
`L^{-1/2}` when `ell[q]=||L^{1/2}q||^2`. The first inequality gives

    ||rho_p||_{A_g^{-1}}^2 <= kappa^{-1}||rho_p||_{ell^*}^2.

Thus (R1) implies the W6 selected inverse estimate with constant
`a+c^2/kappa`, uniformly wherever the hypotheses are uniform. If the
residual is bounded by `c |g| sqrt(b[p])`, its contribution improves to
`c^2 g^2/kappa`. The constant coercivity fraction `kappa` need not tend to
one. It is essential that `L` and its coercivity are supplied independently;
choosing `L=A_g` does not resolve the interacting estimate.

The exact missing Wilson input is therefore a connected, volume-uniform
bound on the residual of the Gaussian selected solution in an independently
controlled local energy dual, together with its diagonal defect and
coercivity. A naive residual in undressed product coordinates can accumulate
spectator vacuum terms. The interacting ground/source identification must
remove or estimate those terms before taking a norm. Nothing in (R1)
establishes that cancellation for coupled Wilson fields.

## 2. Gaussian selected data and a uniform floor do not supply the residual

For `M>0`, let

    A_0=I_2,    t=e_1,
    c_M(g)=M g^2/[2(1+M g^2)],
    A_g=[[1,c_M(g)],[c_M(g),1]].

Then `A_g >= (1/2)I_2`, `u=e_1`, and `d_g[u,u]=0` for every `M,g`.
Each fixed-M family is analytic near zero and its selected Gaussian inverse
energy is one. But

    <e_1,(A_g^{-1}-I)e_1> = c_M(g)^2/[1-c_M(g)^2].

At `M=n^2`, `g=1/n`, the coupling is `c_M(g)=1/4`, the selected inverse
excess is `1/15`, and its ratio to `g` is `n/15`. No uniform O(g) estimate
follows from the floor and Gaussian diagonal data. The missing residual is
explicitly `rho=c_M(g)e_2`; its norm does not vanish on that sequence.
This is an exact logical counterexample, not a Wilson counterexample.

## 3. Even a near-unit global lower Gaussian comparison fails on the SU(2) cell

The high-representation argument in W2-W3 rules out an upper Gaussian form
bound. One might instead try the lower bound

    F_g >= (1-Cg) U_g F_0 U_g^*,                                 (R3)

with a volume-independent constant and a unitary identification. For the
four-link SU(2) cell, (R3) also fails if the retained rank is fixed, or more
generally is `o(g^{-2})`. Its failure is at representations of order
`g^{-2}`. This statement does not exclude a fixed smaller coercivity
fraction `F_g>=kappa U_g F_0 U_g^*`, as used conditionally in (R2).

### Exact radial normalization

On class functions set `r in (0,2pi)`. The Haar radial measure is a constant
multiple of `sin^2(r/2) dr` and

    Delta = partial_r^2 + cot(r/2) partial_r.

Multiplication by `sin(r/2)` takes the physical radial realization to
Lebesgue measure, with Dirichlet endpoints. Direct differentiation gives

    sin(r/2) Delta [v/sin(r/2)] = v''+v/4.

Consequently the exact four-link scaled Wilson operator is unitarily
equivalent to

    H_g = -2g^2 partial_r^2 + 4g^{-2}(1-cos(r/2)) - g^2/2

on `(0,2pi)` with Dirichlet boundary conditions. At zero magnetic potential,
`sin((n+1)r/2)` has electric eigenvalue
`g^2((n+1)^2-1)/2=g^2 n(n+2)/2`, confirming W2's normalization.

Put `h=g^2` and

    K_h=h H_g=-2h^2 partial_r^2+V(r)-h^2/2,
    V(r)=4(1-cos(r/2)).

If `e_g` is the true vacuum energy of `H_g`, then `h e_g -> 0`.
Indeed `H_g>=0` in its original realization. A normalized test function
`v_h(r)=h^{-1/4} phi(r/sqrt(h))`, for fixed smooth compactly supported
`phi` in `(0,infinity)`, has `K_h` energy O(h), because
`V(r)<=r^2/2`. Thus `0<=h e_g<=C_phi h` for small h. This argument needs
no assumption about interacting volume-uniform vacuum asymptotics.

### Elementary counting proof

Let `N_h(E)` count the eigenvalues of `K_h` at most E. For every fixed `E>0`,

    lim_(h->0) h N_h(E)
      = (1/(pi sqrt(2))) int_0^(2pi) sqrt((E-V(r))_+) dr.           (R4)

To prove (R4), partition the interval into a fixed finite number of pieces.
Dirichlet and Neumann bracketing bound the count between sums for independent
intervals with potentials equal to their respective maxima and minima.
On an interval of length ell and constant potential v, either endpoint
condition has count

    ell/(pi h sqrt(2)) sqrt((E-v)_+) + O(1).

The additional scalar `-h^2/2` tends to zero and does not affect the limit.
First take `h->0` with the partition fixed, so the finitely many O(1)
errors disappear after multiplication by h. Then refine the partition.
The upper and lower Riemann sums converge to the same continuous integral.
This is a proof by bracketing, not an invocation of an unverified
semiclassical expansion. The limit is continuous in E, so the same formula
holds after vacuum subtraction, since `h e_g->0`.

At `E=8` the integral is elementary:

    sqrt(8-V(r))=2 sqrt(2) cos(r/4),
    int_0^(2pi) sqrt(8-V(r)) dr=8 sqrt(2),
    lim_(g->0) g^2 N_(H_g-e_g)(8/g^2)=8/pi.                      (R5)

The vacuum-subtracted Gaussian radial oscillator has eigenvalues `4n`,
`n=0,1,...`, so its corresponding limit is `8/4=2`.

For an admissible fast compression of codimension `r`, min-max interlacing
changes any counting function by at most r. Therefore both limits persist
under fixed finite rank retention, and under any retention satisfying
`g^2 r(g)->0`. They also persist under a bounded common spectral shift z.

If (R3) held, min-max comparison would imply

    N_(F_g)(8/g^2)
      <= N_(F_0)(8/[(1-Cg)g^2]).

Multiplying by `g^2` and taking the limit would give `8/pi<=2`, a
contradiction since `pi<4`. Hence (R3) is impossible in this regime,
independently of the unitary identification. In fact any global lower
comparison fractions `kappa_g` have `limsup_(g->0) kappa_g<=pi/4` under
these retention assumptions. This last bound follows from the same count
at E=8; it is only an upper restriction on admissible fractions, not a
proof that `pi/4` or any other positive fraction is attainable.

If the retained rank is of order `g^{-2}` or larger, the counting argument
no longer establishes this obstruction. No assertion is made about that
different retention scheme or about infinite-rank retained algebras.

## 4. Scope and next calculation

(R1)-(R2) are exact conditional analytic statements. The two-by-two
counterexample is exact arithmetic. The SU(2) result (R3)-(R5) is an analytic
all-mode exclusion with an elementary bracketing proof; no claim is made
that an existing Lean theorem formalizes its quantifiers.

A productive next Wilson calculation is to express `rho_p` after the
actual vacuum/source transport as a sum of terms rooted at the source,
prove a volume-independent synthesis bound in `ell^*`, and prove
`a_g>=kappa ell` with a fixed positive fraction. The root must survive
vacuum subtraction and source normalization. The already established
Gaussian synthesis bound does not prove any of these interacting facts.
Without that additional input, W6 and the continuum expectation limit
remain unproved on this route.
