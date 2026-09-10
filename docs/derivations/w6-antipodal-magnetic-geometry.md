# W6 antipodal magnetic geometry and the remaining conditional score

10 September 2026. Reviewed continuation of the
[conditional transport obstruction](w6-conditional-transport-obstruction.md),
especially S2 and S6.

The supplied calculation is correct under the quaternion and original-edge
normalizations below. It establishes seven uniformly positive magnetic Hessian
directions and a two-dimensional gauge kernel at the antipode. It also gives
the leading angular potential after normal relaxation. These are established
analytic inputs to the selected synchronized M10 route. The actual conditional
ground-amplitude, differentiated score and complement estimates remain open.

The [received text](../../runs/w6_antipodal_m10_2026-09-10/sources/pasted-text.txt)
is preserved byte for byte. The author supplied the calculation; this review
adds independent executable checks and expands its orbit, metric and
implicit-function arguments. The original square geometry, constrained
minimizer, actual ground symmetry and synchronized transport are prior project
inputs. See the [review and verification record](../../runs/w6_antipodal_m10_2026-09-10/README.md).

## A1 Exact fixed-Q chart

Use unit quaternions with
\((s,v)(t,w)=(st-v\cdot w,sw+tv+v\times w)\), and write
\(\operatorname{Sc}U=\operatorname{tr}(U)/2\). In particular the vectors below
are quaternion angles, not the twice-as-large Lie coordinates for \(i\sigma/2\).
The actual twelve-edge four-face potential is

\[
 V=16-4\operatorname{Sc}(U_0+U_1+U_2U_0^{-1}+U_3U_1^{-1}).
\]

For \(Q=\exp(\theta n)\), \(0\leq\theta\leq\pi\), set
\(\alpha=\theta/4,\ A=\exp(\alpha n),\ B=A^2,\ Q=A^4\).
The prior S2 minimizer is \(U_0=U_1=A,\ U_2=U_3=B\), and
\(v_*(\theta)=16(1-\cos\alpha)\). At \(\theta=0\), choose any axis; the
configuration itself is unique.

With fixed \(A,B,Q\), take the local nine-dimensional chart

\[
 U_0=Ae^a,\quad U_1=A^{-1}e^bB,\quad
 U_2=Be^c,\quad U_3=e^{-c}B,\qquad a,b,c\in\mathbb R^3.
 \tag{A1}
\]

It preserves \(U_2U_3=Q\) exactly. Quaternion scalar cyclicity, \(A^{-1}B=A\)
and \(BB^{-1}=I\) give

\[
 V=16-4\operatorname{Sc}
 \left(Ae^a+Ae^ce^{-a}+Ae^b+Ae^{-c}e^{-b}\right). \tag{A2}
\]

No commutation of the variations is used. The executable check verifies this
identity for arbitrary unit-quaternion variations before Taylor expansion.

## A2 Noncommutative quadratic form

Write \(C=\cos\alpha,\ S=\sin\alpha\). Expanding the original four face words,

\[
 V-v_*(\theta)=
 2C\left(|a|^2+|c-a|^2+|b|^2+|c+b|^2\right)
 -4S\,n\cdot[c\times(a-b)]+O(|(a,b,c)|^3). \tag{A3}
\]

The linear term vanishes. The cross product is essential. Put
\(p=(a+b)/\sqrt2,\ m=(a-b)/\sqrt2,\ Jm=n\times m\). This is an orthogonal
change for the specified chart norm, and the quadratic term is

\[
 4C(|p|^2+|m|^2+|c|^2)-4\sqrt2\,c\cdot(CI-SJ)m. \tag{A4}
\]

Thus the Hessian is twice the matrix of this quadratic form.

## A3 Full spectrum and seven uniform directions

The singular values of \(CI-SJ\) are \(C\) along \(n\), and \(1,1\) on
\(n^\perp\), since \(C^2+S^2=1\). In the norm
\(|a|^2+|b|^2+|c|^2\), the complete conditional Hessian spectrum is

| Eigenvalue | Multiplicity |
| --- | ---: |
| \(8C\) | 3 |
| \((8-4\sqrt2)C\) | 1 |
| \((8+4\sqrt2)C\) | 1 |
| \(8C-4\sqrt2\) | 2 |
| \(8C+4\sqrt2\) | 2 |

Since \(1/\sqrt2\leq C\leq1\), the seven eigenvalues other than the double
soft branch obey

\[
 \lambda_{\mathrm{normal}}\geq4(\sqrt2-1)>0. \tag{A5}
\]

The soft branch is positive for \(\theta<\pi\), vanishes exactly at \(\pi\),
and, for \(\delta=\pi-\theta\),

\[
 8\cos((\pi-\delta)/4)-4\sqrt2
 =\sqrt2\,\delta-\frac{\sqrt2}{8}\delta^2+O(\delta^3). \tag{A6}
\]

Here "normal" names the seven-dimensional spectral complement continued from
the antipodal normal directions; there is no minimum sphere on a regular
fixed-Q fiber. The constants are chart-metric constants, not asserted
eigenvalues in the original electric metric.

## A4 The antipodal kernel is exactly gauge

At \(Q=-I\) the complete minimizing set, in \(y=(U_0,U_1,U_2)\), is

\[
 \mathcal M=\{(\exp(\pi n/4),\exp(\pi n/4),\exp(\pi n/2)):n\in S^2\}.
 \tag{A7}
\]

The prior constrained minimization argument gives completeness of this set.
It is a smooth embedded sphere: \(U_2=n\) recovers its axis. Simultaneous
conjugation acts transitively, with stabilizer the rotations about \(n\);
\(\mathcal M\) is one gauge orbit in this based description.

At \(n=e_3\), let \(v\perp n\) be an axis variation and \(Jv=n\times v\).
Inverting the differential of A1 gives its chart tangent

\[
 (a,b,c)=\left(\frac{v-Jv}{2},\frac{-v+Jv}{2},-Jv\right). \tag{A8}
\]

Its squared chart norm is \(2|v|^2\). The exact Hessian annihilates both
independent columns A8 and has rank seven. Rotation covariance gives, at
every point of \(\mathcal M\),

\[
 \ker\operatorname{Hess}(V|_{Q=-I})=T\mathcal M. \tag{A9}
\]

This is a Morse-Bott minimum: a smooth minimum manifold with strictly
positive Hessian in its normal directions.

## A5 Comparison with the original electric metric

Let \(G_{\rm product}\) be the product unit-quaternion metric on \(SU(2)^4\),
and let \(G\) be the inverse of the full original-edge cometric
\(\Gamma(f,f)=\sum_{e,j}(E_{e,j}f)^2\).
The [original edge table](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/geometry.md)
includes independent \(L_0,L_1,L_2,L_3\). Each uses \(T=i\sigma/2\), so its
three axes contribute one quarter of the unit-quaternion product cometric.
Every other edge contributes a positive semidefinite square. Consequently

\[
 \Gamma\geq\tfrac14G_{\rm product}^{-1},\qquad
 G\leq4G_{\rm product}. \tag{A10}
\]

This also proves ellipticity. In A1 at the minimum, all left/right
multiplications are isometries; the \(c\) variation appears in both \(U_2\)
and \(U_3\). The pulled-back product metric is
\(\operatorname{diag}(I,I,2I)\leq2I\). Hence \(G\leq8I\) on the chart tangent.

At an antipodal minimum decompose a tangent vector as \(\xi=k+z\), with
\(k\in T\mathcal M\) and \(z\) chart-orthogonal to it. A9 gives
\(\operatorname{Hess}V[\xi,\xi]=\operatorname{Hess}V[z,z]\).
Moreover \(\operatorname{dist}_G(\xi,T\mathcal M)^2\leq G[z,z]\leq8|z|^2\).
Combining with A5,

\[
 \operatorname{Hess}V[\xi,\xi]\geq
 \frac{\sqrt2-1}{2}\operatorname{dist}_G(\xi,T\mathcal M)^2. \tag{A11}
\]

Distance here is the linear tangent-space distance at that minimum, with
the induced fixed-Q metric. It is not distance to a distant configuration
or a claim about Hessians away from the minimum.

## A6 Angular continuation and normal relaxation

Use the common compact fiber \(y=(U_0,U_1,U_2)\in SU(2)^3\) and set

\[
 Q_\delta=-\cos\delta+\sin\delta\,e_3,\qquad
 U_3=U_2^{-1}Q_\delta .
\]

On the old sphere A7, direct multiplication in the original potential gives

\[
 V_\delta(n)=16-2\sqrt2[3+\cos\delta+\sin\delta\,n_3]
 =16-8\sqrt2-2\sqrt2\,\delta n_3+O(\delta^2). \tag{A12}
\]

The remainder is uniform over \(S^2\). This is the restriction to the old
sphere, before relaxation.

For completeness, choose a smooth invariant auxiliary metric on the common
fiber and a tubular neighborhood identified with a neighborhood of the zero
section of the rank-seven normal bundle \(N\mathcal M\). Write the potential
there as \(F(\delta,n,z)\). Its vertical differential satisfies
\(F_z(0,n,0)=0\), and its vertical Hessian is uniformly positive and invertible
by A5 and compactness. The parameter-dependent implicit function theorem
gives a unique small section \(z_\delta(n)\) solving \(F_z=0\).
Local solutions agree on overlaps by uniqueness; compactness supplies one
uniform neighborhood and \(\|z_\delta\|_{C^k}=O(|\delta|)\) for each fixed
finite \(k\), since the potential is smooth. No global trivialization of
\(N\mathcal M\) is required.

Taylor expansion in \(z\), using \(F_z(\delta,n,0)=O(\delta)\), yields
\(F(\delta,n,z_\delta)-F(\delta,n,0)=O(\delta^2)\), uniformly in \(n\).
Therefore the normally relaxed magnetic angular potential is

\[
 V_{\mathrm{eff},\delta}(n)
 =16-8\sqrt2-2\sqrt2\,\delta n_3+O(\delta^2). \tag{A13}
\]

This is a magnetic reduction, not an effective quantum Hamiltonian or an
asymptotic formula for the ground density. For \(\delta>0\), only the
stabilizer of \(Q_\delta\) acts within its fixed-Q fiber. Full angular
variation is not then a gauge orbit; the nonconstant \(n_3\) term is retained.

## A7 Gauge-invariant score and the open successor

For the actual normalized positive ground \(\Psi_g\) and the specified
smooth conjugation-equivariant synchronized transport,
\(D=Z+\tfrac12\operatorname{div}_{\rm Haar}Z\), let

\[
 \sigma_g=\frac{\partial_g\Psi_g+D\Psi_g/g}{\Psi_g}. \tag{A14}
\]

The Hamiltonian and Haar measure are conjugation invariant, so the simple
positive normalized ground is invariant. Its derivative in positive \(g\)
is invariant as well. Equivariance of \(Z\) and invariance of Haar measure
make its divergence invariant and \(D\) commute with conjugation. Thus A14
is constant on every simultaneous-conjugation orbit. In particular its
differential on the antipodal sphere annihilates all of A9:

\[
 d\sigma_g|_{T\mathcal M}=0,\qquad g>0. \tag{A15}
\]

This is an exact symmetry statement. It gives no bound on normal score
derivatives or on the conditional variance over the full antipodal fiber.

**Consequence for M10.** The magnetic antipodal normal-positivity problem
has been resolved, including its actual-electric-metric comparison and
leading angular transition. These inputs allow the remaining true-ground
conditional amplitude and score analysis to use seven controlled normal
directions and a compact angular variable. One must still establish
uniform differentiated relative-amplitude control, actual conditional
moments, and the complement bound with the same reference as S14-S15.
No equality of the magnetic Hessian with \(-\log\Psi_g\), the Agmon Hessian
or the conditional quantum precision is assumed.

The selected synchronized target and the generic M10 target remain open.
M11-M15 apply after M10 is established for the chosen transport. Complete
source-energy jets R10, interacting-volume estimates and continuum
transport keep their separate obligations.

## A8 Reproduction and review scope

Run from the repository environment:

~~~text
workhouse verify --only 'W6 antipodal:'
python scripts/check_w6_antipodal.py --out NEW_PATH.json
~~~

The seven native T1 checks reconstruct the original noncommuting chart,
quadratic form, full characteristic polynomial, uniform eigenvalue bound,
endpoint scaling, tangent kernel, metric normalization and angular restriction.
The companion replay also evaluates 60 seeded original-potential second
directional derivatives, including both endpoints, against the quadratic
form, with its stated numerical tolerance. Their results belong to this
review's retained run, separately from the earlier report's claimed execution.

The global minimum classification uses prior S2. The normal-bundle implicit
function, positive-cometric inversion, gauge symmetry and true-ground
identification are reviewed analytic arguments, with their dependencies
above; the exact algebra checks do not formally prove all of them.
The full analytic results retain status proven and evidence analytic,
with T3 for full-statement machine coverage and separate T1 support nodes.
No new Lean proof is claimed.
