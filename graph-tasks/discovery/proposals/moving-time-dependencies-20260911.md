# Proposed new theorem dependencies

Manual proposal from the reviewed R1/SCB5 pair. Applied by hand to the new
result records in this task's isolated branch, for review through its PR.
No dependency between the two historical statements is proposed.

- `RESULT:MOVING_TIME_SPECTRAL_GAP` depends on
  `DERIV:YANGMILLS_RECONSTRUCTION:R1` for positive spectral domination and
  `RESULT:EXPONENTIAL_SOURCE_TOTALITY` for the normalized exponential tangent.
- `RESULT:SHARP_CUTOFF_SOURCE_GAP_BUDGET` depends on the new moving-time
  theorem. Symbolic rate identities and finite sharpness controls are scoped
  `supported_by` edges, not proofs of measure limits.
- G19 gains an open application route consuming the two proven implications;
  it is not closed by these abstract criteria.

The source statement inventory separately locates MT1-MT5 and records their
actual argument dependencies. Whole-statement Lean coverage remains empty.
