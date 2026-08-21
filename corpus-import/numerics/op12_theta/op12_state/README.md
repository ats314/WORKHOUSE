# op12_state — MC checkpoint states + runner outputs

Per (L, β): `state_*.npz` (link configurations + RNG state), `meta_*.json` (job parameters), `results_*.json` (runner's own per-config outputs; `../results/` holds the scan copies). Consumed by `op12_runner.load_job` — do not hand-edit; certificates and ledgers assume these exact states.

**Provenance:** rescued June 12, 2026 from temporary session outputs into the working home (the June-11 run wrote them outside any store — see `records/SESSION_LOG.md`); without these, the stored-state certificates would be documented-but-not-reproducible.
