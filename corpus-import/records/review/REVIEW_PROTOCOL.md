# REVIEW PROTOCOL — the long pass over 4 years of files

**Purpose (set by Alex, June 12, 2026):** systematically read the entire corpus — thousands of pages, hundreds of iterations — and extract everything that matters into THEORY. This file defines one iteration so that any session can execute the next pass mechanically.

## One iteration

1. Open `REVIEW_LEDGER.md`, take the highest-priority PENDING unit (or continue an IN_REVIEW one). Mark it IN_REVIEW with date.
2. Read the unit's documents. For large units, read substantive documents fully and skim mechanical ones (logs, manifests); record which was which.
3. Extract, per document that carries content:
   - **What it is** (one line) and its era/date if determinable
   - **Claims made** and their *stated* status (proven/conditional/numerical/conjectural/failed) — never upgrade a status; flag if a doc's claim conflicts with the live chain status in `STATE.md` or `theory/`
   - **Connections** to live problems (OP-1…OP-14, CONJ_A–D, campaigns) — cite exact file paths
   - **Actionables**: results worth surfacing, contradictions, useful lemmas/constants, anything Alex must judge
4. Write findings to `findings/Fnnn_<unit>.md` (next number). Keep it dense; quote sparingly; cite paths always.
5. **Deposit the distillate (CLAUDE.md rule 9 / DECISIONS #008).** Findings are the log; the corpus is the product. In the same pass, update or create the matching layer document: reference/status content → `theory/` (e.g. DOC_GOV_chain_status_map.md, DOC_GOV_conventions.md — extend these before inventing new docs), campaign material → `programs/`, engines/data → `numerics/` (with gates), manuscript-facing caveats → `papers/<paper>/README`. A pass with no corpus deposit must say why in the finding.
6. Update the ledger row: DONE (date, Fnnn, one-line verdict). Add any newly discovered sub-units as PENDING rows. Counting convention: **closed = DONE + SKIP**.
7. If anything is status-relevant, update `STATE.md` and flag it in the session summary to Alex. Append one entry to `records/SESSION_LOG.md`. Do this per pass, not per session.

## Rules that bind every pass

- **No mathematical judgment** — describe and cross-reference claims; validity is Alex's and the review pipeline's.
- **Read-only on archives** (E:\YANG, E:\YANG_ANTI, F:). Copy nothing into THEORY except distilled findings, unless Alex directs a recovery (then: MD5 + provenance per CLAUDE.md rule 5). Recovery deposits INTO E:\YANG ORGANIZED follow the F011/F012/F015 precedent: non-destructive, MD5-manifested, provenance README in the receiving directory; stale operational text in archive READMEs gets a dated correction block APPENDED, never edited away (audit-trail style).
- **Flag, don't fix**: contradictions between documents get recorded in findings, not edited away.
- **Token discipline**: a unit too large for one session gets split into sub-units in the ledger, never half-read silently (precedent: #8 → #8b).
- **Concordance reads**: layers already covered by a review generation (CLAUDE_REVIEW, Dec/Jan audits) are read blind-first, then compared — record agreement as "concordance PASS" and only the deltas in detail. The review of reviews is itself corpus content (it tells the papers which filter to trust).
- **Run-log discipline cuts both ways**: presence without a run log confers no status (master doc rule) — and a run log without a locatable file is "documented-but-not-reproducible," which is status-relevant and goes to STATE + Alex.

## Priority logic (queue order rationale)

P1 = never read by anyone (fresh recoveries), or feeds the live bottleneck (OP-1/M3, CONJ_B). P2 = settled-chain context the live campaign cites (synthesis, proven docs, appendices). P3 = the proof/ workspace long tail (sector by sector). P4 = archives/history (brain sessions, snapshots, funzone). Caches and binary data are SKIP with reason.
