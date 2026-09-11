"""Scratch check (not a repository check): iterate the manuscript's own (6.14)
||K_k|| <= lambda^k ||K_0|| + C_ind sum_{j<k} lambda^{k-1-j} g_j^2
with lambda = 1/9 (G19 note Theorem 3) and g_k^2 from (6.12) at leading order,
and compare with 9^{-k} (G19 note Theorem 4's claimed suppression) and with g_k^2.
"""
from fractions import Fraction
import math
L=3; lam=Fraction(1,9); C_ind=1.0; K0=1.0
b0=11*3/(48*math.pi**2)   # SU(3)
g0sq=1.0
def gsq(k): return g0sq/(1+2*b0*g0sq*k*math.log(L))
K=[K0]
for k in range(1,201):
    K.append(float(lam)*K[-1]+C_ind*gsq(k-1))
print(" k   ||K_k||(6.14)   g_k^2      ratio K_k/g_k^2   9^-k")
for k in (1,2,5,10,20,50,100,200):
    print(f"{k:3d}  {K[k]:.6e}  {gsq(k):.6e}  {K[k]/gsq(k):9.4f}   {9.0**-k:.3e}")
print("(9/8) =",9/8)
# forcing-free comparison: what Theorem 4 of the G19 note would need
print("K_k * k for k=50,100,200:", [round(K[k]*k,4) for k in (50,100,200)], "(bounded away from 0 => O(1/k), not summable)")
print("partial sums of K_k up to n:", [round(sum(K[1:n+1]),3) for n in (10,50,100,200)])
