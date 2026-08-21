import math, mpmath as mp
from fractions import Fraction as F
mp.mp.dps=40
print("=== TIER 2: leading SC formula + large-N scaling ===")
sc=lambda N: 2.0*math.sqrt((N*N-1)/N)
print(f"  sc(3)=2*sqrt(8/3)={sc(3):.4f}  (doc claims 3.266; my sc_extrap gave 3.266)  match={abs(sc(3)-3.266)<1e-3}")
# also cross-check (8/3)/sqrt(2/3):
print(f"  (8/3)/sqrt(2/3)={ (8/3)/math.sqrt(2/3):.4f}  == sc(3)? {abs((8/3)/math.sqrt(2/3)-sc(3))<1e-9}")
print("  large-N: sc(N)/(2*sqrt(N)) ->", [round(sc(N)/(2*math.sqrt(N)),4) for N in (10,100,1000,10000)],"-> 1 (so sc~2sqrtN diverges)")
# crossing with N-indep lattice 5.76
a=(5.760/2)**2; Ncross=(a+math.sqrt(a*a+4))/2
print(f"  crossing 2*sqrt((N^2-1)/N)=5.76 at N={Ncross:.2f}  (doc says ~8.4)")

print("\n=== TIER 1a: ordering arithmetic ===")
# 1+- series VERIFIED earlier (theorem): 8/3 + y + 11/306 y^2
print("  1+- O(y) coeff = +1 : matches my verified series 8/3 + y + (11/306)y^2  -> VERIFIED")
d20=F(223,1020)+F(217,1020); print(f"  m(2++)-m(0++) y^2 coeff = 223/1020+217/1020 = {d20} = {float(d20):.4f} >0 -> 0++<2++")
d12=F(11,306)-F(223,1020); print(f"  m(1+-)-m(2++) = 2y + ({d12})y^2 ; sign of 2y makes 1+- heaviest until y~{float(2/abs(d12)):.0f}")
print("  NOTE: 0++ (-217/1020) and 2++ (+223/1020) O(y^2) coeffs are from an UNVERIFIED cert (not in my checked set).")

print("\n=== TIER 3: Borel-Pade with corrected c4(Gamma)=-2.857916 ===")
c4=F(-20721577909065127111,7250590288602460800)
af=[float(x) for x in [F(8,3),F(1),F(11,306),F(-109151,249696),c4]]
print("  coeffs:",[f'{x:.4f}' for x in af],"(grow -> divergent)")
borel=[mp.mpf(str(af[i]))/mp.factorial(i) for i in range(5)]; K0=2/3
for L,M in [(2,1),(1,1),(1,2),(1,3)]:
    p,q=mp.pade(borel,L,M)
    Bp=lambda t,p=p,q=q: sum(p[i]*t**i for i in range(len(p)))/sum(q[i]*t**i for i in range(len(q)))
    vals=[f"y={y}:{float(mp.quad(lambda t: mp.e**(-t)*Bp(y*t),[0,mp.inf]))/math.sqrt(K0):.3f}" for y in (1.5,2.0,2.5)]
    print(f"  [{L}/{M}]:", "  ".join(vals))
print("  -> stable [2/1],[1/1] bracket lattice 6.07 near y~2.3-2.5; divergent => consistency only.")
