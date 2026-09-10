# W6: a residual certificate and the remaining coupled Wilson estimate

9 September 2026 UTC. Standalone continuation of the 8 September W6 record.
The original working checkout and its generated graph are unchanged by this note.

**Result:** an exact variational identity reduces W6 to a selected Gaussian
diagonal estimate and a residual estimate against an independently established
lower fast form. This is a conditional analytic theorem, not a proof of W6 for
the coupled Wilson lattice. The exact stopping point is the uniform connected
residual estimate and its interacting coercivity, in the actual vacuum/source
identification. The Gaussian synthesis theorem alone supplies neither.

## 1. Precise form statement

Suppress the volume, background and spectral parameter. Set

\[
 A_0=F_0-z>0,\quad A_g=F_g-z>0,\quad
 t=t_1p,\quad u=A_0^{-1}t,\quad d=A_g-A_0.
\]

These are the actual vacuum-subtracted fast restrictions in one compatible
physical source chart. The force is the full graph force
\(t_1=QW_1J_z\), including the electric metric, Haar, source motion and reference
graph dressing. The magnetic cubic by itself is insufficient.

Assume \(u\) is in both form domains. Define the residual as the interacting
form functional

\[
 \rho_p(v)=a_g[v,u]-\langle v,t\rangle.
\]

It equals \(d[v,u]\) only where that subtraction is defined. Assume this
functional is continuous in the interacting energy norm and the indicated
weak inverse realizations exist. If \(\rho_p\) is a Hilbert vector, it is
\(A_gu-t\). No global equality of compact and Gaussian form domains is assumed.

The exact identity is

\[
 \boxed{\langle t,(A_g^{-1}-A_0^{-1})t\rangle
       =-d[u,u]+\|\rho_p\|_{a_g^*}^{\,2}.}                 \tag{R1}
\]

Here \(\|\rho\|_{a_g^*}^2=\langle\rho,A_g^{-1}\rho\rangle\), interpreted
by Riesz representation on the form domain.

Proof: \(w=A_g^{-1}t\) satisfies \(A_g(u-w)=\rho_p\) weakly. Completing
the variational square for the functional
\(2\operatorname{Re}\langle t,v\rangle-a_g[v]\) at \(v=u\) gives
\[
 \langle t,A_g^{-1}t\rangle
 =2\operatorname{Re}\langle t,u\rangle-a_g[u]
   +a_g[u-w].
\]
Since \(a_0[u]=\langle t,A_0^{-1}t\rangle\), (R1) follows. Polarization
gives the selected operator identity whenever the forms extend boundedly in
the retained weight. The two terms on the right must remain together unless
each is bounded independently; their cancellation may matter.

For the literal mixed pairing in W6, either require \(w\) to lie in the
common form domain or use the compatible weak extension
\(d[u,w]=\overline{\rho_p(w)}\). The latter agrees with the original
form difference on the common core and gives the signed resolvent identity.
The selected inverse identity (R1) itself does not require \(w\in D(a_0)\).

## 2. A sufficient estimate without the interacting inverse vector

Let \(\ell\) be an independently controlled closed positive fast form, with
operator \(L\). Require \(D(a_g)\subseteq D(\ell)\) and

\[
 a_g[v]\ge\kappa\ell[v],\qquad \kappa>0,                 \tag{R2}
\]

uniformly in the volumes, backgrounds and spectral interval required by W6.
If the residual extends continuously in the \(\ell\)-energy norm, then
\(\|\rho_p\|_{a_g^*}^2\le\kappa^{-1}\|\rho_p\|_{\ell^*}^2\).
Consequently the two explicit estimates

\[
 |d[u,u]|\le a|g|\,b[p],\qquad
 \|\rho_p\|_{\ell^*}\le c|g|\,b[p]^{1/2}                 \tag{R3}
\]

imply

\[
 |\langle t,(A_g^{-1}-A_0^{-1})t\rangle|
 \le(a+\kappa^{-1}c^2g_0)|g|\,b[p],\quad |g|\le g_0.   \tag{R4}
\]

Thus (R2)-(R3) imply W6. Even the weaker residual estimate
\(\|\rho_p\|_{\ell^*}\le c\sqrt{|g|}\,b[p]^{1/2}\) suffices, with
constant \(a+c^2/\kappa\). A known floor \(A_g\ge fI\) permits \(L=I\),
\(\kappa=f\), but the resulting global Hilbert residual may grow with volume.

This route requires a lower bound only. The already refuted global upper
comparison \(F_g\le(1+O(g))F_0\) is not an assumption. Taking
\(L=A_g\) without an independent estimate would merely rename the difficulty.
All constants in (R2)-(R6), including the coupling threshold, must be
independent of volume, the required retained-background range and spectral
interval, and of the coupling within that range.

## 3. Where a volume-independent residual estimate could come from

An explicit sufficient mechanism for (R3) is a local energy factorization
\[
 \rho_p(v)=g\langle K_gYv,Xp\rangle_{\oplus_x\mathcal E_x},\qquad
 \|Xp\|^2\le C_B b[p],\quad \|Yv\|^2\le C_L\ell[v].    \tag{R5}
\]
If the operator blocks obey
\[
 \sup_x\sum_y\|K_{g,xy}\|\le k_r,\qquad
 \sup_y\sum_x\|K_{g,xy}\|\le k_c,                    \tag{R6}
\]
the block Schur test gives
\(\|K_g\|\le\sqrt{k_rk_c}\), hence (R3) with
\(c=\sqrt{C_BC_Lk_rk_c}\). This proof has no factor equal to the volume.
The spaces, derivatives and centering must come from the full Wilson
residual, not an arbitrary replacement force.

The concrete research target is to construct this factorization after the
actual quantum vacuum and source transport, with local conditional centering,
and prove summability of its connected kernels. The existing additive-copy
theorem proves a product version using exact support orthogonality. It does
not prove (R5)-(R6) for plaquettes that couple blocks. Global reference-number
moments fail the recorded spectator test. A global small conditional Fisher
bound also fails the recorded central SU(2) coarse-holonomy test. Therefore
energy/derivative localization and control of the remaining retained energies
must be built into a coupled proof.

The diagonal estimate in (R3) is another explicit obligation. The existing
Gaussian cubic synthesis estimate bounds a quadratic inverse energy, not
automatically \(d[u,u]\) for the complete dressed force.

## 4. A sharp logical check: a fast floor and Gaussian diagonal control do not suffice

For integer \(M\ge1\), let
\[
 A_0=I_2,\quad t=e_1,\quad
 A_{g,M}=\begin{pmatrix}1&c_{g,M}\\c_{g,M}&1\end{pmatrix},\qquad
 c_{g,M}=\frac{Mg^2}{2(1+Mg^2)}.
\]
For every volume label \(M\), this family is analytic near zero, agrees with
the reference at zero, and has a uniform fast floor \(A_{g,M}\ge I/2\).
The Gaussian inverse energy is one and \(d[u,u]=0\). Nevertheless
\[
 \langle t,(A_{g,M}^{-1}-I)t\rangle
 =\frac{c_{g,M}^2}{1-c_{g,M}^2}.
\]
Along \(g=1/n\), \(M=n^2\), this is exactly \(1/15\), so its ratio to
\(g\) is \(n/15\), unbounded. This is an abstract counterexample to the
proposed implication, not a counterexample to the Wilson model or W6 itself.
It isolates why a uniform residual/connected estimate is real new input,
even if the interacting fast floor were already known.

## 5. The precise stopping point and the continuum requirement

An additional exclusion narrows the choice of lower reference: the
[independent radial derivation](agent_route.md#3-even-a-near-unit-global-lower-gaussian-comparison-fails-on-the-su2-cell)
proves that even \(F_g\ge(1-Cg)UF_0U^*\) fails on the four-link SU(2) cell
when the retained rank is fixed or \(o(g^{-2})\). Exact radial conjugacy and
elementary interval bracketing give
\[
 g^2N_{H_g-e_g}(8/g^2)\longrightarrow 8/\pi>2,
\]
whereas the Gaussian radial oscillator count tends to 2. Finite-codimension
interlacing preserves those limits in the stated retention regime. A lower
comparison tending to one would reverse this counting inequality. This is
an analytic exclusion, not just a finite numerical observation. It leaves
open a fixed smaller coercivity fraction or a different compact lower
reference as in (R2); it makes no claim about infinite-rank retained algebras.

I cannot derive (R2)-(R3), or (R5)-(R6), for the actual coupled Wilson family
from the available Gaussian, fixed-cell and additive-copy proofs. In
particular, no proof supplied here controls the centered full graph residual
in an independently controlled fast dual norm uniformly in volume and in the
required retained background and energy range. W6 remains open for this
family. This is a specific missing analytic estimate, not a limitation imposed
by what has previously been published.

Even proving W6 completes only one input of W5. The actual fast floor, direct
and source Taylor remainders, complete second-order coarse matching, physical
clock, induced metric, compatible source maps and high retained energies also
need their stated bounds. The accumulated gap inequalities alone do not
construct correlation limits.

A precise sufficient target for the observable limits is as follows. For
each fixed renormalized, gauge-invariant Euclidean history \(O\), let
\(C_{j,\Lambda}(O)\) be its expectation at spacing \(a_j\). Supply actual
compatible observable identifications and an exhausting physical volume
sequence \(\Lambda_N\). It suffices to prove
\[
 \sup_{\Lambda\supseteq\Lambda_{N_0}}
 |C_{j+1,\Lambda}(O)-C_{j,\Lambda}(O)|\le\epsilon_j(O),
 \quad\sum_j\epsilon_j(O)<\infty,                       \tag{R7}
\]
and
\[
 \sup_j\sup_{M\ge N}
 |C_{j,\Lambda_M}(O)-C_{j,\Lambda_N}(O)|\le\eta_N(O),
 \quad\eta_N(O)\longrightarrow0.                        \tag{R8}
\]
The triangle inequality then bounds any two sufficiently fine, sufficiently
large approximations by a scale-error tail plus \(\eta_N(O)\), establishing a
joint Cauchy limit along that exhaustion. Uniformity over the intended boundary
conditions/exhaustions is needed if their independence is claimed. These are
conditional criteria, not estimates proved by W6.

The resulting correlation system must additionally have the required
regularity, symmetries, positivity, nontriviality and physical mass gap.
Pages 11-12 of the supplied Jaffe-Witten document require observable limits
and explicitly qualify the sufficiency of compactness. This note supplies
neither an unconditional continuum construction nor a proof of impossibility.

## 6. Verification and source record

Run the adjacent checker with the project Python and `SYMPY_GROUND_TYPES=python`:

```powershell
$env:SYMPY_GROUND_TYPES='python'
& 'C:\WORKHOUSE\ALL THEORY\WORKHOUSE\.venv\Scripts\python.exe' 'C:\WORKHOUSE\research\w6_continuation_20260909\verify_w6.py'
```

`verification.json` records exact finite controls and SHA-256 hashes of the
current W6/Schur derivations and the supplied PDF. The general form-domain,
all-volume and limiting quantifiers are analytic arguments or explicit open
hypotheses, not certified by these finite controls. No new Lean proof is claimed.
The live `workhouse why G19` command could not load the existing pyflint DLL
under this sandbox; the checked-in graph and current derivations were inspected
directly. This continuation does not claim a full repository verification run.

Primary local sources:

- `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-selected-inverse-wall.md`, W4-W6.
- `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-schur-excess.md`, SP10, SP16, SP21-SP25.
- `C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md`.
- `C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md`.
- `C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md`.
- Jaffe and Witten, *Quantum Yang-Mills Theory*, supplied PDF SHA-256 `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`; [official copy](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), pages 11-12.
