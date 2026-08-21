# Global O(y^4) band-edge certificate — PROVED

- Kernel: `/mnt/data/_y4run/DATA_Y4_full_real_space_h4_kernel.json.gz`
- SHA-256: `635d40fa8a5d7da841fd30f36185eb96f14ec4c040678ddd8fb010379afb2900`
- Records: **189**
- Basis order: `[(0, 1), (0, 2), (1, 2)]` (bound directly from kernel metadata)

## Exact candidate edges

- Gamma: `c4 = -20721577909065127111/7250590288602460800` = -2.857915988114559
- X: `c4 = -17700498622147435111/7250590288602460800` = -2.441249321447892
- M: `c4 = -4367164159624988707/1812647572150615200` = -2.409273720232096
- R: `c4 = -3447362930970494909/1450118057720492160` = -2.377298119016299
- R-Gamma: `132329431693349/275331901291200` = 0.48061786909826

## Proof reduction

The projected coefficient is `c4=N/D`, where `D=||psi||^2`. The code constructs the exact Laurent
polynomials and certifies the two division-free inequalities:

- `Qmin=N-c4(Gamma)D >= 0`,
- `Qmax=c4(R)D-N >= 0`.

Local zeros are handled by exact Taylor lower bounds; all remaining boxes are handled by interval
branch-and-bound on `[0,pi]^3`, justified by exact independent-reflection symmetry.

## Machine result

```json
{
  "minimum": {
    "name": "GLOBAL MINIMUM AT GAMMA",
    "proved": true,
    "processed_boxes": 1590,
    "interval_pass_boxes": 739,
    "local_taylor_pass_boxes": 88,
    "max_depth": 12,
    "elapsed_seconds": 5.90081524848938,
    "unresolved_boxes": 0,
    "worst_interval_lower_seen": "[-0.57068289261897391386215998370396051876772874332484, -0.57068289261897391386215998370396051876772874323726]"
  },
  "maximum": {
    "name": "GLOBAL MAXIMUM AT R",
    "proved": true,
    "processed_boxes": 76,
    "interval_pass_boxes": 68,
    "local_taylor_pass_boxes": 2,
    "max_depth": 3,
    "elapsed_seconds": 0.25457048416137695,
    "unresolved_boxes": 0,
    "worst_interval_lower_seen": "[-1.9705759654567740059864947265014445596128683557639e-46, -1.9705759654567740059864947265014445596128683557639e-46]"
  },
  "overall_proved": true
}
```

## Verdict

**PROVED.**
