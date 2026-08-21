# Scalar-Lattice Coherence Sweeps and Hypercubic Artifact Tuning (4D)

This note collects two related threads from the project files:

1. A “coherence sweep” computing geometric constants and mass-gap proxies for a free massive scalar on a 4D torus.
2. A scan that tunes a hypercubic correction coefficient \(c\) to reduce lattice anisotropy in the propagator.

These are standard-ish ingredients, but the project organizes them into a practical pipeline with useful diagnostics.

---

## 1. Free massive scalar on a periodic \(L^4\) lattice

Consider a lattice operator
\[
(-\Delta_1 + m^2)\phi = \eta,
\]
where \(\Delta_1\) is the nearest-neighbor Laplacian and \(m^2>0\).
The propagator \(G(x)\) is the inverse kernel.

A key asymptotic in \(d\) dimensions is
\[
G(r) \sim \frac{e^{-\kappa r}}{r^{(d-1)/2}},
\]
so in \(d=4\), a naive log-slope estimator of \(\kappa\) is biased unless one corrects for the \(r^{-3/2}\) prefactor.

---

## 2. Coherence sweep outputs

The project reports a sweep over \(L\in\{64,96,128\}\) and \(m^2\in\{0.1,0.2,0.3\}\), including:

- \(C_0(\Delta_1)\) (a geometric constant),
- \(\eta_{\rm DG}(C_0)\) (a derived “DG” parameter),
- `max_ratio_dist0`,
- \(\kappa_{\rm expected}=\mathrm{arcosh}(1+m^2/(2\alpha))\) for the chosen \(\alpha\).

Example rows (from the printed table):

| \(L\) | backend | \(m^2\) | \(C_0(\Delta_1)\) | \(\eta_{\rm DG}(C_0)\) | max\_ratio\_dist0 | \(\kappa_{\rm expected}\) |
|---:|:--:|---:|---:|---:|---:|---:|
| 64 | cuda | 0.1 | 87.298902 | 0.130643 | 0.318929 | 0.314925 |
| 64 | cuda | 0.2 | 87.298902 | 0.047860 | 0.447025 | 0.443568 |

(Additional rows appear in the project output for \(m^2=0.3\) and larger \(L\).)

---

## 3. Corrected point-to-point fit (remove the 4D prefactor)

The project runs an explicit test comparing:

- \(\eta_{\rm th}\) (the theoretical mass-gap proxy),
- `eta_proj_fit`,
- `eta_pt_raw` (naive point-to-point),
- `eta_pt_corrected` (prefactor-corrected).

Reported table:

| \(m^2\) | \(\eta_{\rm th}\) | \(\eta_{\rm proj\_fit}\) | \(\eta_{\rm pt\_raw}\) | \(\eta_{\rm pt\_corrected}\) |
|---:|---:|---:|---:|---:|
| 0.01 | 0.099958 | 0.088814 | 0.104029 | 0.090171 |
| 0.02 | 0.141362 | 0.136842 | 0.145005 | 0.138179 |
| 0.05 | 0.223144 | 0.217031 | 0.227625 | 0.219144 |
| 0.10 | 0.312346 | 0.307312 | 0.317777 | 0.308893 |
| 0.30 | 0.541097 | 0.539652 | 0.547480 | 0.540783 |
| 0.50 | 0.711990 | 0.707109 | 0.736854 | 0.714361 |

The corrected estimator noticeably reduces bias at larger \(m^2\).

---

## 4. Hypercubic anisotropy healing: scan over a correction coefficient \(c\)

The project also scans an anisotropy correction parameter \(c\) to reduce rotational/hypercubic artifacts.

A sample output table (extract):

| \(L\) | \(m^2\) | \(c_{\rm opt}\) | rel\_err |
|---:|---:|---:|---:|
| 128 | 0.01 | 0.1500 | 0.1112 |
| 128 | 0.02 | 0.1500 | 0.1169 |
| 128 | 0.05 | 0.1500 | 0.1440 |
| 128 | 0.10 | 0.1500 | 0.1866 |
| 128 | 0.20 | 0.1500 | 0.2570 |
| 128 | 0.50 | 0.1500 | 0.3697 |

Interpretation: the “best” \(c\) appears pinned near \(0.15\) in this scan range, at least for these parameters.

---

## 5. Why this matters for the broader project

The SU(2) drift/Lyapunov work depends on quantitative estimates of:

- correlation lengths,
- geometric constants,
- distance metrics on the lattice.

The scalar-lattice pipeline provides:

1. An explicit **sanity check** that mass-gap extraction is not being biased by known prefactors.
2. A method for **reducing anisotropy artifacts**, which can matter if one uses propagator-based distance measures or compares decay rates along different lattice directions.

---

## 6. Suggested extensions

1. Replace \(\Delta_1\) with improved Laplacians (Symanzik-like) and repeat the scans.
2. For the coherence sweep, increase \(L\) and compare finite-size scaling of the “floor” term \(\sim 1/(m^2 L^4)\).
3. Apply the corrected mass-extraction method to interacting scalar fields (weak \(\lambda\)) as a bridge to the \(\phi^4\) quench study.
