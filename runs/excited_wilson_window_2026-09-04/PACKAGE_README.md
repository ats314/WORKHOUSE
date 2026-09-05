# Excited Wilson window: operator-level continuation

Read `EXCITED_WINDOW_OPERATOR_BRIDGE.md` first.

**Established by the arguments in this delivery:** an optimal guaranteed free
spectral block; actual cutoff-free finite-volume Wilson shell/source
completeness with an epsilon-uniform but volume-dependent coupling domain;
a volume-independent full-operator FIRST derivative after explicit local
vacuum rotation; general operator-activity and full-complement sufficient
criteria; source-moment leakage identities.

**Not established:** the required all-orders Wilson operator-activity bound,
thermodynamic complete Wilson band, spatially weighted sharp-shell matching,
or any continuum result. The abstract criteria are not claimed as verified
physical hypotheses. The prior vacuum/source-correlation arguments remain
upstream premises, not independently recertified here.

## Replay

```bash
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python verify_excited_window.py --output replay.json
```

The supplied execution passed 33 tests. Exact algebra tests are distinguished
from floating-point finite-model diagnostics. This is not a Lean proof and
not full WORKHOUSE CI. The SU(3) diagnostic uses a single closed plaquette
with 21 character states, nine of them odd. Its complement test includes all
nine retained odd states but does not bound states outside the truncation.

The mathematical finite-volume theorem is separate and does not use that
truncation or its numerical outputs.

`WILSON_EXCITED_OPERATOR_INSERT.tex` is an additive research insert; it is not
a revised paper and is not automatically imported into the repository.
`graph_proposal.json` stages the dependency structure without changing G18/G19.
`prior/` retains the exact reused primitive and previous note. No repository
push, pull request, merge, or native status change was performed.
