# SOURCES — where everything else lives

`C:\THEORY` holds only the distilled working set (see `CHARTER.md`). Everything below is **read-only archive** — the wider ~4-year exploration THEORY was narrowed down from. Copy from it; never write to it. This page is the map, so nothing has to be re-discovered (GUARDRAILS #2, #4).

## E:\YANG — archive-of-record (~8,100 organized + 43K workspace files)

| Need | Go to |
|---|---|
| Full onboarding to the corpus | `ORGANIZED/AGENT_GUIDE.md`, then `ORGANIZED/INDEX.md` routing tables |
| Any proof document P01–P20, evidence, synthesis | `ORGANIZED/01_PROOFS/` (+ `PROOF_MAP.md` at ORGANIZED root) |
| Clay submission chain (12 reviewed docs + 3 recovered unreviewed) | `ORGANIZED/01_PROOFS/clay_submission/` |
| Independent review + open problems (frozen June 12 edition) | `ORGANIZED/CLAUDE_REVIEW/` (live copy now: `THEORY/theory/DOC_GOV_open_problems.md`) |
| 44 technical appendices | `ORGANIZED/02_APPENDICES/` |
| Manuscripts: Papers A–D, Comprehensive (recovered), legacy LaTeX | `ORGANIZED/03_MANUSCRIPTS/` |
| All simulation history beyond op12 | `ORGANIZED/04_SIMULATIONS/`, `proof/SIMULATION/` |
| Lean: 71 source modules + inventory | `ORGANIZED/05_LEAN/`; **active build:** `proof/lean/` (cached Mathlib, `lake build`, 30–60 min) |
| Research summaries (311 GPT masters, curated topics) | `ORGANIZED/06_RESEARCH_DOCS/` |
| RAG pipeline + tools | `ORGANIZED/07_TOOLS/` |
| arXiv PDFs | `ORGANIZED/08_REFERENCE_PAPERS/` |
| Everything historical | `ORGANIZED/09_ARCHIVE/`, `ORGANIZED/11_PROOF_WORKSPACE/` |
| One-plaquette full deposit (incl. v2.5, probe notebook) | `ORGANIZED/12_ONE_PLAQUETTE/` |
| Sweep/review records (methodology for archive dedup) | `ORGANIZED/00_META/YANG_ANTI_SWEEP_2026-06-12.md`, `SCALAR_CLUSTER_REVIEW_2026-06-12.md` |
| Pre-reorg originals (~52 GB) | `DELETE/originals/` — reference only |
| Inventory DB | `project_inventory.db` at YANG root (copy locally before querying) |

## The wider exploration (non-lattice-gauge work) — mostly in the chat record

THEORY is the lattice-gauge / spectral-geometry residue. The 4-year exploration also produced substantial **non-Yang work** that never consolidated into organized files — it lives almost entirely inside the chat exports. Recorded here only so its existence and location are known; **do not pull it into THEORY without Alex's direction.**

- **ChatGPT export:** `F:\E\conversations.json` (845 MB) + `chat.html` (858 MB) — 2,248 conversations, 2023-01 → 2026-02. Title+date index: `E:\YANG\ORGANIZED\00_META\CHATGPT_EXPORT_INDEX_2026-06-12.md` (raw pair also archived at `ORGANIZED/09_ARCHIVE/chatgpt_export/`). Only ~142 are YM by title; the rest are the wider work.
- Major non-YM threads in that record: a **geometric theory of particle masses & fundamental constants** (Holographic Double-Torus / spiral-seesaw / Koide / modular-forms / fine-structure-constant derivation — by its own in-chat audits, largely numerology; treat as exploratory, not established); cosmology/MOND-adjacent notes; and the **energy-code profession** (IECC / NFPA / ASHRAE — not research; never mix in).

## F:\E — original drive behind DELETE/originals (read-only)

Holds the **codenamed agent workspaces** the project accreted across sessions/tools: `ANTIGRAVITY/` (appendix files + brain sessions), `glacial-einstein/` (RAG pipeline + organized_*), `infrared-glenn/` (CLAY_SUBMISSION, CLEAN, FIRST_PRINCIPLES), `scalar-cluster/` (git repo + claims/deliverables), `AGENTIC_PROOF/` + `AX_PROVER/` (external arXiv papers on automated proving — reference, not ours), `tools/math_discovery/` (LeanConjecturer / TxGraffiti install). All mirrored in `E:\YANG\DELETE\originals/`; reference only. **Do not create more of these** (GUARDRAILS #4).

## E:\YANG_ANTI — early-layout snapshot (6,523 files, frozen)
Fully swept June 12, 2026 (57 truly new → recovered). No remaining unique content known. Reference only.

## F:\ANTIGRAVITY\antigravity\playground\scalar-cluster — original workspace (206,679 files, frozen pre-April)
Reviewed June 12, 2026 (186 recoveries → `YANG ORGANIZED/11_PROOF_WORKSPACE/scalar_cluster_recovery/`). Notable residents: **`proof/lean/` full Mathlib build cache (147K files — backup build option)**; MASTER_RAG chroma_db + venv (derived, not copied); `ARCHIVES/cruft/` contains a plaintext password file (flagged to Alex, do not copy). Reference only.

## F:\STORAGE — accounted June 12, 2026
`yang_mills_lean/` (Jan-15 Lean project → archived to YANG 05_LEAN/yang_mills_lean_jan2026/), `ai_proof_tools/` (LeanAide external, also in DELETE), `lattice_qcd/` (1 script, archived). The ChatGPT export pair lives on F:\E (above).

## C:\SIMULATIONS — Colab authoring store (mounted June 12, 2026; not always mounted)
Flat, **285 files (271 .ipynb + 14 .py engines), 47 MB**, mtimes 2026-03-07 → 06-11; manifests v1+v2 in `records/review/manifests/`. The notebook-side authoring sources of the simulation layers (Untitled### series, Theorem_B v4–v12, SU2_4D_Phase2 variants, A100 runs, GOODRESULTS1–5, SU3 d₃ pair). Surveyed F023: 34 match the archive by name+size; **237 unmatched = new-to-archive candidates** — identification queued (#45b). MD5 manifest: `records/review/manifests/SIMULATIONS_MD5_2026-06-12.txt`. The F015 lost engines are NOT here (hunt negative). Treat read-only pending Alex's intake direction.

## This workspace's own provenance
Every file under `theory/`, `programs/`, `numerics/`, `papers/` was copied June 12, 2026 from E:\YANG (or session outputs for MC state files) with MD5 verification; per-directory READMEs carry source paths. The archive copies remain canonical for history; THEORY copies are the working editions going forward (DECISIONS #003).

## Stray instruction files across the mounts (disregard for THEORY work)

Several mounted drives carry their own `CLAUDE.md` / `AGENTS.md` from earlier eras or unrelated work. **Only `C:\THEORY\CLAUDE.md` is authoritative** (its "Precedence" clause). Of all of them, **only two sit at a mount root and therefore auto-load**: `C:\THEORY\CLAUDE.md` (this project) and `E:\YANG\CLAUDE.md` — and the latter is now a thin read-only stub that points back here (its prior ~24 KB content is preserved verbatim in `E:\YANG\CLAUDE_SESSION_HISTORY.md`; DECISIONS #011). The rest are **nested, do not auto-load, live in read-only archives, and are not modified** — listed here so they are known and disregarded:

| File | What it is | Action |
|---|---|---|
| `E:\YANG\CLAUDE.md` | archive-of-record stub → points here (auto-loads) | keep as stub |
| `E:\YANG\CLAUDE_SESSION_HISTORY.md` | verbatim prior changelog (corruption flagged) | history only |
| `E:\YANG\proof\lean\AGENTS.md` | Lean build notes for the cached Mathlib build | use only when building Lean there |
| `E:\YANG\ORGANIZED\06_RESEARCH_DOCS\scalar_cluster_root\{CLAUDE,AGENTS}.md` | recovered scalar-cluster originals | archive; disregard |
| `E:\YANG\DELETE\originals\scalar-cluster\{CLAUDE,AGENTS}.md` | pre-reorg originals | archive; disregard |
| `F:\E\scalar-cluster\{CLAUDE,AGENTS}.md` | original scalar-cluster workspace | read-only; disregard |
| `E:\YANG_ANTI\ORGANIZED\…\scalar_cluster_root\{CLAUDE,AGENTS}.md` | early-snapshot copy | read-only; disregard |
| `F:\ANTIGRAVITY\…\scalar-cluster\proof\lean\AGENTS.md` | Lean build notes | read-only; disregard |
| `C:\Users\Alex\Downloads\lean4-master\…\.claude\CLAUDE.md` | third-party **Lean 4 compiler** source repo — not ours | ignore entirely |
| `F:\E\IECC\CLAUDE.md` | **Energy-code profession (IECC) — a separate domain** | **out of scope; never mix into THEORY; not modified** |

The CLAUDE.md "Precedence" clause already neutralizes these from the writable side regardless of what loads. If any ever needs neutralizing *in place*, that is an Alex-directed follow-up — most sit in read-only archives this project must not modify.
