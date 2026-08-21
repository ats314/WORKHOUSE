# Proposition 9.X′ (Davies decay with C_0 in place of D_E)

Proposition 9.X′ (Davies decay with C_0 in place of D_E)

In Proposition 9.X, replace every occurrence of \alpha D_E by B_0(L_\Lambda)=\alpha C_0(\Delta_1). Then the same proof yields
\big|\big(M_\Lambda^{-1}\big)_{bb'}\big|_{\mathrm{op}}
\ \le\
\frac{2}{m^2}\,
\exp\!\Big(-\eta_{\mathrm{DG}}^{(0)}\,\mathrm{dist}_E(b,b')\Big),
\tag{9.DG′.1}
with
\eta_{\mathrm{DG}}^{(0)}
\;:=\;
\operatorname{arcosh}\!\Bigl(1+\frac{m^2}{2\,\alpha\,C_0(\Delta_1)}\Bigr)
\;=\;
2\,\operatorname{arsinh}\!\Bigl(\frac{m}{2\sqrt{\alpha\,C_0(\Delta_1)}}\Bigr).
\tag{9.DG′.2}
In particular, for m^2\ll \alpha,
\eta_{\mathrm{DG}}^{(0)}\sim \frac{m}{\sqrt{\alpha\,C_0(\Delta_1)}},
\qquad
\eta_{\mathrm{CT}}\sim \frac{m^2}{\alpha\,C_0(\Delta_1)}.
\tag{9.DG′.3}

Proof change (one line): in the Davies estimate for the symmetric perturbation Q_{\Lambda,\lambda}, instead of using the crude bound
\sum_{\tilde b\neq b}|(L_\Lambda)_{b\tilde b}|\le \alpha D_E,
use the definition \sum_{\tilde b\neq b}|(L_\Lambda)_{b\tilde b}|\le B_0(L_\Lambda)=\alpha C_0(\Delta_1). Everything else is unchanged.

Sanity check with your numbers (just so you can see the scale)

From your diagnostic:
	•	\alpha=1, m^2=0.3, m\approx0.5477
	•	C_0(\Delta_1)=6

So this gives
\eta_{\mathrm{DG}}^{(0)}=\operatorname{arcosh}\!\Big(1+\frac{0.3}{12}\Big)\approx 0.2236,
whereas CT gives
\eta_{\mathrm{CT}}=\log\!\Big(1+\frac{0.3}{12}\Big)\approx 0.0247.
That’s exactly the “m vs m^2” scaling improvement — and it explains why \eta_{\mathrm{DG}}^{(0)} is still below your observed slope \approx0.54: you’re still paying a worst‑case coupling constant in a bound that does not use translation invariance/Fourier symbol information.

⸻

Optional sharpening: count only couplings that actually cross a distance level set

The Davies proof has a built‑in refinement you didn’t cash in: in
Q_{\Lambda,\lambda}\;=\;\frac{L_{\Lambda,\lambda}+L_{\Lambda,-\lambda}}{2}-L_\Lambda,
the factor is \cosh(\lambda(\phi(b)-\phi(\tilde b)))-1, which is zero when \phi(b)=\phi(\tilde b). So you can replace C_0 by a smaller constant that ignores “tangential” neighbors.
