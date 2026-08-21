# farsource_gpu — far-source interaction decay J(p,r) (the open Z.B content)

**Created June 13, 2026 (F043 hand-off).** GPU-ready engine to measure the one object the single-link cap-geometry diagnostics (F037–F043) could **not** reach: the exponential decay of the source–source interaction `J(p,r)` over lattice distance — i.e. whether the defect/source field is **massive**, which is exactly the far-source firewall (Z.B / Bałaban far-source stability).

## What it measures and why it is Z.B

The reduction's target is **(TOS+J)**: `E_{μ^{S,s}} X_p ≤ C·q·exp(Σ_r J(p,r))`, with `J(p,r) ≤ C_J e^{-m_J d(p,r)}`. The single-source (s→∞) log-amplification from the tilted measure (1.1) is

  `J(p,r) = log( ⟨X_p X_r⟩ / (⟨X_p⟩⟨X_r⟩) )`,

the log normalized pair-correlation of the defect-indicator field `X`. So **`m_J` is the mass of the defect field**, and Z.B holds **iff `m_J` stays bounded away from 0 uniformly along the AF trajectory**. Along that trajectory β increases as `a→0`, the field becomes more ordered, and `m_J` grows — so the **binding (hardest) case is the coarse, small-β end**. The engine measures the connected correlation `C_c(d) = ⟨X(0)X(d)⟩ − ⟨X⟩²` (FFT, all-pairs, translation-averaged, transverse to the plaquette plane) and reads `m_J` from the **effective mass** `m_eff(d) = log(C_c(d)/C_c(d+1))` with jackknife errors.

`X_p` = defect indicator of the (0,1)-plaquette at each site: `defect` iff `arccos(½ReTr U_p) > θ_thr`. Sweep `θ_thr` (a few thresholds) — `m_J` is a correlation length and is robust to the exact threshold.

## Files

- `ENGINE_OP1_farsource_jdecay_v2.py` — **the engine to run** (CuPy if `--device gpu`, else NumPy). v2 uses the robust effective-mass estimator (works under fast decay) + jackknife. Standalone (no repo imports).
- `ENGINE_OP1_farsource_jdecay.py` — v1 (global log-linear fit; kept for reference, superseded by v2's effective mass).

## Validation (already done on CPU, here)

Gates all PASS: **G-BK** backend quaternion-mul associativity (1.8e-15); **G-FFT** FFT 2-pt == direct (0.0); **G-HB** β=3.5 equilibrium ½ReTr plaquette = 0.768 vs the `su2_hb_v3` reference 0.778; **G-DECORR** config lag-1 autocorrelation ≈ 0 at nsep≥3; **G-MEFF** a reliable effective mass is produced. CPU spot values: β=2.3 → plaq 0.603, defect frac 0.53, `m_J ≈ 4.0` (`m_eff(d)=[3.99, 2.22, 1.44, …]`) — the defect field is already strongly massive (ξ < 1) even at this coarse β. The heat-bath is the validated `su2_hb_v3` checkerboard, ported to the array backend.

## Recommended A100 production run

```
python3 ENGINE_OP1_farsource_jdecay_v2.py --device gpu --L 24 \
    --betas 2.2 2.4 2.6 2.8 3.0 3.5 4.0 \
    --thetas 0.9 1.2 1.5 \
    --nconfigs 200 --nthermal 400 --nsep 20 \
    --out far_L24.json
```
Then optionally repeat at `--L 32` (a few β, to check the `m_J` plateau is L-converged and not a finite-size artifact). Rough A100 cost: L=24 is ~10⁶ sites; a sweep is a handful of vectorized roll/quaternion ops; the whole ladder is minutes-to-low-tens-of-minutes on an A100. L=32 a few× more.

**What to send back:** the `far_L24.json` (and `far_L32.json` if run). They contain, per (β, θ): `plaquette_mean`, `X_mean`, `Cconn[d]`, `G_normpair[d]`, `m_eff[d]` + jackknife `m_eff_err[d]`, the read-off `m_J` ± `m_J_err`, and `corr_len_xi`. I will then fit/plot `m_J(β)` along the trajectory, check the effective-mass plateau, and write the finding: **does `m_J(β)` stay bounded away from 0 toward the coarse end (Z.B supported) or collapse (Z.B in danger)?**

## Honest scope

- This measures the **bare defect-indicator** correlation mass — a clean, standard, conservative proxy for the reduction's smoothed/conditional source `X_{p,η}`. If even the bare-indicator field is uniformly massive, that is strong evidence for Z.B; the exact `X_{p,η}` version is a refinement.
- A finite-lattice `m_J(β)` curve is **evidence**, not the uniform-in-cutoff theorem. It can pin `m_J`, `C_J`, test trajectory-uniformity, and **falsify** a hoped-for bound cheaply — but the closure of Z.B remains analytic.
- SU(2) here. An SU(3) port (replace the quaternion heat-bath with an SU(3) pseudo-heat-bath / Cabibbo–Marinari) is the natural follow-on if the SU(2) signal is encouraging.
