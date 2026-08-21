# Flat-band paper v0.8 — normalization-definition erratum (2026-06-14)

> **✅ FIXED 2026-06-14 (Alex: "proceed") → `glueball_flat_band_paper_v0_8a.tex/.pdf`.** The corrected
> version defines $y=\beta/6=1/g_H^4$ (was $y=2\beta/3$); the bridge text now reads "evaluate the
> one-plaquette gap at the local class coupling $b=\beta/4=3y/2$" and the formula $4\Delta_\pm(3y/2)=4\Delta_\pm(\beta/4)$.
> **All displayed coefficients are unchanged** (they were always the $u=\beta/6$ values). Recompiled clean
> (pdflatex ×2, 22 pp, byte-verified copy-back, page count identical to v0.8). The original v0.8 .tex/.pdf are
> retained unchanged (they match the archive bundle). Only three lines changed: the \thanks version note, the
> definition (eq. line 233), and the bridge-justification sentence. Details at the bottom of this note.

**Confirmed this session; the fix is now applied in v0.8a (original v0.8 retained for provenance).**

## The issue
v0.8's `glueball_flat_band_paper_v0_8.tex` **line 233** defines the expansion variable as
\[ y = \tfrac{2\beta}{3}, \qquad \beta=\tfrac{3y}{2}. \]
Alex's `AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md` (in `../../programs/one_plaquette/su3_o5_consolidated_y6/`)
shows this definition is **wrong by a factor of four**. The source contraction inserts unit powers of
\(-(\chi_p+\bar\chi_p)\) from \(H_\beta = H_0 - \tfrac{\beta}{6}\sum_p(\chi_p+\bar\chi_p)\), so the natural and
**correct** variable is
\[ \boxed{y = \tfrac{\beta}{6} = \tfrac{1}{g_H^4}} \quad(\text{not } 2\beta/3). \]

## Why it's only a definition error (coefficients are fine)
The displayed coefficients (tower 8/3 + y + ½y² + 7/32 y³ + …; q_N, A_N, B_N; σ-series) are the **correct
u=β/6 values** — they match the one-plaquette bridge `4Δ₋(β/4) = 8/3 + u + ½u² + 7/32 u³` exactly. Only the
*stated definition* y=2β/3 is inconsistent with them. (If one insisted on keeping y=2β/3, every order-n
coefficient — all q_N, A_N, B_N — would have to be divided by 4ⁿ, e.g. A_Y=A_u/256; the band edges, positivity,
factorization, and onset order are invariant under the rescaling.)

## Recommended fix (the audit's "least disruptive repair")
Change the definition to **y := β/6 = 1/g_H⁴** throughout; **all computed coefficients then remain unchanged.**
Touch points to sweep when editing: line 233 (`y=2β/3, β=3y/2` → `y=β/6, β=6y`) and any later place that uses the
β↔y relation or restates it (also confirm §"Setting" / the string-tension and ratio sections use σ(u)=½W(2u),
ratio c₂=11/68). This was **not** edited this pass — manuscript framing is Alex's call (GUARDRAILS #9). Say the word
and I'll do the full sweep + recompile.

## Status
Coefficients/geometry: **correct** (u=β/6). Manuscript variable definition: **CORRECTED in v0.8a** (was `y=2β/3`, now `y=β/6=1/g_H⁴`).
Source: `AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md`; confirmed by direct grep of the v0.8 .tex (line 233); fix in v0.8a verified (compiles, 22 pp, definition + bridge render correctly, only "2β/3" left is this erratum's own footnote).
