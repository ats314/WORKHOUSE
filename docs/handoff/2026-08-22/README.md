# Session handoff, 2026-08-22 — UNREVIEWED agent work products

Everything in this directory is **T3**: produced by background research
agents in the session that discovered and ran the marked-cluster engine
(see runs/mce_freeze_and_first_run_2026-08-22/). None of it has been
adjudicated by the maintainer or registered as a check. It is preserved
here so the scripts and numbers survive the session container; the full
agent reports are in the session's pull-request description
(the PR that added this directory).

| File | What it claims (unverified) |
|---|---|
| `g23_nu_measure_prototype.py` + `sweep_output.txt` | G23 ν-measure prototype (quartic 0+1D transfer kernel, exact quadrature): ν ∝ e^(−S_sp) is NOT the true slice marginal in the interacting case (tail class |φ|³ vs φ⁴; TV diverging as a→0), the Markovization of the archive's own symmetrized strip operator forces ν_true canonically, and the corrected scale-a comparison passes the interacting test with uniform c ≈ ½ (inf 0.512 over the sweep), certifying ≥ 0.999·Δ_OS end-to-end. |
| `run_h_phys.py` + `h_phys_run.log` | G20: first-ever execution of the imported H_phys spec/tools (digests verified against ledger/notes.yaml before running). Plaquette cluster: H_phys(0) = I/4 to 1.9e-16; λ_min rises with radius; interlacing argument that the refuted 0.248 decline is impossible for the Haar-only potential under the pinned convention. Two-plaquette run was still in flight at session end. |

Next-session intake: recompute before registering anything —
the agents' own instructions forbade them from writing checks, and this
directory must not be cited as evidence for any claim.

## Intake, 2026-08-22 (same day)

Done. Nothing here was re-run: this repository's dependency set is
sympy + PyYAML + python-flint, and both scripts above need numpy/scipy
(and, for `run_h_phys.py`, torch), so re-running them would have imported
a float stack the checks cannot use. Each claim was instead **re-derived
exactly**, and six checks were registered in the notes-program suite
(`workhouse verify --tier 1`). Two came out *stronger* than the sweeps:

| Sweep said | What is registered |
|---|---|
| `H_phys(0) = I/4` to 1.943 x 10^-16 | `Hess V_Haar(0) = (C_A/12) I = I/4` **exactly** — the su(3) adjoint Casimir in the pinned convention is exactly 3, so the residual was the float shadow of a rational |
| plaquette (dim 8) and two-plaquette (dim 16) agree | agreement is an **identity**: `Pi_phys` has orthonormal columns, so `Pi^T (I/4) Pi = I/4` for every cluster — not independent evidence |
| lambda_min rises with radius | radial second derivative `>= |x|^2/4` for **every ray and radius**, from the Weyl form plus all-positive Taylor coefficients (bounds the radial curvature, *not* lambda_min of the full Hessian) |
| uniform `c ~ 1/2`, "inf 0.512" | `c_1 = (1-e^-theta)/(1-e^(-2 sinh theta))` exactly, least of the modes, `> 1/2` at **every** spacing, infimum exactly `1/2` and never attained — 0.512 was only the smallest sampled `a` |
| Markovization forces `nu_true` | registered as a FINDING with an exact rational witness: `e^(-S_sp)` cancels for *arbitrary* kernel and spatial action |

Two corrections to the table above, from reading `h_phys_run.log` itself:

- "Two-plaquette run was still in flight at session end" is not what the
  log shows. `two_plaquettes_shared_link` / `total_radius` **completed**
  (409.3 s, `H_phys(0) = I/4` to 2.220 x 10^-16, dim_hor 16). Only the
  `per_link_radius` leg of that cluster died with the container.
- The interlacing argument is sound but was stated too strongly. It gives
  `lambda_min(H_phys) >= lambda_min(H_tot)` and an exact value at the
  origin; it does **not** bound `lambda_min` of the full Hessian away
  from the origin. The registered check says only what is proved.

Still T3 and unregistered: everything about the **interacting** case in
`g23_nu_measure_prototype.py` (the quartic transfer kernel, the tail-class
argument, the TV growth as `a -> 0`, and the interacting `c ~ 1/2`). Those
rest on float quadrature on a finite grid and would need either a
rigorous quadrature bound or a numpy-bearing environment declared as a
dependency. The ledger entries for G20 and G23 record all of this.
