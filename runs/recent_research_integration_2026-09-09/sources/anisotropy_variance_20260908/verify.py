"""Independent exact record identity and numerical falsification probes.
Run with WORKHOUSE's Python; no source/ledger mutations.
"""
import sys
import json
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT = Path(r'C:\WORKHOUSE\ALL THEORY\WORKHOUSE')
sys.path.insert(0, str(ROOT / 'src'))
from workhouse import kernel_orbits as KO
from workhouse.invariants.gamma_isolation import _forms, _q_a_records
import sympy as sp
import mpmath as mp

out = {}
form = _forms()['assembled']
C = form['C']
s = 2*form['nu~'] + 16*form['u'] + 4*form['pi~'] + form['sigma~']
H = KO.combine((1, KO.hodge_records(form)), (-s, KO.identity()))
q = KO.bloch_matrix(_q_a_records())[KO.PLANES[0]][KO.PLANES[0]]
mu = KO.bloch(H.items())
second = KO.bloch(KO.compose(H, H).items())
lhs = KO._add(KO._mul(q, second), KO._mul(mu, mu), -1)
a = []
for i in range(3):
    ai = {(0,0,0): F(2)}
    for sign in (-1,1):
        e = [0,0,0]; e[i] = sign
        ai[tuple(e)] = F(-1)
    a.append(ai)
target = {}
for i in range(3):
    for j in range(i+1,3):
        diff = KO._add(a[i], a[j], -1)
        term = KO._mul(KO._mul(a[i], a[j]), KO._mul(diff,diff))
        target = KO._add(target, term, 4*C*C)
clean = lambda d: {k:v for k,v in d.items() if v}
assert clean(lhs) == clean(target)
out['exact_full_kernel_residual_identity'] = True
out['laurent_terms'] = len(clean(lhs))
out['C'] = str(C)
out['sixth_order_prefactor_minus_4C_squared_over_t3'] = str(-4*C*C/F(5,612))
x,y,z = sp.symbols('x y z', nonnegative=True)
variance = x**3+y**3+z**3-(x*x+y*y+z*z)**2
sos = x*y*(x-y)**2+x*z*(x-z)**2+y*z*(y-z)**2
assert sp.expand((variance-sos).subs(z,1-x-y)) == 0
out['simplex_variance_SOS_identity'] = True
e2 = x*y+x*z+y*z
e3 = x*y*z
assert sp.expand((sos-e2-3*e3+4*e2**2).subs(z,1-x-y)) == 0
out['sixth_order_shape_ratio_1_3_minus4'] = True
# Nodes and a strictly mixing rational holdout.
for point in [(1,0,0),(F(1,2),F(1,2),0),(F(1,3),)*3]:
    assert sos.subs(dict(zip((x,y,z),point))) == 0
assert sos.subs({x:F(1,6),y:F(1,3),z:F(1,2)}) == F(5,324)
out['nodal_and_generic_exact_checks'] = True

mp.mp.dps = 45
mf = lambda r: mp.mpf(r.numerator)/r.denominator
SS = KO.bloch_matrix(H)
LL = KO.bloch_matrix(KO.down_laplacian())
psi = KO.carrier()
def ev(poly,k):
    return sum(mf(c)*mp.expj(sum(e[i]*k[i] for i in range(3))) for e,c in poly.items())
def mat(records,k):
    return mp.matrix([[ev(records[o][i],k) for i in KO.PLANES] for o in KO.PLANES])
points = list(product([mp.mpf('0'),mp.mpf('.4'),mp.mpf('1.2'),mp.pi],repeat=3))[1:]
points += [(mp.mpf('1e-9'),mp.mpf('2e-9'),mp.mpf('3e-9'))]
max_identity_error = mp.mpf(0)
max_overlap_ratio = mp.mpf(0)
max_energy_ratio = mp.mpf(0)
for k in points:
    av = [4*mp.sin(t/2)**2 for t in k]; qv = sum(av)
    xx = [v/qv for v in av]
    V = sum(xx[i]*xx[j]*(xx[i]-xx[j])**2 for i in range(3) for j in range(i+1,3))
    p = mp.matrix([ev(psi[o],k) for o in KO.PLANES])/mp.sqrt(qv)
    h = mat(SS,k); lam = mat(LL,k)
    mean = (p.H*h*p)[0].real
    residual = h*p-mean*p
    actual = (residual.H*residual)[0].real
    expect = 4*mf(C)**2*qv*qv*V
    max_identity_error = max(max_identity_error, abs(actual-expect)/qv**2)
    for u in map(mp.mpf,['.05','.1','.19']):
        t3=mp.mpf(5)/612; ci=mp.mpf(5)/48
        M=t3*u*u*lam+u**4*h
        E,U=mp.eigh(M)
        deficit=max(mp.mpf(0),1-abs((p.H*U[:,0])[0])**2)
        delta=t3-2*ci*u*u
        overlap_bound=4*mf(C)**2*u**4*V/delta**2
        energy_bound=4*mf(C)**2*u**6*qv*V/delta
        error=u**4*mean-E[0]
        assert deficit <= overlap_bound+mp.mpf('1e-30')
        assert -mp.mpf('1e-30') <= error <= energy_bound+mp.mpf('1e-30')
        if V>mp.mpf('1e-25'):
            max_overlap_ratio=max(max_overlap_ratio,deficit/overlap_bound)
            max_energy_ratio=max(max_energy_ratio,error/energy_bound)
assert max_identity_error < mp.mpf('1e-30')
out['numerical']={'precision_digits':45,'momenta':len(points),'couplings':[.05,.1,.19],
 'max_scaled_residual_error':str(max_identity_error),
 'worst_overlap_bound_fraction':str(max_overlap_ratio),
 'worst_energy_bound_fraction':str(max_energy_ratio)}
# Distinguish the induced term from a genuine sixth-order Hamiltonian.
k=tuple(map(mp.mpf,['.4','.8','1.2']))
p=mp.matrix([ev(psi[o],k) for o in KO.PLANES]); qv=(p.H*p)[0].real; p/=mp.sqrt(qv)
h=mat(SS,k); lam=mat(LL,k); mean=(p.H*h*p)[0].real
r=h*p-mean*p; coefficient=-(r.H*r)[0].real/((mp.mpf(5)/612)*qv)
ratios=[]
for u in map(mp.mpf,['.002','.001','.0005']):
    E,_=mp.eigh(mp.mpf(5)/612*u*u*lam+u**4*h)
    ratios.append((E[0]-u**4*mean)/(u**6*coefficient))
assert abs(ratios[-1]-1)<abs(ratios[0]-1)<mp.mpf('.001')
out['induced_sixth_order_ratios']=[str(v) for v in ratios]
out['all_passed']=True
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
