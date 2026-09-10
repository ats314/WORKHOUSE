# W6: raw derivative scaling, the remaining transport estimate, and the physical budget

10 September 2026. Analytic continuation of the actual compact square theorem.
This note proves the desired inverse-power scaling for the **untransported**
vacuum-subtracted form and its ground-energy derivatives through order three.
It then gives explicit sufficient energy-space bounds on the actual transport
generator which imply the complete transported constants `M_j(s) <= c_j s^-j`.
The generator bounds are the remaining model estimate; a first source-frame
bound into L2 alone is not silently substituted for them.

## 1. Inputs, conventions, and what is new

The prior project inputs are:

- [compact_residual.md](../w6_compact_continuation_20260909/compact_residual.md),
  C1-C20: common form domain, actual source/vacuum transport, nonreducing graph,
  complete Schur identity and cubic remainder at positive reference coupling.
- [ground_first_jet_remainder.md](../w6_compact_continuation_20260909/ground_first_jet_remainder.md),
  G4-G7: `e_g = e_0 + O(g^2)` and an actual-ground form-norm remainder.
- [quantile_scale.md](../w6_compact_continuation_20260909/quantile_scale.md),
  Q10-Q14: the bounded dilation-subtracted actual-ground derivative and its
  averaged conditional variance.
- [quantile_source_weight.md](../w6_compact_continuation_20260909/quantile_source_weight.md),
  W4-W6: the Hardy tail-resistance criterion for the centered source derivative.
- The preserved [subdivision theorem](../../worktrees/w6-energy-form-20260910/docs/research/w6-subdivided-compact-transport-2026-09-10.md),
  S2-S5, already removes the extra `c1 < 4` summability restriction. This note
  does not claim that construction as new.

Throughout, `H_g = (g^2/2)T + g^-2 V`, `T,V >= 0`,
`L_g = H_g-e_g`, and the real normalized positive ground is `Omega_g`.
The common form domain is the actual compact electric H1 domain. On the fixed
square and a sufficiently small interval `0<g<g_*`, the prior results supply

```
0 <= e_g <= E < infinity,       L_g >= gamma (I-Pi_g),
Pi_g = |Omega_g><Omega_g|,      gamma > 0.
```

All derivatives below are at positive g, where the existing compact elliptic
argument establishes smoothness. The constants are independent of g on this
interval, but this statement alone does not make them independent of volume.
Write `mathfrak B_g` for the scalar Hardy constant and `F_g` for the operator
forcing called `B_g` in Q9; these are different quantities.

Sections 2-4 are the new derivative reduction. Section 5 explains its exact
relationship to the Hardy step. Section 6 carries all source-energy and clock
factors through the existing subdivision budget.

## 2. Raw electric and magnetic derivatives already have the required scaling

Set `A_g=(g^2/2)T`, `C_g=g^-2 V`, so `H_g=A_g+C_g`. Exactly,

```
g H'_g       = 2 A_g - 2 C_g,
g^2 H''_g    = 2 A_g + 6 C_g,
g^3 H'''_g   = -24 C_g.                                   (R1)
```

For nonnegative forms A,C, Cauchy-Schwarz in their direct-sum energy space
gives `|a A[u,v]+c C[u,v]| <= max(|a|,|c|) sqrt(H[u]H[v])`.
Consequently, with `(a1,a2,a3)=(2,6,24)`, for every pair of form-domain vectors,

```
|H_g^(j)[u,v]| <= a_j g^-j sqrt(H_g[u] H_g[v]), j=1,2,3.   (R2)
```

This controls the complete original-edge electric form and the actual magnetic
potential on all energies. There is no Taylor expansion of V, small-field
restriction, Gaussian replacement, or eigenfunction cutoff in this step.

## 3. Ground-energy derivative constants from the actual reduced resolvent

Put `chi_g=Omega'_g`, so `<chi_g,Omega_g>=0`. Differentiating the actual
eigenvalue equation in the common form domain gives

```
e'_g = H'_g[Omega_g],
L_g[chi_g,u] = -(H'_g-e'_g)[Omega_g,u].                     (R3)
```

On `Omega_g`-perp, `H_g[u] <= h_g L_g[u]`, where
`h_g=1+e_g/gamma`. Taking `u=chi_g` in (R3), applying (R2), and dividing
by `sqrt(L_g[chi_g])` when it is nonzero proves

```
|e'_g| <= 2 e_g/g,
L_g[chi_g] <= 4 e_g h_g/g^2,
||chi_g||^2 <= 4 e_g h_g/(gamma g^2).                      (R4)
```

These are form-dual resolvent estimates: `H'_g Omega_g` need not be bounded
as an L2 vector for the argument. The zero-energy case follows directly from
the undivided inequality.

The exact second and third derivative identities are

```
e''_g = H''_g[Omega_g] + 2 Re H'_g[chi_g,Omega_g],
e'''_g = H'''_g[Omega_g]
       + 6 Re H''_g[chi_g,Omega_g]
       + 6 (H'_g-e'_g)[chi_g].                            (R5)
```

For completeness, the third identity follows by differentiating the second,
using the differentiated ground equation
`L_g Omega''_g = -(H''_g-e''_g)Omega_g - 2(H'_g-e'_g)chi_g`,
and the normalization identity `<Omega''_g,Omega_g>=-||chi_g||^2`.
Thus (R5) includes the normalization term; discarding it gives the wrong
third derivative.

Let `h=1+E/gamma` and define finite constants

```
E1 = 2 E,
E2 = E (6 + 8 h),
E3 = E [24 + 72 h + 48 h (1+2E/gamma)].                   (R6)
```

Then

```
|e_g^(j)| <= E_j g^-j,  j=1,2,3.                         (R7)
```

Proof: the second derivative uses `|H''[Omega]| <= 6e/g^2` and
`2|H'[chi,Omega]| <= 8 e h_g/g^2`. For the third derivative, its three
terms have absolute bounds `24e/g^3`, `72e h_g/g^3`, and
`48e h_g(1+2e/gamma)/g^3`, respectively. For the last one use
`|(H'-e')[chi]| <= (2/g)(1+2e/gamma)L[chi]`, followed by (R4).

It follows, on the actual vacuum complement, that

```
|L_g^(j)[u,v]|
 <= [a_j h + E_j/gamma] g^-j sqrt(L_g[u] L_g[v]).          (R8)
```

This discharges the raw operator and vacuum-energy part of the requested
inverse-power derivative budget. It sharpens the original C5-C9 route, which
used a fixed ordinary H1 norm and incurred avoidable inverse powers from the
comparison with the physical energy. It does not yet differentiate a moving
source-compatible pullback.

### All three actual-ground jets also have the corresponding energy bounds

This same argument controls the vacuum transport jets, rather than leaving
their higher derivatives as additional assumptions. Put `q_g=H_g+gamma I`,
`kappa=2+E/gamma`, `v_j=a_j+E_j/gamma`, and `D0=sqrt(E+gamma)`.
For n=1,2,3 recursively define

```
D_n = kappa sum_(j=1..n) binom(n,j) v_j D_(n-j)
    + D0/(2 gamma) sum_(i=1..n-1) binom(n,i) D_i D_(n-i). (R8a)
```

Then `||Omega_g^(n)||_(q_g) <= D_n g^-n` for n=0,1,2,3.
Indeed, differentiation of `L_g Omega_g=0` gives
`L_g Omega_g^(n)=-sum_(j=1..n) binom(n,j)L_g^(j)Omega_g^(n-j)`.
On the vacuum complement `q_g<=kappa L_g`, so the reduced inverse maps
a q_g-form functional of norm F into a vector of q_g norm at most kappa F.
R2/R7 bound the displayed forcing by the first sum in R8a.
The remaining vacuum component is determined exactly by

```
<Omega_g^(n),Omega_g>
 = -(1/2) sum_(i=1..n-1) binom(n,i)
                           <Omega_g^(i),Omega_g^(n-i)>.
```

Use `q_g>=gamma I` and the induction hypothesis to bound this component by
the second sum. This proves R8a; the normalization sum is empty for n=1.
This is not an estimate obtained by differentiating the first-jet asymptotic.

In particular, the vacuum-only skew generator

```
A_vac(g)=|Omega'_g><Omega_g|-|Omega_g><Omega'_g|
```

obeys explicit energy-operator estimates through its second derivative:

```
||A_vac^(r)(g)||_(q_g -> q_g)
 <= [2/gamma sum_(i=0..r) binom(r,i) D_(i+1)D_(r-i)]
                                                  g^(-r-1), r=0,1,2. (R8b)
```

For a rank-one map `|u><v|`, its q_g operator norm is at most
`||u||_q ||v||_q/gamma`; Leibniz differentiation proves R8b.
These bounds certify the vacuum-only generator, not the complete conditional
source generator in R9. One may alternatively first transport the vacuum by
A_vac, conjugate the actual P_g by that unitary, and then apply Kato transport
to the conjugated source projections: those projections contain the fixed
vacuum, so their Kato generator fixes it. Such a consistently specified chart
still requires the energy bounds on the source projection derivatives.

## 4. An explicit bridge from the actual transport generator to M1,M2,M3

Use the complete source/vacuum transport from C2. Its base-independent
skew-adjoint generator, as already derived in the subdivision source S2, is

```
A(g) = [P'_g,P_g] + |nu_g><Omega_g| - |Omega_g><nu_g|,
nu_g = Omega'_g - [P'_g,P_g]Omega_g,
partial_g R(g,s) = A(g) R(g,s).                            (R9)
```

To avoid a degenerate norm on vacuum components of derivatives of R, set
`q_g[u]=H_g[u]+gamma||u||^2`. The following is a **sufficient model estimate**,
not an already established consequence of the Hardy bound:

```
||A^(r)(g)||_(q_g -> q_g) <= d_r g^(-r-1),  r=0,1,2,      (R10)
```

where the norms refer to the same fixed compact form domain. Suppose R10
holds for finite nonnegative `d0,d1,d2`. On a local interval `s/2 <= t <= s`,
differentiation of `q_t[R(t,s)u]`, R2, and R10 give

```
|partial_t q_t[R(t,s)u]| <= (2+2d0) q_t[R(t,s)u]/t.
```

Gronwall, in either direction, therefore proves
`||R(t,s)||_(q_s -> q_t) <= N = 2^(1+d0)`.
Differentiating the ODE twice gives

```
R'   = A R,
R''  = (A' + A^2)R,
R''' = (A'' + 2A'A + AA' + A^3)R.
```

In particular, if

```
r0=1, r1=d0, r2=d1+d0^2, r3=d2+3d0*d1+d0^3,
```

then `||R^(j)(t,s)||_(q_s -> q_t) <= N r_j t^-j` for j=0,1,2,3.

Now let `l_t[u,v]=L_t[R(t,s)u,R(t,s)v]`, exactly as in C4.
Set `v0=1`, `v_j=a_j+E_j/gamma` for j=1,2,3. The estimate
`|L_t^(j)[u,v]| <= v_j t^-j sqrt(q_t[u]q_t[v])` follows from R2/R7;
for j=0 it uses `0<=L_t<=H_t<=q_t`. Leibniz's formula then proves

```
p1 = v1 + 2 r1,
p2 = v2 + 4 v1 r1 + 2(r1^2+r2),
p3 = v3 + 6 v2 r1 + 6 v1(r1^2+r2) + 2(3r1*r2+r3),

|l_t^(j)[u,v]| <= N^2 p_j (2/s)^j sqrt(q_s[u]q_s[v]).      (R11)
```

For `u,v` perpendicular to `Omega_s`,
`q_s <= (2+E/gamma) l_s`. With the same spectral window and `c_Z` as C9,
`l_s <= c_Z k_s`. Hence the exact derivative constants required by C10 can be
chosen as

```
M_j(s) <= c_j s^-j,
c_j = c_Z (2+E/gamma) N^2 2^j p_j,  j=1,2,3.             (R12)
```

Every derivative in R11 includes source motion on both arguments, vacuum
subtraction, and the full electric/magnetic form. This is a sufficient
all-energy bridge to C14-C20, not a statement limited to first source jets.

## 5. What the Hardy estimate supplies, and the remaining precise estimate

The prior W6 source estimate and a uniform `mathfrak B_g` give

```
||I'_g f||_L2^2 <= (8 mathfrak B_g + 4 Kbar_g/gamma) b_g[f]
```

for centered finite-energy sources in the dilation-adjusted conditional chart.
That is the off-source conditional-frame derivative, after the indicated
unitary coordinate change. It is a useful actual all-source bound. It does
not bound the spatial derivatives of that vector, the full fast-to-fast action
of A, or A' and A'' in q_g. The required spatial conditional moments are
displayed exactly in C8a-C8c of compact_residual; higher parameter derivatives
have the same rank-one structure.

The logical distinction is concrete. In an abstract energy scale take a
unit source p with energy 1 and fast vectors q_n with energy n^2. The map
`D_n p=q_n` has source-energy-to-L2 norm 1 for every n, but
source-energy-to-energy norm n. Its skew extension
`A_n=|q_n><p|-|p><q_n|` has the same divergent energy-operator norm.
Thus a first source derivative into L2 cannot alone imply R10; the missing
energy regularity has a precise mathematical role rather than being a
bookkeeping convention. This example is a norm implication test, not a
counterexample to the actual Wilson source estimate.

The remaining sufficient real-model estimate for this route is R10 for the
actual R9 generator (or a weaker direct proof of the mixed form bounds R11).
The raw H derivatives and ground-energy subtraction need not be reproved:
R1-R8 already provide their inverse-power scaling on the actual square.
The stronger dilated-ground estimate Q12 remains useful to bound the vacuum
part sharply. Its averaged norm is not silently upgraded to all conditional
spatial moments.

If a different, dilation-adjusted source transport is selected, the transformed
operator and its covariant derivatives must be used consistently. R1-R8 refer
to the untransported compact Hamiltonian, and R9-R12 to the specified C2
transport. Identifying their jets with a CDF chart or Gaussian K1/K2 remains
a separate statement.

## 6. Source energies, subdivision, interacting grids, and the physical clock

Once R10 is established, R12 supplies the exact input used by the existing
subdivision theorem. On the prescribed endpoints `g_n=sqrt(kappa/n)`, its
source energy factor is

```
G_n = ((n+1)/n0)^(c1/2),
|E_n[p]| <= A_* G_n/(n^3 m_n^2) b_initial[p],              (R13)
```

where m_n is the number of substeps and A_* is the explicit cubic constant
there. Choosing `m_n^2 >= G_n` makes this composite coupling-error series
summable for every finite c1. It approximates a sum of local jets; it does
not automatically equal the original endpoint Taylor polynomial.

There is one additional factor when these errors are used in physical time.
If the physical generator at stage n is `S_n/tau_n`, `tau_n>0`, then in a
common source chart its exact increment is

```
S_(n+1)/tau_(n+1) - S_n/tau_n
 = (S_(n+1)-S_n)/tau_(n+1)
   + (1/tau_(n+1)-1/tau_n) S_n.                           (R14)
```

The second term is not a coupling Taylor remainder. For local errors in the
first term, the sufficient subdivision choice becomes

```
m_n^2 >= G_n/tau_(n+1),
sum_n |E_n^physical[p]| <= A_* sum_n n^-3 b_initial[p].    (R15)
```

One may use `max(1,G_n/tau_(n+1))` before taking the square root and ceiling.
For exponentially small tau this may require exponentially many substeps;
R15 is an analytic error-budget fact, not an efficiency claim. It also does
not prove convergence of the exact jets or control the explicit clock-change
term in R14.

For a change of grid or block identification, write in addition the actual
matching discrepancy after the prescribed injection, including every source
energy comparison factor. That discrepancy is distinct from E_n. A bound on
the latter cannot set the former to zero. The Gaussian grid theorem supplies
`F_(0,Lambda)>=1/sqrt(2)` with the actual covariance-weighted source and shared
edges. Its interacting counterpart and the coarse-theory identification are
still necessary for the spatial-continuum use of this argument.

There is a further visible volume dependence already in this new proof:
E bounds the ground energy of the entire compact system. On growing grids it
is generally extensive, so R6/R12 do not produce volume-independent constants
by themselves. A linked/local centered-energy estimate must replace that
global E dependence, together with the interacting fast-floor and source
transport estimates. A fixed-square physical gap must not be used as a
uniform growing-volume full gap merely because the Gaussian fast compression
has a uniform floor.

## 7. Consequence and verification boundary

Hypothesis discharged: untransported actual compact electric/magnetic and
vacuum-energy derivatives through order three satisfy the required inverse
powers in the actual energy norm, uniformly toward zero coupling on the fixed
square. Downstream: the complete C19 residual constants follow with explicit
c_j from the specified source-transport energy-jet bound R10. Remaining:
prove that bound (or its exact mixed-form substitute) for the actual quantum
source, then obtain the interacting grid and physical matching/clock inputs.

[residual_verify.py](residual_verify.py) checks the coefficient arithmetic,
the noncommuting 2x2 ground derivative identity including its normalization
term, the Leibniz coefficients, and the clock identity with exact rational
arithmetic. Its output is [residual_checks.json](residual_checks.json).
These finite controls are not a machine proof of compact elliptic regularity,
of R10 for Wilson theory, or of an interacting continuum theorem. The operator
argument R1-R12 is analytic; no new Lean theorem is claimed here.

The 15 exact controls passed on 10 September 2026 using the bundled Python
runtime. The output pins the exact bytes of this note and its checking script.
An independent mathematical review checked R3-R8, the ground-jet recursion
R8a, the vacuum generator bound R8b, and the R9-R12 Leibniz and energy factors;
it found no missing term. This review does not assert the remaining R10
estimate for the actual conditional source generator.
