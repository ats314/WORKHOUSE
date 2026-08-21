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

`mce_adjudication_harness.py` is verified upstream through preflight; the `run`
stage is outstanding and needs the production box. That is G3, the single
computation that gates the most downstream theory.
