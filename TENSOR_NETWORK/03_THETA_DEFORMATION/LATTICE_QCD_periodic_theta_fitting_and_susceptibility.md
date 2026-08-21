# Periodic θ-Dependence: Fourier Fitting and Correct Extraction of Topological Susceptibility
*(A practical method note distilled from the project’s Fourier-fit experiments and θ-scan discussions.)*

## 0. What’s the point?

When \(Z(\theta)\) is well-defined, the free energy (or free energy density) is **\(2\pi\)-periodic** in \(\theta\).
Fitting periodic data with a low-degree polynomial is almost guaranteed to do something cursed near the endpoints.

The project’s Fourier-fit experiment showed dramatically better goodness-of-fit (R²) when using a Fourier series rather than a quadratic polynomial.

The exciting part is not “Fourier series exist”—it’s the discipline of enforcing periodicity and symmetry in the pipeline, and extracting susceptibilities correctly from Fourier coefficients.

---

## 1. Setup and conventions

Define the (intensive) free energy density
\[
f(\theta) := -\frac{1}{V}\ln Z(\theta).
\]

For CP-invariant theories (common in θ-term contexts), \(f(\theta)\) is even:
\[
f(\theta)=f(-\theta),
\]
so the Fourier series contains only cosines:

\[
f(\theta) = a_0 + \sum_{n\ge 1} a_n \cos(n\theta).
\]

(If the data show a sine component, it may reflect numerical noise, broken symmetry in the approximation, or a different observable/definition.)

---

## 2. Topological susceptibility from Fourier coefficients

By definition,
\[
\chi_{\text{top}} := \left.\frac{\partial^2 f}{\partial\theta^2}\right|_{\theta=0}.
\]

Different communities sometimes include a minus sign depending on whether they define \(f\) or \(-\ln Z\); the Taylor form is the safest anchor:

\[
f(\theta)=f(0) + \frac{1}{2}\chi_{\text{top}}\theta^2 + O(\theta^4).
\]

Now expand the Fourier series near \(\theta=0\):

\[
\cos(n\theta)=1-\frac{n^2\theta^2}{2}+O(\theta^4).
\]

Therefore,
\[
f(\theta)=\left(a_0+\sum_{n\ge 1}a_n\right)
-\frac{\theta^2}{2}\sum_{n\ge 1} n^2 a_n + O(\theta^4).
\]

Matching coefficients yields the clean formula:

\[
\boxed{\chi_{\text{top}} = -\sum_{n\ge 1} n^2 a_n.}
\]

So, if you keep only the first cosine mode \(a_1\cos(\theta)\), then \(\chi_{\text{top}}\approx -1^2 a_1\).  
If your Fourier basis is \(\cos(2\theta)\), then \(n=2\) and \(\chi_{\text{top}}\approx -4a_1\), etc.

### Important warning (the project’s example)

The project’s Fourier-fit output used
\[
F(\theta)=a_0 + a_1\cos(2\theta)+b_1\sin(2\theta)+a_2\cos(4\theta)+\cdots
\]
and then reported \(\chi_{\text{top}}=4a_1\).

That is only consistent if:
1. you define \(\chi_{\text{top}}=-F''(0)\) (sign convention), **and**
2. you truncate to the first harmonic (ignore \(a_2\), etc.).

With a non-negligible \(a_2\), the correct second derivative includes additional terms:
\[
F''(0)= -4a_1 -16a_2 -\cdots.
\]

So the extraction should either:
- include enough modes and compute \(-\sum n^2 a_n\), or
- justify why higher modes are negligible.

---

## 3. Why Fourier beats polynomial (in one sentence)

A polynomial fit does not know it must satisfy
\[
f(0)=f(2\pi),\quad f'(0)=f'(2\pi),\quad \ldots,
\]
so it invents non-periodic curvature to accommodate periodic data.

A Fourier series bakes in periodicity and (if enforced) evenness.

---

## 4. Practical fitting recipe

1. Sample \(\theta\) uniformly on \([0,2\pi)\) at \(N_\theta\) points (16–32 is usually a decent start).
2. Enforce symmetry if expected:
   - average data at \(\pm\theta\) to kill sine noise,
   - or fit only cosine modes.
3. Fit
   \[
   f(\theta)\approx a_0 + \sum_{n=1}^{n_{\max}} a_n\cos(n\theta)
   \]
   by least squares (or compute coefficients by discrete Fourier transform if sampling is uniform).
4. Compute
   \[
   \chi_{\text{top}} = -\sum_{n=1}^{n_{\max}} n^2 a_n.
   \]
5. Increase \(n_{\max}\) until \(\chi_{\text{top}}\) stabilizes within error bars.

---

## 5. Evidence inside the project

The “FOURIER WHHHHHH” analysis shows much higher R² for a Fourier fit than a quadratic polynomial fit on the same θ-scan dataset.
That’s exactly the kind of sanity check that prevents extracting nonsense from periodic observables.

---

## Source in the project

This note is based on the Fourier-fit experiment output in `FOURIER WHHHHHH.pdf`, plus the θ-scan observations in `TN_2D_U1_Detail_v2.md`.

