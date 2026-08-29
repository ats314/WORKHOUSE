# The two-cube closure: -1/12 and +5/612 on a genuine face-sharing space

Delivered 2026-08-29, the day of the final-paper draft: the first multi-cube
operator result in the corpus. Everything before this inferred the adjacent
hopping coefficient from an isolated cube or a graph ansatz; this derives it
on an actual open face-sharing `(3,2,2)` two-cube SU(3) Hilbert space
(8,361 states at B=4; 1,590,462 at B=6), with left-cube, right-cube and
shared-face contributions subtracted at the **operator level** (literal
Moebius fold), target-blind, and with the complete 22-state `E* = 8/3`
eigenspace removed from the resolvent.

    B = 4 two-cube    K_conn = -(1/12)  G_conn + D_B4   spectrum {0, (-15/4)^2, (-11/6)^4, (-5/3)^4}
    B = 6 two-cube    K_conn = +(5/612) G_conn + D_B6   spectrum {0, (-15/4)^2, (-34/9)^4, (-129/34)^4}

The B=6 coefficient is the registry's own `t_3 = 5/612` (T0,
`LEAN:hopping_three`), recovered blind on the two-cube space, with the
six-channel mechanism exposed: legacy channels sum to `-51/612`, the restored
`6`, `bar6`, `8` channels to `+56/612`, and the adjoint route (`+16/51`)
forces the sign reversal. The channel list is *provably* closed at B=6 at
this order (endpoint Casimir budgets 6 and 17/3, both inside B=6, both
outside B=4) — the check suite re-derives that.

## What travelled, and what did not

Five files: the B4 and B6 derivation notes, the B6 certificate, the B6
detached 43-role manifest, and the synthesis theorem note. The delivered
subset is byte-consistent with its own authority chain: both notes hash to
the values the manifest and theorem note pin, the certificate matches the
manifest's record, and the manifest hashes to the theorem note's declared
B6 root `021558ce…`. The NPZ artifacts, history ledgers, builders and the
pinned pyclebsch archive did **not** travel, so the 1.59M-state construction
was not re-run here; `src/workhouse/invariants/two_cube.py` audits the
certificate's arithmetic against geometry rebuilt locally, the same posture
as the one-cube B=6 audit.

## Scope — read before citing this in the paper

Second order in `u`, finite volume, strong coupling, one sector. The
delivery's own theorem note says it plainly: no cubic off-axis, rooted
fourth-order scalar, pentagonal, continuum, or infinite-volume claim
changes. **This does not adjudicate C2** (`C_shp` is fourth order). What it
retires is the one-cube-only objection to the second-order channel
mechanism, and it demonstrates, end to end, the target-blind operator-level
machinery a fourth-order adjudication (G3) would need. `D_B6` is
B6-truncated and not proved cutoff-stable; the finite-u validation is a
66-dimensional star, not the full Hamiltonian; no external group has
reproduced the release.
