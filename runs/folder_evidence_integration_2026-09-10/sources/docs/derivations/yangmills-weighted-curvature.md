# Weighted curvature, trial ground states, and a residual gap certificate

This derivation makes the G20/G23 curvature route usable without first knowing an exact ground state. Its main conditional conclusion is

\[
\boxed{\operatorname{gap}(H)\geq c\kappa-
       \bigl(\mathbb E_\nu R-\inf R\bigr)},\qquad
R=\frac{H\psi}{\psi},\quad \psi=N e^{-S/\hbar}.
\tag{GST-6}
\]

The required inputs are a global weighted-curvature floor, a global lower bound on the trial-state residual, and its weighted mean. An upper bound on the residual is unnecessary. The formula gives a concrete positive certificate for the pure quartic oscillator below. No claim of priority over the published literature is made for this derivation.

The exact checks live in [ym_ground_state.py](../../src/workhouse/invariants/ym_ground_state.py). They check differential expressions in flat dimension two, finite matrix algebra, normalization, a quartic certificate, and three falsifiers. The analytic implications are conditional on the operator and domain hypotheses stated here. These checks do not discharge G20, G23, or continuum existence G19.

## Source and graph position

The source conventions are pinned to the acquired versions, not an unspecified latest revision.

| Source | Locators in the pinned PDF | Use here |
|---|---|---|
| [Moncrief–Marini–Maitra, arXiv:1809.06318v2](https://arxiv.org/pdf/1809.06318v2), `MMM_2019_CURVATURE` | pp. 9–12, (II.2), (II.4), (II.9), (II.13), (II.16), (II.22)–(II.23) | Hamiltonian, exponential ground state, conjugation, weighted curvature, gap normalization |
| Same | pp. 12–13, (II.24)–(II.27); pp. 13–17, (II.28)–(II.37) | Oscillator calibration and continuous-spectrum discussion |
| [Mondal, arXiv:2301.06996v7](https://arxiv.org/pdf/2301.06996v7), `MONDAL_2023_GEOMETRIC` | p. 4, Theorem 1.1 and Remark 1; pp. 18–21, (4.1), (4.4), (4.8)–(4.11); pp. 21–22, regulator-removal discussion | Yang–Mills formulation and its stated existence, ground-state, curvature, and regulator assumptions |

The SHA-256 values are `f30b76a441cfedc54c0a3d8b82ab3613be56eaa205d4f46233606845de114e04` for MMM v2 and `fc8f358875ddb6da3a981c829fd7099a76cf246d7a94084849dd7122772cd498` for Mondal v7. PDF page numbers include the first PDF page as page 1. Metadata and local access paths are in [sources_related.json](../../literature/yangmills/sources_related.json).

MMM derives the finite-dimensional comparison using the true ground-state weight. Mondal states a conditional Yang–Mills gap bound assuming an existing quantum theory, a normalizable ground state, and a positive uniform renormalized curvature bound after regulator removal. The residual extension and quartic calculation here retain a trial state's error explicitly.

`workhouse why G20` and `workhouse why G23` were inspected before this derivation. G20's local SAFE-region Hessian certificate does not provide a global curvature bound. G23 also records the unresolved identification of diffusion time with physical Euclidean time. The construction below supplies a precise sufficient identification: derive the weighted generator by unitary conjugacy from the physical Hamiltonian, keeping its residual potential. A sampling generator built from another action or measure still requires a separate identification.

## GST-1: exact conjugation with a trial-state residual

Let \((M,g)\) be a smooth finite-dimensional Riemannian configuration space. On a common smooth core, set

\[
H=-c\Delta_g+V,\qquad c=\frac{\hbar^2}{2m}>0,
\quad \psi=N e^{-S/\hbar}>0,
\quad \int_M\psi^2\,d\mathrm{vol}_g=1.
\]

Here \(c\) is the kinetic prefactor. The source \(S\) is the logarithm of the trial wavefunction with this normalization; it need not be the classical Yang–Mills action. Define

\[
d\nu=\psi^2d\mathrm{vol}_g,\quad
L_S=\Delta_g-\frac2\hbar\langle\nabla S,\nabla\cdot\rangle,
\quad A_S=-cL_S.
\]

The product rule gives

\[
\frac{\Delta_g\psi}{\psi}
=-\frac{\Delta_g S}{\hbar}
 +\frac{|\nabla S|^2}{\hbar^2},\qquad
R:=\frac{H\psi}{\psi}
=V+\frac c\hbar\Delta_g S-\frac c{\hbar^2}|\nabla S|^2.
\]

For \(Uf=\psi f\), \(U:L^2(\nu)\to L^2(d\mathrm{vol}_g)\) is unitary, and the exact differential identity is

\[
\boxed{U^{-1}HUf=A_Sf+Rf.}
\tag{GST-1}
\]

When \(R\equiv E_0\), this is the source's ground-state transform, \(U^{-1}(H-E_0)U=A_S\). For a trial \(S\), deleting \(R\)'s variation changes the operator. Adding a constant to \(V\) shifts \(R\) by the same constant and leaves the later budget \(\mathbb E_\nu R-\inf R\) unchanged. Adding a constant to \(S\) only changes the normalization absorbed in \(N\).

The T1 check differentiates arbitrary functions \(S,V,f\) in two flat coordinates and obtains zero defect. The covariant formula above follows from the Riemannian product rule. A formal equality on a core must still be extended to the chosen self-adjoint operators or their closed quadratic forms.

## GST-2: weighted energy and the needed domain statement

For real \(f\), the pointwise divergence identity is

\[
\psi^2fA_Sf
=c\psi^2|\nabla f|^2
-c\operatorname{div}_g(\psi^2f\nabla f).
\]

Consequently, with compact support or controlled boundary terms,

\[
q_H[Uf]
=c\int_M|\nabla f|^2\,d\nu
 +\int_M R f^2\,d\nu.
\tag{GST-2}
\]

For complex \(f\), use the sesquilinear form and take real parts. Write \(q_A[f]=c\int|\nabla f|^2d\nu\). The necessary extension statement is that the selected core is dense in the relevant form norm, and, when applying the integrated Bochner expression to \(A_Sf\), in a sufficient operator/graph norm. Mere density in \(L^2\) does not control derivatives or unbounded-operator energies. Boundary conditions and completeness/cutoff estimates must justify each integration by parts.

## GST-3: curvature normalization and a spectral argument without a discrete excited state

The weighted Bochner formula is

\[
\frac12L_S|\nabla f|^2-\langle\nabla f,\nabla L_Sf\rangle
=|\nabla^2f|^2+
 \left(\operatorname{Ric}_g+\frac2\hbar\nabla^2S\right)(\nabla f,\nabla f).
\]

Thus the relevant tensor is

\[
\operatorname{Ric}_\nu=\operatorname{Ric}_g+\frac2\hbar\nabla^2S.
\tag{GST-3}
\]

Assume \(\operatorname{Ric}_\nu\geq\kappa g\) globally, \(\kappa>0\), and that integration and domain extension are valid. Integration yields

\[
\|A_Sf\|_{L^2(\nu)}^2
\geq c^2\kappa\int|\nabla f|^2d\nu
=c\kappa\,\langle f,A_Sf\rangle.
\tag{GST-3a}
\]

To turn this into a gap, assume \(A_S\) is self-adjoint, nonnegative, and \(\ker A_S=\operatorname{span}\{1\}\), with (GST-3a) valid on its operator domain. Spectral calculus then excludes spectral mass in \((0,c\kappa)\): a nonzero vector in a spectral projection onto a compact subinterval of that interval would have
\(\int\lambda(\lambda-c\kappa)\,d\mu_f(\lambda)<0\), contradicting (GST-3a). A countable union of such intervals exhausts \((0,c\kappa)\). Therefore

\[
\operatorname{spec}(A_S)\subset\{0\}\cup[c\kappa,\infty),
\quad q_A[f]\geq c\kappa\,\operatorname{Var}_\nu(f).
\tag{GST-3b}
\]

This argument also treats continuous excited spectrum. It does not divide by a conjectured positive gap or infer a uniform gradient bound merely because each member of an approximating sequence is nonconstant. Its substantial premise is the valid closed-operator inequality (GST-3a), including domain control.

MMM uses \(\kappa=\ell_0^{-2}\) and obtains \(\hbar^2/(2m\ell_0^2)\). Mondal's kinetic metric convention has \(c=\hbar^2/2\), giving \(\hbar^2\Delta/2\). The curvature floor itself must always be measured in the same metric as the kinetic operator.

## GST-4: the finite matrix identity and its exact hypotheses

For a real symmetric matrix \(H\), a strictly positive vector \(\psi\), and \(R_i\psi_i=\sum_jH_{ij}\psi_j\), expand the square to obtain

\[
\boxed{
\sum_{ij}H_{ij}(\psi_if_i)(\psi_jf_j)
=\frac12\sum_{ij}(-H_{ij})\psi_i\psi_j(f_i-f_j)^2
 +\sum_iR_i\psi_i^2f_i^2.}
\tag{GST-4}
\]

The \(f_i^2\) terms reduce by the row equation; the \(f_j^2\) terms reduce by symmetry. If \(H_{ij}\leq0\) for \(i\ne j\), the first term is a nonnegative weighted edge energy. Connected positive-conductance support gives constants as its only zero modes. The T1 check expands a generic symmetric \(3\times3\) matrix without an eigenvector assumption; the finite-sum Lean counterpart can state the identity for every finite index set.

For \(x\perp\psi\), division \(f_i=x_i/\psi_i\) gives \(\sum_i\psi_i^2f_i=0\). A weighted Poincare inequality for this exact edge energy therefore transfers to the physical orthogonal complement when \(R\) is constant, or into the residual comparison below. The off-diagonal sign is basis dependent and must be verified for the chosen Hamiltonian representation.

## GST-5: oscillator calibration

Take Euclidean \(\mathbb R^n\),

\[
S=\frac m2\sum_j\omega_jx_j^2,\qquad
V=\frac m2\sum_j\omega_j^2x_j^2,\quad \omega_j>0.
\]

Then \(R=\frac\hbar2\sum_j\omega_j\) is constant,
\(\operatorname{Ric}_\nu=\operatorname{diag}(2m\omega_j/\hbar)\), and

\[
c\kappa=\frac{\hbar^2}{2m}\frac{2m\omega_{\min}}\hbar
=\hbar\omega_{\min}.
\tag{GST-5}
\]

The transformed eigenfunction \(f=x_j\) with \(\omega_j=\omega_{\min}\) attains this value. The explicit three-axis check verifies the residual, curvature, and excitation equation independently. This calibrates the physical-energy factor and the Hessian coefficient \(2/\hbar\).

## GST-6: the residual-mean certificate

Here is a sufficient form of the analytic bridge with no assumed exact trial eigenstate.

1. \(A_S\) is a nonnegative self-adjoint operator on \(L^2(\nu)\), \(\nu\) is a probability measure, and its simple normalized ground vector is \(1\). Its first excited variational level is at least \(\gamma>0\), for example \(\gamma=c\kappa\) by GST-3.
2. \(R\) is real, \(R\geq r_{\min}\) almost everywhere, and \(\bar R=\int R\,d\nu<\infty\).
3. The closed semibounded form corresponding to \(U^{-1}HU\) is \(q_A+\int R|f|^2d\nu\); its domain is contained in that of \(q_A\), and \(1\) belongs to it. The spectrum has a ground level and a first excited variational level to which min-max applies. Compact resolvent is a sufficient finite-regulator hypothesis.

For every admissible \(f\),
\(q_H[Uf]\geq q_A[f]+r_{\min}\|f\|^2\). Min-max gives
\(E_1(H)\geq\gamma+r_{\min}\). The normalized trial vector \(U1=\psi\) gives
\(E_0(H)\leq q_H[\psi]=\bar R\). Subtracting,

\[
\boxed{E_1(H)-E_0(H)\geq\gamma-(\bar R-r_{\min}).}
\tag{GST-6}
\]

Hence a positive certificate needs the explicit budget \(\bar R-r_{\min}<\gamma\). If \(r_{\min}\leq R\leq r_{\max}\), the weaker bound \(\gamma-(r_{\max}-r_{\min})\) follows. The mean bound remains usable when \(r_{\max}=+\infty\).

This comparison uses excited variational levels of \(A_S\) and \(H\); it does not assume that the trial vector is orthogonal to the true excited states. Ground-state simplicity of the physical realization and the meaning of its first excited level must be established in the intended setting. On a smooth connected finite-dimensional Schrödinger problem, positivity of the heat semigroup is one route; this document does not assume an analogous Yang–Mills statement without proof.

The algebraic T1 check parameterizes the two min-max bounds by nonnegative slacks and verifies that the gap exceeds the certificate by their sum. It verifies the implication's arithmetic, not min-max or the analytic premises. The exact finite matrix identity supplies a separate, directly checkable regulated setting.

## GST-7: a complete algebraic certificate for the pure quartic oscillator

Consider the usual Friedrichs realization on \(L^2(\mathbb R)\),

\[
H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+\lambda x^4,
\qquad \hbar,m,\lambda>0.
\]

Its confining potential supplies a semibounded operator with compact resolvent; the positive Gaussian trial is in the form domain. Choose \(S=m\Omega x^2/2\), \(\Omega>0\). The associated Gaussian weighted operator has gap \(\gamma=\hbar\Omega\). Direct calculation yields

\[
R(x)=\frac{\hbar\Omega}{2}-\frac{m\Omega^2x^2}{2}+\lambda x^4,
\quad
r_{\min}=\frac{\hbar\Omega}{2}-\frac{m^2\Omega^4}{16\lambda},
\]

\[
R-r_{\min}=\lambda\left(x^2-\frac{m\Omega^2}{4\lambda}\right)^2.
\]

The normalized trial measure is proportional to \(e^{-m\Omega x^2/\hbar}dx\). Integrating derivatives of \(x\rho\) and \(x^3\rho\) gives its exact moments
\(\mathbb E x^2=\hbar/(2m\Omega)\) and
\(\mathbb E x^4=3\hbar^2/(4m^2\Omega^2)\). Thus

\[
\bar R=\frac{\hbar\Omega}{4}
 +\frac{3\lambda\hbar^2}{4m^2\Omega^2},
\qquad
B(\Omega):=\gamma+r_{\min}-\bar R
=\frac{5\hbar\Omega}{4}
 -\frac{3\lambda\hbar^2}{4m^2\Omega^2}
 -\frac{m^2\Omega^4}{16\lambda}.
\]

Set \(\Omega_*^3=6\lambda\hbar/m^2\). Then

\[
r_{\min}=\frac{\hbar\Omega_*}{8},\qquad
\bar R=\frac{3\hbar\Omega_*}{8},\qquad
\boxed{\operatorname{gap}(H)\geq\frac{3\hbar\Omega_*}{4}
=\frac34\left(\frac{6\lambda\hbar^4}{m^2}\right)^{1/3}.}
\tag{GST-7}
\]

This is the best value furnished by this particular Gaussian residual-floor family. For \(q=\Omega/\Omega_*>0\), the exact factorization

\[
\frac{B(\Omega_*)-B(\Omega)}{\hbar\Omega_*}
=\frac{(q-1)^2(3q^4+6q^3+9q^2+2q+1)}{8q^2}\geq0
\]

proves optimality and uniqueness within the family. It does not identify the true quartic gap. The checks independently verify the completed square, Gaussian recurrence integrands, moments, gap arithmetic, and optimization factorization. The Schrödinger-domain and spectral facts used to apply them are stated analytic inputs; the new checks' T1 scope is the exact algebra.

## GST-8: falsifiers and the Yang–Mills boundary

Two exact checks prevent overusing the bridge.

First, let \(\psi=(1,2)\),

\[
H_0=\begin{pmatrix}2&-1\\-1&1/2\end{pmatrix},\qquad
R=\operatorname{diag}(-3/4,3/4),\qquad H=H_0+R.
\]

Here \(H_0\psi=0\), its gap is \(5/2\), and the gap of \(H\) is \(2\). Dropping the nonconstant residual would falsely give \(\operatorname{gap}(H)\geq5/2\). The valid certificate uses \(\bar R=9/20\), \(r_{\min}=-3/4\) and yields \(13/10\leq2\).

Second, for \(V=\lambda x^4\) and a seemingly more detailed trial logarithm
\(S=\alpha x^2/2+\beta x^4/4\), \(\alpha,\beta>0\), the curvature is globally positive but the exact residual has leading term

\[
R(x)=-\frac{\beta^2}{2m}x^6+O(x^4)\longrightarrow-\infty.
\]

The required residual floor fails for this trial family. A local or perturbative improvement of \(S\) can therefore worsen the global certificate. GST-7 supplies a Gaussian trial that succeeds for the same physical potential. Failure of a trial certificate does not imply a vanishing physical gap.

## GST-9: an exact volume-accumulation falsifier

The residual-mean comparison can lose volume uniformity even for independent systems whose gap is uniform. Take \(n\) independent identical copies of GST-7 and the product of its optimized Gaussian trials. Residuals add, while the Gaussian weighted gap tensorizes by taking the minimum of the one-body gaps. Consequently

\[
\gamma_n=\hbar\Omega_*,\qquad
r_{\min,n}=\frac{n\hbar\Omega_*}{8},\qquad
\bar R_n=\frac{3n\hbar\Omega_*}{8},
\]

and a single application of GST-6 to the entire system yields only

\[
B_n=\left(1-\frac n4\right)\hbar\Omega_*.
\tag{GST-9}
\]

This global certificate is zero at four copies and negative at five. Applying the valid one-body certificate first and then using the spectrum of the tensor sum instead gives
\(\operatorname{gap}(\sum_{j=1}^nH_j)\geq3\hbar\Omega_*/4\) for every \(n\). Exciting one factor realizes the first nonzero tensor-sum energy above its product ground state; adding independent factors does not lower that gap.

The extra exact check directly differentiates the two-coordinate trial to verify residual additivity, then checks the symbolic \(n\)-copy budget, its zero at \(n=4\), and the surviving positive one-body bound. The spectral tensor-product step is an explicit analytic premise, not a claim checked by the finite arithmetic. This falsifier identifies a real weakness of the global residual bound: the ground-level trial error accumulates across factors while the spectral gap is an intensive quantity. A successful Yang–Mills route must control local residuals, tensorization or a suitable interaction comparison, rather than assume that a useful one-site estimate stays uniform when summed over volume.

For a Yang–Mills regulator family indexed by lattice spacing, volume, and any additional cutoff, one sufficient target remains

\[
\inf_{a,L,\chi}\left[
c_{a,L,\chi}\kappa_{a,L,\chi}
-\left(\bar R_{a,L,\chi}-r_{\min,a,L,\chi}\right)\right]>0
\]

in the intended physical-energy units, together with an operator/measure convergence theorem preserving the vacuum and gap. A local SAFE ball cannot supply the displayed global quantities without a proven extension or localization argument. A finite-dimensional identity alone cannot pass either the volume limit or continuum limit.

The outstanding inputs are a physical gauge-invariant Hamiltonian realization, compatible domains through quotient singularities and boundaries, a positive normalizable trial functional, controlled global residual mean and floor, weighted curvature with the same kinetic metric, and uniform regulator removal. If the starting object is an OS reconstruction, the conjugacy must be established for its reconstructed Hamiltonian. Reusing a Langevin generator's spectral number without that identification remains the G23 time-splice problem.

## Verification records and dependencies

The suite is `Yang-Mills ground-state transform and residual certificates (G20, G23)`, exposed as `ym_ground_state`. It has eleven exact Python checks, with complete Lean mappings for the finite residual identity, scalar residual budget and normalized frequency optimization. The registered `rests_on` relations are:

- GST-2 weighted energy rests on GST-1 conjugation.
- GST-5 oscillator calibration rests on conjugation and the flat Bochner identity.
- GST-7 quartic certificate rests on conjugation, oscillator calibration, and the residual-budget implication; its optimization rests on the quartic certificate.
- The finite-gap falsifier rests on the matrix residual identity; the trial-tail falsifier rests on conjugation.
- The tensor-product accumulation falsifier rests on the quartic certificate.

Source citations locate the conventions; they are not machine-checked dependencies that promote a whole source theorem. The Python check names are stable constants in the module for Lean/graph mapping. The compiled finite-sum Lean identities strengthen the finite matrix and scalar implication portions. They do not formalize the manifold Bochner theorem, min-max domain extension, Gaussian integration, or the continuum Yang–Mills construction. See [the formal bridge note](yangmills-formal-bridges.md).
