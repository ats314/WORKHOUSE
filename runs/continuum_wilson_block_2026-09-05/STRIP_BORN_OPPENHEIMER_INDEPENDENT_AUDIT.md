# Independent audit of the physical strip and two-strip first shell

5 September 2026. Outputs-only review by the independent controls collaborator.
The single-strip calculation and the two-strip second-order effective matrix
are accepted under the finite-graph hypotheses below. The coefficients were
rederived from the link co-metric, rather than read back from a proposed
effective Hamiltonian.

The sources are `WILSON_BLOCK_CONDITIONAL_SCORE.md` §6.1,
`WILSON_STRIP_BORN_OPPENHEIMER_FIRST_TERM.md`, and
`PHYSICAL_WILSON_FIBER_FAST_GAP.md`. The literal-source Gaussian normalization
also checks the proposed sources in `FULL_PHYSICAL_TWO_SQUARE_GAP.md`.
No canonical source, graph status, or sealed run was changed by this audit.

## 1. Metric, scaling, Haar measure, and the first coefficients

Set A=ad(Q), alpha=sqrt(2)g and u=g^-4. The exact strip co-metric gives

```text
C_uu=6I-alpha^2 A^2+O(alpha^4),
C_ku=3I+alpha A-alpha^2 A^2/2+O(alpha^3),
S=4I-C_ku C_uu^-1 C_uk=(5/2)I+(5alpha^2/12)A^2+O(alpha^4).
```

Thus the identity-fiber kinetic operator is exactly -(5/4)Delta. In the
fiber coordinate F=exp(gZ/sqrt(2)), the rescaled kinetic operator begins at
-(5/2)Delta_Z. The Gaussian inverse covariance is a=1/sqrt(5), and each
coordinate has variance 1/(2a)=sqrt(5)/2. These factors differ from those
of the bouquet and from those of the classical conditional density.

The balanced horizontal velocity follows by subtracting the motion of H:

```text
C_ku C_uu^-1=I/2+alpha A/6+O(alpha^3),
dU U^-1=alpha E+alpha^2[Q,E]/2+O(alpha^3),
dH H^-1=alpha E/2+alpha^2[Q,E]/8+O(alpha^3).
```

The difference has coefficient 1/4+1/6-1/8=7/24 at alpha^2;
division by the fiber-coordinate scale alpha/2 gives 7alpha/12.
Consequently

```text
D_E phi=-(7g/(6sqrt(10)))<[Q,E],Z> phi0+O(g^2),
||D_E phi||^2=(49g^2/(144sqrt(5)))||[Q,E]||^2+o(g^2).
```

The transformed connection has the correct positive half-divergence term:
Haar divergence freeness implies
rho^(1/2) v.grad rho^(-1/2)=v.grad+(div v)/2. Its leading constant
translation has zero divergence. Positive real normalized ground functions
have zero Berry connection. There is no missing normalization derivative.

For the vertical correction, direct contraction with the normalized Gaussian
gives

```text
Tr_ad A^2=-N|Q|^2,
E[Z^2]=-C_F I/(2a),
Delta e_vertical=-sqrt(5)(N/12+C_F/16)|Q|^2.
```

The Q-dependent quadratic corrector is centered at oscillator level two,
whose energy denominator is 2sqrt(5). The Haar half-density has no Q
dependence in the fixed F chart; its Q-independent corrections cancel from
the displayed vertical energy difference. Thus the balanced partial
derivative begins at g^2 while the intrinsic derivative begins at g.

The exact coarse-coordinate form coefficient is

```text
A_Q=(3/(2g^2))I-(3/4)(ad Q)^2+O(g^2).
```

This follows by multiplying dexp^-1 C_uu dexp^-T, including the factor
1/(2alpha^2). It yields the Born-Huang scalar
49N|Q|^2/(96sqrt(5)). Adding the vertical shift gives precisely

```text
c_N |Q|^2,    c_N=sqrt(5)(5-2N^2)/(160N).
```

The independent coarse magnetic quartic is -Tr(Q^4)/24. Flattening the
coarse Haar density, whose logarithm is -Ng^2|Q|^2/12+O(g^4), contributes
the constant -N(N^2-1)/8 at this order. It does not change c_N. These
quartic, constant, and angular-metric terms must not be folded into c_N.

## 2. Exact single-strip physical cancellation

The leading coupling is proportional to div_Z G_Q, with
G_Q=[Q,grad_Q]. On a jointly invariant smooth function, G_Q F=-G_Z F.
For any smooth F, total antisymmetry of the compact-Lie structure constants
gives

```text
div_Z G_Z F
 =sum_bcd f_bcd(delta_bc partial_d F+Z_c partial_b partial_d F)=0.
```

Therefore h1 vanishes on the entire physical two-variable domain, including
nonfactorized functions. The stronger group-level evenness argument is also
valid. On physical face functions,
L1_a-R2_a and R1_a-L2_a agree by the total Gauss identity. Simultaneous face
inversion exchanges these derivatives, preserves the Casimirs and Wilson
potential, and preserves Haar. Equality of their quadratic-form norms proves
physical operator invariance without assuming that one derivative preserves
the physical subspace. Finally

```text
Phi_-g(Q,Z)=Conj_F[(Phi_g(Q,Z))^-1]
```

for the balanced chart. The final conjugation has no effect on invariant
functions, and the Haar half-density is even. Hence the actual pulled-back
physical family is even in g: all odd local physical Taylor coefficients
vanish. Separate vertical and horizontal pieces need not be even.

## 3. Two strips: the on-shell self-energy and its surviving positive term

Take two edge-disjoint strips meeting at a base vertex, with their actual
link forms and no ambient plaquette interactions. There is one total Gauss
constraint. It does not force each L_i=[Q_i,grad_i] to vanish.
For a coarse oscillator eigenfunction psi and the product fiber Gaussian,

```text
h1(psi Phi0)=(7/(2sqrt(10)))sum_i <Z_i,L_i psi> Phi0.
```

Each L_i commutes with the isotropic coarse oscillator. The image therefore
preserves coarse energy and adds exactly one fiber quantum sqrt(5).
Distinct fiber directions are orthogonal and have variance sqrt(5)/2.
The on-shell Feshbach form is consequently

```text
-g^2 (49/80)sum_i ||L_i psi||^2.
```

The exact coarse metric adds +(3g^2/4) times this angular form, leaving
+(11g^2/80)sum_i||L_i psi||^2. Its sign and coefficient are accepted.
Using the fiber gap as a denominator is exact on this image at this energy;
it is not an energy-independent replacement for the full resolvent.

There is no exact leading Q0 resonance at a fixed coarse oscillator level:
the excitation frequencies sqrt(3) and sqrt(5) are rationally independent,
while a Q0 state has at least one fiber quantum. Compact oscillator
resolvents provide the fixed-level inverse. Its norm is not bounded
uniformly across all coarse energies. A mixed-shell negative control below
explicitly detects misuse of the denominator sqrt(5).

The witness psi=(Q1 dot Q2) times the coarse product Gaussian is physical,
has nonzero individual L_i, and has normalized angular form 2N. The
surviving angular coefficient on it is 11N/40.

## 4. The first physical coarse shell

Write d=N^2-1 and sigma=sqrt(3)/2 for a coarse coordinate variance. The
degree-two physical coarse singlets are

```text
R1=(|Q1|^2-d sigma)Phi, R2=(|Q2|^2-d sigma)Phi,
M=(Q1 dot Q2)Phi.
```

They all have leading excitation 2sqrt(3). The second-order effective
matrix is diagonal in this basis: the radial cross entry factors through
a zero ground overlap; the mixed/radial entries vanish by parity in one
coarse variable; angular terms kill the individual radial states.
Equal strip geometry makes the two radial entries equal.

Rotational averaging and exact Gaussian moments give

```text
angular_average Tr Q^4/|Q|^4=(2N^2-3)/(4N(d+2)),
R_i: Delta sum |Q|^2=2sqrt(3), Delta sum |Q|^4=9(d+2),
M:   Delta sum |Q|^2=2sqrt(3), Delta sum |Q|^4=6(d+2).
```

After subtracting the ground correction, the radial and mixed diagonal
entries are respectively

```text
delta_R=sqrt(15)(5-2N^2)/(80N)-3(2N^2-3)/(32N),
delta_M=sqrt(15)(5-2N^2)/(80N)-(2N^2-3)/(16N)+11N/40.
delta_M-delta_R=(54N^2-15)/(160N)>0  for N>=2.
```

All P0h2P0 terms affecting this difference have been retained: the actual
metric, the coarse quartic, the vertical zero-point shift and Born-Huang
scalar. The Haar and pure-fiber constants cancel between excitation and
ground. No independent strip term can generate an omitted off-diagonal
entry under these hypotheses. Thus the claimed finite effective splitting
is accepted, rather than just its scalar arithmetic.

The revised source supplies the required spectral completion in §7.1,
which has also been independently audited and is accepted. The actual
four-holonomy potential has one global minimum and the link form is
uniformly elliptic. Leading compact localization isolates the rank-three
physical shell. Finite polynomial Hermite correctors through order g^2
solve the first-order complement equation and the displayed second-order
effective eigenvalue equation. The required denominators are nonzero on
the finite set of Hermite levels involved. Cutoff derivatives have
exponentially small Gaussian tails, and smooth local Taylor bounds give
an O(g^3) residual in g^2H. The spectral theorem and the already known
cluster rank then give O(g)=O(u^-1/4) eigenvalue errors in H.

Thus the two gaps are 2sqrt(3)sqrt(u)+delta_R/M+O_N(u^-1/4), and the
positive difference above selects the lower radial doublet for large u.
The doublet is exactly degenerate: the two identical strip Hamiltonians
are additive and each product of a physical radial excitation with the
other strip's ground is an actual physical eigenvector. The common Gauss
restriction creates no coupling between these additive eigenvectors.
This conclusion uses the analytic localization and corrector argument;
the finite computations alone do not establish the remainder theorem.

## 5. Literal sources and exact controls

For v(U)=N-ReTr U, the three centered sources obtained by multiplying
2v(U1U2), 2(v(U1)-v(U2)), and
4(v(U1)+v(U2))-2v(U1U2) by sqrt(u) tend to

```text
|Q|^2-dsqrt(3)/2,  Q dot Z,  |Z|^2-dsqrt(5)/2.
```

They are mutually orthogonal in the limiting Gaussian ground measure and
have squared norms 3d/2, d sqrt(15)/4, and 5d/2. This independently accepts
the proposed physical single-strip source normalization.

Reproducible controls in this directory:

- `check_strip_born_oppenheimer_audit.py` and
  `strip_born_oppenheimer_audit_controls.json`: exact coordinate jets,
  SU(2), SU(3), SU(4) Lie/Gaussian contractions, seven invariant polynomial
  examples, the arbitrary-function divergence identity, and a noninvariant
  negative control.
- `check_multistrip_selfenergy.py` and `multistrip_selfenergy_controls.json`:
  exact SU(2) Gaussian witness, its full leading-oscillator image energy,
  self-energy and angular coefficient, a mixed-shell denominator negative
  control, and the three source Gram entries.
- `check_multistrip_first_shell.py` and `multistrip_first_shell_controls.json`:
  symbolic-rank radial moments, direct Wick trace contractions at ranks
  2, 3, 4, and the complete SU(2) 3-by-3 effective matrix. The mixed/local
  difference is exactly 201/320. Omitting the metric reverses its sign,
  giving -759/320; this negative control detects that material omission.

The scripts use the repository Python environment and all pass Ruff.
Their generation entry points refuse an existing JSON output. Their
calculation functions can be called independently for replay.

The mathematics here is finite-graph physical energy and its local
oscillator expansion. It does not identify a configuration-fiber projector
with an OS-history reducing complement, include plaquettes crossing the
block boundary, or establish a scale-uniform multiblock or continuum bound.
