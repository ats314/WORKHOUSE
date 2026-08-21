#!/usr/bin/env python3
"""
MASTER document v2.0 regression certificate (one-plaquette program).

Re-derives, in exact arithmetic, every internally checkable constant of the
MASTER document (June 11, 2026, evening): the thirteen Section-3 consistency
checks, the full Section-8 strong-coupling web (Theorem 6.2 correction, band
structure, O(y^3) constants), plus two NEW gates not in the document:
  (i)  c3+(N) closed form specializes at N=3 to Theorem 2.1's c3 coefficient;
  (ii) first-principles derivation of the C-even band curvature 4/3 from the
       3x3 plaquette-orientation Bloch matrix (hence 22/459 corrected,
       481/459 manuscript-as-written).
Self-contained; sympy + fractions only; hard gates; exit 1 on any failure.
"""
import sys
from fractions import Fraction as F
import sympy as sp

PASS=[]; FAIL=[]
def gate(name, ok):
    (PASS if ok else FAIL).append(name)
    print(("PASS  " if ok else "FAIL  ") + name)

N = sp.symbols('N', positive=True)
sqrt = sp.sqrt; Rat = sp.Rational

# ---------------- A. Weak-coupling closed forms at fixed N ----------------
c0p = -(2*N**2-3)/(16*N)
c0m = -3*(N**2-3)/(16*N)
c1p = -sqrt(2)*(6*N**4-24*N**2+41)/(1024*N**Rat(3,2))
c1m = -sqrt(2)*(14*N**4-97*N**2+290)/(1536*N**Rat(3,2))
c2p = -(60*N**6-401*N**4+1522*N**2-2297)/(49152*N**2)
c2m = -(95*N**6-981*N**4+5853*N**2-15335)/(49152*N**2)
c3p = -sqrt(2*N)*(2970*N**8-27878*N**6+166512*N**4-546024*N**2+734405)/(2**21*3**2*N**3)

gate("A1  c0+(3) = -5/16",            sp.simplify(c0p.subs(N,3) + Rat(5,16))==0)
gate("A2  c0-(3) = -3/8",             sp.simplify(c0m.subs(N,3) + Rat(3,8))==0)
gate("A3  c1+(3) = -311*sqrt(6)/9216",  sp.simplify(c1p.subs(N,3) + 311*sqrt(6)/9216)==0)
gate("A4  c1-(3) = -551*sqrt(6)/13824", sp.simplify(c1m.subs(N,3) + 551*sqrt(6)/13824)==0)
gate("A5  c2+(3) = -5665/110592",     sp.simplify(c2p.subs(N,3) + Rat(5665,110592))==0)
gate("A6  c2-(3) = -53/864",          sp.simplify(c2m.subs(N,3) + Rat(53,864))==0)
gate("A7* c3+(3) = -8470769*sqrt(6)/509607936  [NEW CHECK 3.1']",
     sp.simplify(c3p.subs(N,3) + 8470769*sqrt(6)/509607936)==0)
gate("A8a c1+(4) = sqrt(8)*(-1193/16384)  [3.10]",
     sp.simplify(c1p.subs(N,4) - sqrt(8)*Rat(-1193,16384))==0)
gate("A8b c1+(6) = sqrt(12)*(-6953/36864) [3.11]",
     sp.simplify(c1p.subs(N,6) - sqrt(12)*Rat(-6953,36864))==0)
gate("A9  c0+(4) = -29/64",           sp.simplify(c0p.subs(N,4) + Rat(29,64))==0)
gate("A10 N=7 targets: q_even=-13271/50176; foil gap in c1 units sqrt(14)*144/50176 ~ 1.07e-2",
     sp.simplify(c1p.subs(N,7) - sqrt(14)*Rat(-13271,50176))==0
     and abs(float(sqrt(14)*Rat(144,50176)) - 1.07e-2) < 5e-4)

R0 = 3*(N**2-4)/(N*(N**2+1)*(N**2+3))
slope = N**2*(N**2-9)/(8*(N**2+1))
gamma_N = (2*N**2-3)/(N*(N**2+1))
gate("A11 R0(3)=1/24; slope(3)=0; slope(4)=14/17; gamma3=1/2; alpha3=3",
     R0.subs(N,3)==Rat(1,24) and slope.subs(N,3)==0 and slope.subs(N,4)==Rat(14,17)
     and gamma_N.subs(N,3)==Rat(1,2) and Rat(3**2-3,2)==3)

# ---------------- B. Bridge towers m+- = 4*Delta+-(3y/2) ----------------
bp = [F(2,3), F(-1,6), F(13,180), F(101,2700)]      # Delta+ tower b0..b3
bm = [F(2,3), F( 1,6), F( 1,18),  F(7,432)]          # Delta- tower
def bridge(b, k):  # y^k coefficient of 4*Delta(3y/2)
    return 4*b[k]*F(3,2)**k
gate("B1  m+ tower: 8/3, -1, 13/20, 101/200",
     [bridge(bp,k) for k in range(4)] == [F(8,3), F(-1), F(13,20), F(101,200)])
gate("B2  m- tower: 8/3, +1, 1/2, 7/32   (and 9*c2- = 1/2)",
     [bridge(bm,k) for k in range(4)] == [F(8,3), F(1), F(1,2), F(7,32)]
     and 9*F(1,18) == F(1,2))
gate("B3  domino vacuum: 2*(-3/4)=-3/2 ; 2*(-9/32)=-9/16",
     2*F(-3,4)==F(-3,2) and 2*F(-9,32)==F(-9,16))

# ---------------- C. Leakage arithmetic, Thm 6.2 correction, Sec.7 ----------------
split = [F(-1,12), F(-16,51), F(-1,6), F(-2,9)]
gate("C1  channel split sums to -481/612", sum(split)==F(-481,612))
gate("C2  N_mixed+N_like=-481/612 ; |t-|=5/612",
     F(-27,68)+F(-7,18)==F(-481,612) and abs(F(-27,68)-F(-7,18)) == F(5,612)
     and abs(-243+238)==5)
diag_per = F(-481,612)+F(3,4)
gate("C3  diag leakage 12*(-11/306)=-22/51 ; coeff 7/102 ; interval [-3/102,17/102]",
     diag_per==F(-11,306) and 12*diag_per==F(-22,51)
     and F(1,2)+12*diag_per==F(7,102)
     and F(7,102)-12*F(5,612)==F(-3,102) and F(7,102)+12*F(5,612)==F(17,102))
gate("C4  manuscript-as-written: per-neighbor -503/612 ; 13/20-503/51 = -9397/1020",
     F(-481,612)+F(3,4)+F(-481,612)==F(-503,612)
     and F(13,20)+12*F(-503,612)==F(-9397,1020))
t_plus = F(-481,612)+F(3,4)
gate("C5  corrected t+ = -11/306 ; per-neighbor -11/153 ; k=0 coeff -217/1020",
     t_plus==F(-11,306) and 2*t_plus==F(-11,153)
     and F(13,20)+24*t_plus==F(-217,1020))
gate("C6  vacuum route (sqrt2)(sqrt2)(3/8)=3/4 ; distant cancel 2/(8/3-16/3)=-3/4",
     F(2)*F(3,8)==F(3,4) and F(2)/(F(8,3)-F(16,3))==F(-3,4))
gate("C7  Sec.7 C-even adjudication: 1879/3060 -+ 110/3060 = {1769/3060, 13/20}",
     F(1879,3060)-F(110,3060)==F(1769,3060) and F(1879,3060)+F(110,3060)==F(13,20)
     and F(110,3060)==F(11,306)
     and F(13,20)+1*t_plus==F(1879,3060))   # one-neighbor diag = within + (self+vac)
gate("C8  Sec.7 C-odd: mean{31/68,17/36}=71/153=1/2+1*(-11/306) ; halfdiff=5/612",
     (F(31,68)+F(17,36))/2==F(71,153) and F(1,2)+diag_per==F(71,153)
     and (F(17,36)-F(31,68))/2==F(5,612))

# ---------------- D. Band structure (Sec. 8.1/8.2) ----------------
codd = lambda mu: F(7,102) + F(5,612)*mu
gate("D1  C-odd band: mu=-4 -> 11/306 (flat) ; mu=8 -> 41/306",
     codd(-4)==F(11,306) and codd(8)==F(41,306))
ceven = lambda lam, t: F(13,20) + 12*(F(-481,612)+F(3,4)) + t*lam
gate("D2  C-even: lam=12 -> -217/1020 ; lam=-4 -> 1109/3060 ; lam=0 -> 223/1020 (t-indep) ; old t -> -9397/1020 ; bw 16|t+|=88/153",
     ceven(12,t_plus)==F(-217,1020) and ceven(-4,t_plus)==F(1109,3060)
     and ceven(0,t_plus)==F(223,1020) and ceven(0,F(-481,612))==F(223,1020)
     and ceven(12,F(-481,612))==F(-9397,1020) and 16*abs(t_plus)==F(88,153))

# Bloch matrix first-principles curvature: orientations (xy),(yz),(zx)
kx,ky,kz,e = sp.symbols('kx ky kz e', real=True)
K = {0:(kx,ky),1:(ky,kz),2:(kz,kx)}            # in-plane directions per orientation
allk = {kx,ky,kz}
S = sp.zeros(3,3)
for i in range(3):
    a,b = K[i]
    S[i,i] = 2*sp.cos(a)+2*sp.cos(b)
for i in range(3):
    for j in range(i+1,3):
        shared = (set(K[i]) & set(K[j])).pop()
        t1,t2  = tuple((set(K[i])|set(K[j])) - {shared})
        S[i,j] = S[j,i] = 4*sp.cos(t1/2)*sp.cos(t2/2)
ok_dirs=[]
lamv = sp.symbols('lamv')
for (ux,uy,uz) in [(1,0,0),(1,1,1),(2,1,0)]:
    Se = S.subs({kx:e*ux, ky:e*uy, kz:e*uz})
    P  = (Se - lamv*sp.eye(3)).det()
    P2   = sp.simplify(sp.series(P.subs(lamv,12), e, 0, 3).removeO().coeff(e,2))
    Plam = P.diff(lamv).subs({lamv:12, e:0})
    c2coef = sp.simplify(-P2/Plam)          # lam_S(e) = 12 + c2coef*e^2 + O(e^4)
    ok_dirs.append(sp.simplify(c2coef + Rat(4,3)*(ux*ux+uy*uy+uz*uz))==0)
gate("D3* Bloch A1 branch: 12 - lam_S(k) = (4/3)|k|^2 +O(k^4) [3 directions] -> curvature (11/306)(4/3)=22/459 ; old (481/612)(4/3)=481/459  [NEW]",
     all(ok_dirs) and F(11,306)*F(4,3)==F(22,459) and F(481,612)*F(4,3)==F(481,459))
gate("D3b Bloch lam_S(0) eigs {12,0,0} ; lam_S(pi,pi,pi) = -4 triple",
     sorted(S.subs({kx:0,ky:0,kz:0}).eigenvals().items(),key=lambda x:-x[0])==[(12,1),(0,2)]
     and S.subs({kx:sp.pi,ky:sp.pi,kz:sp.pi}).eigenvals()=={-4:3})

# ---------------- E. O(y^3) web (Sec. 8.4) ----------------
b3   = F(1975,124848); T3e = F(-6335,249696)
D3o  = F(-24541,62424); D3e = F(-517313,6242400); e3vac = F(-9,16)
leak3o = (D3o - e3vac) - F(7,32)
leak3e = (D3e - e3vac) - F(101,200)
d3     = F(7,32) + 12*leak3o - 4*b3
d3top  = F(7,32) + 12*leak3o + 8*b3
gate("E1  leak3_odd  = -12331/249696", leak3o==F(-12331,249696))
gate("E2  leak3_even = -6335/249696",  leak3e==F(-6335,249696))
gate("E3  identity leak3_even == T3_even  (and n=2: -481/612+3/4 == t+)",
     leak3e==T3e and F(-481,612)+F(3,4)==t_plus)
gate("E4  d3 = 7/32+12*leak3o-4*b3 = -109151/249696", d3==F(-109151,249696))
gate("E5  d3_top = 7/32+12*leak3o+8*b3 = -61751/249696", d3top==F(-61751,249696))
gate("E6  C-even cubic k=0: 101/200+24*T3e = -54049/520200",
     F(101,200)+24*T3e==F(-54049,520200))
gate("E7  C-even cubic lam=-4: 101/200+8*T3e = 471353/1560600",
     F(101,200)+8*T3e==F(471353,1560600))
gate("E8  2nd-order contraction gate: 1/2+12*(-11/306)-4*(5/612) = 11/306",
     F(1,2)+12*F(-11,306)-4*F(5,612)==F(11,306))
gate("E9  d3 ~ -0.437135", abs(float(d3) + 0.437135) < 1e-6)

# ---------------- F. Convention bridges ----------------
p2,p3 = sp.symbols('p2 p3')
H2_206 = sqrt(Rat(3,2))*(p2**3/4 + p3**2/3)/1440        # sqrt(N/2)P6/1440 at N=3, rank-2 Newton
H2_GR1 = sqrt(6)*p2**3/11520 + sqrt(6)*p3**2/8640
gate("F1  H2 conventions agree (206 engine == GR1 cell 12 at N=3)",
     sp.simplify(H2_206 - H2_GR1)==0)
gate("F2  H1: -p4/48 == -p2^2/96 at rank two (p4=p2^2/2)",
     sp.simplify(-(p2**2/2)/48 + p2**2/96)==0)
gate("F3  c2_certificate.py convention sqrt(2N)P6/2880 == sqrt(N/2)P6/1440",
     sp.simplify(sqrt(2*N)/2880 - sqrt(N/Rat(2))/1440)==0)
w0 = sqrt(sp.Symbol('beta',positive=True)/(2*N))
gate("F4  2*w0=sqrt(2b/N), 3*w0=sqrt(9b/2N); at N=3: sqrt(2b/3), sqrt(3b/2)",
     sp.simplify((2*w0)**2 - 2*sp.Symbol('beta',positive=True)/N)==0
     and sp.simplify((3*w0)**2 - 9*sp.Symbol('beta',positive=True)/(2*N))==0)

print()
print(f"TOTAL: {len(PASS)} passed, {len(FAIL)} failed of {len(PASS)+len(FAIL)} gates")
if FAIL:
    print("FAILED:", *FAIL, sep="\n  ")
sys.exit(1 if FAIL else 0)
