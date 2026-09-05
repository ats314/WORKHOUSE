# A convergent rooted chart for the actual Wilson vacuum

Date: 5 September 2026. Analytic theorem and explicit constants.

This proves a finite-volume estimate uniform in volume, representation
dimensions, and temporal mesh. It replaces the same-weight estimate (17)
in `G18_WILSON_ENDPOINT_GAUGE_AND_MAJORANT_20260905.md` by an estimate with
an explicit time-dependent loss of support weight, which the full kinetic
resolvent restores. It does not assert the original uncomposed (17).
The companion `G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md` constructs the infinite-lattice
coefficient family. A physical state and the unitary operator chart require
further arguments.

## 1. Hypotheses and explicit constants

There are finitely many links. Each plaquette uses four distinct links,
and each link belongs to at most four plaquettes. The link Hilbert spaces
may be infinite dimensional. Each has a unit vacuum vector and its
orthogonal complement. Write `H'_X` for the tensor product of excited
factors on a nonempty exact support `X`. A creator family is
`v=(v_X)`, `v_X in H'_X`; its creator is
`hat v_X=|v_X><Omega_X|`, tensored with the identity outside `X`.

The bounded plaquette operators satisfy `||v_p||<=J_*`, with `J_*>0`.
Wilson multiplication operators are a special case. Put `V=sum_p v_p`.
The free kinetic operator is a sum of self-adjoint link operators that
annihilate their vacua and have excited gap at least `gamma>0`. Thus on
each nonempty exact support, `K_X>=gamma|X|`.

Fix `tau_0>0`, `R>0`, and `mu>=gamma tau_0/2`. For `sigma>=0` define

\[
 r_\ell(v;\sigma)=\sum_{X\ni\ell}e^{\sigma|X|}\|v_X\|,
 \quad m_\ell(v;\sigma)=\sum_{X\ni\ell}|X|e^{\sigma|X|}\|v_X\|,
 \quad \|v\|_\sigma=\max_\ell r_\ell(v;\sigma),
\]

\[
 \|v\|_{\sigma,-1}=\max_\ell\sum_{X\ni\ell}
                   \frac{e^{\sigma|X|}}{|X|}\|v_X\|.
 \tag{1}
\]

Let `E_j(x)=sum_{k=0}^j x^k/k!` and define the following polynomials in
the nonnegative real variable `r` (the fixed weight in their constants is
`mu`, not a variable):

\[
 A(r)=16J_*e^{4\mu}E_4(4r)^2,
 \qquad B(r)=32J_*e^{4\mu}E_3(4r)E_4(4r),
\]

\[
 C(r)=A(r)+5rB(r),\qquad L(r)=C'(r).
 \tag{2}
\]

All coefficients are nonnegative and `L(R)>0`. Set

\[
 u_* =\min\left\{
 \frac{\gamma}{2B(R)},\quad
 \frac{R}{2\tau_0 A(R)},\quad
 \frac{\gamma R}{4C(R)},\quad
 \frac{\gamma}{8L(R)}\right\}>0.
 \tag{3}
\]

These constants are deliberately sufficient rather than optimized.

For a fully numerical choice of creator radius, take `R=1/4` and put
`M_*=J_* exp(4mu)`. Then `E_4(1)=65/24`, `E_3(1)=8/3`, and
`E_2(1)=5/2`, so

\[
 A(R)=\frac{4225}{36}M_*,\quad B(R)=\frac{2080}{9}M_*,
 \quad C(R)=\frac{1625}{4}M_*,\quad
 L(R)=\frac{38710}{9}M_*.
 \tag{3a}
\]

Indeed `A'=4B` and
`L(r)=9B(r)+5rB'(r)`; explicitly
`L(r)=M_*[288E_3(4r)E_4(4r)+640r(E_2(4r)E_4(4r)+E_3(4r)^2)]`.
The last bound in (3) is stricter than its first and third bounds at
this radius. Hence (3) simplifies exactly to

\[
 \boxed{u_*=
 \min\left\{\frac{9\gamma}{309680J_*e^{4\mu}},
             \frac9{8450\tau_0J_*e^{4\mu}}\right\}.}
 \tag{3b}
\]

The resulting fixed-point ball has radius `R/4=1/16`.

## 2. Rootwise bounds for the polynomial creator vector field

Define

\[
 Y_u(v)=Qe^{-\widehat v}(uV)e^{\widehat v}\Omega_0.
 \tag{4}
\]

The result is identified with its nonempty exact-support family. The
creator algebra is nilpotent at finite volume. Creators commute; products
of creators with intersecting supports vanish. For one plaquette put
`W_p=sum_{X: X intersects p}hat v_X`. The creators away from `p`
cancel in its conjugation, and `W_p^5=0`, because five mutually disjoint
supports cannot each use one of four plaquette links. Therefore

\[
 e^{-\widehat v}v_pe^{\widehat v}\Omega_0
 =\sum_{a,b=0}^4\frac{(-1)^a}{a!b!}
                       W_p^av_pW_p^b\Omega_0.
 \tag{5}
\]

Expand a term as an ordered tuple of `k=a+b` input creators. Its norm is
at most `J_* product_i ||v_{X_i}||`. Any nonzero such term has every input
excitation outside `p` still excited at output. Indeed the magnetic
operator acts only on `p`; if a left creator intersects a right creator
outside `p`, its vacuum bra kills that term. Left-left and right-right
intersections also kill their respective products. Thus outside `p` the
exact excited support is fixed to the union of input supports there.

Consequently the final decomposition into exact output supports varies
on at most four links, giving at most sixteen orthogonal pieces. The sum
of their norms is at most four times the norm of the undecomposed term.
For each nonempty output support `Z`,

\[
 |Z|\le4+\sum_i|X_i|,\qquad |X_i|\le|Z|+4\le5|Z|.
 \tag{6}
\]

For `0<=sigma<=mu`, the output weight is at most
`exp(4mu) product_i exp(sigma|X_i|)`.

Suppose `||v||_sigma<=r`. Each unrooted creator touching a fixed
plaquette has total weighted norm at most `4r`. To bound the output sum
at a root `ell`, there are two possibilities; overcounting is harmless:

* If the root is in `p`, there are at most four plaquettes. The projection
  factor four, the plaquette count four, and the sum over `a,b` give
  `A(r)`.
* Otherwise the root belongs to an input creator, in one of the `k`
  positions. For that support `X`, at most `4|X|` plaquettes touch it.
  The remaining positions cost `(4r)^(k-1)`. Since
  `sum_{a,b=0}^4 (a+b)x^(a+b-1)/(a!b!)=2E_3(x)E_4(x)`, their total
  contribution is `B(r)m_ell(v;sigma)`.

This proves the rootwise ordinary estimate

\[
 \sum_{Z\ni\ell}e^{\sigma|Z|}\|Y_u(v)_Z\|
 \le |u|\{A(r)+B(r)m_\ell(v;\sigma)\}.
 \tag{7}
\]

For the norm with `1/|Z|`, the first case is unchanged. In the second
case, (6) replaces the placement factor `|X|/|Z|` by at most five.
The same counting then gives

\[
 \boxed{\|Y_u(v)\|_{\sigma,-1}\le |u|C(r).}
 \tag{8}
\]

The counting is multilinear in the norms of the individual input
creators. In a degree-`k` term, telescope the difference between inputs
`v` and `w` into `k` terms, with one input replaced by `v-w` and all
others bounded by `r`. This multiplies each degree-`k` coefficient of
`C(r)` by `k` and lowers its power of `r` by one. Thus

\[
 \boxed{\|Y_u(v)-Y_u(w)\|_{\sigma,-1}
 \le |u|L(r)\|v-w\|_\sigma}
 \quad(\|v\|_\sigma,\|w\|_\sigma\le r).
 \tag{9}
\]

No Hilbert-space dimension enters (7)--(9).

## 3. Moving-weight existence, without an abstract scale theorem

Consider the finite-volume polynomial differential equation

\[
 \dot v(t)=Y_u(v(t)),\qquad v(0)=v_0,
 \quad \sigma(t)=\mu-\gamma t/2.
 \tag{10}
\]

Assume `||v_0||_mu<=R/2`, `|u|B(R)<=gamma/2`, and
`|u|tau_0 A(R)<=R/2`. For as long as
`||v(t)||_{sigma(t)}<=R`, the upper right derivative of each root sum
satisfies, by the triangle inequality for derivatives of vector norms
and (7),

\[
 D^+ r_\ell(v(t);\sigma(t))
 \le-\frac\gamma2m_\ell(v(t);\sigma(t))
   +|u|\{A(R)+B(R)m_\ell(v(t);\sigma(t))\}
 \le |u|A(R).
 \tag{11}
\]

The negative derivative of the moving exponential weight absorbs the
support moment at the same root. The maximum over the finitely many
roots obeys the same upper bound. A first-exit argument gives

\[
 \boxed{\|v(t)\|_{\sigma(t)}
       \le \|v_0\|_\mu+|u|tA(R)\le R,
       \qquad0\le t\le\tau_0.}
 \tag{12}
\]

The assumption on `mu` keeps every weight in (10) nonnegative. The
argument applies also to complex `u` and complex creator families.

For completeness, at fixed finite volume the family space is a finite
direct sum of Hilbert spaces, and (5) is a continuous polynomial vector
field on it. Local existence and uniqueness follow by Picard iteration
on a norm ball, where that polynomial has a finite Lipschitz constant.
The same argument gives holomorphic dependence on initial data and on
`u`, since the Picard iterates are holomorphic and converge locally
uniformly. Equation (12) controls an ordinary family norm as well:
`sum_X ||v_X(t)||<=number_of_links * R`. On this bounded set the
polynomial field and its derivative are bounded, so the local solution
continues up to `tau_0`. This also continues its holomorphic dependence.
These local continuation constants may depend on volume; the actual
existence interval and bound (12) do not.

For boundary equalities in the hypotheses, use the estimate for
`t<tau_0` and bounded continuation to the endpoint. Holomorphic claims
refer to the interiors of the parameter balls.

## 4. The solution is the exact normalized magnetic flow

Put `phi(t)=exp(hat v(t))Omega_0`. The vacuum coefficient of this vector
is one. Commutativity of creators and (4) imply

\[
 \dot\phi(t)=(uV-c(t))\phi(t),\qquad
 c(t)=\langle\Omega_0,uV\phi(t)\rangle.
 \tag{13}
\]

Here `<Omega_0|exp(-hat v(t))=<Omega_0|`, so the scalar removed by `Q`
is exactly the displayed `c(t)`. Solving this bounded linear equation
with scalar coefficient gives

\[
 \phi(t)=e^{tuV}\phi(0)
             \exp\left(-\int_0^t c(q)\,dq\right).
\]

Taking the vacuum coefficient proves

\[
 \boxed{a(t):=\langle\Omega_0,e^{tuV}\phi(0)\rangle
       =\exp\left(\int_0^t c(q)\,dq\right)\ne0.}
 \tag{14}
\]

Thus the scalar normalization cannot vanish anywhere on the constructed
interval, even for complex data in the stated domain. The ODE solution
is exactly the creator logarithm used in the endpoint note:

\[
 F_t(u,v_0)=v(t),\qquad
 N_\tau(u,v_0)=\frac1\tau\int_0^\tau Y_u(F_t(u,v_0))\,dt.
 \tag{15}
\]

These are now defined on a common finite-volume domain, with uniform
size bounds, rather than only as unspecified local germs.

## 5. Cauchy gives a uniform flow Lipschitz constant

For fixed `t`, the holomorphic map `v_0 -> F_t(u,v_0)` sends the open
ball of radius `R/2` in `X_mu` to the ball of radius `R` in
`X_{sigma(t)}`, by (12). If `||v_0||_mu<=R/4` and `||h||_mu=1`, apply
the one-variable Cauchy estimate to `z -> F_t(u,v_0+zh)` on disks with
radius approaching `R/4`. It gives

\[
 \|D_{v_0}F_t(u,v_0)h\|_{\sigma(t)}\le4.
\]

Integrating this derivative on the line segment between two points in
the smaller ball yields

\[
 \boxed{\|F_t(u,v)-F_t(u,w)\|_{\sigma(t)}
          \le4\|v-w\|_\mu,
     \qquad \|v\|_\mu,\|w\|_\mu\le R/4.}
 \tag{16}
\]

Fix `0<tau<=tau_0` and write `sigma_tau=mu-gamma tau/2`. Since
`sigma_tau<=sigma(t)` for `0<=t<=tau`, (8), (9), (12), (15), and (16)
give the precise replacement for the uncomposed estimate (17):

\[
 \boxed{\|N_\tau(u,v)\|_{\sigma_\tau,-1}\le |u|C(R),}
\]

\[
 \boxed{\|N_\tau(u,v)-N_\tau(u,w)\|_{\sigma_\tau,-1}
          \le4|u|L(R)\|v-w\|_\mu.}
 \tag{17}
\]

The factor `|u|` has been retained by integrating the vector field,
rather than estimating `F_tau-v` as a difference of two bounded maps.

## 6. The full resolvent restores the lost weight

Let `R_{tau,X}=tau/(exp(tau K_X)-1)` on each nonempty exact support,
defined by bounded spectral calculus. Monotonicity of this scalar
function and the support gap imply

\[
 \|R_{\tau,X}\|
 \le\frac{\tau}{e^{\gamma\tau|X|}-1}.
\]

For `x=gamma tau |X|>0`,

\[
 \frac{xe^{x/2}}{e^x-1}
       =\frac{x}{2\sinh(x/2)}\le1.
\]

Therefore the exact half-step smoothing estimate is

\[
 \boxed{\|\mathcal R_\tau h\|_\mu
      \le\gamma^{-1}\|h\|_{\mu-\gamma\tau/2,-1}.}
 \tag{18}
\]

It holds for arbitrary exact-support families and uses the kinetic
numerator retained in the endpoint gauge. Replacing this resolvent by
the bound `1/(gamma|X|)` would lose (18).

Define the actual composed map `G_tau(u,v)=R_tau N_tau(u,v)`. Equations
(17)--(18) prove

\[
 \|G_\tau(u,v)\|_\mu\le |u|C(R)/\gamma,
\]

\[
 \boxed{\|G_\tau(u,v)-G_\tau(u,w)\|_\mu
    \le\frac{4|u|L(R)}\gamma\|v-w\|_\mu.}
 \tag{19}
\]

For `|u|<=u_*`, (3) makes this map a self-map of the complete closed
ball `||v||_mu<=R/4` with contraction constant at most `1/2`. Hence it
has a unique fixed point in that ball. Iteration starting at zero
converges in the same rooted norm. On `|u|<u_*`, the fixed point is
holomorphic in `u`, by locally uniform convergence of the holomorphic
iterates. Every estimate and the radius (3) are independent of volume,
mesh, and link Hilbert-space dimensions.

## 7. Exact finite-volume interpretation and remaining scope

Write `C_free=exp(-tau K)` to distinguish it from the polynomial `C(r)`.
The fixed-point equation is equivalent, support by support, to
`v=C_free F_tau(u,v)`. Free transfer is multiplicative for the
disjoint-support creator product. Thus, with `phi=exp_star(v)` and
the nonzero normalizer supplied by (14),

\[
 \lambda\phi=C_{\rm free}e^{\tau uV}\phi,
 \qquad \lambda=\langle\Omega_0,e^{\tau uV}\phi\rangle.
 \tag{20}
\]

Restoring the magnetic endpoint gives an eigenvector of the actual
symmetric Wilson transfer. Near zero, this eigenpair agrees with the
isolated free-vacuum eigenpair by analytic uniqueness.

To identify it throughout the real interval `|u|<u_*`, assume the actual
finite-volume Wilson transfer is compact, self-adjoint and positivity
improving there, as supplied by its positive link kernel and positive
magnetic endpoints. Its top eigenvalue is then simple for every such
real coupling. Let `b(u)` be that top eigenvalue. It is continuous in
`u`, because the finite-volume bounded transfer is norm-continuous.
The constructed `lambda(u)` is continuous and is an eigenvalue with a
nonzero eigenvector for every `u` in the interval. The set where
`lambda(u)=b(u)` contains a neighborhood of zero and is relatively
closed by continuity. It is also relatively open: at a point of
equality the simple top eigenvalue is isolated, and continuity plus
local spectral uniqueness keeps the constructed eigenvalue on that
same branch. Connectedness of the real interval proves equality
throughout it. This identifies the constructed coordinates with the
actual Perron branch under the stated Wilson-kernel premise.

The contraction iterates used above are those of `G_tau=R_tau N_tau`.
They are not being identified with normalized positive-transfer power
iterations, whose creator map is instead `C_free F_tau`.

The theorem proved here is a uniform finite-volume construction of
connected nonunitary vacuum coordinates. The companion
`G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md` constructs their
infinite-lattice coefficient family using connected-witness locality.
Control of a unitary anchored operator chart and the excited
spectral/source bridge are not being inferred from (19) alone.

No external Banach-scale theorem is assumed: the proof uses the explicit
rootwise differential inequality, finite-volume polynomial Picard
iteration and continuation, a one-variable Cauchy estimate, and the
displayed spectral-calculus inequality.

## 8. Provenance and verification

This continuation starts from the endpoint-gauge equation and fixed-order
chart committed at `e6380a25a88ea4764deeb32358967ee44e3ecfe4`, after live
comparison with GitHub main at `f36db9e1a447ff23ed72faf43783f886958a43ef`.
The calibrated kinetic input is the one in the supplied September 4 Wilson
packages. The September C2 resolution, symbolic all-rank assembly, and
fixed-spacing Hamiltonian G18 construction are established upstream results;
none is reopened or used as a missing premise here.

The support counting, moving-weight argument, normalization identity and
Cauchy estimate were independently derived and reviewed. The norm theorem
is the analytic proof above. Its finite binary-support oracle exercises
three overlapping four-link interactions and three distinct initial
families, using exact rational arithmetic for the composed map. The
independent disjoint-block oracle uses two- and three-dimensional local
spaces, exact creation logarithms, exact SU(3) Haar moments, and separate
numerical matrix exponentials. These finite checks do not replace the
Hilbert-space proof.

`G18_SAME_WEIGHT_CREATOR_OBSTRUCTION_20260905.md` identifies why the original uncomposed same-weight
criterion was stronger than necessary: an explicit SU(3) active-plaquette
family makes its proposed uniform derivative bound fail. This does not
falsify a separately restricted statement only about the full uniform
interaction. The theorem above directly treats that full interaction,
overlapping supports, and arbitrary trial creator families after retaining
the kinetic smoothing.

The reproducible source snapshots, certificates, scalar Lean proof and
strict compiler transcript are pinned in
`runs/wilson_rooted_contraction_2026-09-05`. Lean certifies the stated real
rational Taylor inequality used in the obstruction; it does not formalize
the infinite-dimensional contraction argument.
