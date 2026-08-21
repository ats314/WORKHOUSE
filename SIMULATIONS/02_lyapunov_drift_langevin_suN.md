# Lyapunov Drift Diagnostic for SU(N) Gauge Langevin (Plaquette-Defect Lyapunov)

## Goal

A common route to *quantitative ergodicity* for Langevin dynamics on a compact manifold is to exhibit a Lyapunov function \(V\) such that the generator \(L\) satisfies a drift inequality
\[
L V \le -\lambda V + b.
\]
This note records a concrete **stochastic-generator check** of such an inequality for a natural gauge observable.

---

## 1. Setting

- Lattice: periodic \(L^4\).
- Gauge group: \(SU(N)\).
- Link variables \(U_{x,\mu}\in SU(N)\).

### Wilson plaquette defect

For a plaquette \(p\) with holonomy \(U_p\),
\[
z_p(U) \;=\; 1 - \frac{1}{N}\Re \operatorname{Tr}(U_p).
\]

Define the mean plaquette defect and Lyapunov candidate:
\[
B(U) := \frac{1}{|\mathcal P|}\sum_{p\in\mathcal P} z_p(U),
\qquad
\overline V(U) := 1 + B(U).
\]

This choice has nice properties:

- \(\overline V \ge 1\).
- \(\overline V\) is gauge-invariant.
- \(\overline V\) is “small” near the trivial field.

---

## 2. Langevin generator and the target inequality

Write the Langevin generator in the informal schematic form
\[
L f \;=\; \Delta f \;-\;\langle \nabla S,\nabla f\rangle,
\]
where:

- \(S(U)\) is the Wilson action
  \[
  S(U)=\beta \sum_p z_p(U),
  \]
- \(\nabla\), \(\Delta\) are the Riemannian gradient and Laplacian on \((SU(N))^{E}\).

The diagnostic checks whether a choice like
\[
\lambda = 4 C_F,
\qquad
b = 8 C_F,
\qquad
C_F = \frac{N^2-1}{2N}
\]
satisfies
\[
L\overline V(U)\;\le\; -\lambda \overline V(U)+b
\]
for a random test configuration \(U\).

(These constants are motivated by a “Casimir-normalized Laplacian” heuristic; the file explicitly frames this as a quick sanity check, not a theorem.)

---

## 3. Stochastic estimator for \(L\overline V\)

The generator is estimated by sampling random tangent directions \(\Xi\in\mathfrak{su}(N)\) on each link and using symmetric finite differences.

Let \(U_\pm = U\exp(\pm \varepsilon \Xi)\). Then:

- Laplacian estimator:
  \[
  \Delta f(U)\;\approx\;\mathbb E_\Xi \frac{f(U_+)+f(U_-)-2f(U)}{\varepsilon^2}.
  \]

- Drift inner-product estimator:
  \[
  \langle \nabla S,\nabla f\rangle
  \;\approx\;
  \mathbb E_\Xi \left(\frac{S(U_+)-S(U_-)}{2\varepsilon}\right)\left(\frac{f(U_+)-f(U_-)}{2\varepsilon}\right).
  \]

So:
\[
Lf(U)\approx \mathbb E_\Xi\left[\frac{f(U_+)+f(U_-)-2f(U)}{\varepsilon^2}
-\left(\frac{S(U_+)-S(U_-)}{2\varepsilon}\right)\left(\frac{f(U_+)-f(U_-)}{2\varepsilon}\right)\right].
\]

---

## 4. Reference implementation (JAX)

This is a lightly trimmed excerpt of the implementation.

```python
# lyapunov_drift_check.py (excerpt)

def haar_suN(key, shape, N):
    # Approx Haar via QR of complex Gaussian; adjust det to 1
    z = (normal + 1j*normal)/sqrt(2)
    q, r = jnp.linalg.qr(z)
    phase = exp(-1j*angle(diag(r)))
    q = q * phase[..., None, :]
    detq = jnp.linalg.det(q)
    q = q / detq[..., None, None] ** (1.0/N)
    return q

def suN_tangent_gaussian(key, shape, N):
    # Gaussian in su(N): anti-Hermitian traceless
    a = (normal + 1j*normal)/sqrt(2)
    x = a - conj(a.T)
    x = x - (trace(x)/N) * I
    return x

def plaquette(U, mu, nu):
    # periodic rolls; returns U_mu(x) U_nu(x+mu) U_mu(x+nu)^\dagger U_nu(x)^\dagger
    ...

def Vbar(U):
    z_list = []
    for mu<nu:
        Up = plaquette(U, mu, nu)
        z = 1 - (1/N) * ReTr(Up)
        z_list.append(z)
    return 1 + mean(stack(z_list))

def estimate_LV(U, beta, eps, mc_samples, key):
    def S(U):
        return beta * sum_{plaquettes} z_p(U)

    def one_sample(k):
        Xi = suN_tangent_gaussian(k, (L,L,L,L,4), N)
        U_p = U @ expm(eps*Xi)
        U_m = U @ expm(-eps*Xi)
        lap = (Vbar(U_p)+Vbar(U_m)-2*Vbar(U))/eps**2
        dS  = (S(U_p)-S(U_m))/(2*eps)
        dV  = (Vbar(U_p)-Vbar(U_m))/(2*eps)
        return lap - dS*dV

    vals = vmap(one_sample)(split(key, mc_samples))
    return mean(vals), std(vals)/sqrt(mc_samples)
```

---

## 5. Numerical result (one representative run)

Parameters used in the example call:

- \(N=3\)
- \(L=2\) (small sanity lattice)
- \(\beta=6.0\)
- \(\varepsilon=5\times 10^{-3}\)
- MC directions: 128

Output:

- \(\overline V(U)=2.00385046\)
- Estimated \(L\overline V(U) \approx -8.8193 \pm 1.0231\)
- RHS \(= -\lambda\overline V + b \approx -0.0205\)
- Check \(L\overline V \le \text{RHS}\): **True**

So the drift is *strongly negative* in this random test, far below the bound.

---

## 6. Why this matters and what to do next

If one can establish a genuine drift inequality plus a minorization condition, **Harris’ theorem** gives geometric ergodicity and quantitative mixing bounds.

The test here is only a sanity check — but it suggests a real path:

1. Replace heuristic constants \((\lambda,b)\) with data-driven fits across \(\beta,L,N\).
2. Replace “one Haar sample” with ensembles drawn from approximate equilibrium (or from realistic gauge configurations).
3. Add a carré-du-champ computation (or a controllable bound on \(\Gamma(f)=\|\nabla f\|^2\)) to connect drift + curvature to LSI/Poincaré constants.

---

## Sources used

- `RUN 110.pdf` (full JAX code + printed output).
- `Simulations_and_Results_Summary.txt` (program framing: curvature → inequalities → gap).
