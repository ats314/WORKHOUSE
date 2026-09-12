# Corrected fourth-order coercivity and sharp multichannel spectral budgets

September 11, 2026. Derived while applying the received Gemini pillars review.
The [received review and exact correction record](../../runs/pillars_graph_2026-09-11/README.md)
remain preserved. The corrected Q4 expression is an explicit consequence of
ADR 0024, not a new fourth-order amplitude. The multichannel theorem below
extends the reviewed MT4 interface to finitely many decay channels and errors
that can grow exponentially in physical time. Novelty here means this stated
extension relative to the searched repository sources, not a worldwide priority claim.

## Q1. The assembled fourth-order polynomial is coercive

Use the carrier polynomial convention in the fourth-order generalized Hodge
pencil, A=5/48, and the adjudicated coefficient from
[ADR 0024](../decisions/0024-the-corner-cluster-from-a-third-implementation-and-the-ledger-that-was-here.md):

    C = C_historical+25/1024 = -13035490122347/550663802582400.
    b = 2A+4C = 15644916262153/137665950645600.

For every real triple L=(L1,L2,L3),

    Q(L) = A sum_i Li^2 + b sum_(i<j) Li Lj
         = d sum_i Li^2 + e (sum_i Li)^2,                  (Q1)
    d = 13035490122347/275331901291200 > 0,
    e = 15644916262153/275331901291200 > 0.

Expansion proves the identity. Cauchy--Schwarz gives (sum Li)^2<=3 sum Li^2,
so the optimal Euclidean bounds are

    d ||L||^2 <= Q(L) <= (A+b)||L||^2.                    (Q2)

The lower equality is attained by any nonzero sum-zero triple; the upper
equality by a nonzero constant triple. The matrix eigenvalues are d
(multiplicity two) and A+b=29985119454403/137665950645600 (multiplicity one).
This proves positivity for the corrected polynomial, not only the historical
one. The historical b increases by 25/256 under adjudication; the received
decimal -0.0202133 is replaced by -0.02367232068136....

This is a real quadratic-polynomial theorem at fourth order. It does not
assert a full Hamiltonian lower bound, an all-orders remainder estimate, or
a continuum gap. The historical constant remains immutable evidence.

## M1. Several decay channels and time-amplified remainders

Use the physical Hilbert spaces, H_n>=0, intended vectors f_n and approximate
vectors v_n of [MT1--MT2](moving-time-spectral-gap.md). Assume
||f_n-v_n||->0 and either its spectral-limit and totality hypotheses or the
full compatible-history-kernel hypotheses of
[K1--K5](os-kernel-moving-time-gap.md). A scalar estimate alone constructs
neither a continuum object nor its sources.

Let a_n->0 with 0<a_n<1, s>=0, and nonzero alpha_n satisfying
|alpha_n|>=c_alpha a_n^s. The raw correlation is
K_n(t)=alpha_n^2 <v_n,exp(-t H_n)v_n>. Suppose a proposed estimate is

    K_n(t) <= sum_j A_j a_n^(-p_j) exp(-m_j t)
              + sum_l B_l a_n^(r_l) exp(ell_l t).          (M1)

Both index sets are finite and nonempty, and coefficients A_j,B_l,c_alpha
are positive and independent of n. Assume p_j>=0, m_j>0, ell_l>=0 and

    P_j=p_j+2s>0, R_l=r_l-2s>0.                           (M2)

The P_j>0 assumption excludes the flat branch boundary; the older MT4
already handles its one-channel p=s=0 case. For a finite available horizon
h>0, choose t_n=c log(1/a_n), 0<c<=h; for no horizon omit this constraint.
M1 need only be available at the selected times. A whole-horizon bound is
stronger and is used below to demonstrate sharpness.

After division by alpha_n^2 and multiplication by exp(E t_n), the decay
term has cutoff power c(m_j-E)-P_j and the error term has power
R_l-c(E+ell_l). Thus the rate at a chosen c is

    F(c)=min({m_j-P_j/c}_j, {R_l/c-ell_l}_l).              (M3)

Every E<F(c) has strictly positive powers. Finite sums preserve the
vanishing bound, and MT2 or K2 gives support in [F(c),infinity) if F(c)>0.
The source approximation stays outside the exponential amplification.

For a desired 0<M<min_j m_j, F(c)>=M is exactly

    L(M)=max_j P_j/(m_j-M) <= c
       <= U(M)=min_l R_l/(M+ell_l), and c<=h.              (M4)

Endpoint equality still excludes every E<M. The common rate must hold on
the full defining source family for a full-space gap. Times, constants and
channel parameters may depend on the source, provided every source admits
that same positive M and the appropriate norm approximation.

## M2. Closed optimal rate and a witnessing observation time

Define

    M_jl = (R_l m_j-P_j ell_l)/(P_j+R_l),
    M_pair = min_(j,l) M_jl,
    M_h = min_j (m_j-P_j/h) when h is finite,
    M_raw = min(M_pair,M_h), or M_pair without a horizon.  (M5)

The largest positive rate guaranteed by M1 at logarithmic times is M_raw
when M_raw>0; otherwise these data guarantee no positive rate. Indeed, for
0<M<min_j m_j, each lower endpoint is at most each upper endpoint iff

    (P_j+R_l) M <= R_l m_j-P_j ell_l.                      (M6)

This is obtained by multiplying positive denominators in M4. The horizon
condition is equivalently M<=m_j-P_j/h for every j. Thus M4 is feasible
iff M<=M_raw. Since P_j,R_l>0 and ell_l>=0, M_pair<min_j m_j:
choose an l for a j with minimal m_j. No extra endpoint at m_j is missing.

When M_raw>0, c=L(M_raw) is a positive witness satisfying all upper and
horizon bounds. At least one pair or horizon constraint binds, so its
F(c) equals M_raw. This proves the maximum, not only a sufficient bound.
If M_raw<=0, no c has F(c)>0. Reporting zero in the helper means absence
of a positive guarantee, not a proof that a physical model has zero gap.

With one decay term, one constant plateau and ell=0 this reduces exactly to
MT4: M_pair=m(r-2s)/(p+r), with the correct shortened-horizon loss. The
single-channel target interval in the preceding review is this special case.

Example: s=1, decay pairs (p,m)=(1,2),(3,4), error pairs
(r,ell)=(5,0),(8,1). The four pair rates are 1,1,3/2,19/11.
Without a horizon the optimum is M=1 at c=3. With h=2 it is M=1/2 at c=2.
Ignoring the second error's time growth is generally unsound: for a single
(p,m)=(1,2), (r,ell)=(5,1), s=1, the rate is 1/2 rather than 1.

## M3. Sharpness, failure cases and physical scope

Choose a pair (j,l) attaining M_pair, put theta=R_l/(P_j+R_l) in (0,1),
and write X=a^(-p_j)exp(-m_j t), Y=a^(r_l)exp(ell_l t). Direct algebra gives

    X^theta Y^(1-theta)=a^(2s)exp(-M_jl t).                (M7)

Weighted AM-GM bounds this by X+Y. If M_raw=M_pair>0, take a unit target
vector with energy M_raw and v_n=f_n, alpha_n=a_n^s. Its raw correlation is
the left side of M7 and obeys M1 for every t>=0 (the unused positive terms
only enlarge the right side). Its limit is the atom at M_raw. Thus no
larger universal spectral lower bound can follow from the same data.

If instead the horizon binds at j, put M_raw=m_j-P_j/h>0. Then

    a^(2s)exp(-M_raw t) <= a^(-p_j)exp(-m_j t)
    for 0<=t<=h log(1/a).

This supplies the sharp atom throughout the available horizon. Each example
can have a separate unit vacuum of energy zero with the target on its
centered line, so it respects centering and the full one-dimensional
vacuum-complement interpretation.

If M_pair<=0, M7 grows at least as fast as a^(2s) for t>=0; AM-GM therefore
also bounds the raw zero-energy probe. If M_h<=0, the same zero-energy
probe fits its binding decay term over the available horizon. No positive
universal guarantee is possible in either case, even allowing another
sampling time inside that horizon. If an R_l<=0 were admitted, its single
error term would already dominate this zero mode. This explains the strict
normalization margin in M2.

For genuine shrinking exponentials with s>0, use the symmetric two-point
law, centered F=+/-1, and raw source sinh(alpha_n)F. On 0<alpha_n<=1,
|sinh(alpha_n)/alpha_n|<=sinh(1). A fixed enlargement of the coefficients
therefore realizes the same sharp exponents and norm approximation.
For s=0 the exact-probe example applies; it is not a shrinking tilt.

The extension replaces separate ad hoc balances by all pairwise inequalities
M6, including amplification losses and the physical horizon. It supplies
the existing kernel theorem's late-time input once an actual Wilson bound
M1 is proved. It does not supply that bound, kernel convergence, source
totality, a positive limiting separated-time correlator, or Euclidean
field-theory axioms. No G19 or W6 status is closed by this extension.
The analytic optimization and sharpness proofs above are not Lean
formalizations; the registered exact controls cover their algebra and
finite adversarial examples at the scopes recorded in the graph.
