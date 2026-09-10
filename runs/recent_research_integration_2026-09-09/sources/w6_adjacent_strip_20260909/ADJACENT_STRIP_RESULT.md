# Actual adjacent Wilson strip: complete force and inverse-energy calculation

9 September 2026. The seven-edge, two-plaquette SU(2) block, with its
shared electric derivative and literal retained holonomy U=U1 U2.

The immediate calculation is complete. The full first physical force
vanishes. The first nonzero transported force, at order g^2, is explicit,
and its full Gaussian fast inverse satisfies an all-retained-energy bound.
The calculations include the electric metric, Haar half-density, true
quantum ground correction and true marginal normalization.

## 1. Exact operator of the shared-edge block

Use T_a=i sigma_a/2 and the invariant metric making these generators
orthonormal. The electric form is one half of

    3(|grad_1 F|^2+|grad_2 F|^2)
      + sum_a |(L1_a-R2_a)F|^2.

Thus the shared edge is retained explicitly. On physical wavefunctions
set x=Tr(U1)/2, y=Tr(U2)/2, w=Tr(U1 U2)/2. These are complete orbit
coordinates, with Haar density 2/pi^2 on

    1-x^2-y^2-w^2+2xyw >= 0,  -1<=x,y,w<=1.

The exact Hamiltonian is

\[
H_u=-\tfrac12\operatorname{div}(G\nabla)+4u(2-x-y),
\qquad
G=\begin{pmatrix}
1-x^2&(w-xy)/4&3(y-xw)/4\\
(w-xy)/4&1-y^2&3(x-yw)/4\\
3(y-xw)/4&3(x-yw)/4&3(1-w^2)/2
\end{pmatrix}.
\tag{A1}
\]

Let Omega_u be its true positive ground, and let P_u be conditional
expectation onto w in the ground probability. The exact ground-transformed
operator is L_u=Omega_u^(-1)(H_u-E_u)Omega_u. Direct substitution gives

\[
Q_u L_u P_u p
=-(\tau_u-\mathbb E[\tau_u\mid w])p'(w),
\tag{A2}
\]

where

\[
\tau_u=\frac34\left[(y-xw)\partial_x\log\Omega_u
+(x-yw)\partial_y\log\Omega_u
+2(1-w^2)\partial_w\log\Omega_u\right].
\]

All retained second derivatives cancel under Q_u because G_ww depends
only on w. This is an exact full-operator identity for this interacting
two-face block. Its derivation is in [operator.md](operator.md).

## 2. The complete first force vanishes

Simultaneous inversion of two SU(2) holonomies preserves their physical
orbit: a rotation through pi around a common perpendicular reverses both
quaternion vectors. In particular x,y,w are unchanged. In signed weak-field
coordinates this reverses both Lie vectors and acts as the identity on
physical scalar wavefunctions. The rescaling and Haar factor are even.

Consequently, on the fixed-cell physical coefficient core,

\[
H_1=0,\quad e_1=0,\quad \psi_1=0,\quad J_1^{\rm lit}=0.
\]

The source statement includes the BCH term: for a class source its first
variation is proportional to
\(\langle X+Y,[X,Y]\rangle=0\). The true first marginal correction
vanishes too. With the compatible even source-straightening jet,

\[
W_1=H_1-e_1+[H_0,K_1^{\rm src}]=0,
\qquad t_1=QW_1J_z=0. \tag{A3}
\]

Thus the W6 first-force expression is identically zero for this block and
source jet. This does not mean that its finite-g off-diagonal source (A2)
vanishes. We compute its first nonzero coefficient next.

## 3. True-ground and source corrections at order g^2

Set g=u^(-1/4). Use the local chord chart

\[
U_1=\sqrt{1-g^2|X|^2/4}\,I+i(gX/2)\cdot\sigma,
\quad
U_2=\sqrt{1-g^2|Y|^2/4}\,I+i(gY/2)\cdot\sigma.
\]

Write q=(X+Y)/sqrt(2), s=(X-Y)/sqrt(2), and
a=|q|^2, b=|s|^2, c=q dot s. The normalized quadratic operator and
ground are

\[
H_0=-\tfrac32\Delta_q-\tfrac52\Delta_s+\tfrac12(a+b),
\quad e_0=\tfrac32(\sqrt3+\sqrt5),
\quad \Omega_0\propto e^{-a/(2\sqrt3)-b/(2\sqrt5)}.
\tag{A4}
\]

The two Gaussian covariance constants are sigma_q=sqrt(3)/2 and
sigma_s=sqrt(5)/2. The reference retained physical space consists of
radial functions phi(a), times Omega_0, and reduces H_0.

The complete electric and magnetic second jet gives the actual ground
energy coefficient

\[
e_2=-\frac{39}{32}-\frac{9\sqrt{15}}{640}. \tag{A5}
\]

The normalized polynomial p_2 in Psi_g=Omega_0(1+g^2p_2+...) is computed
explicitly in [residual.md](residual.md). It satisfies the complete
ground equation and E[p_2]=0; it is not a classical Gibbs coefficient.

Choose the literal retained trace coordinate

\[
a_g=\frac4{g^2}\left(1-\tfrac12\operatorname{Tr}(U_1U_2)\right)
=a+g^2c^2/8+O(g^4).
\]

Its true relative marginal coefficient is

\[
m_2(a)=-\frac{15\sqrt3}{512}-\frac{9\sqrt5}{640}
+\left(\frac{15}{128}+\frac{\sqrt{15}}{320}\right)a
-\frac{5\sqrt3}{384}a^2.
\tag{A6}
\]

The complete source normalization is therefore

\[
J_2^{\rm lit}\phi
=\Omega_0\left[(p_2-m_2/2)\phi+\frac{c^2}{8}\phi'\right].
\tag{A7}
\]

The independent [source calculation](source_parity.md) verifies the
observation jet, marginal pushforward and isometry coefficient.

## 4. Explicit complete first nonzero fast force

Let F_0 be the restriction of H_0-e_0 to the physical reference Q space,
and use the equivalent ground-transformed Gaussian representation. Put

\[
\beta=b-\frac{3\sqrt5}{2},
\qquad \gamma=c^2-\frac{\sqrt5}{2}a,
\qquad k=\frac{3(\sqrt5-\sqrt3)}{160}.
\]

Assembling H_2, p_2, m_2 and the observation derivative gives, for every
smooth retained radial source,

\[
\boxed{t_2\phi=k[-11a\beta+6\gamma]\phi'(a).} \tag{A8}
\]

This is the complete coefficient of the transported off-diagonal source.
In the wavefunction representation the right side is multiplied by
Omega_0. Because P_0 reduces H_0, the Q-to-Q extension of the second
source generator does not enter QW_2P_0. The assembly uses only

    Q[H2 J0 phi + (H0-e0)J2 phi - J2 L_ret phi],
    L_ret=-6a d_aa+(2sqrt(3)a-9)d_a.

The retained-second-derivative coefficient from H_2 is
3(a^2+c^2)/4. The observation transport cancels 3c^2/4; the remaining
3a^2/4 is retained-only and is killed by Q. The remaining first derivative
is exactly (A8). This cancellation was checked independently.

## 5. Full inverse energy: explicit first excitation

For phi_1(a)=a-3sqrt(3)/2, define the retained energy

\[
\mathfrak b[\phi]=\tfrac32\mathbb E|\nabla_q\phi|^2
=6\mathbb E[a|\phi'(a)|^2].
\]

Then b_frak[phi_1]=9sqrt(3). Direct inversion of the full Gaussian fast
operator gives

\[
\begin{split}
\langle t_2\phi_1,(F_0-z)^{-1}t_2\phi_1\rangle
=(\sqrt5-\sqrt3)^2\bigg[
&\frac{295245}{204800(2\sqrt5-z)}\\
&+\frac{122715}{102400(2(\sqrt3+\sqrt5)-z)}\bigg].
\end{split} \tag{A9}
\]

The second denominator includes the horizontal frequency sqrt(3).
At z=0 this is

\[
\frac{1095201\sqrt5}{204800}-\frac{2187\sqrt3}{320}
\simeq0.120249075624.
\]

Dividing by the retained energy gives

\[
\frac{40563\sqrt{15}}{204800}-\frac{243}{320}
\simeq0.007714.
\]

These are exact algebraic computations of the complete nonzero coefficient,
not fits to sampled couplings.

## 6. Bound over all retained radial energies

The same coefficient has the uniform synthesis estimate

\[
\boxed{\langle t_2\phi,F_0^{-1}t_2\phi\rangle
\le\frac{6561(4-\sqrt{15})}{5120}\,\mathfrak b[\phi].}
\tag{A10}
\]

The constant is approximately 0.1627649. Here is a direct proof retaining
the full inverse.

Let Q_ij(s)=s_i s_j-sigma_s delta_ij, and set

    M_ij phi=6 q_i partial_j phi-11 delta_ij(q dot grad phi).

Equation (A8) is t_2 phi=(k/2)sum_ij Q_ij M_ij phi. Every Q_ij has fast
Hermite degree two. The full inverse on this space is therefore
(L_q+2sqrt(5))^(-1), with L_q=sqrt(3)N_q, and Gaussian covariance gives

    <t2 phi,F0^-1 t2 phi>
      <= (k^2 sigma_s^2/2) sum_ij
         ||(L_q+2sqrt(5))^-1/2 M_ij phi||^2.             (A11)

For the matrix transformation R -> 6R-11Tr(R)I the Frobenius operator
norm is 27: it acts by 6 on traceless matrices and by -27 on scalar
matrices. Thus the sum in (A11) is bounded by 729 times the corresponding
sum for R_ij=q_i partial_j phi.

In Gaussian creation/annihilation notation q_i=sqrt(sigma_q)(a_i+a_i*).
For c_*=2sqrt(5)/sqrt(3)>1, both

    ||(N_q+c_*)^-1/2 a_i|| <= 1,
    ||(N_q+c_*)^-1/2 a_i*|| <= 1.

These follow on each Hermite degree from
n_i/(n-1+c_*)<=1 and (n_i+1)/(n+1+c_*)<=1. Consequently

    ||(L_q+2sqrt(5))^-1/2 q_i|| <= sqrt(2),
    sum_ij ||(L_q+2sqrt(5))^-1/2 q_i partial_j phi||^2
       <=6 ||grad phi||^2.

Combining these inequalities and b_frak=(3/2)||grad phi||^2 yields
(3645/2)k^2 b_frak, which is exactly (A10). No vertical-only inverse or
unweighted residual L2 bound was used.

Prove the estimate first on Gaussian radial polynomials, then extend by
continuity in the retained energy norm. The resulting force may be a
form-dual vector rather than an L2 vector. The same constant works for
real z<=2sqrt(5)-sqrt(3), where the shifted ladder parameter stays at
least one and the physical reference fast inverse remains positive.
Indeed a physical fast oscillator state has either at least two fast
quanta or at least one fast and one retained quantum. Its excitation
energy is therefore at least sqrt(3)+sqrt(5), strictly above that interval.

## 7. What was computed

- The exact shared-edge operator and complete true-ground source (A1)-(A2).
- The complete first physical jet t_1=0, including the source correction.
- The actual fixed-cell second ground, marginal and source coefficients.
- The explicit nonzero t_2 on every retained radial source.
- An exact full inverse-energy value and the all-retained-energy bound (A10).

Equations (A5)-(A10) concern the computed fixed-cell weak-field coefficients
and the full reference inverse. They do not replace the finite-g operator
by its truncated series. Source-chart and cutoff domains are recorded in
the companion notes. The analytic all-energy argument was independently
audited in [inverse_synthesis_audit.md](inverse_synthesis_audit.md);
the scripts verify the finite algebra and coefficient assembly. The four
verification scripts passed 65 exact controls in total: 15 operator,
25 source, 17 residual and 8 inverse-synthesis controls.
No existing graph status or source theorem was changed.
