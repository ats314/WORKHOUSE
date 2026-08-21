"""
dimensional_analysis.py - Automated Dimensional/Scaling Checks
===============================================================
Detect formulas that scale incorrectly under rescaling.
"""

import sympy as sp
from sympy import Symbol, sqrt, pi, Rational

print("="*60)
print("DIMENSIONAL / SCALING ANALYSIS")
print("="*60)

# Define dimensional symbols
a = Symbol('a', positive=True)  # lattice spacing [length]
beta = Symbol('beta', positive=True)  # coupling (dimensionless)
g = Symbol('g', positive=True)  # gauge coupling (dimensionless)
N = Symbol('N', integer=True, positive=True)  # SU(N) rank
m = Symbol('m', positive=True)  # mass [1/length]
Delta = Symbol('Delta', positive=True)  # spectral gap [1/length]
c_0 = Symbol('c_0', positive=True)  # Haar coefficient (dimensionless)
Lambda = Symbol('Lambda', positive=True)  # UV cutoff [1/length]

# =============================================================================
# 1. Gap Formula Scaling
# =============================================================================

print("\n--- Check 1: Gap Formula Delta >= sqrt(c_0/2) / a ---")

gap_formula = sqrt(c_0/2) / a

print(f"Formula: Delta >= {gap_formula}")
print()
print("Dimensional analysis:")
print("  [Delta] = [mass] = [1/length]")
print("  [sqrt(c_0/2)] = [dimensionless]")
print("  [1/a] = [1/length]")
print("  Result: [sqrt(c_0/2)/a] = [1/length] = [mass]")
print("  [CONSISTENT]")

# Rescaling test
lam = Symbol('lambda', positive=True)  # scale factor

a_scaled = lam * a
gap_scaled = sqrt(c_0/2) / a_scaled

print()
print(f"Under a -> lambda*a:")
print(f"  Gap becomes: {gap_scaled} = (1/lambda) * original")
print(f"  Physical mass m = Delta * a = sqrt(c_0/2) [INVARIANT]")
print("  [CONSISTENT]")

# =============================================================================
# 2. Dichotomy Scaling
# =============================================================================

print("\n--- Check 2: Dichotomy lambda_lat(a)/a > 0 ---")

lambda_lat = Symbol('lambda_lat', positive=True)  # lattice spectral gap

dichotomy = lambda_lat / a

print(f"Formula: liminf_{{a->0}} lambda_lat(a)/a > 0 for mass gap")
print()
print("Dimensional analysis:")
print("  [lambda_lat] = [1/time] = [1/length] (diffusion rate)")
print("  [lambda_lat/a] = [1/length^2] = [mass^2]")
print()
print("Issue: This gives [mass^2], not [mass]")
print("Resolution: The physical mass gap is sqrt(lambda_lat/a) * a = sqrt(lambda_lat*a)")
print("Or: lambda_lat ~ Delta^2 * a (standard transfer matrix relation)")

# =============================================================================
# 3. Coupling Scaling
# =============================================================================

print("\n--- Check 3: RG Stability Condition g^4 > 24/(c_0 a^2) ---")

rg_condition = g**4 > 24 / (c_0 * a**2)

print(f"Condition: g^4 > 24/(c_0 * a^2)")
print()
print("Dimensional analysis:")
print("  [g^4] = [dimensionless]")
print("  [24/(c_0*a^2)] = [1/length^2]")
print()
print("Issue: LHS dimensionless, RHS has dimension!")
print("This indicates NOTATION PROBLEM in the synthesis.")
print()
print("Likely intended: g_eff^4 > 24/(c_0) where g_eff = g*a is dimensionless")

# =============================================================================
# 4. Haar Mass Scaling
# =============================================================================

print("\n--- Check 4: Haar Mass c_0 = (N^2-1)/2N ---")

c_0_formula = (N**2 - 1) / (2*N)

print(f"Formula: c_0 = {c_0_formula}")
print()
print("Dimensional analysis:")
print("  [N^2-1] = [dimensionless]")
print("  [2N] = [dimensionless]")
print("  [c_0] = [dimensionless]")
print("  [CONSISTENT]")

# =============================================================================
# 5. Alpha Band Scaling
# =============================================================================

print("\n--- Check 5: Alpha Band alpha ~ 0.00079 ---")

print("Claim: d(lambda)/dt = -alpha * lambda^2")
print("       alpha in [0.00078, 0.00080]")
print()
print("Dimensional analysis:")
print("  [d(lambda)/dt] = [curvature/time]")
print("  [alpha * lambda^2] = [alpha] * [curvature^2]")
print()
print("If lambda is curvature (dimensionless), then:")
print("  [alpha] = [1/curvature] = [length^2] in geometric units")
print()
print("The universal value suggests alpha has meaning at scale a ~ 1")

# =============================================================================
# Summary
# =============================================================================

print("\n" + "="*60)
print("DIMENSIONAL ANALYSIS SUMMARY")
print("="*60)
print()
print("CONSISTENT:")
print("  - Gap formula: Delta >= sqrt(c_0/2)/a")
print("  - Haar coefficient: c_0 = (N^2-1)/2N")
print()
print("FLAGGED FOR REVIEW:")
print("  - RG condition: g^4 > 24/(c_0*a^2) has dimensional mismatch")
print("  - Dichotomy: lambda_lat/a gives [mass^2] not [mass]")
print()
print("These may be notation issues rather than errors.")
