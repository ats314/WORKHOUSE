# An evidence map, not a bibliography

An entry earns its place by naming a target accepted by the current claim
registry and validator, and saying what relationship the
paper has to it. `ledger.validate`'s counterpart here rejects a target that does
not resolve, because a citation attached to no claim is decoration.

```bash
workhouse lit                 # the whole map, with both relevance weights
workhouse lit --for C7        # what published work bears on one claim
workhouse lit --holes         # the missing-link report over bears_on x cites
```

## A published paper is not authority either

Literature relationships retain their recorded source-reading status and
scope. A mathematical result's status and machine tier are separate: an
analytic argument may be established while its complete Lean encoding is
unfinished. Publication alone does not certify it, and unfamiliarity is not
a reason to reject a valid argument.

Use the live register, `workhouse lit`, and the associated invariant/theorem
records to determine what has been read or checked. Do not repeat historical
claims that only one edge was checked or all other papers are unread.
Independence belongs in the provenance: repeated citations or copied source
text are not additional originating arguments.

## Never store a paper you do not have the right to store

`validate()` refuses a `fulltext` path under any licence not in
`REDISTRIBUTABLE` or `VERBATIM_ONLY`. Note what is deliberately *absent*:
`arxiv-assumed-1991-2003`, which covers most pre-2004 arXiv papers. That licence
grants **arXiv** the right to distribute; it grants this repository nothing.

For entries using `VERBATIM_ONLY`, the validator requires `source_sha256` and
compares the stored bytes with that digest. Preserve those copies unchanged.
Inspect the actual source's declared licence and the current entry instead of
inferring permission from download availability or an old stored-paper count.

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

## The citation web binds like everything else

`cites` lists are curated from PRIMARY sources — the INSPIRE reference list of
the entry's `inspire_recid`, or a pinned PDF's own bibliography — never from
memory. Every cited id must resolve to an indexed paper or a `stubs:` entry;
a stub nothing cites is rejected as decoration, and a stub can carry no
`bears_on` — evidence needs a full entry.

Do not record whole reference lists. A citation earns an entry when either
endpoint bears on an indexed claim or it connects two papers already in the
web. Everything else is bibliography for its own sake.

Two relevance weights, never merged: `inspire_citations` is the field's
global count, recorded with `as_of` because an undated count reads as current
forever; the in-web in-degree is computed at generation time and never
stored. A citation edge can rank and connect papers. It can promote nothing.

A hole from `--holes` is a lead, not a claim. Acting on one means reading a
reference list or fixing a `bears_on` conflation — never adding an edge to
make the report quiet.

The web caught its first conflation before it was a day old: Hamer 1989's
"[7] Kogut-Sinclair-Susskind" is the three-author 1976 series paper, not the
two-author KS_1975 this index once pointed the supersession at. Two papers,
one hyphenated name-blur, thirteen years apart. Author counts are data.

## The inbox is not the repository

`inbox/` holds working copies awaiting reading — gitignored except its
README, because storing a paper is republishing it. `workhouse lit --resolve`
downloads only from sources that welcome automation (arXiv, INSPIRE-hosted
documents, KEK library scans, OpenAlex locations); the bot-walled open
archives are `--acquire`'s browser links for a person, and nothing in this
repository may impersonate a browser to defeat a publisher's wall.
`--intake` identifies and hashes what landed and prints the pinning advice;
it never edits the index. Pinning, edge flips, and new checks are curation,
done by hand after the paper is actually read.

## Adding an entry

Verified metadata only. An unverified citation is the same failure mode as an
unverified coefficient — `KS_1975` carries a note because two secondary sources
disagree about its page range, and the ADS bibcode settles it.

Use the existing edge vocabulary: `verified`, `transcription-unverified`,
`not-yet-obtained`, or `refuted`. Keep acquisition and reading distinct. When
the source is available but the specific relationship is unverified, retain
`transcription-unverified` and explain what still needs checking; use
`not-yet-obtained` for a source that has not been obtained. A downloaded file,
an extraction or an abstract is not enough to mark a relationship `verified`.

After a substantive source or relationship change, follow the relevant
validation and graph-generation steps in [Contributing](../CONTRIBUTING.md).
For navigation-only edits, use [documentation maintenance](../docs/documentation_maintenance.md).
