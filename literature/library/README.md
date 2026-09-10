# The maintainer's paper library — an acquisition catalogue, not evidence

The counts, overlap checks, and statements of absence below describe the
**2026-08-21 intake snapshot**. For current coverage, use the
[literature register](../index.yaml), [literature guide](../README.md), and
[current research](../../docs/current_research.md). Later acquisition and
research may supersede the snapshot's coverage statements.

Maintainer-supplied metadata (2026-08-21) for a 99-PDF open-access research
library held on the maintainer's machine, mapped to this repository's
subjects: `paper_manifest.csv` (machine-readable: DOI, arXiv id, INSPIRE
recid, SHA-256, citation snapshot, topic, stated connection), plus three
human indexes (`LIBRARY_GUIDE.md`, `PAPER_INDEX.md`, `LATEST_2024_2026.md`).

**Nothing in this directory is part of the evidence map.** The evidence map
is `literature/index.yaml`, and a paper enters it one at a time, with
verified metadata and a `bears_on` edge, after the licence gate. This
directory is the shopping catalogue that feeds that process — the same role
`workhouse lit --acquire` plays, with the advantage that every row already
carries a content digest.

Two facts established at intake (2026-08-21):

- The library's copies are **reproducible from source**: fresh downloads of
  spot-checked entries (arXiv `2411.11676v2`; the Drouffe–Zuber Physics
  Reports scan from Zuber's author page) byte-matched the manifest's
  recorded SHA-256 exactly. The manifest digest can therefore stand in for
  the file: nothing needs bulk-copying into this repository, and no PDF is
  committed here.
- 11 of the 99 were already in `index.yaml` (9 full entries plus
  byte-identical Münster 1985; the library also supplies the first full
  copy of the `DZ_1983` stub). The other 88 are candidates, not entries.

The relative `papers/...` links and absent auxiliary Markdown files inside the
human indexes refer to the original local library layout. These received
guides retain their provenance and are not repaired by rewriting pinned bytes.
The committed entry points are [Volume 1's guide](LIBRARY_GUIDE.md),
[paper index](PAPER_INDEX.md), [recent-paper index](LATEST_2024_2026.md),
and [Volume 2](volume2/).

`volume2/` holds the second collection (2026-08-21, same day): 161 further
PDFs discovered by citation-trail crawling from Volume 1's anchors, with a
`discovery_path` column recording which seed's citation graph surfaced each
paper. Verified at intake: zero digest overlap with Volume 1 (the audit is
held as a test), and zero overlap with the papers already in `index.yaml`.
Its distinctive slices: 41 Hamiltonian/gauge-invariant-formulation PDFs
(including a 14-paper Kogut–Susskind trail), 36 effective-string PDFs, the
perturbative-gadget/Feshbach–Schur effective-Hamiltonian line, and compact
localized states / line-graph flat-band papers. Notably absent, verified by
sweep: any Combes–Thomas / Helffer–Sjöstrand material — that territory
remains covered only by the maintainer's own notes archive.
