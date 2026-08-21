# Glueball and string-tension normalization audit

**Date:** 2026-06-14  
**Verdict:** variable-label error confirmed; fourth-order glueball kernels survive unchanged.

## 1. Exact lattice coupling

The lattice Hamiltonian is
\[
H_{\beta_{\rm lat}}
=\frac12\sum_\ell C_2(\ell)
+\beta_{\rm lat}\sum_p
\left(1-\frac13\operatorname{ReTr}U_p\right).
\]

Dropping the additive constant gives
\[
H=H_0-\frac{\beta_{\rm lat}}6
\sum_p(\chi_p+\bar\chi_p).
\]

Define
\[
\boxed{u=\beta_{\rm lat}/6=1/g^4}.
\]

Then the perturbation is exactly
\[
V=-\sum_p(\chi_p+\bar\chi_p).
\]

## 2. First-order gate

Using only the SU(3) character moments
\[
\int\chi^3=\int\bar\chi^3=1,
\qquad
\int\chi^2\bar\chi
=\int\chi\bar\chi^2=0,
\]
one obtains
\[
\langle -|(\chi+\bar\chi)|-\rangle=-1,
\qquad
\langle +|(\chi+\bar\chi)|+\rangle=+1.
\]

Therefore
\[
\langle -|V|-\rangle=+1,
\qquad
\langle +|V|+\rangle=-1.
\]

The published glueball first-order coefficients \(\pm1\) therefore fix the
series variable to \(u\), not to \(Y=2\beta_{\rm lat}/3=4u\).

## 3. One-plaquette bridge

Let
\[
h_\alpha=\frac12C_2+\alpha
\left(1-\frac13\operatorname{ReTr}g\right)
\]
be the class Hamiltonian. The lattice one-plaquette restriction is
\[
4h_{\beta_{\rm lat}/4}
=4h_{3u/2}.
\]

Hence the existing bridge
\[
4\Delta_\pm(3u/2)
\]
and all displayed tower coefficients remain correct after renaming the
series variable from the old manuscript \(y\) to \(u\).

## 4. Fourth-order glueball kernels

The exact fourth-order engines contract four plaquette insertions. Replacing
positive character insertions by the physical negative perturbation supplies
the global factor
\[
(-1)^4=+1.
\]

Therefore the 189-record kernels, \(q_N,A_N,B_N\), SOS identity, bandwidths,
and rank-complete fourth-order conclusions are numerically unchanged.

## 5. String-tension correction

The original torelon engine outputs raw positive-character contractions:
\[
\sigma_n^{\rm phys}=(-1)^n\sigma_n^{\rm raw}.
\]

Thus
\[
\sigma_2=-22/153,
\qquad
\sigma_3=-61/408,
\qquad
\sigma_4=-737327120374220449/7250590288602460800.
\]

These agree exactly with KPS Table 2 under
\[
x=2u,
\qquad
\sigma(u)=\frac12W(2u).
\]

## 6. Two valid variable conventions

### Preferred project convention

\[
u=\frac1{g^4}.
\]

The existing glueball coefficients remain unchanged.

### Old manuscript convention

\[
Y=\frac4{g^4}=4u.
\]

Every coefficient at order \(n\), including all glueball coefficients, must
be divided by \(4^n\).

The alternative agent converted the string table correctly in \(Y\), but
then combined it with unrescaled glueball coefficients from \(u\). That
mixed-variable ratio is not valid.

## 7. Remaining provenance issue

The lower-order scripts named in the paper for the exact third-order domino
calculation are absent from the current release. This audit does not recreate
that source chain. The fourth-order normalization conclusion is independent
of that omission.
