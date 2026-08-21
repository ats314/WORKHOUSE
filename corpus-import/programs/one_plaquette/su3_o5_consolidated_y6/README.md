# SU(3) consolidated through O(u⁵) + Y6 (sixth-order) preflight — intake (2026-06-14)

**What this is.** Alex's consolidation pass: it merges the verified fifth-order glueball
calculation with the normalization-corrected string tension into one O(u⁵) statement
(u = β_lat/6 = 1/g_H⁴), and records the **first completed sixth-order (Y6) components** —
the folded/des-Cloizeaux path weights and the universal local-carrier census — as the
groundwork for the one remaining unknown, m₆. Intaken after independent cold verification.
**Also carries the canonical-archive decisions** (`NOTE_SU3_canonical_archive_matrix.md`) — see the
normalization note below; it supersedes part of `../su3_string_tension/`.

## Headline results

**Exact one-flux C-odd rest mass through O(u⁵):**
\[
m_{1^{+-}}(u)=\tfrac83+u+\tfrac{11}{306}u^2-\tfrac{109151}{249696}u^3
-\tfrac{20721577909065127111}{7250590288602460800}u^4
-\tfrac{866236750503342026253096691057}{1169668083793811403447133488000}u^5+O(u^6).
\]
So **m₅ = q₅** (the Y5 fifth-order value) **— this resolves the "m₅ unassigned" gap** noted in
`../su3_string_tension/`. Fifth-order band: c₅(k)=q₅+(A₅Q+B₅R)/2S, A₅=313/240, B₅>0, Δc₅=A₅+B₅
(both shape coeffs positive ⇒ Γ min, R max). m₆ remains the single open coefficient (§6 lays out the
execution path: zero-momentum q₆ first, external-memory sharding, fusion-path basis).

**⚠ String-tension normalization — CORRECTED (canonical):** the bridge is
\[ \boxed{\sigma(u)=\tfrac12 W(2u)} \quad\Rightarrow\quad \sigma(u)=\tfrac23-\tfrac{22}{153}u^2-\tfrac{61}{408}u^3-\tfrac{737327120374220449}{7250590288602460800}u^4+O(u^5). \]
The older **(−1/4)ⁿ conversion is SUPERSEDED** (mixed-variable normalization; must NOT be combined
with the glueball coefficients). This changes the mass-to-string-tension ratio: m/√σ = √6 Σcₙuⁿ with
**c=[4/3, 1/2, 11/68, −7559/499392, −15752822901180179/12642703205932800, …]** (note c₂=**11/68**, not the
O6 bundle's 11/408). σ₅, σ₆ are exact **historical KPS targets** (given in the theorem), **not yet
project-native reruns**. (See `../su3_string_tension/README.md` — corrected this pass to point here.)

**Y6 (sixth-order) preflight — folded terms CLOSED:** the folded/des-Cloizeaux recurrence is verified at
six insertions (all 32 resonance-denominator patterns finite, path-reversal symmetry, nonresonant
resolvent-product limit, 4 rational-matrix comparisons full-vs-folded). The universal local-carrier
census: of 3⁸−1=6560 link signatures, **2,186 are SU(3)-feasible** (triality-zero), covering sectors
(0,3),(0,6),(1,1),(1,4),(1,7),(2,2),(2,5),(3,3),(4,4) — the new sixth-order sectors being the balanced
(4,4) and double-determinant (0,6),(1,7); max singlet fusion-path multiplicity 23, max irrep dim 27.
⇒ the fusion-path representation can carry every sixth-order local sector without hand-picked ε-δ cases.

## Verification this session (T1 machine-gated + independent cross-check)

Cold-run (clean sandbox, Python 3.10, sympy 1.14.0, no caches):

| script | result |
|---|---|
| `ENGINE_SU3_verify_o5_consolidated.py` | **ALL GATES PASS** (source-hash checks of Y5 + normalization certs; m₅ exact; σ₅/σ₆ targets exact; ratio coeffs through O(u⁵); folded + local Y6 preflights; double-determinant sectors present; m₆ flagged unresolved) |
| `ENGINE_Y6_folded_descloizeaux_preflight.py` | **ALL GATES PASS** (4th-order regression; 32 resonance patterns finite; path-reversal; nonresonant product; 5th + 6th order random-matrix regression) |
| `ENGINE_Y6_local_fusion_path_preflight.py` | **ALL GATES PASS** (2186 feasible signatures all triality-zero; (4,4),(0,6),(1,7) present; nonempty path basis every record) |

**Independent cross-check (mine).** I re-expanded m(u)/√σ(u)/√6 in sympy from the §1/§3 series and reproduced
**c₀,c₁,c₂ = 4/3, 1/2, 11/68 exactly** — confirming the corrected normalization (and that c₂≠11/408).
m₅=q₅ confirmed against the independently-verified Y5 value.

**Scope honesty.** T1 (machine-gated, cold-reproduced) + an independent ratio cross-check. The Y6 work is a
**preflight** — folded terms + carrier census are done/closed; **m₆ itself is NOT computed** (open). σ₅,σ₆
are historical KPS targets, not project-native. Not T2/T3; not "established."

## Provenance
- Source: `C:\ALL THEORY\ZIP ARCHIVES\SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14.zip` — md5 `f75790b2dc29eacd3fe02c8493c6d644` (uploaded by Alex 2026-06-14; the other 7 files in that upload were byte-identical re-uploads of bundles already in ZIP ARCHIVES — no action).
- `sources/` holds the Y5 + O4-normalized certs/theorems this consolidates (the verifier hash-checks them). Per-file MD5 in `MAN_SUN_md5sums.txt`.

## Added 2026-06-14 (later uploads)
- **`AUDIT_STRING_m6_sigma56_execution_report_2026-06-14.md`** — honest progress on the two open items. **m₆ local-algebra layer
  CLOSED + verified**: all nine sixth-order sectors' invariant dimensions exact (matching the fusion-path census;
  explicit edge tensors for the new (0,6) double-determinant etc. built to machine precision), electric-energy ladders
  tabulated, censuses independently reproduced (2186, 140). **m₆ itself remains open (HPC-scale)**: the connected
  six-insertion geometry census + global Γ-contraction are the remaining blockers — **m₆ not determined, nothing fabricated.**
  σ₅,σ₆ stay KPS historical targets (native torelon engine absent); the ratio series re-verified exactly; sensitivity
  1% σ₅ → 0.30% of c₅ (soft).
- **`AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`** — the basis for the σ(u)=½W(2u) correction; pins **u=β/6=1/g_H⁴**,
  gives the one-plaquette bridge 4Δ₋(β/4)=8/3+u+½u²+7/32u³, and the full σ and ratio coefficient tables in u. **Also flags a
  manuscript erratum**: the flat-band paper's `y=2β/3` definition is wrong by 4× (coefficients are correct in u; see
  `../../../papers/flat_band/AUDIT_FLUX_normalization_erratum_2026-06-14.md` — confirmed at v0.8 .tex line 233).

## Open / next (per the doc's §6 + CANONICAL_ARCHIVE_MATRIX)
- **m₆** = the highest-value open physical coefficient (zero-momentum q₆): connected six-insertion census (6.68M support classes at O5), triality/C reduction, fusion-path basis, contract zero-momentum trace first.
- σ₅, σ₆ project-native reruns (currently historical-KPS only).
- Canonical-archive decision recorded: do NOT spend the next cycle repairing SU(4) packaging; m₆ is the target.
