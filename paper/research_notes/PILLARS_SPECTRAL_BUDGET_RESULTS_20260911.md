# Review-derived spectral budgets: registered results

September 11, 2026. This result capsule summarizes the
[complete proofs](../../docs/derivations/review-derived-spectral-budgets.md).
The received Gemini review, original correction replay, and evidence boundary
are preserved in the [run](../../runs/pillars_graph_2026-09-11/README.md).
This capsule is a second locator for the same derivation, not independent evidence.

## Q1. Corrected fourth-order coercivity

For the adjudicated C=-13035490122347/550663802582400 and A=5/48,
b=2A+4C=15644916262153/137665950645600. For every real L in R3,

    Q(L)=A sum Li^2+b sum_(i<j)LiLj
        =d||L||^2+e(sum Li)^2,
    d=13035490122347/275331901291200>0,
    e=15644916262153/275331901291200>0.

The sharp Euclidean lower coefficient is d and the upper is
29985119454403/137665950645600. The cross coefficient is the historical one
plus 25/256. Expansion, the zero-sum eigenspace and the constant eigenspace
prove the result. This is an explicit consequence of ADR 0024 in the
fourth-order polynomial convention, not an all-orders physical bound.

## M1-M2. Sharp multichannel rate and witnessing time

Let two finite nonempty channel families have p_j>=0, m_j>0, ell_l>=0,
s>=0, P_j=p_j+2s>0 and R_l=r_l-2s>0. Let a_n->0, 0<a_n<1, and
|alpha_n|>=c_alpha a_n^s. For positive cutoff-independent coefficients assume

    K_n(t)<=sum_j A_j a_n^-p_j exp(-m_j t)
              +sum_l B_l a_n^r_l exp(ell_l t)

at the selected physical times t_n=c log(1/a_n), optionally with 0<c<=h.
Define

    M_pair=min_jl (R_l m_j-P_j ell_l)/(P_j+R_l),
    M_raw=min(M_pair,min_j(m_j-P_j/h))

and omit the horizon term when no h is imposed. When M_raw>0 this is the
optimal guaranteed logarithmic-time rate, witnessed by
c=max_j P_j/(m_j-M_raw). Otherwise no positive rate is guaranteed.

Indeed a target 0<M<min m_j is admissible iff

    max_j P_j/(m_j-M)<=c<=min_l R_l/(M+ell_l), c<=h.

All pairwise lower/upper comparisons reduce to M<=M_pair; the horizon gives
the remaining bound. Endpoint equality still excludes every E<M. The full
proof supplies positive-denominator and maximum-attainment details.

For spectral consequences require actual H_n>=0, approximate vectors with
norm defect tending to zero, squared-source normalization, and either the
existing MT2 spectral-limit/totality hypotheses or full compatible-kernel
construction. These hypotheses are not proved by this scalar optimization.

## M3. Sharpness and zero-rate boundary

For a binding pair set theta=R_l/(P_j+R_l). The weighted product of its decay
and error terms equals a_n^(2s) exp(-M_pair t); AM-GM bounds it by their sum.
A centered unit one-energy source therefore saturates a positive pair rate
throughout the time horizon. A binding horizon term similarly permits an
atom of energy m_j-P_j/h throughout 0<=t<=h log(1/a_n). A nonpositive binding
rate permits a centered zero-energy atom. Symmetric two-point exponentials
realize the same exponents for s>0 after a fixed prefactor enlargement.
Thus the exponent cannot be improved from the stated data alone.

The complete proof treats centering, source approximation and the
nonpositive cases explicitly. This is sharpness among abstract positive
spectral models, not a counterexample to Wilson Yang-Mills.

## Consequence and remaining obligation

The finite-family optimization is discharged and can supply the existing
moving-time/kernel theorem's rate input when a Wilson estimate is proved.
Actual continuum history kernels, fixed-time compatibility, a common positive
rate on the full defining family, nonzero separated-time weight and the
Euclidean field-theory requirements remain open. G19 and W6 are not closed.
The full arguments are analytic; the four native exact controls and
independent envelope tests have their separate T1/regression scope.
