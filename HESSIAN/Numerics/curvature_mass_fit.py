import numpy as np

# Data copied from the project note EVIDENCE_01_Curvature_Mass_Fit.md
beta = np.array([5.7, 5.8, 5.9, 6.0, 6.1])
mu_eff = np.array([0.92, 0.81, 0.74, 0.68, 0.63])
m_lat  = np.array([0.88, 0.78, 0.71, 0.66, 0.61])

# Constrained least squares fit: m_lat ≈ k * mu_eff (no intercept)
k = float(np.dot(mu_eff, m_lat) / np.dot(mu_eff, mu_eff))
pred = k * mu_eff
res = m_lat - pred

R2 = 1.0 - np.dot(res, res) / np.dot(m_lat - np.mean(m_lat), m_lat - np.mean(m_lat))
rms = float(np.sqrt(np.mean(res**2)))

print("k =", k)
print("R^2 =", R2)
print("RMS residual =", rms)
print("residuals =", res)
