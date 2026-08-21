# Concentration-of-measure suppression of the non-convex region (SU(2) one-link model)

This note quantifies a key intuition in the repo:

> Even if the action is not globally convex at large \(\beta\), the *non-convex region* sits at large group angles where the Gibbs weight is exponentially suppressed.

The original code attempt is in `analysis_concentration.py` (JAX + SciPy). fileciteturn2file3  
Here I reproduce the computation without JAX, using analytic Hessian formulas and SciPy’s quadrature.

---

## 1. The one-link radial density

For the SU(2) one-link model with Wilson factor \(e^{\beta\cos\theta}\), the induced radial density in \(\theta\in[0,\pi]\) is
\[
p_\beta(\theta)\,d\theta
\;\propto\;
\sin^2\theta\; e^{\beta\cos\theta}\,d\theta.
\]

Derivation sketch:
- Haar measure gives \(\sin^2\theta\,d\theta\,d\Omega\).
- The Wilson term contributes \(e^{\beta\cos\theta}\).
- Integrating over \(S^2\) direction \(\Omega\) leaves the 1D radial factor above.

---

## 2. Defining the “bad set”

From the convexity analysis (previous note), for \(\beta>\beta_c\approx 4.4139\) there are two radii
\[
\theta_-(\beta) < \theta_+(\beta)
\]
such that the radial Hessian eigenvalue is negative on \((\theta_-,\theta_+)\).

Two natural “bad” sets are:

1. **Strict non-convex set**
\[
B_{\rm nc}(\beta) := \{\theta\in[\theta_-(\beta),\theta_+(\beta)]\}.
\]

2. **Everything beyond the first breakdown radius**
\[
B_{\ge}(\beta) := \{\theta\in[\theta_-(\beta),\pi]\}.
\]
This is a conservative choice used in the repo’s defect heuristics.

---

## 3. The key observable: bad mass ratios

Define
\[
\mathsf{Bad}_{\rm nc}(\beta)=\mathbb P_\beta(\theta\in B_{\rm nc}(\beta)),
\qquad
\mathsf{Bad}_{\ge}(\beta)=\mathbb P_\beta(\theta\in B_{\ge}(\beta)).
\]

Numerically (SciPy `quad`) we get:

| beta | r_start | r_end | nonconv_ratio | bad_ratio |
|---|---|---|---|---|
| 4.500000e+00 | 2.038649e+00 | 2.201505e+00 | 1.081864e-03 | 1.880604e-03 |
| 5.000000e+00 | 1.924823e+00 | 2.332324e+00 | 1.659518e-03 | 1.844956e-03 |
| 6.000000e+00 | 1.831386e+00 | 2.454436e+00 | 9.566965e-04 | 9.748608e-04 |
| 8.000000e+00 | 1.747900e+00 | 2.581050e+00 | 1.830831e-04 | 1.833402e-04 |
| 1.000000e+01 | 1.706223e+00 | 2.654222e+00 | 2.983515e-05 | 2.983933e-05 |
| 2.000000e+01 | 1.633771e+00 | 2.812795e+00 | 2.113171e-09 | 2.113171e-09 |
| 5.000000e+01 | 1.595101e+00 | 2.938592e+00 | 3.249038e-22 | 3.249038e-22 |

Interpretation:

- At \(\beta=5\), the strictly non-convex region already carries only \(\sim 1.7\times 10^{-3}\) of the one-link probability mass.
- By \(\beta=10\), it is \(\sim 3\times 10^{-5}\).
- By \(\beta=20\), it is \(\sim 2\times 10^{-9}\) (already “defect-gas” levels).
- By \(\beta=50\), it is essentially zero at double precision.

---

## 4. Asymptotic intuition (why the decay is basically \(e^{-\beta}\))

For large \(\beta\), the density is dominated near \(\theta=0\) because
\[
\cos\theta = 1-\frac{\theta^2}{2}+O(\theta^4)
\quad\Rightarrow\quad
e^{\beta\cos\theta}\approx e^\beta e^{-\beta\theta^2/2}.
\]

Meanwhile \(\theta_-(\beta)\to\pi/2\) as \(\beta\to\infty\).  
So on the bad set, \(\cos\theta\lesssim 0\), giving roughly
\[
\mathsf{Bad}_{\ge}(\beta)
\approx \frac{\int_{\theta_-(\beta)}^\pi \sin^2\theta\,e^{\beta\cos\theta}\,d\theta}{\int_0^\pi \sin^2\theta\,e^{\beta\cos\theta}\,d\theta}
\sim \frac{e^{0\cdot\beta}}{e^{1\cdot\beta}}
\sim e^{-\beta}.
\]

The \(\beta=20\) row is a dead giveaway: \(e^{-20}\approx 2.06\times 10^{-9}\), matching the computed ratio at the 1–2% level.

---

## 5. What this suggests for the full lattice problem

This is the seed of a plausible “defect gas” story:

- Define defects as links/plaquettes leaving the convex chart.
- Show their density is exponentially small at the relevant scale.
- Prove the system is “almost” uniformly convex away from rare defects.
- Use a multi-scale functional inequality / cluster expansion to control rare regions.

### Caveat (important)
Classical Holley–Stroock perturbation uses a **supremum** bound on potential differences, not a **probability** bound. So concentration alone is not enough; you need either:
- a *localized* perturbation lemma,
- a two-scale log-Sobolev inequality,
- or a decomposition that prevents the “bad” sup bound from scaling with volume.

That gap is visible in the repo’s proof synthesis plan, which treats this step as speculative. (See `proof_synthesis_plan.tex` in the project tree.)

---

## 6. Reproducible code snippet

```python
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def lam_rad_scaled(theta, beta):
    # Same sign as the full Hessian radial eigenvalue.
    return 0.5*(1/math.sin(theta)**2 - 1/theta**2) + (beta/4)*math.cos(theta)

def find_theta_roots(beta, nscan=200000):
    thetas = np.linspace(1e-6, math.pi-1e-6, nscan)
    vals = 0.5*(1/np.sin(thetas)**2 - 1/thetas**2) + (beta/4)*np.cos(thetas)
    s = np.sign(vals)
    idx = np.where(s[:-1]*s[1:] < 0)[0]
    roots=[]
    for j in idx:
        a,b = thetas[j], thetas[j+1]
        roots.append(brentq(lambda x: lam_rad_scaled(x, beta), a, b))
    return roots  # [theta_minus, theta_plus]

def dens(theta, beta):
    return (math.sin(theta)**2)*math.exp(beta*math.cos(theta))

def mass(beta, a, b):
    val,_ = quad(lambda t: dens(t,beta), a,b, limit=200)
    return val

def bad_ratios(beta):
    tminus, tplus = find_theta_roots(beta)
    Z = mass(beta, 0, math.pi)
    return (mass(beta, tminus, tplus)/Z, mass(beta, tminus, math.pi)/Z)

```

