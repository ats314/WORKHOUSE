# Archive intake and provenance review, 2026-09-07

The latest two supplied ZIPs are completely imported. The larger corpus was
not fully unpacked: this census recovered **1,476 distinct member byte streams**
that had no identical loose-file hash in the parent's starting census. This is
a concrete retrieval gap, not a count of newly established mathematical results.

## Scope and reproducible artifacts

`audit_archives.py` consumes `../snapshot_before/files.jsonl` (SHA256
`4977e0e0ab719f62fa9d1f865f673caa44f40ee2543ee3c1baa31cba19c88f4a`).
It read 361 archive paths, representing 217 distinct outer byte streams and
248 containers after recursive nesting. This includes ZIP, TAR, compressed TAR,
single-stream GZIP and the 7z atlas; additional `.tgz`, `.xz` and `.whl` paths
explain the difference from a ZIP/TAR/GZ/7z-only count. There were 241 fully read
containers and seven explicitly recorded runtime/dependency exclusions. No
unsupported container, read error, encrypted unreadable member, unsafe member
path, duplicate member name or unresolved link was encountered.

`members.jsonl` has 7,046 member occurrences, of which 6,625 are hashed files.
Each row preserves the outer container, its hash, every nested ancestor, the
member name and hash, loose-file matches, and the separate set of matches in
tracked repository files. Ignored repository outputs are never counted as
tracked intake. Office documents and NPZ arrays are hashed leaves here; their
internal representation is a separate document/data extraction concern.

All 1,476 absent hashes are materialized and rehashed under `objects/`, totaling
2,348,284,573 bytes. `archive_only_content.json` maps each to all source locations;
`objects_census.jsonl` supplies the root extractor's schema. No archive member
path was extracted into the originals. For 7z, Windows bsdtar 3.8.4 copied the
archive into a temporary TAR byte stream, then Python read its members.

The archive and object ledgers do not claim these files have been mathematically
reviewed. In particular, large JSON/TSV/data members and stored notebook outputs
are evidence to inspect, not a rerun. The separate `archive_extraction/` result
records extracted text, unsupported representations and any errors without
promoting content to proved status.

The final member inventory is `archive_extraction/content_complete.jsonl`,
with eligibility in `classifications_complete.jsonl`. It contains 1,454 eligible
objects after 22 exclusions: 15 bytecode files, six TeX auxiliaries and one
original `.env.local` configuration. Original member names were checked as well
as content-addressed paths so that renaming could not bypass that exclusion.
Its values were not displayed or added to the text index.

Final extraction comprises 1,216 full-text records, 63 image-header records,
136 numeric-array-header records, five pickle-opcode records and 31 nested
containers already covered by the recursive archive census. There are zero
extraction errors and three explicitly unsupported scientific binary streams:
`Y6_FEASIBLE_MEMBERSHIP.bin`, `Y6_CLASS_ENERGY_SPECTRA.bin` and
`y5_connected_supports.bin`. Their complete bytes and provenance are preserved.
Text totals 1,644,754,912 characters because large exact JSON, TSV and NDJSON
datasets were not capped. The PDF pass covered 8,590 pages; five PDFs are flagged
for visual/OCR follow-up. No visual proof check is claimed. Earlier extraction
snapshots remain available and are superseded only by the named complete pair.

## Latest user ZIPs: no missing member

`LATEST_ZIP_INTAKE.json` freshly verifies the root ZIP hashes, every original
member hash, the existing import map, destination bytes and Git tracking:

| Root input | Members | Current intake |
|---|---:|---|
| `workhouse_discrete_time_20260904.zip` | 13 | All 13 byte-identical and tracked |
| `workhouse_excited_window_operator_bridge.zip` | 14 | All 14 byte-identical and tracked |

Their original SHA256 values are respectively
`7c3709c0b398eefac3207e9cb8c3e6bc45a6eaebd85af1e711f2701e2898279c`
and `3fc9447a6120b93e45114da8f7b04cf150ea71ae20b8730265dce9ffaff70d14`.
Their run directories are `runs/discrete_time_wilson_2026-09-04` and
`runs/excited_wilson_window_2026-09-04`. Original notes moved into
`paper/research_notes/` are included in these exact checks, as are renamed
package READMEs and checksum files. There are no unmapped or absent entries.

The excited package deliberately carries byte-identical prior copies of the
discrete-time note, certificate and `wilson_clock.py`; shared numerical code is
declared as reused in its source manifest. That is provenance, not independent
verification. The received `graph_proposal.json` files and their historical
open-status statements remain preserved package records. Later graph routes
must be consulted for current status; rewriting old package bytes would break
their provenance.

## Recovered research and reference content

The archive-only set contains, among other formats, 181 Markdown, nine TeX,
five Lean, 155 Python, 370 JSON and 265 PDF byte streams. Some are external
software or literature, some are historical WORKHOUSE versions, and some are
original experimental data. File extensions and words such as `FINAL` do not
decide scientific authority.

Concrete recoveries include the nested denominator-checker implementation
packet, its rank-three/order-four bound and witness files, early integrated
master/review documents inside `YM_FINAL_COMPLETE_PACKAGE.zip`, exact-run data
inside Y5/Y6 bundles, and distinct publication-edition releases. The five Lean
files were read fully in `RECOVERED_LEAN_REVIEW.md/.json`; their scope is exact
arithmetic infrastructure, with external physics hypotheses retained.

Two `o4/WORKHOUSE_research_library*.zip` files contain **99 and 161 external
papers**. Every PDF matches its library manifest hash; no unmanifested PDF was
found. Across the two downloaded-paper lists there is zero overlap by exact
hash, normalized title, recorded DOI or recorded arXiv ID. There are 86 and 160
papers respectively with no unpacked copy in the starting census, and nine and
zero with an identical tracked-repository copy. Thus **246 of the recovered
PDFs are explicitly external references**, not missing original WORKHOUSE
proofs. `REFERENCE_LIBRARY_PROVENANCE.json` and `content_roles.jsonl` preserve
that distinction. Citation counts and publication metadata are archived source
claims, not newly fetched or independently rechecked facts.

## The supplied oscillator PDF and XML

The root `quantumrep-01-00009.pdf` is byte-identical to the tracked
`literature/fulltext/quantumrep-01-00009.pdf`, SHA256
`907d88f5b4e3142c337e26ad8315d3393f51fba4c0423028d5f24d40da2cf210`.
The literature register identifies Urzua et al. (2019), DOI
`10.3390/quantum1010009`, as an external method/comparison source. The associated
WORKHOUSE note records a checked invariant and specific repaired transformation
formulas. It does not treat the source paper as a Wilson or continuum proof.

The 157,523-byte root XML, SHA256
`26d0488b569d08bfd0db56bbef664d89e16a6a7085de6f7dde5ff06590ac7093`,
has matching article title and DOI and the CC BY 4.0 license text. No identical
XML copy appears elsewhere in the starting census. It is a useful structured
representation not currently imported, rather than a missing new theory
version. `ATTACHED_PAPER_PROVENANCE.json` records these checks.

The user-supplied Fermat repository URL was a suggested Lean resource, not an
attachment asserting that its complete code should be imported. Its absence
from these two ZIPs is not an intake defect. The previously supplied GitHub
screen capture is UI evidence rather than mathematical source material.

## Historical exclusion and duplicate claims need narrower interpretation

`C:/WORKHOUSE/EXCLUDED_FILES_MANIFEST.md` describes a March 2026 `YANG/` to
`ORGANIZED/` reorganization. Its assertion that no content was excluded conflicts
with its own exclusions of unique conversation JSON/HTML and protobuf archives.
`DEDUPLICATION_ANALYSIS.md` explicitly lists those as unique content. Large or
non-plain-text material can require another reader; that does not establish
that it contains no provenance or mathematics. Those documents are useful
historical inventories, not a completeness certificate for the present tree.

The current archive census finds **78 exact outer-hash duplicate groups, with
144 excess path occurrences**. `duplicate_archive_bytes.json` proves that
narrow byte redundancy. Existing copies already in `ALL THEORY/QUARANTINE`
remain represented. Removing or moving any path still needs the parent audit's
reference/path policy; this review moved nothing and does not recommend
discarding the last container or a linked source.

In contrast, publication-edition REV4 and REV5 contain 81 and 111 distinct
direct-member hashes, only 25 shared. There are 56 REV4-specific and 86
REV5-specific hashes. They are distinct release snapshots, not removable exact
duplicates. The 7z graph atlas has all 38 direct/nested hashed members represented
on disk, including 24 in tracked repository files; that establishes member-byte
coverage while retaining its packaging/provenance value.

## Available extraction mechanisms and their actual limits

The live `src/workhouse/corpus_index.py` indexes exact rationals in selected
text/code extensions under `corpus-import`, skips `archive`, and imposes a
12 MiB per-file limit. `corpus_registry.py` states that this is untrusted bulk
data. It is a useful exact-number index, not a recursive document-intake engine
or a review of every source. `.gitignore` also intentionally excludes
`corpus-import/archive/` and outputs, whereas sealed runs are unignored.

Historical `07_PIPELINE_TOOLS/extract_pdfs.py` offers pdfplumber and PyMuPDF text
functions but hardcodes an obsolete `c:/Users/ats31/...` source/output pair.
Its batch main writes files there and is not a safe current-tree intake command.
`create_bundles.py` likewise hardcodes the older corpus paths and prints missing
file warnings rather than proving coverage. Neither was executed. The current
bundled Python provides pypdf/pdfplumber; the parent's output-only extractor was
used with the new object census, followed by binary-header and original-member
text recovery. PDF text extraction supplies retrieval,
not a visual or mathematical equation check.

## Concrete next intake work

Join these exact archive locators and role records into the parent's searchable
content inventory. Review the original research candidates against the current
claim graph by content, while retaining external papers as references and old
versions as historical evidence. The latest ZIPs need no re-import. Denominator
Lean candidates need a fresh toolchain build and their precise external ledger
bridge before any new formal-evidence registration. No canonical file, old run,
original archive or Git state was changed in this audit.
