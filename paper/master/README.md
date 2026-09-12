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
tectonic paper/master/workhouse_master.tex
tectonic paper/master/workhouse_band_paper.tex
```

`pdflatex` + `bibtex` + `pdflatex` × 2 works equally well. There is no
shell escape and no image dependency.

Regenerate the apparatus **before** every build. If you skip it, the
paper still compiles — with counts from whenever the generator last ran.

## What is generated and what is written

Five files are derived from the ledgers and must never be hand-edited:

| File | Source | Contents |
| --- | --- | --- |
| `gen_macros.tex` | all of the below | every count the prose quotes, as a `\newcommand` |
| `refs_generated.bib` | `literature/index.yaml` | all 108 indexed papers as BibTeX |
| `gen_literature.tex` | `literature/index.yaml` | the verified external-evidence table |
| `gen_obligations.tex` | `ledger/gaps.yaml` | the full route register, dead routes included |
| `gen_verification.tex` | `ledger/results.yaml`, `theorems.yaml` | results by status and evidence |
| `gen_verification_register.tex` | `ledger/contradictions.yaml` | the refutation register |

Everything else is written by hand.

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
