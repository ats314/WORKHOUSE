"""Numerical check (scratchpad only) of the exact identity
   W_B'' = -2 eps J_xb J_xb^T + K_b J_xx,   K_b = -eps(Delta_b + 2 grad_b u . grad_b),
for a 2-coordinate Schrodinger operator H = -eps Delta + V on R^2 (x = block, b = outside),
with V = eps z^T Om0^2 z + lam (x^4 + x^2 b^2 + b^4), Om0 = [[A,B],[B,C]].
Also checks  V_B'' + W_B'' = 2 eps J_xx^2 - K_x J_xx  (conditional eigenfunction identity)
and the Gaussian case lam = 0: W_B'' = -2 eps B^2, V_B''+W_B'' = 2 eps A^2  (SC17 R12a)."""
import numpy as np, sys
try:
    import scipy.sparse as sp, scipy.sparse.linalg as spl
except Exception as e:
    print("scipy unavailable:", e); sys.exit(2)

def run(eps, A, B, C, lam, N=241, L=4.0):
    xs = np.linspace(-L, L, N); h = xs[1]-xs[0]
    X, Bc = np.meshgrid(xs, xs, indexing='ij')          # X: block coord, Bc: outside coord
    Om2 = np.array([[A,B],[B,C]]) @ np.array([[A,B],[B,C]])
    V_B  = eps*(Om2[0,0]*X**2 + 2*Om2[0,1]*X*Bc) + lam*(X**4 + X**2*Bc**2)   # every term depending on x
    V_out= eps*(Om2[1,1]*Bc**2) + lam*Bc**4                                # b-only terms
    V = V_B + V_out
    # 1D Dirichlet Laplacian
    e = np.ones(N); D2 = sp.diags([e, -2*e, e], [-1,0,1], shape=(N,N))/h**2
    I = sp.identity(N)
    Lap = sp.kron(D2, I) + sp.kron(I, D2)
    H = (-eps*Lap + sp.diags(V.ravel())).tocsc()
    E, psi = spl.eigsh(H, k=1, sigma=0.0, which='LM', tol=1e-12)
    Om = np.abs(psi[:,0]).reshape(N,N); Om /= Om.max()
    u = np.log(Om)
    d = lambda f, ax: np.gradient(f, h, axis=ax, edge_order=2)
    ux, ub = d(u,0), d(u,1)
    Jxx, Jxb, Jbb = d(ux,0), d(ux,1), d(ub,1)
    # outside pressure directly from H_out Omega / Omega
    W_B = (-eps*d(d(Om,1),1) + V_out*Om)/Om
    W_B_pp = d(d(W_B,0),0)
    # RHS of the claimed identity
    KbJxx = -eps*(d(d(Jxx,1),1) + 2*ub*d(Jxx,1))
    rhs = -2*eps*Jxb**2 + KbJxx
    # conditional eigenfunction identity
    V_B_pp = d(d(V_B,0),0)
    KxJxx = -eps*(d(d(Jxx,0),0) + 2*ux*d(Jxx,0))
    lhs2 = V_B_pp + W_B_pp; rhs2 = 2*eps*Jxx**2 - KxJxx
    # compare on the interior window |x|,|b| <= 1.2
    m = (np.abs(X) <= 1.2) & (np.abs(Bc) <= 1.2)
    def rel(a, b): return np.max(np.abs(a[m]-b[m]))/max(np.max(np.abs(b[m])), 1e-12)
    print(f"eps={eps} A={A} B={B} C={C} lam={lam} N={N} h={h:.4f} E0={E[0]:.6f}  (Gaussian E0 would be eps*(A+C)={eps*(A+C):.6f})")
    print(f"  identity W_B'' = -2eps Jxb^2 + K_b Jxx : max rel err {rel(W_B_pp, rhs):.2e}   (|W_B''| max {np.max(np.abs(W_B_pp[m])):.4f})")
    print(f"  identity V_B''+W_B'' = 2eps Jxx^2 - K_x Jxx : max rel err {rel(lhs2, rhs2):.2e}")
    print(f"  split: max|-2eps Jxb^2| = {np.max(np.abs(2*eps*Jxb[m]**2)):.4f}, max|K_b Jxx| = {np.max(np.abs(KbJxx[m])):.4f}")
    if lam == 0:
        print(f"  Gaussian: W_B'' mean {W_B_pp[m].mean():.5f} vs -2 eps B^2 = {-2*eps*B*B:.5f};  V_B''+W_B'' mean {lhs2[m].mean():.5f} vs 2 eps A^2 = {2*eps*A*A:.5f};  Jxx mean {Jxx[m].mean():.5f} vs -A={-A}")
        # the classical Schur complement (marginal precision) for contrast
        print(f"  contrast: marginal (Schur) precision A - B^2/C = {A - B*B/C:.5f}; conditional precision A = {A}; sqrt(A^2+B^2)={np.sqrt(A*A+B*B):.5f}")
run(0.8, 1.5, 0.6, 2.0, 0.0)
run(0.8, 1.5, 0.6, 2.0, 0.15)
run(1.0, 1.0, 0.9, 1.6, 0.3)
