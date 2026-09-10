# Transverse confinement in Simon's finite-dimensional Yang–Mills model

Date: 2026-09-08. Source ID: `SIMON_1983_DISCRETE`. Related gaps: G22 and G23.

For the explicitly normalized SU(2) matrix Hamiltonian

\[
 H_m(g)=-\sum_{i=1}^m\Delta_{A_i}
       +g^2\sum_{i<j}|A_i\times A_j|^2,
 \qquad A_i\in\mathbb R^3,\quad m\ge2,\quad g>0,
 \tag{1}
\]

the transverse-oscillator argument below gives the quadratic-form bound

\[
 \boxed{H_m(g)\ \ge\ -\frac12\sum_i\Delta_{A_i}
                  +g\sqrt{m-1}\sum_i|A_i|.}
 \tag{2}
\]

Consequently its Friedrichs realization has compact resolvent. An elementary
Hardy completion also gives the explicit lower bound

\[
 \boxed{E_0(H_m(g))\ \ge\
       3m\left(\frac{g^2(m-1)}{32}\right)^{1/3}.}
 \tag{3}
\]

Equation (3) bounds the energy before subtraction of the vacuum energy. A
lower bound for the physical difference `E1 - E0` requires a separate argument.
The exact algebra supporting (2) and (3) is checked in
[`ym_flat_directions.py`](../../src/workhouse/invariants/ym_flat_directions.py).
The integration, density, form-closure, compactness and spectral arguments
given below are analytic derivations; the symbolic checks do not make them
Lean theorems or prove a four-dimensional field-theory statement.

## Source and prior work

Barry Simon, *Some Quantum Operators with Discrete Spectrum but Classically
Continuous Spectrum*, Annals of Physics **146** (1983), 209–220,
[DOI 10.1016/0003-4916(83)90057-X](https://doi.org/10.1016/0003-4916(83)90057-X),
[author-hosted original scan](https://math.caltech.edu/SimonPapers/158.pdf).
The unmodified local scan is
`literature/inbox/JW_2006/sources/ref43.pdf`; SHA256 is
`df9c5af529ad41ed92a78d848a6ffaafb7e85f4cbb6f788a55a03ab76e57dcb7`.
The accession and access record are in
[`sources_26_50.json`](../../literature/yangmills/sources_26_50.json), reference 43.

| Locator | Material used here |
|---|---|
| Printed p.210, equation (1); PDF p.2 | Scalar model `-Delta + x^2 y^2` and five confinement proofs |
| Printed p.211, equation (3); PDF p.3 | Compact semisimple Lie-algebra matrix model, at least two matrices |
| Printed pp.211–212, section 2 and equation (5); PDF pp.3–4 | Oscillator lower bound and retained half-Laplacian |
| Printed pp.216–217, Theorem 3 and Corollary 4; PDF pp.8–9 | Derivatives of quadratic commutator components and discrete matrix spectrum |
| Printed p.220, note added in proof; PDF p.12 | Rellich's earlier work and confinement from growing transverse slice energies |

The scanned equations on printed pp.211–212 were visually checked because
text extraction drops their constants. Simon proves the general matrix
discreteness result through the Fefferman–Phong criterion. Here the SU(2)
case is reconstructed directly by oscillator slices, with a specific allocation
that retains kinetic energy in every variable. Neither the confinement
mechanism nor the matrix discreteness theorem is claimed as new literature.
The explicit coefficient allocation and Hardy bound are calculations developed
here from these definitions; publication priority for those constants has not
been established.

Before deriving them, `workhouse why G22` and `workhouse why G23` were read.
Targeted searches for Simon, `x^2 y^2`, transverse oscillators, and `27/32` in
the invariant modules, theory, imported corpus and notes found the existing
literature graph and G22/G23 checks but no matching derivation. The existing
failure of the six-versus-three Cartan argument and the failed diffusion-to-OS
identification remain applicable constraints.

## Definitions and normalization

In (1), `T = -sum Delta_Ai` and
`V = g^2 sum_(i<j) |Ai cross Aj|^2`, so `H = T + V`.
The number `m` counts matrices; it is neither the color rank nor lattice volume.
The real coordinates use the SU(2) bracket
`[e_a,e_b] = epsilon_abc e_c` and Euclidean inner product. Equivalently one
can use `T_a = -i sigma_a/2` with `-2 Tr(T_a T_b) = delta_ab`.

Simon chooses the negative Killing metric for his kinetic term and a trace
in a faithful matrix representation for the potential. Those conventions
give positive constant multiples of the Euclidean kinetic and quartic terms
in (1); the constants must be translated before importing a numerical bound.
For a model `a T + b sum |Ai cross Aj|^2`, with `a,b>0`, apply this note to
`a H_m(sqrt(b/a))`. In particular its ground-energy lower bound is

\[
 3m\left(\frac{a^2 b(m-1)}{32}\right)^{1/3}.
 \tag{4}
\]

We start on `C_c^infinity(R^(3m))`, use the nonnegative quadratic form and
then take its Friedrichs closure. All form inequalities use the same Hilbert
space and this common smooth core. No gauge fixing or quotient measure is
introduced in this argument.

## 1. The scalar oscillator, including its constant

For `A,B>0` and smooth compactly supported real `u`, integration by parts gives

\[
 \int\left(A^2|u'|^2+B^2q^2|u|^2-AB|u|^2\right)dq
   =\int|Au'+Bqu|^2dq\ge0.
 \tag{5}
\]

The pointwise difference is a total derivative:

\[
 A^2|u'|^2+B^2q^2|u|^2-AB|u|^2
 =|Au'+Bqu|^2-AB(q|u|^2)'.
\]

For complex `u`, apply the real identity to its real and imaginary parts.
The Gaussian `exp(-B q^2/(2A))` solves the equality equation and has
eigenvalue `AB`. Thus the oscillator lower constant is exact. At zero
frequency the bound is zero, the infimum of the free Laplacian; there is no
normalizable Gaussian ground state in that direction.

For Simon's scalar operator `H = T_x + T_y + x^2 y^2`, first hold `y` fixed
to obtain `T_x + x^2 y^2 >= |y|`, and then exchange `x,y`. The allocation

\[
 H=\tfrac12(T_x+x^2y^2)+\tfrac12(T_y+x^2y^2)
                         +\tfrac12(T_x+T_y)
 \ge\tfrac12(T_x+T_y+|x|+|y|)
 \tag{6}
\]

is Simon's equation (5). The retained kinetic term is essential: a multiplication
operator by a function growing at infinity does not itself have compact
resolvent on a continuous configuration space.

## 2. SU(2) has two transverse oscillator modes per slice

For a fixed `x in R^3`,

\[
 |x\times y|^2=y^T M_x y,\qquad M_x=|x|^2I-xx^T.
\]

The identities `M_x x = 0`, `M_x^2 = |x|^2 M_x`, and

\[
 \det(\lambda I-M_x)=\lambda(\lambda-|x|^2)^2
 \tag{7}
\]

show that orthogonal coordinates split the slice into two oscillators of
frequency `sqrt(c)|x|` and one free longitudinal direction. Therefore

\[
 -\Delta_y+c|x\times y|^2\ \ge\ 2\sqrt c\,|x|,
 \qquad c\ge0.
 \tag{8}
\]

This is a bound on the bottom of the slice spectrum. The slice itself still
has a free direction and has no isolated ground eigenvalue. Applying (8)
by Fubini to a smooth compactly supported function of all matrices is valid;
one does not differentiate any coordinate rotation depending on `x`.

## 3. Allocate the pair potential without losing longitudinal control

Put `n=m-1>0` and, for every `i`, define

\[
 K_i=\sum_{j\ne i}\left[-\Delta_{A_j}
                      +n g^2|A_i\times A_j|^2\right].
 \tag{9}
\]

For fixed `A_i`, each of the `n` terms has the lower bound from (8):

\[
 K_i\ \ge\ 2g n^{3/2}|A_i|.
 \tag{10}
\]

In `sum_i K_i`, a kinetic term occurs `n` times, and an unordered pair
potential occurs twice with coefficient `n`. Hence the exact identity is

\[
 \sum_iK_i=nT+2nV,\qquad
 H=\frac12T+\frac1{2n}\sum_iK_i.
 \tag{11}
\]

Combining (10) and (11) proves (2). It retains all longitudinal derivatives;
the slice-by-slice free directions cannot survive simultaneously without
paying the growing zero-point cost in the other slices.

A useful parameterized version, derived by the same counting with
`0<theta<1`, is

\[
 H\ge\theta T+g\sqrt{2n(1-\theta)}\sum_i|A_i|.
 \tag{12}
\]

To obtain it use
`K_i(theta)=sum_(j!=i)[-Delta_j+n g^2/(2(1-theta)) |Ai cross Aj|^2]`
and coefficient `(1-theta)/n`. With the Hardy step below, the cubed
ground-energy lower constant is proportional to `theta(1-theta)`, so
`theta=1/2` maximizes that particular bound. This optimization concerns
this comparison family, not the exact ground energy.

## 4. Compact resolvent follows from the retained gradient and radial tail

Let `k=g sqrt(n)>0` and `R(A)=sum_i |A_i|`. For a family with bounded
`q_H[psi]+||psi||_2^2`, (2) controls its full `H^1` norm and gives

\[
 \int_{R(A)>L}|\psi(A)|^2dA\le\frac{q_H[\psi]}{kL}.
 \tag{13}
\]

For each fixed `L`, the set `{R(A)<=L}` is bounded. Rellich compactness on
a containing ball supplies local `L^2` subsequences; (13) makes their tails
uniformly small as `L` grows. A diagonal argument yields compact embedding
of the closed form domain into `L^2`, hence compact resolvent of the
Friedrichs operator. This reconstructs the compactness mechanism, rather
than identifying confinement with a pointwise force estimate.

The hypotheses matter. For `m=1` or `g=0` the model is free and the proof's
positive radial coefficient disappears. Every statement here keeps finite
`m`; no infinite-dimensional compactness assertion follows from these steps.

## 5. An explicit ground-energy lower bound

For `x in R^3` away from zero let `b(x)=x/(2|x|^2)`. Direct differentiation gives

\[
 \operatorname{div}b=\frac1{2|x|^2},\qquad |b|^2=\frac1{4|x|^2}.
\]

Consequently

\[
 \int|\nabla u+bu|^2
    =\int|\nabla u|^2-\frac14\int\frac{|u|^2}{|x|^2}\ge0.
 \tag{14}
\]

Initially use smooth functions supported away from zero. The usual radial
cutoff extends (14) to the full smooth core: in three dimensions the added
gradient energy for cutting out a ball of radius `epsilon` is `O(epsilon)`
for bounded smooth `u`; then pass to the form closure. Apply (14) to each
`A_i` variable by Fubini. Equation (2) now implies

\[
 H\ge\sum_i\left(\frac1{8|A_i|^2}+k|A_i|\right).
 \tag{15}
\]

The remaining minimum has an exact sum-of-squares certificate. Set
`s=(4k)^(-1/3)` and `r=sz`. For `z>0`,

\[
 \frac1{8r^2}+kr-\frac3{8s^2}
    =\frac{(z-1)^2(2z+1)}{8s^2z^2}\ge0.
 \tag{16}
\]

The minimum is reached at `z=1`, and its cube is `(27/32)k^2`.
Summing (16) proves (3). With coefficient `theta` in (12), Hardy instead
gives a minimum whose cube is `(27/16)theta k_theta^2`, namely
`(27/8)g^2 n theta(1-theta)`. The identity
`theta(1-theta)=1/4-(theta-1/2)^2` explains the choice in (2).

## 6. What Simon's Jacobian condition measures

Write the components of the pair commutators as quadratic polynomials
`Q_(ij,a)(A)=(Ai cross Aj)_a`, so `V/g^2=sum Q^2`. For one pair,

\[
 \|D(x\times y)\|_F^2=2(|x|^2+|y|^2).
\]

Every matrix occurs in `m-1` pairs, giving the all-matrix identity

\[
 \boxed{\sum_{i<j,a,k,b}
   |\partial_{A_{k,b}}Q_{ij,a}|^2
       =2(m-1)\sum_i|A_i|^2.}
 \tag{17}
\]

This verifies Simon's Theorem 3 derivative nondegeneracy for SU(2), with
an explicit constant in the convention (1). It concerns `DQ`. It does
not say that `grad V` is nonzero. Indeed, at every commuting configuration
`Ai=a_i e3`, all `Q` vanish and
`grad V=2g^2 sum Q grad Q=0`, while the right side of (17) is positive
away from the origin. Confusing the two derivatives would erase the very
mechanism the source is exhibiting.

One can see the growing normal stiffness exactly. Write transverse
perturbations as `ui=(u_i,v_i,0)`, put `a=(a_i)` and `rho^2=sum a_i^2`.
The quadratic part of the potential divided by `g^2` is

\[
 \sum_{i<j}|a_i u_j-a_j u_i|^2
 =\rho^2\sum_i|u_i|^2-\left|\sum_i a_i u_i\right|^2.
 \tag{18}
\]

To derive (18), expand every pair, collect each `|u_i|^2` with coefficient
`sum_(j!=i) a_j^2`, and complete `|sum_i a_i u_i|^2`. For each of the two
transverse coordinate directions the matrix is `M=rho^2 I-aa^T`, satisfying
`M a=0` and `M^2=rho^2 M`. Thus when `rho>0`, the transverse Hessian of
`V` has eigenvalue `2g^2 rho^2` with multiplicity `2(m-1)` and two zero
modes corresponding to common rotations. The `m` longitudinal Cartan
directions also have zero Hessian. For three matrices the exact symbolic
check expands (18) and the complete six-dimensional transverse Hessian.

This calculation identifies normal oscillators even though the classical
force vanishes on the valley. The global estimate (2), unlike the Hessian
expansion alone, already controls configurations away from that expansion.

## 7. Energy scale, vacuum subtraction and the research gaps

The potential in (1) is homogeneous of degree four. Under the unitary
dilation `A=g^(-1/3) B`,

\[
 H_m(g)\simeq g^{2/3}H_m(1).
 \tag{19}
\]

Therefore each eigenvalue, and each difference between eigenvalues, scales
as `g^(2/3)` at fixed `m`. The bound (3) has exactly this scaling. Compact
resolvent alone does not furnish a gap uniform as `g` tends to zero.

For this connected Euclidean configuration space, the scalar polynomial
potential gives a positivity-improving heat semigroup by the Feynman–Kac
formula. Combined with compactness, the standard positive-ground-state
argument gives a simple lowest eigenvalue and hence a strictly positive
`E1-E0` for fixed `m,g`. This is an analytic finite-dimensional consequence;
its numerical value is not established by (3). A quantitative gap estimate
would need, for example, a lower bound on `E1` together with an independent
upper bound on `E0`, or a ground-state-weighted Poincare estimate.

The simultaneous SU(2) action preserves both terms of (1). Restriction to
its invariant closed subspace preserves the form lower bound and compact
resolvent. This observation does not identify that subspace or its operator
with the repository's lattice transfer operator.

For G22, the useful result is the explicit transverse mechanism and the
distinction between `DQ`, `Hess V` and `grad V`. The commuting configurations
used in (17) are Cartan aligned and have zero commutator energy; they are
outside the rough, nonaligned region in the actual G22 conjecture. They
neither prove nor refute that conjecture. To use the mechanism there, the
local Wilson operator, kinetic metric, pair couplings, localization errors
and volume dependence must first be identified under one convention.

For G23, (1) supplies a concrete selfadjoint operator whose compactness and
coupling scale can be derived. It supplies no identification of a diffusion
generator with a physical transfer Hamiltonian, no four-dimensional OS
reconstruction and no regulator-independent field-theory mass gap. The
existing Gaussian counterexample to the naive diffusion-to-OS bridge remains
untouched. A comparison of models must specify the vacuum subtraction and
the operator map, not just compare positive constants.

## Verification and exact dependencies

All nine checks use exact symbolic arithmetic. Their detailed outputs state the analytic
inputs separately. The names below are the exact registry names.

| Check | Registered dependencies |
|---|---|
| `YM flat directions: oscillator square completion fixes the zero-point constant` | None |
| `YM flat directions: Simon's scalar split retains half the Laplacian` | Oscillator square completion |
| `YM flat directions: SU(2) slice has two transverse modes` | Oscillator square completion |
| `YM flat directions: commutator Jacobian is coercive while the force vanishes` | None |
| `YM flat directions: commuting-valley Hessian is a Gram projector` | Commutator Jacobian; SU(2) slice |
| `YM flat directions: balanced slice aggregation retains half the kinetic energy` | SU(2) slice |
| `YM flat directions: three-dimensional Hardy completion has coefficient 1/4` | None |
| `YM flat directions: radial lower-bound minimum has cube 27/32` | Hardy completion; balanced slice aggregation |
| `YM flat directions: quartic coupling dilation scales energies as g^(2/3)` | None |

Standalone reproduction from the repository root:

```powershell
$env:PYTHONPATH = 'src'
.venv\Scripts\python.exe -X utf8 -c "from workhouse.invariants.ym_flat_directions import ym_flat_directions; rs=ym_flat_directions.run(); [print(r.passed,r.name,r.detail) for r in rs]; raise SystemExit(not all(r.passed for r in rs))"
```

The nine exact checks passed on 2026-09-08 and are registered in the native
invariant and theory graph pipeline. The balanced aggregation check also has
a complete Lean mapping. The finite valley identity and radial comparison
have compiled Lean lemmas for their algebra; those lemmas do not formalize
the analytic oscillator, Hardy or compactness arguments. See
[the formal bridge note](yangmills-formal-bridges.md) for the exact scope.
