# Moving-time spectral exclusion with approximate sources

11 September 2026. New graph-guided derivation in this task, built from the
project's positive spectral inequality R1 and small-exponential source limit
SCB9. The general result is an analytic theorem; its finite exact controls
are separately registered. This is a new connection relative to the reviewed
sources, not a claim of worldwide mathematical priority.

The contribution is a sharp sufficient interface for the continuum spectral
gap: one observation time tending to infinity per cutoff, approximate source
vectors, and vague convergence of their intended spectral measures suffice.
Uniform estimates at all late times for each cutoff, quantitative convergence
at the moving times, and a uniform small-source radius are not prerequisites
of this implication. The actual Wilson estimates and continuum realization
remain application hypotheses, specified in section 6.

## 1. Premises and the finite-cutoff projection estimate (MT1)

For each n let H_n be a nonnegative self-adjoint operator on a Hilbert space
Hcal_n, and let f_n and v_n be vectors in that SAME space. Their norms and
operators may vary with n. Set

    d_n = ||f_n-v_n||,
    nu_n(B) = ||1_B(H_n) f_n||^2,
    C_n(t) = <v_n, exp(-t H_n) v_n> >= 0.

Every t in this note is physical time for H_n. The spectral theorem and the
triangle inequality, for every E,t>=0, give

    sqrt(nu_n([0,E])) <= d_n + exp(E t/2) sqrt(C_n(t)).       (MT1)

Proof. For P=1_[0,E](H_n), positivity implies

    ||P v_n||^2 <= exp(E t) C_n(t).

Now ||P f_n||<=||P(f_n-v_n)||+||P v_n|| and ||P||<=1.
No inverse, isolated eigenvalue, source frame lower bound, or comparison
between Hcal_n and Hcal_(n+1) is used.

This ordering matters. Comparing full correlators first can introduce an
error multiplied by exp(E t). In MT1 the source-approximation error stays
outside that exponential. It only has to tend to zero, at any rate.

## 2. Moving-time exclusion and totality (MT2)

Assume d_n->0 and the positive finite measures nu_n converge vaguely to a
positive Radon measure nu on [0,infinity). Vague means convergence against
continuous compactly supported functions; total mass need not be preserved.
Suppose there are t_n->infinity and b_n>=0 such that

    C_n(t_n) <= b_n,
    exp(E t_n) b_n -> 0 for every 0<=E<M, with M>0.         (MT2a)

Then

    nu([0,M)) = 0.                                        (MT2)

Proof. MT1 implies nu_n([0,E])->0 for each E<M. If h>=0 is continuous and
compactly supported in [0,M), select E<M containing its support. Then

    0 <= integral h dnu
      = lim_n integral h dnu_n
      <= ||h||_infinity lim_n nu_n([0,E]) = 0.

Exhausting [0,M) by such functions proves MT2. This proof avoids the wrong
direction of the compact-set Portmanteau inequality: vanishing masses of
a single closed interval alone would not exclude an atom arriving at its
boundary. The slightly larger support E<M supplies the needed margin.

A convenient sufficient rate is

    liminf_n [-log(b_n)/t_n] >= M,                          (MT2b)

with -log(0)=+infinity. For any E<M choose E<E'<M. Eventually
b_n<=exp(-E' t_n), which proves MT2a. No assertion is made about an atom at M.
The theorem does not assert a uniform gap for the cutoff operators H_n.

For a physical-space consequence, suppose the limiting measures are the
ACTUAL spectral measures nu_f(B)=||1_B(H)f||^2 of one reconstructed H>=0,
for a family whose span is dense in Omega-perp. Apply MT2 separately to
each member, allowing its own t_n, approximate probes, and prefactors, with
one common M>0. The bounded projection 1_[0,E](H) kills the dense family
and hence Omega-perp. Thus

    H restricted to Omega-perp >= M,                       (MT2c)

and no additional zero-energy state remains there. This does not construct
H, establish density, ensure nontriviality, or choose a unique continuum
subsequence. It applies to every subsequential continuum object satisfying
the hypotheses. Nonzero finite-energy source weight is a separate input.

## 3. Shrinking exponential sources without a Taylor rate penalty (MT3)

On each probability space let F_n be real with ||F_n||_infinity<=B, where B
may depend on the observable but is uniform in n. Assume the spectral
identification uses its L2 norm, or an isometric identification into Hcal_n.
For nonzero real alpha_n->0 put

    f_n = F_n-E_n F_n,
    s_n = exp(alpha_n F_n)-E_n exp(alpha_n F_n),
    v_n = s_n/alpha_n,
    K_n(t) = <s_n, exp(-t H_n) s_n>.

The graph's SCB9 gives

    d_n <= |alpha_n| B^2 exp(|alpha_n| B) -> 0,
    C_n(t) = K_n(t)/alpha_n^2.                              (MT3a)

Consequently the finite-cutoff certificate is

    sqrt(nu_n([0,E]))
      <= |alpha_n| B^2 exp(|alpha_n|B)
         + exp(E t/2) sqrt(K_n(t))/|alpha_n|.               (MT3)

Only the normalized correlation K_n/alpha_n^2 enters the moving-time rate.
There is no requirement exp(E t_n)|alpha_n|->0. In particular alpha_n may
converge arbitrarily slowly if the normalized correlation satisfies MT2a.
If observable bounds B_n grow, replace B by B_n and explicitly require
|alpha_n| B_n^2 exp(|alpha_n| B_n)->0; boundedness is not silently retained.

The precise novelty relative to SCB5 is the joint limit: both the cutoff
and the exponential tilt now change while only one late observation is
available at each cutoff. SCB5 treats arbitrarily late times for each
fixed source on an already identified object. MT1 allows approximate probes
to be compared at the spectral-projection level before taking these limits.

## 4. Optimal power-law budget and finite observation horizon (MT4)

Let 0<a_n<1 tend to zero and L_n=log(1/a_n). Assume p>=0, r>0, m>0,
s>=0, and positive constants c_alpha,A,B independent of n. Suppose

    |alpha_n| >= c_alpha a_n^s,
    K_n(t) <= A a_n^(-p) exp(-m t) + B a_n^r               (MT4a)

at the selected physical times t_n=c L_n. If a horizon is imposed, require
0<c<=c_max and availability at the selected time; proving the bound over
the whole horizon is sufficient but stronger than needed. Also assume the
source approximation and vague spectral limit of sections 2-3. Then

    exp(E t_n) K_n(t_n)/alpha_n^2
      <= c_alpha^(-2) [A a_n^[c(m-E)-p-2s]
                       + B a_n^[r-2s-cE]].                (MT4b)

Thus every energy strictly below

    M(c) = min(m-(p+2s)/c, (r-2s)/c)                       (MT4c)

is excluded in the limiting measure, when M(c)>0. For r>2s and p+2s>0,
the first branch increases and the second decreases. Their unique crossing
and the unrestricted optimum are

    c_* = (p+r)/m,
    M_* = m(r-2s)/(p+r).                                  (MT4d)

With a finite available horizon,

    c_opt = min(c_max,c_*),
    M_opt = min(m-(p+2s)/c_opt, (r-2s)/c_opt).              (MT4e)

A positive certificate exists exactly when r>2s and
c_max>(p+2s)/m (omit the horizon condition if unrestricted).
In the boundary case p=s=0, M(c)=min(m,r/c); any
0<c<=min(c_max,r/m) gives the same optimum m. If r<=2s no
positive gap follows from this budget alone. Constants A,B,c_alpha do not
affect the exponential rate. The raw error must survive division by the
source amplitude squared; an unnormalized decay rate is not a gap bound.

Example: p=1, r=5, s=1, m=2 gives c_*=3 and M_*=1. With
c_max=2 the best guaranteed rate is 1/2. The retained positive-energy
interval is [M_opt,infinity); an atom exactly at M_opt is allowed.

If s=0, the lower bound on alpha_n precludes alpha_n->0. MT4 still applies
to the general approximate probes of MT1 (including exact probes).
For shrinking tilts whose inverse is sub-polynomial in 1/a_n, apply MT4
for every arbitrarily small positive s and take the supremum of the
resulting excluded intervals. This recovers m r/(p+r) without imposing
a nonzero limiting tilt. Do not assert a constant lower bound for a
sequence already assumed to tend to zero.

## 5. Sharpness and falsifiers (MT5)

The rate loss in MT4 is unavoidable from those hypotheses alone. Let
theta=(r-2s)/(p+r) in (0,1), M_*=m theta, and choose one
unit target vector of energy M_* with probe alpha_n times that vector,
alpha_n=a_n^s. Its raw correlator is a_n^(2s) exp(-M_* t).
For X=a_n^(-p)exp(-m t) and Y=a_n^r, the exact identity is

    X^theta Y^(1-theta) = a_n^(2s) exp(-M_* t).

Weighted arithmetic-geometric mean gives X^theta Y^(1-theta)<=X+Y.
So MT4a holds for ALL t>=0 with A=B=1, while the limiting measure is
delta_(M_*). No larger universal gap can follow from this same data.
When p=s=0, the atom at m supplies the endpoint example directly.

For c_max<c_* and M_opt>0, an atom at
M_opt=m-(p+2s)/c_max obeys

    a_n^(2s) exp(-M_opt t) <= a_n^(-p) exp(-m t)
    for 0<=t<=c_max L_n.

This proves sharpness of the shortened-horizon rate as well. These abstract
one-mode probes already belong to the general MT1 class. For actual
exponentials, take a symmetric two-point probability space with F=+/-1
and H having energy M on its centered line. Then s_alpha=sinh(alpha)F,
and |sinh(alpha)/alpha|<=sinh(1) for 0<alpha<=1. Multiplying A and B
by the fixed constant sinh(1)^2 gives the same sharp exponents for s>0.

Further exact or explicit negative controls:

1. Source amplitude: H=0, a unit f=v, and raw probe s_n=alpha_n f with
   alpha_n=exp(-sigma t_n) give K_n=exp(-2sigma t_n). The raw apparent
   rate 2sigma is positive, but K_n/alpha_n^2=1 and the actual energy is 0.
   The symmetric two-point exponential realizes the same asymptotic example.
2. An inadequate plateau: if r<=2s, the same zero-energy probe with
   alpha_n=a_n^s obeys K_n=a_n^(2s)<=a_n^r. A positive universal gap is
   impossible. An endpoint r=2s is not a strict margin.
3. Missing totality: H=diag(0,1/4,2), vacuum e1, and source e3 have an
   exact rate 2 while the full vacuum-complement gap is 1/4.
4. Fixed times: for t_n=1 and H=epsilon, the estimate
   C(1)<=exp(m-epsilon) exp(-m) holds for any m>epsilon. Its fixed
   prefactor contains no asymptotic rate information.
5. Wrong clock: one-step T_n=exp(-1) and physical step length tau_n=n
   give H_n=1/n. At k_n=n steps the correlator is exp(-n), but physical
   time is n^2 and the physical exponential rate tends to zero.
6. No cutoff gap is implied: nu_n=exp(-2t_n)delta_0+delta_1 converges
   vaguely to delta_1 and satisfies C_n(t_n)<=2exp(-t_n), while every
   cutoff measure still has a zero-energy atom.
7. No nontriviality is implied: nu_n=delta_n has a zero vague limit. Its
   excellent decay cannot establish a nonzero continuum field.
8. No uniform Taylor rate is necessary: in the two-point model with energy
   2, take alpha_n=1/n and t_n=n. MT3 tends to zero below energy 2,
   while exp(E n)/n diverges for every E>0. Comparing projected vectors
   avoids that artificial obstruction.

## 6. Graph consequence and remaining Wilson obligation

Established inputs reviewed here:

- [Reconstruction R1 and plateau R4-R5](yangmills-reconstruction.md): positive
  spectral domination and the exact fixed-object localization-error budget.
- [SCB5 / SCB9](source-currents-and-spectral-totality.md): the true bounded
  exponential-source tangent and totality consequence.
- The preserved [matrix carrier measure theorem](../../notes/imported/WORK_SINCE_2026-08/WORKHOUSE_MATRIX_KL_CARRIER_ATOM_THEOREM_2026-08-22.md),
  sections 3.1-3.4: vague convergence versus UV escape and source weight.

The support argument here follows directly from the definition of vague
convergence; it is not a new spectral theorem or a new Portmanteau theorem.
The contribution is MT1-MT4 together: approximate probes, a moving cutoff
time, a shrinking source window, and an optimal physical-rate budget.
Exact controls and the finite counterexamples are in
`src/workhouse/invariants/moving_time_gap.py`. The measure-limit proof and
physical totality argument remain analytic with no whole-statement Lean
certificate.

For G19, a sufficient open successor is now concrete: on an actual continuum
trajectory, produce the intended nontrivial reconstructed positive spectral
measures and a total family of approximated centered sources, prove their
vague convergence, and prove the normalized one-time estimate MT2a with
a common positive PHYSICAL rate. The power-law realization needs MT4a,
an admissible source exponent s, r>2s, and a long enough physical horizon.

Hypothesis discharged: all-late-time cutoff control and a quantitative
moving-time convergence estimate are unnecessary for this spectral
implication. Downstream theorem: MT2c then applies to any actual continuum
object meeting the remaining assumptions. Remaining blocker: the Wilson
trajectory estimates and continuum spectral/source identification above.
This does not remove the separate existence, Euclidean invariance,
nontriviality, interacting W6, or normalized cross-scale obligations, and
does not alter the established fixed-spacing G18 results.
