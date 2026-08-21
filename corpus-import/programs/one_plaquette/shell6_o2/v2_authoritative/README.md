# Exact shell-six O(u²) SU(3) release V2

## Scope

This release computes the complete connected second-order effective matrix in
the 44-state shell-six Wilson-loop space using

\[
u=\frac{\beta_{\rm lat}}6=\frac1{g^4},
\qquad
H=H_0-uW.
\]

The exact trace-word resolvent retains non-simple octet, sextet, and epsilon
intermediate sectors. The 44 basis states reduce to three \(O_h\) orbits of
sizes

\[
12+24+8.
\]

Only three exact columns are computed; every other column is reconstructed by
symmetry and subjected to stabilizer, Hermiticity, \(O_h\), and charge-
conjugation gates.

## Reproduce

```bash
bash ENGINE_STRING_reproduce.sh
```

A clean run requires no precomputed cache and ends with

```text
ALL SHELL6 V2 REPRODUCTION GATES PASS
```

## Main shell-six results

The shell-six \(T_1^{+-}\) branches are

\[
\begin{aligned}
E_{6,-}(u)
&=4-\frac{2\sqrt2}{3}u+
\left(-\frac{13029053}{959310}-\frac{\sqrt2}{2}\right)u^2+O(u^3),\\
E_{6,0}(u)
&=4-\frac{52959}{3553}u^2+O(u^3),\\
E_{6,+}(u)
&=4+\frac{2\sqrt2}{3}u+
\left(-\frac{13029053}{959310}+\frac{\sqrt2}{2}\right)u^2+O(u^3).
\end{aligned}
\]

The exotic ordering satisfies

\[
E_{3^{+-}}-E_{0^{--}}
=
-\frac{1107923}{959310}u^2+O(u^3),
\]

so \(3^{+-}\) lies below \(0^{--}\) at second order.

## Shell-four/shell-six coupling

The exact projected coupling strengths are

\[
g_-^2=\frac49,\qquad
g_0^2=\frac89,\qquad
g_+^2=\frac49.
\]

Explicitly coupling the shells requires unfolding the virtual-shell
contributions already present in the separate perturbative series. The
shell-four diagonal becomes

\[
m_{2,\rm unfolded}=\frac{419}{306}.
\]

See `THM_SHELL6_shell46_theorem_v2.md` for the complete four-state normal form.

## Interpretation

The connected shell-six matrix omits disconnected vacuum bubbles, which are a
common scalar and cancel in channel ordering. The finite-\(u\) CSV scan is a
truncated \(O(u^2)\) diagnostic only; it is not a continuum prediction.
