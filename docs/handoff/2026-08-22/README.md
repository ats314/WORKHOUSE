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
