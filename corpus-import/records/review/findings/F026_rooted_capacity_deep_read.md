# F026 — Unit #47b: rooted-capacity trio deep read — status table, M3a mapping, engine concordance, one degraded export

**Date:** 2026-06-12 · **Unit:** `programs/rooted_capacity_program/` (3 docs). Logical Status Map + SU(3) Three-Term read in full; Rooted Source Stability read in full **as uploaded** (see §4).

## 1. Theorem-by-theorem status (the docs' OWN labels — they ship a five-level convention: Theorem / Finite certificate / Numerical audit / Conditional theorem / Open input, declared "part of the mathematical content")

| Item | Statement | Own status |
|---|---|---|
| SU(3) three-term gap | Δ_SU(3)(β) = √(2β/3) − 5/16 − (311√6/9216)β^(−1/2) + O(β⁻¹), boxed with proof from H₂-direct + H₁-resolvent pieces | **Theorem** (local class-sector) |
| Rank-two correction | c₁ − c₁^rad = √6/576, exactly the p₃² degree-six invariant's contribution ("the third coefficient is not determined by the radial Laguerre sector") | **Theorem** (local) |
| Fixed-rank SU(N) even gap | √(2β/N) − (2N²−3)/16N − √2(6N⁴−24N²+41)/1024N^{3/2}·β^(−1/2) + O_N(β⁻¹) | Theorem + **Finite certificates** (Wick: q_res^{(N),+} = −(34N⁴−120N²+171)/3072N²) |
| Fixed-rank SU(N) odd gap | √(9β/2N) − **3(N²−3)/16N** − √2(14N⁴−97N²+290)/1536N^{3/2}·β^(−1/2); **erratum: −3(2N²+1)/16N "does not belong to the final theorem stack"** | Theorem + Finite certificate (q₋^{(N)}) |
| Leakage matrix | "finite-channel diagnostic only… not asserted to be a full-channel polymer constant" (radial Laguerre tail obstruction named) | **Numerical audit / diagnostic** |
| Global top-norm firewall | ‖P𝟙_D P‖ ≤ c < 1 uniformly — "**Such a statement is false in large volume**" (rare islands) | rejected target (their words) |
| Rooted summability | Σ_{Γ∋p₀} exp{a\|Γ\|+sΘ_Λ(Γ)} ℙ_β(Γ⊂D_δ) < ∞ | **Conditional theorem** — inputs: linear capacity envelope (deterministic) + hard-defect Peierls (conditional) |
| Source stability | rooted exponential moment ⇒ stability of local source insertions | **Conditional theorem** (chain: free-energy stability ⟹ Peierls ⟹ summability ⟹ source stability) |
| Wilson free-energy stability (inhomogeneous, volume-uniform) | "The missing theorem is not a local class-gap computation. It is the volume-uniform Wilson free-energy and projected-capacity estimate" | **Open input** — the single named gap |

"What is not claimed" section is exemplary (no glueball-mass claim, no OS construction, no continuum gap, numerics ≠ proof).

## 2. M3a mapping (descriptive)

The trio = the doc layer of the **projected-capacity spine** already named in the OP-1 dossier's M3 addendum. Its Open Input ("inhomogeneous Wilson free-energy stability") is the **Z.B / Bałaban-far-source-stability class**: the PMBSF master states verbatim "The rooted version holds for Y_p^LCI if the rooted far-source stability estimate holds," and the trio's chain (free-energy stability ⟹ hard-defect Peierls ⟹ rooted summability ⟹ source stability) is that route written from the capacity side. **Z.A (LCI typicality) is not addressed by the trio.** Net for M3a: one of its two open theorems now has a second, rooted-capacity formulation; the other is untouched. Consumers unchanged (dossier §3, M2 W(r) tables as the ρ₂ interface).

## 3. Engine concordance (verified)

`ENGINE_SUN_codd_local_gap_exact.py` (F015 recovery, re-run PASS) prints **c0_-(N) = −3(N²−3)/(16N)** — exactly the Map's corrected coefficient. The deposited engine certifies the corrected theorem stack; the superseded −3(2N²+1)/16N is a **quoting hazard in older era documents** (CONVENTIONS-class warning recorded in the program README).

## 4. Degraded export (action for Alex)

The Rooted doc as uploaded has **its display math empty in the source** (chat→docx export stripped Unicode/OMML: capacity definition, envelope, exponential moment, theorem statement all blank; prose + hypothesis structure intact; raw extraction confirms — `NOTE_RCAP_rooted_raw_extract.txt`). The Map's Layer III recovers the schematic content, so identification is solid, but **the rooted theorem's exact statement is not in any store** — please re-export that document (or paste the LaTeX source); until then it is documented-but-display-degraded.

## 5. Deposits

This finding; program README updated (status table pointer, degraded-export flag, erratum warning); OP-1 dossier dated addendum (rooted-capacity correspondence); STATE; ledger #47b → DONE; SESSION_LOG.
