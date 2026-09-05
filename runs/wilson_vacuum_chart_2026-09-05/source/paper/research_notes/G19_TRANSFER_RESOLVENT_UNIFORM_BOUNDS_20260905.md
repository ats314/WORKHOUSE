# Uniform reduced-resolvent bounds for the actual transfer step

Derived 5 September 2026 in the WORKHOUSE continuation. This note concerns the
actual symmetric transfer's second-order weight from
`G19_UNIFORM_WILSON_WINDOW_20260904.md`, Section 5:

\[
d_\tau(\Delta)=\frac{\tau}{2}\coth\frac{\tau\Delta}{2},\qquad \tau>0.
\]

It supplies an entire-spectrum propagator bound for the operator chart in
`G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md`. No representation cutoff,
finite spectral upper bound, or spatial volume enters the constants.

## Scalar estimate

For every real \(\Delta\ne0\),

\[
\boxed{\left|d_\tau(\Delta)-\frac1\Delta\right|
\le\min\left\{\frac\tau2,\frac{\tau^2|\Delta|}{12}\right\}.}
\tag{1}
\]

The difference has the same sign as \(\Delta\). To prove this, oddness reduces
to \(\Delta>0\); put \(x=\tau\Delta/2\). Define

\[
A(x)=x\cosh x-\sinh x,\quad
F(x)=(1+x^2/3)\sinh x-x\cosh x.
\]

Both vanish at zero. Their derivatives satisfy

\[
A'(x)=x\sinh x\ge0,\qquad F'(x)=xA(x)/3\ge0.
\]

Since \(\sinh x>0\), these inequalities give
\(0\le x\coth x-1\le x^2/3\), proving the second bound in (1).
Also \(e^{2x}-1\ge2x\), so
\(\coth x=1+2/(e^{2x}-1)\le1+1/x\); this proves the first bound.
This is an analytic proof, not an inference from a numerical scan.

## Operator consequences

Let \(A\) be any self-adjoint operator with
\(\operatorname{spec}(A)\subset(-\infty,-\gamma]\cup[\gamma,\infty)\),
where \(\gamma>0\). Functional calculus applied to (1) gives bounded operators
and the dimension-independent estimates

\[
\boxed{\begin{aligned}
\|d_\tau(A)\|&\le\gamma^{-1}+\tau/2,\\
\|d_\tau(A)-A^{-1}\|&\le\tau/2,\\
\|(d_\tau(A)-A^{-1})|A|^{-1}\|&\le\tau^2/12.
\end{aligned}}
\tag{2}
\]

The inverse and all displayed products commute because they are functions of
the same self-adjoint operator. Thus (2) also applies to a reduced kinetic
operator on a shell complement, including intermediates below the shell.
For \(B,C\) bounded between the appropriate Hilbert spaces,

\[
\|B[d_\tau(A)-A^{-1}]C\|\le\tfrac\tau2\|B\|\|C\|.
\tag{3}
\]

If the range of \(C\) lies in the domain of \(|A|\) and \(|A|C\) is bounded,
the sharper energy-weighted estimate is

\[
\|B[d_\tau(A)-A^{-1}]C\|
\le\tfrac{\tau^2}{12}\|B\|\,\||A|C\|.
\tag{4}
\]

At fixed nonzero \(\tau\), the scalar discrepancy approaches \(\tau/2\) as
\(\Delta\to+\infty\). Consequently an unweighted uniform
\(O(\tau^2)\) bound over arbitrary unbounded spectra cannot replace (2).
The constant \(1/12\) in the energy-weighted estimate is attained as a limit
when \(\tau|\Delta|\to0\).

## Application and boundary

The chart's first local rotation uses \(d_\tau(E_s)\). For
\(0<\tau\le\tau_0\), its stated first-derivative bound therefore obeys

\[
16J(s+2d_\tau(E_s))\le16J(s+2/E_s+\tau_0).
\]

This gives explicit mesh-independent control of the propagator factor used
by that derivative. It does not construct an exact nonlinear vacuum chart,
prove a linked operator-activity majorant, control the extensive norm of a
global interaction, or establish thermodynamic source totality. In
particular, (4) requires its stated energy-weighted interaction hypothesis;
boundedness of a multiplication operator alone does not supply it.

The result preserves the actual transfer weight. It does not identify the
transfer logarithm with the auxiliary Hamiltonian \(K_\epsilon-uV\), nor does
it establish a spatial continuum limit. No global novelty claim is made.
