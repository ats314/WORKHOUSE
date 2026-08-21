# Corollary 9.X′′ (Davies decay with C_\partial)

Corollary 9.X′′ (Davies decay with C_\partial)

With the same hypotheses,
\eta_{\mathrm{DG}}^{(\partial)}
\;:=\;
\operatorname{arcosh}\!\Bigl(1+\frac{m^2}{2\,\alpha\,C_\partial(\Delta_1)}\Bigr)
=
2\,\operatorname{arsinh}\!\Bigl(\frac{m}{2\sqrt{\alpha\,C_\partial(\Delta_1)}}\Bigr)
\tag{9.DG″.1}
is admissible in (9.DG′.1).

Proof change: in the estimate for \|Q_{\Lambda,\lambda}\|, restrict the row‑sum to neighbors with |\phi(b)-\phi(\tilde b)|=1, since all terms with \phi(b)=\phi(\tilde b) vanish identically.

⸻

What to do next in your repo (one practical suggestion)

Add a one‑liner to NOTATION_AND_CONSTANTS.md like:
	•	C_0(\Delta_1)=\max_b\sum_{\tilde b\neq b}|(\Delta_1)_{b\tilde b}|_{\mathrm{op}}
	•	C_\partial(\Delta_1) as in (9.DG.boundary)

and record the values your diagnostic script reports for the lattice/geometry you’re using (e.g. cubic torus: C_0=6). Then Proposition 9.X can cite either the crude universal D_E or the precomputed C_0 constant, depending on how “referee‑safe” you want to be.

If you paste your computed C_\partial for L=24 as well, I can tell you immediately how much the exponent improves numerically under the same lemma.
