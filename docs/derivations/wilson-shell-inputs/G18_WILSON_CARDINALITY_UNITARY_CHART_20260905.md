# A local unitary chart with an exponential support bound

5 September 2026. Analytic continuation of the symmetric-creator theorem
and the connected active-plaquette coefficient construction.

The convergent actual Wilson vacuum creators determine a local
anti-Hermitian generator by a uniformly convergent real-linear Neumann
series. Its finite-volume unitary transports the product vacuum line to
the actual symmetric Wilson vacuum line. A holomorphic doubled system
and connected plaquette witnesses give exponential bounds on the
**assigned interaction supports**, including the support of the coupling
variables on which a coefficient depends. These are the supports needed
for induced-subsystem activity estimates.

This constructs a new chart, denoted `V`, with a direct support bound. It
is generally different from the common-filter spectral-flow chart `U`
in the preceding parent note. Their vacuum lines agree. No equality of
their actions on excited vectors is asserted.

## 1. Inputs and notation

Use the calibrated finite Wilson model and constants in
`G18_ROOTED_WILSON_CONTRACTION_20260905.md` and
`G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md`:

```text
mu >= max(gamma tau0/2, log(2)+gamma tau0/4),
sigma0=mu-gamma tau0/4 >= log(2),
u_star=min(9 gamma/(309680 J_star exp(4mu)),
           9/(8450 tau0 J_star exp(4mu))).
```

The actual symmetric vacuum creators obey

```text
w(0)=0,  ||w(u)||_(sigma0)<=a=1/8  for |u|<u_star.
```

For finite nonempty link sets `X`, the vector `w_X` belongs to the exact
excited tensor factor on `X`. Set

```text
a_X(h_X)=|h_X><Omega_X| tensor 1_(X complement),
W=sum_X a_X(w_X),
||h||_nu=max_i sum_(X contains i) exp(nu |X|)||h_X||,
M1(h;nu)=max_i sum_(X contains i) |X|exp(nu |X|)||h_X||.
```

Creators commute, and two whose supports intersect have zero product.
Consequently `exp(W)` and `exp(-W)` are finite operator polynomials in
every finite link volume. No estimate of their global norms is needed.

All Hilbert spaces may be infinite dimensional. The operators used below
are bounded finite-volume operators; the uniform estimates do not depend
on local Hilbert-space dimensions or on the number of links.

## 2. Exact inversion of the creator tangent map

Let `s -> w(s)` be a continuously differentiable real-parameter path,
with `w(0)=0`. For a family `b`, write

```text
B=sum_X a_X(b_X),
S(b)=B-B*,
T_w b = Q exp(-W) B* exp(W) Omega.
```

Here `Q` removes the scalar vacuum component and identifies the remaining
vector with its family of exact nonempty excited supports. The map `T_w`
is conjugate linear in `b`. It is a bounded real-linear operator on the
underlying real creator space, not a complex-linear operator.

**Tangent estimate.** Put `a_nu=||w||_nu`. If `nu>=a_nu`, then

```text
||T_w b||_nu
  <= 2 exp(-2(nu-a_nu)) M1(w;nu) ||b||_nu.              (1)
```

If the coefficient on the right is `theta<1`, the equation

```text
b-T_w b=dot w                                             (2)
```

has the unique solution

```text
b=sum_(k>=0) T_w^k dot w,
||b||_nu <= (1-theta)^(-1)||dot w||_nu.                    (3)
```

Each local generator term has the exact off-diagonal block norm

```text
||a_X(b_X)-a_X(b_X)*||=||b_X||.                           (4)
```

Indeed its vacuum and exact excited ranges are orthogonal, and its
square is minus the corresponding pair of positive diagonal blocks.

### 2.1. Proof of the support estimate

Fix a lowering support `X`. Creators disjoint from `X` commute with
`a_X(b_X)*` and cancel between the two exponentials. Only

```text
W_X=sum_(Y intersects X) a_Y(w_Y)
```

remains. Expand `exp(-W_X) a_X(b_X)* exp(W_X) Omega` into left and right
creator tuples, with their factorial coefficients. Each nonzero tuple
has the following exact properties:

1. The right creator supports are mutually disjoint and cover every
   link of `X`. Otherwise the exact excited bra of the lowerer kills it.
2. The lowerer returns every link in `X` to its vacuum. A left creator
   cannot overlap any surviving right excited link outside `X`.
3. The output belongs to one exact support `Z`, with

```text
|Z|=sum_left |Y| + sum_right |Y| - |X|.                  (5)
```

There is no additional sum over output support projections. Partial
contraction by the possibly entangled vector `b_X` preserves the exact
excited factors on the surviving links and has norm at most `||b_X||`.

For each output root `i in Z`, point one left or right creator containing
`i`. With `t_Y=exp(nu|Y|)||w_Y||`, the touching sum satisfies

```text
sum_(Y intersects X) t_Y <= |X| a_nu.
```

Summing the remaining left and right tuples gives
`exp(2|X|a_nu)`; pointing either side gives a factor two. Formula (5)
contributes `exp(-nu|X|)`. Thus the rooted output norm is at most

```text
2 sum_(Y contains i) t_Y
    sum_(X intersects Y) exp(-nu|X|+2a_nu|X|)||b_X||.
```

Set `beta_X=exp(nu|X|)||b_X||`. Since `nu>=a_nu` and `|X|>=1`,

```text
sum_(X intersects Y) exp(-2(nu-a_nu)|X|) beta_X
  <= exp(-2(nu-a_nu)) |Y| ||b||_nu.
```

This proves (1), including the factor `M1(w;nu)`. The argument also
proves the bound when the input lowering family is an independent
element of the conjugate Hilbert spaces; that version is used below.

### 2.2. Exact vacuum-line transport and its scalar phase

Let `phi(s)=exp(W(s))Omega`. Commutativity of creators gives
`dot phi=exp(W) dot W Omega`. Equations (2) and the definition of `T_w`
therefore imply

```text
S(b) phi = dot phi + c(s) phi,
c(s)=<Omega,exp(-W)S(b)exp(W)Omega>.                     (6)
```

Let `V'=S(b)V`, `V(0)=1`. Anti-Hermiticity makes `V` unitary, and

```text
V(s)Omega=exp(integral_0^s c(t)dt) phi(s).                (7)
```

The scalar is nonzero. Unitarity fixes its modulus to `1/||phi(s)||`.
Its phase need not vanish for a general complex-valued creator path,
even when the path parameter is real. The resulting vector state and
vacuum projection are exactly those of `phi(s)`; no scalar-phase
assumption is needed for transfer conjugation.

If a symmetry preserves the product vacuum and the given creator path,
it intertwines `T_w`, (2), and its unique solution. The chart preserves
that symmetry. If the creator path splits over disjoint link components,
the Neumann series remains a sum of component families; `S` and `V`
factor over those components. In particular the chart is the identity
on an isolated free singleton.

## 3. A uniform multivariate holomorphic chart

Replace the scalar coupling times the magnetic sum by
`sum_p z_p V_p`, with independent complex plaquette couplings. The
rooted-contraction and magnetic-flow proofs use only the local incidence
bound, the bound `||V_p||<=J_star`, and the maximum magnitude of the
couplings. Replacing every occurrence of `|u|` in those majorants by
`max_p |z_p|` leaves their constants unchanged. The same holomorphic
contraction proof and half-flow consequently give

```text
w(z) holomorphic on max_p|z_p|<u_star,
||w(z)||_(sigma0)<=1/8.                                  (8)
```

This is a finite-variable polydisk statement, uniform in the number of
variables. Its analytic branch agrees with the previously identified
actual finite vacuum germ. Positivity is only used for its stated real
Perron interpretation, not for holomorphic construction at complex `z`.

Put

```text
r=u_star/4,  nu=log(2)/2.
```

For `max|z_p|<=r` and `0<=s<=1`, apply Cauchy's estimate on the circle
`|t-s|=1` to `t -> w(tz)`. It stays inside `max|tz_p|<=u_star/2`, so

```text
||d_s w(sz)||_(sigma0)<=1/8.                             (9)
```

Since `sigma0-nu>=nu>=1/3` and `e>=8/3`,

```text
M1(w;nu) <= (1/8)/(e(sigma0-nu)) <= 9/64.
```

Using `a_nu<=1/8`, `exp(-2nu)=1/2`, and `exp(1/4)<=4/3`, (1) gives

```text
theta <= 2 (1/2)(4/3)(9/64)=3/16 <=1/4.                 (10)
```

### 3.1. Holomorphic complexification of the real-linear equation

Adjoint is not holomorphic. To extend the chart, use the conjugate
Hilbert spaces and the holomorphic family

```text
w#(z)=overline(w(conjugate(z))).
```

Regard a lowering family `c` as an independent vector in the conjugate
creator space. Denote by `T(w)c` the complex-linear-in-`c` version of the
lowering expression in Section 2, and solve the doubled system

```text
b-T(w(sz))c = d_s w(sz),
c-T(w#(sz))b = d_s w#(sz).                              (11)
```

Both off-diagonal maps satisfy (10). On the direct-sum maximum norm their
off-diagonal operator therefore has norm at most `1/4`. Its Neumann
inverse is holomorphic in the couplings. Equations (9)-(11) give

```text
max(||b(s,z)||_nu,||c(s,z)||_nu)<= (4/3)(1/8)=1/6.        (12)
```

At real couplings conjugation swaps the two equations; uniqueness implies
`c=overline(b)`. Thus the holomorphic generator

```text
S(s,z)=sum_X (a_X(b_X(s,z))-lower_X(c_X(s,z)))             (13)
```

restricts to the anti-Hermitian generator of Section 2. At complex
couplings it need not be anti-Hermitian. Its holomorphic finite-volume
evolution remains invertible, with inverse determined by the usual
inverse evolution equation. No holomorphic continuation of an adjoint
or of the common-filter spectral-flow chart has been assumed.

## 4. Connected active witnesses and assigned interaction supports

The multivariate coefficient argument of
`G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md` applies to the
actual symmetric half-flow creators. A nonzero creator coefficient has
a connected active-plaquette set, and its exact support lies inside
that set's full link footprint. The conjugate family has the same
property.

Every nonzero monomial in `T(w)c` uses at least one `w` input. Each such
input has an exact support touching the lowering input support. Hence
its connected active witness touches the lowering input's witness in a
link. The union of these witnesses is connected. A degree-`n`
coefficient of (11) receives only finitely many Neumann terms because
every application adds at least one positive degree. Induction proves:

```text
S_alpha=0 unless the active plaquettes of alpha are connected;
S_alpha acts inside their full link footprint Y_alpha;
|Y_alpha|<=3|alpha|+1.                                   (14)
```

The footprint in (14) is the **assigned** support of the interaction.
It may strictly contain every individual exact excited support in the
coefficient. Keeping this larger footprint retains the locality of the
coupling dependence and compatibility with induced subsystems.

For `n=|alpha|>=1`, Banach-valued multivariate Cauchy estimates in the
polydisk of radius `r`, followed by summing the rooted coefficient
bounds over the links of `Y_alpha`, give

```text
||S_alpha(s)|| <= 2 |Y_alpha| (1/6) r^(-n)
                = |Y_alpha|/3 r^(-n).                  (15)
```

The factor two here is appropriate: the two independent holomorphic
families in (11) are bounded separately. It does not replace the sharper
real local-block identity (4).

These statements also prove exact coefficient stabilization in the
interior of growing boxes, or in faithful interior charts of periodic
volumes. Each coefficient is computed on its finite active footprint.
No coefficient outside that footprint or absent from an induced
subsystem is silently retained.

### 4.1. An explicit witness interaction majorant

Plaquettes have at most twelve neighbors sharing a link. A connected
set of `k` plaquettes containing a specified plaquette can be encoded
by a deterministic depth-first walk of length `2(k-1)`, so their number
is at most `144^(k-1)`. There are at most four choices of a plaquette
through a fixed link. For total degree `n`, distribute positive
multiplicities over the `k` active plaquettes in
`binomial(n-1,k-1)` ways. Therefore the number of connected degree-`n`
multi-indices whose footprint contains a specified link is at most

```text
4 sum_(k=1)^n 144^(k-1) binomial(n-1,k-1)
  =4*145^(n-1).                                        (16)
```

Assign each diagonal-coupling term `u^n S_alpha(s)` to `Y_alpha` and
keep distinct terms with the same footprint, or sum them there. Define
the resulting interaction norm

```text
||S(s;u)||_rho^assigned
  =sup_i sum_(Y contains i) exp(rho|Y|)||S_Y(s;u)||.
```

For `rho>=0` and `q=145 exp(3rho)|u|/r<1`, (14)-(16) imply

```text
||S(s;u)||_rho^assigned
  <= (4 exp(rho)/435) q(4-q)/(1-q)^2.                   (17)
```

This bound is uniform in `s`, volume, and mesh. The path has length one,
so it also bounds the integrated generator norm. Two unitary legs cost
at most twice its right side. A nonzero assigned support is a connected
plaquette footprint; in the link graph its diameter is at most `|Y|-1`.
Thus a margin in `rho` also supplies a spatial exponential weight.

The geometric tail in (17) gives absolute coefficient convergence and
quantitative local convergence after any strict weight margin. It is
the bound needed to compare volume-dependent induced-subsystem charts,
not just a bound on the exact excited support of their vacuum vectors.

## 5. Transport of local sources with a support margin

Here is a general consequence of a bound such as (17). It applies to
the new chart and its inverse. Let an anti-Hermitian interaction `S(s)`
have assigned norm at weight `rho_plus`, and put

```text
g(s)=||S(s)||_(rho_plus)^assigned,
G=integral_0^1 g(s) ds.
```

Choose `rho0<rho_plus` and define
`rho(s)=rho0-2 integral_0^s g(t)dt`. Suppose `rho(1)>=0`.
If an operator family evolves by `dot A=[S,A]`, assigning every
commutator to the union of its intersecting input supports, then

```text
||A(1)||_(rho0-2G)^assigned
 <= exp(2G/(e(rho_plus-rho0))) ||A(0)||_(rho0)^assigned.  (18)
```

To prove this, use `||[S_X,A_Y]||<=2||S_X||||A_Y||` and sum separately
according to whether the output root is in `X` or in `Y`. With `M1`
denoting the additional support-cardinality moment, the rootwise bound
is

```text
r_i([S,A];rho)
 <=2 g(s) m_i(A;rho)+2 m_i(S;rho)||A||_rho.
```

The decreasing weight cancels the first term. The second satisfies
`M1(S;rho)<=g(s)/(e(rho_plus-rho0))`, by
`x exp(-delta x)<=1/(e delta)`. Taking the upper Dini derivative of the
maximum rooted norm and integrating proves (18). Finite-volume
solutions can first be obtained in any fixed lower weight and then
estimated this way; the resulting absolute sums pass to the limit.

For example, if (17) gives

```text
rho_plus=1+log(2),  G<=1/2500,
```

take `rho0=log(2)+1/2`. Since `e>=2`, (18) yields the convenient weaker
bound

```text
||A(1)||_(log(2))^assigned
 <= exp(1/1250) ||A(0)||_(log(2)+1/2)^assigned.           (19)
```

For a fixed bounded source `O` assigned to a finite connected link set
`R`, every term obtained by this commutator construction contains `R`.
The rooted bound at any one link of `R` therefore bounds its entire
operator-norm sum. Its initial norm is
`exp((log(2)+1/2)|R|)||O||`. Every output support is connected, and

```text
exp(log(5/4)|Y| + log(8/5) diameter(Y))
 <= exp(log(2)|Y|).                                     (20)
```

Thus (19) provides both the desired source-cardinality factor `5/4`
and an additional spatial exponential weight. An arbitrary finite
source may be assigned to any fixed finite connected set containing
its actual support. The resulting estimate depends on that chosen
source set but is independent of total volume and mesh.

The differential equation above directly describes `V O V*`. The
inverse conjugation `V* O V` is the same construction with the
time-reversed generator `-S(1-s)`, and has the identical integrated
bound. It is not necessary to identify the two time-dependent
Heisenberg differential equations.

For infinite-volume convergence, work at any coupling for which these
inequalities hold with a strict margin. The holomorphic doubled chart
and its inverse obey the same commutator bound at complex couplings in
a slightly larger disk; anti-Hermiticity was not used to prove (18).
Their degree-`n` source coefficients use only finitely many connected
active plaquette witnesses attached to `R`, so they stabilize in every
sufficiently large interior volume. The uniform source bound on the
larger disk and Cauchy's estimate bound both coefficient tails by a
geometric series. Hence both finite-volume conjugations converge in
operator norm on each fixed local observable, uniformly on the unit
ball of its fixed finite-support algebra. Periodic volumes use faithful
interior charts for the finite active footprints.

On real couplings the finite-volume maps are isometric. Their local
limits and the inverse limits are inverse: approximate the image of a
local observable by a local observable, use its operator-norm local
convergence, and use isometry to control the approximation error. The
limits therefore extend to inverse automorphisms of the quasi-local
algebra. Equation (7) identifies their transported product state with
the same selected finite-volume Wilson vacuum limit. This is another
chart of that state; it does not identify the new automorphism with the
former NSY one.

## 6. Scope, provenance, and next use

The analytic inputs are the rooted Wilson contraction, the actual
symmetric half-flow creator identity, and the exact connected active
plaquette factorization. Sections 2-5 provide the additional inversion,
holomorphic complexification, assigned-support bounds, and source
transport arguments. The finite controls accompanying this continuation
test narrower tangent identities and estimates; a finite matrix check
is not a substitute for the uniform arguments here.

The new chart preserves the actual vacuum line, induced component
factorization, and the free singleton chart. Therefore the partition
activity extraction lemma applies to its dressed finite transfers as
well. Those activities belong to this chart; they are not asserted to
equal the activities of the common-filter chart. Bounding the full
ordered transfer and its extensive scalar normalization requires the
companion operator-activity argument. Neither equality of vacuum states
nor (18) alone establishes an excited Riesz-range identification or an
actual Wilson excitation spectrum.
