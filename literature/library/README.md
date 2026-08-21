# The maintainer's paper library — an acquisition catalogue, not evidence

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

The relative `papers/...` links inside the human indexes refer to the
maintainer's local library layout, not to paths in this repository.
