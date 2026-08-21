# Vacuum Stiffness Gravity in Spherical Symmetry
## Exact force law, asymptotic expansions, screening radius, BTFR, and the external field effect

### What this document is
This is a **stand-alone derivation module** for the phenomenology that falls out of the
vacuum-stiffness modified Poisson equation
\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=4\pi G\rho,
\qquad \mu(x)=1-e^{-x}.
\]
We derive the exact spherical reduction, obtain the implicit force law,
compute both strong- and weak-field asymptotics, identify the **screening radius**
\[
r_s(M):=\sqrt{\frac{GM}{a_0}},
\]
and derive the **baryonic Tully–Fisher relation** (BTFR)
\[
V_\infty^4 = G\,M_b\,a_0.
\]
We also show how the **external field effect** (EFE) emerges from linearization around a background acceleration.

---

## 1. Spherical reduction of the field equation

Assume a static, spherically symmetric source:
\[
\rho(x)=\rho(r),\qquad r=|x|.
\]
Then the potential is radial: \(\Phi=\Phi(r)\), and
\[
\nabla\Phi = \Phi'(r)\,\hat r,\qquad g(r):=|\nabla\Phi|=|\Phi'(r)|.
\]

In spherical coordinates,
\[
\nabla\cdot(A(r)\hat r)=\frac{1}{r^2}\frac{d}{dr}\bigl(r^2A(r)\bigr).
\]
Apply this with
\[
A(r)=\mu\!\left(\frac{g(r)}{a_0}\right)\Phi'(r),
\]
to get
\[
\frac{1}{r^2}\frac{d}{dr}\left(r^2 \mu\!\left(\frac{g(r)}{a_0}\right)\Phi'(r)\right)
=4\pi G\rho(r).
\]

Integrate from \(0\) to \(r\):
\[
r^2 \mu\!\left(\frac{g(r)}{a_0}\right)\Phi'(r)
=G\,M(r),
\]
where
\[
M(r):=4\pi \int_0^r \rho(\tilde r)\,\tilde r^2\,d\tilde r
\]
is the enclosed mass.

Since \(\Phi'(r)\) is negative for an attractive potential, it is convenient to write the **magnitude** form:
\[
\boxed{
\mu\!\left(\frac{g(r)}{a_0}\right)\,g(r)=\frac{G\,M(r)}{r^2}=:g_N(r),
}
\]
where \(g_N(r)\) is the Newtonian acceleration that the same baryonic mass would produce.

This relation is exact in spherical symmetry.  No approximation has been used.

---

## 2. The implicit force law for \(\mu(x)=1-e^{-x}\)

Insert \(\mu(x)=1-e^{-x}\):
\[
\bigl(1-e^{-g/a_0}\bigr)g=g_N.
\]

Equivalently,
\[
g-g\,e^{-g/a_0}=g_N
\quad\Longleftrightarrow\quad
g=\frac{g_N}{1-e^{-g/a_0}}.
\]
This is an implicit equation for \(g\) given \(g_N\).  It has:
- a unique solution \(g(g_N)\ge 0\) for each \(g_N\ge 0\),
- smooth dependence on \(g_N\),
because the left side is strictly increasing in \(g\).

---

## 3. Strong-field regime: Newtonian recovery with nonperturbative corrections

Assume \(g_N\gg a_0\).  Then the solution satisfies \(g\gg a_0\), hence \(e^{-g/a_0}\) is exponentially small.

Write \(g=g_N+\varepsilon\) with \(|\varepsilon|\ll g_N\).  Plug into
\[
g_N+\varepsilon-(g_N+\varepsilon)e^{-(g_N+\varepsilon)/a_0}=g_N
\]
to get
\[
\varepsilon=(g_N+\varepsilon)\,e^{-g_N/a_0}\,e^{-\varepsilon/a_0}.
\]
Since \(\varepsilon/a_0\) is small compared to \(g_N/a_0\), the leading behavior is
\[
\boxed{
g(r)=g_N(r)\left[1+e^{-g_N(r)/a_0}+O\!\left(e^{-2g_N(r)/a_0}\right)\right].
}
\]
So the approach to Newtonian gravity is **nonperturbatively fast**: the correction is \(\sim e^{-g_N/a_0}\).

This is a very strong form of screening.

---

## 4. Weak-field regime: deep law and systematic expansion

Assume \(g_N\ll a_0\).  Then \(g\ll a_0\) and we can expand
\[
1-e^{-g/a_0}=\frac{g}{a_0}-\frac{g^2}{2a_0^2}+\frac{g^3}{6a_0^3}+O\!\left(\frac{g^4}{a_0^4}\right).
\]
Then the force law becomes
\[
\left(\frac{g}{a_0}-\frac{g^2}{2a_0^2}+O\!\left(\frac{g^3}{a_0^3}\right)\right)g=g_N,
\]
i.e.
\[
\frac{g^2}{a_0}-\frac{g^3}{2a_0^2}+O\!\left(\frac{g^4}{a_0^3}\right)=g_N.
\]

Let \(g=\sqrt{a_0 g_N}\,u\), where \(u\) is dimensionless and \(u\to 1\) as \(g_N/a_0\to 0\).
Then
\[
\frac{a_0 g_N u^2}{a_0}-\frac{(a_0 g_N)^{3/2}u^3}{2a_0^2}+ \cdots = g_N
\]
simplifies to
\[
u^2-\frac12\sqrt{\frac{g_N}{a_0}}\,u^3+O\!\left(\frac{g_N}{a_0}\right)=1.
\]
Solve perturbatively: \(u=1+\alpha \sqrt{g_N/a_0}+O(g_N/a_0)\).
Then
\[
(1+2\alpha\sqrt{\epsilon})-\frac12\sqrt{\epsilon}(1+3\alpha\sqrt{\epsilon})+O(\epsilon)=1
\]
with \(\epsilon=g_N/a_0\).  Matching \(O(\sqrt{\epsilon})\) gives \(2\alpha-\tfrac12=0\), so \(\alpha=\tfrac14\).

Therefore
\[
\boxed{
g(r)=\sqrt{a_0 g_N(r)}\left[1+\frac14\sqrt{\frac{g_N(r)}{a_0}}+O\!\left(\frac{g_N(r)}{a_0}\right)\right].
}
\]
The leading term is the deep-field law \(g\sim \sqrt{a_0 g_N}\).

---

## 5. Screening radius and regime matching

Define the screening radius for a point mass \(M\) (or total enclosed mass) by the radius where the Newtonian acceleration equals \(a_0\):
\[
g_N(r_s)=a_0.
\]
For \(g_N(r)=GM/r^2\), this gives
\[
\boxed{
r_s(M)=\sqrt{\frac{GM}{a_0}}.
}
\]

- For \(r\ll r_s\): \(g_N\gg a_0\), the field is Newtonian up to exponentially small corrections.
- For \(r\gg r_s\): \(g_N\ll a_0\), the deep-field law \(g\sim \sqrt{GM a_0}/r\) holds.

The transition is smooth because \(\mu\) is smooth.

---

## 6. Flat rotation curves and BTFR

Consider a test particle moving on a circular orbit of radius \(r\) around a spherically symmetric mass.
Centripetal balance gives
\[
\frac{V^2(r)}{r}=g(r).
\]

In the far field \(r\gg r_s\), we have \(g_N(r)=GM_b/r^2\ll a_0\), hence
\[
g(r)\sim \sqrt{a_0 g_N(r)}
=\sqrt{a_0\,\frac{GM_b}{r^2}}
=\frac{\sqrt{GM_b a_0}}{r}.
\]
Then
\[
\frac{V^2(r)}{r}\sim \frac{\sqrt{GM_b a_0}}{r}
\quad\Longrightarrow\quad
V^2(r)\to \sqrt{GM_b a_0}
\quad(r\to\infty).
\]
So the rotation curve asymptotes to a constant \(V_\infty\), and
\[
\boxed{
V_\infty^4 = G\,M_b\,a_0.
}
\]
This is the baryonic Tully–Fisher relation, derived directly from the field equation.

---

## 7. External Field Effect (EFE) from linearization

The EFE is the statement that a system’s internal dynamics can depend on an approximately uniform external gravitational field.

In this framework, the EFE is not optional: it is a generic consequence of **nonlinearity in \(\nabla\Phi\)**.

### 7.1 Decompose background + internal field

Write
\[
\Phi(x)=\Phi_{\mathrm{ext}}(x)+\phi(x),
\]
where
- \(\Phi_{\mathrm{ext}}\) is a slowly varying background with nearly constant gradient in the region of interest,
- \(\phi\) is the internal potential sourced by \(\rho_{\mathrm{int}}\).

Assume
\[
\nabla\Phi_{\mathrm{ext}}\approx p_{\mathrm{ext}}\ \text{constant},\qquad
|\nabla\phi|\ll |p_{\mathrm{ext}}|.
\]

### 7.2 Linearized equation for \(\phi\)

Define the flux map
\[
A(p):=\mu\!\left(\frac{|p|}{a_0}\right)p.
\]
Then the field equation is \(\nabla\cdot A(\nabla\Phi)=4\pi G\rho\).

Linearize:
\[
A(p_{\mathrm{ext}}+\nabla\phi)=A(p_{\mathrm{ext}})+DA(p_{\mathrm{ext}})\nabla\phi+O(|\nabla\phi|^2).
\]
Taking divergence and using that the background solves the sourceless equation locally, we obtain
\[
\nabla\cdot\!\bigl(DA(p_{\mathrm{ext}})\nabla\phi\bigr)=4\pi G\,\rho_{\mathrm{int}}.
\]

But
\[
DA(p)=\mu(x)I+\frac{\mu'(x)}{a_0|p|}\,p\otimes p,\qquad x=\frac{|p|}{a_0}.
\]
So the internal potential obeys a **linear, anisotropic Poisson equation**.

### 7.3 Effective Newton constant in the isotropized approximation

If we ignore anisotropy (or average over directions), we can replace \(DA(p_{\mathrm{ext}})\) by \(\mu(x_{\mathrm{ext}})I\), yielding
\[
\mu\!\left(\frac{g_{\mathrm{ext}}}{a_0}\right)\Delta\phi \approx 4\pi G\,\rho_{\mathrm{int}}.
\]
Equivalently,
\[
\Delta\phi \approx 4\pi G_{\mathrm{eff}}\,\rho_{\mathrm{int}},
\qquad
G_{\mathrm{eff}}:=\frac{G}{\mu(g_{\mathrm{ext}}/a_0)}.
\]

This immediately gives two limits:

- **Strong external field** \(g_{\mathrm{ext}}\gg a_0\): \(\mu\to 1\), so \(G_{\mathrm{eff}}\to G\) and internal dynamics are Newtonian.
- **Weak external field** \(g_{\mathrm{ext}}\ll a_0\): \(\mu(g_{\mathrm{ext}}/a_0)\sim g_{\mathrm{ext}}/a_0\), so \(G_{\mathrm{eff}}\sim G\,a_0/g_{\mathrm{ext}}\), i.e. a large effective coupling (the classic MOND-like EFE scaling).

This dependence on the environment is the external field effect.

---

## 8. What is genuinely novel / worth pushing further?

1. The **screening is exponentially sharp** in the strong-field regime because the constitutive choice produces \(e^{-g/a_0}\) corrections.
2. The EFE is derived as a clean **linearization-of-a-convex-Hamiltonian** statement.  It is literally Hessian physics.
3. The BTFR is not an axiom; it is a corollary of \(\mu(x)\sim x\) as \(x\to 0\).

---

## 9. Immediate “next calculations” that would be decisive

1. Keep the anisotropy term in \(DA(p_{\mathrm{ext}})\) and derive observable EFE anisotropy signatures.
2. Solve the full 3D equation numerically for a realistic galaxy+environment density map and compare with:
   - rotation curves,
   - satellite galaxy dynamics (EFE-sensitive),
   - strong-field Solar System bounds (should be automatically safe due to exponential screening).

