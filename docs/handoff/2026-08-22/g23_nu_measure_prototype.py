"""G23 nu-measure prototype: does the archive's nu ∝ e^(-S_sp) equal the true
slice marginal in the INTERACTING case, and what does the mismatch do to the
corrected scale-a bridge?

Model: 0+1 dimensional lattice scalar field = quartic anharmonic oscillator,
the minimal interacting extension of the archive's own Gaussian toy
(REFLECTION_POSITIVITY/01_OS_RECONSTRUCTION/06_toy_os_dirichlet_hinge_gaussian.md,
digest f406c532...), with the archive's definitions transcribed:

  Euclidean chain measure  mu ∝ prod_t That(phi_t, phi_{t+1}),
  That(x,y) = (2 pi a)^{-1/2} exp(-(x-y)^2/(2a)) e^{-(a/2)V(x)} e^{-(a/2)V(y)},
  V(phi) = (1/2) m^2 phi^2 + lam phi^4          (lam = 0 is the Gaussian control)

  S_sp(phi)  = a V(phi)      -- "the purely spatial plaquette action in the
                                slice" (06_OS_mass_gap_reductions.md L110-112);
                                in 0 spatial dimensions the in-slice part of
                                the action is the potential term. The strip
                                weight W_a carries e^{-S_sp/2} on each side
                                (J_..._comparison.md §2.1 L68-70), which is
                                exactly That above.
  nu_arch    ∝ e^{-S_sp} dphi   (the archive's boundary measure,
                                 J_..._comparison.md §2.3 L84-87;
                                 06_OS_mass_gap_reductions.md §3.1 L108-112)
  nu_true    = psi_0^2 dphi     (the mu-law of one slice: for the periodic chain
                                 marginal(phi) = [That^T](phi,phi)/Tr That^T ->
                                 psi_0(phi)^2, psi_0 the L^2(dphi)-normalized
                                 Perron eigenfunction of That)

All numbers are floats from deterministic quadrature on a uniform grid (no
Monte Carlo); lam = 0 rows are checked against closed forms:
  Var_true = 1/(m sqrt(a^2 m^2 + 4)),   Var_arch = 1/(a m^2),
  Delta_OS = arccosh(1 + a^2 m^2/2)/a,  gap(-L_true) = 2*omega_t,
  omega_t  = m sqrt(a^2 m^2 + 4)/2  (psi_0 ∝ e^{-omega_t phi^2/2}),
  commuting-basis bridge constant c_1 = (1-e^-theta)/(1-e^{-2 sinh theta}).

Computed per (lam, a), m^2 = 1 throughout:
 (1) measure gap nu_true vs nu_arch: Var ratio, total variation, KL, tail
     exponents (-ln nu ~ |phi|^p: p -> 3 for the true marginal of a quartic
     model (Agmon), p = 4 for e^{-S_sp}: no coupling rescaling reconciles them)
 (2) FINDING (algebra + machine check): the archive's own symmetrized strip
     operator on L^2(nu_arch) equals sqrt(nu_arch) G_a sqrt(nu_arch), which is
     PROPORTIONAL TO That: the e^{-S_sp} weights cancel identically. Hence its
     Perron vector is h = e^{S_sp/2} psi_0 and its Doob Markovization is a
     Markov operator w.r.t. h^2 nu_arch = psi_0^2 = nu_true EXACTLY.
     Markovianity + self-adjointness force the true marginal; e^{-S_sp} is
     never the invariant measure. Also: Markov defect of the un-Doobed
     operator (A1 != const) on the physical window.
 (3) isometry defect: for F = f(phi_1) in A^+, site reflection gives exactly
     (F,F)_OS = ||E_mu[F|phi_0]||^2_{L^2(nu_true)}; the archive integrates the
     same JF against nu_arch. Both numbers and their ratio.
 (4) corrected scale-a bridge on the TRUE marginal (the interacting version of
     the review's Gaussian c ~ 1/2 test): pencil extremes of
     (I - K_a) vs (I - P_a) on mean-zero f in L^2(nu_true), K_a = Doob
     transform of That (exact compressed OS transfer operator), P_a = e^{aL},
     L reversible for nu_true with Gamma(f)=|f'|^2 (graph Laplacian). Plus the
     end-to-end mass the chain (3.5)-(3.8) certifies, vs the exact Delta_OS.
 (5) the same bridge with nu = nu_arch (the archive's literal reading):
     vacuum dissipation of the constant (0 for a Markov operator), overlap of
     the constant with the actual Perron vector, and the mass the wrong-measure
     chain certifies.

Single core (env pinned by caller).
"""

import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal

M2 = 1.0  # m^2 (float)


def V(phi, lam):
    return 0.5 * M2 * phi**2 + lam * phi**4


def build_grid(lam, a, boost=1.0):
    m = np.sqrt(M2)
    sig_true_gauss = (1.0 / (m * np.sqrt(a * a * M2 + 4.0))) ** 0.5  # lam=0; quartic narrows
    x = np.linspace(-60, 60, 24001)
    w = np.exp(-a * (V(x, lam) - V(0.0, lam)))
    sig_arch = np.sqrt(np.trapezoid(x * x * w, x) / np.trapezoid(w, x))
    L = 6.0 * max(sig_true_gauss, sig_arch) + 4.0 * np.sqrt(a)
    dphi = min(np.sqrt(a) / 5.0, sig_true_gauss / 10.0) / boost
    n = int(2 * L / dphi) + 1
    n = min(n | 1, 2001)
    return np.linspace(-L, L, n)


def heat_kernel(phi, a):
    return np.exp(-((phi[:, None] - phi[None, :]) ** 2) / (2.0 * a)) / np.sqrt(2 * np.pi * a)


def laplacian_H(nu, dphi):
    """Symmetric rep H = D^{-1/2} Lambda D^{-1/2} of -L, Dirichlet form
    int nu |f'|^2, weight D = nu*dphi. Returns (diag, offdiag, D)."""
    D = nu * dphi
    c = 0.5 * (nu[:-1] + nu[1:]) / dphi
    lam_diag = np.zeros_like(nu)
    lam_diag[:-1] += c
    lam_diag[1:] += c
    s = 1.0 / np.sqrt(D)
    return lam_diag / D, -c * s[:-1] * s[1:], D


def pencil_extremes(Asym, Bsym, g0):
    """min/max of f'Af/f'Bf over f orthogonal to unit vector g0."""
    n = len(g0)
    v = g0.copy()
    v[0] += 1.0 if g0[0] >= 0 else -1.0
    v /= np.linalg.norm(v)
    Hh = np.eye(n) - 2.0 * np.outer(v, v)
    Q = Hh[:, 1:]
    Ap = Q.T @ Asym @ Q
    Bp = Q.T @ Bsym @ Q
    Ap = 0.5 * (Ap + Ap.T)
    Bp = 0.5 * (Bp + Bp.T) + 1e-13 * np.eye(n - 1)
    vals = eigh(Ap, Bp, eigvals_only=True)
    return float(vals[0]), float(vals[-1])


def tail_exponent(phi, dens, lo_sig=2.5, hi_sig=5.0):
    dens = dens / dens.max()
    sig = np.sqrt(np.sum(phi**2 * dens) / np.sum(dens))
    mask = (phi > lo_sig * sig) & (phi < hi_sig * sig) & (dens > 1e-12)
    if mask.sum() < 8:
        mask = (phi > 1.5 * sig) & (dens > 1e-12)
    x = np.log(phi[mask])
    y = np.log(-np.log(dens[mask]))
    sol = np.linalg.lstsq(np.vstack([x, np.ones_like(x)]).T, y, rcond=None)[0]
    return float(sol[0])


def run_point(lam, a, boost=1.0, verbose=True):
    phi = build_grid(lam, a, boost)
    dphi = phi[1] - phi[0]
    n = len(phi)
    G = heat_kernel(phi, a)
    half = np.exp(-0.5 * a * (V(phi, lam) - V(0.0, lam)))  # e^{-S_sp/2}, gauge-fixed at 0
    Ksym = (half[:, None] * G * half[None, :]) * dphi  # symmetric rep of That (x const)

    evals, evecs = eigh(Ksym)
    lam0, lam1, lam2 = evals[-1], evals[-2], evals[-3]
    u0 = evecs[:, -1]
    if u0[n // 2] < 0:
        u0 = -u0
    Delta_OS = -np.log(lam1 / lam0) / a
    Delta2_OS = -np.log(lam2 / lam0) / a

    # measures on the full grid
    nu_true_full = np.maximum(u0, 0.0) ** 2 / dphi
    nu_true_full /= np.sum(nu_true_full) * dphi
    w_arch = half**2
    nu_arch = w_arch / (np.sum(w_arch) * dphi)

    var_true = float(np.sum(phi**2 * nu_true_full) * dphi)
    var_arch = float(np.sum(phi**2 * nu_arch) * dphi)
    tv = float(0.5 * np.sum(np.abs(nu_true_full - nu_arch)) * dphi)
    mk = nu_true_full > 1e-12 * nu_true_full.max()
    kl = float(np.sum(nu_true_full[mk] * np.log(nu_true_full[mk] / nu_arch[mk])) * dphi)
    p_true = tail_exponent(phi, nu_true_full)
    p_arch = tail_exponent(phi, nu_arch)

    # ---- (2) the archive strip operator on L^2(nu_arch) ----
    # restrict nu_arch-side OPERATORS to where nu_arch has float support
    # (quartic tails underflow; mass loss <= 1e-30)
    ga = np.where(nu_arch > 1e-30 * nu_arch.max())[0]
    asl = slice(ga.min(), ga.max() + 1)
    phia = phi[asl]
    na = len(phia)
    nu_arch_a = nu_arch[asl] / (np.sum(nu_arch[asl]) * dphi)
    sqa = np.sqrt(nu_arch_a * dphi)
    Asym = (sqa[:, None] * G[asl, asl] * sqa[None, :]) * dphi  # symmetrized strip op
    # theorem: Asym ∝ Ksym (e^{-S_sp} cancels).  machine check:
    prop_dev = float(np.max(np.abs(Asym / np.max(Asym) - Ksym[asl, asl] / np.max(Ksym))))
    const = np.max(Asym) / np.max(Ksym)
    lamA = lam0 * const
    u0a = u0[asl]
    # Perron in function coords: h = u0/sqrt(nu_arch dphi) ∝ e^{S_sp/2} psi_0 -- identity
    # Markovization measure = u0^2 ∝ nu_true: identity by the same algebra.
    # Markov defect of A/lamA on the physical window |phi| < 4 sqrt(var_true):
    one_arch = sqa / np.linalg.norm(sqa)
    A1_f = (Asym @ sqa) / lamA / sqa
    win = np.abs(phia) <= 4.0 * np.sqrt(var_true)
    markov_defect = float((A1_f[win].max() - A1_f[win].min()) / np.median(A1_f[win]))
    vac_diss = float(one_arch @ one_arch - one_arch @ (Asym @ one_arch) / lamA)
    overlap = float(abs(one_arch @ u0a) / np.linalg.norm(u0a))

    # ---- trim to the true-measure core for the true-side operators ----
    good = np.where(np.abs(u0) > 1e-13 * np.abs(u0).max())[0]
    sl = slice(good.min(), good.max() + 1)
    phit, u0t = phi[sl], u0[sl]
    u0t = np.maximum(u0t, 1e-200)
    nt = len(phit)
    gt = u0t / np.linalg.norm(u0t)
    nu_true = gt**2 / dphi
    KMt = Ksym[sl, sl] / lam0  # Doob/Markov transfer op in g-coords, kernel gt

    # ---- (3) isometry defect ----
    iso = {}
    for name, fvals in (("phi", phit.copy()), ("phi^2", phit**2)):
        gf = gt * fvals
        Jf_g = KMt @ gf                      # JF = E[F | phi_0] in g-coords
        os_true = float(Jf_g @ Jf_g)         # (F,F)_OS exactly (site reflection)
        Jf_vals = Jf_g / gt                  # function values of JF
        os_arch = float(np.sum(Jf_vals**2 * nu_arch[sl]) * dphi)
        iso[name] = (os_true, os_arch, os_arch / os_true)

    # ---- (4) corrected bridge on the TRUE marginal ----
    Hd, Ho, _ = laplacian_H(nu_true, dphi)
    muL, UL = eigh_tridiagonal(Hd, Ho)
    muL = np.maximum(muL, 0.0)
    gapL = float(muL[1])
    Psym = (UL * np.exp(-a * muL)) @ UL.T
    A_true = np.eye(nt) - 0.5 * (KMt + KMt.T)
    B_true = np.eye(nt) - 0.5 * (Psym + Psym.T)
    c_min, c_max = pencil_extremes(A_true, B_true, gt)
    lamP = c_min * (1.0 - np.exp(-a * gapL))
    m_cert = -np.log(1.0 - lamP) / a

    # ---- (5) the bridge with nu = nu_arch ----
    lamPw, _ = pencil_extremes(np.eye(na) - Asym / lamA, np.eye(na), one_arch)
    m_wrong_gap = -np.log(max(1.0 - lamPw, 1e-300)) / a
    Hd2, Ho2, _ = laplacian_H(nu_arch_a, dphi)
    muA, UA = eigh_tridiagonal(Hd2, Ho2)
    muA = np.maximum(muA, 0.0)
    gapL_arch = float(muA[1])
    PsymA = (UA * np.exp(-a * muA)) @ UA.T
    cw_min, cw_max = pencil_extremes(
        np.eye(na) - 0.5 * (Asym + Asym.T) / lamA,
        np.eye(na) - 0.5 * (PsymA + PsymA.T),
        one_arch,
    )
    lamPwc = cw_min * (1.0 - np.exp(-a * gapL_arch))
    m_wrong_chain = -np.log(max(1.0 - lamPwc, 1e-300)) / a

    out = dict(
        lam=lam, a=a, n=n, nt=nt, L=float(phi[-1]), dphi=dphi,
        Delta_OS=float(Delta_OS), Delta2_OS=float(Delta2_OS),
        var_true=var_true, var_arch=var_arch, tv=tv, kl=kl,
        p_true=p_true, p_arch=p_arch,
        prop_dev=prop_dev, markov_defect=markov_defect,
        vac_diss=vac_diss, overlap=overlap, iso=iso,
        gapL=gapL, gap_ratio=gapL / (2 * Delta_OS),
        c_min=c_min, c_max=c_max, m_cert=m_cert,
        lamPw=lamPw, m_wrong_gap=m_wrong_gap,
        cw_min=cw_min, gapL_arch=gapL_arch, m_wrong_chain=m_wrong_chain,
    )
    if verbose:
        report(out)
    return out


def report(o):
    lam, a = o["lam"], o["a"]
    print(f"\n=== lam={lam}  a={a}   (n={o['n']} core {o['nt']}, L=+-{o['L']:.1f}, dphi={o['dphi']:.4f}) ===")
    print(f"  Delta_OS = {o['Delta_OS']:.6f}   Delta2_OS = {o['Delta2_OS']:.6f}")
    if lam == 0.0:
        m = np.sqrt(M2)
        th = float(np.arccosh(1 + a * a * M2 / 2))
        vt = 1.0 / (m * np.sqrt(a * a * M2 + 4))
        va = 1.0 / (a * M2)
        gl = m * np.sqrt(a * a * M2 + 4)
        c1 = (1 - np.exp(-th)) / (1 - np.exp(-2 * np.sinh(th)))
        print(f"    lam=0 controls:  Delta {th/a:.6f} (rel gap {abs(o['Delta_OS']-th/a)/(th/a):.1e})"
              f"   Var_true {vt:.6f} (rel gap {abs(o['var_true']-vt)/vt:.1e})")
        print(f"                     Var_arch {va:.6f} (rel gap {abs(o['var_arch']-va)/va:.1e})"
              f"   gap(-L) {gl:.6f} (rel gap {abs(o['gapL']-gl)/gl:.1e})")
        print(f"                     commuting-basis c_1 = {c1:.6f}  (pencil c_min = {o['c_min']:.6f})")
    print("  [1] nu_true vs nu_arch:")
    print(f"      Var_true = {o['var_true']:.6f}  Var_arch = {o['var_arch']:.6f}  ratio = {o['var_arch']/o['var_true']:.4f}")
    print(f"      TV = {o['tv']:.6f}   KL(true||arch) = {o['kl']:.6f}")
    print(f"      tail exponents: p_true = {o['p_true']:.3f}   p_arch = {o['p_arch']:.3f}")
    print("  [2] archive strip operator on L^2(nu_arch):")
    print(f"      symmetrization ∝ That: max dev = {o['prop_dev']:.2e} (e^-S_sp cancels identically)")
    print("      => Perron h = e^(S_sp/2) psi_0 and Markovization measure = psi_0^2 = nu_true (exact)")
    print(f"      Markov defect of A/lamA on |phi|<4sig: rel range of A1 = {o['markov_defect']:.4f} (Markov: 0)")
    print(f"      vacuum dissipation <1,(I-A/lamA)1>_arch = {o['vac_diss']:.6f} (Markov: 0)")
    print(f"      overlap |<1,Perron>|_arch = {o['overlap']:.6f} (constant = ground state would be 1)")
    for name, (t, w, r) in o["iso"].items():
        print(f"  [3] isometry, F={name}(t=1):  (F,F)_OS = {t:.6f}   archive nu_arch integral = {w:.6f}   ratio = {r:.4f}")
    print("  [4] corrected scale-a bridge on TRUE marginal:")
    print(f"      gap(-L_true) = {o['gapL']:.6f}   gap/(2*Delta_OS) = {o['gap_ratio']:.4f}")
    print(f"      pencil: c_min = {o['c_min']:.6f}   c_max = {o['c_max']:.6f}")
    print(f"      chain-certified mass = {o['m_cert']:.6f} = {o['m_cert']/o['Delta_OS']:.4f} * Delta_OS")
    print("  [5] bridge with nu = nu_arch (literal reading):")
    print(f"      constrained 'gap' of strip op on 1-perp -> mass {o['m_wrong_gap']:.6f} = {o['m_wrong_gap']/o['Delta_OS']:.4f} * Delta_OS")
    print(f"      wrong-measure pencil c_min = {o['cw_min']:.6f}, gap(-L_arch) = {o['gapL_arch']:.6f}"
          f" -> chain mass {o['m_wrong_chain']:.6f} = {o['m_wrong_chain']/o['Delta_OS']:.4f} * Delta_OS")


if __name__ == "__main__":
    results = []
    for lam in (0.0, 0.5, 2.0):
        for a in (1.0, 0.4, 0.1):
            results.append(run_point(lam, a))
    for lam in (0.0, 2.0):
        results.append(run_point(lam, 0.05))

    print("\n--- convergence check: lam=0.5, a=0.4 at 1.4x resolution ---")
    run_point(0.5, 0.4, boost=1.4)

    print("\n\n================ SUMMARY (all floats) ================")
    hdr = ("lam", "a", "TV", "KL", "Va/Vt", "p_tru", "p_arc",
           "c_min", "m_cert/D", "m_wrong/D", "ovlp")
    print(("{:>4} {:>5} {:>7} {:>8} {:>8} {:>6} {:>6} {:>8} {:>9} {:>10} {:>7}").format(*hdr))
    for o in results:
        print("{:>4} {:>5} {:>7.4f} {:>8.4f} {:>8.4f} {:>6.3f} {:>6.3f} {:>8.4f} {:>9.4f} {:>10.4f} {:>7.4f}".format(
            o["lam"], o["a"], o["tv"], o["kl"], o["var_arch"] / o["var_true"],
            o["p_true"], o["p_arch"], o["c_min"], o["m_cert"] / o["Delta_OS"],
            o["m_wrong_chain"] / o["Delta_OS"], o["overlap"]))
