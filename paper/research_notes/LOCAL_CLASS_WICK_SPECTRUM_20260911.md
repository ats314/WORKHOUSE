# Local class Wick spectrum over all ranks

## W1. Rank-uniform formal recurrence

For the traceless Gaussian covariance E[X_ab X_cd]=(delta_ad delta_bc-delta_ab delta_cd/N)/2,
put D=Delta/2, L=Euler-D, and W=exp(-D/2). The commutator [Euler,D]=-2D gives
L W=W Euler. Consequently Pi_d=W H_d W^-1 and R_s=sum_(d!=s) Pi_d/(s-d)
resolve every finite polynomial source. Differentiation preserves each integer-rank
trace ideal. Shells s=0,2,3 are simple, except that the odd shell vanishes at N=2.

For K(g)=L+sum_(j>=1)g^j(-1)^j P_(2j+2)/(2^j(2j+2)!), g=sqrt(2N/beta),
projecting the order-r forcing onto Pi_s gives its unique eigenvalue coefficient,
and applying R_s gives the orthogonal state coefficient. Induction cancels the
whole eigen-equation at every order. All operations lie in Q[N,N^-1]: the
resonant coefficient is extracted in the one-dimensional homogeneous shell,
without dividing by rank-dependent norms. Degree at order r is at most s+4r.
This proves a finite constructive recursion at every order, not convergence.

## W2. Both sectors through beta^-2

The exact polynomial recurrence recovers the archived c0,c1,c2 and c3+ values.
It derives, in the convention Delta=s/g+sum_(j>=0)c_j beta^(-j/2),

    c3- = -sqrt(2N)(14267N^8-186257N^6+1596792N^4-8442260N^2+20165216)/(56623104N^3),
    c4+ = -(204120N^10-2448353N^8+19880740N^6-101716794N^4+294734750N^2-362174143)/(4529848320N^3),
    c4- = -(329385N^10-4937377N^8+52194445N^6-403915341N^4+1985928205N^2-4449690457)/(4529848320N^3).

Here s=2 for even N>=2 and s=3 for odd N>=3. At N=3 the c4 values are exactly
-56673445/1528823808 and -290599777/6115295232, the earlier recorded anchors.
The native rational-field recurrence, original expression recurrence, and
independent Cartesian SU3/SU2 controls agree. All polynomial residuals vanish.

## W3. Coefficient signs and successor

Removing the negative prefactor and positive denominator from each c0..c4 gives
a polynomial in z=N^2. Substitution z=x+4 in the even sector, and z=x+9 in the
odd sector, yields strictly positive coefficients. Thus each correction is
strictly negative throughout its allowed integer ranks. Exact witnesses are
recomputed by the registered suite; this establishes signs of coefficients.

The [complete derivation](../../docs/derivations/local-class-wick-spectrum.md)
provides the operator formulas and proofs. The
[pinned run](../../runs/local_class_wick_2026-09-11/README.md) retains prior sources
and independent checks. Compact-group eigenvalue remainders, interacting-volume
control and continuum source transport remain open application obligations.
