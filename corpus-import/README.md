# ALL THEORY

The working home and master corpus for the **SU(N) cubic flux-band spectral program** — rigorous, computer-verified lattice-gauge and spectral-geometry mathematics.

**Read `CLAUDE.md` first** — it states the conventions, what is established, the one disputed coefficient, what is open, and the traps. Then `corpus/`, which is the authority it summarizes.

---

## What is here

| Layer | What it holds |
|---|---|
| `corpus/` | **The scientific authority.** The four-document August 20, 2026 stack: unified master, technical appendix, navigation guide, provenance manifest. Everything else defers to this. |
| `theory/` | The mathematical object — open problems, proof chain, citation-safety and conventions maps, conjectures, standalone theorems, notes. |
| `programs/` | Active campaigns, each with a milestone ladder. `hodge_o4_adjudication/` is the live front. |
| `numerics/` | Engines, notebooks, certificates, results, and data that re-verify the computational claims. |
| `papers/` | Manuscripts in flight. Flat-band paper at v1.1; unified spectral-geometry manuscript at v1.4. |
| `literature/` | External and third-party papers, plus novelty/priors literature checks. |
| `records/` | Session log, review findings, audits, run logs, transcripts, governance archive, reorg manifests. |
| `archive/` | Bulk material — release zips, the SU(2)/TRG simulation archive, verification bundles. |
| `export/` | The frozen handoff layer for [github.com/ats314/WORKHOUSE](https://github.com/ats314/WORKHOUSE). |
| `GITHUB/` | Flat mirror of the whole corpus for upload. Generated — never edit by hand. |
| `QUARANTINE/` | Material moved out of the tree. **Nothing was deleted** — see `QUARANTINE/RESTORE_MANIFEST.tsv`. |

## The result, in one paragraph

For SU(N), N ≥ 3, the cubic incidence complex carries a charge-odd one-plaquette flux band that is **exactly flat at the incidence level**. The Bloch factorization `S(k) + 4I = B(k)B(k)†` is exact; on the three-torus `dim ker ∂₂ = L³ + 2 = (L³ − 1) + 3`; the all-rank second-order hopping `t_N = 2N(N²−4)/[(N²−1)(2N²−1)(4N²−9)]` is positive for every N ≥ 3; and for SU(3) the charge-odd effective operator factorizes through third order, so the carrier energy is independent of momentum through `O(u³)`. First mobility appears at fourth order. **What is not settled** is the complete physical fourth-order kernel: two independent computations agree on the axial coefficient but disagree in one planar mixed-gradient direction, and that disagreement is *not* removable by a scalar shift. Nothing here is, or claims to be, a continuum Yang–Mills mass-gap theorem.

## Relationship to WORKHOUSE

`ALL THEORY` is the **upstream corpus**; [WORKHOUSE](https://github.com/ats314/WORKHOUSE) is the downstream **machine verifier**. WORKHOUSE re-derives the corpus's exact claims from their stated definitions and reports where a printed number and its own definition disagree. It does not restate the theory.

The handoff is one-directional and explicit: freeze a corpus document → record it in `export/MAN_GOV_export_manifest.csv` with its SHA-256 → WORKHOUSE consumes that frozen copy. **Do not edit `corpus/` documents casually**; a change there invalidates WORKHOUSE's constants registry. See `export/README.md`.

## Filenames are metadata

Every file follows `CLASS_TOPIC_descriptor[_vN][_YYYY-MM-DD].ext` — see [NAMING_CONVENTION.md](NAMING_CONVENTION.md). `CLASS` and `TOPIC` are uppercase closed vocabularies, so `ls THM_*`, `ls *_O4_*` and `ls CERT_*` are real queries against the corpus without opening anything. 773 of 836 files conform; the rest are `README.md` files (whose topic is their directory) and root governance.

The exact rationals that identify this corpus — 205 of them, some cited in 39 separate files — are indexed in [theory/DOC_FLUX_constants_index.md](theory/DOC_FLUX_constants_index.md).

## Four things that bite

1. **Truth status and evidence level are independent axes.** A claim can be analytically exact *and* rest on a disputed input kernel. "Certified" never means "proved."
2. **`Y = 2β_lat/3 = 4u` in archived sources is a label erratum, not a rescaling rule.** Those coefficients were already generated in `u`. Never multiply or divide them by `4^r`.
3. **A newer file does not outrank an exact counterexample**, and a file named `final` does not override a failed invariant.
4. **The `Γ` curvatures are radial directional derivatives, not a Hessian** — a cubic Hessian exists only when `β = 2α`, which the historical kernel does not satisfy.

`CLAUDE.md` §5 carries the full list.

## Provenance of this layout

Reorganized August 20, 2026 (DECISIONS #012). 621 file moves, 0 name collisions, nothing deleted. Every move is recorded with size and MD5 in `records/REORG_MANIFEST_2026-08-20.tsv`; the pre-move plan is preserved beside it. The June 15, 2026 governance documents are byte-preserved in `records/governance_archive/`. The agent-process documents (`CHARTER`, `GUARDRAILS`, `AGENT_PROTOCOL`) were retired to `QUARANTINE/process_docs/` — they carried session conventions accumulated from earlier conversations rather than mathematics.
