# Finite-coupling remainder for the actual square quantum ground

This converts the square's computed first ground coefficient into an
estimate for its actual compact quantum ground state. Constants concern
the fixed twelve-edge square and sufficiently small positive g.

## The concrete approximation

Use the based chord coordinates
\(U_i=\sqrt{1-|\theta_i|^2/4}\,I+i(\theta_i/2)\cdot\sigma\)
on a fixed neighborhood of the unique well. Write Haar measure there as
\(j(\theta)d\theta\). Choose a smooth simultaneous-rotation-invariant
cutoff chi supported inside this chart and equal to one near zero.
Let Omega be the normalized Gaussian ground, e0 its energy, and p1 the
explicit cubic in the preceding square source calculation:

\[
p_1=c(T_{012}+T_{013})+d(T_{023}+T_{123}),
\quad c=-\frac18+\frac{\sqrt6}{24},
\quad d=-\frac3{56}-\frac{\sqrt2}{56}+\frac{\sqrt6}{48}.
\]

The exact polynomial identity already checked against the original-edge
operator is

\[
(H_0-e_0)(p_1\Omega)+H_1\Omega=0,\qquad
\langle\Omega,p_1\Omega\rangle=0.
\tag{G1}
\]

Define an actual compact physical trial vector by

\[
\widetilde v_g(U)=g^{-6}j(\theta)^{-1/2}\chi(\theta)
\Omega(\theta/g)[1+g p_1(\theta/g)],
\qquad v_g=\widetilde v_g/\|\widetilde v_g\|.
\tag{G2}
\]

It is extended by zero outside the chart. Smooth cutoff makes it a
globally smooth physical vector. For every fixed N,
\(\|\widetilde v_g\|^2=1+g^2\|p_1\Omega\|^2+O(g^N)\),
because Gaussian tails control the cutoff and the linear term is odd.

## Operator remainder on this vector

After the exact Haar half-density conjugation and theta=gX scaling,
the original compact differential operator has first terms H0+gH1.
On the chart its smooth coefficient Taylor remainders obey bounds of
the following form when applied to a fixed Gaussian times a polynomial:

\[
\|(\widehat H_g-H_0-gH_1)f\|
\le Cg^2\sum_{|\alpha|\le2}
\|(1+|X|)^4\partial^\alpha f\|.
\tag{G3}
\]

Here the electric principal coefficient remainder is bounded by
Cg^2|X|^2, its drift remainder by Cg^2(1+|X|), and its scalar
half-density term by Cg^2. The potential has zero cubic coefficient in
these coordinates and its remainder after the quadratic term is bounded
by Cg^2|X|^4. All bounds follow from Taylor's formula on a fixed smaller
chart; their constants do not depend on g.

Apply this to f=Omega and f=p1 Omega. The derivatives in the commutator
with chi(gX) are supported at |X|>=c/g; all resulting polynomial powers
of g and X are dominated by the Gaussian tail. Thus their norms are
O(g^N) for every fixed N. Using (G1) cancels the order-g term exactly,
and gives the actual compact residual estimate

\[
\boxed{\|(H_g-e_0)v_g\|\le Cg^2.}
\tag{G4}
\]

This calculation keeps the shared electric metric, Haar density and
true first ground coefficient. It does not replace the ground by a
classical Gibbs weight.

## Resolving the actual ground error

The previous compact quantum min-max proof establishes that the first
physical eigenvalue tends to e0 and the next one to e0+2sqrt(2).
For sufficiently small g, the only physical eigenvalue within distance
one of e0 is therefore the true ground energy eg. Equation (G4), the
spectral theorem and ||v_g||=1 imply

\[
|e_g-e_0|\le Cg^2.
\tag{G5}
\]

Let Pi_g be the true ground projection and r_g=(H_g-e0)v_g. On its
physical orthogonal complement,

\[
(1-\Pi_g)v_g=(H_g-e_0)^{-1}(1-\Pi_g)r_g.
\]

The complementary spectrum stays at distance at least one from e0.
Moreover, writing x=lambda-eg>=2 and |eg-e0|<=1,

\[
\frac{x}{(\lambda-e_0)^2}
\le\frac{x}{(x-1)^2}\le2.
\]

Consequently

\[
\|(1-\Pi_g)v_g\|\le\|r_g\|,
\quad
\|(H_g-e_g)^{1/2}(1-\Pi_g)v_g\|
\le\sqrt2\|r_g\|.
\tag{G6}
\]

Choose the positive phase of the true ground Psi_g so its overlap with
v_g is positive. The existing harmonic ground convergence gives that
overlap tending to one; its deficit from one is O(g^4) by (G6).
We obtain

\[
\boxed{
\|\Psi_g-v_g\|+
\|(H_g-e_g)^{1/2}(\Psi_g-v_g)\|\le C' g^2.}
\tag{G7}
\]

Thus the computed first ground jet has an actual finite-g Hilbert and
vacuum-subtracted form remainder. The statements concern the actual
compact Hamiltonian, not a polynomial truncation used as an operator.

## What this supplies to the source comparison

The ground input to the source map now has a controlled remainder in
these two norms. Multiplying it by an arbitrary retained source is a
separate weighted operation: (G7) alone is not an essential-supremum
conditional estimate and cannot justify the all-source finite-g
residual closure. The accompanying conditional-score calculation
identifies that stronger norm explicitly.

The already checked exact identity (G1) supplies the finite algebra.
Taylor remainder estimates, Gaussian cutoff estimates and the spectral
argument above are analytic proof steps; they are not Lean formalizations.
