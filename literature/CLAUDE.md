# An evidence map, not a bibliography

An entry earns its place by naming a claim in this repository — a `C`, `G`,
`R`, or `U` id, or a registered constant — and saying what relationship the
paper has to it. `ledger.validate`'s counterpart here rejects a target that does
not resolve, because a citation attached to no claim is decoration.

```bash
workhouse lit                 # the whole map
workhouse lit --for C7        # what published work bears on one claim
```

## A published paper is not authority either

It is T3 until something checks it, exactly like a corpus document. What makes
an external result valuable is **independence** — it was produced without any
knowledge of this program, so agreement is evidence rather than bookkeeping.

One edge here has been promoted past T3: `CS_2006 → C7`. The SU(3) Weingarten
values that falsified the stranded-flux zero backend are now re-derived
symbolically in `N` from the `n = 2` Gram matrix, so they no longer rest on a
transcript. Everything else is still an assertion about a paper nobody here has
read.

The counter is printed at the bottom of `workhouse lit` on purpose.

## Never store a paper you do not have the right to store

`validate()` refuses a `fulltext` path under any licence not in
`REDISTRIBUTABLE` or `VERBATIM_ONLY`. Note what is deliberately *absent*:
`arxiv-assumed-1991-2003`, which covers most pre-2004 arXiv papers. That licence
grants **arXiv** the right to distribute; it grants this repository nothing.

`VERBATIM_ONLY` holds the NoDerivatives licences. They permit storing the file
and forbid changing it, so an entry using one must record `source_sha256` and
the stored bytes are hashed against it — extracted text, a reformat, or an
excerpt would all be derivatives. One paper qualifies (`KRS_2023`, CC BY-NC-ND);
the rest are pinned by digest and not stored.

## A scope firewall binds

`scope_firewall` is not a caveat, it is a rule. A paper from another regime —
different dimension, different field content — may be compared against and
borrowed from methodologically, and its **numbers may never enter**.
`validate()` rejects any firewalled entry carrying a `supplies-value` edge, and
a test mutates one to confirm the rule fires. This is corpus §12 made
executable.

This matters more than usual here: the repository's own `NOTICE` reserves all
rights over its contents, and a repository that guards its own copyright while
republishing other people's is not one to defend.

## Adding an entry

Verified metadata only. An unverified citation is the same failure mode as an
unverified coefficient — `KS_1975` carries a note because two secondary sources
disagree about its page range, and the ADS bibcode settles it.

If you have not read the paper, the edge status is `not-yet-obtained` and the
`detail` says what you expect to find. That is a useful entry. What is not
useful is an edge marked `verified` because the abstract sounded right.
