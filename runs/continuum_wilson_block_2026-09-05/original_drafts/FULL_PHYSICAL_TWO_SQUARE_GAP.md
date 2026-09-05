# The actual coupled two-square Wilson Hamiltonian at large magnetic coupling

5 September 2026. Analytic finite-block theorem. This note advances the
physical fast-mode comparison beyond a constrained fiber: it treats the
entire actual two-adjacent-square Hamiltonian on its gauge-invariant Hilbert
space, retaining the shared-edge electric coupling. It does not identify
this block with a conditional subsystem in an ambient lattice or with the
complement of an OS-history blocking isometry.

Inputs are the exact link geometry in
[WILSON_BLOCK_CONDITIONAL_SCORE.md](WILSON_BLOCK_CONDITIONAL_SCORE.md), §6.1,
and the localization method proved in
[PHYSICAL_WILSON_FIBER_FAST_GAP.md](PHYSICAL_WILSON_FIBER_FAST_GAP.md), §2.
The exact physical inversion identity in §2 below gives the stronger local
form comparison needed for the stated remainder. It is independent of an
unproved Born-Oppenheimer remainder or a numerical spectral fit.

## 1. Operator and theorem

Fix N>=2 and G=SU(N), with d=N^2-1 and Lie metric
<X,Y>=-2ReTr(XY). Use two based face holonomies U1=s b1 and U2=b2 s^(-1):
s is the common edge and each b_j is a three-edge outer path. Maximal-tree
gauge gives Haar space L2(G^2,dU1 dU2), with the residual simultaneous
conjugation action. Its invariant subspace is the physical block Hilbert
space H_phys.

Let L_j,a and R_j,a be the skew-adjoint left and right Lie derivatives in
face j. The electric and shifted magnetic operators are exactly

```text
H_E = -(1/2)[3Delta_1+3Delta_2+sum_a(L_1,a-R_2,a)^2]
    = -2(Delta_1+Delta_2)+sum_a L_1,a R_2,a,

V_u = 2u[v(U1)+v(U2)],   v(U)=N-ReTr U,
H(u) = H_E+V_u.                                          (1)
```

The first identity follows by differentiating the seven original links:
three outer edges per face and the common edge with opposite orientation.
The scalar shift is 4uN; it does not change excitation gaps. This operator
is uniformly elliptic on the full compact G^2, has compact resolvent, and
preserves H_phys. The potential has its unique global zero at (I,I).

Write E_j^phys(u), j=0,1,..., for its ordered physical eigenvalues, counting
multiplicity. Define

```text
e_*= (d/2)(sqrt(3)+sqrt(5)).
```

Then as u tends to infinity,

```text
E0^phys = e_* sqrt(u)+O_N(u^(1/4)),
E1^phys = [e_*+2sqrt(3)] sqrt(u)+O_N(u^(1/4)),
E2^phys = [e_*+sqrt(3)+sqrt(5)] sqrt(u)+O_N(u^(1/4)),
E3^phys = [e_*+2sqrt(5)] sqrt(u)+O_N(u^(1/4)).            (2)
```

For all sufficiently large u the first three physical excited levels are
simple and mutually isolated, and the next physical level obeys

```text
E4^phys >= [e_*+3sqrt(3)] sqrt(u)-O_N(u^(1/4)).          (3)
```

In particular the true full physical block gap is

```text
E1^phys-E0^phys = 2sqrt(3) sqrt(u)+O_N(u^(1/4)),
E1^phys-E0^phys >= sqrt(3) sqrt(u)                       (4)
```

for u above an N-dependent finite threshold. No uniformity in N or in the
number of coupled blocks is claimed. This is a theorem about the coupled
physical Hamiltonian (1), rather than a statement about its fixed-coarse
fiber or about the weighted configuration-diffusion generator.

## 2. Exact Gauss cancellation and physical inversion symmetry

The physical constraint is

```text
G_a F=(L_1,a-R_1,a+L_2,a-R_2,a)F=0,  for every a.        (5)
```

Left and right derivatives commute within each face, all derivatives on
different faces commute, and sum_a L_j,a^2=sum_a R_j,a^2=Delta_j. Thus
contracting (5) first with L1+R1+L2+R2 gives

```text
(L1.L2-R1.R2)F=0.
```

Contracting (5) with L1+R1 then gives

```text
[(L1.L2-R1.R2)+(R1.L2-L1.R2)]F=0.
```

Consequently the exact operator identity on smooth physical functions is

```text
(L1.R2)F=(R1.L2)F.                                     (6)
```

These are contracted Gauss identities: they do not assume separately that
each face is a class function. In particular they apply to functions such
as ReTr(U1 U2), which retain relative orientation data.

Let I act by simultaneous inversion,
(IF)(U1,U2)=F(U1^(-1),U2^(-1)). It is a Haar-unitary involution preserving
the physical subspace. It sends L_j to -R_j and R_j to -L_j, so (1),(6) give

```text
I H_E I=H_E  on H_phys,
I V_u I=V_u.                                           (7)
```

This symmetry is specific to the physical operator; the unsymmetrized
shared-edge cross term need not commute with inversion on arbitrary
functions of the two holonomies.

The useful consequence is an exact equality of quadratic forms. In product
exponential coordinates Uj=exp Xj, simultaneous inversion sends x to -x,
and product Haar density J(x) is even. Let C(x) be the smooth link cometric
in these coordinates. For a smooth physical function with support in a
small inversion-invariant chart, (7) implies

```text
q_E(F)=q_E(IF)
      =(1/2) integral <grad F,C(-x) grad F> J(x) dx,
q_E(F)=(1/2) integral <grad F,C_even(x) grad F> J(x) dx,
C_even(x)=[C(x)+C(-x)]/2=C(0)+O_N(|x|^2).               (8)
```

This proves cancellation of the linear metric form on all physical
functions, including mixed coarse/fiber ones. A formal version of the same
identity uses diagonal Gauss and antisymmetry of the Lie structure constants:

```text
sum_b partial_Zb [Q,grad_Q]_b F
 =-sum_b partial_Zb [Z,grad_Z]_b F=0.                    (9)
```

The exact form argument (8) supplies the uniform local estimate; a formal
weak-field coefficient alone would not supply that estimate.

The exact inversion identity used here is special to this two-square
geometry and physical constraint. A general lattice block can retain cubic
magnetic terms involving a curl and a Lie bracket even after Gauss reduction.
This proof does not assert that the operator expansion of an arbitrary
physical Wilson block is even in the weak-field parameter.

## 3. The physical oscillator and its first three excited shells

At the identity the actual link cometric on (X1,X2) is

```text
C(0)=[[4,-1],[-1,4]] tensor I_d.
```

Set Q=(X1+X2)/sqrt(2), Z=(X1-X2)/sqrt(2). Its eigenvalues are 3 in Q
and 5 in Z. Since v(exp X)=|X|^2/4+O_N(|X|^4), the local potential is

```text
2[v(exp X1)+v(exp X2)]
 = (|Q|^2+|Z|^2)/2+O_N((|Q|^2+|Z|^2)^2).              (10)
```

After the u^(-1/4) spatial rescaling the limiting oscillator is

```text
H_osc = -(3/2)Delta_Q-(5/2)Delta_Z+(|Q|^2+|Z|^2)/2,
phi_0(Q,Z) proportional to
 exp[-|Q|^2/(2sqrt(3))-|Z|^2/(2sqrt(5))].               (11)
```

The physical action is simultaneous Ad on Q,Z. The oscillator level with
Hermite degrees n_Q,n_Z has excitation energy

```text
n_Q sqrt(3)+n_Z sqrt(5).                               (12)
```

There is no invariant degree-one vector because su(N) is simple. At total
degree two the complete invariant subspace has dimension three, because
the invariant bilinear form on the adjoint is unique. Its three eigenvectors
are proportional to

```text
(|Q|^2-d sqrt(3)/2) phi_0,       excitation 2sqrt(3),
(Q.Z) phi_0,                   excitation sqrt(3)+sqrt(5),
(|Z|^2-d sqrt(5)/2) phi_0,       excitation 2sqrt(5).      (13)
```

Each is a one-dimensional invariant shell. Every higher Hermite degree has
excitation at least 3sqrt(3), and

```text
2sqrt(3) < sqrt(3)+sqrt(5) < 2sqrt(5) < 3sqrt(3).        (14)
```

Thus all three shells lie below every possible cubic or higher invariant,
including the invariant cubic tensors available for N>=3. No assertion that
higher invariant polynomials are absent is used. For N=2 some potential
cubic shells may be absent, which can raise the subsequent threshold but
does not alter (13)-(14).

## 4. Compact localization proves the theorem

Put h=u^(-1/2), so H(u)=u P_h, with P_h=h^2 H_E+2(v(U1)+v(U2)). On a
radius-2r product logarithm ball, the physical form comparison (8), Haar
estimate J=1+O_N(r^2), and potential estimate (10) bound the local physical
Rayleigh quotients between 1+O_N(r^2) multiples of the oscillator
quotients with parameter h.

The unique global potential minimum and compactness give

```text
2[v(U1)+v(U2)] >= c_N[dist(U1,I)^2+dist(U2,I)^2].        (15)
```

Choose a radial physical partition chi_0^2+chi_1^2=1 with chi_0 supported
in radius 2r and chi_1 supported outside radius r. The exact electric form
is a sum of seven squared vector fields with bounded metric coefficients,
so its IMS localization error is at most C_N h^2/r^2. The outside form is
at least c_N r^2 times its norm. The cutoffs preserve both simultaneous
conjugation and inversion.

The min-max argument is the same as the compact rotor proof, now wholly
inside the physical subspace: impose the first j local physical Dirichlet
orthogonality conditions on chi_0 F, compare their zero extensions with the
invariant Euclidean oscillator, and use the outside lower bound. Conversely,
cut off the first finitely many invariant Hermite eigenfunctions to obtain
the matching finite-dimensional trial spaces. Gaussian tails at radius r
are exponentially small in r^2/h. With r=h^(1/4), for each fixed j,

```text
E_j^phys(P_h) = h e_j^phys + O_(N,j)(h^(3/2)).           (16)
```

In particular the potentially dangerous O(r) local metric error is absent
by (8). Without that exact physical cancellation, the same argument would
still give leading convergence with a weaker remainder, but would not
justify (16).

Multiplication by u and the invariant oscillator ordering (13)-(14) prove
(2)-(4). For large u, the scaled error tends to zero relative to each fixed
separation in (14), which proves simplicity and isolation of the first
three physical excited eigenvalues as well. The fourth-level lower bound
follows by applying (16) at j=4 and using the lower threshold 3sqrt(3).

All singular gauge orbits, including (I,I), are handled by working on the
smooth group product and then its closed invariant subspace. No guessed
boundary condition on a gauge quotient is part of the argument. Likewise,
secondary central or other local potential wells are excluded by (15) and
the outside IMS energy; no landscape classification is required.

## 5. The first shells have an explicit physical source frame

The three shells can be reached by bounded gauge-invariant Wilson functions,
with an explicit large-u normalization. Put

```text
S_Q=2v(U1U2),
S_M=2[v(U1)-v(U2)],
S_Z=4[v(U1)+v(U2)]-2v(U1U2),

a_Q=sqrt(3d/2),  a_M=sqrt(d sqrt(15))/2,  a_Z=sqrt(5d/2).
```

Let Omega_u be the normalized ground state and define the centered sources

```text
A_j(u)=sqrt(u)[S_j-<Omega_u,S_j Omega_u> I]/a_j,
j=Q,M,Z.                                               (17)
```

These are real physical sources. They do not use an odd fundamental trace,
so they also apply to SU(2). Let Pi_3(u) project onto exactly the first three
physical excited eigenvalues in (2). The synthesis map

```text
J_u:C^3 -> ran Pi_3(u),
J_u c=sum_(j=Q,M,Z) c_j Pi_3(u) A_j(u) Omega_u
```

obeys

```text
J_u^* J_u -> I_3  as u->infinity.                       (18)
```

In particular, for sufficiently large u, its Gram lies between I_3/2 and
3I_3/2 and it is onto the entire three-shell range. The source S_Q alone has
a nonzero projection onto the actual lowest physical excited eigenstate.

Here is a proof including the source-moment issue. Under Xj=sqrt(h)x_j,
h=u^(-1/2), the source functions divided by h tend locally to |Q|^2,Q.Z,|Z|^2.
The Gaussian variances in (11) are sqrt(3)/2 and sqrt(5)/2 in each component.
Consequently the centered limiting source vectors are precisely the three
orthogonal functions in (13), with squared norms

```text
3d/2,  d sqrt(15)/4,  5d/2.                             (19)
```

Ordinary L2 convergence of low eigenfunctions would not alone justify a
source divided by h. The needed weighted convergence follows from the same
variational argument. The potential lower bound gives tightness after the
sqrt(h) rescaling; local ellipticity gives compactness on fixed rescaled
balls. Any limit of the first four normalized eigenfunctions is an
oscillator eigenfunction, and simplicity identifies it up to phase. Their
Rayleigh energies converge to the matching oscillator energies. Lower
semicontinuity separately bounds the nonnegative kinetic and potential
parts by the corresponding oscillator parts. Equality of the sums forces
convergence of both parts, including vanishing potential-energy tails
outside large rescaled balls.

Every source above is form-controlled by the potential. Indeed
v(U)=||I-U||_F^2/2 gives

```text
v(U1U2)<=2[v(U1)+v(U2)],
|S_j|<=2P,   P=2[v(U1)+v(U2)].                          (20)
```

On a fixed rescaled ball the source matrix elements converge directly.
Outside it, (20) and Cauchy-Schwarz bound the matrix element of S_j/h by
twice the product of the two square roots of the potential-energy tails.
Those tails vanish by the preceding energy convergence. This proves the
convergence of all projected source matrix elements, including the ground
expectations used in (17), without assuming convergence of an unprojected
source vector with an unbounded rescaled norm.

Choose phases of the three low eigenvectors to match (13). Their overlap
matrix with the three sources in (17) tends to I_3 by (19). Equation (18)
follows. The already-proved rank three of Pi_3 and this invertible overlap
matrix establish totality of the source frame in the full finite-block
three-shell range. No infinite-dimensional rank shortcut is used.

## 6. Physical implication and its remaining scope

With the project's physical convention
u=g_H^(-4) and H_phys_units=c_H(a) g_H^2 H/a, the full physical two-square
gap is

```text
2sqrt(3) c_H(a)/a + O_N(c_H(a) g_H/a).                  (21)
```

This establishes a fast energy in the full interacting two-square physical
block, not merely a conditional fiber. The slowest physical block excitation
comes from the coarse oscillator, while the fiber gap remains higher. The
first three isolated physical shells quantify their separation and mixed
channel explicitly, and (17)-(18) provide physical Wilson sources spanning
their complete finite-block range.

The result still concerns a fixed finite graph with no interactions crossing
its boundary. Applying it to a family of spatial blocks requires comparison
with the actual surrounding Wilson interactions, a projection onto the
appropriate slow band, estimates of the induced couplings and ground-energy
shifts, and the actual OS-history intertwiner. It supplies a physical local
spectral input for that comparison; it neither proves the multiblock
complement bound nor transports a continuum mass by itself.
