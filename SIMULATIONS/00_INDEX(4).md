# 12-18-25 Project Extracts — Selected “Most Promising” Notes (Index)

This mini-file-set contains the strongest *reusable* lemmas/propositions, plus the most promising “new theory” directions that emerged from the project notes and this chat.

## Contents

1. **Reflection-positive RG + projective limits + gap persistence**
   - File: `01_reflection_positive_rg_and_gap_persistence.md`
   - Why: gives a clean *continuum interface*: what must be preserved by coarse graining, and why a uniform gap cannot disappear in a monotone form limit.

2. **Davies decay for massive Maxwell (and the boundary row-sum refinement)**
   - File: `02_davies_decay_maxwell_boundary_rowsum.md`
   - Why: a sharp and modular decay lemma with the key **linear-in-$m$** exponent scaling, plus the “boundary constant” $C_\partial$ trick.

3. **Local cancellation rigidity in SU(2): “rough ⇒ force bounded below”**
   - File: `03_local_cancellation_alignment_su2.md`
   - Why: isolates the single geometric input that would make the bad-set coercivity route volume-uniform.

4. **Two no-go theorems about cross-scale maps / Markov kernels**
   - File: `04_no_go_coarse_graining_kernels.md`
   - Why: prevents wasted effort: it explains *why* certain natural-looking RG kernels cannot exist, and what must be weakened.

5. **Simulation appendix (includes an A100-ready workload)**
   - File: `05_simulation_appendix_maxwell_and_a100_su2.md`
   - Why: includes (i) a verified FFT inversion check of Prop 9.X-style bounds, (ii) the gauge-fixing “$C_0$ collapse” experiment, and (iii) a large batched SU(2) GPU simulation designed to directly test GAP-FC-02 and GAP-FC-04.

---

## How to read

If you want the “physics storyline”:

`01` (continuum interface)  →  `02` (fixed-cutoff decay engine)  →  `03` (geometric coercivity input)  →  `04` (RG obstructions)  →  `05` (numerical stress tests).

