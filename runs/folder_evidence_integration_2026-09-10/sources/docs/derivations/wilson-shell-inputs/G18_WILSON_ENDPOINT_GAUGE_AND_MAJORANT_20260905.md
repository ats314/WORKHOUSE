# An endpoint gauge for the actual Wilson vacuum recursion

Date: 5 September 2026.

This note sharpens the convergence question left by
`G18_VACUUM_CHART_RECURSION_20260905.md`. The first result is an exact
change of vacuum-vector coordinates for the fine Wilson transfer. It
recovers a support-size denominator uniformly in the temporal mesh. A
connected-creator reformulation then identifies the nonlinear norm estimate
that is still required. The estimate is stated as a sufficient condition,
not assumed to have been proved.

## 1. What the existing crude recurrence loses

The reviewed fixed-order note uses a finite-subsystem polydisc of radius

\[
 r_n=\log(41/40)/(J s_1 n)
\]

and bounds a degree-`n` residual by
`k_n=(41/39) exp(2P_n) r_n^{-n}`. Even after discarding the exponential
factor, this displayed majorant has

\[
 k_n^{1/n}\ge(41/39)^{1/n}\frac{J s_1 n}{\log(41/40)}
        \longrightarrow\infty.
 \tag{1}
\]

Thus the particular bounding sequence in that note has zero power-series
radius. This is a statement about the bound, not the actual coefficients.
Its source is identifiable: it keeps the operator perturbation of the
entire `n`-face subsystem small by its extensive norm, shrinking the
Cauchy polydisc as `1/n`. Multiplying that estimate by a connected-support
census cannot recover the factorial information that was discarded.

A second loss is the coarse vacuum inverse
`||(1-D_X)^{-1}Q_X||<=5`. That bound is uniform but has no `1/|X|` gain.
The following exact gauge exposes a stronger inverse together with the
numerator that belongs to it.

## 2. Exact endpoint removal

Work first in a finite spatial volume on the full link Hilbert space. Let

\[
 T(u)=M(u)C M(u),\qquad
 M(u)=e^{\tau u V/2},\quad C=e^{-\tau K},\quad
 V=\sum_pv_p.
 \tag{2}
\]

The potential is a bounded multiplication operator in every finite volume.
`K` is the nonnegative self-adjoint sum of the unbounded link kinetic
operators. Let `Omega_0` be its product vacuum. On a real small-coupling
interval let `Omega_W(u)` be the actual Perron vector of `T(u)` and
`lambda(u)>0` its eigenvalue. Normalize

\[
 \phi(u)=\frac{M(u)^{-1}\Omega_W(u)}
                   {\langle\Omega_0,M(u)^{-1}\Omega_W(u)\rangle},
 \qquad\langle\Omega_0,\phi(u)\rangle=1.
 \tag{3}
\]

The denominator is nonzero near zero. All expressions have their
finite-volume analytic germs there. Multiplying the actual eigenvector
equation by `M^{-1}`, with `Omega_W` proportional to `M phi`, gives

\[
 \boxed{\lambda\phi=C e^{\tau uV}\phi.}
 \tag{4}
\]

This is an exact bounded similarity at finite volume:
`M^{-1} T M=C e^{tau uV}`. No kinetic logarithm is expanded or replaced.
The right-hand operator is generally not self-adjoint in the Haar inner
product; positivity and spectral claims still refer to the original
symmetric transfer. No volume-uniform bound on `||M|| ||M^{-1}||` is
claimed.

Define the scalar normalizer

\[
 \omega(u)=\tau^{-1}\log\lambda(u),\qquad
 W_\tau(u,\omega)=\frac{e^{\tau(uV-\omega)}-1}{\tau}.
 \tag{5}
\]

Here `omega` is the logarithm of the transfer vacuum eigenvalue, not a
plaquette excitation energy. With `P=|Omega_0><Omega_0|` and `Q=1-P`,
(4) is equivalent to

\[
 P W_\tau\phi=0,\qquad
 Q\phi=R_\tau QW_\tau\phi,
 \quad R_\tau:=\tau C(1-C)^{-1}Q.
 \tag{6}
\]

The scalar equation is also

\[
 \lambda(u)=\langle\Omega_0,e^{\tau uV}\phi(u)\rangle.
 \tag{7}
\]

## 3. The inverse and its domain

Define `R_tau` by the bounded Borel function

\[
 r_\tau(E)=\frac{\tau}{e^{\tau E}-1}\quad(E>0),
 \qquad r_\tau(0)=0
\]

on `K`. Writing `tau/(exp(tau K)-1)` on `Q` means this spectral calculus,
not an operation on an assumed domain of the unbounded exponential.
Since `exp(x)-1>=x` for `x>=0`,

\[
 0\le R_\tau\le K^{-1}Q,\qquad
 \|K R_\tau\|\le1.
 \tag{8}
\]

The second statement implies `R_tau H subset Dom(K)`. Equation (6) is
therefore a Hilbert-space identity with a well-defined kinetic-domain
gain: `W_tau` is bounded at finite volume and its argument is a Hilbert
vector. No high-representation cutoff is used.

For the exact excited-link support projection

\[
 P_J=\bigotimes_{\ell\in J}q_\ell
       \bigotimes_{\ell\notin J}p_\ell,
 \quad p_\ell=|1_\ell\rangle\langle1_\ell|,\quad q_\ell=1-p_\ell,
\]

all factors commute with `K`. If the calibrated one-link gap is
`gamma=C_F/2`, then `K_J>=gamma |J|` on every nonempty exact support.
Consequently

\[
 \boxed{
 \|r_\tau(K_J)\|\le\frac1{\gamma|J|},\qquad
 \|K_Jr_\tau(K_J)\|\le1.}
 \tag{9}
\]

This is uniform in the fine mesh, spatial volume and link representation
dimensions. It is stronger than the coarse inverse bound because the
endpoint gauge leaves the factor `C` next to the vacuum inverse. Dropping
that numerator would restore `tau/(1-e^{-tau K})`, which contains a
mesh-sized large-energy term and does not satisfy (9).

## 4. First-order recovery and exact disconnected cancellation

For Wilson plaquette multiplication ` <Omega_0,V Omega_0>=0`.
Differentiating (6)--(7) at zero gives

\[
 \omega'(0)=0,\qquad \phi'(0)=r_\tau(K)V\Omega_0.
\]

Restoring the endpoint in (3), the first vacuum derivative of the symmetric
transfer is

\[
 \left(\frac\tau2+r_\tau(K)\right)V\Omega_0.
\]

Each one-plaquette source has calibrated energy `E_s`, and

\[
 \boxed{
 \frac\tau2+\frac\tau{e^{\tau E}-1}
       =\frac\tau2\coth(\tau E/2)=d_\tau(E).}
 \tag{10}
\]

Thus this gauge reproduces the previously derived actual-Wilson first
rotation; it does not change the transfer's reduced-resolvent weight.

There is a useful exact two-component identity:

\[
 \boxed{
 r_\tau(E_1+E_2)
       \big(r_\tau(E_1)+r_\tau(E_2)+\tau\big)
   =r_\tau(E_1)r_\tau(E_2).}
 \tag{11}
\]

To prove it, substitute `a=exp(tau E_1)`, `b=exp(tau E_2)`; the numerator
`(a-1)+(b-1)+(a-1)(b-1)` is `ab-1`.
For two disjoint active plaquettes, the two sequential first-order terms
give `r_tau(E_1)+r_tau(E_2)` and the mixed coefficient of the magnetic
exponential gives `tau`. Equation (11) makes their second vacuum-vector
coefficient precisely the tensor product of the two first coefficients,
as required by exact factorization. Replacing the exponential kick by
`1+tau uV` would lose that last term and break the identity.

For completeness an exact finite-volume coefficient recursion follows from
(6). Write `phi=Omega_0+sum_{n>=1}u^n phi_n` with `P phi_n=0`, and
`omega=sum_{n>=1}u^n omega_n`. Having computed lower orders, put

\[
 Z_n=[u^n]\left\{
 \frac{e^{\tau(uV-\omega_{<n}(u))}-1}{\tau}
                         \phi_{<n}(u)\right\}.
\]

Then

\[
 \omega_n=\langle\Omega_0,Z_n\rangle,\qquad
 \phi_n=R_\tau QZ_n.
 \tag{12}
\]

The new scalar enters only as `-omega_n Omega_0`, killed by `Q`; this is
why (12) is triangular. For example
`Z_2=V r_tau(K)V Omega_0+(tau/2)V^2 Omega_0`.
Equation (12) alone is still an extensive finite-volume recurrence, not a
rooted norm estimate.

## 5. Connected creation coordinates and the exact missing map

The extensive recurrence can be reformulated without guessing its
connected counterterms. A coefficient family `v=(v_J)` has
`v_J in H'_J`, the exact excited tensor factor on `J`. Its local creator is
`hat v_J=|v_J><Omega_J|`, embedded by the identity outside `J`.
Two such creators commute: disjoint ones commute as tensor factors, while
both products vanish when their supports intersect because every shared
link is orthogonal to its vacuum in `v_J`.

Equivalently use the commutative disjoint-support product `star` on
coefficient families,

\[
 (f\star g)_X=\sum_{I\mathbin{\dot\cup}J=X}f_I\otimes g_J.
\]

At finite volume the nonempty-support ideal is nilpotent. A vector with
vacuum coefficient one has a unique finite creation logarithm; write

\[
 \phi_v=\exp_\star(v),\qquad v=\log_\star(\phi_v).
\]

Vectors and their exact-support coefficient families are identified in
this notation. Define

\[
 a_\tau(u,v)=\langle\Omega_0,e^{\tau uV}\phi_v\rangle,
\]

\[
 \mathcal F_\tau(u,v)=
 \log_\star\left(\frac{e^{\tau uV}\phi_v}{a_\tau(u,v)}\right),
 \qquad
 \mathcal N_\tau(u,v)=\frac{\mathcal F_\tau(u,v)-v}{\tau}.
 \tag{13}
\]

These are finite-volume analytic germs near the free point. Scalar
normalization precedes the creation logarithm. The free link transfer is
multiplicative for `star`, so
`C exp_star(w)=exp_star(Cw)`. Thus the actual vacuum equation (4) becomes

\[
 \boxed{
 v_J=r_\tau(K_J)\mathcal N_{\tau,J}(u,v),
 \qquad\lambda=a_\tau(u,v).}
 \tag{14}
\]

This is an exact algebraic connected-coordinate equation, not yet a
convergent infinite-volume construction. In particular

\[
 \mathcal F_\tau(0,v)=v,\qquad
 \mathcal N_\tau(0,v)=0,
\]

so its nonlinear correction has at least one magnetic mark. The bounded
plaquette multipliers commute even when they overlap, giving the exact
input `e^{tau uV}=product_p e^{tau u v_p}`. Disconnected active-link
components factor before the creation logarithm, which then makes their
logarithms additive. These facts identify the linked subtraction that the
extensive recurrence (12) had not displayed.

### 5a. The exact creator flow has local degree at most eight

This statement is finite-volume algebra. Assume finitely many links and
four distinct links in each plaquette. The link Hilbert spaces may remain
infinite dimensional. Every creator is bounded, and the sum
`hat v=sum_{J nonempty}hat v_J` is finite and nilpotent. Thus its
exponential is a finite operator polynomial. Identify
`exp_star(v)` with `exp(hat v) Omega_0`.

For a fixed initial family `v`, set, where the scalar denominator is
nonzero,

\[
 \phi(t)=\frac{e^{tuV}e^{\widehat v}\Omega_0}
 {\langle\Omega_0,e^{tuV}e^{\widehat v}\Omega_0\rangle},
 \qquad v(t)=\log_\star\phi(t).
\]

All statements hold on the finite-volume analytic germ at `t=0`.
Creators commute also with their derivatives, so differentiation gives
`phi'(t)=exp(hat v(t)) hat v'(t) Omega_0`. Differentiating the normalized
magnetic evolution gives `phi'=(uV-c(t))phi`, with
`c(t)=<Omega_0,uV phi(t)>`. Multiplication by `exp(-hat v(t))` and removal
of the vacuum component therefore yield the exact vector field

\[
 \boxed{\dot v(t)=\mathcal Y_u(v(t)),\qquad
 \mathcal Y_u(v)=Qe^{-\widehat v}(uV)e^{\widehat v}\Omega_0.}
 \tag{13a}
\]

Here `Q` returns the nonempty exact-support coefficient family. The
removed scalar is exactly `c(t)`: indeed
`<Omega_0|exp(-hat v)=<Omega_0|`. Consequently
`F_tau(u,v)=v(tau)` and
`N_tau(u,v)=tau^{-1} integral_0^tau Y_u(v(t)) dt`, wherever this germ
continues with nonzero normalization. This last statement does not
assert a volume-uniform continuation interval.

For one plaquette let

\[
 W_p=\sum_{J:\,J\cap p\ne\varnothing}\widehat v_J.
\]

Creators supported away from `p` commute with its multiplication operator
`v_p` and with every creator, so their exponentials cancel exactly:
`exp(-hat v) v_p exp(hat v)=exp(-W_p) v_p exp(W_p)`. A nonzero product
of creators in `W_p` must have mutually disjoint supports. Every such
support uses at least one of the four links of `p`; hence a product of
five is zero and `W_p^5=0`. It follows that

\[
 e^{-\widehat v}v_pe^{\widehat v}
 =\sum_{a,b=0}^{4}\frac{(-1)^a}{a!b!}W_p^av_pW_p^b
 =\sum_{k=0}^{8}\frac{(-1)^k}{k!}
       \operatorname{ad}_{W_p}^{k}(v_p).
 \tag{13b}
\]

The last identity uses `ad_W(A)=WA-AW`; all terms at degree above eight
vanish because one side contains at least five copies of `W_p`.
Thus each local contribution to (13a) is a polynomial of degree at most
eight in the creator family. This bound is independent of volume and
link representation dimensions. It concerns the vector field, not its
finite-time flow: iterating the flow can generate arbitrarily large
supports and arbitrarily high degree.

The remaining norm issue is a support-weight loss, not an infinite local
commutator series. For example, when a rooted creator has support `J`,
summing plaquettes touching it can cost `4|J|` on the cubic lattice.
The norm in (15) alone does not bound its first support moment
`sup_l sum_{J contains l}|J| exp(mu|J|)||v_J||` at the same weight.
For `mu'<mu` that moment is bounded by
`[e(mu-mu')]^{-1}||v||_mu`, since
`x exp(-(mu-mu')x)<=1/[e(mu-mu')]`.
The finite polynomial identity therefore does not by itself justify
integrating (13a) in one common rooted-norm ball. A uniform analytic
map estimate such as (17), or a justified treatment of this loss
together with the free kinetic damping, remains to be supplied.

## 6. A precise sufficient rooted inequality

For an exact-support family define

\[
 \|v\|_\mu=\sup_\ell\sum_{J\ni\ell}e^{\mu|J|}\|v_J\|,
 \qquad
 \|w\|_{\mu,-1}=\sup_\ell\sum_{J\ni\ell}
                         \frac{e^{\mu|J|}}{|J|}\|w_J\|.
 \tag{15}
\]

Equation (9) gives the actual, proved estimate

\[
 \|\mathcal R_\tau w\|_\mu\le\gamma^{-1}\|w\|_{\mu,-1}.
 \tag{16}
\]

One sufficient nonlinear estimate would be constants `A,B>0`, independent
of volume and mesh, such that on `||v||_mu,||w||_mu<=1/B`,

\[
 \|\mathcal N_\tau(u,v)\|_{\mu,-1}
      \le A|u|e^{B\|v\|_\mu},
\]

\[
 \|\mathcal N_\tau(u,v)-\mathcal N_\tau(u,w)\|_{\mu,-1}
      \le AB|u|e^{B\max(\|v\|_\mu,\|w\|_\mu)}\|v-w\|_\mu.
 \tag{17}
\]

If the map in (13) were also defined analytically in this common ball,
then (16)--(17) would make (14) a contraction with constant at most one
half for

\[
 |u|\le\gamma/(2ABe).
 \tag{18}
\]

Its image would have norm at most `1/(2B)`. This would construct a
convergent connected nonunitary vacuum coordinate, uniformly in the mesh.
The constants in (17) have **not** been obtained here, and (17) is not
claimed to follow merely from scalar KP convergence. It is the explicit
unresolved estimate on the marked multiplication/creation-log map.

The linear input is already bounded: at `v=0,u=0`,
`partial_u N=V Omega_0`. For SU(3), each plaquette contribution has norm
`sqrt(2)` and exact four-link support, giving
`||partial_u N(0,0)||_{mu,-1}<=sqrt(2)e^{4mu}`. The unknown part is its
uniform nonlinear rooted Lipschitz bound, including the connected
normalization for arbitrary trial creator families.

Even proving (17) would not directly construct the self-adjoint anchored
operator chart of the reviewed recursion note. Endpoint removal is
nonunitary. The conversion to an equivalent controlled unitary chart, or
an excited-resolvent argument in a justified metric, remains an additional
operator step. No complete excited band or source totality is claimed.

## 7. Difference from the imported discrete-time polymer construction

The imported `G19_DISCRETE_TIME_VACUUM_AND_WINDOW_20260904.md` blocks a
fixed physical duration and conditions on free bridges to construct a
scalar space-time polymer expansion for traces and multiplication-source
correlations. Its remaining task is an excited operator contour estimate.

The present calculation stays with the fine transfer, removes one exact
magnetic endpoint from its vacuum vector, and retains the kinetic
numerator next to the inverse. Equations (9), (11) and (14) are not supplied
by that scalar bridge construction. They exhibit a support-size denominator
and a specific nonlinear connected map that can be targeted by a rooted
majorant. They are compatible with the imported normalization and restore
the same `d_tau` coefficient when the endpoint is put back.

This note uses no external general stability theorem. The rational identity
(11) is separately formalized in `lean/Workhouse/VacuumChart.lean`; its
exponential-energy interpretation, domain statements and
finite-volume identities follow directly from spectral calculus and the
actual transfer eigenvector equation. The displayed positive-radius
criterion remains conditional on (17) and on the uniform analytic map
construction stated there.
