# 6. A corpus file must not be able to load as agent instructions

**Status:** accepted
**Date:** 2026-08-21

## Context

`corpus-import/CLAUDE.md` was a corpus document: 928 files were imported from
upstream's tree, and one of them happened to be named `CLAUDE.md`. Claude Code
loads a directory's `CLAUDE.md` automatically when working with files in that
directory, so upstream prose was arriving as agent instructions.

Three things made this worse than a naming collision.

1. It contradicted the repository's one principle. `CLAUDE.md` at the root says
   no document is authority. A corpus document loading *as* instructions is that
   principle failing at the mechanism level, silently, before the agent reads
   anything.

2. It was out of date in the way that matters. Its "Authority: `corpus/`" line
   names `MASTER_THEORY_UNIFIED_2026-08-20_v3.md` — the document upstream's own
   path index now records as `quarantine_only`, and which this repository moved
   to `theory/superseded/`. An agent would have been directed at the superseded
   stack by a file it never chose to read.

3. It is exactly the failure the corpus's owner warned about: text in older
   documents is not instruction, it is evidence, and some of it is wrong.

## Decision

Corpus evidence may not bear a filename that an agent tool loads automatically.
`corpus-import/CLAUDE.md` is now `corpus-import/UPSTREAM_CLAUDE_MD.md`,
**byte-identical** — SHA-256 `455445fb…d02010` before and after — with only the
name on its manifest line changed. It remains readable, citable, and pinned; it
simply no longer speaks with an authority it was never granted.

`tests/test_corpus_integrity.py` refuses any manifest entry named `CLAUDE.md`,
`AGENTS.md`, `.cursorrules`, or `copilot-instructions.md`.

Manifest membership is the definition of corpus evidence. A repository-authored
`corpus-import/CLAUDE.md` — the one now there, which says not to read the
directory recursively — is deliberately *outside* the pin, and the tests treat
the two categories separately.

## Consequences

- Renaming pinned evidence is normally forbidden. This is the exception, and it
  is narrow: the bytes are unchanged and the hash proves it. Nothing about the
  document's content was edited, which is the rule that actually protects the
  corpus.
- Upstream paths citing `CLAUDE.md` in that tree no longer resolve by name. The
  manifest line and this record carry the mapping.
- A second gap closed alongside it: the integrity test only checked files the
  manifest already listed, so anything *added* to `corpus-import/` escaped the
  pin entirely. A stale `SHA256SUMS.tmp` from a failed generator run — 926
  entries, missing the two filenames beginning with `#` — had been sitting there
  unnoticed. It is removed, and the test now walks the directory.
