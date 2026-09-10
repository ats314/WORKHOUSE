# The full-space Gaussian test, its repair, and the precise remaining estimate

8 September 2026. This is the requested proof attempt following the completed
theory-graph update. It tests the spatial comparison against an actual compact
Wilson cell, repairs the failed hypothesis, and states the exact derivation
at which the present argument stops. It does not infer that Yang-Mills theory
is impossible or that other methods cannot establish the missing estimate.

## 1. The requirement in the supplied document

The supplied *Quantum Yang-Mills Theory*, Arthur Jaffe and Edward Witten,
has 14 pages, SHA-256
`3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`.
Its printed pages 6, 11 and 12 were both extracted and visually inspected.
The original attachment remains unchanged.

Page 6, Section 4, asks for a nontrivial theory on R4 for every compact simple
gauge group, with a positive mass gap and the stated axiomatic properties.
The requirement immediately relevant to the spatial passage is the following
exact text from page 11, Section 6.5:

> One must then verify the existence of limits of appropriate expectations of gauge-invariant observables as the lattice spacing tends to zero and as the volume tends to infinity.

Page 12, footnote 2, explicitly qualifies the use of compactness:

> We specifically exclude weak-existence (compactness) as the solution to the existence part of the Millennium problem, unless one also uses other techniques to establish properties of the limit (such as the existence of a mass gap and the axioms).

The calculation below addresses one sufficient route to those limits. An
isolated one-particle carrier is useful in that route, but is not an additional
requirement imposed on every possible solution: page 6 lists an isolated
one-particle state among extensions of the stated problem.

## 2. First attempted step: global relative Gaussian fast-form control

The [spatial Schur theorem](wilson-spatial-schur-excess.md), SP8, has a
sufficient smallness condition

    ||F_0^(-1/2)(F_g-F_0)F_0^(-1/2)|| <= c |g|.                    (W1)

Here the forms are already in their specified common physical source chart
and vacuum-subtracted, and F_0 is strictly positive on the fast space.
The theorem conditional on this assumption remains correct. The attempted
application tested here uses a Gaussian oscillator as a reference for the
**entire** fast space after retaining only finitely many source directions.

That application fails on an actual four-link SU(2) Wilson plaquette. Impose
all four vertex gauge transformations. The physical space is the class-function
space of its holonomy U. Each original link contributes the group Laplacian,
so in the conventions of the pinned finite-cell input the scaled operator is

    H_g = -2 g^2 Delta_SU2 + 2 g^(-2)(2-Re Tr U),       g=u^(-1/4)>0.

The spin-n/2 character, n=0,1,..., has electric energy n(n+2)/2 before the
factor g^2. For a direct check, in z=cos(r/2) the radial Laplacian is

    Delta = (1/4)(1-z^2) partial_z^2-(3/4)z partial_z,

and the character is the Chebyshev polynomial U_n(z). Its elementary
second-order differential equation gives this eigenvalue. The
character equation for all n follows by coefficient extraction from
`G(z,t)=(1-2zt+t^2)^(-1)`: direct differentiation gives
`(1-z^2)G_zz-3zG_z+t^2G_tt+3tG_t=0` as a rational identity.
The Haar class
measure is proportional to sqrt(1-z^2) dz; its first moment is zero.
Consequently 0<=2 g^(-2)(2-Re Tr U)<=8 g^(-2), and the constant trial vector
gives a vacuum energy e_g<=4 g^(-2).

Order eigenvalues starting at n=0 and counting multiplicity. Min-max gives

    lambda_n(H_g-e_g) >= (g^2/2)n(n+2)-4/g^2.                      (W2)

The physical harmonic reference for this cell is a three-dimensional radial
oscillator of frequency 2. After subtraction of its ground energy 3 its
eigenvalues are 4n, n=0,1,.... These normalizations keep the original four-link
electric metric; replacing it by one face Laplacian changes them incorrectly.

Now retain any finite rank r, containing the vacuum, and compare fast
compressions under any unitary identification for which the proposed form
inequality is meaningful. Finite-codimension interlacing gives

    lambda_n(F_g) >= (g^2/2)n(n+2)-4/g^2,
    lambda_n(F_0) <= 4(n+r).

If even an upper form bound F_g<=C F_0 held with finite C, min-max would force

    (g^2/2)n(n+2)-4/g^2 <= 4 C(n+r)          for every n.           (W3)

This is false for every fixed g>0 and finite C,r. One explicit proof chooses
integers k>=max(C,1), m>=1/g with 32 k m^2>=r, and n=32 k m^2. The left side
is at least (512 k^2-4)m^2; the right side is at most 256 k^2 m^2.
Their difference is strictly positive. At g=1/4, r=1, n=1024, (W2) is 32768,
whereas (1+1/4)4(n+r)=5125.

Thus (W1) cannot be justified for this complete Gaussian fast reference,
even at a fixed cell and fixed positive coupling. The failure is at high
representations, not in the already proved finite low-energy asymptotics.
This argument does not classify infinite-rank retained algebras and does
not refute (W1) for a different, genuinely compact reference. It refutes the
specific full-space Gaussian implementation just tested.

## 3. Repair: only compare inverses on the graph force

The exact square completion does not require the failed global bound. Work
at a real energy z below both full fast restrictions. Let R_g=(F_g-z)^(-1)
and R_0=(F_0-z)^(-1). Use the fixed reference graph J_z from SP1, and put

    d_g=H_g-H_0,              A_g=J_z* d_g J_z,
    r_g=Q d_g J_z.

For finite retained smooth vectors assume J_z p lies in the interacting form
domain and r_g is a Hilbert-space vector, or has the corresponding bounded
fast-form dual realization. The completed interacting fast square then gives

    S_g(z)-S_0(z)=A_g-r_g*R_g r_g.                                (W4)

Indeed write a vector as J_z p+q. The reference cross term is zero and the
remaining q-form is <q,(F_g-z)q>+2 Re<q,r_g p>. Its minimizer is -R_g r_g p.
This proof does not require equality of the complete Gaussian and compact
form domains. It requires the displayed graph vectors and minimizer to be
admissible in the interacting form domain.
For different form domains, define the residual first by the interacting
cross functional `(H_g-z)[q,J_z p]`. Its identification with `Q d_g J_z p`
is made on an admissible common core and must extend continuously to the
interacting fast form domain. One must not subtract forms on a vector on
which either form is undefined. The reference restriction to the graph
also has to be defined. These are hypotheses of (W4), not a constructed
unitary identification of the full compact and Gaussian problems.

Let b[p]=||B^(1/2)p||^2 be the intended retained energy weight on the
vacuum-orthogonal source domain. Suppose F_g-z>=f>0 and

    ||B^(-1/2)(A_g-g A_1-g^2 A_2)B^(-1/2)|| <= a_3 |g|^3,
    ||(r_g-g t_1)B^(-1/2)|| <= t_2 g^2,
    ||t_1 B^(-1/2)|| <= t_0,
    ||B^(-1/2)t_1*(R_g-R_0)t_1 B^(-1/2)|| <= c_sel |g|.           (W5)

Here t_1=Q W_1 J_z includes the complete dressed first jet, not just a
magnetic cubic. Set K_1=A_1 and K_2=A_2-t_1*R_0 t_1. Expanding the two
factors of r_g in (W4) proves

    ||B^(-1/2)(S_g-S_0-g K_1-g^2 K_2)B^(-1/2)||
       <= |g|^3 [a_3+(2t_0 t_2+g_0 t_2^2)/f+c_sel],  |g|<=g_0.

All three terms arise explicitly: direct remainder, the two force factors,
and the selected inverse variation. Thus the high-representation failure
of (W1) is not itself a stopping point; (W5) is a weaker sufficient route.

It can work when (W1) fails. On l2(N_positive), take F_0 e_n=n e_n and
F_g e_n=(n+g^2 n^2)e_n. The relative perturbation has unbounded eigenvalues
g^2 n. Nevertheless for every t in l2,

    0<=<t,(R_0-R_g)t>
       =g^2 sum_n |t_n|^2/(1+g^2 n)<=g^2||t||^2.

This is an infinite-dimensional example, proved by its exact diagonal
spectral expansion. The finite controls check its denominators independently.

## 4. Attempt to establish the repaired estimate for Wilson

There is one elementary order method. If F_g=F_0+g^2 V with V>=0 as closed
forms, then for t such that R_0 t lies in the V form domain,

    0<=<t,(R_0-R_g)t><=g^2 V[R_0 t].

The upper inequality follows by inserting R_0 t into the variational formula
for <t,R_g t>; the lower follows from form order. This supplies a genuine
selected-inverse estimate without global relative boundedness.

It does not apply to the required Wilson forms as stated. The actual local
Wilson expansion has negative quartic character contributions; for the
single exponential, 2 g^(-2)(2-2cos(r/2)) has a negative r^4 coefficient.
The full W_2 also includes electric metric, Haar, moving-source and vacuum
terms. Even positivity of a bare perturbation would not suffice after true
vacuum subtraction. For example H_0=diag(0,2), V=diag(100,0)>=0 and g=1/20
give vacuum energy 1/4 and an excited restriction F_g=7/4<2=F_0. Its inverse
4/7 exceeds 1/2. The attempted order direction has reversed.

The signed resolvent identity identifies what must replace that argument:

    <t,(R_g-R_0)t> = -d_g,QQ[R_0 t,R_g t],

with the compatible form-domain assumptions and the actual vacuum-subtracted
fast-form difference. The existing dynamic Gaussian theorem controls the
quadratic synthesis t*R_0 t for its stated localized cubic forces, using
R_0<=D_vertical^(-1). It gives neither the interacting vector R_g t nor the
signed form pairing on the right. It also bounds only part of the full force
Q W_1 J_z when the reference retained space does not reduce H_0.

A direct attempt using global reference-excitation moments introduces a
second identifiable failure. Take M independent qubits with

    omega=(1,g)/sqrt(1+g^2),   chi=(-g,1)/sqrt(1+g^2),
    H_M=sum_i (I-|omega><omega|)_i,
    psi_M=chi tensor omega^(tensor(M-1)),
    N_0=sum_i |1><1|_i,                 p=g^2/(1+g^2).

The true ground energy is zero, H_M psi_M=psi_M, and its exact reduced
inverse on psi_M is psi_M. Yet

    <N_0>_psi=1+(M-2)p,
    ||N_0 psi_M||^2=[1+(M-2)p]^2+M p(1-p).

These identities follow by multiplying the normalized two-by-two density
matrices, or by independent Bernoulli moments. For every fixed g>0 the second
quantity grows as M^2, although the exact selected inverse energy remains
one. Therefore a proof of (W5) by bounding global reference-number moments
of the interacting inverse vector is not volume-uniform even in this
noninteracting control. This is a counterexample to that proposed estimate,
not to the physical gap or to the Wilson model.

For these independent factors the repair is explicit: conjugate each factor
by the rotation taking |0> to omega. The transformed ground is the reference
vacuum and the transformed N_0 moment of the rooted excitation is one.
The existing Wilson additive-copy/local-gradient theorem makes precisely
this kind of cancellation usable in its actual product setting. Its proof
uses exact support orthogonality under the product ground marginal.
The coupled lattice does not have that product marginal; its corresponding
connected source/ground comparison has to be estimated, not replaced by the
independent-copy identity.

## 5. The exact point at which this argument cannot proceed

After the preceding repair, the unproved step is the following actual
interacting inequality, with the physical source identification, vacuum
subtraction and normalization included as above:

    sup_(finite spatial Lambda) sup_(p: b_Lambda[p]=1)
      |d_(g,Lambda),QQ[
          R_(0,Lambda) t_(1,Lambda)p,
          R_(g,Lambda) t_(1,Lambda)p]|
        <= C |g|,                                                 (W6)

for all `0<g<=g_0`, with C independent of g, Lambda and the required
retained-background range, uniformly over the spectral-energy interval
where the fast inverses and the transport comparison are required.
For full scale transport it must hold on the complete relevant retained
energy space, not just one selected trial state, with the high-retained
contribution controlled. The weight b must be comparable to the actual
normalized coarse energy above the vacuum, as specified after SP25.

I cannot establish (W6) for the actual coupled Wilson family from the
available proofs. More specifically, the Gaussian estimate controls the
first inverse vector, while the signed pairing with the **interacting**
inverse vector has no proved connected volume-independent bound here.
The attempted global relative comparison is contradicted by (W2)-(W3);
the positive-form shortcut fails after vacuum subtraction; and the attempted
global excitation-moment bound has the explicit spectator growth above.
The product repair works exactly but does not supply the missing coupled
ground/source estimate. An actual uniform lower floor for F_g and the direct
and source remainder estimates in (W5) are also required; they have not been
silently assumed to follow from the Gaussian floor.

This is a derivation wall for the present argument: the implication from
the established Gaussian/full-reference synthesis bound to (W6) is not
proved. Consequently the O(g^3) interacting comparison cannot be inserted
into the accumulated physical-gap/source budget, and this route has not
constructed the gauge-invariant expectation limits required by the exact
page-11 quotation above. No claim that those limits cannot exist follows.

The previously established fixed-spacing Wilson vacuum, complete shell and
temporal transport are unaffected. The conditional Schur theorems also
remain valid. The status of (W6) is open; the failed global Gaussian
implementation is a distinct, falsified attempt.

## Evidence and reproducibility

The native selected-inverse suite checks the actual SU(2) character kinetic
normalization, the exact spectral-growth witness, the selected-inverse
denominators, the vacuum-subtraction order reversal and the spectator moments.
The full character/min-max argument and conditional form reduction above
are analytic proofs. The finite controls do not formalize their quantifiers
or establish (W6).

Inputs consulted include the live G19 theory graph, the pinned spatial inputs,
and the September 5 actual localized-score, local-gradient-support and
ground-marginal-Schur notes in the autonomous checkout, pinned to commit
`4bf812428e0af51d1ffcda299b0d97b38b644926` by the
[validation record](../validation/wilson-selected-2026-09-08.json).
Their fixed-cell,
additive-copy and Gaussian scopes are retained in this argument.
