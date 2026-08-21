# Progress on $m_6$ and native $\sigma_5,\sigma_6$ — execution report

**Date:** June 14, 2026
**Scope:** the two open items from the consolidated theorem —
(1) the sixth-order SU(3) rest-mass coefficient $m_6$, and
(2) promoting $\sigma_5,\sigma_6$ from historical KPS targets to project-native.

**Honest summary up front.** Neither item is reducible to a final exact
rational in a single sandbox session: $m_6$ is an HPC-scale global contraction
(the fifth order already had 6.68M supports), and a from-scratch native
$\sigma_5,\sigma_6$ is a PRL-grade strong-coupling computation whose engine
source is not in the project. **No values were fabricated.** What follows is
verified, reproducible progress on the bounded sub-problems, with every result
cross-checked against already-certified orders, plus the exact specification of
the remaining compute.

---

## Part 1 — $m_6$: local-algebra layer closed

The bundle had pre-cleared two of the three sixth-order blockers (folded
des-Cloizeaux weights; the universal local carrier census). The third —
*"explicit normalized edge tensors/projectors for the geometry-realised
degree-eight and double-determinant signatures"* — is now built and verified.

### 1.1 All nine sixth-order local sectors, exactly

Using exact integer SU(3) rep theory (fusion paths; no floating point), with
dense explicit-kernel cross-checks wherever the tensor space fits in memory:

| Sector $(n_f,n_{\bar f})$ | $\dim\mathrm{Inv}$ | explicit kernel | determinant # | max $C_2$ |
|:---:|:---:|:---:|:---:|:---:|
| $(0,3)$ | 1 | 1 ✓ | 1 | $4/3$ |
| $(0,6)$ | 5 | 5 ✓ | 2 | $10/3$ |
| $(1,1)$ | 1 | 1 ✓ | 0 | $4/3$ |
| $(1,4)$ | 3 | 3 ✓ | 1 | $10/3$ |
| $(1,7)$ | 21 | (3⁸ — fusion-exact) | 2 | $6$ |
| $(2,2)$ | 2 | 2 ✓ | 0 | $10/3$ |
| $(2,5)$ | 11 | 11 ✓ | 1 | $6$ |
| $(3,3)$ | 6 | 6 ✓ | 0 | $6$ |
| $(4,4)$ | 23 | (3⁸ — fusion-exact) | 0 | $28/3$ |

Every sector with $\dim\le 3^7$ was cross-checked by explicitly diagonalizing
the total quadratic Casimir on the $3^{n_f+n_{\bar f}}$-dimensional tensor
space and counting the zero-eigenvalue (singlet) subspace; **$\dim\mathrm{Inv}$
equals the fusion-path count in every case**. The two $3^8$ sectors $(1,7)$ and
$(4,4)$ exceed a dense-matrix memory budget and are given by the exact (integer)
fusion count, which the smaller sectors prove agrees with the kernel.

The genuinely new sixth-order sectors are the **balanced degree-eight $(4,4)$**
(23 paths, electric ladder up to $14/3$) and the **double-determinant $(0,6)$
and $(1,7)$**. Maximum singlet multiplicity 23 and maximum intermediate irrep
dimension 27 both match the certified universal census.

### 1.2 Explicit edge tensors for the new sectors

The named blocker — explicit, normalized invariant tensors for the new sectors
— is constructed and verified:

- **$(0,3)$ single determinant:** the unique invariant is confirmed to be the
  normalized Levi-Civita tensor $\varepsilon_{ijk}$ (matches to machine
  precision up to phase).
- **$(0,6)$ double determinant (new at sixth order):** the 5-dimensional
  invariant subspace is constructed explicitly; the basis is orthonormal to
  $4\times10^{-16}$ and genuinely SU(3)-invariant (every generator annihilates
  it to $2.6\times10^{-15}$). These are the $\varepsilon\otimes\varepsilon$
  symmetry classes on six antifundamental indices.
- **$(2,2)$ and $(3,3)$ balanced:** dimensions 2 and 6, orthonormal and
  invariant to machine precision.

### 1.3 Exact electric-energy ladders

The intermediate-Casimir (electric energy $=C_2/2$ per link) levels reachable
in each sector, exactly:

| Sector | electric-energy levels |
|:---:|---|
| $(1,1)$ | $0,\ 2/3$ |
| $(2,2)$ | $0,\ 2/3,\ 5/3$ |
| $(3,3)$ | $0,\ 2/3,\ 3/2,\ 5/3,\ 3$ |
| $(4,4)$ | $0,\ 2/3,\ 3/2,\ 5/3,\ 8/3,\ 3,\ 14/3$ |
| $(0,6)$ | $0,\ 2/3,\ 3/2,\ 5/3$ |
| $(1,7)$ | $0,\ 2/3,\ 3/2,\ 5/3,\ 8/3,\ 3$ |

These are the exact energy denominators the folded des-Cloizeaux engine
consumes at sixth order.

### 1.4 Independent reproduction of the certified censuses

A clean reimplementation of the fusion-path enumeration reproduces, exactly:

- universal feasible signatures at six insertions (8 events): **2186** — matches
  the bundle's certified value;
- balanced local signatures at four insertions: **140** — matches the certified
  fourth-order balanced count.

(The universal counts at four/five insertions are 242/728; these are the
free-boundary census, larger than the physically-bounded ordered counts
140/574, as expected.)

### 1.5 What remains for $m_6$ (HPC-scale)

Two blockers remain, both genuinely large:

1. **Connected six-insertion geometry census.** Enumerate the connected spatial
   plaquette supports at sixth order. The fifth-order census had 6.68M supports
   and 39.4M support/output pairs; sixth order is larger and, per the bundle's
   own guidance, needs external-memory sharding rather than an in-memory
   expansion.
2. **Global trace-wiring contraction at $\Gamma$.** Contract the realised
   local edge tensors (now available) against the geometry census, fold with
   the certified des-Cloizeaux weights, and sum to the scalar
   $q_6=m_6=\tfrac13\operatorname{tr}H_6(0)$.

The recommended architecture (unchanged): triality + charge-conjugation
reduction before contraction; fusion-path basis as the primary local basis
(it carries all new sectors, as shown above); contract the zero-momentum trace
only, deferring the full real-space kernel until $m_6$ is fixed.

**Status:** local layer **closed and verified**; global geometry + contraction
**open (HPC)**. $m_6$ value: **not yet determined; not fabricated.**

---

## Part 2 — native $\sigma_5,\sigma_6$: verified, not yet native

### 2.1 What is and isn't available

The project has a **native** string-tension engine through $O(u^4)$ (the
"pair-ledger" torelon character expansion producing
$\sigma_0=\tfrac23,\ \sigma_1=0,\ \sigma_2=-\tfrac{22}{153},\ \sigma_3=-\tfrac{61}{408},\ \sigma_4=-\tfrac{737327120374220449}{7250590288602460800}$).
$\sigma_5$ and $\sigma_6$ are **exact KPS historical targets**
(Kogut–Pearson–Shigemitsu Table 2, 3+1D), not project-native reruns. The
native torelon engine source is **not** in the project files (only its
certificate output and the $L=4$/$L=5$ pair ledgers); the A100 notebooks are
numerical Monte-Carlo string-tension *proxies*, a different method.

### 2.2 Consistency verification (all pass)

- **Bridge.** $\sigma(u)=\tfrac12 W(2u)$ with KPS variable $x=2u$, i.e.
  $W_n=\sigma_n/2^{\,n-1}$. The implied $W$-series has the correct structure:
  $\sigma_0=\tfrac23=C_2(\text{fund})/2$ (bare flux energy per link);
  $\sigma_1=0$ (a single plaquette cannot return to the flux line);
  $\sigma_{n\ge2}<0$ (magnetic dressing lowers the flux energy). The superseded
  $(-1/4)^n$ mixed-variable conversion is **not** used.
- **Ratio coefficients.** $c_0,\dots,c_5$ in
  $m/\sqrt\sigma=\sqrt6\sum_n c_n u^n$ were re-derived from scratch from the
  $m$- and $\sigma$-series; **all six match the certificate exactly.**
- **Sixth-order ratio.** $c_6=\tfrac{m_6}{2}+K$ verified: the slope
  $\partial c_6/\partial m_6=\tfrac12$ exactly, and the constant
  $K=\tfrac{1181646977233006828729169209802562361069278851250351799}{168641444007491247688836385300053017225944999004544000000}$
  matches the certificate exactly. So once $m_6$ (Part 1) is known, $c_6$ is
  fixed — the only $\sigma$-input it needs is $\sigma_6$, already given.

### 2.3 Sensitivity — does the $\sigma_5/\sigma_6$ softness matter?

The transmission of a $\sigma_5$ error into the ratio is:

$$
\frac{\partial c_5}{\partial(\text{frac }\sigma_5)} = +0.0685,
\qquad
c_5 = -0.2281.
$$

A **1% error in $\sigma_5$ shifts $c_5$ by $+0.000685$, i.e. 0.30% of $c_5$** —
genuinely soft (sub-linear transmission), but a real $0.3{:}1$ ratio, not
negligible. This quantifies the "soft dependency" label: the historical-target
reliance affects the fifth-order ratio coefficient at the few-tenths-of-a-percent
level per percent of $\sigma_5$ uncertainty. Since the strong-coupling series is
not yet continuum-extrapolatable (the project diagnostic shows the truncation
peaks near $R\approx3.73$ versus the continuum $6.065$), the practical role of
$\sigma_5,\sigma_6$ is in firming up the *series coefficients* themselves, which
is precisely what a native rerun would deliver.

### 2.4 Native-engine specification (the remaining work)

Promoting $\sigma_5,\sigma_6$ to project-native requires extending the torelon
strong-coupling engine from $O(u^4)$ to $O(u^6)$. The exact specification:

1. **Model space.** A single static fundamental flux line of length $L$ wrapping
   a periodic spatial direction: $L$ links in the fundamental, electric energy
   $C_2(\text{fund})/2=\tfrac23$ per link, $E_0=\tfrac23 L$.
2. **Perturbation.** $V=-u\sum_p(\chi_p+\bar\chi_p)$, the fundamental-character
   plaquette operator, which dresses the flux line with plaquette excitations
   and recouples adjacent link reps via SU(3) fusion.
3. **Matrix elements.** The plaquette operator between flux configurations
   requires the explicit SU(3) recoupling (6j / Clebsch–Gordan) coefficients —
   the same local invariant/Casimir machinery validated in Part 1 supplies the
   intermediate-rep ladders and edge tensors.
4. **Perturbation theory.** Apply the **certified** order-generic folded
   des-Cloizeaux recurrence (it passed all sixth-order gates) to assemble the
   energy corrections through $O(u^6)$.
5. **Extensivity.** Extract $\sigma_n$ as the $L$-linear (per-unit-length)
   coefficient; the linked-cluster theorem guarantees only connected local
   decorations contribute. Validate by the certified $L$-independence
   ($L=4$ vs $L=5$).
6. **Validation gate.** The engine must first reproduce the native
   $\sigma_0,\dots,\sigma_4$ exactly, then the KPS $\sigma_5,\sigma_6$ targets;
   matching both promotes the targets to project-native.

This is a self-contained computation with a perfect external check (the KPS
targets), but it is a genuine engine build at PRL scale, not a sandbox
one-liner — which is why it is specified here rather than executed with
unverified output.

**Status:** $\sigma$-series and ratio **internally verified**; $\sigma_5,\sigma_6$
**remain KPS historical targets** pending the native torelon engine. Values:
**not fabricated.**

---

## Combined status

$$
\boxed{m_6\text{ local algebra + new-sector edge tensors: closed, verified}}
$$

$$
\boxed{m_6\text{ global geometry census + contraction: open (HPC)}}
$$

$$
\boxed{\sigma\text{-series + }m/\sqrt\sigma\text{ ratio: internally verified exactly}}
$$

$$
\boxed{\sigma_5,\sigma_6\text{ native promotion: open (requires absent torelon engine)}}
$$

$$
\boxed{\text{No }m_6,\ \sigma_5,\ \sigma_6\text{ values fabricated}}
$$

### Artifacts

- `CERT_Y6_su3_sixth_order_local_algebra.json` — nine-sector invariant dimensions,
  explicit-kernel cross-check flags, universal census counts.
- `CERT_SU3_edge_tensor_certificate.json` — epsilon-alignment, double-determinant
  dimension, per-sector electric-energy ladders.
