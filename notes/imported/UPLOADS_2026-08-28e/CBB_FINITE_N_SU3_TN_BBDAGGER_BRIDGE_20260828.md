# Exact bridge from the published finite-rank SU(3) truncation to \(t_NBB^\dagger\)

## Verdict

There is an exact embedding, but it is **not** an embedding into the leading-large-\(N_c\), one-qutrit Hamiltonian that was simulated in Ciavarella--Bauer, *Phys. Rev. Lett.* **133**, 111901 (2024). That Hamiltonian deliberately makes the charge-odd plaquette inert. The exact embedding is the second-order Feshbach/Schur complement of the charge-odd one-plaquette block of the later Ciavarella--Burbano--Bauer \((1,2,2)\) truncation, including its \(1/N_c\) singlet transition. For SU(3), the entire local operator, including the determinant-specific first-order scalar, sits most naturally in their explicit \((2,2,2)\) qu6-plus-link-qubit Hamiltonian.

This bridge produces a result not extracted in either publication: the first controlled finite-\(N\) charge-odd kinetic operator in three spatial dimensions, its exact \(O(N^{-3})\) coefficient, and its homological zero-mode count. It also gives an unusually sharp truncation diagnostic: the leading-large-\(N\) model gives zero hopping, while the exact \(p+q\leq1\) link cutoff omits the \(\mathbf 8\) and \(\mathbf 6\) channels and gives the wrong sign, \(-1/12\), whereas the channel-complete result is \(+5/612\).

## Primary-source dictionary

The published Hamiltonian is

\[
\widehat H_{\rm CBB}
=\frac{g^2}{2}\sum_l \widehat E_l^2
-\frac{1}{2g^2}\sum_p(\widehat\Box_p+\widehat\Box_p^\dagger).
\]

After division by \(g^2\),

\[
\widetilde H:=\frac{\widehat H_{\rm CBB}}{g^2}
=\frac12\sum_l\widehat E_l^2-uV,
\qquad
V=\sum_p(\widehat\Box_p+\widehat\Box_p^\dagger),
\qquad
\boxed{u=\frac1{2g^4}}.
\]

This is exactly the normalization of the WORKHOUSE effective Hamiltonian. No further factor of two is required.

The qutrit plaquette states of the PRL map as

\[
|p,F\rangle=|\circlearrowleft\rangle_p=\widehat\Box_p|0\rangle,
\qquad
|p,\bar F\rangle=|\circlearrowright\rangle_p=\widehat\Box_p^\dagger|0\rangle,
\]

up to the paper's orientation convention. Hence

\[
\boxed{
|p,\pm\rangle
=\frac{|p,F\rangle\pm|p,\bar F\rangle}{\sqrt2}
=\frac{|\circlearrowleft\rangle_p\pm|\circlearrowright\rangle_p}{\sqrt2}.}
\]

The PRL explicitly identifies the minus combination as charge odd and shows that it decouples in the leading-large-\(N_c\), \(p+q\leq1\) qutrit Hamiltonian. Thus that simulated Hamiltonian predicts no nontrivial propagation in this sector.

The later paper's gauge-invariant basis is

\[
|\{\mathcal R_p\},\{\mathcal L_l\}\rangle
=\mathcal N
\prod_l |\mathcal L_l\rangle_l\langle\mathcal L_l|
\prod_p\widehat\Box_p^{(\mathcal R_p)}|0\rangle.
\]

Its \((n_p,n_l,k)=(1,2,2)\) truncation is exactly the first published truncation that retains the four shared-link irreps needed by the offsite second-order calculation:

\[
F\otimes\bar F=\mathbf1\oplus\mathrm{Adj},
\qquad
F\otimes F=\Lambda^2F\oplus\mathrm{Sym}^2F.
\]

The singlet is included by the paper's explicit \(1/N_c\) correction. The \((2,2,2)\) SU(3) Hamiltonian additionally restores the local determinant transition because \(\Lambda^2F\simeq\bar F\) for SU(3).

## Exact derivation from the published matrix elements

Appendix D of Ciavarella--Burbano--Bauer gives the exact plaquette matrix element

\[
|M_\rho|=
\sqrt{\frac{\dim\rho}{\dim A\,\dim R}}.
\]

For two fundamental factors, \(\dim A=\dim R=N\), so

\[
\boxed{|M_\rho|^2=\frac{d_\rho}{N^2}.}
\]

Thus the published finite-rank matrix element is exactly the channel-weight theorem used in WORKHOUSE. The paper's displayed \((1,2,2)\) transition amplitudes are the same statement written channel by channel:

\[
\frac1N,qquad
\sqrt{1-\frac1{N^2}},qquad
\sqrt{\frac12\left(1-\frac1N\right)},qquad
\sqrt{\frac12\left(1+\frac1N\right)}.
\]

The external one-plaquette energy in \(\widetilde H\) is

\[
E_F=2C_F,
\qquad C_F=\frac{N^2-1}{2N}.
\]

For a neighboring two-plaquette intermediate state, the six nonshared links contribute \(3C_F\), while the fused shared link contributes \(C_\rho/2\). Therefore

\[
\Delta_\rho=(3C_F+C_\rho/2)-2C_F
=C_F+\frac{C_\rho}{2}.
\]

The second-order Schur-complement weight is consequently

\[
w_\rho=-\frac{|M_\rho|^2}{\Delta_\rho}
=-\frac{d_\rho/N^2}{C_F+C_\rho/2}.
\]

Using the exact dimensions and Casimirs printed in the later paper gives

\[
\begin{aligned}
A_N&:=w_{\mathbf1}+w_{\mathrm{Adj}}
=-\frac{2N^3}{(N^2-1)(2N^2-1)},\\
B_N&:=w_{\Lambda^2F}+w_{\mathrm{Sym}^2F}
=-\frac{4N(N^2-2)}{(N^2-1)(4N^2-9)}.
\end{aligned}
\]

Charge-odd projection subtracts the two link-fusion families. Inserting the oriented face-boundary signs turns this difference into the signed shared-link adjacency \(S=BB^\dagger-4I\). Hence

\[
K^{(2)}_-=d_NI+(B_N-A_N)S
=E^{(2)}_{\rm flat,N}I+t_NBB^\dagger,
\]

with

\[
\boxed{
t_N=B_N-A_N
=\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)}.}
\]

This is therefore a sector-specific exact Schur complement of the published finite-rank truncation, not an unrelated coefficient formula.

## SU(3) ledger

For \(N=3\), \(C_F=4/3\). The four exact channel terms are

| link fusion | irrep | \(|M_\rho|^2\) | \(\Delta_\rho\) | \(w_\rho\) |
|---|---:|---:|---:|---:|
| \(F\otimes\bar F\) | \(\mathbf1\) | \(1/9\) | \(4/3\) | \(-1/12\) |
| \(F\otimes\bar F\) | \(\mathbf8\) | \(8/9\) | \(17/6\) | \(-16/51\) |
| \(F\otimes F\) | \(\bar{\mathbf3}\) | \(1/3\) | \(2\) | \(-1/6\) |
| \(F\otimes F\) | \(\mathbf6\) | \(2/3\) | \(3\) | \(-2/9\) |

Therefore

\[
A_3=-\frac{27}{68},
\qquad
B_3=-\frac7{18},
\qquad
\boxed{t_3=B_3-A_3=\frac5{612}}.
\]

In the physical convention of the published Hamiltonian,

\[
\widehat H_{\mathrm{eff},-}
=E_{\mathrm{flat}}(g)I
+\frac{5}{2448g^6}BB^\dagger+O(g^{-10}),
\]

because \(g^2u^2=1/(4g^6)\). The determinant-specific SU(3) local term gives the first-order rest energy

\[
\frac{E_-}{g^2}=\frac83+u+O(u^2),
\]

which is why the explicit SU(3) \((2,2,2)\) Hamiltonian, rather than the general-\(N\) \((1,2,2)\) formula alone, is the clean comparison object for the full operator.

## What the connection adds beyond the publications

1. **It activates a sector the PRL simulation made inert.** The leading-large-\(N_c\) qutrit Hamiltonian makes \((|\circlearrowleft\rangle-|\circlearrowright\rangle)/\sqrt2\) decouple. The published quantum runs and the later DMRG mass calculation use the vacuum-accessible/even sector; neither extracts a charge-odd dispersion.

2. **It controls a residual beyond the nominal large-\(N_c\) order.** Although \(A_N\) and \(B_N\) are individually \(O(N^{-1})\), their difference begins at

   \[
   t_N=\frac1{4N^3}+O(N^{-5}).
   \]

   The later truncation generally discards transitions suppressed by \(1/N_c^2\) or more. Ordinarily an \(O(N^{-3})\) residual extracted from such a Hamiltonian would be uncontrolled. Here the exact microscopic fusion census proves that the four displayed channels exhaust every second-order shared-link route in this one-particle charge-odd sector. That sector-specific exhaustiveness is the additional result.

3. **It is a sharp truncation diagnostic.** In common dimensionless units:

   \[
   t_3^{\rm leading\ large\ N}=0.
   \]

   Projecting instead to the exact finite-SU(3) link cutoff \(p+q\leq1\) retains only \(\mathbf1\) and \(\bar{\mathbf3}\), while removing \(\mathbf8\) and \(\mathbf6\). Its projected second-order value is therefore

   \[
   t_3^{p+q\leq1}=w_{\bar3}-w_{\mathbf1}
   =-\frac16+\frac1{12}=-\frac1{12},
   \]

   opposite in sign and about ten times larger in magnitude than the channel-complete \(+5/612\). The higher channels do not give a small correction; they reverse the kinetic sign through cancellation.

4. **It supplies a three-dimensional analytic benchmark.** The later paper gives three-dimensional circuit resource estimates but numerical spectra only in \(2+1\) dimensions and only for the scalar/even channel. The bridge predicts a complete finite-volume charge-odd spectral fingerprint for the proposed three-dimensional truncation.

## Decisive small-volume comparisons

### A. One open cube: smallest full-Hamiltonian test

Use the explicit SU(3) \((2,2,2)\) Hamiltonian on the six plaquettes of one open cube. Work in the global charge-odd block and track the six eigenvalues that tend to the one-plaquette electric energy as \(u\to0\). On the face space of one cube,

\[
\operatorname{spec}(\partial_2^\dagger\partial_2)
=\{0,4,4,4,6,6\}.
\]

After subtracting the common scalar, the exact prediction is

\[
\boxed{
\frac{E_j(u)-E_{\rm common}(u)}{u^2}
\longrightarrow
\left\{0,\frac5{153},\frac5{153},\frac5{153},
\frac5{102},\frac5{102}\right\}.}
\]

The zero mode is the signed cube boundary

\[
|\partial c,-\rangle
=\frac1{\sqrt6}\sum_{f\subset\partial c}
\operatorname{sgn}(c,f)|f,-\rangle.
\]

In the physical \(\widehat H\) units the splittings are

\[
\left\{0,
\frac5{612g^6}\ (\times3),
\frac5{408g^6}\ (\times2)\right\}+O(g^{-10}).
\]

This is small enough for exact diagonalization and directly tests the compact closed-surface carrier against the published finite-rank Hamiltonian.

### B. Periodic \(3^3\) reduced-Krylov test

Construct the exact charge-odd one-plaquette block and all adjacent two-plaquette fusion states of the published \((1,2,2)\) Hamiltonian. Form its exact second-order Schur complement. The one-face space has \(3L^3=81\) states. The predicted coefficient spectrum is

\[
\operatorname{spec}(t_3BB^\dagger)=
\left\{
0^{\times29},
\left(\frac5{204}\right)^{\times12},
\left(\frac5{102}\right)^{\times24},
\left(\frac5{68}\right)^{\times16}
\right\}.
\]

The \(29=L^3+2\) zero modes are a particularly discriminating test. Diagonalizing the full finite matrix at several small values of \(u\), tracking the one-plaquette cluster, and verifying that the residual after subtracting these coefficients is \(O(u^3)\) would be an independent small-volume spectral confirmation.

### Acceptance gates

- Reconstruct the four SU(3) amplitudes directly from the published Eq. (D1), not from WORKHOUSE constants.
- Reconstruct the denominators directly from the published Casimir table.
- Verify exact rational equality \(t_3=5/612\).
- Build the cubical incidence matrix independently from oriented cell boundaries.
- Verify the one-cube \(\{0,4^3,6^2\}\) and periodic-\(3^3\) multiplicity fingerprints.
- Compare the full-truncation eigenvalues at several small \(u\), with overlap-based state tracking through the degenerate cluster.
- Keep the result scoped to the charge-odd one-plaquette effective sector; this test does not by itself identify a physical glueball or establish continuum persistence.

The companion standard-library certificate
[`verify_cbb_tn_bridge.py`](./verify_cbb_tn_bridge.py) performs the algebraic
and finite-volume gates in exact rational arithmetic. Its fresh run passes
**18/18** checks, including the wrong-sign \(p+q\leq1\) control, the complete
open-cube scalar counterterm, and both finite-volume spectral fingerprints. It
intentionally does not claim the final full-Hamiltonian
small-\(u\) diagonalization, which remains the independent numerical comparison
to perform.

## Primary sources

- A. N. Ciavarella and C. W. Bauer, [“Quantum Simulation of SU(3) Lattice Yang-Mills Theory at Leading Order in Large-\(N_c\) Expansion,”](https://doi.org/10.1103/PhysRevLett.133.111901) *Phys. Rev. Lett.* **133**, 111901 (2024), [arXiv:2402.10265v3](https://arxiv.org/abs/2402.10265). The Hamiltonian is Eq. (1); the qutrit plaquette basis and charge-odd decoupling are Eqs. (7)--(9).
- A. N. Ciavarella, I. M. Burbano, and C. W. Bauer, [“Efficient Truncations of SU(\(N_c\)) Lattice Gauge Theory for Quantum Simulation,”](https://arxiv.org/abs/2503.11888) arXiv:2503.11888v5 (2026). The basis is Eq. (10); the \((1,2,2)\) Hamiltonian and transition amplitudes are Eqs. (17)--(18); the explicit SU(3) \((2,2,2)\) Hamiltonian is Eq. (20); the dimensions and Casimirs are in Appendix C; the exact dimension-ratio plaquette matrix element is Eq. (D1).
