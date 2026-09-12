# The master edition

Two papers from one source tree. Part I is written so that it extracts
cleanly; the two drivers share every section file, so the editions cannot
drift apart.

| Driver | What it builds |
| --- | --- |
| `workhouse_master.tex` | The full monograph: exact spectral theory, the fixed-spacing construction, and the continuum obligation register. |
| `workhouse_band_paper.tex` | Part I alone, as a standalone paper on the flux-band spectral theory. |

## Build

```bash
python paper/master/generate_apparatus.py
python paper/master/generate_sources.py
tectonic paper/master/workhouse_master.tex
tectonic paper/master/workhouse_band_paper.tex
```

`pdflatex` + `bibtex` + `pdflatex` × 2 works equally well. There is no
shell escape and no image dependency.

### One file, for handing to someone

```bash
python paper/master/assemble_selfcontained.py
```

Flattens each driver's `\input` tree and inlines the compiled `.bbl`,
producing `workhouse_master_selfcontained.tex` (~665 KB) and
`workhouse_band_paper_selfcontained.tex` (~122 KB). Each builds alone in
an empty directory with no `.bib`, no images and no other file.

These are **derived**. The modular sources are the source of truth; edit
those and re-assemble. Build the drivers first so the `.bbl` exists,
otherwise the assembler leaves `\bibliography` in place and says so.

Regenerate both generators **before** every build. If you skip them, the
paper still compiles — with counts from whenever they last ran.

**Delete the intermediates after changing a table.** `longtable` caches
column widths in the `.aux`, keyed by a running table counter. This
document has around seventy longtables, so editing one renumbers the
rest and a warm rebuild applies the wrong stored widths — the symptom is
an overfull box in a table that compiles cleanly on its own. `rm -f
*.aux *.toc *.out *.bbl *.blg` and rebuild before believing an overfull
warning.

## What is generated and what is written

Fourteen files are derived and must never be hand-edited.

From `generate_apparatus.py` — claims, routes, evidence:

| File | Source | Contents |
| --- | --- | --- |
| `gen_macros.tex` | all of the below | every count the prose quotes, as a `\newcommand` |
| `refs_generated.bib` | `literature/index.yaml` | all indexed papers as BibTeX |
| `gen_literature.tex` | `literature/index.yaml` | the verified external-evidence table |
| `gen_obligations.tex` | `ledger/gaps.yaml` | the full route register, dead routes included |
| `gen_verification.tex` | `ledger/results.yaml`, `theorems.yaml` | results by status and evidence |
| `gen_verification_register.tex` | `ledger/contradictions.yaml` | the refutation register |

From `generate_sources.py` — where derivations come from:

| File | Source | Contents |
| --- | --- | --- |
| `gen_srcmacros.tex` | all of the below | source-layer counts |
| `gen_concordance.tex` | `ledger/derivation_statements.yaml` | every `DERIV` → document, SHA-256, line locator |
| `gen_open_statements.tex` | same | the statements that do not close, with what remains |
| `gen_lean.tex` | `ledger/theorems.yaml` + the Lean tree | every theorem → module:line, formalizes/promotes |
| `gen_library.tex` | `literature/library/*/paper_manifest.csv` | the acquired reading library by category |
| `gen_extraction.tex` | `literature/yangmills/extraction/pages.jsonl` | the page-level extraction index |
| `gen_symbols.tex` | `ledger/symbols.yaml` | join keys: canonical name, spellings, code names, values |
| `gen_documents.tex` | `ledger/documents.yaml` | document aliases and their standing |

Everything else is written by hand.

Theorem line numbers in `gen_lean.tex` are recovered by scanning
`lean/**/*.lean`, not transcribed: the dependency export records
qualified names but not positions, and positions are what a reader
needs.

The reason for the split is that a paper about a verification repository
should not be able to misstate the repository. Counts appear in the prose
only as macros, so a stale figure is a rebuild away from correct rather
than a claim nobody notices is wrong.

## Conventions the text depends on

- **Verification badges** `\Tzero` `\Tone` `\Ttwo` `\Tthree` mark machine
  certification, which is independent of mathematical status. A fully
  proved analytic theorem carries `\Tthree` when no single check covers
  the whole statement. Do not "upgrade" a badge to match a result's
  importance.
- **`\gid{...}` and `\gidc{id}{command}`** attach a statement's graph
  identity, so any assertion in the paper can be run through
  `workhouse why`.
- **`\notasserted{...}`** states what a theorem does not say. These
  paragraphs are load-bearing; several exist because an earlier, broader
  version of the claim was refuted.
- The temporal mesh is `\varepsilon`. The planar variable is `\tau`. They
  are unrelated and the distinction is deliberate.

## Adding a section

Add the file, `\input` it in **both** drivers if it belongs to Part I, and
in `workhouse_master.tex` only otherwise. Part I must not reference
anything in Parts II or III; the band paper build will fail with an
undefined reference if it does, which is the intended guard.

## When the science changes

Re-run the generator. Then check three hand-written places that the
generator cannot reach:

1. the numbered Problems in `36_obligations.tex`, which are curated from
   the live routes rather than derived;
2. the six obstructions in `34_breaks.tex`, if one is ever cleared;
3. the two abstracts.

The task record for this edition is
`navigation/tasks/2026-09-12-master-paper.md`.
