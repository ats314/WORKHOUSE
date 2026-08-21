import itertools
from collections import Counter
def plq(x,y,z,o):
    if o==0: return frozenset({(x,y,z,'x'),(x,y+1,z,'x'),(x,y,z,'y'),(x+1,y,z,'y')})
    if o==1: return frozenset({(x,y,z,'x'),(x,y,z+1,'x'),(x,y,z,'z'),(x+1,y,z,'z')})
    return frozenset({(x,y,z,'y'),(x,y,z+1,'y'),(x,y,z,'z'),(x,y+1,z,'z')})
def bnd(S):
    c={}
    for p in S:
        for l in plq(*p): c[l]=c.get(l,0)^1
    return frozenset(l for l,v in c.items() if v)
# (A) unit cube faces close?
cube=[(0,0,0,0),(0,0,1,0),(0,0,0,1),(0,1,0,1),(0,0,0,2),(1,0,0,2)]
print("(A) unit cube (6 faces) is a closed surface (boundary empty):", len(bnd(cube))==0)
# (B) minimal closed surface < 6 ? search a tight local set {0,1}^3 x 3 orient = 24 plaquettes
P=[(x,y,z,o) for x in (0,1) for y in (0,1) for z in (0,1) for o in range(3)]
print("(B) local plaquettes:",len(P))
small=None
for k in range(1,6):
    if any(len(bnd(S))==0 for S in itertools.combinations(P,k)):
        small=k; break
print("    smallest closed surface with <=5 plaquettes:", small, "(None => minimal is 6)")
# (C) onset
print("(C) => one-plaquette hopping needs >=4 plaquette ops  =>  first dispersion at O(y^4).")
# (D) order-4 single-plaquette hops = cube completions: faces of cubes containing source p0
SRC=(0,0,0,0)
# the two cubes having the xy-plaquette at origin as a face: cube at z=-1 and z=0
def cube_faces(cx,cy,cz):
    return [(cx,cy,cz,0),(cx,cy,cz+1,0),(cx,cy,cz,1),(cx,cy+1,cz,1),(cx,cy,cz,2),(cx+1,cy,cz,2)]
cubes=[(0,0,0),(0,0,-1)]   # both contain the z=0 xy plaquette at origin
hop=Counter(); disp=set()
for c in cubes:
    for f in cube_faces(*c):
        if f!=SRC:
            r=(f[0]-SRC[0],f[1]-SRC[1],f[2]-SRC[2]); disp.add((r,f[3]))
            hop[(sum(abs(x) for x in r),max(abs(x) for x in r))]+=1
print("(D) order-4 single-plaquette cube-completion hops:",len(disp),"->",dict(sorted(hop.items())))
# kernel support shells for comparison
import gzip,json
K=json.load(gzip.open('DATA_Y4_full_real_space_h4_kernel.json.gz'))['kernel']
ks=Counter((sum(abs(c) for c in r['displacement']),max(abs(c) for c in r['displacement'])) for r in K)
print("    kernel (cube-STATE to cube-STATE) support shells:",dict(sorted(ks.items())))
print("    [single-plaquette completion is the seed; the 1+- basis is the 6-face cube state,")
print("     so the kernel's support is the cube-to-cube generalization, reaching Linf=2.]")
