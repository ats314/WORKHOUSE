# Finite-\(N\) SU(3) truncation bridge and changed-capability result

**Date:** 2026-08-28  
**Status:** exact through second order in the charge-odd one-plaquette sector  
**Main result:** the channel-complete finite-\(N\) Schur complement turns the published finite-SU(3) truncation into an exact three-dimensional spectral calculation that its simulated \(T_1\) cutoff cannot reproduce.

## 1. Verdict

The requested connection exists, and it produces a concrete new capability.

The exact finite-rank plaquette matrix element published by Ciavarella, Burbano, and Bauer implies the four shared-link channel weights needed by the WORKHOUSE operator. After charge-odd projection, their second-order Schur complement is

\[
H_{\mathrm{eff},-}^{(2)}
=E_{\mathrm{flat}}^{(2)}I+t_NBB^\dagger,
\qquad
t_N=
\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)}.
\]

For SU(3),

\[
\boxed{t_3=\frac5{612}}.
\]

The capability change is not merely that this number agrees with a published matrix element. It is that the published three-dimensional one-cube calculation uses the \(T_1=\{1,3,\bar3\}\) truncation, which omits the \(8\) and \(6\) intermediate channels. In the charge-odd one-plaquette sector that cutoff predicts

\[
t_3^{T_1}=-\frac1{12},
\]

whereas exact elimination of the omitted channels gives

\[
t_3^{T_1}+\underbrace{\left(w_6-w_8\right)}_{14/153}
=-\frac1{12}+\frac{14}{153}
=\frac5{612}.
\]

Thus the omitted finite-\(N\) channels reverse the kinetic sign. On one open cube the \(T_1\) and channel-complete theories predict opposite orderings of the same \(1+3+2\) charge-odd multiplets.

This establishes a **new exact reduced-sector benchmark and a real scaling improvement**: a complete \(O(u^2)\), three-dimensional, finite-volume spectrum can be obtained from four local channel contractions and a sparse incidence operator, without constructing the full \(d=3\), \(T_2\) plaquette transition table that the published resource analysis estimates at \(\gtrsim10^{20}\) matrix elements.

It does **not** yet establish a nonperturbative finite-coupling spectrum, a continuum glueball identification, or a full-Hamiltonian \(T_2\) cube diagonalization.

### Incidence convention

The WORKHOUSE momentum-space notation uses the face-by-edge incidence \(B_{\mathrm W}\), so its face operator is \(B_{\mathrm W}B_{\mathrm W}^\dagger\). In the real-space certificate below, \(D_2:C_2\to C_1\) is the conventional edge-by-face boundary matrix. Therefore

\[
G=D_2^\dagger D_2
=B_{\mathrm W}B_{\mathrm W}^\dagger.
\]

The symbols \(G\), \(D_2^\dagger D_2\), and the requested \(BB^\dagger\) thus denote the same face-space operator; no transpose changes the spectrum or coefficient.

## 2. Published targets and the normalization dictionary

There are two closely related published Hamiltonian conventions, and they differ by a factor of two in the magnetic term.

### 2.1 Ciavarella--Burbano--Bauer convention

Ciavarella, Burbano, and Bauer use

\[
H_{\mathrm{CBB}}
=\frac{g^2}{2}\sum_l E_l^2
-\frac1{2g^2}\sum_p(\Box_p+\Box_p^\dagger).
\]

After division by \(g^2\), this matches the canonical WORKHOUSE convention

\[
\widetilde H=\frac12\sum_lE_l^2-uV,
\qquad V=\sum_p(\Box_p+\Box_p^\dagger),
\]

with

\[
\boxed{u_{\mathrm{CBB}}=\frac1{2g^4}}.
\]

The Hamiltonian normalization and its electric-basis construction are explicit in [Ciavarella--Burbano--Bauer, arXiv:2503.11888v5](https://arxiv.org/html/2503.11888v5).

### 2.2 Balaji et al. one-cube convention

Balaji et al. use, after dropping the extensive constant and setting \(a=1\),

\[
H_{\mathrm B}
=\frac{g^2}{2}\sum_lE_l^2
-\frac1{g^2}\sum_p(\Box_p+\Box_p^\dagger).
\]

Therefore

\[
\boxed{u_{\mathrm B}=\frac1{g^4}}.
\]

This is the convention relevant to their exact-diagonalization benchmark on the six-face open cube. Their Eq. (1) and their statement that the cube calculation uses \(T_1=B=4\) are in [Balaji et al., arXiv:2509.25865v3](https://arxiv.org/html/2509.25865v3).

The coefficient \(t_3\) is the same dimensionless canonical coefficient in both conventions. Only its conversion to powers of the published coupling differs:

| publication | canonical \(u\) | physical relative shift from incidence eigenvalue \(q\) |
|---|---:|---:|
| CBB | \(1/(2g^4)\) | \(q t_3/(4g^6)\) |
| Balaji et al. | \(1/g^4\) | \(q t_3/g^6\) |

This distinction is essential; combining the two conventions without the factor-of-two dictionary gives a fourfold error in the \(g^{-6}\) spectral coefficient.

## 3. Exact basis embedding

Let

\[
|p,F\rangle=\Box_p|0\rangle,
\qquad
|p,\bar F\rangle=\Box_p^\dagger|0\rangle.
\]

The charge eigenstates are

\[
|p,\pm\rangle
=\frac{|p,F\rangle\pm|p,\bar F\rangle}{\sqrt2}.
\]

These are exactly the symmetric and antisymmetric combinations of the qutrit plaquette states \(|\circlearrowleft\rangle\) and \(|\circlearrowright\rangle\) in the published large-\(N_c\) construction. The earlier leading-large-\(N_c\) Hamiltonian explicitly makes the antisymmetric state decouple; see [Ciavarella--Bauer, arXiv:2402.10265v3, Eqs. (7)--(9)](https://arxiv.org/html/2402.10265v3). Consequently its charge-odd hopping is identically zero:

\[
t_3^{\mathrm{leading}\;N_c}=0.
\]

The finite-\(N\) bridge begins when two adjacent plaquettes share one link. The two orientation families are

\[
F\otimes\bar F=\mathbf1\oplus\mathbf8,
\qquad
F\otimes F=\bar{\mathbf3}\oplus\mathbf6.
\]

All four are required before projecting to charge odd.

## 4. Derivation from the published finite-rank matrix element

The exact plaquette matrix element in Appendix D, Eq. (265), of Ciavarella--Burbano--Bauer is

\[
|M_\rho|
=\sqrt{\frac{\dim\rho}{\dim A\,\dim R}}.
\]

For two fundamental factors, \(A=R=F\) and \(\dim F=N\), hence

\[
\boxed{|M_\rho|^2=\frac{d_\rho}{N^2}}.
\]

This is independently visible in their channel amplitudes

\[
\frac1N,
\quad
\sqrt{1-\frac1{N^2}},
\quad
\sqrt{\frac12\left(1-\frac1N\right)},
\quad
\sqrt{\frac12\left(1+\frac1N\right)}.
\]

The external one-plaquette state has electric energy \(2C_F\). An adjacent two-plaquette intermediate has six unshared fundamental links and one fused shared link, so

\[
E_\rho=3C_F+\frac{C_\rho}{2},
\qquad
\Delta_\rho=E_\rho-2C_F=C_F+\frac{C_\rho}{2}.
\]

The second-order resolvent weight is therefore

\[
\boxed{
w_\rho=-\frac{d_\rho/N^2}{C_F+C_\rho/2}.}
\]

Summing within the mixed- and like-orientation families gives

\[
A_N=w_{\mathbf1}+w_{\mathrm{Adj}}
=-\frac{2N^3}{(N^2-1)(2N^2-1)},
\]

\[
B_N=w_{\Lambda^2F}+w_{\mathrm{Sym}^2F}
=-\frac{4N(N^2-2)}{(N^2-1)(4N^2-9)}.
\]

Charge-odd projection subtracts the orientation families. If \(B\) is the signed edge-by-face boundary matrix, the signed face adjacency is

\[
S=B^\dagger B-4I.
\]

The local scalar and the \(-4I\) term can be combined, leaving

\[
K_-^{(2)}=E_{\mathrm{flat}}^{(2)}I+(B_N-A_N)B^\dagger B.
\]

Thus

\[
t_N=B_N-A_N
=\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)}.
\]

The result is an exact, sector-specific Schur complement of published finite-rank matrix elements. It is not an empirical fit.

## 5. SU(3) channel ledger and the truncation failure

For \(N=3\), \(C_F=4/3\). Substituting the published dimensions and Casimirs gives:

| fusion | \(\rho\) | \(d_\rho/9\) | \(C_F+C_\rho/2\) | \(w_\rho\) |
|---|---:|---:|---:|---:|
| \(F\otimes\bar F\) | \(\mathbf1\) | \(1/9\) | \(4/3\) | \(-1/12\) |
| \(F\otimes\bar F\) | \(\mathbf8\) | \(8/9\) | \(17/6\) | \(-16/51\) |
| \(F\otimes F\) | \(\bar{\mathbf3}\) | \(1/3\) | \(2\) | \(-1/6\) |
| \(F\otimes F\) | \(\mathbf6\) | \(2/3\) | \(3\) | \(-2/9\) |

Therefore

\[
A_3=-\frac1{12}-\frac{16}{51}=-\frac{27}{68},
\]

\[
B_3=-\frac16-\frac29=-\frac7{18},
\]

and

\[
\boxed{t_3=B_3-A_3=\frac5{612}}.
\]

Balaji et al. define \(T_1\) to retain only \(\{1,3,\bar3\}\), while \(T_2\) includes the two-index tensors. Their one-cube exact diagonalization is explicitly \(T_1=B=4\). At second order, \(T_1\) retains the singlet and \(\bar3\) shared-link routes but removes the \(8\) and \(6\) routes. Hence

\[
t_3^{T_1}=w_{\bar3}-w_1
=-\frac16+\frac1{12}
=-\frac1{12}.
\]

The exact missing-channel completion is

\[
\Delta t_3=w_6-w_8
=-\frac29+\frac{16}{51}
=\frac{14}{153},
\]

so

\[
-\frac1{12}+\frac{14}{153}=\frac5{612}.
\]

This cancellation is the important physics and the useful diagnostic. The higher channels are not a small correction to \(T_1\); they change the sign and reduce the magnitude by about an order of magnitude.

### 5.1 The correct counterterm for the published \(T_1\) Hamiltonian

The published \(T_1\) Hamiltonian already contains the \(\mathbf1\) and \(\bar{\mathbf3}\) routes. Therefore one must **not** append the full \((5/612)u^2G\) term to that Hamiltonian; doing so would double count those channels. The exact missing shape counterterm is only

\[
\boxed{
\Delta H_{\mathrm{shape},T_1}^{(2)}
=\left(w_6-w_8\right)u^2G
=\frac{14}{153}u^2G.}
\]

On the open cube, the complete scalar counterterm can also be written explicitly. In the vacuum-subtracted charge-odd gap, the \(T_1\) within-plaquette coefficient is \(3/4\): the vacuum contributes \(-3/4\), while the projected one-dimensional odd plaquette state has no second-order self route. The full theory adds the omitted local sextet route \(-1/4\), reducing this to \(1/2\). For each adjacent face,

\[
\mathrm{leak}_{T_1}=w_1+w_{\bar3}+\frac34=\frac12,
\qquad
\mathrm{leak}_{\mathrm{full}}=w_1+w_8+w_{\bar3}+w_6+\frac34=-\frac{11}{306}.
\]

With four adjacent faces and \(S=G-4I\),

\[
H_{2,T_1}=\frac{37}{12}I-\frac1{12}G,
\qquad
H_{2,\mathrm{full}}=\frac{11}{34}I+\frac5{612}G.
\]

Consequently the exact open-cube counterterm to add to the published \(T_1\) one-plaquette charge-odd block is

\[
\boxed{
\Delta H_{2,T_1\rightarrow\mathrm{full}}
=-\frac{563}{204}I+\frac{14}{153}G.}
\]

Only the second term affects relative shell ordering; the first is needed if absolute second-order gap coefficients are compared.

## 6. Exact one-cube spectrum

Take the six oriented faces of one open cube in the order

\[
(xy)_0,(xy)_1,(xz)_0,(xz)_1,(yz)_0,(yz)_1.
\]

Direct construction of the integer edge-by-face boundary gives

\[
G:=B^\dagger B=
\begin{pmatrix}
4&0&1&-1&-1&1\\
0&4&-1&1&1&-1\\
1&-1&4&0&1&-1\\
-1&1&0&4&-1&1\\
-1&1&1&-1&4&0\\
1&-1&-1&1&0&4
\end{pmatrix}.
\]

Exact rational elimination yields

\[
\det(xI-G)=x(x-4)^3(x-6)^2,
\]

and therefore

\[
\boxed{\operatorname{spec}G=\{0^{(1)},4^{(3)},6^{(2)}\}.}
\]

The kernel vector is the signed boundary of the cube. It is the local closed-surface carrier; its zero eigenvalue follows from boundary-of-boundary zero.

### 6.1 Channel-complete prediction

After subtracting the common scalar, the exact spectrum through \(O(u^2)\) is

\[
\boxed{
u^2\left\{
0^{(1)},
\left(\frac5{153}\right)^{(3)},
\left(\frac5{102}\right)^{(2)}
\right\}.}
\]

The ordering is singlet, then triplet, then doublet.

In the Balaji coupling convention this becomes the physical strong-coupling gap prediction

\[
\boxed{
\lim_{g\to\infty}g^6
\begin{pmatrix}
E_{3}-E_{1}\\[2pt]
E_{2}-E_{1}
\end{pmatrix}
=
\begin{pmatrix}
5/153\\[2pt]
5/102
\end{pmatrix}.}
\]

### 6.2 Published \(T_1\) prediction

The same incidence eigenvalues with \(t_3^{T_1}=-1/12\) give

\[
\boxed{
u^2\left\{
0^{(1)},
\left(-\frac13\right)^{(3)},
\left(-\frac12\right)^{(2)}
\right\}.}
\]

The doublet is now lowest, followed by the triplet and then the signed cube boundary. Any common scalar cancels in this ordering test. Therefore the published \(T_1\) cube and the channel-complete finite-\(N\) theory make opposite, directly falsifiable predictions for the charge-odd shell.

### 6.3 Optional common scalar for the untruncated open cube

The periodic scalar cannot simply be copied to an open cube. Each cube face has four adjacent faces rather than twelve. With the exact within-plaquette term \(1/2\) and per-neighbor second-order leakage

\[
\mathrm{leak}_2=-\frac{11}{306},
\]

the open-face diagonal is

\[
d_{\mathrm{open}}=\frac12+4\,\mathrm{leak}_2=\frac{109}{306}.
\]

Since \(S=G-4I\),

\[
H_{2,\mathrm{open}}
=d_{\mathrm{open}}I+t_3S
=\frac{11}{34}I+\frac5{612}G.
\]

The full channel-complete open-cube energies through this order are therefore

\[
\frac83+u+
\left\{
\left(\frac{11}{34}\right)^{(1)},
\left(\frac{109}{306}\right)^{(3)},
\left(\frac{19}{51}\right)^{(2)}
\right\}u^2+O(u^3).
\]

This scalar uses the independently established local leakage coefficient. The relative \(1+3+2\) splittings above are the cleaner published-truncation test because they do not require any boundary scalar convention.

## 7. Exact periodic \(3^3\) spectrum

For a periodic cubic lattice with \(L=3\), the retained face space has

\[
3L^3=81
\]

states. At momentum \(k\),

\[
\operatorname{spec}G(k)=\{0,q(k),q(k)\},
\qquad
q(k)=4\sum_{j=1}^3\sin^2\frac{k_j}{2}.
\]

On the \(L=3\) momentum grid, exact counting gives

\[
\boxed{
\operatorname{spec}G
=\{0^{(29)},3^{(12)},6^{(24)},9^{(16)}\}.}
\]

The 29 zero modes equal \(L^3+2\), the exact dimension of \(\ker\partial_2\) on the three-torus.

Multiplication by \(t_3=5/612\) gives the full relative second-order spectral fingerprint

\[
\boxed{
\operatorname{spec}(t_3G)
=\left\{
0^{(29)},
\left(\frac5{204}\right)^{(12)},
\left(\frac5{102}\right)^{(24)},
\left(\frac5{68}\right)^{(16)}
\right\}.}
\]

Including the periodic common scalar \(11/306\), the canonical energies are

\[
\frac83+u+
\left\{
\left(\frac{11}{306}\right)^{(29)},
\left(\frac{37}{612}\right)^{(12)},
\left(\frac{13}{153}\right)^{(24)},
\left(\frac{67}{612}\right)^{(16)}
\right\}u^2+O(u^3).
\]

This is an exact finite-volume prediction, not a thermodynamic extrapolation.

## 8. The scaling improvement

Balaji et al. estimate that a direct \(T_2\) plaquette construction in \(d=3\) requires at least \(10^{20}\) magnetic matrix elements. Even their softer \(B\) truncation reaches only selected states involving all two-index irreps at roughly \(10^8\) matrix elements. Their public \(\texttt{ymcirc}\) release presently supports circuit generation only in \(d=3/2\) and \(d=2\), and lists \(d\ge3\) and open boundary conditions as future work. These boundaries are stated in [arXiv:2509.25865v3](https://arxiv.org/html/2509.25865v3).

The reduced-sector construction instead requires:

1. four exact local channel entries \(\{1,8,\bar3,6\}\);
2. the oriented cubical boundary with four nonzero entries per face;
3. one sparse multiplication by \(B\) and one by \(B^\dagger\), or the closed momentum formula above.

For an \(L^3\) periodic lattice:

\[
n_{\mathrm{faces}}=3L^3,
\qquad
\operatorname{nnz}(B)=12L^3.
\]

Thus application of the effective operator is \(O(L^3)\) in memory and time, and the whole spectrum is obtained by evaluating \(q(k)\) on \(L^3\) momenta. The local color computation remains \(O(1)\) at fixed order.

The comparison is therefore:

| task | published direct route | exact reduced-sector route |
|---|---:|---:|
| channel-complete \(d=3\) local preprocessing | estimated \(\gtrsim10^{20}\) \(\Box\) entries for \(T_2\) | 4 exact channel weights |
| one-cube charge-odd shell | published only at \(T_1\), wrong \(O(u^2)\) kinetic sign | exact \(6\times6\) spectrum |
| periodic \(3^3\) charge-odd shell | no published \(T_2\) result | exact 81-mode spectrum |
| arbitrary periodic \(L^3\) at \(O(u^2)\) | no current \(d=3\) \(\texttt{ymcirc}\) path | closed \(q(k)\) formula, \(O(L^3)\) |

This is an end-to-end improvement for one controlled physical sector and perturbative order. It is not a replacement for a full finite-coupling simulation.

## 9. What is genuinely new, and what is published input

### Published input

- The Kogut--Susskind Hamiltonians and their two coupling normalizations.
- The electric-basis and local-Krylov truncations.
- The exact dimension-ratio plaquette matrix element.
- SU(3) dimensions and Casimirs.
- The \(T_1\), \(T_2\), and \(B\)-cut definitions.
- The \(T_1=B=4\) one-cube ground-state exact diagonalization.
- The resource estimate for a \(d=3\), \(T_2\) transition table.

### New result established here

- The charge-odd Schur complement of the published finite-rank matrix elements is exactly \(t_NB^\dagger B\).
- The SU(3) \(T_1\) truncation predicts \(-1/12\), while channel completion gives \(+5/612\).
- The omitted \(8\) and \(6\) channels reverse the one-cube band ordering.
- The exact open-cube fingerprint is \(\{0,(5/153)^3,(5/102)^2\}u^2\) after scalar subtraction.
- The exact periodic \(3^3\) fingerprint has multiplicities \(29,12,24,16\).
- At fixed order the full three-dimensional finite-volume charge-odd spectrum is reduced from a prohibitive local transition census to four color weights plus sparse topology.

I did not find these extracted charge-odd spectra or the \(T_1\)-sign reversal in the named publications. A formal novelty claim still requires normal peer review and a broader literature search; the statement proved here is that the result is absent from, and adds a capability to, the specific published truncations used for comparison.

## 10. The remaining decisive full-Hamiltonian test

The strongest next test is not another symbolic manipulation. It is a small-\(u\) diagonalization of the authors' complete one-cube Hamiltonian at successively enlarged cutoffs.

For each of \(B=4\), \(B=17/3\), and \(B=6\):

1. project to charge conjugation \(C=-\);
2. track the six eigenstates whose overlap with the one-plaquette shell tends to one as \(u\to0\);
3. resolve the \(1+3+2\) cube multiplets;
4. subtract the lowest member of the shell;
5. fit the two gaps against \(u\) at \(u, u/2, u/4\).

The acceptance limits in the Balaji normalization are

\[
\lim_{g\to\infty}g^6(\Delta E_3,\Delta E_2)
=
\begin{cases}
(-1/3,-1/2),&B=4=T_1,\\[3pt]
(5/153,5/102),&B=6\text{ with all four local channels}.
\end{cases}
\]

After subtracting these limits, the residual should scale as \(O(g^{-10})\), equivalently \(O(u^3)\) in the canonical dimensionless Hamiltonian.

The published paper provides only ground-state cube energies and fidelities, not this charge-odd excited spectrum. The public \(\texttt{ymcirc}\) package does not currently provide the required \(d=3\), open-boundary, \(B\)-cut construction. Therefore this final numerical comparison remains an explicitly identified next experiment, not a completed claim.

## 11. Reproducibility artifacts

- `verify_cbb_tn_bridge.py` reconstructs every SU(3) channel weight from dimensions and Casimirs, checks \(t_3\), checks the \(T_1\) sign reversal, constructs both cubical boundary matrices independently, and verifies all finite-volume multiplicities over the rationals.
- `su3_finite_n_bridge_certificate.json` is the machine-readable result.
- `CBB_FINITE_N_SU3_TN_BBDAGGER_BRIDGE_2026-08-28.md` contains the detailed Ciavarella--Burbano--Bauer embedding and source dictionary.

The verifier has no non-standard dependencies. A fresh run produced:

```text
PASS: 18/18 exact bridge gates
```

## 12. Final claim boundary

The strongest defensible statement is:

> The exact finite-rank SU(3) plaquette matrix elements admit a charge-odd, second-order Schur complement equal to \((5/612)u^2B^\dagger B\). This supplies a channel-complete three-dimensional finite-volume spectrum using four local fusion channels and sparse cubical incidence. On the published open cube, the standard \(T_1\) truncation omits the \(8\) and \(6\) channels and therefore predicts the opposite kinetic sign and reversed charge-odd shell ordering. The construction bypasses the full \(d=3\), \(T_2\) transition census at this order, but it is not yet a full finite-coupling or continuum calculation.

That is more than a specialist coefficient identity: it is a proved diagnostic and a changed calculation capability. It becomes a substantially stronger physics result once the predicted \(1+3+2\) shell is verified in an independent full one-cube diagonalization.
