# CBB finite-N bridge certificate, re-run here

`verify_cbb_tn_bridge.py` as received, executed unmodified in this session.
Standard library only, exact `Fraction` arithmetic, and it imports nothing
from WORKHOUSE — it rebuilds the SU(3) channel weights from dimensions and
Casimirs and the cubical boundary matrices from oriented cell boundaries.

    python3 verify_cbb_tn_bridge.py --output su3_finite_n_bridge_certificate.json

Result: **18/18** exact gates. The JSON written here is identical, key for
key and value for value, to the certificate that arrived with the documents
(`notes/imported/UPLOADS_2026-08-28e/su3_finite_n_bridge_certificate.json`),
so the received certificate is what this program actually prints.

## What this run does and does not establish

It establishes that the arithmetic is right: the four channel weights, the
sums `A_3 = -27/68` and `B_3 = -7/18`, `t_3 = 5/612`, the `T_1` cutoff value
`-1/12` and its completion `w_6 - w_8 = 14/153`, and both finite-volume
incidence spectra over the rationals.

It does not establish the bridge's *physics* premise — that the published
Ciavarella–Burbano–Bauer matrix element is the one this weight formula should
be fed, and that the four channels exhaust the second-order shared-link
routes in this sector. That premise is argued in prose in the two imported
documents and is T3 here.

Note that the derivation chain the certificate walks is **already** T1-checked
in this repository, in the "second order, all ranks" suite, from the corpus's
own appendix. This run's value is that the same numbers come out of a program
with no WORKHOUSE imports, and that the truncation diagnostic and the
finite-volume fingerprints — which the registry did not carry — check out.
