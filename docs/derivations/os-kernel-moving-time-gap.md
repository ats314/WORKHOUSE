# A kernel criterion for the G19 moving-time route

11 September 2026. Analytic theorem and G19 closure attempt. This is a
continuation of the moving-time theorem, not a declaration that G19 is closed.
The result removes a separate spectral-measure convergence assumption and a
separate frame estimate when the full physical history space is constructed
from the same limiting kernels. It does not supply the Wilson kernel limits
or their required large-time bound on the weak-coupling trajectory.

## K1. Construct the physical semigroup from compatible limiting kernels

Let D be a complex vector space with a distinguished vector 1 and a semigroup
S_t:D->D, t>=0, satisfying S_0=I, S_(s+t)=S_s S_t, S_t 1=1.
For each cutoff n let H_n>=0 be self-adjoint on Hcal_n, let Omega_n be a unit
vacuum with H_n Omega_n=0, and let I_n:D->Hcal_n be linear with I_n 1=Omega_n.
Inner products below are conjugate-linear in the first argument. Assume:

1. For every f,g in D, q_n(f,g)=<I_n f,I_n g> tends to a finite q(f,g).
2. For every fixed f and physical time t,
   ||I_n S_t f-exp(-t H_n)I_n f|| -> 0. This permits a proved time-grid
   approximation; its defect must be checked, not hidden in a clock change.
3. For every f in D, q(f,S_t f)->q(f,f) as t decreases to zero.

Then q is a positive semidefinite Hermitian form, q(1,1)=1. On the quotient
by its null space and subsequent Hilbert completion, S_t induces a strongly
continuous self-adjoint contraction semigroup T_t=exp(-tH) with H>=0 and
vacuum Omega=[1].

Proof. Positivity and the Hermitian identity pass through every finite Gram
matrix. The fixed-time defects vanish in pairings since all fixed-vector
norms are bounded by assumption 1. Thus

    q(S_t f,S_t f)<=q(f,f),
    q(f,S_t g)=q(S_t f,g),
    q(f,S_t f)>=0.                                         (K1)

The first inequality preserves the null space. Each S_t therefore extends
to a contraction on the completion; the algebraic semigroup and symmetry
identities persist by density. Finally

    ||T_t[f]-[f]||^2 <= 2(q(f,f)-Re q(f,S_t f)) -> 0.

Contraction and density extend continuity to every vector, and the semigroup
law gives continuity at all times. The self-adjoint contraction semigroup
theorem supplies H>=0. No operator-norm convergence or common cutoff Hilbert
space is assumed. This is a Hilbert/semigroup construction, not by itself the
construction of a Euclidean-covariant local Yang--Mills field theory.

Centering is explicit: ell_n(f)=q_n(1,f), ell(f)=q(1,f),
f_n=I_n f-ell_n(f)Omega_n, and f_c=[f]-ell(f)Omega. Then

    ||f_n||^2 -> ||f_c||^2,
    <f_n,exp(-tH_n)f_n> -> <f_c,exp(-tH)f_c>               (K2)

for every fixed t. The centered classes of D have dense span in Omega-perp:
they are the image of the dense defining space under the bounded projection
I-|Omega><Omega|. This closes totality for the FULL defining history space.
A family of plaquette sources or a carrier sector cannot be substituted for
D without proving it generates that space. Nor may extra physical sectors
be adjoined without applying the criterion to their defining sources.

## K2. A single late-time bound controls every limiting fixed time

For H>=0, v in its Hilbert space and 0<t<T, the spectral theorem and Holder
give the logarithmic convexity inequality

    C_v(t)<=||v||^[2(1-t/T)] C_v(T)^(t/T),
    C_v(t)=<v,exp(-tH)v>.                                  (K3)

Indeed integrate (exp(-TE))^(t/T)*1^(1-t/T) against the positive spectral
measure and apply Holder with conjugate exponents T/t and T/(T-t).
The zero-vector case is separate and immediate.

Fix f in D. Suppose approximate centered probes v_n satisfy
||v_n-f_n||->0. Let physical T_n->infinity and b_n>=0 satisfy

    <v_n,exp(-T_n H_n)v_n> <= b_n,
    liminf_n [-log(b_n)/T_n] >= M>0.                       (K4)

Here -log(0)=+infinity. For any fixed t>0, K3 and K4 imply

    limsup_n <v_n,exp(-tH_n)v_n> <= ||f_c||^2 exp(-Mt).

To justify the endpoint, first use M-epsilon in K4, then let epsilon->0.
The norm powers converge to ||f_c||^2; if this norm is zero the bound follows
from contraction directly. The fixed-time source error is at most

    |C_(f_n)(t)-C_(v_n)(t)|
       <= ||f_n-v_n|| (||f_n||+||v_n||) -> 0.              (K5)

Combining with K2 proves the limiting estimate WITH its exact norm prefactor:

    <f_c,exp(-tH)f_c> <= ||f_c||^2 exp(-Mt), t>=0.          (K6)

For every 0<=E<M, spectral positivity now gives
||1_[0,E](H)f_c||^2<=exp(Et)<f_c,exp(-tH)f_c>->0.
If K4 holds for each member of a spanning family of D, with a common M but
source-dependent times, probes and bounds, K1 totality yields

    H on Omega-perp >= M, and ker H=span{Omega}.            (K7)

No separate vague-limit premise, quantitative fixed-time convergence rate,
uniform source frame constant or uniform choice of observation times is
needed in this kernel formulation. K1's actual kernel convergence,
time compatibility and continuity remain indispensable premises.

The shrinking-source power budget of moving-time MT4 applies to K4 with
M=m(r-2s)/(p+r) when its hypotheses hold, including r>2s. A fixed additive
plateau does not supply K4. The norm approximation still needs no rate.

## K3. Nontrivial finite-energy weight from one separated-time lower bound

Let V=||f_c||^2 and suppose a fixed physical tau>0 has
C=<f_c,exp(-tau H)f_c>>0. Then V>=C>0. Put

    R=tau^(-1) log(2V/C).

For the actual spectral measure nu of f_c,

    C <= nu([0,R])+exp(-tau R)(V-nu([0,R])).

Hence

    nu([0,R]) >= C/(2-C/V) >= C/2 > 0.                   (K8)

Under K7 the same nonzero weight lies in [M,R], and R>=M+log(2)/tau.
This establishes nontrivial finite physical energy WITHOUT requiring an
isolated atom, a uniform cutoff upper gap, or a prescribed glueball spin.
An actual positive limiting separated-time correlator is still needed.
In particular an equal-time Euclidean variance need not equal the physical
OS norm, and ultraviolet norm can disappear if K1.3 is omitted.

## K4. Falsifiers and actual Wilson application check

1. Missing continuity: take H_n=diag(0,n), I_n the identity on C^2, and
   S_0=I, S_t=diag(1,0) for t>0. K1.1 and K1.2 hold, as does arbitrarily
   fast late-time decay on the centered line. The limit kills that line
   instantly and is not strongly continuous. It has no self-adjoint
   Hamiltonian exponential realization. Thus positivity and bounded
   fixed-time kernel limits alone do not establish K1.3.
2. Missing full space: observing only the energy-2 line in
   H=diag(0,1/4,2) proves a gap on its cyclic subspace; the full centered
   space still has energy 1/4. Use the full defining D in K7.
3. Missing late-time rate: H=diag(0,1/n) has compatible fixed-time limits
   and a nonzero centered norm, but its limiting centered energy is zero.
   Fixed-time convergence and nontriviality do not imply K4.
4. Wrong clock: transfer exp(-1) with physical time step n has physical
   energy 1/n, not 1. Count the actual physical T_n in K4.

For the established SC17 thermodynamic construction, P1--P9 already give
actual fixed-time multitime kernel convergence at fixed spacing and
0<=lambda<=lambda_c, with physical gap 4epsilon/3. Its finite uniform gap
supplies K4 there. This is an application to an established regime, not a
new proof that this regime contains the spatial continuum trajectory.

The actual spatial continuum uses lambda proportional to g^(-4), which
escapes every bounded SC17 bare interval as g->0. The small-u infinite
Wilson band likewise occupies an eventually disjoint coupling interval.
The proposed continuum Cauchy proof bounds increments only by O(1/k),
which does not imply convergence. Its repaired O(1/k^2) map/source drift
requires the actual common-space normalized response estimate. The retained
unmerged D5--D6 continuation correctly preserves its coupling denominator:
for u_k=1/(alpha+beta k), |Delta u|/(4u_k u_(k+1))=beta/4.
A merely bounded covariance therefore does not give a summable increment.

Consequently this attempt closes the abstract source/semigroup passage
under K1 and K4; it does not close G19. The precise remaining inputs are:
actual continuum history-kernel convergence and fixed-time compatibility;
one positive separated-time physical source limit; a common positive
moving-time rate on the full defining history family; and the required
Euclidean/local field-theory structure. No reviewed Wilson argument here
supplies these on the weak-coupling trajectory. This is the present proof
boundary, not a claim that future closure is impossible.


## K5. Positive-time history separation supplies zero-time continuity

K1.3 need not be an independent estimate for a defining space of strictly
positive-time histories. A sufficient algebraic condition is

    D = union_(tau>0) S_tau D.                            (K9)

The ranges are nested as tau decreases, so an equivalent condition is that
their span equals D. Assume K1.1--K1.2 and K9. Fix f=S_tau g with tau>0.
At each cutoff the spectral theorem gives

    ||(exp(-tH_n)-I) exp(-tau H_n)||
      <= sup_(E>=0) exp(-tau E)(1-exp(-tE))
      <= t sup_(E>=0) E exp(-tau E) = t/(e tau).          (K10)

The compatibility defects for the fixed times tau and tau+t tend to zero.
Passing their norm identity to the limiting Gram form therefore proves

    ||[S_t f]-[f]|| <= (t/(e tau)) sqrt(q(g,g)) -> 0.     (K11)

This is obtained before constructing a limiting generator, using only the
cutoff Hamiltonians. Cauchy--Schwarz gives K1.3, and hence K1--K3 apply.
Thus the zero-time continuity needed for the physical semigroup is
discharged by positive-time divisibility and finite compatible kernels.

For the algebra of bounded cylinder histories with support in a compact
subset of the open positive-time half-space, K9 has a direct construction:
shift the finite support backward by any tau smaller than its distance
from time zero. The resulting history still belongs to the same algebra;
finite sums use the minimum available tau, and constants are fixed by all
shifts. The same support argument applies to finite sums of smeared-field
histories when that algebra and its cutoff embeddings have been defined.
This geometric argument requires the FULL physical defining history algebra.
It does not replace its kernel-convergence or cutoff-compatibility proof.

The instantaneous-loss example in K4 violates K9: its disappearing centered
direction lies in no positive-time shift range. More generally one may form
the closed span of positive-time ranges first; K10 proves strong continuity
on that part, but does not authorize calling it the whole physical space
unless the defining-history construction proves that identification.

K10 also controls a time-rounding error after a fixed positive filter. It
does not identify differently discretized source insertions or change the
physical clock. Full Euclidean distribution regularity and covariance
remain separate field-theory requirements.

## Source reading and verification scope

The starting graph is live main at 54d1ce6, including the
[moving-time theorem](moving-time-spectral-gap.md). The positive spectral
implication is [reconstruction R1](yangmills-reconstruction.md). The
[matrix carrier theorem](../../notes/imported/WORK_SINCE_2026-08/WORKHOUSE_MATRIX_KL_CARRIER_ATOM_THEOREM_2026-08-22.md),
sections 3.3--3.4, already proves spectral-measure convergence from normalized
fixed-time correlators. That result is prior work, not a new claim here.
K1--K2 instead combine compatible defining kernels, quotient construction,
source centering and log-convex interpolation to remove a separately assumed
limiting Hamiltonian, vague convergence and totality from this formulation.
Holder's inequality and the self-adjoint semigroup theorem are standard
ingredients; the complete argument above is analytic, not Lean formalized.

The actual-model checks use
[SC17 P10](wilson-sc17-physical-time-limit.md#p10-exact-scope-and-inputs-still-required-for-spatial-continuum),
the [continuum coupling bridge](../../paper/research_notes/G19_CONTINUUM_BRIDGE_INSERT.tex),
and the [normalized Cauchy repair](../validation/wilson-g19-cauchy-repair.md).
The separate unmerged D5--D6 source was read with its path and hash retained
in the task record; it is not silently treated as a merged Wilson estimate.

Five exact controls and six adversarial tests exercise finite Gram
quotients, rational interpolation, finite-energy weight, smoothing and omitted
hypotheses. They do not certify the infinite-dimensional analytic theorem
or the weak-coupling Wilson inputs.
