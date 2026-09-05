# Working backward from a finite glueball mass to the Wilson endpoint

5 September 2026. Conditional reverse constraints and an exact OS blocking
intertwiner. This note uses the project's existing G19 scaling and atom
passage arguments; it assumes no numerical glueball value and does not
infer a theorem from phenomenological data.

## 1. Specify the physical target before rescaling the lattice answer

Fix a physical source channel and momentum, or first work in a box of
fixed physical volume. A candidate nonzero continuum glueball contribution
is a spectral atom

```text
mu({M})=Z>0,  0<M<infinity.
```

The spectral measure is that of a renormalized source in physical energy
units. On the infinite translation-invariant lattice, an entire moving
band need not be an atom of a localized source: its momentum integral is
usually continuous. The fixed-momentum or fixed-physical-volume convention
must therefore be retained when applying the atom-passage proposition.

A nonzero mass in the charge-odd channel is different from the overall
Yang-Mills mass-gap statement. It bounds the global physical gap from
above if that excitation exists; it supplies no lower bound on other
sectors. A full mass gap requires a positive energy bound on the entire
physical vacuum complement, or an equivalent complete spectral argument.

The new Wilson theorem supplies both a fixed-cutoff full transfer vacuum
gap and a complete odd band with literal sources. It gives a controlled
infrared spectral object to which a reverse continuum construction could
connect. Its small-coupling domain does not already contain the
ultraviolet continuum trajectory.

## 2. Necessary energy and clock behavior at the fine cutoff

Write the physical/electric energy conversion as

```text
H_phys(a)=c_H(a) g_H(a)^2 H_el(a)/a,
c_H(a)->c_H>0,
u(a)=g_H(a)^(-4).
```

If an electric-time transfer block has duration `s_a`, its physical
duration is

```text
h_a = a s_a/[c_H(a) g_H(a)^2].                           (1)
```

For a vacuum-normalized spectral value `lambda_a`, the corresponding
physical mass is exactly

```text
M_a=-(1/h_a)log(lambda_a),
E_a=-(1/s_a)log(lambda_a).
```

Thus finite positive `M_a->M` requires

```text
lambda_a=exp(-h_a M+o(h_a)),
E_a=a M/[c_H(a) g_H(a)^2]+o(a/g_H(a)^2).                 (2)
```

When `s_a` remains bounded away from zero and infinity along an
asymptotically free trajectory, `h_a->0`. The microscopic normalized
transfer eigenvalue must approach one, rather than stay a fixed amount
below it.

Substituting the matched two-loop scaling used in
`G19_CONTINUUM_BRIDGE_INSERT.tex` gives its necessary electric-unit law

```text
E(u) ~ [M/(c_H Lambda_H)] b0^(-p)
        u^((1+p)/2) exp(-sqrt(u)/(2b0)),  p=51/121.        (3)
```

Equation (3) is a reverse consistency condition under the stated
coupling/clock matching. It is not a derivation of `M`, a proof that
the coupling trajectory exists, or a continuation of a small-`u`
Taylor polynomial. The existing polynomial obstruction explains why
finite strong-coupling coefficients alone cannot meet it.

## 3. How a controlled infrared transfer can meet (2)

Choose a fixed physical blocking time `h_IR>0`. If microscopic physical
time is `h_a`, take integers `n_a` with `n_a h_a->h_IR`. Then the
required microscopic eigenvalue in (2) has

```text
lambda_a^(n_a) -> exp(-h_IR M).                          (4)
```

The right side is a fixed number strictly between zero and one. This
is the appropriate spectral scale for comparison with the controlled
strong-coupling Wilson block at a fixed physical infrared length/time.
There is no contradiction between a fixed infrared transfer gap and a
microscopic eigenvalue approaching one. A proved RG/time-block
intertwiner is what must connect them.

## 4. An exact OS isometry from an actual deterministic block

Let a fine Euclidean measure `mu_f` already have a positive transfer
`T_f` in its OS reconstruction. Let `P` be a deterministic map on its
full configurations and set `mu_c=P_# mu_f` exactly. Assume:

```text
P theta_f = theta_c P, possibly modulo a gauge transformation
                         on the tested invariant algebra;
P* A_c,+ subset A_f,+;
P sigma_f^b = sigma_c P,  b a positive integer.
```

The first two are the existing deterministic reflection-positivity
premises. The third is time-translation covariance of the actual block
map. All statements apply to the complete positive-time histories, not
to an independently chosen approximate slice marginal.

For a coarse history `F`, define

```text
J[F]_c=[F composed with P]_f.
```

The exact change of variables and reflection identity give

```text
<J[F],J[H]>_f
 = integral conjugate(F(theta_c P U)) H(P U) dmu_f(U)
 = <[F],[H]>_c.                                         (5)
```

Thus the null spaces descend correctly and `J` extends to an isometry
from the coarse OS Hilbert space onto a closed subspace of the fine one.
Time covariance gives on histories, and hence by continuity,

```text
T_f^b J = J T_c,  J Omega_c=Omega_f.                     (6)
```

The range of `J` is invariant under the self-adjoint `T_f^b`, so it is
reducing. If `T_f>=0`, it also reduces `T_f=(T_f^b)^(1/b)`, and

```text
T_f J = J T_c^(1/b).                                    (7)
```

This is a genuine operator intertwiner. The isometry follows from the
true pushforward history measure; it is not assumed from agreement of
time-zero distributions or a convenient conditional measure. The
reflection-adapted raw Balaban-type map is an available candidate for
the first premises, but its actual time covariance and complete
effective measure must be used when applying (5)-(7).

## 5. Exactly which coarse information transports backward

Suppose the coarse physical vacuum complement has

```text
||T_c|Omega_c^perp||<=exp(-h_c m_c),  m_c>0,
h_c=b h_f.
```

Equation (7) gives on `ran J` the same physical mass bound:

```text
||T_f|_(ran J minus vacuum)||<=exp(-h_f m_c).             (8)
```

It says nothing by itself about `(ran J)^perp`. A full fine-theory gap
follows if, in addition, the eliminated physical modes obey

```text
||T_f|_(ran J)^perp||<=exp(-h_f m_fast),  m_fast>0.        (9)
```

Then the entire fine physical vacuum complement has mass lower bound
`min(m_c,m_fast)`. To retain the coarse **complete isolated band** as
the complete fine band in a prescribed energy interval, require the
complement (9) to lie above that interval, not merely above zero.

For an exact coarse eigenprojection, (6) lifts it to the corresponding
fine spectral subspace. Source vectors from pullback histories retain
their norms and spectral weights by (5). Those fine sources are the
actual blocked/renormalized sources specified by `P`; they need not be
bare microscopic plaquette operators. Matching them to a desired local
continuum field is an additional source-renormalization statement.

This identifies where the conditional-form work meets the physical
problem: a bound on the eliminated modes must be a bound of the actual
OS transfer as in (9), or come with a proved comparison to it. The
configuration-space score estimate in `G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md`
does not silently supply (9).

## 6. A precise forward/backward meeting statement

A sufficient intermediate target is an actual reflection-positive RG
trajectory for fine Wilson measures, with physical scale calibration,
whose infrared effective measure has a normalized transfer `G_eff,a`
on a common infrared physical Hilbert space satisfying

```text
||G_eff,a-G_IR(u_IR)|| ->0,
u_IR inside the proved strong-coupling interval,
physical infrared time h_IR(a)->h_IR in (0,infinity).
```

Here `G_IR` is the actual controlled Wilson transfer or a proved
extension of its activity theorem to the generated effective
interactions. Replacing a general blocked action by a nearest-plaquette
Wilson action without an error theorem would not establish this target.

The norm error must be below the infrared spectral contour margin to
transport the complete band. Simultaneously, the renormalized source
synthesis must converge in its full operator norm, as in the literal
frame argument, or satisfy an equivalent cross-kernel estimate. This
preserves totality and nonzero normalized spectral weight. The actual
OS intertwiners (5)-(7), plus eliminated-mode bounds (9), then transmit
the infrared mass scale and the full gap backward to fine cutoffs.

If matching is approximate at successive scales, its errors must be
summable in the correctly normalized form or logarithmic-energy units.
A fixed error in a microscopic transfer norm is insufficient when the
physical time step tends to zero: equations (1)-(2) show that mass
differences then divide by that time step.

## 7. What atom passage still requires

For renormalized fixed-momentum or fixed-physical-volume source measures
`mu_a`, the existing G19 atom-passage proposition applies once

```text
M_a in [m_minus,m_plus] with m_minus>0,
mu_a({M_a})>=z_star>0,
mu_a converges vaguely to mu.
```

It then gives a nonzero limiting atom at every subsequential limiting
bottom mass. This is the exact reverse target for a glueball pole.
Its hypotheses must be verified after physical energy and source
normalization. The bare odd-plaquette absolute scaling
`a^9 |Z_6(a)|^2` is not a normalized residue statement and cannot
replace the lower bound above.

The existence, regularity, locality and spacetime covariance of the
continuum field theory require the corresponding continuum correlation
limits as well. A single channel's surviving atom does not prove those
axioms or the full physical mass gap. The meeting problem is therefore
specific: connect the actual ultraviolet measures to the proved infrared
operator, control eliminated modes, retain renormalized source weight,
and take the continuum reconstruction with the physical clock fixed.
