# B=6 Open-Cube Sign-Reversal Validation

**Date:** 2026-08-28  
**Status:** **PASS — the channel-complete adjacent-face coefficient is \(+5/612\)**  
**Scope:** \(SU(3)\), one open cube, charge-odd one-face shell, through second order in \(u=g^{-4}\)

## Result

The public `pyclebsch` open-boundary master-formula implementation was run directly at local cutoff \(B=6\) on all six faces of a \(2\times2\times2\) open cube. The second-order calculation was performed without enumerating the full global \(B=6\) Hilbert space: only the states in

\[
M|0\rangle
\quad\text{and}\quad
M\mathcal P_{C=-}^{\mathrm{one\ face}}
\]

are required, where

\[
K(u)=H/g^2=H_0-uM,
\qquad
M=\sum_f(\Box_f+\Box_f^\dagger).
\]

The resulting charge-odd gap operator is

\[
\boxed{
W_{\mathrm{gap},B=6}^{(2)}
=\frac{39}{68}I_6+\frac{5}{612}G
},
\qquad
G=B^\mathsf TB,
\qquad
\operatorname{spec}G=\{0^{(1)},4^{(3)},6^{(2)}\}.
\]

The fitted hopping coefficient was

\[
t_{B=6}=0.008169934640514463,
\]

which rationally reconstructs to

\[
\boxed{t_{B=6}=\frac5{612}}
\]

with numerical error \(8.41\times10^{-15}\). The full matrix residual against \(39I/68+(5/612)G\) was \(6.66\times10^{-16}\).

Thus the \(B=4=T_1\) sign

\[
t_{B=4}=-\frac1{12}
\]

is reversed when the shared-link 
\(\mathbf6\) and \(\mathbf8\) channels are restored:

\[
\boxed{-\frac1{12}\longrightarrow +\frac5{612}}.
\]

## Absolute and relative shell coefficients

The six second-order gap coefficients at \(B=6\) are

\[
\boxed{
\left\{
\left(\frac{39}{68}\right)^{(1)},
\left(\frac{371}{612}\right)^{(3)},
\left(\frac{127}{204}\right)^{(2)}
\right\}.
}
\]

After subtracting the \(G=0\) singleton coefficient, the shell is

\[
\boxed{
\left\{
0^{(1)},
\left(\frac5{153}\right)^{(3)},
\left(\frac5{102}\right)^{(2)}
\right\}.
}
\]

In cubic language this is the same \(1+3+2\) shell as at \(B=4\), but with the ordering reversed: the singleton is lowest, the triplet is intermediate, and the doublet is highest at order \(u^2\).

The complete gap expansion through this order is therefore

\[
\Delta K_{C=-}(u)
=\frac83+u
+u^2\left(\frac{39}{68}I_6+\frac5{612}G\right)
+O(u^3).
\]

## Direct channel census

For any adjacent face pair with oriented Gram entry \(G_{ff'}=+1\), the independently generated Schur contraction gives the following raw shared-link contributions:

| raw shared-link irrep | contribution |
|---|---:|
| \(\mathbf1\) | \(+1/12\) |
| \(\mathbf3\) | \(-1/12\) |
| \(\bar{\mathbf3}\) | \(-1/12\) |
| \(\mathbf6\) | \(-1/9\) |
| \(\bar{\mathbf6}\) | \(-1/9\) |
| \(\mathbf8\) | \(+16/51\) |

Combining charge-conjugate raw labels into the four theory routes gives

\[
-w_{\mathbf1}=+\frac1{12},
\qquad
w_{\bar{\mathbf3}}=-\frac16,
\qquad
w_{\mathbf6}=-\frac29,
\qquad
-w_{\mathbf8}=+\frac{16}{51}.
\]

Their sum is

\[
\frac1{12}-\frac16-\frac29+\frac{16}{51}
=\boxed{\frac5{612}}.
\]

All twelve adjacent face pairs reproduce the same four-route identity, with the overall sign fixed by \(G_{ff'}=\pm1\).

## Why the reduced calculation is sufficient

At second order the degenerate Schur operator is

\[
W_{ab}^{(2)}
=\sum_{m\notin\mathcal P}
\frac{\langle a|V|m\rangle\langle m|V|b\rangle}
{E_0-E_m},
\qquad V=-M.
\]

It depends only on states reached by one action of \(M\) from the shell. The run found:

- 40 reachable states from each one-face odd basis vector;
- 127 states in their union;
- 12 states in \(M|0\rangle\);
- 1,000 directed local Wilson-loop transitions on each cube face;
- 24 ordered trivalent singlet tuples at \(B=6\).

No approximation is introduced by omitting states outside this one-step support at second order. A full global matrix would be necessary for finite-\(u\) diagonalization or higher perturbative orders, but not for the coefficient tested here.

Accordingly, **complete** in this report means the complete second-order reachable frontier. It does not mean construction or finite-\(u\) diagonalization of the full 3,864-state \(B=6\) physical Hamiltonian.

The first-order shell operator was \(I_6\) to \(2.22\times10^{-16}\), and the vacuum second-order shift was \(-9/2\).

## The important B=6 versus B=7 boundary

\(B=6\) is channel-complete for the **adjacent-face hopping coefficient** because the shared-link sextet route saturates

\[
C_2(\mathbf6)+2C_2(\mathbf3)
=\frac{10}{3}+\frac{8}{3}=6.
\]

It is not yet complete for every **same-face onsite** route. A same-face sextet pair requires

\[
C_2(\mathbf6)+C_2(\bar{\mathbf6})
=\frac{20}{3}>6,
\]

so it first appears at the integer cutoff \(B=7\).

A separate bounded \(B=7\) probe confirmed exactly this distinction:

\[
W_{\mathrm{gap},B=7}^{(2)}
=\frac{11}{34}I_6+\frac5{612}G.
\]

Thus

\[
\alpha_{B=7}-\alpha_{B=6}
=\frac{11}{34}-\frac{39}{68}
=-\frac14,
\]

while

\[
t_{B=7}=t_{B=6}=\frac5{612}.
\]

The \(B=7\) absolute spectrum is

\[
\left\{
\left(\frac{11}{34}\right)^{(1)},
\left(\frac{109}{306}\right)^{(3)},
\left(\frac{19}{51}\right)^{(2)}
\right\}.
\]

Therefore the sign-reversal prediction is genuinely settled at \(B=6\), but \(39/68\) must be described specifically as the **\(B=6\) scalar**, not as the final same-face-complete scalar.

## Reproducibility and hostile checks

The canonical run passed 19/19 gates in 3.66 seconds. A fresh-cache replay regenerated the CGCs and reproduced the first-order matrix, second-order gap matrix, Gram matrix, vacuum shift, channel ledger, rational spectra, and all gates exactly.

Additional checks were:

1. The executed `lattice_data.py` and `plaquette_matrix_elements.py` bytes match the downloaded public source archive exactly.
2. Every generated cube face has the same 1,000-entry absolute-coefficient multiset as the authors' public **OBC/universal** \(B=6\) trivalent master table, `B6_dim(3_2)_magnetic_hamiltonian.json.gz`. The maximum discrepancy, entirely from its 10-digit serialization, is \(4.82\times10^{-11}\).
3. The similarly named **PBC/develop** table, `B6_dim(3_2)_PBC_magnetic_hamiltonian.json.gz`, is a distinct 10,247-byte artifact. Its SHA-256 is recorded below for provenance, but it was not used in the coefficient-multiset cross-check. The two table hashes therefore identify different byte artifacts and are not conflicting measurements of one file.
4. All six cube faces were generated directly. No periodic-padding assumption was used.
5. The \(B=7\) boundary probe independently kept \(t=5/612\) while shifting only the scalar by \(-1/4\).

## Claim boundary

This is a decisive **author-code-derived** validation of the WORKHOUSE \(B=6\) sign-reversal prediction. The coefficient was not supplied to the generator; it emerged from the public local CGC/master-formula calculation and the independently assembled reachable-state Schur contraction.

It is not yet:

- an independent-group replication, because `pyclebsch`, `ymcirc`, and the Balaji et al. paper share author/code lineage;
- a symbolic exact-CGC computation—the local coefficients are double precision and were retained to 14 decimal places, while the rational claims are supported by rational reconstruction and residual gates;
- a construction of the full 3,864-state \(B=6\) matrix or a finite-\(u\) \(B=6\) spectrum;
- a continuum or infinite-volume glueball claim.

Within the stated finite open-cube, charge-odd, second-order sector, the result closes the proposed stronger test:

> **Restoring the shared-link \(\mathbf6\) and \(\mathbf8\) channels reverses the one-cube hopping coefficient from \(-1/12\) to \(+5/612\), and the independently generated \(B=6\) Schur spectrum exhibits the predicted positive \(1+3+2\) ordering.**

## Artifacts

Stable promoted artifacts at the workspace root:
 
- `B6_OPEN_CUBE_SIGN_REVERSAL_VALIDATION_2026-08-28.md` — this report.
- `reduced_b6_cube_second_order.py` — direct local generation and complete second-order reachable-frontier Schur calculation.
- `b6_cube_reduced_certificate.json` — canonical 19-gate result.
- `b6_cube_reduced_certificate_fresh_replay.json` — clean-cache replay.
- `b7_same_face_scalar_probe.json` — \(B=7\) scalar-shift certificate.
 
Supporting scratch artifacts:
 
- `.scratch/b6_cube_reduced/probe_b7_same_face_scalar.py` — bounded \(B=7\) interpretation probe.
- `.scratch/b6_cube_reduced/b6_run_stdout.txt` and `.scratch/b6_cube_reduced/b6_fresh_replay_stdout.txt` — complete run transcripts.

Pinned artifact hashes at completion:

| artifact | SHA-256 |
|---|---|
| stable `reduced_b6_cube_second_order.py` | `fb79dd04e532b54d1a7136da039b421d55d22b841bbe3f7db581558d8cab4575` |
| stable `b6_cube_reduced_certificate.json` | `2aab926a1387a143aa56440fc563d95b2566b79f1b4d24fc9826be599d54a6a1` |
| stable `b6_cube_reduced_certificate_fresh_replay.json` | `de16a1bb94060d9b7893a7671f27ee43eeee56aed1468ede19061cb1ab576ea9` |
| scratch `probe_b7_same_face_scalar.py` | `e2a8a0c66dd375fd3ca2d6833a1543da1abb902292052a366292d1e56246fb59` |
| stable `b7_same_face_scalar_probe.json` | `62ef39c9f6dad7b72fa1beee4880aae0c7b5cb373a7747116e2cd4f2a7369b2b` |
| public OBC/universal `B6_dim(3_2)_magnetic_hamiltonian.json.gz` (11,017 bytes; used) | `d72c876489193b89429b190426493e53219e79b58e2fe51b91ba5dd7f6e32f0e` |
| public PBC/develop `B6_dim(3_2)_PBC_magnetic_hamiltonian.json.gz` (10,247 bytes; not used) | `36f8c0992fb4e42b475878eb617034bba0511e45d725491ed8d9577c586f449f` |
| public `pyclebsch` source archive | `6d16ee0fa055b143d8373efa8d57e4f5a745b362bcab6eb12318a9c09922111b` |
