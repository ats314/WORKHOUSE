# Moving-time continuum spectral gap criterion

11 September 2026. Full proof and falsifiers:
[moving-time spectral exclusion](../../docs/derivations/moving-time-spectral-gap.md).

## A. Approximate probes and the moving-time limit

For nonnegative self-adjoint H_n, target f_n and approximate probe v_n in
the same Hilbert space, put d_n=||f_n-v_n|| and
C_n(t)=<v_n,exp(-tH_n)v_n>. Positive spectral measures satisfy

    sqrt(nu_(f_n)([0,E])) <= d_n+exp(E t/2)sqrt(C_n(t)).

If d_n->0, nu_(f_n) converges vaguely to nu_f, t_n->infinity, and
exp(E t_n)C_n(t_n)->0 for every E<M, then nu_f([0,M))=0.
With actual spectral measures of one reconstructed physical H and a total
centered family with common M>0, H on the vacuum complement is at least M.
Only one growing physical observation time per cutoff is needed. There
is no rate requirement on d_n, no uniform late-time cutoff estimate, and
no quantitative convergence requirement at those moving times.

For bounded F_n and centered exponential source s_n, use
v_n=s_n/alpha_n. The established Taylor bound gives
d_n<=|alpha_n|B^2 exp(|alpha_n|B), while C_n=K_n/alpha_n^2.
The normalization loss is essential. Full statement: MT1-MT3, sections
1-3 of the source. Vague convergence, identification, density and positive
physical rate are hypotheses; no actual Wilson continuum object is
constructed by this abstract implication.

## B. Sharp cutoff and source budget

Assume 0<a_n->0, p,s>=0, r,m>0, |alpha_n|>=c_alpha a_n^s,
and K_n(t)<=A a_n^(-p)exp(-mt)+B a_n^r at t=c log(1/a_n).
Then every E below

    M(c)=min(m-(p+2s)/c,(r-2s)/c)

is excluded from the limiting target measure. If r>2s, the unrestricted
optimum is M_*=m(r-2s)/(p+r) at c_*=(p+r)/m. A horizon c_max
uses c_opt=min(c_max,c_*); a positive certificate requires
c_max>(p+2s)/m. The p=s=0 case has a flat optimum m for c<=r/m.
For shrinking sub-polynomial tilts, take the limiting s down to zero,
not a constant lower bound on a tilt tending to zero.

One-atom positive measures saturate both the full and shortened-horizon
rates. The all-time example is the weighted geometric mean of the two
terms of the raw bound. A symmetric two-point exponential source gives
the same exponents with fixed prefactors. Full statement: MT4-MT5,
sections 4-5 of the source.

## Evidence and successor

Both results have analytic proofs; the whole statements remain T3.
Four T1 checks verify the exponent identities and finite positive-transfer
controls. Thirteen software tests cover exact inputs, degenerate margins,
and constrained optimality. Neither finite tests nor the graph certify
the measure limit or the physical hypotheses.

The G19 successor is to prove this one-time normalized bound on an actual
continuum trajectory and identify nontrivial limiting physical spectral
measures for a total source family. Existing fixed-spacing G18 results,
the interacting W6 estimate, and the separate continuum-existence and
normalized scale-transport obligations retain their scopes.
