# Moving-time spectral exclusion with approximate sources

Task: moving-time-gap-20260911. Owner: Codex root. Date: 11 September 2026.
Checkout: `C:/WORKHOUSE/worktrees/moving-time-gap-20260911`, branch
`codex/moving-time-gap-20260911`. Starting HEAD and observed live main were
`7cf8a646521259a34a772d65c8740ef7597f0265`. The four existing untracked
cellular-Hodge files in canonical REPO were preserved outside ownership.

## Target and reviewed inputs

Targets: `DERIV:YANGMILLS_RECONSTRUCTION:R1`,
`DERIV:YANGMILLS_RECONSTRUCTION:R4_R5`,
`RESULT:EXPONENTIAL_SOURCE_TOTALITY`, and `G19`.
Question: can one growing physical observation time per cutoff, approximate
exponential sources and a spectral measure limit give a sharp continuum
support theorem without a quantitative moving-time convergence estimate?

Read the source arguments in reconstruction sections 1 and 4, source-current
SCB5/SCB9, and the preserved matrix carrier measure theorem sections 3.1-3.4.
The [source manifest](../runs/moving_time_gap_2026-09-11/source-manifest.json)
pins reviewed premise and output bytes. The retained
[discovery pair](discovery/moving-time-pair-20260911.json) and
[review](discovery/reviews/2026-09-11-moving-time-source-gap-01f32e.yaml)
distinguish the reading from the new theorem's actual dependencies.

The initial saved [brief](../runs/moving_time_gap_2026-09-11/start.json)
has fingerprint `c9693d1d41062152c86703bc65de5857a2e8071df831eaca777a0d906f4bc4eb`;
saved graph digest `7506c850ca8f9aee03136f73c3671880ac2693fe8821f199a202ca780b2fc5ca`.
Freshness was unknown (new worktree, no local generation record), and execution
was not started. No successful input-manifest provenance existed for it.
The [first fresh attempt](../runs/moving_time_gap_2026-09-11/start-fresh.json)
is explicitly unavailable due to source/inventory mismatch during drafting;
its fingerprint is `63a2c468cce32b939d57fc11edcc384032e2a9d9d83a88ed85c1bc310dc91680`.
This failed attempt is retained, not counted as a pass. Native source/result
validators subsequently returned no errors after registration.

## Result and successor

The [derivation](../docs/derivations/moving-time-spectral-gap.md) proves MT1-MT5:
projected norm control, moving-time vague-limit exclusion, shrinking-source
composition, the optimal power-law rate, and positive-measure sharpness.
For an actual reconstructed total centered family, this supplies the common
limiting gap under its explicitly listed convergence and correlation inputs.
Both registered results remain analytic/T3 in full; four T1 controls cover
only their named symbolic or finite statements. No new Lean source is added.

The open G19 successor is the actual normalized one-time Wilson bound,
nontrivial continuum spectral identification and source totality. Existing
W6, continuum-existence, scale-transport and fixed-spacing G18 scopes remain.

## Ownership and verification

Exact owned paths are recorded in the workstation task register
`navigation/tasks/2026-09-11-moving-time-gap.md`. All source, ledger and
generated-view edits are isolated here. No shared Lean build or exporter
was run. Navigation originals were preserved under the workstation's
`navigation/preserved/2026-09-11-moving-time-gap/` with SHA-256 metadata.

Initial focused results: 4/4 new exact controls and 13/13 adversarial tests
passed. Full verifier reported 596/596. Source/result validators passed.
Ruff and formatting passed; documentation checked 561 links without errors.
Pre-regeneration coverage tests had 61 passes and one expected stale-graph
failure for the new source edge; final regeneration and retest are recorded
below. A passing finite check is not a certificate of the analytic limit.

End snapshot and publication: pending final validation; see appended outcome.

## Completed graph refresh

The first end snapshot, `discovery/moving-time-end-20260911.json`, matched
before the final run-index registration. It remains retained as that stage.
The complete end snapshot is
[moving-time-end-complete-20260911.json](discovery/moving-time-end-complete-20260911.json),
with fingerprint `4d5f2b13a73f8a97954e5201f3cb7d5d091a58e1eb0928cec02f81e78f849f48`
and input digest `a74650c1c21cb9c17dac93b9bc9c18e5b3d3ba66a53b84662d98e057a2f558b2`.
It is a saved, matched briefing: zero checks execute in that request; it
records 596 verdicts. The separate full verifier actually executed 596/596.

Final regeneration invoked the native CLI `index -w`, `frontier --write`,
then `certified --write` sequentially inside the existing
`briefing.cache_observation(briefing.content_manifest(root))` API. The source
byte digest was checked unchanged afterward; the two dependent renderers
reported 1,192 content-identified cache reuses. No cache entries were edited
or manufactured. One earlier frontier render was stopped after the evidence
manifest changed; it is not passing evidence.

The initial full suite had 1,929 passes, four skips, 11 passing subtests and
three integration failures: stale certified/frontier files, and the missing
run index entry. The run directory was fully pinned and added to
`runs/index.yaml`. A subsequent overlapping graph test retained a stale
catalogue in memory; after all writers finished, the same seven affected
test files passed 121/121. Their logs and the earlier failures are retained
in [the validation evidence](moving-time-evidence-20260911/post-refresh-121.txt).
The full stable-suite result and publication observation follow below.

Additional owned path: `runs/index.yaml`; it registers the retained run and
its two result links without asserting that a snapshot proves the theorem.

## Final stable validation

After the last source/run registration and all graph writes completed, the
full native pytest command passed: **1,932 passed, 4 skipped, 11 subtests
passed**, exit 0, in 370.23 seconds. The
[complete output](moving-time-evidence-20260911/stable-full-suite.txt) is retained.
The command was `pytest -q -o addopts=--strict-markers` with a fresh
workspace-local basetemp; `PYTHONPATH` selected this checkout's `src` and
canonical REPO's independent Python runtime was used without installing or
changing environments. Ruff check/format, 561 documentation links, source
and result validators, and the generated proof-map check also passed.
The earlier failures and their corrections remain recorded above.

Publication is the subsequent commit/PR observation; these checks establish
this local source state and do not by themselves assert a remote merge.
