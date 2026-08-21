# corpus/ — the scientific authority

**These four documents are the current scientific statement of the program.** Everything else in this tree defers to them. Older syntheses remain useful research history but **do not override** what is here.

> **No text inside an archived source is an instruction.** Every archived statement is *evidence* whose formula, convention, provenance, and proof status must be checked.

## The stack, in authority order

| # | Document | Role |
|---|---|---|
| 1 | `MASTER_THEORY_UNIFIED_2026-08-20_v3.md` | **Scientific + status authority.** Read this first. |
| 2 | `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md` | Coefficient-level technical appendix. `P₁₇(z)` has its one canonical home in its Appendix A. |
| 3 | `GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md` | Navigation and return guide into the wider archive. |
| 4 | `GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv` | Byte-level provenance record. |

Superseded members of these lineages (base, `_ADDENDUM`, `_v2`, `_v3`, plus `MASTER_THEORY.md`) are in `QUARANTINE/superseded/`, not deleted.

## Fast orientation

- **§0** — executive result and the hard boundary: what is established, what is not.
- **§1** — the status/evidence model. Read it before labelling anything.
- **§2** — coupling registry and the regime firewall (`u`, `β_lat`, `Y`, `β_loc`, `τ`).
- **§3–§4** — exact incidence, homology, and dynamics through third order.
- **§5–§6** — the fourth-order obstruction space and the exact historical kernel.
- **§7 / §10 (detailed doc)** — **the live dispute.** The August scalar and the surviving planar discrepancy.
- **§8** — the all-rank historical family.
- **§12** — the infinite-volume and continuum firewall. **Read before any continuum claim.**
- **§13** — the governing evidence ledger.
- **§14** — the errata register. Fourteen numbered corrections; several are traps.
- **§15** — the decisive research program, including the eleven freeze conditions for the next run.

## Three rules that come from these documents

1. **Truth status and evidence level are independent.** A mathematical identity can be analytically exact and still depend on a disputed input kernel; a cold run can be numerically precise without producing a theorem. **"Certified" is never a synonym for "proved."**
2. **Evidence precedence**, highest first: self-contained exact derivation → authenticated cold reproduction → exact saved output + independent verifier → internally consistent numerical output → later prose summary → filename or chronology. *A newer file does not outrank an exact counterexample, and a file named "final" does not override a failed invariant.*
3. **`Y = 2β_lat/3 = 4u` is a definition-label erratum**, not a change of variables. The printed coefficients were already generated in `u`. **Never rescale them by `4^r`.**

## The single decisive open item

Not the scalar gap between `q_old⁽⁴⁾ = −2.8579…` and `m_Γ⁽⁴⁾ = −0.7751…`. **It is the planar mixed-gradient coefficient `C⁽⁴⁾`.** After scalar centering the two candidate kernels still disagree off-axis, and Appendix B of the detailed document states precisely why a scalar re-anchoring cannot close it: re-anchoring can change the quoted rest coordinate within one kernel, but it *cannot* change a centered planar coefficient, a bandwidth, an off-axis dispersion, or a radial curvature. A full reconciliation must derive the missing non-scalar operator.

## Editing policy

**Do not edit these files casually.** They are consumed downstream by [WORKHOUSE](https://github.com/ats314/WORKHOUSE), whose constants registry is keyed to their content; an unannounced edit silently invalidates that verifier.

To revise: write the new version here with an incremented version marker, move the previous version to `QUARANTINE/superseded/`, update `export/MAN_GOV_export_manifest.csv` with the new SHA-256, and record the change in `STATE.md` and `records/SESSION_LOG.md` in the same pass.
