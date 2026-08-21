# F007 — PMBSF paper lines vs publication bundle (#34)

**Date:** June 12, 2026. Bundle manifest (3 items, May 26) verified complete in `13_PMBSF/`; already superseded in-folder by later merges. Pointer READMEs added: `THEORY/papers/pmbsf_su2/`, `papers/pmbsf_su3/`.

## Version genealogy

**SU(2):** sections 1–15 → firewall paper v1 (May 25) → v2 (+LCI exactHB) → v3_start → v3.3 unified core → **v3.4-merged (May 26, 1,142 lines — current)**. **SU(3):** class-function gap paper v1 → v1.1 + sections/extended drafts + DERIVATION_HEAVY_FINAL.tex → **MERGED_DRAFT 2026-05-30 (1,486 lines — newest dated research document in the corpus)**.

## Material refinement found (updates M3a's precise form)

v3.4's changelog: the conditional architecture was *sharpened* from three inputs to **two open analytic theorems plus one deterministic auxiliary** — "Lemma Q is now a derived consequence of TOS+J via two formally-proved chain pieces (Propositions Z.1 + Z.2 of the master), not an axiom of the conditional theorem stack." Open content = **Theorem Z.A (LCI typicality) + Theorem Z.B (Bałaban far-source stability)**; boundary-band gate is deterministic auxiliary. ⇒ **M3a's canonical target is (Z.A, Z.B)**, with Lemma Q and the pass-10 covariance bound downstream of them. STATE and the translation note updated accordingly; DECISIONS #007 unchanged in substance (the canonical *formulation* is still the PMBSF stack — now at its sharper two-theorem form).

## SU(3) line's own honesty register (noted)

The May-30 merged draft separates a "rigorous core" (local spectral computation) from a "conditional polymer/firewall layer", and **corrects its own older draft**: the polymer threshold is finite-channel only — the radial Laguerre tower is not automatically a compact perturbation (off-diagonal growth ~n² vs one shell denominator; Schur symmetrisation gives boundedness, not tail-compactness); a full-channel theorem needs new input. Failure-mode candour consistent with the program's culture; this finite-channel caveat should be quoted whenever the SU(3) threshold is cited.

## Actionables
- M3a statement in STATE now reads (Z.A, Z.B). Translation note gains one line (Lemma Q derived, not axiomatic).
- Unit #35 (notebooks/PDF identification) remains the open PMBSF review unit.
- When the flat-band paper's companion-manuscript question recurs: the PMBSF SU(3) one-plaquette class-spectrum merge (May 30) is the closest thing to a companion-manuscript successor in store — candidate home for the §6 patch if the original source TeX never surfaces (Alex to confirm).
