# 14. A manuscript that cites this repository enters as pinned evidence

Date: 2026-08-28. Status: accepted.

## Context

The program produced its first outward-facing manuscript: *Homological flat
bands in strongly coupled SU(N) Hamiltonian lattice gauge theory*, 28 August
2026. It is unlike anything the repository already had a home for.

It is not `theory/`: that is the received corpus, immutable evidence of what
someone believed, pinned so a check can cite a section. It is not `literature/`
either, and the difference matters. `literature/` exists for work produced
*without knowledge of this program*, which is exactly why agreement with it
counts as evidence rather than bookkeeping. A manuscript written from this
corpus is the opposite case: agreement with it is bookkeeping, and the only
useful question is whether each displayed line is checked.

It also makes two claims that are unusual in being claims *about this
repository*, both machine-checkable, neither with anywhere to live:

- §9 pins commit `ca3d440a7f93c17569e12d0511847505b6b72c5a` and reports four
  counters for it — 119 exact-rational checks, 29 numerical cross-checks, 349
  repository tests, 28 Lean theorems with no omitted proofs. All four are
  correct at that commit; they were re-measured before anything in this session
  changed them.
- §9 also names a companion, `verify_core.py`, "distributed with the source".
  At the pinned commit it did not exist anywhere in the repository. The
  reproducibility sentence named an artifact that was not there.

And a third, sharper one. §6 says: "no fourth-order band, bandwidth, or derived
higher-order quantity is used in this paper. This is a scientific boundary, not
merely a choice of presentation." That is a claim about a document — and this
repository already owns an instrument that decides claims about documents, the
coefficient-signature scanner behind `workhouse triage`.

## Decision

`paper/` holds the manuscript, byte-pinned by its own `SHA256SUMS` exactly as
`runs/` pins a transcript, with a README carrying a **claim-to-check map**:
every displayed statement and the one-second command that re-establishes it
here. `verify_core.py` lives at the repository root, so §9's printed
`python3 verify_core.py` is true as printed.

Four rules come with it.

1. **The manuscript is T3 like everything else.** Nothing in `paper/` promotes
   anything. Where a displayed statement had no check, the check was written.
2. **The map records its own gaps.** A claim-to-check map that hides what it
   does not cover is worse than none, so `paper/README.md` carries a *What is
   not checked* section naming, among others, the single unproved physical
   input of the whole second-order chain (eq. (18)'s "isotropy").
3. **Where an existing check turned out to be weaker than the displayed
   statement, that is recorded and repaired, not quietly relabelled.**
   Theorem 2 is the case in point: the homology suite carried
   `dim Z_2 = (L^3-1)+3 = L^3+2` as a checked claim, but both of its checks
   were arithmetic on the formula — one simplified `(L**3-1)+3 - (L**3+2)` to
   zero, the other evaluated the same formula at L = 3, 4, 5. Neither ever
   built a boundary map. Both stay (a Lean theorem promotes the first), and the
   suite now also builds the complex over Z and settles the ranks.
4. **The portable verifier is independent in implementation, not in values.**
   It reimplements the algebra with nothing but `fractions`, which is the point
   — a referee who installs nothing can still run it — but a test joins its
   ledger to `constants.py`, because two verifiers that drift apart certify two
   different papers.

## Consequences

- The evidence vocabulary is unchanged and no tier is added. A manuscript is a
  document; documents are T3; the checks are the checks.
- `paper/` is for manuscripts *this program* writes. External published work
  keeps going to `literature/` under its own rules, and the copyright reason
  that directory never stores third-party PDFs is untouched.
- A future revision is a new pinned artifact plus a regenerated map, in one
  visible diff — the same discipline as re-pinning `theory/`.
- §6's firewall is now a check. If a later revision starts using a fourth-order
  number, `no fourth-order coefficient enters the manuscript` fails, and the
  disagreement surfaces as a failing check rather than as a sentence nobody
  re-read.
