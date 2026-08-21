# Extracting \(\chi_{\text{top}}\) from periodic \(F(\theta)\): Fourier curvature beats polynomials

## 1. Definition: susceptibility is curvature of the free energy

Given a θ-dependent partition function

\[
Z(\theta) = \sum_{Q\in\mathbb{Z}} e^{i\theta Q}\, Z_Q,
\]

define free energy density

\[
f(\theta) = -\frac{1}{V}\log Z(\theta).
\]

Then

\[
\chi_{\text{top}} = \left.\frac{\partial^2 f(\theta)}{\partial\theta^2}\right|_{\theta=0}.
\]

If \(Z_Q\ge 0\) and CP symmetry holds at \(\theta=0\), then \(\chi_{\text{top}} = \frac{1}{V}\langle Q^2\rangle_{\theta=0}\ge 0\).

## 2. Why a Fourier model is the mathematically “right” prior

Because \(Z(\theta)\) is a Fourier series in \(Q\), it is \(2\pi\)-periodic in \(\theta\), hence so is \(f(\theta)\) (up to branch choices).

A generic periodic fit is

\[
f(\theta) = a_0 + \sum_{n=1}^N \left(a_n\cos(n\theta) + b_n\sin(n\theta)\right).
\]

Then the curvature is

\[
f''(0) = -\sum_{n=1}^N n^2 a_n.
\]

So:
- the **cosine coefficients** directly determine \(\chi_{\text{top}}\),
- the sine coefficients should vanish in an exactly CP-even situation (numerically they measure asymmetry / noise / branch issues).

### Special case used in the project: even harmonics

Some project fits use only \(n=2,4\) terms:

\[
f(\theta)\approx a_0 + a_1\cos(2\theta)+b_1\sin(2\theta)+a_2\cos(4\theta)+b_2\sin(4\theta).
\]

Then
\[
\chi_{\text{top}} = f''(0) = -4a_1 -16 a_2.
\]

If you *truncate further* to only the leading harmonic,
\[
f(\theta)\approx a_0 + a_1\cos(2\theta),
\quad\Rightarrow\quad
\chi_{\text{top}}\approx -4a_1.
\]

(So the sign matters: if \(\chi_{\text{top}}>0\), then you expect \(a_1<0\) in that convention.)

## 3. Why quadratic polynomials are a trap

A local Taylor fit near \(\theta=0\),
\[
f(\theta)\approx c_0 + c_1\theta + \tfrac{1}{2}\chi_{\text{top}}\theta^2,
\]
is valid only for sufficiently small \(|\theta|\) **and** ignores periodicity.

If you feed it data across \([0,2\pi]\), it will generally:
- bias curvature,
- invent a linear term \(c_1\neq 0\) (unphysical if symmetry is present),
- fit badly overall.

## 4. What the project evidence shows

The project explicitly compares polynomial vs Fourier fits and reports that the Fourier model fits dramatically better (example: \(R^2\) near 0.95 for Fourier vs ~0.07 for a polynomial), i.e. periodic structure dominates.

This is exactly what you expect if:
- the computed \(F(\theta)\) truly has a periodic dependence,
- the dataset spans a wide θ range.

## 5. Recommended extraction pipeline (rigorous and repeatable)

1. Compute \(f(\theta_i)\) at \(N_\theta\) points across \([0,2\pi]\).
2. Fit a Fourier model with controlled harmonics \(n\le n_{\max}\).
   - Start with \(n_{\max}=2\) or \(4\).
   - Increase until residuals stop improving (or use regularization).
3. Compute curvature analytically from coefficients:
   \[
   \chi_{\text{top}} = -\sum_{n=1}^{n_{\max}} n^2 a_n.
   \]
4. Estimate uncertainty:
   - bootstrap resampling in θ,
   - or propagate least-squares covariance to \(\chi_{\text{top}}\).

## 6. Extension: \(\chi_{\text{top}}(\beta)\) as a phase-diagram observable

Once you can do θ scans fast, you can produce \(\chi_{\text{top}}\) vs coupling \(\beta\) curves:
- scan a grid \((\beta_i,\theta_j)\),
- fit Fourier in θ for each β,
- then analyze trends and scaling with β.

This naturally links tensor-network numerics to physical phases (strong vs weak coupling).
It’s not a mass-gap proof by itself—but it creates *measurable structure* you can try to control analytically.

## 7. The big theoretical bridge (speculative, but testable)

If the project’s θ↔q hypothesis is even approximately right, then:
- the Fourier coefficients \(a_n(\beta)\) might correspond to controlled features of a q-deformed recoupling theory,
- and \(\chi_{\text{top}}(\beta)\) becomes a renormalization-group observable you can track through coarse-graining.

That’s where “numerics → conjecture → proof attempt” can start.
