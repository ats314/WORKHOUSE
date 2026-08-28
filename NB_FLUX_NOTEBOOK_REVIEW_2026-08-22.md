# NB_FLUX notebook review and repair

**Verdict:** preserve the idea, discard the original notebook workflow. The repaired notebook is worth running as a deterministic certificate, published-data replay, and tiny Monte Carlo regression. The current pilot and continuum campaign are **not** worth A100 time yet.

## Provenance and scope

- Original: `NB_FLUX_untitled238.ipynb`
- Original SHA-256: `EB0E4D364976692289AE24FE25021898BCB015FD86E5E2EC159420A4F01074E5`
- Repaired engine SHA-256: `258FEFD36B4155D1E96376A7FFCC4282B810BD2F1279B90DD58A8727FABCB42C`
- The original attachment and the WORKHOUSE repository were not modified.
- The unrelated notebook shown in the original upload-cell output was treated as historical output, not as an instruction or input.

The useful core is a Wilson-action SU(3) experiment intended to connect the WORKHOUSE zero-momentum charge-odd plaquette carrier to Euclidean cubic-channel spectroscopy. It combines:

1. chain-complex and cubic-symmetry checks on the tested $L=4$ torus;
2. SU(3) Monte Carlo, APE-dressed planar loops, a GEVP, and a torelon scale;
3. a replay of the published Athenodorou--Teper $T_1^{+-}$ continuum fit.

This is a meaningful representation/source diagnostic. It is not a proof that the protected strong-coupling carrier survives as a continuum particle.

## Decisive defect in the original

The original `reunitarize_matrix` used ordered column Gram--Schmidt. Although it returned nearly unitary matrices, it was not covariant under independent gauge rotations at the two endpoints of a link. Consequently, all APE-smeared loops, torelons, and the GEVP that used them were gauge dependent.

Measured on a generic field:

| SU(3) projection | RMS gauge-covariance defect | Maximum defect |
|---|---:|---:|
| Original column Gram--Schmidt | 0.4319 | 1.7993 |
| Repaired polar/SVD projection | $1.75\times10^{-7}$ | $6.02\times10^{-7}$ |

The repaired engine uses the polar factor $Q=UV^\dagger$ and a scalar determinant-phase correction to SU(3). It adds both a bi-unitary projection test and an end-to-end random-local-gauge test of the complete APE step.

## Other original problems

- The notebook was two incompatible workflows pasted together. One cell uploaded an unrelated `.ipynb`; later cells called two absent Python files and an unsupported `next` profile. One cell could rename an arbitrary Python file.
- The first 1,730-line cell executed immediately in Jupyter instead of separating definitions from runs.
- The “physical carrier” gate was hard-coded `True`; incidence ranks called floating-point SVD “exact.”
- The saved smoke mass hit its optimization ceiling, two-point/dof-zero fits passed, and `p=NaN` could pass.
- A negative, extremely uncertain “ground fraction” passed because its uncertainty enlarged the allowed interval. It was not a normalized residue.
- Bootstrap failures were silently discarded without reporting the success fraction.
- Nonfinite autocorrelation inputs were assigned the minimum blocking time.
- JSON was written before hard-gate failure, emitted non-standard `NaN`, and combine mode ignored stored failures.
- Repeated runs in one kernel accumulated stale global gates.
- Unknown/misspelled scientific arguments were silently ignored.
- The code could install CuPy during a run and had no checkpoints for a huge production campaign.

## Repairs made

- Replaced Gram--Schmidt with gauge-covariant polar/SVD projection to SU(3).
- Added projection and full APE gauge-covariance regressions.
- Moved the staple/action audit to a post-warm-up nontrivial field; added global over-relaxation action invariance. Forty warm-up cycles do not establish equilibration.
- Replaced floating ranks with exact modular elimination over two primes.
- Replaced the hard-coded carrier gate with an actual signed plaquette-cochain permutation check, including basepoint and orientation signs.
- Required at least three fit times, non-boundary solutions, positive dof, finite diagnostic p-values, and at least 50% bootstrap-fit success.
- Rejected non-positive/singular bootstrap GEVP metrics instead of clipping them into existence.
- Corrected the periodic $t=0$ factor in the raw amplitude proxy and renamed it an **exploratory amplitude ratio**. It has no pass gate and is not called a residue.
- Cleared gates on every run; stripped only the standard Jupyter `-f kernel.json` pair and now reject other unknown arguments.
- Disabled in-run package installation and protected large profiles behind an explicit acknowledgement.
- Added strict JSON (`null`, never `NaN`), schema/version/source/config hashes, atomic writes, and combine-time rejection of failed or mixed-source results.

## Repaired validation result

The executed repaired CPU smoke run completed in about five seconds:

- all 16 hard gates passed;
- APE projection covariance error: $3.12\times10^{-7}$;
- full APE-step local-gauge error: $4.55\times10^{-7}$;
- post-warm-up staple identity error: $1.79\times10^{-7}$;
- global over-relaxation drift per plaquette: $1.14\times10^{-8}$;
- published same-data replay: $M/\sqrt\sigma=6.0598(441)$ versus the paper's $6.065(40)$, a deterministic regression delta of $-0.0052$ rather than an independent statistical pull.

There were three intentional warnings: too little autocorrelation coverage, only four bootstrap blocks, and $L a\sqrt\sigma=1.67<3$. The exploratory T1 fit was a soft diagnostic and only 35 of 60 bootstrap fits succeeded. Therefore the smoke mass and amplitude ratio are **execution diagnostics, not physics evidence**.

The exact seeded numbers were executed with CPython 3.12.13, NumPy 2.3.5, and SciPy 1.18.1; the companion requirements lock records the environment because other NumPy versions produce a different deterministic random trajectory.

## Scientific limitation that remains

The raw diagonal plaquette source is not spin-pure. Its leading continuum tensor obeys

$$
S_{iii}=H_{iii}+\frac35 V_i,
$$

so the cubic $T_1$ source contains both $J=3$ and $J=1$ operator components. The notebook has no separate $V_{T_1}$, $H_{T_1}$, $H_{A_2}$, or $H_{T_2}$ sources, so it cannot decide the WORKHOUSE $J=1$ versus $J=3$ question. A finite-spacing $T_1$ label alone is not continuum spin.

It also omits the WORKHOUSE improved source

$$
o_3^{\rm imp}(U)=\frac{32\,\operatorname{ImTr}U-\operatorname{ImTr}U^2}{24},
$$

and its fixed APE-level schedule does not hold a physical dressing radius fixed as $a\to0$.

## Run decision

Run the repaired notebook now only as a validation artifact. Do **not** start the pilot or continuum suite yet.

Before spending A100 time, redesign the measurement layer to include:

1. raw and improved sources at fixed physical flow/smearing radius;
2. spin-resolved $V_{T_1}$, $H_{T_1}$, $H_{A_2}$, and $H_{T_2}$ operators;
3. scattering/torelon contaminant operators and multiple spatial volumes;
4. shared blocked resampling, correlated fit-window/basis stability, and joint mass/string-scale ratios;
5. topology and optimized-correlator autocorrelation monitoring, multiple chains, checkpoints, and raw-correlator preservation.

The A100 will be useful after that redesign. The delivered CUDA backend was not configured or validated for the local 7900 XTX; using it requires a separately validated ROCm-capable backend rather than a runtime flag.

## Reference

The hard-coded published arrays match the Wilson-action data and continuum $T_1^{+-}$ result in [Athenodorou and Teper, *The glueball spectrum of SU(3) gauge theory in 3+1 dimensions*](https://arxiv.org/abs/2007.06422). The replay is a transcription/regression check, not independent evidence.
