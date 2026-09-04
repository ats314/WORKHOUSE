# Hecke cover correspondence — strict-infrared cubic-chain level

Landed 2026-08-31. This document is the maintainer's own result note,
transcribed here from the task that requested its import. **It is corpus
evidence, T3, like everything else in `corpus-import/`.** Nothing in this
repository has independently re-run the generator or the verifier it
describes; see *What this repository has actually checked* below for the
one thing that has.

## What the note claims

For every tested odd prime, the construction maps a line

\[
\ell\subset\mathbf P^2(\mathbf F_p),\quad Q(\ell)=0
\longmapsto
M_\ell\subset L,\ L_\ell,
\]

with

\[
L=\mathbb Z^3,\qquad
L_\ell=M_\ell+\mathbb Z\,\frac{w_\ell}{p},
\qquad
[L:M_\ell]=[L_\ell:M_\ell]=p.
\]

The explicit homology push-pull is

\[
T_{\ell,j}
=
(\wedge^j A'_\ell)\,
p(\wedge^j A_\ell)^{-1},
\]

and every resulting \(H_1,H_2\) matrix is claimed integral. Locally,

\[
\partial'_jJ_j=J_{j-1}\partial_j,\qquad
J_2B=B'J_1,\qquad
\partial'_3J_3=J_2\partial_3,
\]

while the charge-odd source is claimed to obey

\[
J_2\mathcal O^-_{ij}(x)
=
\mathcal O^-_{U_iU_j}(Ux).
\]

### Target-blind prime values

The note states that the generator contains no expected eigenvalues, and
obtains

\[
\lambda_p=
\frac{\sum_\ell\sum_{|x|^2=1,\ x\in L_\ell}\widetilde{\mathcal H}_4(x)}
{12},
\qquad
A_p=p^4\lambda_p,
\]

directly from the \(p+1\) neighbors:

| \(p\) | \(\lambda_p\) | Geometric \(A_p\) |
|---:|---:|---:|
| 3 | \(-52/27\) | \(-156\) |
| 5 | \(174/125\) | \(870\) |
| 7 | \(-136/343\) | \(-952\) |
| 11 | \(-56148/14641\) | \(-56148\) |
| 13 | \(178094/28561\) | \(178094\) |
| 17 | \(-247662/83521\) | \(-247662\) |
| 19 | \(315380/130321\) | \(315380\) |
| 23 | \(204504/279841\) | \(204504\) |
| 29 | \(-3840450/707281\) | \(-3840450\) |
| 31 | \(-1309408/923521\) | \(-1309408\) |

The note reports that a separate, post-hoc verifier constructed the level-2
eta/Eisenstein newform independently and found agreement at all ten values,
and that its literal-target scan found no derived \(A_p\) embedded in the
generator.

### Fourth-order kernel result

The note claims that, for either kernel, the neighbor sum acts on the
infrared parameters by

\[
\begin{aligned}
\tau'&=(p+1)\tau,\\
C'&=\lambda_p C,\\
S_0'&=(p+1)S_0,\\
A'&=(p+1)A+\frac45\bigl((p+1)-\lambda_p\bigr)C,
\end{aligned}
\]

so that

\[
S_0|\xi|^2+
6C\frac{\mathcal H_4(\xi)}{|\xi|^2}
\longmapsto
(p+1)S_0|\xi|^2+
6\lambda_pC\frac{\mathcal H_4(\xi)}{|\xi|^2}.
\]

The note's own summary:

- The cubic harmonic Hecke eigenline survives both kernels.
- The historical 189-record pencil closes exactly for all ten primes.
- The raw v10a.26 pencil closes with maximum residual \(4.18\times10^{-13}\),
  against a declared tolerance of \(2\times10^{-8}\).
- The complete gap trace splits into a scalar eigenline \(p+1\) and a
  harmonic eigenline \(A_p/p^4\).
- Nine tests pass (in the note's own, external test suite).
- The remaining boundary is stated as microscopic: the two rational cubic
  cellulations need a common refinement carrying SU(N) link variables and
  Haar integration. Until that is constructed, the note describes this as an
  exact infrared chain/neighbor theorem — **not yet** a full interacting
  prime-orbit trace formula.

## Provenance, and what is missing from this repository

The note names six artifacts, all under a path on the maintainer's own
machine (`/C:/ALL THEORY/programs/gauge_dressed_spectral_zeta_20260830/
harmonic_packet_20260831/`):

- `NOTE_FLUX_hecke_cover_correspondence_2026-08-31.md` — the source of this
  transcription
- `ENGINE_FLUX_hecke_cover_correspondence.py` — the target-blind generator
- `generated/CERT_FLUX_hecke_cover_correspondence.json` — the geometric
  certificate
- `ENGINE_FLUX_verify_hecke_cover_correspondence.py` — the post-hoc verifier
- `generated/CERT_FLUX_hecke_cover_correspondence_replay.json` — the replay
  report
- `ENGINE_FLUX_test_hecke_cover_correspondence.py` — the nine tests

**None of the five Python/JSON artifacts are present in this repository.**
Only the prose note reached here. That makes this note's status, in the
corpus's own evidence vocabulary (`AGENTS.md`), **record-backed**: the
argument and its numbers are asserted, and the artifact that would let
someone here re-run it is absent — the same gap `G1` names for other
families. Landing the generator, the verifier, and both certificates, with
their SHA-256 digests, is what would let this repository's own `triage` and
`corpus_index` machinery see them, the same as every other program under
`corpus-import/programs/`.

## What this repository has actually checked

One thing, and only one: that the target-blind prime table above is
**internally consistent** — that the printed \(A_p\) equals \(p^4\lambda_p\)
computed from the printed \(\lambda_p\), for all ten listed primes, in exact
rationals. See `the geometric A_p column is p^4 times the printed lambda_p`
in `src/workhouse/invariants/hecke.py` (suite "Hecke cover correspondence
table"). That is a transcription check, not a re-derivation: it confirms the
table was copied without arithmetic slips, and says nothing about whether
\(\lambda_p\) is actually a Hecke eigenvalue of any newform, whether the
lattice construction is correct, or whether the boxed infrared
transformation holds. All of that remains **T3**.

## Open question this repository has not resolved

The note's \(C\), \(S_0\), \(A\), \(\tau\) and the quartic harmonic
\(\mathcal H_4\) use names that echo this corpus's own fourth-order
vocabulary (`C_shp`, the quartic obstruction shapes \(A, B, C, D\) of
`UNIFIED §5.1`, and the harmonic representatives of the 189-record kernel).
**Whether the note's \(C\) is the same object as this corpus's `C_shp`, under
a compatible normalization, has not been checked here and is not asserted by
this note.** Treating the resemblance as identity without deriving the
correspondence is exactly the `q_band^(4)` / `m_Γ^(4)` trap `CLAUDE.md`
warns about — two differently-anchored objects are not the same object
because they share a letter. See the falsifier recorded for unifying
candidate `U6` in `ledger/gaps.yaml`.
