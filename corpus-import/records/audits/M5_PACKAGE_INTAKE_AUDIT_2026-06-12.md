# M5 Tier-2 Package — Intake Audit

**Date:** June 12, 2026  
**Scope:** Uploaded compact-window proof/certificate, Lemma-B review materials, C-form proof, final-review script, and archival-verification note.

## 1. Verdict

The **mathematical chain is credible and no counterexample or sign error was found**. The compact-window theorem was rerun from source and independently reviewed. Region A and the C-form/full-channel conversion were independently reconstructed from the displayed formulas and passed.

The upload is **not yet a self-contained archival proof package**. The supplied `m5_final_review_checks.py` fails because four required generated records are absent, and the original Lemma-B proof/certificate sources are also absent. Therefore the correct status is:

> **Theorem closed within the displayed model; archival closure pending restoration of missing source/certificate artifacts.**

## 2. Checks completed in this intake

### 2.1 Lemma A compact window

Executed:

```text
python3 m5_10_lemma_a_compact_certificate.py
python3 lemma_a_compact_review_checks.py
```

Both completed without assertion failure.

Decisive certified margins:

- uniform pre-mixing margin: `0.163955698444`;
- uniform compact lower bound: `0.006854458247993`;
- finite compact lower bound: `0.004846293203062`.

The analytic steps were also checked: roots-of-unity identity, contour-shift rate, convex geometric tail, monotonicity in `tau` and `L`, heat-kernel upper/lower envelopes, and directed cell inequalities.

### 2.2 Lemma A Region A

The missing Region-A engine was independently reconstructed from the formulas stated in the final archival note.

For

```text
U(tau)=2 exp(-16 tau)/(1-exp(-48 tau)),
h(u)=(1+u)^4-1,
```

convexity gives `u h'(u) >= h(u)`, while

```text
(d/dtau) log U < -16.
```

Hence

```text
(d/dtau) log[tau^2 h(U(tau))] < 2/tau - 16 <= -11
```

for `tau >= 2/5`. The endpoint interval calculation gives

```text
(4/5)^4/(16 pi^2 tau^2) - h(U(tau))
>= 0.002852525682303
```

at `tau=2/5`. Thus the Region-A envelope is valid.

### 2.3 C-form and full-channel conversion

The derivative algebra was checked independently. For `C=1/28`,

```text
D_C(beta)=beta + gamma log(beta) - 56/5 - gamma/2 + 22/21,
gamma=11/(8 pi^2).
```

Directed evaluation gives

```text
D_C(9.9) < 0 < D_C(10),
```

so the unique maximizer has `beta_* > 9.9`. At stationarity,

```text
Tbar(C)=(27/22)(beta_*+gamma/2)/beta_*^2.
```

Using only `pi^2>9`, hence `gamma<11/72`, gives the exact rational ceiling

```text
Tbar(1/28) < 3265/26136
             = 0.124923477196204...
             < 1/8,
```

with exact margin `1/13068`. The calibrated optimum is

```text
Tbar(1/28)=0.124806009996272...
```

The remaining arithmetic is exact:

```text
T_H=1/64,
T_full<1/64+1/8=9/64,
N_C^*>=8,
N^*>=7.
```

### 2.4 Lemma B reviewer

The portable reviewer was rerun using the constants recorded in the uploaded independent-review note:

```text
G_BOUND=0.018664535031499407,
C2=0.2311.
```

LR2-LR5 all passed, including

```text
RHS_true(15/28)=0.017880806390313 < G_BOUND,
psi(4)=0.004051160184 < dC=0.005043865741.
```

This confirms the reviewer-side numerical and analytic consistency. It does **not** replace the missing original `ENGINE_OP1_lemma_b_cert.py` and `LEM_OP1_lemma_b_proof_2026-06-12.md` for source-level reproducibility.

## 3. Archival failures in the delivered upload

The delivered `m5_final_review_checks.py` requires:

| Dependency | Delivered? |
|---|---:|
| `m5_10_lemma_a_compact_certificate.json` | No; regenerated during intake |
| `lemma_a_compact_review_checks.json` | No; regenerated during intake |
| `m5_region_a_certificate.json` | No |
| `m5_cform_full_channel_certificate.json` | No |
| `LEM_MISC_lemma_b_cert_rerun.json` | No |
| `lemma_b_review_checks_portable.json` | No |

Consequently, the final checker terminates with `FileNotFoundError` at `m5_region_a_certificate.json`.

Additional missing provenance sources named by the package itself:

- `LEM_OP1_lemma_b_proof_2026-06-12.md`;
- `ENGINE_OP1_lemma_b_cert.py`;
- original upstream M4 normalization source;
- the claimed checksum manifest and final ZIP archive.

## 4. Formatting defects found

The uploaded compact-window proof still contains three malformed LaTeX tokens:

```text
\\frac
```

at the derivative and Fourier-envelope formulas. The uploaded C-form proof ends with one orphan display closer:

```text
\]
```

Corrected copies were produced without changing mathematical content.

## 5. Files produced in this intake

- `m5_10_lemma_a_compact_certificate.json`
- `lemma_a_compact_review_checks.json`
- `m5_region_a_certificate_reconstructed.py`
- `CERT_MISC_m5_region_certificate_reconstructed.json`
- `m5_cform_full_channel_certificate_reconstructed.py`
- `CERT_MISC_m5_cform_full_channel_certificate_reconstructed.json`
- `LEM_OP1_compact_window_proof_corrected_2026-06-12.md`
- `THM_Y5_m5_cform_full_channel_proof_corrected_2026-06-12.md`

The reconstructed files are explicitly labeled as independent reconstructions, not as recovered originals.

## 6. Freeze criterion

Do not label the repository archive “fully reproducible” until the original Lemma-B proof/certificate and all six final-checker dependencies are deposited and `m5_final_review_checks.py` runs from a clean directory without reconstructed or hand-seeded inputs.

The mathematical statement that may be frozen now, under the displayed M4/M5 definitions, is:

```text
T_C < 1/8,
T_full < 9/64,
N_C^* >= 8,
N^* >= 7.
```

This is a theorem about the stated finite-lattice harmonic-plus-coexact AF-diagonal model, not a physical Yang-Mills mass-gap theorem.
