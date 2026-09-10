# Page-level extraction index

`sources.json` records all 65 works: the Clay seed, its 61 separately identified cited works, and three later geometric sources. All pages of the 27 complete local PDFs (including the seed) and the one two-page preview have been extracted: **777 PDF pages**. The remaining 37 records have no local full text. An acquired earlier version retains the version distinction in the source manifests; it is not silently identified with its journal revision.

`pages.jsonl` records the source hash, extracted-text hash, PDF page number, and line positions of topic matches on every acquired page. It also records candidate theorem/lemma/definition labels on 191 pages. A label can occur in a citation or contain an OCR error. This is a search index; it does not assert 191 pages of verified results.

The complete extracted reading copies are in `literature/inbox/JW_2006/extracted/`, beside the existing ignored source corpus. The versionable index contains locators rather than republishing source text. `scripts/extract_yangmills_pages.py` rebuilds it using the PDF-enabled workspace Python and refuses a source PDF whose hash differs from the acquisition manifest.

Five pages have fewer than 80 extracted characters and remain explicitly flagged: BFS_1980_II page 58, MRS_1993 page 60, MR_1976_CRITICAL page 10, OS_1975 page 26, and OS_SENEOR_1976 page 13. The last four are trailing scan pages; do not infer their contents from the text index. Exact equations from legacy scans must be checked in the PDF.

The manually reconstructed mathematics is kept separately:

- [Ground-state and curvature derivation](../../../docs/derivations/yangmills-weighted-curvature.md)
- [Simon and finite matrix confinement](../../../docs/derivations/yangmills-simon-flat-directions.md)
- [OS spectral and localization derivation](../../../docs/derivations/yangmills-reconstruction.md)

Search `pages.jsonl` for a paper ID and one of `ground_state`, `spectral_gap`, `curvature`, `reconstruction`, `uniform_limits`, `constructive`, or `gauge_geometry`. Follow the page/line locator into the reading copy, then verify equations in the pinned PDF. A new derivation earns a graph certificate only through an actual invariant or Lean theorem.
