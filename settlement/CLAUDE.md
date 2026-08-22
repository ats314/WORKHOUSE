# Cold-run evidence

Transcripts and harness code from runs executed outside this repository.
`SHA256SUMS` pins them and they are excluded from formatters — a reformatted
transcript is a corrupted transcript.

Two things to keep straight, because the corpus conflates them:

- **The generating script's hash is not the transcript's hash.** `SOURCE_SHA256`
  inside a transcript hashes a script that is *not in this repository*;
  `SHA256SUMS` here hashes the transcript. Never quote one as the other.
- **"Cold-reproduced" is an evidence level, not a status.** The stranded-flux
  audit is cold-reproduced *and* the claim it tested is falsified. Both are true
  at once (`CLAUDE.md`, non-negotiable 5).

`mce_adjudication_harness.py` is verified upstream through preflight. The
received README records the engine it drives as absent; that is stale — the
corpus-import rename manifest shows it arrived as
`Hodge_SU3_Exact_MarkedCluster_m4_Colab.py` and now sits at
`corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py`
(the received README is pinned evidence: correct the record here, never there).
The engine passes `freeze` in this repository — self-test 47/47, geometry
preflight matching both pinned SHAs — but its `run` stage fail-closes on the
first production cluster: the shipped H0-closure cap (`max_states=100`) is
exceeded during the R2 stage of even a single-face cluster, and no
pre-production path (self-test, preflight, upstream sandbox) ever exercised
that guard at production size. See `runs/` for the transcript and G3 in
`ledger/gaps.yaml` for the standing. That failure, not hardware, is what G3
is blocked on.
