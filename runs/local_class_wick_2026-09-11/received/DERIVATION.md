# A rank-uniform continuation of the local SU(N) class spectrum

Date: 2026-09-11. Author of this continuation: Codex, building on the user's
archived one-plaquette derivations and exact covariance convention.

## Result and scope

The archived local spectrum admits a finite exact recursion at every perturbative
order, with coefficients in the Laurent ring Q[N,N^-1]. The recursion needs no
Gram-matrix inversion and specializes directly through the small-rank trace
identities. It applies to the vacuum, the first charge-even shell for N>=2,
and the first charge-odd shell for N>=3.

This calculation independently recovers the archived c0, c1 and c2 formulas
in both sectors, and the archived all-rank c3+ formula. It additionally derives
the explicit c3- and both all-rank c4 formulas below. The actual certificate includes full polynomial
eigen-equation residuals, not just agreement with those constants.

The statements proved here concern the formal local Wilson oscillator expansion.
A new error bound for the compact-group eigenvalues is not claimed. Local
spectral coefficients also do not by themselves identify the interacting Wilson
spectrum or a continuum source measure.

## 1. The exact algebra

Let X be a traceless Hermitian N by N matrix with density proportional to
exp(-Tr(X^2)), and write P_k=Tr(X^k), P_0=N, P_1=0. Its covariance is

    E[X_ab X_cd] = (delta_ad delta_bc - delta_ab delta_cd/N)/2.

Use a traceless Hermitian basis normalized by Tr(T_a T_b)=delta_ab.
Let D=Delta/2 be half the Euclidean Laplacian and E be the polynomial Euler
operator. The completeness identity for this basis gives

    D P_k = (k/2) sum_(l=0)^(k-2) P_l P_(k-2-l)
            - k(k-1) P_(k-2)/(2N),

    D(fg) = (Df)g + f(Dg) + grad(f) dot grad(g),

    grad(P_k) dot grad(P_l)
        = k l (P_(k+l-2) - P_(k-1) P_(l-1)/N).

These identities follow by differentiating the trace and contracting the two
matrix insertions with the displayed completeness relation. They are exact for
every integer rank, including ranks at which some traces become dependent.

For a homogeneous polynomial F of positive degree d, Gaussian integration by
parts gives

    E_mu[F] = E_mu[D F]/d.

Together with E_mu[1]=1 and vanishing odd moments, this is a finite exact
moment recursion. The independent archive engine first uses full-GUE cut/join
and then subtracts the trace; the new engine applies D directly in traceless
coordinates.

## 2. A shell resolvent without singular Grams

Define L=E-D. Since [E,D]=-2D, the terminating exponential W=exp(-D/2) satisfies

    L W = W E.

If H_d denotes extraction of the homogeneous degree-d part, then

    Pi_d = exp(-D/2) H_d exp(D/2)

is the exact oscillator-shell projector. On each finite polynomial space,

    R_s = sum_(d != s) Pi_d/(s-d),

    (s-L) R_s = R_s(s-L) = 1-Pi_s.

Proof: apply the conjugation identity to each homogeneous component. The
exponentials terminate because D lowers degree by two. Different shells are
orthogonal under the Gaussian inner product since L is symmetric there.
No matrix inverse or rank-dependent spectral denominator occurs.

Any polynomial identity on traceless N by N matrices remains an identity after
differentiation, homogeneous extraction and these exponentials. Thus this
construction descends to the finite-rank trace quotient. In particular, one need
not incorrectly treat P4 as independent of P2^2 at N=3.

The simple initial states are

    psi_0 = 1,
    psi_2 = P2-(N^2-1)/2,
    psi_3 = P3.

Their squared norms are 1, (N^2-1)/2 and
3(N^2-1)(N^2-4)/(8N), respectively. The last vanishes at N=2, explaining the
excluded charge-odd branch. The degree-0, degree-2 and degree-3 invariant shells
each have multiplicity one whenever the corresponding state is nonzero.

## 3. All-order constructive theorem

Put g=sqrt(2N/beta). In the archive's normalization the formal gap Hamiltonian,
after the irrelevant common scalar is removed, is

    H_formal = g^-1 K(g),
    K(g) = L + sum_(j>=1) g^j V_j,
    V_j = (-1)^j P_(2j+2)/(2^j (2j+2)!).

In particular V1=-P4/48, V2=P6/2880 and V3=-P8/322560.
These constants follow directly by expanding the Wilson cosine with
theta=sqrt(g/2) X and beta/N=2/g^2. Multiplying H_formal by g explains the
power of g in K; these two series must not be confused.

For s in {0,2,3}, set psi_(s,0)=psi_s and e_(s,0)=s. At order r, define

    F_r = sum_(j=1)^r V_j psi_(s,r-j),
    Pi_s F_r = e_(s,r) psi_s,
    psi_(s,r) = R_s [F_r - sum_(j=1)^(r-1) e_(s,j) psi_(s,r-j)].

Then Pi_s psi_(s,r)=0 and the coefficient of every positive power of g in

    (K(g)-sum_r e_(s,r) g^r) sum_r psi_(s,r) g^r

vanishes. This follows by substituting the recurrence and the identity in
Section 2. Uniqueness follows order by order from the one-dimensional resonant
shell and invertibility on its complement.

Every operation belongs to Q[N,N^-1]. To see this without assuming cancellation
of a Gram determinant, compute e_(s,r) by taking the coefficient of P_s in the
degree-s part of exp(D/2)F_r (the constant coefficient for s=0).
That homogeneous part has only one possible invariant monomial. Thus no division
by N^2-1, N^2-4, or any other rank polynomial is needed at all.
The implementation also computes the Gaussian inner-product quotient; the
vanishing full resonant-shell residual checks its equivalence at each executed
order.

The degree bound deg psi_(s,r)<=s+4r follows by induction from
deg V_j=2j+2 and the fact that the shell resolvent never raises degree.
Consequently every fixed order is a finite computation, independently of rank.

This proves an all-order formal recursion and rationality theorem. It does not
assert convergence of the infinite perturbation series.

## 4. Recovered coefficients and the next odd term

Write a_(+,r)=e_(2,r)-e_(0,r) and a_(-,r)=e_(3,r)-e_(0,r). Then

    Delta_+ = 2/g + sum_(r>=1) a_(+,r) g^(r-1),
    Delta_- = 3/g + sum_(r>=1) a_(-,r) g^(r-1).

With the usual beta expansion, c_j=(2N)^(j/2) a_(j+1).
The source's c0 and c1 formulas are recovered exactly, including the SU(3)
angular contribution sqrt(6)/576 missed by the radial approximation.

The third-order gap coefficients reproduce the source:

    c2+ = -(60N^6-401N^4+1522N^2-2297)/(49152N^2),
    c2- = -(95N^6-981N^4+5853N^2-15335)/(49152N^2).

The next charge-odd coefficient derived here is

    c3-(N) =
      -sqrt(2N) (14267N^8-186257N^6+1596792N^4-8442260N^2+20165216)
      / (56623104 N^3).

At N=3 this is

    c3-(3) = -15674731 sqrt(6)/764411904.

The corresponding even coefficient exactly reproduces the archived formula:

    c3+(N) =
      -sqrt(2N) (2970N^8-27878N^6+166512N^4-546024N^2+734405)
      / (18874368 N^3).

The distinction in provenance matters: c2+/- and c3+ belong to the earlier
research; this work supplies a new independent reconstruction. No match for
the c3- numerator was found in the selected current source/paper directories
or the inspected origin/main source, paper, docs, ledger and one-plaquette
import paths. That bounded search is not a claim of publication novelty or
an exhaustive search of the entire research archive.


## 4.1 Fifth perturbative order: both all-rank c4 formulas

The next complete recurrence gives

    c4+(N) =
      -(204120N^10-2448353N^8+19880740N^6-101716794N^4
        +294734750N^2-362174143)/(4529848320 N^3),

    c4-(N) =
      -(329385N^10-4937377N^8+52194445N^6-403915341N^4
        +1985928205N^2-4449690457)/(4529848320 N^3).

These specialize exactly to the previously recorded SU(3) anchors

    c4+(3) = -56673445/1528823808,
    c4-(3) = -290599777/6115295232.

The full all-rank expressions were computed without interpolation or an assumed
coefficient shape. No exact-value match was found in the same bounded source
search described above. The source's SU(3) values are recovered prior results;
the present contribution is their all-rank derivation and reproducible engine.

## 4.2 Sign corollary

All five corrections c0 through c4 are strictly negative in the first even
branch for every N>=2, and in the first odd branch for every N>=3.

Proof: remove the minus sign and the strictly positive denominator from each
a_r. The numerator is a polynomial in z=N^2. After z=x+4 in the even sector,
or z=x+9 in the odd sector, every coefficient is strictly positive.
The exact positive coefficient lists are retained in validation_order5.json.
Thus each numerator is positive for x>=0. This proves the coefficient signs,
not a finite-beta bound on a remainder or the sign of an infinite series.

## 5. Independent verification

The new trace engine verifies the polynomial eigen-equation, intermediate
normalization and resonant-shell compatibility at every executed order.
coefficients_order4.json retains these checks and exact expressions.

independent_su3.py uses ordinary differentiation in two Cartesian coordinates,
not the trace Laplacian or trace-moment recursion. It multiplies by the Weyl
alternant x(x^2-3y^2), uses the three diagonal eigenvalue coordinates, and integrates
ordinary Gaussian monomials. It exactly reproduces both sector gaps through c3.
Its certificate is independent_su3.json.

verify_wick.py passed 87 checks, including independent full-GUE trace-subtraction
moments at ranks 2,3,4,5,7; fresh archived odd-sector coefficients; symbolic
agreement with the archived formulas; heat/projector identities; retention of
the angular term; the vanishing N=2 odd norm; and a separate one-variable SU(2)
calculation through c3. validation.json records their scope.

The order-five run retains all three polynomial checks for each of five orders
in each of the three initial shells: 45 passed exact residual/normalization/
compatibility assertions. The separate verify_order5.py passed 37 checks,
including independent SU(3) and SU(2) Cartesian reconstructions through c4,
both old SU(3) c4 anchors, reproducibility of the preceding order, and exact
positive-polynomial sign witnesses. Its certificate is validation_order5.json.

There is no Lean build or repository-tier promotion in this standalone campaign.

## 6. Consequence and next obligation

The missing/restricted-rank certificate problem is discharged for the recovered
coefficients by a rank-uniform construction. The local polynomial continuation
can now advance to any specified finite order without separately discovering and
filtering trace bases at each rank.

The next analytic obligation is to attach explicit remainder and localization
bounds to the compact-group eigenvalue branches, with their dependence on N.
Only after that can these coefficients give certified finite-beta enclosures.
Interacting volume control and the continuum source-transport obligations of
G19 are separate successors.

## Sources and preservation

Read source and hash details in provenance.json. The initial graph snapshot
was saved/matched with 611 recorded checks and zero checks executed by the
briefing; it is not the mathematical certificate for this calculation.

C: ran out of free space after the order-three algebra passed and before its
JSON certificate could be written. No successful order-three JSON was claimed.
The original script and start snapshot remain in
C:/WORKHOUSE/research/local_class_wick_20260911. Subsequent completed calculations
and this deliverable are saved in D:/WORKHOUSE-output/local_class_wick_20260911.
No archive files were deleted or modified.

