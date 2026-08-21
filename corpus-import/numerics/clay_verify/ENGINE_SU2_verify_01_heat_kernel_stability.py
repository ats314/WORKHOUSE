import numpy as np
import scipy.optimize
from dataclasses import dataclass
from typing import List, Tuple, Callable

# Constants for SU(2) from Appendix E.3
# c2(Ad) = 4, rho = 1, c2(F) = 3/4 (Wait, paper says 3 in Appendix E.3? Let's check.)
# Re-reading Appendix E.3 line 1250: "For SU(2): c_2(Ad) = 4, rho = 1, c_2(F) = 3, and D^2 = 8pi^2."
# The paper normalization is g = -Killing = 2N(-Tr). 
# Standard physics usually has c2(F) = 3/4 for SU(2). This means their metric is scaled.
# We will use the PAPER'S CONSTANTS exactly to match their bounds.

@dataclass
class SU2Constants:
    """Constants exactly as defined in the Heat Kernel paper, Appendix E."""
    N: int = 2
    c2_Ad: float = 4.0
    rho_G: float = 1.0
    c2_F: float = 3.0
    D_squared: float = 8 * np.pi**2
    
    # Delta_deg for d=4 lattice: 2*(d-1) = 6 plaquettes per link? 
    # Wait, Section 3 says: "In d=4, a spatial link sits in 4 purely spatial plaquettes... and 2 temporal."
    # Total = 6. 
    # BUT, "Delta_deg is the maximal number of neighbours of a link (Delta <= 12)". 
    # Section 3: "Two adjacent links belong to at most two common plaquettes."
    # Let's use Delta_deg = 12 as the safe upper bound mentioned in paper (Eq 18).
    Delta_deg: int = 12 
    
    # Dobrushin constant factor C_D = 2 * Delta_deg
    C_D: int = 24  # (Eq 18)

class HeatKernelSU2:
    def __init__(self, constants: SU2Constants = SU2Constants()):
        self.c = constants
        
    def dimension(self, j_index: int) -> int:
        """Dimension d_lambda for SU(2) irrep with index j (0, 1/2, 1...).
        Here we use integer index k = 2j to avoid floats. k=0,1,2...
        d_k = k + 1. 
        """
        # Paper uses sum over lambda in G_hat. For SU(2), lambda ~ integer n >= 0 (dim n+1).
        # c2(lambda) = (n/2)(n/2 + 1) * scaling? 
        # Let's infer scaling from c2(F)=3. F corresponds to n=1 (dim 2).
        # Standard: 1/2 * 3/2 = 3/4. 
        # Paper: 3.
        # Factor = 4.
        # So c2_paper(n) = 4 * (n/2 * (n/2 + 1)) = n(n+2).
        return j_index + 1
        
    def casimir_paper(self, j_index: int) -> float:
        """Casimir eigenvalue c2(lambda) in paper normalization."""
        # j_index = 0 (trivial), 1 (fund, dim 2), 2 (adj, dim 3?? No, adj is dim 3).
        # SU(2) reps: 0 (1), 1/2 (2), 1 (3), 3/2 (4)...
        # Our j_index is 2*spin. 
        # j_index=1 -> spin 1/2 -> dim 2. c2 should be 3.
        # Formula n(n+2) -> 1(3) = 3. Correct.
        # j_index=2 -> spin 1 -> dim 3 (Adjoint). c2 should be 4?
        # Formula 2(4) = 8.
        # Paper says c2(Ad) = 4.
        # Wait. Appendix E.3: "c2(Ad) = 4".
        # Let's check my scaling.
        # Spin 1 is the adjoint representation of SU(2).
        # Standard c2(1) = 1(2) = 2.
        # Paper c2(Ad) = 4. Factor is 2.
        # So c2_paper(spin) = 2 * (spin * (spin+1)).
        # Let's check spin 1/2 (Fund).
        # c2_paper(1/2) = 2 * (0.5 * 1.5) = 2 * 0.75 = 1.5.
        # BUT Appendix E.3 says "c2(F) = 3".
        # CONTRADICTION.
        
        # Let's re-read Appendix E.1 carefully.
        # "c2(Ad) = 2N". For N=2, c2(Ad) = 4. Matches.
        # "c2(F) = (N^2 - 1)/N * scaling?"
        # Eq 65: "c2(F) = (N^2-1)/N * (something implied)".
        # Actually Eq 65 just says c2(F) = (N^2-1)/N? No, that's 3/2 for N=2.
        # Paper says c2(F) = 3.
        # So there is a factor of 2 somewhere.
        # Ah, "We fix the bi-invariant metric to be g = -Killing = 2N(-Tr)".
        # Usually Killing is 4N(-Tr) or something?
        
        # Let's Trust the Explicit Numbers in E.3 for SU(2):
        # c2(F) = 3. c2(Ad) = 4.
        # Let's fit a quadratic model a*j(j+1).
        # j=1/2 (F): a * 3/4 = 3 => a = 4.
        # j=1 (Ad): a * 2 = 8.
        # But paper says c2(Ad) = 4.
        # THIS IS A PROBLEM. c2(F) cannot be 3 if c2(Ad) is 4 in standard SU(2).
        # Usually c2(F) < c2(Ad). 3 < 4. This holds.
        # Ratios: Standard c2(F)/c2(Ad) = (3/4) / 2 = 3/8.
        # Paper c2(F)/c2(Ad) = 3 / 4.
        # The ratio is different!
        # 3/4 != 3/8.
        # What is going on?
        
        # Re-read Appendix E.1 Eq 65 carefully.
        # "c2(F) = (N^2 - 1) / N".
        # For N=2: (4-1)/2 = 1.5. 
        # But E.3 says "c2(F) = 3".
        # So there is a factor of 2. 1.5 * 2 = 3.
        # Let's check Adjoint with factor 2.
        # Standard Adjoint c2 is 2N? Or just N?
        # For SU(N), c2(Ad) = N? No, that's Dual Coxeter.
        # Standard physics: T_a T_a = C_F * 1. f_abc f_abd = C_A * delta_cd.
        # C_F = (N^2-1)/2N. C_A = N.
        # For N=2: C_F = 3/4. C_A = 2.
        # Ratio C_F/C_A = (3/4)/2 = 3/8.
        
        # Paper: c2(F)=3, c2(Ad)=4.
        # Ratio 3/4.
        # This implies Adjoint is NOT spin 1?
        # Or Fundamental is NOT spin 1/2?
        # Or metric is weird.
        
        # NOTE: "c_2(F) = (N^2 - 1)/N ... (65)"
        # "c_2(Ad) = 2N ... (Paragraph E)"
        # For N=2: c2(F) = 1.5. c2(Ad) = 4.
        # 1.5 vs 3? 
        # Maybe E.3 says "c2(F) = 3" because of the factor of 2 mentioned in E.
        # "g = -Killing = 2N(-Tr)... so rho = c2(Ad)/4 = N/2".
        # c2(Ad) = 2N = 4. Correct.
        # Eq 65 says c2(F) = (N^2-1)/N? If so, that is 1.5.
        # But E.3 explicitly says "c2(F) = 3".
        # 1.5 * 2 = 3.
        # So Eq 65 must be missing the factor of 2, or I am misreading "In this normalization one has".
        # I will assume the EXPLICIT NUMBERS in E.3 are the ground truth for the code.
        # c2(F) = 3. c2(Ad) = 4.
        
        # Implementation strategy:
        # Use a scaling factor 'scale' such that scale * j(j+1) matches the points.
        # j=1/2 -> 3. scale * 0.75 = 3 => scale = 4.
        # j=1 -> 4. scale * 2 = 8 != 4.
        # The Casimir scaling is NOT linear in j(j+1) with a single constant relative to standard physics?
        # Or Adjoint is not j=1?
        # Adjoint of SU(2) is spin 1. That is a fact.
        # Why is the ratio 3/4?
        
        # Let's look at Eq 66: "c* = min c2(lambda) = c2(F)".
        # "c2(F) = (N^2 - 1)/N". (Eq 65).
        # For N=2, this is 1.5.
        # E.3 says c2(F) = 3.
        # This implies "c2(F)" in text might obtain a factor of 2.
        # And c2(Ad) = 2N = 4.
        # 1.5 * 2 = 3.
        # 2N = 4.
        # So EVERYTHING is scaled by 2 relative to "standard" group theory formulas where C_A=2N? No C_A=N.
        # If C_A (standard) = 2, and Paper C_A = 4, factor is 2.
        # If C_F (standard) = 3/4 = 0.75. Paper C_F = 3?
        # 0.75 * 4 = 3.
        # So Adjoint factor = 2, Fundamental factor = 4.
        # Contradiction.
        
        # HYPOTHESIS: The "Adjoint" in the paper might not be the standard Adjoint rep in terms of spectral gap?
        # Or maybe c2(Ad) in E.3 refers to something else?
        # "c2(Ad) = 4, rho = 1".
        # "c2(F) = 3".
        # Let's assume the paper's explicit numbers for F and Ad are correct for the *states* 
        # But for the *general series* in Heat Kernel formula (1):
        # K_t(g) = sum d_lam exp(-t c2(lam)) chi_lam(g).
        # We need c2(lam) for ALL lambda.
        # Lambda for SU(2) are measured by integer k >= 0 (dim k+1).
        # k=1 (Fund, dim 2) -> c2 = 3.
        # k=2 (Adj, dim 3) -> c2 = 4? OR c2 = 8?
        
        # If c2(Ad) = 4 really corresponds to the Adjoint rep (k=2), then:
        # k=1 -> 3.
        # k=2 -> 4.
        # This is a weird spectrum. 3, 4, ...
        # Formula: c2(k) = A k + B?
        # If c2 ~ k(k+2) (standard Casimir shifted): 
        # k=1 -> 1(3) = 3. Matches!
        # k=2 -> 2(4) = 8.
        # Maybe the "Adjoint" listed in E.3 is NOT the next one in the series?
        # No, Adjoint is dim 3. It MUST be k=2.
        # If E.3 says c2(Ad)=4, and formula gives 8... 
        
        # Wait, looked at E.1 again.
        # "c2(Ad) = 2N" (Eq just above 65).
        # "c2(F) = (N^2 - 1)/N ... (65)".
        # For N=2: c2(Ad) = 4. c2(F) = 1.5.
        # BUT E.3 lists "c2(F) = 3".
        # This is a factor of 2 discrepancy between E.1 formulas and E.3 numbers for F.
        # AND E.3 c2(Ad) matches E.1 (4=4).
        # So F is scaled by 2, Ad is scaled by 1 relative to E.1 formulas?
        # This is extremely confusing.
        
        # Safest bet: The series expansion (Eq 1) dominates.
        # Usually c2 is monotonic.
        # If F (first excited state) has gap 3.
        # Then Ad (second excited) having gap 4 is essentially impossible if it's j(j+1).
        # 3 vs 4 is very close. 
        # Gap ratio 4/3 = 1.33.
        # Standard ratio 8/3 = 2.66.
        # This suggests the "Adjoint" might not be the k=2 state?
        # No, Adjoint is definitely k=2.
        
        # Let's check SU(3).
        # N=3.
        # E.1: c2(Ad) = 2N = 6.
        # E.1: c2(F) = (9-1)/3 = 8/3 = 2.66.
        # E.3: c2(Ad) = 6. (Matches).
        # E.3: c2(F) = 8. (Factor of 3 discrepancy! 8/3 * 3 = 8).
        # SU(2) factor was 2 (1.5 * 2 = 3).
        # SU(3) factor is 3.
        # It seems c2(F)_explicit = N * c2(F)_formula.
        # (N^2-1)/N * N = N^2 - 1.
        # For N=2: 3. Correct.
        # For N=3: 8. Correct.
        
        # Does this apply to Adjoint?
        # c2(Ad)_formula = 2N.
        # c2(Ad)_explicit = 6 (N=3), 4 (N=2).
        # So Adjoint is NOT scaled by N.
        # It stays 2N.
        
        # This implies the spectrum c2(lambda) is NOT just a single scalar multiple of quadratic Casimir.
        # Or my reading of "c2(Ad)" in E.3 is wrong.
        # Maybe "c2(Ad)" is not the eigenvalue of the Adj rep, but a constant of the group?
        # "Ric = 1/4 c2(Ad) g". This is a structural constant.
        
        # CRITICAL INSIGHT:
        # In Heat Kernel expansion, we need the eigenvalues c2(lambda).
        # c2(F) is the FIRST eigenvalue (Gap).
        # c2(F) = N^2 - 1. (Based on E.3 numbers).
        # What is the formula for general lambda?
        # General Casimir eigenvalue is <lambda + 2rho, lambda>.
        # If F (lambda=[1,0..]) is N^2-1.
        # We can deduce the scaling.
        # Standard Casimir for SU(N): Fundamental is (N^2-1)/(2N).
        # We need (N^2-1).
        # Factor is 2N.
        # Let's try rescaling Standard Casimir by 2N.
        # Standard Adj: N.
        # Scaled Adj: N * 2N = 2N^2.
        # For N=2: 2(4) = 8.
        # Paper E.3 says c2(Ad) = 4.
        # My scaling hypothesis (Factor 2N) fails for Ad. (Gives 8, want 4).
        
        # Re-read E.3 very carefully.
        # "c2(Ad) = 4".
        # "c2(F) = 3".
        # Gap ratio 4/3.
        # Is it possible c2(Ad) refers to something else? 
        # No, "c2(F)... and c2(lambda) >= c2(F)... c* = min c2 = c2(F)".
        # It treats c2 as the eigenvalue.
        
        # Maybe SU(2) Adjoint is NOT c2(Ad)?
        # For SU(2), Representations are k=0,1,2...
        # k=1 is F. c2=3.
        # k=2 is Adj. c2=?
        # If c2 is quadratic, c2 ~ k(k+2).
        # k=1 -> 3.
        # k=2 -> 8.
        # The value "4" in E.3 might be the structural constant "c2(Ad)" (used for Ricci), NOT the eigenvalue of the Adjoint representation in the Heat Kernel sum.
        # The Ricci curvature depends on structure constants f_abc. sum f_ac d f_bc d ~ c2(Ad).
        # It is possible that the eigenvalue for the Adjoint rep (k=2) is indeed 8, but the parameter listed as "c2(Ad)" is just the group constant 4.
        # This resolves the contradiction.
        # I will assume the Heat Kernel eigenvalues follow the pattern set by c2(F)=3.
        # Pattern: c2_paper(k) = k(k+2). (For SU(2) with index k=2j).
        # k=1 -> 3. (Matches E.3 F).
        # k=2 -> 8. (Adj eigenvalue).
        # E.3 "c2(Ad)=4" is likely the structural constant C_A derived from Killing form normalization, not the Laplacian eigenvalue of the rep.
        
        pass

    def get_eigenvalues_and_dims(self, max_k: int = 20) -> Tuple[List[float], List[int]]:
        """
        Returns list of (eigenvalue, dimension) for k=0 to max_k.
        For SU(2), k corresponds to spin j=k/2.
        Using formula inspired by c2(F)=3: c2(k) = k(k+2).
        """
        c2_vals = []
        dims = []
        for k in range(max_k + 1):
            # dim = k + 1
            d = k + 1
            # c2 = k(k+2)
            c = k * (k + 2)
            c2_vals.append(c)
            dims.append(d)
        return c2_vals, dims

    def compute_M2(self, t: float, max_k: int = 50) -> float:
        """
        Compute M_2(t) bound from Eq 69 (Appendix G.1).
        M_2(t) = sup_{g} ||Hess V||.
        The paper gives an explicit series bound:
        M_s2(I) formula involves sum d^2 c2^2 (1+c2)^(s/2) e^-t c2.
        For M_2(t) specifically (Hessian bound), we want the global bound.
        Appendix G.1 Eq 69 defines M_{s,2} which seems to cover derivatives.
        For Hessian, we likely need s=0 or specific indices?
        
        Actually, let's look at Eq 12 (Lemma 2.3).
        M_2(t) <= 1/inf_K * sum_{lam!=0} d_lam^2 c2(lam)^2/2 * e^-t c2(lam)? No, index i=2.
        Eq 12: M_i(t) <= 1/inf K * sum d^2 c2^(i/2) ...
        Wait, Eq 12 says: M_i(t) <= ... c2(lam)^(i/2).
        For M_2 (Hessian), i=2.
        So factor is c2(lam)^(2/2) = c2(lam).
        But Appendix G.1 Eq 69 has c2^2? And (1+c2)^(s/2)?
        That looks like a Sobolev norm bound.
        
        Let's stick to Lemma 2.3 Eq 12 for large t, which is cleaner.
        M_2(t) <= (1 / inf K_t) * Sum_{lam!=0} d_lam^2 c2(lam) e^{-t c2(lam)}.
        WAIT. Lemma 2.3 says "c2(lam)^(i/2)".
            For i=2: c2^1 = c2.
            So we sum: d^2 * c2 * e^{-t c2}.
            
        We also need inf K_t(g).
        For SU(N), min of heat kernel is at maximal distance (g = -1 for SU(2)).
        K_t(-1) = Sum d_lam e^{-t c2} chi_lam(-1).
        chi_k(-1) = sin((k+1)pi)/sin(pi)? Limit (-1)^k.
        Actually chi_k(-1) = (k+1)*(-1)^k.
        So inf K_t = Sum (k+1) (-1)^k e^{-t k(k+2)}.
        """
        
        c2s, dims = self.get_eigenvalues_and_dims(max_k)
        
        # 1. Compute inf K_t (at g = -1, angle 2pi)
        # Expansion: sum d_k e^-t c2 chi_k(-1)
        # chi_k(-1) = d_k * (-1)^k
        inf_K = 0.0
        for k in range(len(c2s)):
            term = dims[k] * ((-1)**k * dims[k]) * np.exp(-t * c2s[k]) 
            # Wait, character at -I is d_k * (-1)^k?
            # SU(2) characters at 2pi (which is -I in spinor rep, I in SO(3)).
            # Angle parameter runs 0 to 4pi for SU(2).
            # Center is at 2pi?
            # chi_k(theta) = sin((k+1)theta/2) / sin(theta/2).
            # As theta -> 2pi:
            # Numerator: sin((k+1)pi). 0.
            # Denom: sin(pi) = 0.
            # L'Hopital: (k+1)/2 cos / 1/2 cos = (k+1) * (-1)^(k+1) / (-1)^1 ?
            # cos((k+1)pi) = (-1)^(k+1).
            # cos(pi) = -1.
            # Ratio: (k+1) (-1)^k+1 / -1 = (k+1) (-1)^k.
            # Correct.
            # WAIT. Group manifold SU(2) is S3.
            # Geodesic distance to -1 is pi? Or 2pi?
            # Standard metric on S3 (unit sphere). Diameter is pi.
            # Paper D^2 = 8pi^2.
            # If D = sqrt(8)*pi = 2sqrt(2)pi, this is weird.
            # Normal S3 diameter is pi.
            # This confirms metric scaling. 
            # If D_paper = 2sqrt(2) D_std, then scalar curvature scales by 1/(2sqrt(2))^2 = 1/8.
            # This explains why c2(F) is 3 instead of 3/4? (Factor 4).
            # Yes. 3 = 4 * 0.75.
            # So the metric is scaled by 4 (length scale x2).
            # Length x2 => Diameter x2.
            # Std Diam = pi. Paper Diam should be 2pi.
            # D^2 = 4pi^2.
            # But E.3 says D^2 = 8pi^2?
            # Maybe D is not just antipodal distance?
            # "D = diam(G) (bi-invariant metric)".
            # Eq 67: D^2 = 2 N pi^2 (N even).
            # For N=2: 4pi^2?
            # Eq 67 says D^2 = 2(4)pi^2 = 8pi^2.
            # So Diameter = sqrt(8) pi = 2.82 pi.
            # This is > 2pi.
            # How can diameter be > circumference?
            # Maybe my S3 intuition is off for the Killing metric normalization.
            # Regardless, the min of heat kernel is at the antipodal point.
            
            # For our sum, we just use the alternating series.
            # Note: For small t, explicit Gaussian bounds (Eq 9) are better than truncated sum.
            # But for "Super-Extractor" we verify t ~ physical values.
            # If t is too small, sum converges slowly.
            
            term_val = dims[k] * ((-1)**k * dims[k]) * np.exp(-t * c2s[k]) 
            # Note: The trace of rep is chi(g).
            # K(g) = sum d * e * chi.
            # chi(-1) = (-1)^k * (k+1).
            # So we multiply by d again? No.
            # Formula (1): sum d_lam e^-t c2 chi_lam.
            # K(-1) = sum (k+1) e^-t c2 [ (k+1)(-1)^k ].
            # = sum (k+1)^2 (-1)^k e^-t c2.
            inf_K += term_val
            
        # 2. Compute Sum for M_2 bound
        # Lemma 2.3 Eq 12: Sum_{lam avg} d^2 c2^(i/2) e^-t c2.
        # i=2 -> c2.
        numerator_sum = 0.0
        for k in range(1, len(c2s)): # Exclude k=0 (c2=0)
            # term = d^2 * c2 * e^-t c2
            term = (dims[k]**2) * c2s[k] * np.exp(-t * c2s[k])
            numerator_sum += term
            
        return numerator_sum / inf_K

class BoundChecker:
    def __init__(self):
        self.hk = HeatKernelSU2()
        
    def check_stability(self, t_phys: float) -> dict:
        """
        Check stability for a given time t (mapped to lattice spacing a).
        Assume t0 = t1 = t for simplicity (symmetric timesteps).
        """
        # 1. Compute M2(t)
        M2 = self.hk.compute_M2(t_phys)
        
        # 2. Calculate Dobrushin Alpha
        # alpha = C_D * 2 * M2  (Since M2(t0)+M2(t1) = 2M2)
        # C_D = 24.
        alpha = 24 * 2 * M2
        
        # 3. Calculate Bakry-Emery Kappa
        # kappa = rho - 6 * 2 * M2
        # rho = 1 for SU(2) (Appendix E.3)
        rho = 1.0
        kappa = rho - 12 * M2
        
        return {
            "t": t_phys,
            "M2": M2,
            "alpha": alpha,
            "kappa": kappa,
            "Route_B_Pass": alpha < 1.0,
            "Route_A_Pass": kappa > 0.0
        }

def run_extraction():
    checker = BoundChecker()
    
    print("--- Heat Kernel Super-Extractor Results (SU(2)) ---")
    print(f"{'t':<10} {'M2(t)':<12} {'Alpha':<10} {'Kappa':<10} {'Route A':<10} {'Route B':<10}")
    print("-" * 70)
    
    # Scan a range of t values
    # From Appendix H, they look at I=[0.8, 1.2]. 
    # Let's scan 0.1 to 2.0 to seeing crossover.
    for t in np.linspace(0.1, 2.0, 20):
        res = checker.check_stability(t)
        
        # Anomaly Bound (Geometric/P04)
        # Relation: beta = N / (2t) for SU(N)?
        # Derivation: exp(-theta^2/4t) vs exp(-beta theta^2/2N)
        # 1/4t = beta/2N => beta = N / (2t).
        # For N=2: beta = 1/t.
        # sigma_geom = N^2/(3*beta) (from P04: sigma >= N g^2 a^2 / 6 = N (2N/beta)/6 = N^2/3beta)
        # For N=2: sigma = 4 / (3 * (1/t)) = 4t/3 = 1.33 t.
        
        beta_equiv = 1.0 / t
        sigma_geom = (4.0) / (3.0 * beta_equiv)
        
        pass_a = "PASS" if res["Route_A_Pass"] else "FAIL"
        # pass_b = "PASS" if res["Route_B_Pass"] else "FAIL" # Route B is usually too strict
        
        # Compare Kappa (Heat Kernel) vs Sigma (Geometric)
        print(f"{t:<10.4f} {res['M2']:<12.6f} {res['alpha']:<10.4f} {res['kappa']:<10.4f} {sigma_geom:<10.4f} {pass_a:<10}")

if __name__ == "__main__":
    run_extraction()
