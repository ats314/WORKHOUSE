# Quantum ground transport at small coupling

9 September 2026. These estimates concern the actual twelve-edge, four-face
compact square, with its true normalized positive quantum ground. They use
the fixed-square physical spectral floor already proved in
`../w6_square_block_20260909/finite_g_quantum_floor.md`.

Write

\[
 T=-\tfrac12\sum_{e,a}E_{e,a}^2,\qquad
 H_g=g^2T+g^{-2}V,\qquad H_g\Psi_g=e_g\Psi_g,
 \quad d\mu_g=\Psi_g^2dU.
\]

Choose a fixed small-coupling interval on which
\(e_g\le E\) and the physical excitation gap is at least \(\gamma>0\).
The preceding fixed-square result allows \(\gamma=2\). Constants below
depend on this one compact square, not on a classical Gibbs replacement.

## 1. Exact quantum moments and exponential concentration

For a face trace \(x_f=\operatorname{Tr}U_f/2\), precisely its four original
edges differentiate it. The fundamental SU(2) Casimir gives
\(\Delta_E x_f=-3x_f\), where \(\Delta_E=\sum E_{e,a}^2\). Consequently

\[
 \boxed{\Delta_E V=48-3V.}\tag{Q1}
\]

For \(v_f=4(1-x_f)\), summing the four original edge derivatives gives
\(\sum|E v_f|^2=16(1-x_f^2)\le8v_f\). At most two faces contain any one
edge. Applying the two-term square inequality edge by edge therefore gives

\[
 \boxed{\sum|EV|^2\le16V.}\tag{Q2}
\]

Multiply the actual ground equation by \(V^k\Psi_g\), integrate by parts,
and retain the nonnegative weighted electric term:

\[
 e_g\,\mathbb E V^k
 =\frac{g^2}{2}\sum\mathbb E\!\left[V^k|E\log\Psi_g|^2\right]
 -\frac{g^2}{4}\mathbb E\Delta_E(V^k)
 +g^{-2}\mathbb E V^{k+1}.
\]

Equations (Q1)--(Q2) imply
\(\Delta_E(V^k)\le16k(k+2)V^{k-1}\), hence

\[
 \boxed{\mathbb E V^{k+1}\le g^2e_g\mathbb E V^k
       +4g^4 k(k+2)\mathbb E V^{k-1}.}\tag{Q3}
\]

Thus \(\mathbb E V^k\le A_k g^{2k}\), with explicit constants
\(A_0=1,A_1=E,A_{k+1}=EA_k+4k(k+2)A_{k-1}\). In particular

\[
 \boxed{\mathbb E V^2\le g^4(e_g^2+12).}\tag{Q4}
\]

There is also a direct exponential version with a fixed exponent. Put
\(h=g^2\), \(\phi=V/4\), and \(u=e^{\phi/h}\Psi_g\). The weighted ground
identity for \(-h^2\Delta_E/2+V\) is

\[
 0=\frac{h^2}{2}\sum\|Eu\|^2+
 \int\left(V-he_g-\frac12\sum|E\phi|^2\right)|u|^2.
\]

By (Q2), the last coefficient is at least \(V/2-hE\). On
\(V\le4hE\), the exponential weight is at most \(e^{2E}\); on its
complement the coefficient is at least \(hE\). Splitting the integral
therefore proves

\[
 \boxed{\mathbb E_{\mu_g}\exp\!\left(\frac{V}{2g^2}\right)
       \le2e^{2E}.}\tag{Q5}
\]

These are quantum ground estimates, obtained without a pointwise formula
for \(\Psi_g\). They control ground-weighted tails; multiplication by an
arbitrary retained source requires its own estimate.

## 2. The ordinary ground derivative has order at most \(1/g\)

At every positive coupling, ellipticity and the simple ground eigenvalue
give a smooth real normalized ground. Differentiating its equation,
with \(Q_g^\mathrm{vac}=1-|\Psi_g\rangle\langle\Psi_g|\), gives

\[
 (H_g-e_g)\partial_g\Psi_g
 =-Q_g^\mathrm{vac}(\partial_gH_g)\Psi_g
 =4g^{-3}Q_g^\mathrm{vac}V\Psi_g.
\tag{Q6}
\]

The last equality follows from
\((\partial_gH_g)\Psi_g=2e_g\Psi_g/g-4V\Psi_g/g^3\).
The derivative is physical and orthogonal to the ground. By (Q4),

\[
 \boxed{\|\partial_g\Psi_g\|
 \le\frac{4\sqrt{e_g^2+12}}{\gamma g},\qquad
 \|(H_g-e_g)^{1/2}\partial_g\Psi_g\|
 \le\frac{4\sqrt{e_g^2+12}}{\sqrt\gamma\,g}.}\tag{Q7}
\]

The ordinary fixed-compact \(H^1\) norm can lose one additional factor
\(g^{-1}\), since the kinetic part of the quantum form carries \(g^2\).
Equation (Q7) is therefore stated in the actual scaled quantum norm.

## 3. A full compact dilation that preserves the retained algebra

Use the global Haar-preserving product coordinates

\[
 (U_0,U_1,U_2,U_3)\longmapsto(U_0,U_1,U_2,Q=U_2U_3).
\]

On each SU(2) factor choose a smooth conjugation-equivariant radial vector
field equal to the Euler vector field in logarithmic coordinates near the
identity and zero near the antipodal element. Let \(Z\) be their sum in
these product coordinates. It is a smooth complete physical vector field
on the compact configuration space. On the last factor its flow sends
\(w=\operatorname{Tr}Q/2\) to a smooth monotone function of \(w\) alone.
Thus its flow preserves the entire literal retained algebra, exactly.

Let

\[
 D=Z+\tfrac12\operatorname{div}_{dU}Z.\tag{Q8}
\]

Then \(D\) is skew-adjoint on its flow domain; its unitary flow is the
diffeomorphism pullback including the square root of the Haar Jacobian.
It preserves the physical sector and the compact form domain at every
finite flow time. Near the unique well, it is the usual twelve-dimensional
dilation generator up to smooth coordinate and Haar corrections.

## 4. Bounded actual ground derivative after subtracting dilation

Define

\[
 \dot\Psi_g^{\mathrm{ren}}
    =\partial_g\Psi_g+g^{-1}D\Psi_g,
 \qquad
 B_g=\partial_gH_g+g^{-1}[D,H_g]
    =g(2T+[D,T])+g^{-3}(ZV-2V).
\tag{Q9}
\]

The complete forcing \(B_g\) retains the variable electric coefficients,
the Haar correction, and the actual magnetic potential. The following
bound uses the true ground rather than its Gaussian approximation:

\[
 \boxed{\|B_g\Psi_g\|\le C,\qquad 0<g<g_* .}\tag{Q10}
\]

Here is the detailed estimate. In a smooth local chart \(x\) at the unique
well, \(V\asymp|x|^2\) and
\(ZV-2V=O(|x|^3)\). Away from that well, \(V\) has a positive minimum.
Consequently \(|ZV-2V|\le C V^{3/2}\) globally. The \(k=3\) moment in
(Q3) gives \(g^{-3}\|(ZV-2V)\Psi_g\|\le C\).

The second-order coefficients of \(2T+[D,T]\) vanish at the well: this is
the exact cancellation \([x\cdot\partial,T(0)]=-2T(0)\). They are
therefore \(O(|x|)\); its first-order and zeroth-order coefficients are
bounded. To estimate the weighted second derivatives, choose a chart
cutoff \(\chi\) and set \(f_i=x_i\chi\Psi_g\). Uniform ellipticity of
the fixed operator \(T\) gives

\[
 \|f_i\|_{H^2}\le C(\|Tf_i\|+\|f_i\|).
\]

The ground equation and a first-order commutator give exactly

\[
 Tf_i=x_i\chi(g^{-2}e_g-g^{-4}V)\Psi_g
             +[T,x_i\chi]\Psi_g.
\]

Now \(\|x_i\chi\Psi_g\|=O(g)\) by the first moment;
\(\|x_i\chi V\Psi_g\|=O(g^3)\) by the third moment; and
\(\|\nabla\Psi_g\|=O(g^{-1})\) by the positive kinetic energy and
uniform ellipticity. Hence \(\|Tf_i\|=O(g^{-1})\) and
\(\|f_i\|_{H^2}=O(g^{-1})\). Expanding the two derivatives of
\(x_i\chi\Psi_g\) proves

\[
 \||x|\chi\nabla^2\Psi_g\|=O(g^{-1}).\tag{Q11}
\]

For the complement of the chart, (Q5) gives exponentially small ground
mass on nested fixed neighborhoods. A cutoff energy estimate gives the
same smallness for \(g\nabla\Psi_g\); applying the displayed elliptic
estimate to the outer cutoff then gives a polynomial in \(g^{-1}\)
times an exponentially small bound for \(\nabla^2\Psi_g\). Equivalently,
arbitrarily high moments from (Q3) give every required polynomial order.
Thus the outside contribution to \(g(2T+[D,T])\Psi_g\) tends to zero.
Inside, (Q11) and \(\|\nabla\Psi_g\|=O(g^{-1})\) bound that contribution
uniformly. This proves (Q10).

Skewness and reality give \(\langle\Psi_g,D\Psi_g\rangle=0\), so
\(\dot\Psi_g^{\mathrm{ren}}\perp\Psi_g\). The exact differentiated
equation is

\[
 (H_g-e_g)\dot\Psi_g^{\mathrm{ren}}
       =-Q_g^\mathrm{vac}B_g\Psi_g.
\]

Applying the existing physical gap now proves

\[
 \boxed{\|\partial_g\Psi_g+D\Psi_g/g\|\le C/\gamma,
 \quad
 \|(H_g-e_g)^{1/2}(\partial_g\Psi_g+D\Psi_g/g)\|
       \le C/\sqrt\gamma.}\tag{Q12}
\]

This is a uniform finite-coupling remainder estimate for the actual
ground transport. Its proof does not differentiate an assumed asymptotic
series. In particular, the singular \(1/g\) vacuum motion has been
removed by an explicit full compact source-algebra-preserving unitary.
For \(W_g=e^{\log(g/g_*)D}\), the derivative of
\(\widehat\Psi_g=W_g\Psi_g\) is
\(W_g\dot\Psi_g^{\mathrm{ren}}\), which is uniformly bounded in \(L^2\).
Thus \(\widehat\Psi_g\) has a strong \(L^2\) limit at zero coupling.
The fixed compact \(H^1\) operator norms of \(W_g\) are not asserted
uniform as its flow time tends to minus infinity.

## 5. Exact conditional projection speed and the remaining distinction

Disintegrate Haar over the literal trace \(w\) using probability fiber
measures \(dm_w\), and set

\[
 h_g(w)=\int\Psi_g^2dm_w,\quad v_g=\Psi_g/\sqrt{h_g(w)},
 \quad s_g=\partial_g\log\Psi_g.
\]

The retained projection is the fiberwise rank-one projection
\(P_g(w)=|v_g\rangle\langle v_g|\), and

\[
 v'_g=(s_g-\mathbb E_{\mu_g}[s_g\mid w])v_g.
\]

Since \(v'_g\perp v_g\), its two-by-two projection derivative matrix
has off-diagonal entry \(\|v'_g\|\). Therefore the exact operator formula is

\[
 \boxed{\|P'_g\|=\|[P'_g,P_g]\|
 =\operatorname*{ess\,sup}_{w}
       \sqrt{\operatorname{Var}_{\mu_g}(s_g\mid w)}.}\tag{Q13}
\]

This avoids a bound involving the global minimum of \(h_g\). For the
dilated projection \(\widehat P_g=W_gP_gW_g^*\), its algebra is still the
literal \(w\)-algebra because the dilation flow normalizes that algebra.
The same formula uses the renormalized score

\[
 \sigma_g=\frac{\partial_g\Psi_g+D\Psi_g/g}{\Psi_g}
\]

after the smooth change of coarse and fiber coordinates. In particular,
(Q12) gives the concrete averaged conditional bound

\[
 \boxed{\int\operatorname{Var}_{\mu_g}(\sigma_g\mid w)\,d\nu_g(w)
       \le C^2/\gamma^2.}\tag{Q14}
\]

For a bounded retained multiplier this already bounds its source-frame
derivative by \((C/\gamma)\|f\|_\infty\). It is not the essential-supremum
bound in (Q13), nor an all-Gaussian-energy estimate. Obtaining the needed
source-weighted conditional estimate is a separate precise step. The
previous loss caused solely by the actual ground's dilation has now been
removed, with (Q12) proved rather than postulated.

## 6. The original compact transport must accumulate logarithmic length

The already proved strong harmonic ground limit also quantifies why the
unrenormalized transport cannot be continued with a bounded generator at
zero. For any fixed \(c>1\), the two true ground vectors satisfy

\[
 \lim_{g\to0}\langle\Psi_g,\Psi_{cg}\rangle
       =\left(\frac{2c}{1+c^2}\right)^6.\tag{Q15}
\]

Indeed the twelve-dimensional normalized oscillator ground is Gaussian
with a positive quadratic matrix; the overlap of this Gaussian with its
scalar dilation has the displayed value, independent of that matrix.
Strong harmonic convergence suffices for this statement; convergence of
ground derivatives is not assumed.

It follows that \(\int_g^{cg}\|\partial_s\Psi_s\|ds\) is eventually
bounded below by any constant smaller than
\(\sqrt{2-2(2c/(1+c^2))^6}\). Summing disjoint geometric intervals proves
a logarithmic lower bound on the accumulated ground path length; (Q7)
provides a logarithmic upper bound. Every differentiable unitary source
transport sending a fixed normalized constant source to \(\Psi_g\) has
at least this much operator-norm path length. This statement concerns
the complete vacuum-compatible transport; it does not infer a pointwise
lower bound on the projection derivative from mere harmonic convergence.

For comparison only, in the exact scaled twelve-dimensional Gaussian
model, conditioning on the retained outer norm leaves nine Gaussian
fast coordinates. Its conditional score variance is exactly
\(9/(2g^2)\), and its Kato norm is \(3/(\sqrt2 g)\).
This Gaussian coefficient is not substituted for an unproved uniform
conditional asymptotic of the compact model.

## 7. Compact quantile endpoints give a second quantitative diagnostic

For the exact Haar-compact CDF map \(\eta_g\) in the preceding source
domain report, matching the square-root endpoint tails gives the exact
identities

\[
 \boxed{\eta'_g(1)=h_g(1)^{2/3},\qquad
        \eta'_g(-1)=h_g(-1)^{2/3}.}\tag{Q16}
\]

The transported compact source form weight divided by its Haar reference
weight has endpoint limits \(g^2h_g(\pm1)^{2/3}\). At the outer antipode,
the exact constrained potential minimum is

\[
 \min_{U_2U_3=-I}V=16-8\sqrt2>0.\tag{Q17}
\]

To see this, put \(a=\operatorname{Tr}U_2/2\); then
\(\operatorname{Tr}U_3/2=-a\). Optimizing the two middle holonomies gives
the maximum sum of four traces
\(\sqrt{2+2a}+\sqrt{2-2a}\le2\sqrt2\), attained at \(a=0\).

By (Q5), local elliptic estimates, and Sobolev embedding on nested compact
neighborhoods of this fiber, for every \(\varepsilon>0\) there are finite
\(C_\varepsilon,N_\varepsilon\) such that

\[
 h_g(-1)\le C_\varepsilon g^{-N_\varepsilon}
 \exp\!\left[-\frac{16-8\sqrt2-\varepsilon}{2g^2}\right].\tag{Q18}
\]

Thus the lower source-form comparison constant of that particular
Haar-compact quantile identification degenerates exponentially as
\(g\to0\). Its valid positive-base common-domain theorem cannot be
upgraded to uniform small-coupling coercivity by taking a limit of those
comparison constants. The explicit dilation construction and (Q12)
address the ground motion directly; the all-source conditional bound
identified in (Q13)--(Q14) is the next relevant source estimate.
