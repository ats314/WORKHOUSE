# Reviewed theory connections: currents, source frames and residual certificates

Date: 2026-09-10. These are the new conclusions of the read-only theory-graph
exploration, integrated after the supplied independent review. They build on
the cited WORKHOUSE sources; the earlier corpus results are not claimed as
new contributions. Detailed arguments and exact computational definitions are
in the two linked derivations. The accompanying run distinguishes analytic
proof, exact controls and the precisely encoded Lean statements.

## E1. Degenerate energy and the bounded-inverse W6 composition

Let E,L be real Hilbert spaces, Y:E -> L bounded, kappa>0, and let a satisfy
a[v]>=kappa ||Yv||^2. If rho(v)=g <j,Yv>, completing the square gives

    2 rho(v)-a[v] <= g^2 ||j||^2/kappa                 (E1)

for every v. This variational inequality requires no inverse and permits a
kernel of Y. With a bounded self-adjoint A and a bounded inverse R, evaluation
at R rho gives the corresponding selected inverse-energy estimate. The checked
W6 composition still assumes both bounded inverses of its reference and
interacting operators. It does not require a uniform inverse-norm bound.
Extending the complete W6 identity to an operator without a bounded inverse
requires a separate closed-form/energy-completion argument.

Proof and source-current realization: [source derivation](../../docs/derivations/source-currents-and-spectral-totality.md).

## E2. The fixed square's complete first residual current

In the actual twelve-edge/four-face square, use the specified source-compatible
first operator W1=H1+[H0,K]. In the Gaussian ground representation its full
first cometric M1 satisfies W1=-(2 mu0)^(-1) div(mu0 M1 grad). With
M0=diag(4 Iq,2 Iu,8 Is,3 Iv), u0=F0^(-1)t1 phi and rho1=Q0 W1 u0, define

    j_phi = (1/sqrt(2)) M0^(-1/2) M1 grad u0.
    <v,rho1> = <(1/sqrt(2)) M0^(1/2) grad v,j_phi>, v in Q0.  (E2)

For every radial finite-energy source, a=|q|^2 and b[phi]=8 E[a|phi'|^2],

    <rho1,F0^(-1)rho1> <= ||j_phi||^2 <= K_star b[phi],
    K_star=(48213-16675 sqrt(2))/20706224 < 1/840.       (E3)

The strict comparison is between constants; the source-energy inequality is
non-strict, including b=0. The previous exact constant was
0.001891232457546..., so the new constant is 37.1021% smaller. The horizontal
and v-current components are retained. This is an admissible current bound,
not a claim that the current minimizes its norm.

Proof: exact Wick integration, radial integration by parts, and the joint
positive-resolvent estimate in the [source derivation](../../docs/derivations/source-currents-and-spectral-totality.md).
The [original complete operator](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/source.md)
and [previous inverse bound](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/residual_inverse.md)
retain their historical statements. Complete means the complete FIRST
coefficient of this FIXED square. Finite coupling and uniform volume remain
separate obligations.

## E3. Selected inverse control from the complete residual

Let a0,ag be real symmetric positive fast forms and R0,Rg the inverses in
their actual common-domain variational identity. Let u=R0 t and w=Rg t
belong to the required form domains, so S0=<t,R0 t> and Sg=<t,Rg t>
are nonnegative, and set
rho(v)=a_g(v,u)-<t,v>. If S0<=C0 b and
|rho(v)|<=epsilon sqrt(b) sqrt(a_g[v]), with nonnegative C0,b,epsilon, then

    |Sg-S0|=|rho(w)| <= epsilon sqrt(b) sqrt(Sg)
                 <= (epsilon sqrt(C0)+epsilon^2) b.   (E4)

Indeed x^2-y^2<=e x implies x<=y+e for x,y,e>=0; apply
x=sqrt(Sg), y=sqrt(S0), e=epsilon sqrt(b), then the residual bound again.
Thus epsilon=O(|g|) gives the selected-inverse estimate without an independent
diagonal estimate. This is a proved implication; the complete finite-g
residual estimate is still its unsupplied physical premise. The scalar
quadratic implication has a Lean proof; the full closed-form identity has its
own existing inverse/domain assumptions.

For a normalized conditional density rho and justified fiber integration by
parts, let s_a=partial_a log(rho)+div_rho(b_a)=-div_rho(J_a). With the coarse
cometric A depending only on retained coordinates, the mixed form has
h[f,v]=-(1/2) integral grad_F(v).J_(A grad f). Cauchy--Schwarz bounds its
square by the vertical energy times (1/2) integral J* S^-1 J. This implication
assumes a finite-cost current; it does not construct the density-score current.
Coefficient multiplication retains D*(c j)+j.Dc, and differentiating a moving
centered vector retains the connection [P',P]. The detailed hypotheses and
the balanced-strip 49/120 leading geometric cost are in source section SCB4.

## E4. Small exponential sources and spectral totality

On a probability space, bounded f with |f|<=B has centered exponential
s_alpha=exp(alpha f)-E exp(alpha f). As nonzero real alpha tends to zero,

    ||s_alpha/alpha-(f-E f)||_2 <= |alpha| B^2 exp(|alpha|B).  (E5)

Consequently the closed span of arbitrarily small centered exponential
sources contains every bounded centered cylinder observable. If that cylinder
family is dense, the centered exponential family is total. If each fixed
admissible source has its actual positive spectral correlation bounded by a
source-dependent finite prefactor times exp(-m t) for arbitrarily large
physical times, with ONE common m>0, spectral positivity forces its spectral
measure to vanish on [0,m). Totality supplies the spectral gap on the centered
space. Windows and prefactors may depend on the source; the common rate,
arbitrarily late times, density and actual spectral identification may not be
dropped. Proof: [source derivation](../../docs/derivations/source-currents-and-spectral-totality.md).

For normalized mesoscopic exponentials, write K(s)=log E exp(sX), with a
footprint of size N. If differentiation is justified and K''<=sigma N on
the interval from 0 to 2alpha, then
||exp(alpha X)/E exp(alpha X)-1||_2^2<=exp(sigma N alpha^2)-1. In particular
alpha=t/sqrt(N) yields a bound independent of N. The double-integral identity
for K(2alpha)-2K(alpha) proves this statement; an untilted variance bound
alone is insufficient. A lower tilted susceptibility gives the corresponding
lower inequality. Source section SCB6 supplies the full argument.

## E5. Three-coordinate sharp anisotropy and soft-energy compensation

For EXACTLY three nonnegative coordinates with x1+x2+x3=1,

    V=sum_(i<j) xi xj (xi-xj)^2
      <= (827+73 sqrt(73))/18432 < 2/25,               (E6)

with equality precisely at permutations of (a,a,1-2a),
a=(13-sqrt(73))/48. The stationary-point and boundary proof is in the
[geometry derivation](../../docs/derivations/theory-geometry-and-riccati-bridges.md).
In four coordinates, (4/5,1/15,1/15,1/15) exceeds this maximum, so the
dimension restriction is essential.

For the existing Hodge leakage identity ||delta||^2=4 C_shp^2 q^2 V,
take Y=sqrt(q) and j=delta/sqrt(q) where q>0, with j=0 at q=0. Then
||j||^2=4 C_shp^2 q V. Subject to the actual energy domination and
integrability assumptions of E1, this compensates a soft inverse weight q^-1.
Integrated comparisons are non-strict; the result does not construct an
interacting Wilson energy domination or an undefined normalized carrier at q=0.

## E6. Cubic secular identity and the source-frame metric

Let U=psi psi*, ai=|psi_i|^2, q=sum ai, R=diag(ai)-U,
H=alpha I+b U+c R on three coordinates, xi=lambda-alpha, and e2,e3
the elementary symmetric functions of the ai. Then exactly

    det(lambda I-H)=xi^3-b q xi^2+c(2b-c)e2 xi-c^2(3b-2c)e3. (E7)

This describes the displayed matrix/truncation, not uncomputed higher-order
physical terms. The proof is the rank-one determinant identity, also checked
by exact polynomial expansion in the [geometry derivation](../../docs/derivations/theory-geometry-and-riccati-bridges.md).

For the same displayed truncation M=q u^2[tQ+u^2 h], h=eta I+beta P+cX,
P=pp*, Q=I-P, |p_i|^2=x_i and t>0, the retained eigenbranch has
E0=q[u^4 mu-u^6 c^2 V/t+u^8(c^3 kappa3-beta c^2 V)/t^2+O(u^10)]. Here
mu=<p,hp>, V=sum x_i^3-(sum x_i^2)^2 and
kappa3=sum x_i^4-3(sum x_i^2)(sum x_i^3)+2(sum x_i^2)^3.
This new induced eighth-order coefficient follows from the reduced inverse
Q/t and centered moments, as proved in TG4. It is a fixed-momentum expansion
of this finite matrix and contains no independent higher-order physical kernel.

For an actual compatible differentiable Schur graph J and skew source
generator K, the full source commutator compresses as

    J*[H,K]J = S L+L* S, L=P K J.
    S'=D_eff+S L+L* S, V'=-L V
    (V* S V)'=V* D_eff V.                            (E8)

Carry the retained metric with this generally NONUNITARY congruence. If
M=-partial_z S, then -partial_z(V* S V) equals V* M V minus
(partial_z V)* S V and V* S (partial_z V). Those extra pairings vanish on
shell, not for arbitrary off-shell vectors. Algebraic cancellation neither
proves common-domain regularity nor bounds the actual transport generator.

## E7. Riccati residual certificate and scalar-source parity

For the stated Banach-algebra Riccati map T(X)=S(X^2-D), a fixed point X_star
and trial Y in the radius-r ball, a linear map bound ||S||<=beta and
2 beta r<1 imply

    ||Y-X_star|| <= ||Y-T(Y)||/(1-2 beta r).          (E9)

The existing abstract default parameter functions on lambda in [0,3/100]
give contraction below 3/20 and amplification below 20/17. This abstract
interval is not a new physical SC17 closure window. Cross-scale use requires
residual summability in one common norm, or the corresponding transported
norm factors. See the [geometry derivation](../../docs/derivations/theory-geometry-and-riccati-bridges.md).

In the actual square's parity-compatible scalar outer-trace representation
specified in TG7,
signed chart reflection gives S(-g,z)=S(g,z). Every existing odd two-sided
Taylor coefficient therefore vanishes, including the cubic one. W1 itself
is generally nonzero. Evenness does not imply a uniform fourth-order
remainder: |g|^3 is a counterexample. A controlled fourth-order expansion
and extension of the actual source transport toward g=0 remain separate.

## Consequence and remaining work

The explicit first current is an established input to a finite-coupling
current-remainder construction. A complete residual bound would enable E4
and its selected-inverse estimate. Volume-uniform control, compatible
source/metric/physical-clock transport, and summable scale errors remain
additional hypotheses for the continuum route. The formalized variational
estimate must not be described as an inverse-free formalization of W6.

The [integration run](../../runs/theory_current_bridges_2026-09-10/README.md)
records recovered proof provenance and fresh checks of this revision.
