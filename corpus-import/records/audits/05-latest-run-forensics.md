# Latest attempted-run forensics

Date: 2026-08-19  
Scope: the five notebooks supplied from `C:\Users\Alex\Downloads`  
Method: read-only notebook/metadata/hash inspection and static source audit. Notebook prose and comments were treated as claims to test, not as instructions.

> **Runtime-evidence addendum:** a separately supplied transcript now proves that v25 was executed outside the saved notebook and crashed at `Q2 Haar unsupported occurrence pattern (2, 5)`. The notebook itself remains output-empty. The exact failure and its order-boundary cause are documented in `06-pattern-2-5-runtime-forensics.md`, which supersedes this report wherever this report says the v25 runtime failure was unknown.

## Executive verdict

These attachments are not preserved runs. They are five downloads representing only three unique, syntax-valid source notebooks. Every code cell has `execution_count: null` and `outputs: []`. They contain no runtime result, traceback, gate summary, timing, checkpoint, environment manifest, or output hash.

The user's concern is justified at the process-integrity level:

- duplicate downloads inflate five apparent attempts into three artifacts;
- the artifacts are roughly 95% copy-forward monoliths rather than isolated changes;
- important markdown claims about blindness, gate coverage, exactness, completeness, and checkpoint matching are contradicted or materially weakened by the code;
- final success checks omit prerequisite gates created earlier in the same notebook;
- several advertised proofs are configuration checks, same-implementation comparisons, or equalities forced by construction;
- none implements the required canonical 3,895-record Stage-3H computation.

This is strong evidence of a broken generation, execution, and reporting workflow. It is not evidence by itself that an agent deliberately sabotaged or fabricated a run. With outputs absent, the files cannot establish that any run occurred, what failed, or why the outputs disappeared.

## Attachment identity and evidence status

| Attachment | SHA-256 | Disposition |
|---|---|---|
| `NB_O4_hodge_v10a25_hamer_gelfand_a100.ipynb` | `4E0F7970D659CF569BD99E7EBDDBF41F3590E1DFEC615A6CDD6F5498F9BFE61D` | unique source candidate; no run evidence |
| `NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb` | `96E3263BCA6534E6E598FEC07F2310EAF88EB48266C0B7EAE17CBEC26D0DC9CA` | unique source candidate; no run evidence |
| `Hodge_v10a26_Factor52Complete_ExactSW_RootedOracle_A100 (1).ipynb` | same as preceding row | byte-identical duplicate download |
| `NB_O4_hodge_v10a24c_section15_reduced_gpu_benchmark_fresh.ipynb` | `C779D4BDC9CB561912DACB0AE03DABD8F7D6CD81ABF8841767BDAE8CD961F435` | unique narrow benchmark source; no run evidence |
| `Hodge_v10a24c_SECTION15_REDUCED_GPU_BENCHMARK_FRESH_A100 (1).ipynb` | same as preceding row | byte-identical duplicate download |

All three unique notebooks contain one markdown cell and one large code cell. The code parses successfully, so this audit did not find a simple syntax failure. That does not make the notebooks runnable, evidential, mathematically complete, or practically feasible.

About 95% of the logical lines in each unique notebook also occur verbatim in the others. The v10a.25 file is 97.66% line-similar to the earlier v10a.24c production-no-watchdog source. Version-number churn is therefore obscuring a small number of tail changes inside repeated 7,000-plus-line programs.

## v10a.25: Hamer/Gelfand candidate

### What may be salvageable

- an order-by-order Gelfand recurrence replaces finite-`u` polynomial fitting in the finite-cluster tail;
- the one-particle effective block is vacuum-subtracted before the rooted incidence transform;
- a disconnected-spectator comparison is present.

These are candidate implementation ideas, not accepted evidence.

### Critical defects

1. **The stated blind boundary is false.** The markdown says the Hamer number remains unavailable until recurrence and `m1`-`m3` gates pass. The source hard-codes `_HAMER_X4`, computes and prints the Hamer residual, and records its gate at logical code lines 7385-7399. Only afterward does it test `if not all(...)` at 7401-7406. The shared `gate()` function merely logs; it does not stop execution. Hamer is therefore loaded even when a protected lower-order gate failed.

2. **The final gate slice omits earlier prerequisites.** `V23_GATE_START` is set at logical line 6444. Both the pre-Hamer and final checks use only `gates[V23_GATE_START:]`. Earlier Haar, Hodge, physical-Q, and support gates—including the support-resolved pole check—can fail without preventing the final v10a.25 PASS conclusion.

3. **The Q-depth “proof” is vacuous.** Logical lines 7256-7258 accept “Q-depth two covers every closed magnetic walk” solely when `V10A25_ORDER <= 4`. That checks a requested order, not basis closure, omitted-state leakage, or support completeness.

4. **The final scalar equality is forced.** Logical lines 7418-7424 define `local_shift = M4_ORACLE - ax_rest` and add that shift to the anchor diagonal. Lines 7435-7440 then gate that the shifted rest equals the oracle/Hamer value. The oracle equality is true by construction; the Hamer equality repeats the earlier scalar comparison. The non-scalar checks are unchanged by a local scalar shift.

5. **A structural regression was removed.** The file calculates and prints `record_count` but does not require `record_count == 189`, unlike the earlier v10a.24c candidate.

6. **The normalization bridge remains an assumption.** The Hamer comparison asserts `H=W/2, u=x/2`; the project-wide audit still lists the canonical magnetic-normalization derivation as open. A numerical match under an unproved conversion cannot close that gate.

### Disposition

Quarantine as a source experiment and do not migrate its recurrence into production. Do not accept its PASS, Hamer certificate, blindness claim, or final shifted kernel as evidence.

## v10a.26: Factor-(5,2) and SW candidate

### Production salvage decision

Nothing from the Factor52 branch is eligible for the canonical O4 implementation. Its numerical SW/BCH and atomic-write ideas are generic techniques already available independently; they do not justify migrating this branch or its `(5,2)/(2,5)` contractor. The notebook has no execution record and the advertised certificate is not closed.

### Critical defects

1. **Prerequisite failures are again excluded.** `gate()` only logs at logical lines 142-145. The terminal barriers inspect only `gates[V23_GATE_START:]`, with the slice beginning at line 6439. Every required gate recorded before that point is outside final success.

2. **Preflight can report process success without gate success.** With `V10A26_PREFLIGHT_ONLY=1`, logical lines 7628-7630 exit with status 0 after printing a successful-smoke message. No assertion first proves that the logged preflight or earlier gates passed.

3. **Failed work can enter the resume cache.** The preflight result and each shape are checkpointed before the terminal all-gates barrier. Logged failures therefore do not prevent cache acceptance.

4. **“Exact matching resume” is false.** The checkpoint signature covers only a schema string, `L`, polarization, and shape-key representations. It omits source hash, effective configuration, Haar/SW implementation hash, dependencies, backend, precision, and environment. The loader uses untrusted Python pickle and can silently resume stale results after meaningful code changes.

5. **The completeness gate is self-referential.** Logical lines 6953-7000 hard-code an occurrence cap of seven and a supported-pattern set, enumerate the center-admissible pairs under that same cap, and compare the two sets. This does not independently prove that the actual P+Q1+Q2 production states never exceed seven occurrences. No production occupancy census is the premise of the gate.

6. **“Exact” overstates the arithmetic.** Integer Grams and a symbolic inverse are converted to `float64`; tensor contractions and acceptance checks use floating tolerances. This may be a sound numerical realization, but it is not an exact-arithmetic run artifact.

7. **The new projector lacks an independent `(5,2)` oracle.** The rank/span/projector checks are internal algebraic checks on the same constructed invariant family. There is no separate dense or exact contractor comparison for the new production pattern.

8. **The SW audit is not independent enough.** The NumPy SW recurrence is compared with a rational implementation of the same BCH/SW algorithm. The production preflight's SW-vs-fit comparison is one-face (`dim(P)=1`), so it does not test the multidimensional physical cluster problem. v10a.25's disconnected-spectator additivity firewall is absent.

9. **The final rest equality is again forced.** The notebook sets a diagonal local shift from `M4_ORACLE - ax_rest` before gating equality with `M4_ORACLE`. Historical fourth-order constants and the 189-record count then participate in branch selection; neither belongs in the canonical production result.

10. **The new tail is largely CPU work.** Basis construction, Haar collapse, cache work, checkpoint serialization, and per-shape rebuilds use CPU NumPy/SciPy/opt-einsum paths. The A100 does not automatically solve the dominant new workload. The million-entry cache and repeated whole-cache pickle rewrites further weaken feasibility.

### Disposition

Quarantine the entire Factor52 tail. Do not migrate the `(5,2)/(2,5)` invariant basis, floating finite-cluster SW result, or checkpoint. The supplied v25 traceback shows that this pattern is reached only after the finite-cluster builder constructs the O4-forbidden `W22`/`Q2->Q2` block; v26 entrenches that wrong block instead of removing it.

## v10a.24c Section-15 reduced benchmark

### What it actually is

This file copies the earlier no-watchdog production source through logical line 7240, then replaces the real Section-15 census/unblind tail with a reduced runner. It evaluates only:

- one rooted one-face cluster, with hard-coded known coefficients; and
- one adjacent two-face cluster, with internal fit-stability, Hermiticity, and P-Gram checks.

It does not run the remaining rooted shapes, duplicate-class checks, rooted incidence transform, `m1`-`m3` recovery, `m4` oracle, unblind comparison, scalar shift, 189-record test, or final dual-oracle verdict.

### Critical defects

1. **It is a smoke test, not Section-15 validation.** The two-face case has no independent expected coefficient. Passing means only that two fits agree within a loose window and internal matrices look numerically well behaved.

2. **It does not prove A100 feasibility.** CUDA is optional, CPU fallback may still reach “GO,” and there is no performance threshold. Only batched eigensolves use CuPy; most Haar and basis work remains on CPU.

3. **The advertised hot-path firewall is not enforced.** The notebook prints that the bulk/dense path is forbidden, but no assertion requires a 432x432 block or a `(4,1)` signature to occur. A `(4,1)` representative deliberately calls the dense `_qcache` reference.

4. **Its strict factor engine omits `(5,2)/(2,5)`.** The later supplied v25 transcript now proves where the hard stop occurs: the new finite-cluster builder applies `W` to Q2 and constructs `W22`, even though the inherited O4 code says that block first enters one order later. The hard stop is therefore detecting an upstream order violation, not a missing O4 tensor.

5. **“GO” is too broad.** Even a completed PASS would justify only further benchmark work. It cannot authorize the full fourth-order census or any mathematical promotion.

### Disposition

Retain only as a narrow development smoke test after renaming it accordingly. It is not a failed or successful production run and cannot support the fourth-order claim.

## What is suspicious—and what is not proved

### Supported by the files

- Activity has been reported in a form that is not auditable as execution.
- Copy-forward source generation has been mistaken for experimental progress.
- Certificate language is materially stronger than the implemented gates.
- Some pass conditions exclude prior failures, while other checks prove values created by the same construction.
- Version and duplicate filenames obscure artifact identity.

### Not supported by the files

- deliberate sabotage;
- fabricated stdout or altered numerical results (there is no stdout to inspect);
- a coordinated attempt by agents to prevent progress;
- the exact runtime failure of any attempted A100 session.

The correct immediate conclusion is **process failure with misleading assurance**, not a finding of malicious intent.

## Stop-the-line recovery path

### 0. Evidence freeze

- Classify all five attachments as `source-only / unexecuted evidence`.
- Keep the two duplicate aliases only in an identity ledger; do not count them as attempts.
- Keep SU(3) fourth order `audit-pending`.
- Do not create v10a.27 or another monolithic notebook.

### 1. Replace notebook delivery with an execution contract

Every submitted attempt must contain:

- source SHA-256 and version-control revision;
- exact effective configuration and corpus identifier;
- environment/dependency lock, backend, precision, seed, device, and wall time;
- start and terminal timestamps/status;
- structured required-gate results, with failure/NaN/skip immediately nonzero and terminal;
- immutable outputs and their hashes;
- a separate human-readable log;
- checkpoints signed by source/config/environment/corpus hashes.

A notebook with null execution and no outputs is a source proposal, never a run.

### 2. Extract only what the one path needs

- start from the executed v10a2 physical-Q frontier;
- repair the v10a3 typed block-key defect;
- retain the Section-15 pair-collapse idea only as an optimization inside the one exact Haar contractor;
- reject the v10a26 `(5,2)/(2,5)` invariant basis and statically forbid `W22`/`Q2->Q2` at O4;
- use one exact rational canonical Hermitian SW/BCH implementation based on the physical-PVP/fold specification.

Reject the v10a25 Gelfand recurrence, v10a26 floating finite-cluster result, fitted cluster path, rooted adjudicator, and dual-oracle branch. Do not carry forward the 7,000-line historical prelude.

### 3. Close prerequisites inside that path

- enumerate actual canonical O4 local occurrence patterns before finalizing the one Haar contractor;
- enforce the fourth-order `p+q<=6` ceiling and require `(2,5)/(5,2)` to stop with complete state/layer/link provenance; never add a projector for it;
- run fixed exact multidimensional, noncommuting fixtures against the one SW/BCH implementation;
- add a leakage/closure gate for P+Q1+Q2;
- make every required gate raise immediately;
- remove the one-/two-face GO benchmark from promotion criteria.

### 4. Compute fourth order once

The single runner proceeds sequentially:

1. exact P/Q1/Q2;
2. exact physical `PVP` and canonical SW/BCH fold;
3. exactly 3,895 canonical topology amplitudes, including the missing 2,417 folded cases;
4. one unshifted 189-record H4 kernel;
5. normalization, outward-interval, and Gamma gates;
6. sealed pre-unblind manifest;
7. one Hamer/historical comparison and one claim decision.

There is no finite-cluster scalar, alternate kernel, reconciliation step, or target-derived scalar shift.

### 5. Promotion rule

Promote no fourth-order claim until the single content-addressed chain completes from a fresh process. A missing record, failed gate, skipped gate, NaN, stale checkpoint, absent output, or hash discontinuity terminates that run and keeps the claim audit-pending.

## Immediate next decision

The shortest defensible next task is not another full A100 run. It is the single-runner implementation plan followed by an order-aware physical P/Q1/Q2 occurrence census. `W22` and v10a26 Factor52 are excluded before that census begins; no benchmark or alternate solver may add them back.

The broader unified architecture and six-gate exit criteria remain in `03-unified-proposal.md`; these new attachments do not change that critical path.
