# Search coverage

- Root: C:/WORKHOUSE. Included hidden and ignored files and preserved checkouts. No junction traversal and no Git-object-history search.
- Physical paths listed by rg: 192,937.
- Distinct content records from normal/archive extraction: 15,373; three further oversized payloads have separate streaming receipts.
- Distinct texts keyword-searched: 15,227.
- Distinct contents with keywords: 6,882. This count includes literature, metadata and implementation material; it is not a count of new proofs.
- First-pass archive coverage: 139 distinct ZIP containers, 2,741 listed members. The supplemental archive log separately records the large ZIP (174 members), TAR/GZ/7z/ZST and duplicates.
- Earlier revision formats: .resolved and numbered .resolved revisions, .bak and .before_scope_correction were included in the supplemental pass.
- PDF/DOCX: extracted text was searched; 411 exact-hash prior extractions were reused only after verifying the extraction hash. No OCR claim is made for image-only equations.
- The malformed historical SU2 notebook was recovered by flattening its nested text outputs. Its original bytes were not changed.
- Three compressed data payloads larger than the initial 128 MiB extraction limit were fully streamed: 621,965,034 uncompressed bytes, zero keyword matches. See oversize_stream_scan.json.

The ordinary extraction formats are Markdown, TeX, text, Lean, Python, notebook cells/outputs, JSON/JSONL, YAML, RST, Wolfram/Mathematica text, Sage, R, HTML, XML, CSV, logs, PDF, DOCX, ODT and RTF. Generated indices, prior extraction directories and selected navigation/catalogue copies were inventoried but not repeatedly searched. Binary numerical arrays, images without text, databases, spreadsheets, slides and other unhandled formats remain outside semantic coverage. See physical_inventory.jsonl for per-path selection and scan.py for the exact format set.

## Explicit exclusions and errors

The runtime directory exclusions were: .cache, .git, .graph-state, .ipynb_checkpoints, .lake, .mypy_cache, .pytest_cache, .ruff_cache, .uv-cache, .venv, .workhouse-local, __pycache__, node_modules, site-packages, uv-cache, venv.

rg returned code 2 with 57 traversal error lines, retained in rg-errors.txt. The reported locations are test, cache, temporary and quarantined-test directories. These were not claimed as searched. The scan did not bypass filesystem permissions.

The first pass recorded a large ZIP and malformed notebook as incomplete; both were subsequently searched. Its other extraction errors are eight deliberately invalid PDF test fixtures and one Word owner-lock file. One concurrent worktree SHA256SUMS path disappeared between enumeration and reading. The supplement additionally encountered a deliberately invalid gzip test fixture. These are visible in the original logs; no error record was erased.

The .zst path in the supplement was an empty file when read (SHA-256 of empty content), so its listing had zero members. This is recorded as an empty container, not evidence of recovered mathematics.

## Graph coverage

The initial live comparison used ffff7bb2e67b976ba50fe5cf7184966dd581535f. During the audit GitHub main advanced to bc9da0233ceb72ed76739dc9b892d9c6ca1b50d5; baseline_final and graph_comparison_final.json retain that revision. The 26 added/changed graph rows were inspected in graph_delta.json. They concern the R10 repair and do not register the selected earlier findings.

The local checkout stayed at b9651bea3d772d3968eaddce72f0c6ad316928db. Its saved start/end brief reports freshness matched and identical fingerprint `0607fb6e2e66466e2cb9257f33adfe74e02fa65b743fdafd92df10444cf10f8c`. The brief executed zero checks and recorded 611 saved checks; Lean was not executed. Remote saved graph files are source-pinned snapshots, not a freshly executed graph validation.

Source inventory, substantive mathematical registration, and mathematical verification are recorded separately. All 12 selected source/findings F01-F12 have inventory coverage. F08 also has an existing substantive check, so the missing-registration list contains seven priority candidates plus four supporting candidates.

## Preservation and disk space

All 14 selected original source/certificate hashes were rechecked unchanged. A report save encountered a full C: drive. NTFS compression was applied only to task-generated files in this audit directory; it preserved paths and logical file contents. The command reported 388,683,368 logical bytes stored in 160,642,578 bytes for the files it compressed. The report was then saved successfully. No research source, archive, worktree or duplicate was deleted.
