# numerics/certificates/

Machine-emitted JSON certificates from gate runs — the artifacts that back numerical claims in the documents.

Notable: `CERT_Y5_su3_m5_certificate.json`, `CERT_SU4_hybrid_certificate_v2.json`, `CERT_SU6_determinant_certificate.json`, `CERT_SHELL6_o2_exact_channel_certificate_v2.json`, `CERT_SHELL6_shell46_t1_coupling_certificate_v1.json`, `CERT_SUN_closed_surface_stage1_certificate.json`, `CERT_SU3_edge_tensor_certificate.json`, plus the `m5_*`, `lemma_b_*`, `d3_*` and `sigma5_m6_attempt` certificates.

**A certificate is not a proof.** On the corpus evidence scale (§1.2) a certificate is `Output-certified` — exact saved outputs plus an independent verifier agree, but the full upstream generator was not necessarily re-run atomically. Only a self-contained exact derivation or an authenticated cold reproduction outranks it. Never write "certified" where you mean "proved".

A certificate that is not bound to source and input hashes is weaker still. `CERT_O4_next14.json` is the cautionary case: it reports 23/23 gates passing, but one "physical zero-momentum carrier" gate is a **literal truth value in the source** rather than a computed test, it is not source-hash bound, and it contains non-RFC `NaN` tokens.
