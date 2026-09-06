# Literal endpoint transfer: complete low windows without global score smallness

5 September 2026. Analytic research continuation. The new object is the
exact compressed quantum endpoint transfer, including its generated temporal
memory. It is not the static Schur operator, the exponential of the marginal
Dirichlet generator, or an identification of an OS-history range.

Inputs are the accepted literal true-vacuum source and its inverse-energy
addendum, the common-Gauss source theorem, and the exact ground-marginal
construction. The existing FORM theorem already handles a static normalized
Schur operator; the argument below instead compares the spectrum of the full
endpoint transfer directly. The true-ground central score obstruction explains
why a global pointwise small-Fisher hypothesis should not be inserted here.
The earlier [G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md](G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md), Sections 6-7,
already proves the exact source-moment leakage identity and a full-complement
separation criterion; its received 33-check packet preserves that provenance.
Section 3.1 below extends those inputs with a tail bound from the COMPLETE
literal low frame and a threshold-dependent matrix spectral-count certificate.

## 1. Exact endpoint object and its domain

Let h>=0 be self-adjoint on a Hilbert space H, let J:L->H be an isometry,
P=JJ*, Q=I-P, and suppose P contains the entire vacuum kernel. For tau>0 set

    C_tau=J* exp(-tau h) J,
    K_tau=-(1/tau) log C_tau.                              (1)

C_tau is a positive self-adjoint contraction with zero kernel: its quadratic
form is ||exp(-tau h/2)Jf||^2, positive for every nonzero f. Hence spectral
calculus defines the possibly unbounded, nonnegative self-adjoint K_tau on
a dense domain. Zero may be in the spectrum of C_tau, but is not an
eigenvalue. No bounded inverse of C_tau is assumed.

Its exact vacuum correspondence is

    ker K_tau = J* ker h.                                 (2)

Indeed ||exp(-tau h/2)Jf||=||f|| is equivalent to Jf belonging to ker h.
The assumed vacuum inclusion supplies the converse on the whole fine kernel.

For the actual Wilson true-ground source Jf=f(U)Omega, identify L with the
actual marginal L2(mu). Ground-state transformation makes exp(-tau h) the
stationary reversible fine diffusion transfer. Thus

    C_tau f(U)=E[f(U_tau) | U_0=U].                       (3)

The conditioning uses the true quantum ground distribution. C_tau preserves
positivity and constants and is self-adjoint in L2(mu). It is an exact
two-endpoint coarse transition. It need not reproduce longer coarse histories
when composed with itself.

## 2. Complete spectral comparison

Assume the full form bound h>=cQ, c>0. For every 0<=E<c, the established
literal frame is

    Pi_E P Pi_E >= (1-E/c) Pi_E,
    Pi_E=1_[0,E](h).                                     (4)

More generally one may use any established sharper complete-window frame
Pi_E P Pi_E>=gamma Pi_E, gamma>0.

Put B_tau=exp(-tau h/2)J. Its two positive products are

    B_tau*B_tau=C_tau,
    B_tau B_tau*=exp(-tau h/2)P exp(-tau h/2)=T_tau.      (5)

Their nonzero spectra, with multiplicity, are unitarily equivalent by polar
decomposition. On the whole fine space,

    0<=T_tau<=exp(-tau h).                               (6)

On ran Pi_E, spectral invariance of exp(-tau h/2) and the frame give

    <psi,T_tau psi> >= gamma <psi,exp(-tau h)psi>.        (7)

Thus compact min-max, or bounded-operator spectral positive-index arguments,
apply to the COMPLETE source space. In the discrete case write lambda_j for
the increasing fine energies, including vacua, and sigma_j for the decreasing
positive eigenvalues of C_tau. Whenever lambda_j<c,

    (1-lambda_j/c) exp(-tau lambda_j)
       <= sigma_j <= exp(-tau lambda_j),

    lambda_j <= kappa_j
       <= lambda_j-(1/tau)log(1-lambda_j/c),             (8)

where kappa_j are the eigenvalues of K_tau. For a larger whole low window
with frame gamma, its levels obey the sharper bound

    lambda_j <= kappa_j <= lambda_j-(log gamma)/tau.     (9)

The proof of the lower sigma bound uses the full j-dimensional fine spectral
space in (7), not separately chosen column overlaps. The upper bound (6)
automatically includes arbitrarily high retained source energies.

For general spectral types use open counting functions, permitting infinity.
For E<c and F_tau(E)=E-log(1-E/c)/tau,

    N_K(E)<=N_h(E),
    N_h(E)<=N_K(F_tau(E)).                              (10)

One may take strict endpoints or limits from inside a spectral interval to
handle boundary eigenvalues. These inequalities follow from positive index
of T_tau-r, polar decomposition, and (6)-(7). They do not infer finite rank
from an infinite-dimensional lower bound.

In particular let Delta be the full fine nonvacuum spectral bottom and mu
the full coarse nonvacuum bottom. If mu>0, then Delta>0. More precisely,

    Delta >= F_tau^(-1)(mu),                            (11)

where the increasing inverse has range [0,c), and an infinite coarse gap is
interpreted by the endpoint c. If Delta<c, apply (7) on spectral intervals
arbitrarily close to Delta and then let their width vanish; this gives
mu<=F_tau(Delta). If Delta>=c the result is immediate. Thus a zero fine gap
cannot be hidden by the literal compression under h>=cQ. This is a complete
spectral statement, not a claim that a selected source variational energy
bounds the full gap.

All gap and nonvacuum counting comparisons are made on the corresponding
vacuum orthogonal complements in (2). This removes every vacuum direction
before taking an index, including when the original vacuum multiplicity is
infinite. Raw counting functions that are already infinite from the vacuum
alone would not establish a nonvacuum gap.

## 3. A complete isolated cluster and explicit high-source control

Suppose a complete finite fine low space Pi has rank r, all its energies
are at most ell<t, and h>=t on Pi-perp. Suppose Pi P Pi>=gamma Pi. If

    gamma exp(-tau ell)>exp(-tau t),                    (12)

then K_tau has exactly r eigenvalues below t, counting vacuum multiplicity.
All of them obey (9); there are no additional coarse states below t.

There is a useful exact decomposition explaining why the high retained
space has not been discarded. Define

    R=projection onto ran(J*Pi),
    C_low=J*Pi exp(-tau h)Pi J,
    C_high=J*(I-Pi)exp(-tau h)(I-Pi)J.

The frame makes ran(J*Pi) closed and has dimension r. Moreover

    C_tau=C_low+C_high,
    C_low>=gamma exp(-tau ell) R,
    0<=C_high<=exp(-tau t) I,
    (I-R)C_tau(I-R)<=(exp(-tau t))(I-R).                (13)

There are no low/high spectral cross terms before source compression.
C_high nevertheless produces cross terms between R and its source-space
orthogonal complement; (13) retains them. Min-max using R proves at least
r eigenvalues above exp(-tau t), while min-max on R-perp proves at most r.
This is a full high-retained control, but R uses the complete fine low
projector. A computational source approximation needs a quantitative
subspace certificate for this R. Replacing it by an arbitrary low spectral
space of the marginal generator is not justified by (4).

### 3.1. A finite two-lag certificate with a complete high-source bound

Choose a finite literal source isometry J0, with P0=J0J0*, Q0=I-P0, retaining
the exact vacuum. For an unnormalized finite list its actual quantum marginal
Gram G is first retained and synthesis is multiplied by G^-1/2. Suppose a
COMPLETE low projection Pi has vacuum plus energies in [a,ell],
0<a<=ell<t, the rest of h is at least t, and Pi P0 Pi>=gamma0 Pi, where
0<gamma0<=1. The entire Q0 space includes both the literal fast space and
every omitted retained source direction. Spectral order gives

    D:=Q0 exp(-tau h) Q0|Q0 <= d I_Q0,
    d=gamma0 exp(-tau t)+(1-gamma0)exp(-tau a).          (13a)

The upper spectral bound for exp(-tau h) has coefficients 1 on the vacuum,
exp(-tau a) on the complete low excited space, and exp(-tau t) elsewhere.
Q0 kills the first coefficient and its compressed low excited projector
has norm at most 1-gamma0. This proves (13a) on the ENTIRE complement.

Only two finite correlation matrices are needed to measure the coupling:

    A=J0*exp(-tau h)J0,
    V=J0*exp(-2tau h)J0-A^2
     =J0*exp(-tau h)Q0 exp(-tau h)J0>=0.                (13b)

This is exactly the established source-moment identity, now at the physical
endpoint lag. Writing R=Q0 exp(-tau h)J0, it says R*R=V. For z>d, bounded
block elimination and resolvent order give

    N_exp(-tau h)(z)
      =n_+(A-zI+R*(z-D)^-1 R),
    n_+(A-zI)<=N_exp(-tau h)(z)
      <=n_+(A-zI+V/(z-d)).                             (13c)

Here N_T(z)=dim 1_(z,infinity)(T), and n_+ counts STRICT positive matrix
eigenvalues. The bounded invertible triangular congruence has a negative
Q0 block D-z, so all positive inertia lies in the finite displayed matrix.
The estimate (z-D)^-1<=(z-d)^-1 I proves the upper inequality. No finite
approximation of the Q0 spectrum or small cross block is assumed.

If the two finite positive indices coincide, their common integer is the
COMPLETE fine spectral count above z. Thresholds z=exp(-tau E) certify
whole energy windows. Keeping V as a matrix retains directional information
that would be discarded by a scalar norm bound.

If only the full literal source frame gamma is known and R0 is a finite
coarse source projection, require also that R0 contain J*ker h exactly.
Approximate low-space overlap alone does not supply this vacuum hypothesis.
Then the additional approximation certificate
||(I-R0)J*Pi||<=eta, with eta^2<gamma, gives gamma0>=gamma-eta^2 for
J0=J|ran R0. Thus the
finite-source input is precise and measured in the actual source Hilbert
norm. It is not supplied merely by assigning high marginal-form energy to
unselected directions. Formula (13a), unlike (13b), uses a COMPLETE spectral
and source premise; the earlier packet's dark-state negative control still
applies if that premise is omitted.

## 4. Actual additive strips at their natural time scale

Use the actual fixed-SU(N) strip and its true-vacuum literal source. The
accepted physical low spectrum has first energy a(u) and next threshold
t(u), with

    a(u)/sqrt(u)->2sqrt(3),
    t(u)/sqrt(u)->sqrt(3)+sqrt(5),
    delta(u)=||Q Pi_first||->0.

For M independent physical Gauss copies, once 2a>=t the complete low space
has rank 1+M. Exact excitation supports give gamma=1-delta^2, uniformly in
M. Choose any fixed s>0 and the natural Hamiltonian time

    tau(u)=s/sqrt(u).                                   (14)

Then tau(t-a) tends to s(sqrt(5)-sqrt(3))>0, whereas -log gamma tends to
zero. Therefore (12) holds for all sufficiently large u uniformly in M.
The exact endpoint Hamiltonian has precisely the same vacuum plus M-state
first cluster below t, with

    0<=kappa_j-lambda_j<=sqrt(u)(-log gamma)/s=o(sqrt(u)) (15)

uniformly over the complete cluster and copy count.

With one common Gauss constraint, use the accepted unrestricted slow
adjoint and physical radial classification. The low energies are a(u) and
2alpha(u), and

    t=min(b,alpha+beta,3alpha),
    gamma=1-max{d_r^2,2d_A^2-d_A^4}->1.

The complete physical low rank is 1+M+M(M-1)/2. The same argument, with
ell=max(a,2alpha), proves exact preservation of that complete rank below
t and the uniform estimate (15). This includes all pair singlets, not
merely separate single-block invariant states. The O(1) radial/pair splitting
is not recovered from delta->0 alone: that would require
(-log gamma)/tau=o(1), or a sharper energy-resolved argument.

These conclusions also have an exact tensor structure. Before any common
Gauss restriction the true vacuum, source isometry, and fine heat transfer
factor over additive blocks. Hence for every finite M,

    C_tau^(M)=tensor_i C_tau^(i),
    K_tau^(M)=sum_i K_tau^(i).                           (16)

Equivariance permits restriction to one common Gauss action after forming
these products. Independent Gauss restriction factors separately. The
corresponding countable exact-vacuum tensor product is defined on the
finite-excitation core, with its additive closed generator. The known local
gap/irrep thresholds exclude three or more nonvacuum factors in the selected
common-Gauss window, so the one-/two-support classification and uniform
conclusion extend to that countable product. This step uses the exact
additive structure; infinite cardinality in (10) alone would not establish
the classification.

Explicitly local UNRESTRICTED equivariant endpoint min-max gives
alpha<=kappa_A<=alpha-log(1-d_A^2)/tau for the slow adjoint, with every
next energy outside the vacuum and that adjoint at least beta. Local
invariant comparison gives a<=kappa_r<=a-log(1-d_r^2)/tau, with every
next physical energy at least b. Thus pair singlets have energy 2kappa_A;
a pair using a state outside the slow adjoint costs at least alpha+beta,
three nonvacuum factors cost at least 3alpha, and one invariant factor
outside the radial costs at least b. These transferred local thresholds
and exact excitation supports justify the countable common-Gauss assertion.

For a physical Hamiltonian c_H H, (14) means the physical time
s/(c_H sqrt(u)). No energy unit is silently reset.

## 5. Temporal memory and the Markov/RP boundary

The exact defect is

    C_(tau+sigma)-C_tau C_sigma
       =J*exp(-tau h)Q exp(-sigma h)J.                  (17)

At equal times it is positive semidefinite. It vanishes precisely when
Q exp(-tau h)P=0, equivalently P reduces h. Thus generic literal coarse
sources generate memory. In particular

    C_2tau>=C_tau^2,
    K_2tau<=K_tau                                       (18)

as closed forms. The last implication follows from operator monotonicity
of log, interpreted for injective positive contractions through the
resolvent integral for -log. The squared contraction has
-log(C_tau^2)=2[-log(C_tau)]. No commutation of C_tau and C_2tau is needed.
Together with (8), dyadic temporal coarsening decreases every controlled
sorted low level to the corresponding fine level as tau tends to infinity.

At fixed tau, C_tau is a reversible Markov transition in the true-ground
setting. Its stationary discrete-time Markov chain is reflection positive:
site reflection yields a conditional L2 norm square; bond reflection yields
<f,C_tau f>_mu>=0. Its two-endpoint law agrees with the fine law at time tau.
Its multitime law generally differs from the exact projected fine history
law by (17). This construction therefore does not identify an OS-history
range or erase the original generated memory.

Nor need -K_tau=log(C_tau)/tau be a continuous-time Markov generator. Take
the symmetric continuous-time random walk on the four-vertex path and
observe the blocks {1},{2,3},{4}. The coarse marginal is (1,2,1)/4. Write
C_tau=I+tau A+tau^2 B+O(tau^3) in its Markov coordinates. Exact generator
compression gives

    A=[[-1,1,0],[1/2,-1,1/2],[0,1,-1]],
    B_13=0,     (A^2)_13=1/2.

Consequently (log C_tau)_13=-tau^2/4+O(tau^3)<0 for sufficiently small
positive tau. A continuous-time Markov generator cannot have that negative
off-diagonal entry. K_tau is a legitimate positive quantum Hamiltonian,
but need not be a local Wilson Hamiltonian or generate Markov transitions
at fractional multiples of tau.

## 6. Exact obstruction to truncating the marginal generator

Let h=diag(0,1,L), and retain the exact vacuum e0 together with
p=(0,24/25,7/25). Then the true low literal frame is 576/625. The rank-one
fast inverse cap is

    Q h_+^-1 Q=[49/625+576/(625L)]Q,
    h>=c_L Q,   c_L=625/(49+576/L).

For L>=4096, c_L>12, while the fine excitation is exactly 1. Nevertheless
the marginal-form energy of p is

    <p,hp>=(576+49L)/625 -> infinity.                   (19)

This is a finite self-adjoint source model satisfying the abstract spectral
premises; it is not asserted to be an actual Wilson or Markov realization.
Any fixed upper-energy cutoff of J*hJ eventually removes the source that
contains 576/625 of the actual low state. Exact vacuum retention, a large
full fast floor and a good literal L2 frame do not prevent this failure.
Taking p=(0,(n^2-1)/(n^2+1),2n/(n^2+1)) and L=n^6 makes the frame tend to
one and the full fast coefficient diverge, while (19) still diverges.

The exact endpoint excitation instead has transfer eigenvalue

    (576/625)exp(-tau)+(49/625)exp(-tau L),

and hence the correct energy within -log(576/625)/tau. This explicitly
distinguishes C_tau from exp(-tau J*hJ). It locates the missing premise in
a low-marginal-generator truncation: an energy-weighted approximation or
spectral-tail certificate is needed, not merely source norm overlap.

## 7. Conditional physical-time scale budget

For 0<=lambda<=E_*<c,

    F_tau(lambda)<=lambda[1+1/(tau(c-E_*))].             (20)

Suppose an exact hierarchy in a single physical energy clock identifies
each coarse Hamiltonian with the full endpoint K_tau of its fine level,
retains the actual vacuum, and supplies h_j>=c_j Q_j. Suppose the relevant
coarse gaps are <=E_* and c_j>E_*. Then complete-gap comparison gives

    Delta_j>=Delta_(j-1)/(1+rho_j),
    rho_j=1/[tau_j(c_j-E_*)].                           (21)

Thus a positive initial gap and sum rho_j<infinity imply a positive lower
bound Delta_0 exp(-sum rho_j). If c_j>=C/a_j, a_j decreases geometrically,
and tau_j=a_j(j+1)^(1+epsilon)/C with epsilon>0, then eventually
c_j>=2E_* and rho_j<=2/(j+1)^(1+epsilon). The sum converges while tau_j
tends to zero in physical time. This budget does not require summability
of a coupling squared.

This is conditional. It supplies neither interacting full-form floors,
an exact compatible hierarchy, locality or prescribed spatial coarse-law
matching, nor a continuum correlation limit or Euclidean invariance.
Even exact endpoint kernels at different scales need not assemble into a
single compatible Wilson theory without those additional arguments.

## 8. Evidence and consequence

The accompanying exact controls check a noncommuting complete low cluster,
all retained high energies, both products in (5), equal-time memory, the
source-energy truncation obstruction, and the genuine Markov compression's
negative logarithmic rate. They use rational matrices and exact polynomial
series; no numerical eigenvalue extrapolation is used.

The new actual consequence is a complete natural-clock endpoint coarse
spectrum for additive physical Wilson blocks, uniformly in copy count and
with common-Gauss pair states retained. The remaining interacting target
is concrete: prove a corresponding actual full fast/source estimate and
compare these endpoint kernels to a consistent coarse quantum law with
controlled spatial interactions. Global pointwise Fisher smallness is
not a prerequisite for the complete spectral transport proved here.

## Canonical source provenance and reproduction

This is the canonical copy of the independently reviewed 5 September
derivation [LITERAL_ENDPOINT_COMPLETE_WINDOW.md](../../runs/wilson_endpoint_local_score_2026-09-05/LITERAL_ENDPOINT_COMPLETE_WINDOW.md),
whose original SHA256 is `4dcb8da8880414960035de61780dedd5ac7f31f3e1159846b37235000e01b930`. The original proof bytes are
preserved; this copy adjusts only stage metadata and relative links,
then appends this explicitly separate provenance and follow-up record.

The [reproduction run](../../runs/wilson_endpoint_local_score_2026-09-05/README.md) preserves the analytic
sources and the precisely scoped finite controls:

- [check_literal_endpoint_window.py](../../runs/wilson_endpoint_local_score_2026-09-05/check_literal_endpoint_window.py)
- [literal_endpoint_window_controls_frozen.json](../../runs/wilson_endpoint_local_score_2026-09-05/literal_endpoint_window_controls_frozen.json)
- [INDEPENDENT_ENDPOINT_WINDOW_AUDIT.md](../../runs/wilson_endpoint_local_score_2026-09-05/INDEPENDENT_ENDPOINT_WINDOW_AUDIT.md)
