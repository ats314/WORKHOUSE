# A uniform weighted activity bound for the actual Wilson transfer

5 September 2026. Additive continuation from GitHub main
`3731ca556da8fc0c86d6cabd761dd5840651d37f` (PR #100).

The missing cardinality-weighted operator estimate now holds on an explicit
nonzero coupling interval. The construction uses the local creator-velocity
unitary in the [companion chart theorem](G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md).
This is a different chart from the earlier parent spectral flow. Its
activities are extracted anew; no equality on their excited blocks is assumed.

## 1. Statement, regime and precise consequence

Use the actual calibrated Wilson transfer on a finite open or periodic cubic
link geometry, with four distinct links per plaquette, at most four
plaquettes per link and at most twelve other plaquettes sharing a link with
a plaquette. Link Hilbert spaces may be infinite dimensional. The bounded
self-adjoint magnetic terms have norm at most `J>0`. The additive free
kinetic operator has one-link excited gap at least `gamma>0`. Retain the
compact, self-adjoint, positivity-improving real Wilson kernel premise that
identifies the established analytic vacuum with the Perron vacuum.

Choose

```text
mu >= max(gamma tau0/2, log(2)+gamma tau0/4),
u_star = min(9 gamma/(309680 J exp(4mu)),
             9/(8450 tau0 J exp(4mu))),
s_sp = log(5/4)/gamma,
0 < tau <= tau0 <= s_sp/4,
m = ceil(s_sp/tau),  s=m tau <= s1=s_sp+tau0,
r = u_star/4,
u0 = u_star/1252800000.
```

Let `V_X(u)` be the companion creator-velocity unitary on every induced
finite link subsystem `X`, with the same coupling path and `V_X(0)=I`.
Use each subsystem's own actual Perron eigenvalue `b_X` of `T_X^m` and put

```text
G_X = b_X^(-1) V_X^* T_X^m V_X,   G_empty=1,
D_i = exp(-s K_i).
```

**Theorem.** For real `|u|<=u0`, partition inversion of this induced family
gives unique self-adjoint activities `F_i=0`, with

```text
F_X P_X=P_X F_X=0,
G_Lambda = sum_(disjoint families A)
             (tensor_(X in A) F_X) tensor D_(Lambda outside union A),

sup_(Lambda,tau,i) sum_(X contains i) 2^|X| ||F_X|| <= 1/2500.       (1)
```

Every nonzero activity support is a connected union of retained plaquettes.
There is no representation cutoff. The bound is on full operator norms,
uniform in finite volume and temporal mesh. It supplies the earlier target
with `(5/4)^|X|`, and the stronger combined estimate

```text
sup_i sum_(X contains i)
   (5/4)^|X| exp(log(8/5) diameter(X)) ||F_X|| <= 1/2500,            (2)
```

where distance is in the retained plaquette link graph, intrinsically on
periodic systems. Indeed `diameter(X)<=|X|-1` on a connected support.

The [excited-window bridge](G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md),
Theorem 5, now applies to this actual family. Since `delta<=4/5`, it gives

```text
||G_Lambda-D_Lambda|| <= 1/998 < (1024/15625)/10.                  (3)
```

In the neutral physical charge-odd sector, the calibrated free-window
premise therefore gives a complete isolated finite-volume plaquette shell
on this common coupling interval. On the periodic lattices covered by that
premise its rank is `3 L^3`. The contour projection is close to the free
projection and includes every eigenstate inside the contour, including
states that a selected source might fail to detect.

This is an actual Wilson transfer result. It uses the established physical
free-window theorem for the last spectral conclusion; the abstract norm
estimate needs only the stated tensor-product kinetic gap. It does not
identify an infinite-volume Riesz range or prove a uniformly invertible
literal-source frame. The companion theorem supplies weighted transport of
local source operators; source-frame invertibility and the complete
thermodynamic range identification are subsequent statements.

The constants are deliberately conservative. The theorem establishes a
nonzero common interval; it does not claim this interval is optimal or
numerically useful for phenomenology.

## 2. Established creator inputs and assigned operator supports

The rooted contraction and symmetric-creator theorems apply also to
independent complex plaquette variables with `sup_p |z_p|<u_star`.
Their norm estimates use the maximum magnetic coupling, and their contraction
and magnetic-flow arguments are unchanged. The symmetric creators obey
`||w(z)||_sigma0<=1/8`, with `sigma0=mu-gamma tau0/4>=log(2)`.

The companion theorem solves the real-linear creator-velocity equation,
complexifies it as a pair of holomorphic equations, and proves that the
generator along `t -> tz`, `0<=t<=1`, has connected coefficients

```text
S(t,z) = sum_(connected nonzero multiindices alpha)
             z^alpha S_alpha(t),
||S_alpha(t)|| <= (|Y_alpha|/3) r^(-n),
n=|alpha|,   Y_alpha=union of the active plaquettes,
|Y_alpha| <= 3n+1.                                                (4)
```

Each `S_alpha` is assigned to its entire active footprint `Y_alpha`, even
when the exact excited support of one of its creator vectors is smaller
or disconnected. Its coefficient is computed on its minimal active
subsystem and agrees in every larger subsystem after embedding by the
identity. This assigned-support convention is essential for the following
operator expansion.

At a fixed link, the number of connected degree-`n` active monomials is at
most

```text
4 * 145^(n-1).                                                    (5)
```

There are at most four choices of a root plaquette. A connected set of `k`
plaquettes containing it injects, by a fixed depth-first spanning-tree walk,
into at most `12^(2k-2)=144^(k-1)` walks. Positive multiplicities summing
to `n` have `binom(n-1,k-1)` choices. Summing over `k` gives (5). This is
an upper bound and is valid on finite periodic geometries as well.

For a weight `rho>0`, put

```text
q = 145 exp(3rho) |u|/r.
```

When `q<1`, (4)-(5) prove absolute convergence in the assigned-support
interaction norm. The integrated primitive cost of both unitary legs is
bounded by

```text
E_U <= (8 exp(rho)/435) q(4-q)/(1-q)^2.                            (6)
```

Indeed each of the two legs has parameter length one, and
`sum_(n>=1)(3n+1)q^n=q(4-q)/(1-q)^2`. The inverse unitary is the
oppositely ordered evolution with the negative generator and has the same
integrated norm cost.

## 3. The actual Perron normalizer has a connected local expansion

This step retains the subsystem-dependent scalar normalizers. They are
neither replaced by an extensive norm bound nor discarded as vacuum terms.

Use the endpoint fixed point `v(z)` and its full magnetic creator flow
`v(t,z)`, `0<=t<=tau`, from the rooted-contraction theorem. Its moving
weight is nonnegative, and

```text
||v(t,z)||_(mu-gamma t/2) <= R=1/4.
```

Writing `A(v)` for the creator sum, the exact scalar equation is

```text
c(t,z) = sum_p c_p(t,z),
c_p(t,z) = z_p <Omega, v_p exp(A(v(t,z))) Omega>,
lambda(z) = exp(integral_0^tau c(t,z) dt),
log b(z) = m integral_0^tau c(t,z) dt.                             (7)
```

Here `lambda` is the fine-transfer eigenvalue, and the logarithm is the
analytic branch equal to zero at the free point. The nonvanishing scalar
normalizer and exact endpoint equation prove (7); at real coupling this
is precisely the actual Perron eigenvalue, with `b=lambda^m`.

Only right creators supported entirely inside plaquette `p` contribute to
the vacuum matrix element in `c_p`. Any excited link outside `p` survives
the magnetic action and is killed by the vacuum bra. Thus

```text
sum_(X subset p) ||v_X|| <= 4R=1,
|c_p(t,z)| <= |z_p| J exp(4R) <= r J e                            (8)
```

on the independent-variable polydisc of radius `r`. This estimate is
independent of volume and of the dimensions of the link spaces.

Let `ell_alpha=[z^alpha] log b`. When inactive variables are zero, the
transfer and its vacuum normalize component by component. Consequently
the analytic logarithm is additive, so `ell_alpha=0` for disconnected
active monomials. Cauchy extraction on the minimal active subsystem,
which has at most `n=|alpha|` active plaquettes, yields

```text
|ell_alpha| <= n s1 J e r * r^(-n).                               (9)
```

Assign `ell_alpha I` to the active footprint `Y_alpha`. The identity
operator can be assigned this support even though it acts trivially on
each link: the label specifies which induced subsystem contains the
coefficient. It is not an assertion that identities on different assigned
supports are linearly independent.

The scalar factor `b^(-1)` is therefore a length-one evolution with local
generator `-sum_alpha u^|alpha| ell_alpha I_(Y_alpha)`. Its integrated
primitive cost is at most

```text
E_b <= (4 exp(rho)/145) s1 J e r * q/(1-q)^2.                     (10)
```

Absolute convergence follows from the same connected count as (6), so
this scalar expansion equals the actual analytic logarithm in each
finite subsystem. All induced subsystems use the same coefficients.

## 4. Primitive contour and an operator connected-cluster lemma

Represent `V^* T^m V exp(-log b)` as an ordered contour of bounded local
insertions interleaved with the free factors. The two unitary legs use (4).
The magnetic half factors in `T^m` have total magnetic duration `m tau=s`,
including both endpoints. Every kinetic factor is the tensor product of
one-link contractions. The scalar leg uses (9). With no insertions, the
contour is exactly the free product `D=exp(-sK)`.

The magnetic primitive cost is

```text
E_M <= 4 exp(4rho) s1 J |u|.                                     (11)
```

The contour may be parameterized by finitely many intervals separated by
kinetic contraction jumps. No inverse kinetic factor and no unbounded
kinetic commutator is used. It acts on the full, untruncated Hilbert space.

Here is the general estimate, valid for arbitrary bounded local insertions
with a common induced-subsystem interpretation. Let

```text
a_Y = integral_contour ||J_Y(t)|| dt,
E = sup_i sum_(Y contains i) exp((kappa+h)|Y|) a_Y,
kappa>=0,  0 <= E <= h,  h>0.                                    (12)
```

Then grouping the absolutely convergent ordered-insertion expansion into
components of the overlap graph gives a disjoint-support expansion whose
connected activities satisfy

```text
sup_i sum_(X contains i) exp(kappa|X|) ||F_X|| <= E.               (13)
```

**Proof, including operator order.** A term with `n` insertions has an
ordered integration simplex. Inside any connected component keep its
actual insertion order and all internal kinetic contractions. Insertions
on disjoint supports commute and their free contractions tensorize.
Shuffling their ordered times partitions the global integration simplex.
Thus disconnected components factor exactly, while their connected
components give local activities. Norms of each component are bounded
by the product of the insertion norms because the kinetic factors are
contractions. Overlapping insertions need not commute.

After this norm bound, integration of the permutation-symmetric positive
majorant gives the usual `1/n!` times the product of the `a_Y`. Repeated
supports are allowed. The weight of the union is at most the product of
the support weights; put `b_Y=exp(kappa|Y|)a_Y`.

To bound the sum meeting a fixed link, mark one insertion whose support
contains the link. This overcounts a component at least once. Its connected
overlap graph has a spanning tree, so replacing connectedness by a sum
over rooted labeled spanning trees only increases the positive sum.
The resulting rooted-tree series obeys the monotone recursion

```text
T_Y = b_Y exp(sum_(Z intersects Y) T_Z).
```

Its finite-height iterates start with `b_Y` and have supersolution
`T_Y<=b_Y exp(h|Y|)`, because

```text
sum_(Z intersects Y) b_Z exp(h|Z|) <= |Y| E <= h|Y|.
```

Hence its root sum is at most
`sum_(Y contains i) b_Y exp(h|Y|)<=E`. Monotone convergence proves the
tree bound and absolute convergence of the connected sum, giving (13).
One can first retain finitely many primitive types and insertion orders;
the same positive bound permits removal of these truncations. This proves
the lemma without any dimension-dependent matrix estimate.

The primitive coefficients here agree on every induced subsystem. Thus
the contour activities reconstruct every `G_X`, with the same `D_i` on
unoccupied sites. The [partition-extraction lemma](G18_WILSON_ACTIVITY_EXTRACTION_20260905.md)
proves uniqueness of such a family. They therefore equal the partition
cumulants of the new induced family. Since that family is self-adjoint
and fixes the local vacuum, its activities are self-adjoint and annihilate
both vacuum legs. This obtains anchoring after the exact connected sum;
no claim that each primitive insertion is vacuum-annihilating is needed.

All primitive assigned supports are connected unions of active plaquettes.
An overlap-connected union of them is again connected. The same conclusion
also follows from component factorization of the induced family. In
particular the singleton activities, and all activities on two or three
links, vanish.

## 5. Explicit evaluation of the sufficient smallness condition

Take `kappa=log(2)`, `h=1`, so `rho=1+log(2)`. First,

```text
s1 gamma <= (5/4) log(5/4) < 1,
s1 J r <= 9 s1 gamma/(1238720 exp(4mu)) < 1.                       (14)
```

The harmless estimate `s1 J r<=1` therefore follows from the first branch
in the definition of `u_star`, uniformly even as `tau` tends to zero.

Combining (6), (10) and (11), with `s1 J r<=1`, gives

```text
E <= (4 exp(rho)/145)
       [q + (e + 8/3) q/(1-q)^2].                               (15)
```

For `q<=1/2`, use `exp(rho)=2e<6`, `e<3` and `(1-q)^(-2)<=4`:

```text
E <= (568/145) q.                                                (16)
```

Finally `exp(3rho)=8e^3<216` and `|u|<=u_star/1252800000` imply

```text
q = 145 exp(3rho) |u|/r <= 1/10000,
E <= 568/1450000 < 1/2500 < 1.                                  (17)
```

Equations (12)-(13) now prove (1), with a genuine cardinality margin over
the requested `(5/4)^|X|`. The norm consequence (3) uses

```text
eta <= 1/2500,
eta / (e (log(5/4)-eta))
  <= (1/2500) / (2 (1/5-1/2500)) = 1/998.
```

The calibrated rounded shell margin is `g_star=1024/15625`; direct
rational comparison gives `1/998<g_star/10`. Gauge, charge-conjugation and
one-form symmetries are preserved by the creator-velocity equation, its
unique inverse, and the resulting unitary path. Restricting the full norm
bound to the physical neutral odd sector is therefore legitimate. The
existing contour argument then proves the finite-volume spectral assertion.

## 6. What remains, and reproducibility scope

The requested weighted activity estimate is established for the new chart.
It is not a claim that the earlier common-filter spectral-flow activities
coincide with it or obey the same estimate. Those earlier exact activities
and their algebraic theorem remain unchanged as historical and mathematical
inputs. The [companion chart theorem](G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md)
also controls local source transport with an assigned-support margin.

The next physical task is to construct the compatible thermodynamic
operator/Riesz range in the transported representation and prove uniform
invertibility and totality of the projected literal-source frame. Weighted
source locality is an input to that task, not the frame conclusion itself.
Temporal sharp-shell matching and spatial continuum statements retain
their own hypotheses. G18 and G19 are not globally closed by (1).

The full statements here are analytic theorems. The companion exact
finite-tensor controls check the creator-velocity identities, complex
phase and component behavior; rational controls verify the displayed
constants. Those controls do not formalize the full infinite-dimensional
norm argument or prove it by finite sampling. The primitive contour/tree
argument, normalization calculation and cost sums were derived and checked
independently before integration into this note.
