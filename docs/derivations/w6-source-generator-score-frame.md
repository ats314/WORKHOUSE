# W6: the complete source generator in the ground-state frame and the score Poisson equation

10 September 2026. Analytic continuation of the
[fixed-square derivative reduction](w6-ground-jets-and-transport-budget.md)
(R1-R12) toward its open model input R10. Everything below is for the actual
fixed twelve-edge compact square at positive coupling, in the conventions of
that note and of
[compact_residual.md](../../runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md)
C1-C2.

This note retains the reviewed part of a derivation attempt that claimed to
close R10. The closure claim was rejected; section 6 records the exact failed
steps so they are not repeated. What survives is exact: a unitary
representation of the complete R9 generator in the ground-state frame, the
identification of the R9 vacuum-cross vector with the conditional mean of the
ground score, a Poisson equation for the ground score whose forcing is purely
magnetic, an exact fiber identity for the conditional score energy, and a
reduction of the order-zero bound in R10 to five conditional-energy estimates
whose averaged forms are already established. **R10 remains open.** M10 is a
different fiberwise statement about a different (dilated) score and is not
implied by, and does not imply, anything here.

## 1. Conventions

```
M = SU(2)^4 (twelve edges),  H_g = (g^2/2)T + g^-2 V,  0 <= V <= 32,
T[u,v] = sum_(e,c) <E_(e,c) u, E_(e,c) v>,   L_g = H_g - e_g,
Omega_g > 0 the normalized ground,  chi_g = Omega'_g,  <Omega_g,chi_g> = 0,
h_g = 1 + e_g/gamma,   q_g[u] = H_g[u] + gamma||u||^2 = L_g[u] + (e_g+gamma)||u||^2.
```

`E_(e,c)` are the anti-self-adjoint Haar-invariant edge fields, so on smooth
functions `T u = -Delta u` with `Delta = sum_(e,c) E_(e,c)^2`. Write the
carre du champ

```
Gamma(u,v) = sum_(e,c) conj(E_(e,c) u) (E_(e,c) v),     T[u,v] = integral Gamma(u,v) dU.
```

Source variable and literal source projection (C1):

```
w = Tr(U2 U3)/2,   E_w = Haar conditional expectation given w,
h_g(w) = E_w[Omega_g^2],   P_g f = Omega_g h_g^-1 E_w[Omega_g f].
```

Ground measure and its marginal:

```
dmu_g = Omega_g^2 dU,   dnu_g = rho_g(w) dw,   rho_g = h_g rho_0,
rho_0(w) = (2/pi) sqrt(1-w^2)  (Haar marginal of the SU(2) trace).
```

Source energy, as in the conditional-score note (M6):

```
b_g[f] = g^2 integral (1-w^2) |f'(w)|^2 dnu_g,
H_g[Omega_g f(w)] = e_g ||f||^2_(L2(nu_g)) + b_g[f].                      (SF0)
```

SF0 is equivalent to `Gamma(w,w) = 2(1-w^2)`. Since `w` is a spin-1/2 matrix
coefficient on each of the two edges it involves, `Delta w = -c_w w` is also
a function of `w` (`c_w = 6` in this normalization; only the functional
dependence is used below).

Regularity: at each fixed `g > 0`, `Omega_g`, `chi_g` and `h_g` are smooth,
`h_g` has a positive minimum, and `P_g` is norm smooth in `g` on L2 and on
the form domain (C1). All identities below are at fixed positive `g`; no
uniformity in `g` is claimed except where a constant is displayed.

## 2. The ground-state frame (SF1-SF2)

Let `U_g : L2(dU) -> L2(mu_g)`, `U_g psi = psi/Omega_g`. It is unitary. On
smooth `Phi` put

```
Delta_mu Phi = Delta Phi + 2 Gamma(log Omega_g, Phi).
```

**SF1 (kinetic form in the ground frame).** For `Phi_1, Phi_2` in the
transformed form domain,

```
L_g[U_g^* Phi_1, U_g^* Phi_2] = (g^2/2) integral Gamma(Phi_1,Phi_2) dmu_g,
q_g[U_g^* Phi] = (g^2/2) integral Gamma(Phi,Phi) dmu_g + (e_g+gamma) integral |Phi|^2 dmu_g,
U_g L_g U_g^* = -(g^2/2) Delta_mu  on the smooth core.                      (SF1)
```

Proof. For smooth `Phi`,
`-Delta(Omega Phi) = -(Delta Omega)Phi - 2Gamma(Omega,Phi) - Omega Delta Phi`.
The ground equation `(g^2/2)(-Delta Omega) + g^-2 V Omega = e_g Omega`
removes the potential and the eigenvalue:

```
L_g(Omega Phi) = (g^2/2) Omega [ -Delta Phi - 2 Gamma(log Omega, Phi) ] = -(g^2/2) Omega Delta_mu Phi.
```

Integrating by parts once on the closed manifold, with the Haar-invariant
fields,

```
integral conj(Phi_1) (Delta Phi_2) Omega^2 dU
  = - integral Omega^2 Gamma(Phi_1,Phi_2) dU - integral conj(Phi_1) Gamma(Omega^2,Phi_2) dU,
```

and `Gamma(Omega^2,Phi_2) = 2 Omega^2 Gamma(log Omega, Phi_2)`, so
`integral conj(Phi_1)(-Delta_mu Phi_2) dmu = integral Gamma(Phi_1,Phi_2) dmu`.
Form closure from the smooth core is the C1 statement that the direct-product
holonomy change of variables preserves the form domain. The `q_g` identity
adds `(e_g+gamma)||.||^2` and uses unitarity.

**SF2 (the source projection is the conditional expectation).**

```
U_g P_g U_g^* = Pi_w := E_(mu_g)[ . | w ],                                   (SF2)
```

the orthogonal projection of `L2(mu_g)` onto functions of `w`. Indeed
`U P U^* Phi = U[Omega h^-1 E_w[Omega^2 Phi]] = E_w[Omega^2 Phi]/E_w[Omega^2]`.
Its defining property, for every bounded `eta(w)`, is

```
integral (Pi_w Phi) eta dmu_g = integral Phi eta dmu_g.                     (SF2a)
```

## 3. The complete R9 generator in the ground-state frame (SF3-SF5)

Define the ground score, its conditional mean and its centered part:

```
sigma_g = chi_g/Omega_g = partial_g log Omega_g = U_g chi_g,   ||sigma_g||_(mu_g) = ||chi_g||,
integral sigma_g dmu_g = <Omega_g,chi_g> = 0,
m_g(w) = E_(mu_g)[sigma_g | w] = h_g^-1 E_w[Omega_g chi_g] = (1/2) partial_g log h_g(w) = (1/2) partial_g log rho_g(w),
tilde sigma_g = sigma_g - m_g(w),   E_(mu_g)[tilde sigma_g | w] = 0,
K^0_g(w) = E_(mu_g)[tilde sigma_g^2 | w] = Var_(mu_g)(sigma_g | w).
```

The superscript `0` marks the undilated score `partial_g log Omega_g`. The
`K_g` of the [conditional-score note](w6-conditional-score-tail-control.md)
uses the Q8-dilated score `(partial_g Psi_g + D Psi_g/g)/Psi_g`; it is a
different function of `w`, and no statement here transfers to it.

**SF3 (derivative of the projection).** `P_g = U_g^* Pi_w U_g` with
`partial_g U_g = -sigma_g U_g` and `partial_g U_g^* = U_g^* sigma_g` as
multiplication operators, so

```
P'_g = U_g^* ( sigma_g Pi_w + partial_g Pi_w - Pi_w sigma_g ) U_g.
```

Here `partial_g Pi_w` is the derivative of the conditional expectation with
respect to the moving measure. Differentiate SF2a for fixed `Phi` and
`g`-independent `eta(w)`, using `partial_g dmu_g = 2 sigma_g dmu_g` and the
fact that `partial_g (Pi_w Phi)` is again a function of `w`:

```
integral (partial_g Pi_w Phi) eta dmu = 2 integral (Phi - Pi_w Phi) sigma eta dmu
  = 2 integral Pi_w[ sigma (I-Pi_w) Phi ] eta dmu,
hence   partial_g Pi_w = 2 Pi_w sigma_g (I - Pi_w).                         (SF3)
```

**SF4 (the Kato generator).** Multiply the bracket in `P'_g` by `Pi_w` on
either side, using `(partial_g Pi_w) Pi_w = 0` and `Pi_w (partial_g Pi_w) = partial_g Pi_w`:

```
( sigma Pi + partial Pi - Pi sigma ) Pi = (I-Pi) sigma Pi,
Pi ( sigma Pi + partial Pi - Pi sigma ) = Pi sigma (I-Pi).
```

Subtracting,

```
U_g [P'_g,P_g] U_g^* = (I-Pi_w) sigma_g Pi_w - Pi_w sigma_g (I-Pi_w)
                     = (I-Pi_w) tilde sigma_g Pi_w - Pi_w tilde sigma_g (I-Pi_w),   (SF4)
```

the second form because multiplication by `m_g(w)` commutes with `Pi_w`.
Back in `L2(dU)`, for a source vector `u_P = Omega_g f(w)` and a fast vector
`u_Q = Omega_g Phi` with `Pi_w Phi = 0`:

```
[P'_g,P_g] u_P = f(w) tilde sigma_g Omega_g = f(w) ( chi_g - m_g(w) Omega_g ) = f(w) (I-P_g) chi_g,   (SF4a)
[P'_g,P_g] u_Q = - Omega_g E_(mu_g)[ tilde sigma_g Phi | w ] = - Omega_g h_g^-1 E_w[ chi_g u_Q ].      (SF4b)
```

For SF4b the `m_g` term drops because `E_w[Omega_g u_Q] = h_g Pi_w Phi = 0`.

**SF5 (the vacuum-cross vector).** R9 defines
`nu_g = chi_g - [P'_g,P_g] Omega_g`. SF4a with `f = 1` gives
`[P'_g,P_g] Omega_g = (I-P_g) chi_g`, hence

```
nu_g = P_g chi_g = m_g(w) Omega_g,     ||nu_g||^2 = integral m_g^2 dnu_g <= ||chi_g||^2.   (SF5)
```

The complete R9 generator in the ground-state frame is therefore

```
U_g A(g) U_g^* Phi = (I-Pi_w)( tilde sigma_g Pi_w Phi ) - Pi_w( tilde sigma_g (I-Pi_w) Phi )
                     + m_g(w) integral Phi dmu_g - integral m_g Phi dmu_g.              (SF5a)
```

Every term of the complete generator is expressed through the ground score,
its conditional mean and its conditional fluctuation on the level sets of `w`.
The draft that prompted this note wrote `nu_g = (I-P_g) Omega'_g`; that is not
the R9 vector. SF5 is the correct identification.

## 4. The score Poisson equation (SF6-SF7)

**SF6 (first-order forcing is purely magnetic).** In the sense of forms on the
common domain,

```
L_g[chi_g, u] = 4 g^-3 < (V - <V>_(mu_g)) Omega_g , u >     for all u in the form domain,
e'_g = 2 e_g/g - 4 g^-3 <V>_(mu_g),                                                   (SF6)
```

equivalently, by SF1 with `u = Omega_g Phi`,

```
(g^2/2) integral Gamma(sigma_g, Phi) dmu_g = 4 g^-3 integral (V - <V>_(mu_g)) Phi dmu_g,
i.e.  -(g^2/2) Delta_mu sigma_g = 4 g^-3 ( V - <V>_(mu_g) )   in L2(mu_g).
```

Proof. R3 states `L_g[chi_g,u] = -(H'_g - e'_g)[Omega_g,u]` with
`H'_g = g T - 2 g^-3 V`. The ground equation in form sense,
`(g^2/2) T[Omega,u] = e_g <Omega,u> - g^-2 <V Omega,u>`, gives
`g T[Omega,u] = (2 e_g/g) <Omega,u> - 2 g^-3 <V Omega,u>`. Therefore

```
(H'_g - e'_g)[Omega,u] = (2 e_g/g - e'_g) <Omega,u> - 4 g^-3 <V Omega,u>.
```

Taking `u = Omega` and `e'_g = H'_g[Omega]` gives the displayed `e'_g`;
substituting back gives `(H'_g - e'_g)[Omega,u] = -4 g^-3 <(V-<V>)Omega,u>`.
Since `V` is bounded, the right side is an honest L2 pairing, so the identity
holds on the whole form domain. The electric form `T` is absent from the
forcing: the first ground jet is driven by the magnetic fluctuation alone.
This is special to first order; see section 6.

**SF7 (exact consequences).**

```
L_g[chi_g] = (g^2/2) integral Gamma(sigma_g,sigma_g) dmu_g = 4 g^-3 Cov_(mu_g)(sigma_g, V),   (SF7a)
integral K^0_g dnu_g = ||chi_g||^2 - integral m_g^2 dnu_g <= 4 e_g h_g /(gamma g^2),          (SF7b)
Cov_(mu_g)(sigma_g, V) <= e_g h_g g.                                                          (SF7c)
```

SF7a is SF6 with `u = chi_g`; SF7b is the law of total variance with R4;
SF7c is SF7a with R4. So the averaged conditional score variance carries the
`g^-2` scaling that R10 requires; what R10 needs is fiberwise control.

Conditional divergence identity. For a smooth vector field `X` on `M` with
`mu_g`-divergence `div_mu X` (so `integral (div_mu X) phi dmu = -integral X(phi) dmu`),
testing against `phi(w)` and using `X(phi(w)) = phi'(w) X(w)` gives, as
distributions on `(-1,1)`,

```
E_(mu_g)[ div_mu X | w ] = rho_g(w)^-1 d/dw ( rho_g(w) E_(mu_g)[ X(w) | w ] ).            (SF7d)
```

Fiber identity for the conditional score energy. Put

```
J_g(w) = (g^2/2) E_(mu_g)[ Gamma(tilde sigma_g, tilde sigma_g) | w ],
D_g(w) = E_(mu_g)[ tilde sigma_g Gamma(log Omega_g, w) | w ],
S_g(w) = E_(mu_g)[ tilde sigma_g^2 Gamma(log Omega_g, w) | w ].
```

Apply SF7d to `X = tilde sigma grad tilde sigma` and to `Y = tilde sigma^2 grad w`,
use `-Delta_mu tilde sigma = -Delta_mu sigma + m'' Gamma(w,w) + m' Delta_mu w`,
`Delta_mu w = -c_w w + 2 Gamma(log Omega, w)`, SF6, and `E[tilde sigma | w] = 0`.
The result is, as distributions on `(-1,1)` at fixed positive `g`,

```
J_g = 4 g^-3 Cov_(mu_g)(sigma_g, V | w) + g^2 m'_g D_g
      + (g^2/(4 rho_g)) d/dw [ (2(1-w^2) rho_g K^0_g)' + c_w w rho_g K^0_g - 2 rho_g S_g ].   (SF7e)
```

The drift term `g^2 m'_g D_g` and the flux `S_g` are absent from the rejected
draft (section 6). Integrating SF7e against `dnu_g` the flux vanishes and one
recovers `integral J_g dnu_g = 4 g^-3 integral Cov(sigma,V|w) dnu_g + g^2 integral m'_g D_g dnu_g`,
consistent with pairing SF6 against `tilde sigma_g` directly.

## 5. Exact reduction of the order-zero R10 bound (SF8-SF9)

**SF8 (exact energy expressions).** For `u_P = Omega_g f(w)`, by SF4a and SF1,

```
||[P'_g,P_g] u_P||^2 = integral |f|^2 K^0_g dnu_g,
L_g[[P'_g,P_g] u_P] = (g^2/2) integral Gamma(f tilde sigma, f tilde sigma) dmu_g
   <= 2 integral K^0_g g^2 (1-w^2) |f'|^2 dnu_g + 2 integral |f|^2 J_g dnu_g,          (SF8a)
```

using `Gamma(f tilde sigma, f tilde sigma) <= 2 tilde sigma^2 |f'|^2 Gamma(w,w) + 2 |f|^2 Gamma(tilde sigma,tilde sigma)`
and `Gamma(w,w) = 2(1-w^2)`. For `u_Q = Omega_g Phi` with `Pi_w Phi = 0`, by
SF4b with `eta(w) = E_(mu_g)[tilde sigma Phi | w]`,

```
[P'_g,P_g] u_Q = - Omega_g eta,   integral |eta|^2 dnu_g <= integral K^0_g E_(mu_g)[|Phi|^2 | w] dnu_g,
q_g[[P'_g,P_g] u_Q] = (e_g+gamma) integral |eta|^2 dnu_g + b_g[eta].                    (SF8b)
```

For the vacuum-cross term, by SF5 and the rank-one bound
`|| |u><v| ||_(q_g -> q_g) <= ||u||_q ||v||_q / gamma` (transport note, after R8b),
with `||Omega_g||_q = sqrt(e_g+gamma)`,

```
q_g[nu_g] = (e_g+gamma) integral m_g^2 dnu_g + b_g[m_g],
|| |nu_g><Omega_g| - |Omega_g><nu_g| ||_(q_g -> q_g) <= 2 sqrt(e_g+gamma) ||nu_g||_q / gamma.   (SF8c)
```

**Conditional-energy hypotheses.** With constants independent of `g` on
`0 < g < g_*`:

```
(H0)  b_g[ E_(mu_g)(Phi | w) ]              <= kappa_P q_g[Omega_g Phi]        for all Phi in the form domain;
(H1)  sup_w K^0_g(w)                         <= kappa_0 g^-2;
(H2)  J_g(w)                                 <= kappa_1 g^-2 ( 1 + g^-2 E_(mu_g)[V | w] )   nu_g-a.e.;
(H3)  b_g[ E_(mu_g)(tilde sigma_g Phi | w) ] <= kappa_2 g^-2 q_g[Omega_g Phi]   for all Phi with Pi_w Phi = 0;
(H4)  b_g[m_g] = L_g[P_g chi_g]              <= kappa_3 g^-2.
```

H0 is the uniform `q_g`-boundedness of the source projection (its L2 part is
trivial; the energy part is the content). H1, H2 and H3 are fiberwise
strengthenings of established averaged statements: `integral K^0_g dnu_g` is
SF7b; `integral J_g dnu_g <= 8 e_g h_g g^-2 + 2 b_g[m_g]` by
`Gamma(tilde sigma,tilde sigma) <= 2Gamma(sigma,sigma) + 2Gamma(m,m)` and SF7a, so the
averaged H2 follows from H4; the L2 part of H3 is SF8b with H1. H4 is a single
number, the source energy of the conditional mean of the score; no bound on it
is established, and it is exactly the `q_g`-size of the R9 vacuum-cross vector.

**SF9 (conditional theorem: order zero of R10).** Assume H0-H4. Then for all
`u` in the form domain

```
||A(g) u||_(q_g) <= d_0 g^-1 ||u||_(q_g),
d_0 = sqrt(c_P (1+kappa_P)) + sqrt(2 c_Q (2+kappa_P)) + c_X,
c_P = 2 kappa_0 + 2 kappa_1 (1 + 1/gamma) + (E+gamma) kappa_0/gamma,
c_Q = (E+gamma) kappa_0/gamma + kappa_2,
c_X = (2 sqrt(E+gamma)/gamma) sqrt( 4 E (E+gamma)(1+E/gamma)/gamma + kappa_3 ).
```

Proof. Write `u = u_P + u_Q`, `u_P = P_g u = Omega_g f(w)`, `u_Q = Omega_g Phi`.
By H0, `q_g[u_P] <= (e_g+gamma)||u||^2 + kappa_P q_g[u] <= (1+kappa_P) q_g[u]`,
and `q_g[u_Q] <= 2 q_g[u] + 2 q_g[u_P] <= 2(2+kappa_P) q_g[u]`.
Source part: in SF8a, `b_g[f] <= q_g[u_P]`, `integral |f|^2 dnu_g = ||u_P||^2 <= q_g[u_P]/gamma`,
and `integral |f|^2 g^-2 E[V|w] dnu_g = g^-2 <u_P, V u_P> <= H_g[u_P] <= q_g[u_P]`;
with H1, H2 this gives `q_g[[P',P]u_P] <= c_P g^-2 q_g[u_P]`.
Fast part: SF8b with H1 and H3 gives `q_g[[P',P]u_Q] <= c_Q g^-2 q_g[u_Q]`.
Vacuum-cross part: SF8c, SF5, R4 (`||chi_g||^2 <= 4 e_g h_g/(gamma g^2)`) and H4
give `q_g[nu_g] <= g^-2 [ 4E(E+gamma)(1+E/gamma)/gamma + kappa_3 ]`, hence the
operator bound `c_X g^-1`. Add the three `q_g` norms.

SF9 is the `r = 0` case of R10 and nothing more. For `r = 1,2` the second
ground jet obeys `L_g chi''_g = -2(H'_g - e'_g) chi_g - (H''_g - e''_g) Omega_g`;
the first term contains `g T chi_g`, so the forcing is no longer purely
magnetic and no analogue of SF6 is available. `P''_g` additionally involves
`sigma_g^2` and `partial_g sigma_g`. Those orders are not reduced here.

## 6. Reviewed and rejected steps of the closure attempt

The submitted argument asserted R10 in full. Each of the following steps was
checked and fails; they are recorded so the next attempt does not repeat them.

1. **The pointwise score bound was assumed.** The bound `sup_w K^0_g <= C g^-2`
   (H1) was invoked as "the score bound / tail control". Only the averaged
   SF7b is established. H1 is a stronger fiberwise statement than M10 and is
   itself the open content.
2. **A second-derivative term was dropped.** Integrating the flux term of
   SF7e twice by parts against `|f|^2` produces `Re(conj(f) f'')`, which the
   energy form does not control; integrating once instead places a derivative
   on `rho_g K^0_g`, whose regularity is unknown.
3. **The fiber identity omitted two terms.** Replacing `Delta_mu tilde sigma`
   by `Delta_mu sigma` discards `m'_g D_g`; the flux `S_g` was also dropped.
   SF7e is the exact identity.
4. **Energy-norm adjointness was misused.** `[P'_g,P_g]` is skew in L2, not in
   the `q_g` inner product, and `P_g` is not `q_g`-orthogonal. The fast-to-source
   bound SF8b needs H3 and does not follow from the source-to-fast bound.
5. **The projection was assumed to contract the energy norm.** Conditional
   expectation does not contract a Dirichlet form in general; H0 and H4 are
   the required statements. The draft also misidentified `nu_g` (see SF5).
6. **Orders one and two were asserted by analogy.** The second-order forcing
   contains the electric term; see the end of section 5.

Minor slips, harmless in direction: a factor 4 in place of 2 in front of the
score-energy term, a missing square root in the conditional covariance bound,
and `||Omega_g||_q = e_g+gamma` in place of its square root.

## 7. Consequence and verification boundary

- Established here, analytic at fixed positive `g` on the actual fixed square:
  SF1-SF5 (ground-frame representation of the complete R9 generator, including
  `nu_g = m_g(w) Omega_g`), SF6-SF7 (score Poisson equation, its averaged
  consequences and the exact fiber identity SF7e).
- Conditional: SF9, the `r = 0` case of R10 under H0-H4 with the displayed
  `d_0`.
- Open: H0-H4 individually; the `r = 1,2` cases of R10; R10 itself. Nothing
  here changes the status of M10 or of the interacting-grid comparison.
- The natural next target is a fiberwise version of SF7a: a Poincare-type
  inequality for the diffusion `-Delta_mu` restricted to the level sets of `w`,
  uniform in `g`, which would give H1 and H2 from SF6.
- No Lean coverage. No numerical replay of the actual four-face model is
  attached; a one-dimensional rotor check of SF6 was reported externally and
  is not repository evidence.
