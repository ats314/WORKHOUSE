# CHARTER — what THEORY is, and is not

**Read this first. One page. The north star. If anything in an older doc conflicts with this, this wins — and fix the older doc.**

## What this is

`C:\THEORY` is the **distilled working core** of a ~4-year research exploration. Across hundreds of AI sessions and several drives, that exploration produced an enormous sprawl; THEORY is the narrowed-down residue — the strongest, most rigorous, most novel results worth carrying forward and finishing.

## What it's about

Rigorous, computer-verified **lattice-gauge & spectral-geometry mathematics**. The load-bearing, genuinely novel pieces:

- the **deterministic Birman–Schwinger defect-sparsity framework** — exact kernel certificates (OP-1: M1/M2 + Lemmas A/B, all hard gates passing);
- the **one-plaquette flat-band glueball spectroscopy** — exact constants through O(y³), machine-certified;
- the **analytic sparsity programs** — PMBSF / Lemma Q and rooted projected-capacity.

## What it is NOT

- **Not** a Yang–Mills / Clay Millennium "solver." That telos is retired (DECISIONS #010). Do not re-open "is this a proof of the mass gap" — it is not trying to be one.
- **Not** the archive. The wider exploration it was distilled from (geometric particle-mass/constants models, AI-proof tooling, the energy-code profession) lives on the other drives; see `SOURCES.md`.

## What "done" looks like (the target — not "more hardening")

Self-contained results written to a standard a real external referee would accept, then submitted. Concrete deliverables:

1. the flat-band spectroscopy paper (`papers/flat_band/`) — closest to done;
2. *(candidate)* a standalone note on the Birman–Schwinger criterion + d=4 resolvent constants — the most distinctive method.

## The map (work at this level first)

- `theory/` — the mathematical object + citation-safety maps (`CHAIN_STATUS_MAP`, `CONVENTIONS`)
- `programs/` — the active campaigns: `op1_defect_sparsity`, `one_plaquette`, `pmbsf`, `rooted_capacity_program`
- `numerics/` — gated engines + data that re-verify the claims
- `papers/` — manuscripts in flight
- `records/` — `SESSION_LOG` + review findings (history)

## Current lead

OP-1's deterministic side is closed by exact computation; the **stochastic sparsity lemma (S)** is the single open analytic piece. `STATE.md` is the living status — read it second.
