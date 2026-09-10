# Actual finite-coupling quantum floor on the coupled square

This proof concerns the actual twelve-edge, four-face compact square.
It supplies a positive floor for its full physical fast compression at
small nonzero coupling, using the quantum spectrum and true vacuum.

## Exact compact operator

On M=SU(2)^4 with product Haar measure, let E_(e,c) be the original-edge
fields in `geometry.md`, with color index c. The normalized operator is

\[
H_g=-\frac{g^2}{2}\sum_{e,c}E_{e,c}^{\,2}+g^{-2}V,
\quad
V=4\left[4-\frac{\operatorname{Tr}U_0}{2}
-\frac{\operatorname{Tr}U_1}{2}
-\frac{\operatorname{Tr}(U_2U_0^{-1})}{2}
-\frac{\operatorname{Tr}(U_3U_1^{-1})}{2}\right].
\tag{F1}
\]

Every summand in V is nonnegative. Equality forces U0=U1=I and then
U2=U3=I. Thus V has precisely one zero on M. The four non-tree edge
fields include the full three left derivatives on each group variable.
Consequently the electric form is uniformly elliptic on this compact
manifold. It is invariant under simultaneous conjugation; physical states
are the invariant subspace.

At the unique minimum, write Ui=exp(theta_i.i sigma/2). Taylor expansion
gives V(theta)=theta^T M0 theta/2+O(|theta|^3), with positive matrix

\[
M_0=\begin{pmatrix}2&0&-1&0\\0&2&0&-1\\-1&0&1&0\\0&-1&0&1\end{pmatrix}.
\]

The exact tangent electric matrix is C from `geometry.md`. In the
coordinates theta=gX, the limiting oscillator is

\[
H_0=-\frac12\nabla^T C\nabla+\frac12 X^T M_0X,
\]

tensored with the color identity. Its four frequencies are
\(\sqrt2,2,2,\sqrt6\). Put
\(e_0=\frac32(\sqrt2+4+\sqrt6)\).

## Low eigenvalue convergence, proved by localization and min-max

Fix the finite square. Let d denote any smooth-background Riemannian
distance from the identity tuple. Positive Hessian at the unique minimum
and compactness away from it give a number c>0 such that
V(U)>=c d(U,I)^2 everywhere. Therefore every normalized state f_g with
bounded H_g energy satisfies

\[
\int_{d(U,I)>gR}|f_g|^2\,dU\le\frac{C}{cR^2}.
\tag{F2}
\]

Take a smooth coordinate cutoff equal to one near I. Rescale its product
with f_g by theta=gX, including the Haar square-root density. The omitted
mass tends to zero by (F2). Uniform ellipticity and the kinetic energy
bound give uniform H1 bounds on every fixed X-ball. Rellich compactness,
followed by (F2) as R tends to infinity, gives a subsequence converging
strongly in L2(R12). Its norm is preserved.

On each fixed ball the rescaled electric coefficients, Haar density and
potential converge smoothly to their oscillator values. Weak lower
semicontinuity of the nonnegative kinetic energy and convergence of the
potential give

\[
\langle f,H_0f\rangle
\le\liminf_{g\to0}\langle f_g,H_gf_g\rangle.
\tag{F3}
\]

One can obtain this inequality first on fixed balls, then increase their
radius; no boundary subtraction or global Gaussian form comparison is
used. A diagonal compactness argument applies to each fixed finite family
of orthonormal eigenvectors, preserving their inner products and invariant
symmetry. This supplies the min-max lower bound for every fixed physical
eigenvalue.

Conversely, multiply finitely many physical Gaussian eigenfunctions by a
radial cutoff in a fixed small group chart, rescale back, and include the
inverse Haar square-root density. Their Gram and energy matrices converge
to the Gaussian ones. Smooth coefficient bounds and Gaussian decay control
the cutoff annulus and tails. Min-max supplies the matching upper bounds.
Thus every fixed physical eigenvalue converges to the corresponding
physical oscillator eigenvalue, counted with multiplicity.

## Vacuum subtraction and fast compression

Uniform ellipticity on connected M gives a unique strictly positive ground
state Psi_g. Symmetry and uniqueness imply that it is physical. The first
nonconstant physical oscillator state has excitation energy 2sqrt(2):
one-quantum states transform as color vectors, while the radial two-quantum
state of the lowest-frequency vector is invariant. All other invariant
excitations have at least this energy. Therefore

\[
e_g\longrightarrow e_0,
\qquad
\lambda_1^{\rm phys}(H_g)-e_g\longrightarrow2\sqrt2.
\tag{F4}
\]

It follows that there exists g_*>0 such that

\[
\boxed{H_g-e_g\ge2I\quad\text{on }\{\Psi_g\}^{\perp}
\cap\mathcal H_{\rm phys},\quad0<|g|<g_*.}
\tag{F5}
\]

Let Pg be the exact retained-source projection constructed from Psi_g and
the literal outer trace, so that its range contains Psi_g. Let Qg=I-Pg
on the physical space, and define Fg by the closed-form compression to Qg.
Equation (F5) immediately yields the actual coupled quantum floor

\[
\boxed{F_g\ge2I,\qquad
\|(F_g-z)^{-1}\|\le\frac1{2-\operatorname{Re}z}
\quad(\operatorname{Re}z<2).}
\tag{F6}
\]

The compression form is densely defined: smooth physical functions can
be centered by their smooth conditional expectation in the outer
holonomy, and are dense in Qg. Equivalently, use the smooth compact
holonomy disintegration with the positive smooth density Psi_g^2.
This statement is independent of any Gaussian identification of the
full finite-g source form domain.

Equivalently, for the **true coupled quantum measure**
\(d\mu_g=\Psi_g^2\,dU\), the ground-state transform gives

\[
\boxed{\frac{g^2}{2}\sum_{e,c}\int|E_{e,c}f|^2\,d\mu_g
\ge2\int|f|^2\,d\mu_g,
\qquad E_{\mu_g}[f\mid w]=0,\quad f\text{ physical}.}
\tag{F7}
\]

Indeed conditional centering implies total centering, and the left side
is exactly the vacuum-subtracted quantum form on Psi_g f. All original
edge directions are retained in this inequality.

## Interacting inverse applied to the computed residual coefficient

The independently audited estimate in `residual_inverse.md` gives
\(\|\rho_1\varphi\|^2\le K_{\rm res}b[\varphi]\), where
\(K_{\rm res}=0.0037824649150914063\ldots<1/256\).
Let U_g be a unitary identification of the reference fast Hilbert space
with the exact physical Qg space, and put
\(A_g=U_g^*F_gU_g\). Such Hilbert-space identifications exist; the floor
is independent of their choice. Then (F6), without any comparison with
the Gaussian form, proves

\[
\boxed{
\langle g\rho_1\varphi,A_g^{-1}g\rho_1\varphi\rangle
\le\frac{g^2 K_{\rm res}}2 b[\varphi]
\le\frac{g^2}{512}b[\varphi].}
\tag{F8}
\]

This bound involves the **actual interacting inverse** acting on the
transported first residual coefficient. Its validity uses the all-source
L2 bound established for that complete coefficient, rather than assuming
such an L2 bound for the complete finite-g residual. For a real shift
z<2 the right side is g^2 K_res/(2-z) times b for this same coefficient.

To apply this to the entire W6 residual one must use the actual source
transport, identify its first coefficient with rho_1, and control the
remaining finite-g residual in the same interacting dual norm. A
Hilbert-space unitary alone does not preserve the relevant form domains;
the source-domain calculation in `finite_g_source_domain.md` addresses
that additional issue explicitly.

## Scope of the constant

This is an actual finite-g quantum coercivity result for the coupled
four-face square, not a classical Hessian inference: localization and
quantum min-max control the true ground subtraction and the entire
excited physical space. It neither assumes nor proves a conditional
vertical gap at each retained value.

The threshold g_* is an existence threshold for this fixed block. The
proof does not claim that it or its localization constants are uniform
over growing lattices or external boundary backgrounds. Extending that
uniformity requires a further estimate on the actual coupled family.
