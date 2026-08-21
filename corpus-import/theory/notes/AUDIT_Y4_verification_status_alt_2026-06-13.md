# Y4 breaking verdict — independent verification status & required framing corrections

**Reviewer:** lead math agent · **Date:** 2026-06-13 · **Subject:** the claim that the
SU(3) one-flux \(T_1^{+-}\) C-odd band is exactly flat through \(O(y^3)\) and acquires its
first nonzero bandwidth at \(O(y^4)\) (archive `Y4_FINAL_ARCHIVE_2026-06-13`).

This record is written to be dropped into `records/` next to STATE.md / DECISIONS.md. It
**revises the confidence upward** on the physics while flagging framing in the archive that
overstates what has been proven.

---

## 1. Net assessment (one line)

The breaking verdict is **probably correct and the mathematical risk is now low**: the
genuinely-new fourth-order perturbation-theory machinery has been validated end-to-end
against exact and certified references. The archive's **"theorem / criterion resolved /
independent audit"** framing nonetheless **overstates** the current backing and must be
corrected before the result is presented as proven.

---

## 2. What has been independently re-verified

All checks are exact-arithmetic, reproduced from read-only sources; scratch in `/tmp/verify`.

| # | Check | Result | What it covers |
|---|-------|--------|----------------|
| V1 | Cold re-run of `y4_stage3a` (firewall) and `y4_stage3d` (raw trace) — the two O(y²) stages the from-scratch bundle **skips** | PASS. Reproduces `−481/612`, `−11/306`, even/odd levels; derives \(\rho_{\text{shared}}=I_9/9\) from \(\int dU\,U U^\* = \delta\delta/3\) | The **normalization the O(y⁴) engine inherits**: Haar moment, projectors, energy/resolvent units, C-phase signs — SOUND |
| V2 | `PWP` extracted directly (single-plaquette and domino) | `PWP` = the **charge-conjugation operator** (swaps \(\chi\leftrightarrow\bar\chi\)); eigenvalue \(+1\) on C-even, \(-1\) on C-odd | 3I's literal precondition "`PVP=aP` scalar" is **false on the full manifold**, but… |
| V3 | des-Cloizeaux anticommutator vs scalar reduction on the C-odd subspace | \(\tfrac12\{A,B\}=-A\) **exactly** on C-odd; reproduces certified `b3 = 1975/124848` | …C-parity rescues it: the scalar shortcut is **exact on the C-odd flat band** at O(y³) |
| V4 | **O(y³) through the engine's convention.** 3I-style factorization (energy-path sum × folded coefficient), in the engine's own units \((16-E)/6 = 8/3 - E_{\text{phys}}\), vs the **certified** `su3_domino_d3.spectral_single()` | PASS. vacuum `−9/32`; C-even gap `101/200`; C-odd gap `7/32` — on the real degenerate \(\{3,\bar 3\}\) manifold | The **2-cut resolvent + folding for resonant returns** reproduces certified physics |
| V5 | **4th-order folded coefficient, degenerate non-scalar case.** 3I's *actual* `folded_coefficient_from_denominators` on a degenerate 2-level model with **non-scalar `PVP`**, vs the exact eigenvalue spectrum (trace & det) | PASS through \(y^4\): trace `(1, −129/80, 2873/19200, −281257/4608000)`, det `(−9/4, −109/80, 10433/4800)` | The exact case the engine's own **I0 gate never covered** (resonant intermediate = *other* model-space state) |
| V6 | **Independent representation-layer audit (NO project code).** Cloned public `pyclebsch` at pinned commit `35e3926…`; ran the 30 fusion-tree intertwiner edges through `find_direct_sum`/`calc_dimension` and the 18 unique CGC products through `calc_cgcs`/`check_cgcs` | PASS cold: 30/30 edges reproduced (mult 1, correct dims), 18/18 CGC orthogonality checks pass | **First genuinely third-party confirmation in the program.** The SU(3) group-theory inputs Stage 3G builds and 3H/3I contract are correct |

**Reading of V1–V6.** The contraction *primitive* (V1: SU(3) Haar + projectors, cross-checked
by 3G's intertwiner equality) and the perturbation-theory *bookkeeping* (V4–V5: resolvent
products and des-Cloizeaux folding, including the non-scalar degenerate case) are each
validated against independent references; C-parity (V2–V3) makes 3I's scalar simplification
exact on the band that matters. **New (V6): the representation layer — the 30 fusion edges and
their CGCs — is now reproduced by an external library with no project code in the loop.** These
were the parts most likely to hide a subtle error.

**On Stage 3H (`y4_stage3h_complete_nonresonant_contraction.py`).** This is the *real* global
nonresonant contraction: all 6,598 nonresonant orbits contracted through the 24 trace-corner
variables using the actual Stage 3G path tensors, with extensive internal-consistency gates
(record counts, amplitude histograms). It is **honestly scoped** — its docstring states "this is
not yet the complete H4 … does not claim the final fourth-order band." Note the *shipped verdict*
chain runs `3G → I → J` and does **not** route through 3H; 3H is a standalone exact contraction
of the nonresonant sector, computed by a different code path from 3I but sharing the 3E/3G inputs.
It does not regenerate a known physical constant (its gates are internal, not vs. certified physics).

---

## 3. Residual gaps before "theorem"-strength

1. **Lower-order constant not threaded through 3I's *actual* multi-link contraction code.**
   V1 validates the contraction primitive at O(y²); V4 validates the PT convention at O(y³);
   3G validates the projector/path-tensor equality. But the physical `d3 = −109151/249696`
   (or any lower-order constant) has **not** been regenerated by running 3I's real
   `contract_choice` + folded coefficient on a 3-insertion geometry. The two validated halves
   have not been joined. **Belt-and-suspenders, not a suspected error** — but it is the one
   regression the O(y²)/O(y³) claims passed (lower-order through the same engine) that the
   O(y⁴) claim has not.

2. **No genuinely independent recomputation of the full \(H_4\) *kernel*.** **Narrowed by V6:**
   the representation layer (30 fusion edges + 18 CGC products) is now independently reproduced
   by `pyclebsch` with no project code. What remains un-reproduced is the *downstream* pipeline —
   orbit enumeration → global contraction → folding → real-space assembly → the 189-entry kernel,
   `c4`, and witness — by a second from-scratch implementation. The `pyclebsch` audit's own verdict
   scopes this precisely: public `ymcirc` lacks the d=3 state/Hamiltonian dictionaries, so its
   stated "next implementation target" is to generate those from `pyclebsch` CGCs and project the
   microscopic Hamiltonian onto the certified one-flux basis. Until that exists, the kernel is
   produced once (by 3J); only its *inputs* have an independent check.

---

## 4. Required framing corrections (honesty — non-negotiable)

These are **factual mislabels in the archive**, independent of whether the physics is right.

- **The "independent audit" is not independent.** `y4_final_independent_audit.py` loads
  `DATA_Y4_full_real_space_h4_kernel.json.gz` — the **output of Stage 3J** — and re-runs the
  ~10 lines of downstream arithmetic (apply kernel to the cube state, recompute the
  30-plaquette residual, the `5/48`, the Rayleigh witness), then asserts the same hardcoded
  `c4` and witness. It **re-derives nothing upstream** of 3J: not the orbits, not the
  contraction, not the folded coefficients. It confirms only that 3J did not fabricate its own
  printed verdict.

- **The three advertised SHAs are not three confirmations.** In MAN_FLUX_manifest.md the
  "independent clean-room kernel SHA-256 `635d40fa…`" **is** the 3J output kernel file; the
  "independent audit" reads that file. No script in the archive regenerates the kernel
  (confirmed: only 3J writes it, only the audit reads it).

- **Real-space residual (J1) and momentum-space witness (J2) are two readouts of one
  kernel**, not mutual corroboration. The paper's "Independently, the former flat-branch
  correction…" (abstract) and "Direct evaluation of the same…" (§) overstate this.

- **Action:** remove/replace the word **"independent"** wherever it describes the audit, the
  clean-room kernel, or the momentum-space calculation — in the paper abstract & §, STATE.md
  ("independent kernel-only audit PASS"), DECISIONS #010 ("An independent Bloch witness"),
  and MAN_FLUX_manifest.md. State plainly: one kernel, computed once by 3J, checked for internal
  self-consistency.

- **Constructive replacement (now available).** There *is* a real independence result to cite —
  just at the representation layer, not the kernel: *"The 30 SU(3) fusion-tree intertwiner edges
  and their 18 Clebsch–Gordan products are independently reproduced by the public `pyclebsch`
  library (commit `35e3926…`), with no project code"* (verified cold, V6). Cite **that** as the
  independent check, and state precisely that the real-space \(H_4\) kernel itself is computed
  once and checked for self-consistency, with a fully independent kernel recomputation pending the
  d=3 dictionaries. This is honest and still strengthens the paper.

- **"Criterion resolved / not mathematics at this order / closed" is stronger than the
  backing** while §3 (1)–(2) are open. Choose one:
  - **(a) Earn it:** close §3.1 (run `d3` through 3I's real contraction) **and** §3.2 (a second,
    genuinely independent kernel implementation). Then "theorem" is defensible.
  - **(b) Downgrade the language** to match the evidence: *an exact, reproducible computational
    result — first nonzero bandwidth at \(O(y^4)\); the PT machinery validated at O(y²)/O(y³)
    and on the degenerate non-scalar case; full certification pending the two checks above.*
    Given V1–V5 this is already a **strong** claim.

- **Verify the "we correct a constant in the companion paper" claim** (the `5/481` hop)
  independently before it ships — correcting a published constant is a strong assertion.

---

## 5. What is correctly stated and intact

- Exact \(O(y^2)\) and \(O(y^3)\) flatness (`11/306`, `−109151/249696`); the lattice
  Gauss-law / incidence-factorization mechanism; the all-\(L\) topological degeneracy
  (\(\dim\ker = L^3+2\)); the \(T_1^{+-}\) assignment. (These cleared the same bar — lower-order
  regression + independent cross-check — that the O(y⁴) claim has not yet fully cleared.)
- Scope disclaimers — no all-orders flatness, no convergence, no continuum dispersion, no
  Yang–Mills mass gap — **appropriate and consistent** across paper/STATE/DECISIONS/MANIFEST.
- The dispersion witness framed (paper, bandwidth row) as a **rigorous lower bound** on the
  first nonzero bandwidth coefficient — correct framing for that object.

---

## 6. Recommendation

The result is in good shape and likely correct. **Fix §4 (the "independent" mislabel)
regardless** — it is the kind of claim a careful reader will catch and it is not true as
written. Then either close §3 to earn the theorem, or ship (b) the downgraded-but-strong
computational claim. Do **not** ship the current combination of a theorem-strength statement
with self-referential "independent" certificates.
