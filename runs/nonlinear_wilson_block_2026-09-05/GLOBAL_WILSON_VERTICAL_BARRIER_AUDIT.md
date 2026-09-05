# Independent audit of the global Wilson vertical barrier

5 September 2026. Outputs-only review of the actual bouquet and adjacent-strip
fiber operators in `GLOBAL_WILSON_VERTICAL_BARRIER.md`, and of the sharper
companion construction communicated by the exact-controls reviewer. No canonical
proof, ledger or sealed run is changed here.

The mathematical comparisons below are accepted. They control the full fiber
spectrum before true full-block vacuum subtraction. The physical class gap at
the identity is not used as a uniform noncentral fiber gap.

## 1. Actual metric and fiber Hilbert space

For the strip, put R=Ad(U). The original-link cometric in the based variables
(U=U1 U2,K=U1) has blocks

```
C_uu=8I-R-R*,  C_uk=4I-R,  C_ku=4I-R*,  C_kk=4I.
```

The blocks commute because they are polynomials in the orthogonal R and R*.
Thus the vertical Schur complement is exactly

```
S(U)=4I-(4I-R*)(8I-R-R*)^-1(4I-R)
    =15(8I-R-R*)^-1,
(3/2)I <= S(U) <= (5/2)I.
```

The map (U1,U2) to (U,K) preserves product Haar measure. At fixed U, the
left-invariant vertical fields have zero Haar divergence and S(U) is constant
in K. Therefore the stated vertical operator is the actual divergence-form
Schur term, not an independently imposed rotor metric. At U=I it is
`-(5/4)Delta`; the bouquet term is `-Delta`. Completing the electric form
leaves a nonnegative horizontal square with its real coupling retained.

Each full fiber has a uniformly elliptic scalar operator on connected compact
SU(N), a bounded real potential and compact resolvent. Its positive ground
state is simple. Conjugation covariance preserves the fiber-ground projection
on the residual gauge-invariant direct-integral space. Restricting a valid
full-space inequality to that physical subspace cannot improve its constant
by an unproved class-space factor.

## 2. SU(N) root and exact noncommuting potential comparison

The parent's radius `v(U)<=N^-2` is valid. The sharpened radius also works:

```
epsilon_N=min(1,4/N),    v(U)<=epsilon_N.
```

For principal eigenangles theta_i, the elementary chord bound and Cauchy give

```
sum_i |theta_i| <= (pi/2) sqrt(N sum_i |1-exp(i theta_i)|^2)
                = pi sqrt(N v(U)/2) <= pi sqrt(2) < 2pi.
```

Their signed sum is an integer multiple of 2pi because det(U)=1, hence is
zero. The principal square root H is therefore in SU(N), not merely U(N).
Writing A=Re H, c_i=cos(theta_i/2), eta=Tr(I-A), gives

```
0<=eta<=v(U)/2<=1/2,
v(U)=4eta-2 sum_i(1-c_i)^2,
3eta <= v(U) <= 4eta,
A >= (1-eta)I.
```

The lower `3eta` follows from `sum(1-c_i)^2<=eta^2` and eta<=1/2.
After K=HF, the exact potential is

```
2u[v(HF)+v(F^-1 H)] = 4u eta + 4u Tr[A(I-Re F)].
```

Both `A-(1-eta)I` and `I-Re F` are positive semidefinite. Their product need
not be positive or commute, but its trace equals the trace of a positive
congruence. This proves the asserted lower form bound without a simultaneous
diagonalization assumption on A and F.

## 3. Improved adjoint estimate and the whole counted spectrum

In an eigenbasis for U, the adjoint eigenvalues on off-diagonal root spaces
are z_i/z_j, while Cartan directions have eigenvalue one. Consequently

```
||I-Ad(U)||^2 = max_(i,j) |z_i-z_j|^2
             <= 2 sum_i |z_i-1|^2 = 4v(U) <= 16eta.
```

For alpha=8/3 and t=(1+alpha eta)^-1, the strip metric satisfies
`S(U)>=(5/2)t I`. Left translation by H rotates derivatives by Ad(H) or its
inverse, according to the field convention. These commute with R and S(U),
so the actual translated electric form has this bound.

Since `1-t-eta=eta(5-8eta)/(3+8eta)>=0`, the potential coefficient
`1-eta` also dominates t. Thus, on the common translated Haar fiber,

```
A_U >= t A_I+4u eta I.
```

The same bound is valid for the bouquet because its translated kinetic term
is unchanged and positive. One particularly short route to the spectral cap is

```
1-t <= alpha eta <= v(U) <= v(U)/epsilon_N,
A_U >= (1-v(U)/epsilon_N) A_I + u v(U) I.
```

The last coefficients are nonnegative inside the root chart. Outside it, the
Frobenius triangle inequality gives `A_U>=u v(U)I>=epsilon_N u I`. Min-max
therefore proves, for every index j including multiplicities,

```
E_j(U) >= min(E_j(I),epsilon_N u).
```

No representation cutoff, numerical rank pattern, gap premise or large-u
asymptotic enters this all-j statement. The original weaker cap follows too.

## 4. Scalar energy cost, ground upper bound and exact nongap control

Set e_j=E_j(I), delta=e1-e0 and Q_U=I-P_U. The same near-chart comparison,
combined with `v(U)>=epsilon_N` outside, yields

```
E_j(U) >= e_j+(u-e_j/epsilon_N)v(U),
A_U-e0 >= delta Q_U+(u-e1/epsilon_N)v(U)I.
```

The scalar term is nonnegative once u>=e1/epsilon_N. In particular, twice that
threshold gives a retained barrier `(u/2)v(U)`. This uses the full fiber e1,
not the first invariant oscillator excitation.

For a matching upper bound, let phi_I be the normalized positive central
ground state. Its probability density is invariant under conjugation and
inversion, so Schur's lemma in the defining representation gives

```
integral K |phi_I(K)|^2 dK = m I,   m real,   m<=1.
```

Both block metrics satisfy `T_U<=T_I`. Testing A_U on this same central state
therefore gives the exact upper bound

```
E0(U)-e0 <= 2u m v(U) <= 2u v(U).
```

Together these prove the claimed actual ground-potential comparison. No
assumption that m is positive is needed for the upper inequality.

At U=-I in SU(2), the exact potential is the constant 8u. The conditional
gaps are exactly 3/4 for the bouquet and 15/16 for the strip under the stated
Casimir convention. This is a useful negative control: subtracting E0(U)
globally cannot preserve the order-sqrt(u) fast gap. Retaining the coarse
offset is essential to the accepted theorem.

## 5. Precise multiblock consequence and remaining obligation

For every E<epsilon_N u, the fiber counting function obeys
`N_U(E)<=N_I(E)` and is zero wherever `u v(U)>E`. Thus the global bound also
localizes low spectral weight in coarse holonomy without falsely identifying
that weight with a conditional excitation gap.

For disjoint original-edge blocks with the actual additive Hamiltonian,
completion and integration give, before true vacuum subtraction,

```
H-r e0 >= delta sum_j Q_(U_j) + sum_j (u-e1/epsilon_N)v(U_j).
```

The inequality survives a common vertex Gauss restriction. This states only
the exact additive situation; surrounding or overlapping Wilson interactions
require their own decomposition and allocation estimates.

The actual full vacuum E_vac exceeds the sum of central fiber vacua by slow
zero-point energy, already of order sqrt(u) per strip in the harmonic theory.
Replacing r e0 by E_vac and omitting this extensive offset would invalidate
the comparison. The next actual target is the ground-bundle horizontal form
and its mixed coupling, with the varying scalar potential retained, followed
by the vacuum-adapted nonlinear fast compression in common energy units.
Neither the configuration fiber nor its ground bundle is identified here
with the exact full-history OS complement.

## 6. Evidence scope

The final written `GLOBAL_WILSON_VERTICAL_BARRIER_SHARPENED.md` was read in
full. Its proof agrees with the independent derivation above. It additionally
proves m>=0 by using the constant central Haar trial, which gives
`e0<=4uN` and hence `4uN m>=<phi_I,T_I phi_I>>=0`. Its corrected original
metric locator is Sections 3--4 of the canonical fiber note. No substantive
mathematical correction was required.

The final `check_global_wilson_vertical_barrier.py` was inspected and its
read-only companion replay was executed independently. All three exact payload
families match: arbitrary-symbol matrix identities and a noncommuting PSD
example; actual rational SU(2) metric/Casimir examples; and symbolic scalar
budgets for the cap, affine bound and ground trial. The replay checks five
source pins, prohibits NumPy/SciPy imports, and verifies overwrite and optimized-
Python rejection. Its final certificate SHA256 is
`1e0239bd3e9b3ebe639bcac9d56f92a5b940dd5bd893bc0f4b69d4fb66a252ec`.
The earlier `*_pre_format.json` and `*_pre_locator.json` are historical
certificates only. No finite calculation is promoted to the all-rank min-max,
elliptic-domain or ground-positivity theorem.
