# Conditional Spectral Floor Monotonicity
*(and why it behaves like a “gap-preservation engine” under coarse observation)*

## 1. Setting

Let \((\Omega,\mathcal F,\mu)\) be a probability space and let \(\mathcal H\) be a (real or complex) separable Hilbert space.

We consider a measurable family \(\omega\mapsto H(\omega)\) of self-adjoint, lower-bounded operators on \(\mathcal H\), all represented by closed quadratic forms on a **common dense form domain** \(\mathcal D\subset\mathcal H\).  
Write the closed forms
\[
q_\omega(v):=\langle v,\,H(\omega)v\rangle,\qquad v\in\mathcal D,
\]
and assume a uniform lower bound:
\[
q_\omega(v)\ge -C\|v\|^2\qquad(\forall v\in\mathcal D,\ \forall \omega),
\]
for some finite \(C\).

Let \(\mathcal G\subset\mathcal F\) be a sub-\(\sigma\)-algebra. Define the **quadratic-form conditional expectation**
\[
\overline q_\omega(v):=\mathbb E\!\left[q_\cdot(v)\mid \mathcal G\right](\omega),
\qquad v\in\mathcal D.
\]
Then \(\overline q_\omega\) is again closed and lower-bounded on \(\mathcal D\), and thus determines a unique self-adjoint operator \(\overline H(\omega)\) (Kato’s representation theorem).

Define the spectral floor (bottom of spectrum) in quadratic-form language:
\[
\lambda_{\inf}(H(\omega)):=\inf\{q_\omega(v): v\in\mathcal D,\ \|v\|=1\},
\quad
\lambda_{\inf}(\overline H(\omega)):=\inf\{\overline q_\omega(v): v\in\mathcal D,\ \|v\|=1\}.
\]

---

## 2. Theorem: conditional spectral floor monotonicity

### Theorem 2.1 (Conditional spectral floor monotonicity)
Under the standing assumptions above, for \(\mu\)-almost every \(\omega\),
\[
\boxed{
\lambda_{\inf}\!\big(\overline H(\omega)\big)
\ \ge\
\mathbb E\!\left[\lambda_{\inf}(H)\mid \mathcal G\right](\omega).
}
\]

### Proof
Fix \(\omega\) and any \(v\in\mathcal D\) with \(\|v\|=1\). By definition of \(\overline q_\omega\),
\[
\overline q_\omega(v)=\mathbb E\!\left[q_\cdot(v)\mid\mathcal G\right](\omega).
\]
Pointwise in \(\omega'\) we have \(q_{\omega'}(v)\ge \lambda_{\inf}(H(\omega'))\) because the spectral floor is the infimum over all unit vectors. Hence,
\[
\overline q_\omega(v)
=\mathbb E\!\left[q_\cdot(v)\mid\mathcal G\right](\omega)
\ge
\mathbb E\!\left[\lambda_{\inf}(H)\mid\mathcal G\right](\omega).
\]
Taking the infimum over \(\|v\|=1\) gives the claim. \(\square\)

---

## 3. Corollaries that actually do work

### Corollary 3.1 (Defect monotonicity for convex decreasing penalties)
Let \(\phi:\mathbb R\to\mathbb R\) be convex and non-increasing. Define the **spectral defect**
\[
D_\phi(H(\omega)):=\phi\!\big(\lambda_{\inf}(H(\omega))\big).
\]
Then
\[
\boxed{
D_\phi(\overline H(\omega))
\ \le\
\mathbb E\!\left[D_\phi(H)\mid\mathcal G\right](\omega)
\qquad\text{a.s.}
}
\]

**Proof.** From Theorem 2.1 and monotonicity of \(\phi\),
\[
\phi(\lambda_{\inf}(\overline H))\le \phi\!\left(\mathbb E[\lambda_{\inf}(H)\mid\mathcal G]\right).
\]
By Jensen’s inequality for convex \(\phi\),
\[
\phi\!\left(\mathbb E[\lambda_{\inf}(H)\mid\mathcal G]\right)\le \mathbb E[\phi(\lambda_{\inf}(H))\mid\mathcal G].
\]
Combine. \(\square\)

A canonical choice is \(\phi(x)=(\kappa-x)_+\), yielding
\[
(\kappa-\lambda_{\inf}(\overline H))_+\ \le\ \mathbb E[(\kappa-\lambda_{\inf}(H))_+\mid\mathcal G].
\]

---

### Corollary 3.2 (Filtration irreversibility / coarse graining arrow)
Let \(\mathcal F\supset \mathcal G_1\supset \mathcal G_2\supset\cdots\) be a decreasing filtration (information is discarded as \(n\) increases), and define \(H_n:=\mathbb E[H\mid\mathcal G_n]\) in the quadratic-form sense.

Then the sequence of floors is **monotone non-decreasing**:
\[
\boxed{
\lambda_{\inf}(H_{n+1})
\ \ge\
\mathbb E[\lambda_{\inf}(H_n)\mid\mathcal G_{n+1}]
\ \ge\
\operatorname*{ess\,inf}\lambda_{\inf}(H_n).
}
\]
In particular, “coarsening cannot create new soft directions in the worst-case spectral floor.”

*(This is the structural content behind using the theorem as a one-line gap-preservation lemma in multiscale arguments.)*

---

## 4. Interpretation as a physics tool

If you read:

- \(H(\omega)\) as a physical Hessian / generator at microscopic resolution,
- \(\mathcal G\) as “what a coarse observer can see,”
- \(\overline H=\mathbb E[H\mid\mathcal G]\) as the effective operator after coarse observation,

then Theorem 2.1 says: the **effective** operator’s spectral floor is bounded below by the **coarse-conditioned** expectation of the microscopic floor. In plain language:

> the gap cannot be lost *because of averaging itself*; if the gap disappears, it must happen at a genuinely microscopic step (where the floor is already small), not in the act of forgetting information.

This is the exact mechanism exploited when one rewrites localization / decoupling / reconstruction steps as conditioning on \(\sigma\)-algebras.

---

## Appendix A. Minimal numerical sanity check (random-matrix model)

This is **not** evidence for any Yang–Mills claim. It is just a fast sanity check that the inequality is visible numerically in a non-commuting setting.

### Model
Let \(Z\in\{0,1,2\}\) be discrete and take
\[
H = H_0(Z) + \sigma\,\Xi,
\]
where \(\Xi\) is a zero-mean random symmetric matrix (non-commuting noise). Then
\[
\mathbb E[H\mid Z]=H_0(Z)
\quad\Rightarrow\quad
\lambda_{\min}(\mathbb E[H\mid Z])=\lambda_{\min}(H_0(Z)).
\]
The theorem predicts
\[
\lambda_{\min}(H_0(Z))\ \ge\ \mathbb E[\lambda_{\min}(H)\mid Z].
\]
We also test defect monotonicity with \(\delta_\kappa(H):=(\kappa-\lambda_{\min}(H))_+\).

### Code
```python
import numpy as np
import numpy.linalg as la

rng = np.random.default_rng(20251229)

def rand_sym(n, scale=1.0):
    A = rng.normal(size=(n,n))
    return scale*(A + A.T)/2

def make_H0(n, z):
    diag = np.linspace(1.0+0.5*z, 3.0+0.5*z, n)
    H = np.diag(diag)
    u = rng.normal(size=n)
    v = rng.normal(size=n)
    H += 0.15*np.outer(u,u) - 0.10*np.outer(v,v)
    return H

def run(n=12, samples_per_z=20000, noise_scale=0.2):
    out=[]
    for z in [0,1,2]:
        H0 = make_H0(n,z)
        lam0 = la.eigvalsh(H0).min()
        kappa = lam0 + 0.4

        lams=[]
        defs=[]
        for _ in range(samples_per_z):
            H = H0 + rand_sym(n, scale=noise_scale)
            lam = la.eigvalsh(H).min()
            lams.append(lam)
            defs.append(max(0.0, kappa-lam))

        out.append({
            "z": z,
            "lam_min_EH": lam0,
            "E_lam_min": float(np.mean(lams)),
            "Delta": lam0 - float(np.mean(lams)),
            "def_EH": max(0.0, kappa-lam0),
            "E_def": float(np.mean(defs)),
        })
    return out
```

### Results (one run)
| z | n | samples | noise | λ_min(E[H|z]) | E[λ_min(H)|z] | Δ | δ(E[H|z]) | E[δ(H)|z] |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 12 | 20000 | 0.20 | 0.109041 | -0.017874 | 0.126915 | 0.400 | 0.527019 |
| 1 | 12 | 20000 | 0.20 | 0.785482 | 0.651898 | 0.133584 | 0.400 | 0.533682 |
| 2 | 12 | 20000 | 0.20 | 1.242283 | 1.112244 | 0.130039 | 0.400 | 0.530186 |

In each case, \(\Delta=\lambda_{\min}(E[H|Z=z]) - E[\lambda_{\min}(H)\mid Z=z]\) is positive, and the defect inequality
\(\delta(E[H|Z])\le E[\delta(H)\mid Z]\) is also visible.

