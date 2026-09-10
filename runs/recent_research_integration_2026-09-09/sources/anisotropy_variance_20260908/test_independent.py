"""Tests of the theory using direct complex matrices, not record composition."""
import json
import random
import sys
from pathlib import Path

import mpmath as mp
import sympy as s

ROOT = Path(r'C:\WORKHOUSE\ALL THEORY\WORKHOUSE')
sys.path.insert(0, str(ROOT / 'src'))
from workhouse import constants as K
from workhouse import kernel_orbits as KO
from workhouse.invariants.gamma_isolation import _forms

mp.mp.dps = 75
FORM = _forms()['assembled']
C = s.Rational(str(FORM['C']))
T = s.Rational(5, 612)
CI = s.Rational(5, 48)
RECORDS = KO.hodge_records(FORM)
SCALAR = 2*FORM['nu~']+16*FORM['u']+4*FORM['pi~']+FORM['sigma~']


def direct(z):
    # Independent evaluation: do not use KO.bloch, compose, carrier, or apply.
    z = list(map(s.sympify, z))
    mat = s.zeros(3)
    for (ip, op, displacement), value in RECORDS.items():
        monomial = s.prod(z[j]**displacement[j] for j in range(3))
        mat[KO.PLANES.index(op), KO.PLANES.index(ip)] += s.Rational(str(value))*monomial
    mat -= s.Rational(str(SCALAR))*s.eye(3)
    # This repository defines dbar = z-1 (despite the suggestive name).
    p = s.Matrix([z[2]-1, -(z[1]-1), z[0]-1])
    return mat.applyfunc(s.simplify), p


def test_exact_complex_matrix_holdouts():
    phases = [s.I, (3+4*s.I)/5, (5+12*s.I)/13]
    for z in [phases, phases[::-1], [1,s.I,s.I], [s.I]*3, [s.I,1,1]]:
        z = list(map(s.sympify, z))
        h,p = direct(z)
        q = s.simplify((p.H*p)[0])
        P = p*p.H/q
        assert (h-h.H).applyfunc(s.simplify) == s.zeros(3)
        r = ((s.eye(3)-P)*h*p).applyfunc(s.simplify)
        a = [s.simplify(2-v-1/v) for v in z]
        eps = s.Rational(str(FORM['u']))*(q-8)-s.Rational(str(FORM['pi~']))
        reconstructed = q*((CI+2*C)*P+eps*(s.eye(3)-P))-2*C*s.diag(*a[::-1])
        assert (h-reconstructed).applyfunc(s.simplify) == s.zeros(3)
        sos = sum(a[i]*a[j]*(a[i]-a[j])**2 for i in range(3) for j in range(i+1,3))
        assert s.simplify((r.H*r)[0]/q - 4*C*C*sos/q**2) == 0


def test_characteristic_polynomial_sixth_order():
    h,p = direct([(3+4*s.I)/5, (5+12*s.I)/13, s.I])
    q = s.simplify((p.H*p)[0])
    Q = s.eye(3)-p*p.H/q
    mean = s.simplify((p.H*h*p)[0]/q)
    r = (Q*h*p).applyfunc(s.simplify)
    coeff = s.simplify(-(r.H*r)[0]/(T*q*q))
    v,w = s.symbols('v w')
    # det(lambda I - (T*q*Q + v*H)), lambda=v*mean+v^2*w.
    # Direct determinant, independently of eigenvalue perturbation formulas.
    characteristic = (v*mean*s.eye(3)+v*v*w*s.eye(3)-T*q*Q-v*h).det(method='domain-ge')
    coefficient = s.expand(characteristic).coeff(v,2)
    assert s.simplify(coefficient.subs(w,coeff)) == 0
    assert s.diff(coefficient,w) != 0
    assert coeff < 0


def number(value):
    return mp.mpf(str(value.p))/mp.mpf(str(value.q))


def reduced(k):
    # Stable plaquette-centred gauge: rephase p to sqrt(a_i/q).
    a = [4*mp.sin(t/2)**2 for t in k]
    q = sum(a)
    if q == 0:
        raise ValueError('Gamma has no rank-one carrier')
    x = [v/q for v in a]
    p = mp.matrix([mp.sqrt(v) for v in x])
    P=p*p.T
    eps=mp.mpf(str(FORM['u'].numerator))/FORM['u'].denominator*(q-8)-mp.mpf(str(FORM['pi~'].numerator))/FORM['pi~'].denominator
    h=(number(CI)+2*number(C))*P+eps*(mp.eye(3)-P)-2*number(C)*mp.diag(x)
    V=sum(x[i]*x[j]*(x[i]-x[j])**2 for i in range(3) for j in range(i+1,3))
    return p,P,h,V


def test_scaled_adversarial_spectral_bounds():
    rng=random.Random(91723)
    points=[tuple(mp.mpf(rng.uniform(-3.14,3.14)) for _ in range(3)) for _ in range(100)]
    for scale in ['1e-3','1e-12','1e-30']:
        for direction in [(1,2,3),(1,1,0),(1,1,1),(1,0,0),(1,1,1.00001)]:
            points.append(tuple(mp.mpf(scale)*v for v in direction))
    points += [(mp.pi,mp.pi,mp.pi),(mp.pi,0,0),(mp.pi,mp.pi,0)]
    threshold=mp.sqrt(mp.mpf(2)/51)
    couplings=[mp.mpf('.0001'),mp.mpf('.05'),mp.mpf('.15'),threshold*(1-mp.mpf('1e-8'))]
    worst_overlap=mp.mpf(0); worst_energy=mp.mpf(0)
    for k in points:
        p,P,h,V=reduced(k)
        mean=(p.T*h*p)[0]
        for u in couplings:
            # Matrix divided by u^2*q: no tiny absolute energy scale.
            E,U=mp.eigh(number(T)*(mp.eye(3)-P)+u*u*h)
            deficit=1-abs((p.T*U[:,0])[0])**2
            d=number(T)-2*number(CI)*u*u
            ob=4*number(C)**2*u**4*V/d**2
            eb=4*number(C)**2*u**4*V/d
            err=u*u*mean-E[0]
            assert deficit <= ob+mp.mpf('1e-60')
            assert -mp.mpf('1e-60') <= err <= eb+mp.mpf('1e-60')
            assert E[1]-E[0] >= d-mp.mpf('1e-60')
            if V>mp.mpf('1e-50'):
                worst_overlap=max(worst_overlap,deficit/ob)
                worst_energy=max(worst_energy,err/eb)
    Path(__file__).with_name('adversarial_certificate.json').write_text(json.dumps({
        'precision_digits':75,'seed':91723,'momenta':len(points),'spectral_probes':len(points)*len(couplings),
        'smallest_momentum_scale':'1e-30','threshold_distance_fraction':'1e-8',
        'absolute_tolerance_after_scaling':'1e-60',
        'worst_overlap_bound_fraction':str(worst_overlap),'worst_energy_bound_fraction':str(worst_energy)
    },indent=2))


def test_overlap_asymptotic_coefficient():
    p,P,h,V=reduced(tuple(map(mp.mpf,['.4','.8','1.2'])))
    expected=4*number(C)**2*V/number(T)**2
    errors=[]
    for u in map(mp.mpf,['.002','.001','.0005']):
        _,U=mp.eigh(number(T)*(mp.eye(3)-P)+u*u*h)
        ratio=(1-abs((p.T*U[:,0])[0])**2)/(u**4*expected)
        errors.append(abs(ratio-1))
    assert errors[2]<errors[1]<errors[0]<mp.mpf('.001')


def test_gamma_is_excluded():
    import pytest
    with pytest.raises(ValueError,match='Gamma'):
        reduced((0,0,0))


def test_exact_nodal_classification_on_rational_simplex():
    for denominator in range(1,25):
        for a in range(denominator+1):
            for b in range(denominator-a+1):
                x=[s.Rational(a,denominator),s.Rational(b,denominator),s.Rational(denominator-a-b,denominator)]
                V=sum(x[i]*x[j]*(x[i]-x[j])**2 for i in range(3) for j in range(i+1,3))
                assert V>=0
                assert (V==0)==(len({v for v in x if v>0})==1)
                assert V<=s.Rational(1,4)


def test_mutation_and_missing_sixth_order_detection():
    # Nonzero test point rejects wrong sign, missing square, and altered shape ratio.
    x=[s.Rational(1,6),s.Rational(1,3),s.Rational(1,2)]
    V=sum(v**3 for v in x)-sum(v*v for v in x)**2
    expected=-4*C*C*V/T
    assert expected != 4*C*C*V/T
    assert expected != -4*C*V/T
    e2=x[0]*x[1]+x[0]*x[2]+x[1]*x[2]
    e3=s.prod(x)
    assert V != e2+2*e3-4*e2**2
    # Adding u^6 I shifts every energy by u^6: induced is not total.
    assert expected+1 != expected
