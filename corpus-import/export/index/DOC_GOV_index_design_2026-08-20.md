# Index + retrieval design for the ALL THEORY corpus

**Date:** 2026-08-20 · **Status:** design proposal, nothing built yet · **Audience:** whoever builds the index and the WORKHOUSE-side tooling.

---

## 0. The measurement that should drive every decision

Before choosing an architecture, here is what is actually being indexed (excluding `QUARANTINE/` and `archive/`):

| | |
|---|---:|
| Prose files (`.md` + `.tex`) | 319 |
| Words of prose | 474,652 |
| **Approximate tokens of prose** | **~665,000** |
| Headings (natural chunk anchors) | 3,276 |
| Display-math blocks | 4,248 |
| **Distinct non-trivial exact rationals** | **174** |
| Total occurrences of those rationals | 851 |
| Python files / notebooks | 200 / 97 |

Two facts follow, and they invert most of the standard RAG playbook.

**Fact 1 — the corpus is tiny.** 665K tokens is roughly four Claude context windows. Every published benchmark that motivates a vector database assumes 10²–10⁴× this. The 2026 consensus for corpora of this size and kind is that an agent driving `ripgrep` in a loop beats a frozen embedding index: a simple RAG baseline on SWE-bench scored 1.96% while agentic tool-use systems now exceed 80%, and none of the leaders use vector retrieval over the target repo. **Do not start by building a vector database.**

**Fact 2 — the corpus's real identity keys are exact rational numbers, not concepts.** 174 distinct rationals carry 851 occurrences; the top ones appear in dozens of files each:

| Constant | Occurrences | Files |
|---|---:|---:|
| `109151/249696` | 70 | 37 |
| `17607806155349/275331901291200` | 42 | 23 |
| `20721577909065127111/7250590288602460800` | 30 | 18 |
| `1975/124848` | 26 | 18 |
| `132329431693349/275331901291200` | 26 | 17 |
| `304746539168/160249753125` | 21 | 16 |

**No embedding model will ever retrieve `20721577909065127111/7250590288602460800` from a semantic query.** These are the join keys of the entire corpus, and they demand an exact index. This is the single most important design consequence.

---

## 1. Build a claims index, not a document index

Fixed-size chunking is wrong here. It severs LaTeX blocks from the sentence that gives them status, and it produces chunks that cannot carry provenance. Chunk on **claims** instead — one record per assertion, typed:

```yaml
id: CLM-0412                       # stable across corpus revisions
kind: theorem | definition | coefficient | gate | caveat | erratum
slogan: >                          # one plain-English line; THIS is what gets embedded
  the all-rank second-order hopping coefficient is positive for every N >= 3
statement_md: "For SU(N), N >= 3, ..."
latex: 't_N = \frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)}'
constants: ["2/1", "..."]          # canonicalized exact rationals appearing in the claim
symbols:   [t_N, N]
status:    proven                  # proven|conditional|disputed|open|superseded|falsified
evidence:  analytic                # analytic|cold-reproduced|output-certified|numerical|record-backed|prose-only
source:
  file:    corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md
  sha256:  134a604b96bec35c...     # already pinned in export/MAN_GOV_export_manifest.csv
  section: "4.1"
  lines:   [479, 500]
supersedes: [CLM-0311]
gates:     [numerics/certificates/CERT_Y5_su3_m5_certificate.json]
```

3,276 headings and 4,248 math blocks will collapse to roughly **1,500–2,500 claims** — small enough that a human can actually audit the index, which is the point.

Three properties of this corpus make the typed schema mandatory rather than nice-to-have:

1. **Status is load-bearing.** Returning a superseded document as if current is not a degraded answer here, it is a wrong one. This project has a documented history of exactly that failure — "PROVEN" banners sitting over conditional content in every era.
2. **Contradiction must survive retrieval.** The fourth-order `C⁽⁴⁾` dispute is the live research front. A ranker that picks a winner between `C_old` and `C_new` destroys the finding. Disputed claims must return **both sides, always**.
3. **Provenance is already content-addressed.** `export/MAN_GOV_export_manifest.csv` pins each corpus document by SHA-256. Cite that hash in every claim and a corpus edit that invalidates downstream claims becomes mechanically detectable.

---

## 2. Embed slogans, not LaTeX

The most useful recent result for this corpus: on a 9-million-theorem retrieval benchmark, **embedding theorems via natural-language slogans significantly outperforms embedding their raw LaTeX formulations.** That system reached 45.0% Hit@20 at theorem level against 19.8% for a frontier chat model with search.

So: generate a one-line slogan per claim (an LLM pass over the corpus, done once, human-spot-checked), embed the slogan, and keep the LaTeX as retrievable payload rather than as embedding input. This is the `slogan:` field above.

---

## 3. Retrieval stack

Three indexes in parallel, fused, then filtered. **Not** a single vector search.

```
query
  ├─ (A) exact constant lookup      hash map over canonicalized rationals
  ├─ (B) BM25 / SQLite FTS5         over slogan + statement + symbol names
  └─ (C) dense k-NN                 over slogan embeddings
        │
        ├─ if the query contains a rational, (A) short-circuits to the top
        ├─ else fuse (B)+(C) by Reciprocal Rank Fusion
        ▼
  cross-encoder rerank
        ▼
  HARD status filter  ──  superseded/falsified excluded unless asked;
                          disputed claims expand to all sides
```

Design notes:

- **RRF, not weighted score averaging.** BM25 and cosine scores are not commensurable; naive weighted blending is a known production failure mode. RRF operates on ranks and sidesteps it. Tuned hybrid measurably beats either leg alone (≈7.4% NDCG lift on WANDS), and hybrid-RRF-plus-cross-encoder-rerank dominates in the published comparisons — the reranker being the single largest quality jump.
- **Weight lexical high.** Generic advice balances sparse and dense. Here, symbol names (`t_N`, `q_a`, `\lambda_4`, `P_17`), file names, and constants are all lexical, and the vocabulary is small and consistent. Start at roughly 70/30 in favour of BM25 and tune on a real query set.
- **(A) outranks everything.** If the query contains an exact rational, the constant index is authoritative and semantic similarity is noise.

**Concrete components.** SQLite with FTS5 (BM25 built in) plus `sqlite-vec` for the dense leg — one file, no server, small enough to commit or ship as a release asset. For models, the Qwen3 embedding/reranker family is the open-source default to beat as of 2026 (`Qwen3-Embedding-8B` tops MTEB multilingual at 70.58; the 0.6B variants are the sensible local starting point, with `BGE-M3` + `bge-reranker-v2` the common alternative). At 2,500 claims you do not need approximate nearest neighbours — brute-force cosine over 2,500 vectors is sub-millisecond.

---

## 4. The constant linter — build this first

This is the highest-value component and it is not RAG at all. It is a **linter for the mathematics**, and it exists because the corpus documents two live traps: the `Y = 4u` label erratum (never rescale by `4^r`) and the factor-2 metric-convention trap.

Both traps have the same machine-detectable signature: **the same quantity appearing at an exact 2× or 4× ratio in two places.** So index every exact rational, then flag every pair related by exactly ×2 or ×4 and require each pair to be classified.

**This was prototyped against the live corpus. It found four pairs, and all four resolve to known, legitimate conventions:**

| Pair | Ratio | Resolution |
|---|---|---|
| `17607806155349/1101327605164800` ↔ `.../275331901291200` | ×4 | `β/4` real-space form vs `β` symbol form. Legitimate. |
| `247051057231349/2202655210329600` ↔ `.../550663802582400` | ×4 | Same `α/4, β/4` real-space convention. Legitimate. |
| `2861009/16877460600` ↔ `2861009/8438730300` | ×2 | `τ₄` vs the cap coefficient `2τ₄`. Legitimate (corpus §9.3). |
| `132329431693349/3303982815494400` ↔ `.../1651991407747200` | ×2 | **Symbol collision** — see below. |

The fourth is the interesting one. The corpus defines `κ(n) = 2a(n)` where `λ₄(tn) = a(n)t² + O(t⁴)`, and prints `κ₁₁₁ = (α+β)/6`. The flat-band manuscript v1.1 prints `κ_diag = (A+B)/12` — which is `a(n)`, the `t²` coefficient, not the second derivative. **Both documents are internally correct. They use the letter `κ` for two quantities differing by exactly 2×.** Nothing is wrong; but this is a live cross-document factor-2 hazard sitting on a symbol the corpus already flags as a trap (`CLAUDE.md` §5 trap 4), and it is precisely what someone quoting across the two documents would get wrong.

That is the whole argument for the linter: it finds every such pair mechanically, forces each to be classified once, and then **any new unclassified pair is a genuine alarm.** The corpus is currently clean on this axis — that is worth knowing and worth keeping true.

Extend the same idea to: same claim id with two different constants across corpus revisions; a constant present in a manuscript but absent from any certificate; a certificate whose value disagrees with the document that cites it.

---

## 5. GitHub architecture

```
 ALL THEORY  (corpus, authoring)
      │  export/MAN_GOV_export_manifest.csv   SHA-256 freeze
      ▼
 WORKHOUSE  (github.com/ats314/WORKHOUSE)
      ├── index/extract/     md+tex → claims.jsonl        (parser)
      ├── index/index.db     FTS5 + sqlite-vec + constants (build artifact)
      ├── ledger/*.yaml      contradiction register        (already exists)
      ├── .github/workflows/ reindex + lint on push
      └── mcp/               MCP server over the index
```

WORKHOUSE is the right home: it already re-derives the corpus's claims from their stated definitions and reports where a printed number disagrees with its own definition, and it already has `ledger/` as a machine-readable contradiction register. The index is the missing substrate under work it is already trying to do.

**Ten concrete GitHub moves, roughly in order of value:**

1. **The constant linter as a required PR check.** A pull request that introduces an unclassified 2×/4× constant pair fails CI. This is the cheapest possible defence against the erratum recurring.
2. **Rebuild the index in Actions on push**, and publish `index.db` as a **release asset** rather than committing it — keeps the repo small, gives you one immutable index per corpus version, and makes "which index answered this question" a stable citation.
3. **`repository_dispatch` from corpus freeze to reindex.** When `export/MAN_GOV_export_manifest.csv` changes, fire an event at WORKHOUSE. The manifest hash becomes the index's version key.
4. **Drift check as a gate.** CI recomputes the SHA-256 of every corpus document against the manifest; a mismatch fails before anything else runs. You have this check written already — promote it to CI.
5. **MCP server over the index.** Expose `search_claims`, `lookup_constant`, `get_claim`, `find_contradictions` as tools. This is the actual delivery mechanism — the index is for agents, and `code-index-mcp` / `claude-context` are existing patterns to crib from. Local-first, nothing leaves the machine.
6. **GitHub Pages claim explorer with zero backend.** `sql.js-httpvfs` serves a SQLite file over HTTP range requests, so the browser fetches only the pages a query touches. A browsable, searchable claim index as a static site, no server, no hosting bill.
7. **Issue-per-open-problem, keyed by claim id.** `CLM-0412` in an issue body; CI cross-links. The eleven freeze conditions for the fourth-order run become eleven checkboxes with claim references.
8. **CODEOWNERS on `corpus/`** so authority-document edits require explicit review — the editing policy is already written down, this makes it enforced rather than remembered.
9. **Label PRs that touch disputed claims.** A bot comments with the current state of the dispute so nobody silently "fixes" `C_old` to match `C_new`.
10. **GitHub Code Search for exact constants** across your repos as a zero-build fallback while the real index is being written — it does exact string matching, which is what these constants need.

**On `git init` for `ALL THEORY` itself:** you decided against it, and the index does not require it — `MAN_GOV_export_manifest.csv` already gives content addressing, which is the property that actually matters. Worth revisiting only if you want per-claim blame across time.

---

## 6. What NOT to build

- **A vector database.** 2,500 claims. Brute force is faster than the network call.
- **A chunk-and-embed-everything pipeline** over notebooks and `.npz` files. 91 MB of the corpus is matrix caches; 34 MB is notebook output cruft. Index notebook *source* cells and skip outputs.
- **A single-answer RAG chatbot.** The corpus's most valuable content is a live disagreement. A system whose job is to produce one confident answer is structurally wrong for it.
- **GraphRAG, initially.** A knowledge graph over claims (supersedes / depends-on / contradicts) is genuinely attractive here, and provenance-tracking graph RAG is a real 2026 direction. But it earns its complexity only after the claims table exists — the graph is a view over `supersedes:` and `constants:` edges you will already have.

---

## 7. Build order

| # | Deliverable | Effort | Payoff |
|---|---|---|---|
| 1 | Constant extractor → `constants.jsonl` + ratio linter | hours | Immediate. Prototype already works. |
| 2 | Wire the linter into WORKHOUSE CI as a required check | hours | The erratum can never silently recur. |
| 3 | Claim extractor → `claims.jsonl` (headings + math blocks + status) | days | The substrate for everything else. |
| 4 | SQLite FTS5 index + `lookup_constant` + `search_claims` CLI | days | Covers most real queries with no embeddings at all. |
| 5 | MCP server over 4 | days | Agents can use it. This is the actual goal. |
| 6 | LLM slogan pass + `sqlite-vec` dense leg + RRF + reranker | ~a week | Semantic recall for "what do we know about X". |
| 7 | GitHub Pages explorer | days | Human browsing, zero infrastructure. |

**Stop after step 4 and reassess.** For a 665K-token corpus, steps 1–4 plus an agent with `ripgrep` may be the whole answer, and step 6 may never pay for itself. Build the semantic leg only if you can point at real queries that steps 1–4 failed.

---

## Sources

- Hybrid search / RRF / reranking: [denser.ai](https://denser.ai/blog/hybrid-search-for-rag/), [digitalapplied.com](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026), [From BM25 to Corrective RAG (arXiv)](https://arxiv.org/html/2604.01733v1)
- Agentic search vs vector RAG: [DEV Community](https://dev.to/nimay_04/rag-is-not-always-the-answer-anymore-how-ai-agents-search-code-in-2026-43m3), [SmartScope](https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/), [Beyond Semantic Similarity (arXiv)](https://arxiv.org/pdf/2605.05242)
- Math retrieval / slogans: [Semantic Search over 9 Million Mathematical Theorems (arXiv)](https://arxiv.org/html/2602.05216v1), [Mathematical Information Retrieval review (ACM)](https://dl.acm.org/doi/10.1145/3699953), [SSEmb (arXiv)](https://arxiv.org/pdf/2508.04162)
- Embedded vector search: [sqlite-vec](https://www.sqlite.ai/sqlite-vector), [embedded vector DB comparison](https://shaharia.com/blog/choosing-embeddable-vector-database-go-application/)
- Models: [Qwen3-Embedding](https://qwenlm.github.io/blog/qwen3-embedding/), [Qwen3-Reranker-0.6B](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)
- Static SQLite serving: [phiresky, SQLite on GitHub Pages](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/), [sql.js-httpvfs](https://recca0120.github.io/en/2026/03/07/sql-js-httpvfs-static-hosting/)
- MCP code index patterns: [code-index-mcp](https://github.com/trondhindenes/code-index-mcp), [claude-context](https://github.com/zilliztech/claude-context)
- GraphRAG (deferred): [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG)
