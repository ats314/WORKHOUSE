# The inbox is not the repository

Working copies of papers land here — dropped by a person from a browser, or
downloaded by `workhouse lit --resolve` from sources that welcome automation
(arXiv, INSPIRE-hosted documents, KEK library scans, OpenAlex locations).

Everything in this directory except this file is **gitignored, and must stay
that way**. Storing a paper is republishing it; a copy you obtained lawfully
for reading grants no right to redistribute. The only files that ever move
from here into the repository are the rare openly-licensed ones, and only
through a curated `fulltext:` entry in `../index.yaml` that `validate()`
checks against the licence gate.

The loop:

```bash
workhouse lit --acquire        # what is worth fetching, ranked, with links
workhouse lit --resolve ID     # try the open sources first, no browser needed
# ...save PDFs here, ideally named <ID>.pdf...
workhouse lit --intake         # identify, hash, and get the pinning advice
```

`--intake` never edits the index. Pinning a digest, flipping an edge to
`verified`, and adding a published-comparisons check are curation — a
judgement recorded in `index.yaml` after the paper is actually read.
