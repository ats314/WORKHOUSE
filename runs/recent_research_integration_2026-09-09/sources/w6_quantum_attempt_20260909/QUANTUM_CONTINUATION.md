# The quantum continuation of the W6 graph path

9 September 2026 UTC. Analytic results and explicit stopping point.

The two requested bounds have not been proved for the coupled Wilson
family. Attempting them has identified a necessary change of route:
an unrestricted, coupling-independent **vertical conditional gap** is too
strong for an actual Wilson block, and the proposed **derivative norm of
the residual** can discard essential retained-energy denominators.
Neither result disproves W6. The surviving target uses the full quantum
fast form and a weak residual estimate that retains its horizontal energy.

## 1. An actual Wilson obstruction to the unrestricted vertical conversion

The eight-edge SU(2) two-square bouquet has two loops sharing a vertex.
With the established electric normalization, its actual Hamiltonian and
true ground are

\[
H_u=h_u\otimes I+I\otimes h_u,
\quad h_u=-2\Delta+2u(2-\operatorname{ReTr}K),
\quad \Omega_u(U_1,U_2)=\omega_u(U_1)\omega_u(U_2).
\]

Condition on the literal retained observation \(U=U_1U_2\), with \(K=U_1\).
The true quantum conditional density is

\[
\rho_U(K)=\frac{\omega_u(K)^2\omega_u(K^{-1}U)^2}{\mu_u(U)}.
\]

The factorization of the *joint* ground follows from this graph's exact
separability; the conditional density couples its two arguments. This is
not a classical Gibbs replacement. Let \(g=u^{-1/4}\), and let \(D_g\)
be the vertical part of the exact ground Dirichlet form, scaled by \(g^2\).
On the physical literal complement

\[
Q_{\rm phys}=\ker\mathbb E[\,\cdot\mid U]\cap\mathcal H_{\rm phys},
\qquad
\boxed{\inf\operatorname{spec}D_g\le\tfrac34g^2.} \tag{Q1}
\]

This follows without asymptotics. Writing
\(K=xI+i\mathbf v\cdot\sigma\), the radial heat equation proves that
\(\log\omega_u(x)\) is concave in \(x\in[-1,1]\). At \(U=-I\), the
conditional density relative to the Haar scalar law is consequently even
and decreasing in \(|x|\). Therefore
\(\mathbb E[|\mathbf v|^2\mid U=-I]\ge3/4\).
The angular quaternion test \(\mathbf n\cdot\mathbf v\) has
\(|\nabla(\mathbf n\cdot\mathbf v)|^2=(1-(\mathbf n\cdot\mathbf v)^2)/4\),
which gives (Q1). Contracting with \(\mathbf v(U)\), subtracting its true
conditional mean and localizing in punctured neighborhoods of \(-I\)
produces smooth, gauge-invariant tests on sets of positive measure.
Thus this is not an argument confined to one exceptional fiber.

In contrast, the established compact-rotor theorem gives, at small \(g\),

\[
\boxed{g^2Q(H_u-2e_u)Q\ge I.} \tag{Q2}
\]

The literal source contains the true vacuum, so its complement is
orthogonal to that vacuum and inherits the full spectral floor. Horizontal
derivatives supply the energy that (Q1) omits.

**Scope:** this is a bona fide finite Wilson graph, not the adjacent
seven-edge strip or the periodic anchored-path source family. It refutes
the unrestricted conversion principle from local fast tangent positivity;
it does not refute a conditional estimate on a specified good retained
set, the full coupled fast floor, or W6. The actual coupled-family
extension remains a separate obligation.

The full proof, constants, domain and physical-localization arguments are
in [fast_agent.md](fast_agent.md). It was independently audited.

## 2. What a valid conversion theorem additionally needs

For comparison, the actual joint ground of
\(H=-\tfrac12\Delta+V\) on Euclidean space does have conditional fast
gap at least \(m/\sqrt M\) if, globally,

\[
0\le\nabla^2V\le MI,
\qquad (\nabla^2V)_{FF}\ge mI.
\tag{Q3}
\]

Under smooth confinement, this follows from the ground-Hessian evolution:
if \(B=\nabla^2(-\log\Omega)\), then
\(0\le B\le\sqrt M I\) and \(B_{FF}\ge m/\sqrt M\).
The conditional negative log density has Hessian \(2B_{FF}\), so the
half-gradient Dirichlet form has the stated gap. This proof retains the
horizontal derivatives of the actual joint ground.

The global convexity hypothesis cannot be replaced by the existing local
fast Hessian bound. A smooth rotated oscillator and broad double well
provide an exact two-dimensional quantum counterexample: the fast
potential curvature stays positive and the entire potential Hessian
stays bounded, while a true conditional density has two peaks and its
gap tends to zero exponentially. The proof and the positive theorem are
in [conversion_agent.md](conversion_agent.md). Neither is a Wilson
comparison theorem.

The missing term is visible even in fixed Euclidean coordinates. If
\(H=T_F+T_H+V\) and \(H\Omega=E\Omega\), then each positive slice of
\(\Omega\) obeys

\[
\left(T_F+V+\frac{T_H\Omega}{\Omega}\right)\Omega=E\Omega.
\tag{Q4}
\]

The actual conditional amplitude is a ground amplitude for this modified
fiber potential, not necessarily for \(T_F+V\). The classical tangent
bound controls neither the horizontal quotient in (Q4) nor its fast
derivatives. In the Wilson chart the induced metric and transport terms
must also be included.

## 3. The full residual needs its retained-energy denominator

An exact local quantum model isolates the issue with the proposed bound
\(\ell_F[\rho_p]\le Cg^2b[p]\). On the normalized two-torus set

\[
H_g=-\partial_k^2-(1+g\cos k)\partial_y^2,
\quad |g|<\tfrac12,
\quad P=\mathbb E_k,
\quad b[p]=\|\partial_yp\|^2.
\]

The actual ground is constant, all transports are the identity, the
conditional vertical gap is one, and
\(A_g=QH_gQ\ge(1-|g|)A_0\). There are no omitted source, vacuum or
higher-order terms. For \(p_n=e^{iny}\), the complete first force and
residual at \(z=0\) are

\[
t_n=t_1p_n=n^2\cos k\,p_n,\qquad
u_n=A_0^{-1}t_n=\frac{n^2}{n^2+1}\cos k\,p_n,
\qquad
\rho_n=\frac{gn^4}{2(n^2+1)}\cos(2k)\,p_n.
\]

The Gaussian synthesis
bound is \(\langle t_n,A_0^{-1}t_n\rangle/b[p_n]\le1/2\), and the
Gaussian diagonal defect is zero. Nonetheless,

\[
\frac{\ell_F[\rho_n]}{g^2b[p_n]}
=\frac{n^6}{2(n^2+1)^2}\longrightarrow\infty,
\quad\text{whereas}\quad
\frac{\langle\rho_n,A_0^{-1}\rho_n\rangle}{b[p_n]}
=\frac{g^2n^6}{8(n^2+1)^2(n^2+4)}\le\frac{g^2}{8}.
\tag{Q5}
\]

Inverse form order therefore proves W6 in this model with the stronger
bound \(g^2/[8(1-|g|)]\). The vertical derivative estimate fails because
it loses the horizontal \(n^2+4\) denominator in (Q5). This example is
not Wilson and does not satisfy the additional special condition that
the horizontal cometric depends only on retained coordinates. It shows
precisely which inference needs more structure.

The actual Wilson source derivative also contains retained derivatives:

\[
(J_g^{\rm lit})'_0f
=\Psi_0\left[Y_1\cdot\nabla f+
\left(p_1-\tfrac12m_1\right)f\right]. \tag{Q6}
\]

It includes the true quantum marginal correction \(m_1\). The complete
first force is \(t_1=QW_1J_z\), with
\(W_1=H_1-e_1+[H_0,K_1^{\rm src}]\); it is not supplied by the magnetic
cubic alone. One must construct a compatible full-space source transport
and estimate its action on the fast space. The source isometry alone
specifies its retained-range action, not its fast-to-fast block.

See [residual_agent.md](residual_agent.md) for the all-mode proof,
the complete marginal jet and a full-form weak estimate that succeeds
in the model.

## 4. Surviving route and the exact stopping point

Use \(A_g=F_g-z\), \(A_0=F_0-z\), \(t=t_1p\),
\(u=A_0^{-1}t\), and the weak residual
\(\rho_p(q)=a_g[q,u]-\langle q,t\rangle\), with inner products
antilinear in the first entry. These must be the actual transported
operators, on compatible form domains, with \(A_g\) strictly positive.
The exact identity from the preceding continuation is

\[
\langle t,(A_g^{-1}-A_0^{-1})t\rangle
=-d_g[u,u]+\|\rho_p\|_{a_g^*}^2,
\quad
\|\rho_p\|_{a_g^*}^2
=\sup_{q\ne0}\frac{|\rho_p(q)|^2}{a_g[q]}.
\tag{Q7}
\]

Thus the following **full-form** estimate is sufficient:

\[
|\rho_p(q)|\le C|g|\sqrt{b[p]}\sqrt{a_g[q]},
\qquad |d_g[u,u]|\le C_0|g|b[p]. \tag{Q8}
\]

Together they imply W6 with constant \(C_0+C^2g_0\) for
\(|g|\le g_0\). A weaker \(\sqrt{|g|}\) residual estimate already
suffices for its stated order. The literal mixed form in W6 also needs
its common-domain justification, or the compatible weak extension.

The coefficient and derivative factors in (Q8) must retain horizontal
directions and inverse denominators. The torus example proves this can
work when the stronger local derivative norm fails. No pointwise uniform
vertical gap is needed by (Q7).

**The specific unresolved Wilson step is to prove (Q8), or its weaker
square-root version, for the complete transported residual on the actual
coupled physical complement, together with positivity of the full
\(F_{g,\Lambda}-z\) throughout the required spectral interval.** The
constants must be uniform in volume, coupling and the specified retained
background/energy range. The graph's local tangent theorem and finite-cell
ground/source expansions do not establish these interacting estimates.
The known Gaussian synthesis theorem must also be extended to the
complete force wherever its current scope covers only localized cubic
terms.

For a route restricted to good retained backgrounds, an alternative
missing theorem is a quantitative estimate on the contribution from their
complement for these actual residuals, in the full energy dual norm.
Small marginal probability alone cannot bound arbitrary normalized sources
localized there.

## 5. Evidence and files

- The SU(2) heat identity, metric and moment algebra: **6/6 exact controls**
  in [fast_agent_controls.json](fast_agent_controls.json).
- The torus norm and denominator identities: **7/7 exact rational mode
  controls** in [residual_agent_checks.json](residual_agent_checks.json).
- The Euclidean conversion and double-well finite algebra: **8/8 exact
  controls** in [conversion_algebra_checks.json](conversion_algebra_checks.json).

The heat maximum principles, compact-operator limits, physical localization
and all-energy norm arguments are analytic proofs, not Lean formalizations.
Finite checks certify the stated algebra, not the operator quantifiers.
No coupled Wilson W6 proof or continuum observable limit is claimed.
No generated graph, theorem status or existing source derivation was changed.

This report continues [the graph-path audit](../w6_graph_path_20260909/GRAPH_PATH.md)
and [the W6 residual identity](../w6_continuation_20260909/W6_PATH_FORWARD.md).

## 6. Review of the proposed Combes–Thomas closure

The [subsequent audit and repair](../w6_combes_thomas_20260909/CT_AUDIT.md)
confirms the positive-form dual identity and the geometric lattice sum.
It does not validate the proposed Wilson closure. In the exact torus
model, even the unweighted L2 residual ratio diverges:
\(\|\rho_n\|^2/(g^2b[p_n])=n^6/[8(n^2+1)^2]\to\infty\).
Thus the 21 prior controls cannot determine the proposed uniform local
L2 constant. The bouquet full quantum gap also does not identify a
pointwise magnetic curvature or establish the coupled floor by positive
boundary addition after vacuum subtraction.

The audit proves a conditional Combes–Thomas theorem with full-energy
weights and gives the corresponding source-synthesis version for a
many-body space. Those estimates preserve the horizontal inverse
denominators. Establishing their hypotheses for the complete coupled
Wilson operator and residual remains the stopping point; W6 stays open.

## 7. Actual adjacent-strip calculation

The next [concrete shared-edge calculation](../w6_adjacent_strip_20260909/ADJACENT_STRIP_RESULT.md)
evaluates the actual seven-edge SU(2) two-plaquette block. Its complete
first physical force vanishes by inversion symmetry, including the
source jet. The complete first nonzero force at order g^2 is computed
explicitly, including the shared electric derivative, Haar correction,
true ground and marginal corrections. Its full Gaussian inverse obeys
an all-retained-radial-energy bound with exact constant
\(6561(4-\sqrt{15})/5120\). The companion scripts pass 65 exact controls.
The report states the precise fixed-block coefficient and source domain.

## 8. Actual square: complete residual and quantum floor

The [subsequent continuation](../w6_square_block_20260909/SQUARE_BLOCK_RESULT.md)
first proves complete first-order cancellation on every finite open
strip, then computes the actual twelve-edge 2x2 square where that
cancellation fails. Its complete first force is nonzero and obeys the
sharp all-radial-source inverse-energy bound
\((4-\sqrt2)^3/1372\) times the retained reference energy.

The full next insertion \(\rho_1=QW_1F_0^{-1}t_1\varphi\) is also
computed and estimated for all radial finite-energy sources:
\(\|\rho_1\|^2\le b[\varphi]/256\) and
\(\langle\rho_1,F_0^{-1}\rho_1\rangle\le b[\varphi]/512\).
Its first diagonal defect vanishes by parity. The estimates retain
the complete source-compatible operator and full horizontal inverse.

The same continuation proves a small-coupling floor \(F_g\ge2\) for
the actual compact square using quantum localization and min-max.
This supplies an interacting-inverse estimate for the computed leading
residual component. The fixed-block threshold is not asserted uniform
over larger coupled lattices.

Finally, it constructs an exact finite-g source isometry and exhibits
an explicit Gaussian finite-energy source whose transported compact
energy is infinite. A compact Haar source reference with a common
weighted form domain is constructed, with full form-preserving source
transport at positive coupling. Thus the next full finite-g residual
estimate has an explicit admissible core and source-norm choice; the
first coefficient is no longer the uncomputed step.

## 9. Full compact-reference finite step and shared-edge grid floor

The [next continuation](../w6_compact_continuation_20260909/CONTINUATION_RESULT.md)
proves a complete finite-coupling selected-inverse comparison around every
positive compact reference on the actual square. Its exact source-range
and vacuum transport is norm smooth on the physical form domain. The
nonreducing graph, complete operator difference and all retained form
energies are included. A cubic Schur remainder and actual source-energy
comparison follow. Its constants depend on the positive reference
interval; this is not identified with the Gaussian-reference W6 at zero.

For actual shared-edge 2m by 2n planar rectangles, the same continuation
proves the volume-independent Gaussian fast floor 1/sqrt(2), using the
original edge incidence matrix, the covariance-weighted retained source
and second quantization. It does not assume that the retained source
reduces the coupled operator.

The actual compact square ground now has uniform potential moments and
exponential concentration. An explicit compact dilation preserving the
outer-trace algebra removes its singular 1/g motion, with a bounded
derivative in Hilbert and actual quantum energy norms. The computed
first ground correction also has a proved finite-g O(g^2) remainder.

The remaining source-weighted estimate is expressed by an explicit
conditional-variance tail/resistance quantity B_g. Its averaged variance
is controlled; its uniform tail bound and the interacting growing-volume
floor are not yet established. The continuation supplies 115 new exact
finite controls alongside the analytic proofs.
