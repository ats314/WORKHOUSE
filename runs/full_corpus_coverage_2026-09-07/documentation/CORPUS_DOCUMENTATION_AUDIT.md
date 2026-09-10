# Corpus ingestion and review evidence audit

Date: 2026-09-07. Read-only source inspection; outputs confined to this directory. The parent supplied the 58,119-file census and the completed 7,046-row archive-member inventory. Its 187 explicitly skipped infrastructure subtrees limit any inference of absence. This audit did not scan other drives or certify the mathematics of the entire collection.

The repository has strong provenance for a selected imported corpus and for later result packages. The available documentation does **not** establish that all of `C:/WORKHOUSE` has been ingested or mathematically considered. Several historical scope claims are inconsistent, and the more careful source and review records explicitly identify unfinished intake.

## Declared scope versus demonstrated coverage

| Record | What it actually demonstrates | Boundary or correction |
|---|---|---|
| Root `README.md`, March 29, especially lines 103–124 | A copied `ORGANIZED/` collection, with 1,313 reported files and pointers to omitted large stores. | It is a historical organizational snapshot, not a current census of this root. |
| Root `GAP_ANALYSIS.md`, lines 6, 35–81 | A different 1,514-file snapshot and named research categories still in original locations. | GPT Masters, second-pass intake, useful organized documents, experiments, and authoring stores were not thereby reviewed or excluded as useless. |
| Root `EXCLUDED_FILES_MANIFEST.md`, lines 4, 15–19, 60–78, 103–106 | Reasons for excluding caches, vendor trees, conversation files and other categories from the organized copy. | “Zero content files excluded” conflicts with the listed conversation exports and with `GAP_ANALYSIS.md`. “Every file reviewed” has no per-file review evidence here. Its ~6,377 organized-file figure differs from both other snapshots. Binary, large, or monolithic does not mean scientifically empty. |
| Root `CROSS_REFERENCE.md` | Exactly 195 pairs of organized path and source path. | 193 destination files exist after stripping the relocated `ORGANIZED/` prefix; none exists at the literal prefixed path. No hashes or review outcomes are stored. This cannot map every file in a 1,313/1,514/6,377-file collection. |
| `ALL THEORY/SOURCES.md`, lines 3–50 | Explicit map from a **distilled working set** to much wider stores; dated MD5 recovery/survey claims. | It does not claim the working set contains everything. External-drive paths are unresolved external provenance unless the census finds a local hash-equivalent copy. Its authoring-store survey explicitly left 237 unmatched notebook candidates for further identification. |
| `ALL THEORY/README.md`, lines 13–23, 31–39, 54–56 | August authority stack, typed directories, export path and recorded reorganization. | Its unresolved C2 language and 836-file count are historical; September resolution must continue to control current status. `archive`, `QUARANTINE`, or a “superseded” label does not make source content disposable. |
| `docs/decisions/0016-the-whole-corpus-is-in-the-graph.md`, lines 7, 22–37 | Every file pinned by the imported corpus's `SHA256SUMS` is represented as a T3 corpus node, with exact-rational carrier edges where found. | “Whole corpus” here means the specified 928-file import, not all root folders, later loose bundles, archives, or conversation exports. Graph membership is neither semantic review nor proof acceptance. |
| `ledger/provenance.yaml` introduction and ADR0009 | Curated originating documents, pinned bytes, observed quotations near specified lines, targets and stated meaning. | This is meaningful claim provenance. Tests verify the quotation/path/target, not the truth of the quoted claim or exhaustive corpus coverage. |

## Existing machine-readable mappings

The accompanying `MANIFEST_EVIDENCE.json` and reproducible `inspect_manifests.py` record these comparisons against the parent's fixed census.

| Mapping | Actual rows | Existing fields and measured result |
|---|---:|---|
| `ALL THEORY/corpus/GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv` | 148 | `id, tier, target_folder, source_path, role, status, bytes, sha256`; 90 exact digests recovered: 84 among loose census files and six additional archive-only identities. Fifty-eight remain unresolved after both joins. |
| `ALL THEORY/records/MAN_GOV_all_theory_local_path_index_v4_3.csv` | 148 | `id, canonical_path, match_count, original_path, sha256, status`; historical statuses are 60 active, 83 missing, 5 quarantine-only. Twenty-five of those 83 historically missing identities are now recovered: 19 loose-file and six archive-only matches. |
| `ALL THEORY/export/MAN_GOV_export_manifest.csv` | 4 | `file, role, bytes, sha256, md5, frozen_on`; all four digests found. This freezes the four-document authority stack. |
| `ALL THEORY/records/REORG_MANIFEST_2026-08-20.tsv` | 621 | `original_path, new_path, reason, size_bytes, md5`; move provenance, not a scientific review checklist. |
| `01_PROOFS/proven/MANIFEST.md` example | 21 declared | Name, extension and rounded size. A useful directory inventory, without content hashes, claim provenance or review records. |

The 58 remaining source-manifest identities have no exact match in either completed inventory. This is an unresolved provenance finding, not proof of mathematical absence: excluded infrastructure or edited/recoded derivatives remain outside that exact-byte inference. The JSON preserves every unresolved ID, historical source path and digest, and gives container/member/hash locators for the six archive recoveries. Recovery does not change the historical scientific verdict attached to a source. No search of external drives was performed.

`src/workhouse/corpus_index.py` is an exact-rational retrieval index. Its supported prose/code extensions, 12 MiB size ceiling, directory exclusions and notebook-source-only handling are explicit. It does not parse PDF/DOCX/ZIP/image contents, notebook outputs or `.lean` through this scanner; it does not extract arbitrary symbolic formulas or record that a reader understood them. These are limitations of this particular retrieval surface, not evidence those formats are useless or lack separate repository tooling.

`ledger/documents.yaml` records citation aliases, title/path, standing, documentary citations, notes and explicit unresolved referents. `ledger/provenance.yaml` adds source hash, role, origin meaning and observed claim locators. Neither is a complete per-file ingestion and semantic-review ledger for the whole root.

## What counts as consideration

There is substantive historical review evidence worth preserving:

- `ALL THEORY/records/review/REVIEW_PROTOCOL.md` requires read-versus-skim scope, claims with stated status, live-problem connections, findings and a deposited conclusion. This is a proposed review procedure, not evidence every unit completed it.
- `records/review/findings/F001_scalar_cluster_recovery_core.md`, lines 3 onward, records exactly which documents/chapters were read, which remained unread, specific mechanism connections and limitations on January numerical or percentage claims.
- `records/review/findings/F023_simulations_store_survey.md` distinguishes a 199-byte stub from the real 12,987-byte CW extractor, with MD5-backed recovery and explicitly **unrun, unverified** status. This is a concrete reason never to deduplicate mathematical files by name alone.
- `records/review/REVIEW_LEDGER.md`, introduction, admits truncation, reconstructed descriptions, unrecovered units 38–44 and unidentified historical SKIP rows. DONE-plus-SKIP counts must not be reported as the number of fully read or mathematically accepted documents.
- `10_ALREADY_REVIEWED/README.md` says files were previously flagged as reviewed, but supplies no per-document findings or reviewer/test linkage. The folder name alone is not sufficient evidence of review scope or validity.

A completed reconciliation should separately store: **file identified; exact bytes preserved; content extracted with method/version and limitations; duplicate/variant lineage resolved; semantically reviewed sections; mathematical finding and scope; graph/claim consequences; remaining work**. These statuses should not collapse into one “ingested” flag.

## Exclusion and quarantine recommendations

No mathematical source inspected in this audit was established to be useless. Failed and superseded arguments can retain indispensable definitions, counterexamples and provenance.

Generated caches and unmodified vendor/build trees can reasonably be excluded from the primary mathematical reading queue if their versions, restoration route and exclusion reason are recorded. Preserve original custom source and dependency/build metadata. Git history may contain deleted derivations; excluding its internal objects from a document copy is reasonable, but does not prove all historical intellectual content was retained. Never copy a known credential file into the research corpus; record its exclusion without exposing its contents.

Large conversation JSON/HTML, protobuf records, notebook outputs, PDFs, and compressed bundles need extraction or an explicit unresolved-access status. Size or format alone does not support “no content.” No proposal here expands the task to other drives.

Four narrow duplicate candidates are listed in `MANIFEST_EVIDENCE.json`: same-folder `- Copy.tex` files in `10_ALREADY_REVIEWED/tex` whose SHA-256 equals the corresponding retained non-Copy edition. These are candidates to move **only after the parent verifies retention and references**, not declarations that the mathematics is useless. A bounded exact-name search found no references in root `CROSS_REFERENCE.md`, `README.md`, `GAP_ANALYSIS.md`, or `10_ALREADY_REVIEWED/MANIFEST.md`; this is not a complete incoming-reference audit. This agent moved nothing.

## Next actionable reconciliation

The disk-plus-archive reconciliation is complete for these manifests: append the 25 recovered historical missing mappings and retain the 58 unresolved byte identities. Review unique research families through the historical findings and current G19/G23 dependencies, recording full/partial reading and actual mathematical conclusions. Keep current C2, symbolic all-rank and G18 results intact while treating older conflicting status language as historical. The bounded `SYNTH_COPY` pass is recorded separately in `SYNTH_COPY_REVIEW.md`; its exact read and unread ranges are machine-readable.
