# G19: compatible history kernels and the moving-time gap

11 September 2026. Result: a stronger proved analytic implication; G19 remains
open because its actual weak-coupling Wilson inputs are not established.

## A. Kernel construction and full-space implication

The [full proof](../../docs/derivations/os-kernel-moving-time-gap.md), K1--K2,
starts with a common defining history space D, physical shifts S_t and cutoff
embeddings I_n into actual positive Hamiltonian spaces. Assume all fixed
Gram kernels converge to finite limits, the fixed-time shift/semigroup
defects vanish in norm, and q(f,S_t f)->q(f,f) at zero time.

For the full algebra of strictly positive-time histories, continuity is
automatic: every f=S_tau g for some tau>0, and the cutoff spectral theorem
gives ||(exp(-tH_n)-I)exp(-tau H_n)||<=t/(e tau). Finite compatible kernel
limits pass this estimate to the quotient before a limiting generator is
assumed. K5 therefore discharges the separate zero-time-continuity premise
for that defining history geometry; full Euclidean field regularity is still
a different requirement.

These hypotheses construct the quotient Hilbert space and its strongly
continuous positive self-adjoint contraction semigroup. The centered
defining space is automatically total in the vacuum complement.

If norm-approximate centered probes v_n have one physical T_n->infinity with
C_(v_n)(T_n)<=b_n and liminf -log(b_n)/T_n>=M>0, Holder interpolation gives

    C_(v_n)(t)<=||v_n||^[2(1-t/T_n)] b_n^(t/T_n).

Passing to each fixed t yields C_f(t)<=||f_c||^2 exp(-Mt). A common M on a
spanning defining family gives H on Omega-perp>=M and ker H=span{Omega}.
No separate vague-limit premise or source frame bound is required in this
formulation. The actual kernel limits, compatibility and zero-time
continuity remain hypotheses. It does not construct the full Euclidean
local Yang--Mills field theory merely from a spectral upper bound.

The prior moving-time power budget still supplies
M=m(r-2s)/(p+r), r>2s, when the actual raw and normalized estimates hold.

## B. Nontriviality at finite physical energy

For the actual limiting centered vector, suppose V=||f_c||^2 is finite and
C=<f_c,exp(-tau H)f_c>>0 at a fixed physical tau>0. Put
R=tau^-1 log(2V/C). The positive spectral measure obeys

    nu([0,R]) >= C/(2-C/V) >= C/2 > 0.

With the gap from A, the same weight lies in [M,R]. This needs no isolated
atom or spin assignment. An actual positive limiting correlator is an
input, not a consequence of an upper bound or of Euclidean equal-time
variance before the OS quotient.

## C. Attempted Wilson closure and precise stopping point

The established SC17 physical-time and infinite-volume theorems apply at
fixed spacing in bounded bare-coupling intervals. The continuum trajectory
g->0 has u=g^-4->infinity and leaves those intervals. Their decay estimates
cannot be inserted into A on that tail.

The reviewed continuum Cauchy argument controls only O(1/k) increments;
its repaired summable map/source drift remains an actual-model obligation.
For u_k=1/(alpha+beta k), the exact normalized action coefficient
|Delta u|/(4u_k u_(k+1))=beta/4 shows why a bounded covariance alone does
not recover an O(1/k^2) increment.

The remaining route is therefore actual continuum history-kernel
convergence with fixed-time compatibility, positive separated-time physical
weight, a common growing-time decay rate on the full history family, and
the required Euclidean/local field-theory structure. G19 is not closed.

Five registered exact controls test finite Gram quotients, interpolation,
weight and limiting counterexamples. Six adversarial tests include a
nonvanishing compatibility defect, divergent source norms, an OS-null
source with positive Euclidean variance and an unobserved slow sector.
The whole theorem is analytic and is not claimed to be Lean formalized.
