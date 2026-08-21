# Evidence, not authority

These documents are the corpus's own statements. They are **pointers to claims**,
not proof of them. A statement here is true in this repository only if something
machine-checkable says so — see the verification tiers in `CLAUDE.md`.

`SHA256SUMS` pins every file. Changing it is a deliberate, reviewed event.

## Current stack (2026-08-20 v3)

| File | Role |
|---|---|
| `MASTER_THEORY_UNIFIED_2026-08-20_v3.md` | scientific statement and status register |
| `GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md` | coefficient-level appendix |
| `GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md` | navigation |
| `GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv` | provenance |

## superseded/

Kept, not deleted — earlier checks were run against them and the audit trail
needs them readable.

| File | Superseded by | Why it matters |
|---|---|---|
| `MASTER_THEORY_UNIFIED_2026-08-20_v2.md` | v3 | 301 lines, **truncated mid-structure at §2.5**. v3 is 1809 lines with the governing register at §14. |
| `MASTER_THEORY.md` | v3 §14 | Its §8 register (C1–C22) is the ancestor of `ledger/contradictions.yaml`. v3 §14 is the *governing* 14-item version and controls where they differ. |

**A known conflict between them.** `MASTER_THEORY.md` §4.3 writes
`F⊗F = 1⊕Adj` and `F⊗F̄ = Λ²⊕Sym²`. v3 governing item 3 writes the opposite,
and v3 is correct: the singlet lives in `F⊗F̄` (the invariant `δⁱⱼ`), while
`F⊗F` has no invariant for `N > 2`. Dimensions alone do not separate them —
both sum to `N²`.
