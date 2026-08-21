#!/usr/bin/env python3
"""Find the 3-holonomy 'corner' cluster (the membrane a twisted hexagon bounds):
the hexagon Tr(g1 g2 g3) must be an EXACT H0-eigenstate at energy 4 = 6*(2/3).
Scan cross-term signs (s12,s23,s13) and word orientations to identify the geometry."""
import sys, os, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ENGINE_FLUX_cluster_pt import make_H0_cluster
from ENGINE_FLUX_su3_domino_d3 import expr_of, expr_add, expr_scale, canon_word

def hexword(e1,e2,e3):
    return canon_word(((1,e1),(2,e2),(3,e3)))   # Tr(g1^e1 g2^e2 g3^e3)

print("scanning corner cross-signs x word-orientations for H0(hex)=4*hex (exact eigenstate):")
found=[]
for s12,s23,s13 in itertools.product((+1,-1),repeat=3):
    H0=make_H0_cluster([1,2,3],[(1,2,s12),(2,3,s23),(1,3,s13)])
    for e1,e2,e3 in itertools.product((+1,-1),repeat=3):
        w=hexword(e1,e2,e3)
        Hw=H0(w)
        # is Hw == 4*w exactly (eigenstate, no leakage)?
        resid=expr_add(Hw, expr_scale(w,F(-4)))
        if resid=={}:
            found.append((s12,s23,s13,e1,e2,e3))
# also report, for the all-+ word, what eigenvalue/leakage each sign combo gives
print(f"  exact-eigenstate-at-4 combos: {len(found)}")
for f in found[:8]: print("   signs(s12,s23,s13)=",f[:3]," word orient=",f[3:])
# diagnostic: for signs (-1,-1,-1) word(+,+,+), show H0(hex)
H0=make_H0_cluster([1,2,3],[(1,2,-1),(2,3,-1),(1,3,-1)])
w=hexword(1,1,1); Hw=H0(w)
print("  sample H0(Tr g1g2g3) with all-minus cross:")
for m,c in sorted(Hw.items())[:6]: print(f"     {c}  *  {m}")
