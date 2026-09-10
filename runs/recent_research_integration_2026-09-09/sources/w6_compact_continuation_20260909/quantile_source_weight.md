# A source-energy criterion for the conditional quantum frame

9 September 2026. This is the next quantitative consequence of the actual
ground transport estimate in `quantile_scale.md`. It uses a weighted
one-dimensional source inequality; a bounded essential supremum of the
conditional frame speed is sufficient but is not necessary.

## Exact source quantity

Keep the actual quantum ground measure and the literal coarse trace:

\[
 d\mu_g=\Psi_g^2dU,\qquad d\nu_g(w)=\rho_g(w)dw,
 \quad -1<w<1.
\]

For the explicit dilation preserving the entire retained algebra, put

\[
 \sigma_g=\frac{\partial_g\Psi_g+D\Psi_g/g}{\Psi_g},
 \qquad K_g(w)=\operatorname{Var}_{\mu_g}(\sigma_g\mid w).
\tag{W1}
\]

The prior actual-ground estimate proves
\(\overline K_g:=\int K_gd\nu_g\le C^2/\gamma^2\) uniformly at small
coupling. The normalized conditional frame derivative applied to a source
\(f\) has squared norm exactly \(\int K_g|f|^2d\nu_g\), after the harmless
unitary coordinate change along the dilation flow.

The exact compact retained energy is

\[
 b_g[f]=\int_{-1}^1 v_g(w)|f'(w)|^2dw,
 \qquad v_g(w)=g^2(1-w^2)\rho_g(w).
\tag{W2}
\]

Here \(v_g\) is the energy density with respect to Lebesgue measure; it
includes the probability density. It is unrelated to the normalized
fiber vector denoted by the same letter in the earlier projection
calculation. Since \(\Psi_g f(w)\) is physical, the established actual
quantum gap implies the exact coarse Poincare inequality

\[
 \int|f-\nu_g f|^2d\nu_g\le\gamma^{-1}b_g[f].\tag{W3}
\]

Choose a median \(m_g\) of \(\nu_g\). The density is smooth and positive
in the interior, so both sides of this median have mass one half.
Define the two explicit nonnegative numbers

\[
 B_{g,+}=\sup_{m_g<x<1}
 \left(\int_x^1 K_g(w)d\nu_g(w)\right)
 \left(\int_{m_g}^x\frac{dw}{v_g(w)}\right),
\tag{W4}
\]

\[
 B_{g,-}=\sup_{-1<x<m_g}
 \left(\int_{-1}^x K_g(w)d\nu_g(w)\right)
 \left(\int_x^{m_g}\frac{dw}{v_g(w)}\right),
 \qquad B_g=\max(B_{g,+},B_{g,-}).
\tag{W5}
\]

These are weighted tail masses times one-dimensional resistance
integrals. They retain the actual coupled quantum marginal and its
actual conditional frame variance.

## The resulting source estimate

For every function in the compact source form domain,

\[
 \boxed{\int K_g|f-\nu_g f|^2d\nu_g
 \le\left(8B_g+\frac{4\overline K_g}{\gamma}\right)b_g[f].}
\tag{W6}
\]

In particular, a uniform bound on \(B_g\), together with the already
proved bound on \(\overline K_g\), is sufficient for a uniformly bounded
renormalized conditional frame map on centered finite-energy sources.
There is no essential-supremum hypothesis on \(K_g\).

Here is a proof with explicit constants.

First, the median and (W3) imply

\[
 \int|f-f(m_g)|^2d\nu_g\le\frac2\gamma b_g[f].\tag{W7}
\]

Indeed let \(h=f-f(m_g)\), and restrict \(h\) separately to the right
and left half-interval, extending each restriction by zero. Both belong
to the form domain and are supported on a set of probability at most
one half. For either piece \(h_\pm\), Cauchy--Schwarz gives
\(|\nu_g h_\pm|^2\le\|h_\pm\|^2/2\), hence
\(\operatorname{Var}_{\nu_g}(h_\pm)\ge\|h_\pm\|^2/2\).
Applying (W3) and adding the two inequalities proves (W7). The point
value at the interior median is the usual local Sobolev trace; the
argument first applies on a smooth core and extends by form closure.

Next, the anchored weighted Hardy inequality gives

\[
 \int K_g|f-f(m_g)|^2d\nu_g\le4B_g b_g[f].\tag{W8}
\]

To prove it on the right half, abbreviate
\(d\lambda=K_gd\nu_g\),
\(Q(x)=\lambda([x,1))\), and
\(R(x)=\int_{m_g}^x v_g^{-1}\). For \(h(m_g)=0\) and
\(0<\alpha<1\), weighted Cauchy--Schwarz gives

\[
 |h(x)|^2\le\frac{R(x)^{1-\alpha}}{1-\alpha}
       \int_{m_g}^x |h'(t)|^2v_g(t)R(t)^\alpha dt.
\]

Since \(Q(x)R(x)\le B_{g,+}\), integration by parts in the tail yields

\[
 \int_t^1 R(x)^{1-\alpha}d\lambda(x)
 \le\frac{B_{g,+}}{\alpha}R(t)^{-\alpha}.
\]

For completeness, its first boundary term is
\(R(t)^{1-\alpha}Q(t)\); its remaining term is
\((1-\alpha)\int_t^1Q(x)R(x)^{-\alpha}dR(x)\).
Bounding each by \(Q\le B_{g,+}/R\) gives the displayed factor
\(1+(1-\alpha)/\alpha=1/\alpha\). The endpoint contribution vanishes:
if \(R\) diverges it is at most \(B_{g,+}R^{-\alpha}\), and if \(R\)
stays finite the atom-free tail mass tends to zero.

Fubini now bounds the anchored integral by
\(B_{g,+}/[\alpha(1-\alpha)]\) times its half-interval energy. Set
\(\alpha=1/2\), repeat on the left, and add. This proves (W8).

Finally write \(f-\nu_g f=h-\nu_g h\). The squared two-term inequality,
(W8), and (W7) give

\[
 \int K_g|h-\nu_g h|^2d\nu_g
 \le2\int K_g|h|^2d\nu_g+2\overline K_g|\nu_g h|^2
 \le\left(8B_g+4\overline K_g/\gamma\right)b_g[f],
\]

which is (W6).

The tail criterion is quantitatively sharp for the anchored problem:
if its best right-hand constant is \(C_H\), then
\(B_{g,+}\le C_H\le4B_{g,+}\). For the lower bound use the test
\(h_t(x)=R(\min(x,t))\): its energy is \(R(t)\), while its weighted
norm is at least \(Q(t)R(t)^2\). Cutoff approximations justify this test
when needed. The same statement holds on the left.

## An explicit unbounded-variance example

Let \(\mu_0\) be the actual retained Gaussian law
\(\operatorname{Gamma}(\alpha=3/2,\theta=2\sqrt2)\), with

\[
 b_0[f]=8\int_0^\infty a|f'(a)|^2d\mu_0(a),
 \qquad K(a)=a.
\]

Although \(\operatorname*{ess\,sup}K=\infty\), every centered source
satisfies the concrete estimate

\[
 \boxed{\int_0^\infty a|f(a)|^2d\mu_0(a)\le7b_0[f].}\tag{W9}
\]

For a smooth core function, the Gamma density identity gives

\[
 \int a|f|^2d\mu_0
 =\alpha\theta\int|f|^2d\mu_0
      +2\theta\operatorname{Re}\int a\overline f f' d\mu_0.
\]

Applying Young's inequality to the last integral, with half of the left
side absorbed, gives

\[
 \int a|f|^2d\mu_0
 \le2\alpha\theta\|f\|^2+4\theta^2\int a|f'|^2d\mu_0
 =3\theta\|f\|^2+\frac{\theta^2}{2}b_0[f].
\]

The radial Gaussian gap is \(8/\theta=2\sqrt2\), so for centered \(f\),
\(\|f\|^2\le\theta b_0[f]/8\). Since \(\theta^2=8\), the last bound
is precisely \(7b_0[f]\). Form-core approximation extends it to every
centered finite-energy source. This example shows concretely that an
unbounded conditional multiplier can still satisfy the required
source-energy bound.

Its Hardy tail products also remain finite: at infinity the product in
(W4) tends to \(\theta^2/8=1\); at zero its left counterpart tends to
zero. Interior continuity then gives finite \(B\). A bounded
essential-supremum requirement would discard this admissible case.

## What is now reduced to a concrete estimate

For the actual compact square, the uniform estimate on \(B_g\) in
(W4)--(W5) has not yet been proved. The quantum moment and dilation
arguments establish \(\overline K_g\), while the remaining task is the
explicit product of the conditional-variance tail and the coarse
resistance integral. This is weaker than requiring a uniform global
Kato operator norm and directly targets the source energy.

Equation (W6) controls the conditional source-frame derivative. The
complete transported operator residual has additional terms, so this
criterion alone is not a residual closure. Its right side is the exact
compact energy \(b_g\). Pulling it through a probability coordinate
change transforms that energy as well; it does not silently replace it
by the original Gaussian source norm \(b_0\).
