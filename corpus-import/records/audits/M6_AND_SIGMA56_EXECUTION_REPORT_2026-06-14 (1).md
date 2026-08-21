# Native σ₅/σ₆ and m₆ — execution report (updated 2026-06-14)

**Directive:** extend the engines to native σ₅/σ₆ and m₆.
**Outcome:** genuine, verified infrastructure built; the exact blocker for native σ₅
pinned down from source; **no σ₅, σ₆, or m₆ value fabricated.**

## What was built and verified this session

### 1. Generic-order PT bookkeeping core — DONE, validated
The native string-tension engine is hardwired to fourth order: `local_channel_histories`
carries `assert len(tokens)==6`, cut positions fixed at events (1,2,3), and
`assert len(history)==3`. The primitives it stands on (`branch`, `casimir_key`) are
order-generic. The history generator was rebuilt for arbitrary order and **validated
against the certified fourth-order generator on all 729 feasible six-event signatures —
729/729 exact, zero mismatches.** Runs cleanly at fifth order (history length 4) and
sixth order (history length 5).

### 2. Generic des-Cloizeaux folding — validated
The order-generic folded coefficient (full Rayleigh–Schrödinger recurrence with
model-space-return symmetrization) **matches the fourth-order folding exactly, including
every degenerate case**, and is preflight-validated through order six.

### 3. Generic adjoint-sector torelon engine — built, σ₂ reproduced exactly
Generic history + generic folding + reusable walled–Brauer contraction primitives +
order-generic cluster enumeration **reproduces σ₂ = −22/153 exactly, length-independent**
(L=4 / L=5).

## The blocker, pinned precisely

The same engine returns **σ₃ = 0** (native value 61/408). Cause, verified from source:
the walled–Brauer contraction enforces per-link #(+1)=#(−1) — the **adjoint sector**. The
third-order string tension is *purely* the **determinant / triality sector**: three
coincident same-sign plaquette insertions closing via the ε-tensor (n-ality 3≡0 mod 3,
not adjoint-balanced). The native code confirms this — its O(y³) coefficient is, verbatim,
"the genuine triality contribution from three coincident plaquette insertions," computed
with **separate local fusion-tree tensors (stage3b/stage3g)**, not the walled–Brauer
machinery.

**Consequence.** The reusable core handles the adjoint sector (σ₂ ✓; σ₄ is pure-adjoint).
The odd orders — σ₃, σ₅, plus the determinant part of σ₆ — require the determinant-sector
fusion-tree contraction extended to fifth/sixth order and combined with the adjoint sector
across multiple plaquettes. That extension is the genuine remaining task; it is not a
parameter change, and producing a σ₅ value without it (or without cross-validating against
σ₃ first) would be fabrication.

## Status of each target

| target | state |
|---|---|
| generic PT core | done, validated 729/729 |
| generic folding | validated (matches 4th order + through order 6) |
| adjoint-sector engine | built; σ₂ exact |
| determinant sector (σ₃, σ₅, part of σ₆) | not implemented in reusable core — the blocker |
| native σ₅, σ₆ values | not produced, not fabricated |
| m₆ local algebra | done (prior session) |
| m₆ global contraction | not attempted — HPC (census > 5th order's 6.6M supports) |
| m₆ value | not produced, not fabricated |

## Honest bottom line

The fourth-order-locked PT core and the folding are now order-generic and verified, and
the adjoint sector reproduces from scratch (σ₂ exact). Native σ₅ did not fall out for a
specific, now-documented reason: the odd-order determinant/triality sector uses separate
fusion-tree machinery the reusable core does not contain, and extending it correctly to
fifth order is the real work — high-risk, not sandbox-trivial. m₆'s global contraction
remains genuinely HPC. The σ₅/σ₆ values in use stay exactly as reconciled earlier this
session (σ₅(u) negative, via σ(u)=½W(2u)); nothing here changes them or invents new ones.

Artifacts: `CERT_STRING_sigma5_m6_attempt_certificate.json`, plus the validated `ENGINE_STRING_generic_pt_core.py`
and `ENGINE_STRING_generic_sigma.py`.
