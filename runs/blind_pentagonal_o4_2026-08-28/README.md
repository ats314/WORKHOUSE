# Target-blind pentagonal fourth-order run — 2026-08-28

The first execution in this repository of a **target-blind** fourth-order
engine. `backend_full_link_balanced_control.py` reached the session on
2026-08-28, after the notes-graph pass proved it was missing from every
inventory; it is pinned verbatim at
`notes/imported/UPLOADS_2026-08-28c/backend_full_link_balanced_control.py`
(sha256 `a938e466…`) and was run unmodified on this container
(CPython 3.11.15, sympy 1.14.0).

## Why "blind" is a measurement here, not a claim

The engine's own docstring says it computes the coefficient "without importing
a target coefficient or any stored microscopic amplitudes" and that its
"source intentionally contains no claimed final numerator or denominator".
That is the author's word. The machine statement of the same thing: this
repository's coefficient-signature scanner — the one `workhouse triage` points
at any unpinned archive — finds **zero** registered coefficient signatures in
these bytes. The engine cannot have been fitted to a number it does not
contain.

## What it produced

| Quantity | Cold value |
|---|---|
| `A_+` (endpoint `+cap1`) | `6482621/21879000` |
| `A_-` (endpoint `-cap1`, signed) | `-9714969/32784500` |
| `h_4^side` | `-2861009/84387303000` |
| `tau_4` (five sides) | `-2861009/16877460600` |

24/24 internal gates passed, including the two balanced-control gates that
remove the determinant and `(4,1)` invariant ranks, D5 rotation covariance of
the fixed-side trace, and the vanishing of all 28 proper-return Q-chain
contributions.

## What it changes

`h_4^side` was already registered and already checked as `A_+ - A_-`. What was
*not* established is where `A_+` and `A_-` come from: both were transcriptions
from the corpus. This run derives **both amplitudes independently**, from
oriented prism geometry, exact Wilson trace-word algebra, the SU(N) Fierz
identity, exact SU(3) Haar projectors and exact reduced resolvents —
enumerating all 48 fixed-side endpoint histories and the 20 P-irreducible ones.
The agreement is exact, on both amplitudes, not merely on their difference.

## What it does NOT change

**It does not adjudicate C2, and must not be read as doing so.** `h_4^side` is
the *pentagonal-prism side* coefficient; the registry's own note says
"separate geometry; does not bear on the cubic kernel", and the check
`h_4^side and the cubic kernel share no denominator structure` is the machine
form of that separation. The disputed off-axis `C_shp` lives in the cubic
kernel and is untouched here. Neither side is preferred, and G3 remains open:
what it asks for is a blind run on the *marked-cluster cubic* engine, which is
a different program from this one.
