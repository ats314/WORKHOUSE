# Evidence, not authority

These documents are the corpus's own statements. They are **pointers to claims**,
not proof of them. A statement here is true in this repository only if something
machine-checkable says so — see the verification tiers in `CLAUDE.md`.

`SHA256SUMS` pins every file. Changing it is a deliberate, reviewed event.

## Current stack (2026-08-20 v4.3)

| File | Role |
|---|---|
| `MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md` | scientific statement, evidence ledger (§13), governing register (§14) |
| `GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md` | coefficient-level appendix — **still current at v3.1**, not superseded by v4.3 |
| `GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md` | navigation |
| `GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv` | provenance |

## governance/

Upstream's own map of the tree this corpus was extracted from. It describes
directories that do **not** exist in this repository; it is here so a path cited
by a corpus document can be resolved to the file it names.

| File | Role |
|---|---|
| `INDEX.md` | upstream tree map and topic router |
| `MAN_GOV_all_theory_local_path_index_v4_3.csv` | upstream path index, with per-file disposition |

## superseded/

Kept, not deleted — earlier checks were run against them and the audit trail
needs them readable.

| File | Superseded by | Why it matters |
|---|---|---|
| `MASTER_THEORY_UNIFIED_2026-08-20_v3.md` | v4.3 | `MAN_GOV_all_theory_local_path_index_v4_3.csv` records it `quarantine_only`. Its §14 register is the first 13 items of v4.3's, byte-identical, plus the item v4.3 renumbered to 23. |
| `GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md` | v4.3 | navigation for the v3 stack |
| `GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv` | v4.3 | provenance for the v3 stack |
| `MASTER_THEORY_UNIFIED_2026-08-20_v2.md` | v3 | 301 lines, **truncated mid-structure at §2.5** |
| `MASTER_THEORY.md` | v4.3 §14 | Its §8 register (C1–C22) is the ancestor of `ledger/contradictions.yaml`. v4.3 §14 is the *governing* 23-item version and controls where they differ; the crosswalk is `ledger/governing_register.yaml`. |

**A known conflict.** `MASTER_THEORY.md` §4.3 writes `F⊗F = 1⊕Adj` and
`F⊗F̄ = Λ²⊕Sym²`. Governing item 3 writes the opposite, and governing item 3 is
correct: the singlet lives in `F⊗F̄` (the invariant `δⁱⱼ`), while `F⊗F` has no
invariant for `N > 2`. Dimensions alone do not separate them — both sum to `N²`.

## What v4.3 changed

Nine register items were **added** (14–22: string signs, sixth-order scope,
registry lag, cap geometry, atomic shell-six source, OP1 enclosure, pentagonal
provenance, the pentagonal Hamiltonian firewall, pentagonal fifth-order scope).
Nothing recorded in v3 was retracted. Items 1–13 are byte-identical; v3's item 14
("Scope") is v4.3's item 23. `ledger/governing_register.yaml` carries all 23 with
their crosswalk to `contradictions.yaml`, and `tests/test_ledger.py` checks that
the transcription is complete.
