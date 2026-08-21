import numpy as np
import matplotlib.pyplot as plt

beta = np.array([5.7, 5.8, 5.9, 6.0, 6.1])
mu   = np.array([0.92, 0.81, 0.74, 0.68, 0.63])
mlat = np.array([0.88, 0.78, 0.71, 0.66, 0.61])

# No-intercept least squares: minimize ||mlat - k*mu||_2
k = float(np.dot(mu, mlat) / np.dot(mu, mu))
pred = k * mu
resid = mlat - pred

# R^2 against mean model
ss_res = float(np.dot(resid, resid))
ss_tot = float(np.dot(mlat - np.mean(mlat), mlat - np.mean(mlat)))
R2 = 1.0 - ss_res/ss_tot
rms = float(np.sqrt(np.mean(resid**2)))

print(f"k (no-intercept) = {k:.6f}")
print(f"R^2             = {R2:.6f}")
print(f"RMS residual    = {rms:.6f}  (lattice units)")

# Plot
plt.figure()
plt.plot(mu, mlat, "o", label="data")
x = np.linspace(mu.min()*0.98, mu.max()*1.02, 200)
plt.plot(x, k*x, "-", label=f"fit: m = {k:.4f} μ")
plt.xlabel("μ(β)  (curvature-derived scale)")
plt.ylabel("m_lat(β)  (lattice mass gap)")
plt.legend()
out = "SELECTED_E04_fit.png"
plt.savefig(out, dpi=200, bbox_inches="tight")
print(f"Saved plot      = {out}")
