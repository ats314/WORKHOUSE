# Settlement package — what settles what

Three tools, in increasing order of what they decide. All were executed against the
corpus during consolidation on 2026-08-20; results below.

## 1. verify_master_identities.py  — RAN, 66/66 PASS
Independent re-derivation of every claim settleable by finite exact computation,
importing no corpus code. Highlights: incidence factorization + flat eigenvector +
spectrum proved symbolically; Betti formula re-proved on freshly built boundary
matrices for T^3, T^2xI, I^3 (both conventions), including the b2=3 pinning count
under a cube-channel perturbation; Wick moments re-derived from explicit index-sum
pairings at N=3,4; Delta_res = -205*sqrt(6)/3072 rebuilt from the Laguerre recurrence;
the odd-sector certificate table (N=3..12) regenerated from closed forms; the full
m/sqrt(sigma) ratio series; all fourth-order pencil algebra including the v3.1
stencil and its Fourier-symbol identity; the dispute arithmetic.
Run:  python3 verify_master_identities.py     (needs sympy; ~4 min)

## 2. Cold reruns of the two in-corpus audits — RAN, both re-certify
- cold_rerun_stranded_flux_audit.txt      : 8/8, ZERO_BACKEND_FALSIFIED
- cold_rerun_pentagonal_frontier.txt      : 8/8, raw Gram/Haar frontier closed
(SOURCE_SHA256 differs from the archived runs only because output paths were
patched; the physics code is byte-identical upstream of that.)

## 3. mce_adjudication_harness.py — the actual dispute decider (needs your A100)
Frozen-protocol driver for the marked-cluster engine, per GLUE3 v3.1 §18.1.
Verified in sandbox through: contamination scan (engine source is clean of all
quarantined target constants), engine self-test 47/47, geometry preflight
(609 evaluations, coverage SHA match, zero physics), sealed-memfd authenticated
launch (the missing Colab bootstrap, reimplemented), first Phase-3 cluster
evaluation started, checkpoint written, interrupt + resume verified.

On the production box (Linux; the A100 machine that did the 15-hour run):
    python3 mce_adjudication_harness.py --engine Hodge_SU3_Exact_MarkedCluster_m4_Colab.py freeze
    python3 mce_adjudication_harness.py --engine Hodge_SU3_Exact_MarkedCluster_m4_Colab.py run
        # long; interrupt/resume freely; RESUME_SECRET.json (chmod 600) must be kept
    python3 mce_adjudication_harness.py --engine Hodge_SU3_Exact_MarkedCluster_m4_Colab.py adjudicate

The adjudicate stage unquarantines the comparison targets ONLY after verifying the
sealed certificate hash, then reports: nearest scalar anchor (RUN15 linked oracle
vs historical q_old vs quarantined shortcut), the vacuum-ledger test
q_old - E0^(4) =? m_Gamma (protocol item 9) if the certificate carries E0^(4),
and the shape adjudication (A =? 5/48, B,D =? 0, C vs C_old vs C_new, blind R
holdout) if it carries a kernel block. Items the certificate cannot discharge are
reported OPEN and the verdict is labeled PARTIAL — the harness will not overstate.

## Still NOT settled by anything here
- The C^shp / rest-scalar dispute itself: requires the `run` stage on real hardware.
- h4_side: requires the pentagonal Fierz/resolvent closure engine (buildable next;
  the frontier and all its gates are re-certified above, so the launchpad is warm).
- Record-backed ledgers (Q32, P402, N>=9 kernels): require restored artifacts, not code.
