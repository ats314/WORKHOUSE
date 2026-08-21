#!/usr/bin/env python3
"""Independent cross-check of the SU3_Y6_M6_EXACT_INTERNAL_V1 fold layer.
Confirms the release's folded-weight formula against the project's sigma5-certified
des-Cloizeaux module, and reproduces the dominant-anchor contribution exactly.
Does NOT re-do the full color/topology contraction (the outstanding 2nd implementation)."""
from fractions import Fraction as F
import math, importlib.util as iu, random
def h_complete(vals,z):
    dp=[F(0)]*(z+1); dp[0]=F(1)
    for x in vals:
        for k in range(1,z+1): dp[k]+=x*dp[k-1]
    return dp[z]
def folded_release(ds):           # release formula (y6_folded_weight_catalog.folded)
    nz=[d for d in ds if d]; z=len(ds)-len(nz)
    if not nz: return F(0)
    return F((-1)**z,z+1)*h_complete([F(1)/d for d in nz],z)/math.prod(nz)
spec=iu.spec_from_file_location('fp','../su3_o5_consolidated_y6/ENGINE_Y6_folded_descloizeaux_preflight.py')
fp=iu.module_from_spec(spec); spec.loader.exec_module(fp); mine=fp.folded_coefficient
# (1) two independent folds agree on random 5-denominator vectors
rng=random.Random(7); ok=True
for _ in range(500):
    dv=[F(rng.randint(1,9),rng.randint(1,9))*rng.choice([1,-1]) for _ in range(5)]
    if folded_release(dv)!=mine(dv): ok=False; break
assert ok, "fold implementations disagree"
# (2) dominant anchor: E6=(32,16,32,16,32), d=(16-E)/6
ds=[F(16-e,6) for e in (32,16,32,16,32)]
cf=folded_release(ds); assert cf==F(-243,16384) and mine(ds)==F(-243,16384)
contrib=65208*1*cf; assert contrib==F(-1980693,2048) and 8*contrib==F(-1980693,256)
print("PASS independent fold cross-check (500 vectors) + dominant anchor -243/16384, 8-block -1980693/256")
print("m6 (release) = -156998370765216917515896262601525405897211506214753116643443873"
      "/4880681791275629050759264798095652027950878794719744000000  (PROVISIONAL, exact-internal)")
