"""Exact first Rayleigh coefficients; no asymptotic remainder is certified."""

import sympy as sp

x=sp.Symbol("x",real=True)
constants=[]
for level in (1,3):
    polynomial=sp.hermite(level,x)
    mass=sp.integrate(polynomial**2*sp.exp(-x*x),(x,0,sp.oo))
    fourth=sp.simplify(sp.integrate(x**4*polynomial**2*sp.exp(-x*x),(x,0,sp.oo))/mass)
    constant=-sp.Rational(1,4)-fourth/48
    constants.append(constant)
    print(f"odd oscillator index {level}: fourth moment {fourth}; constant correction {constant}")
assert constants==[-sp.Rational(21,64),-sp.Rational(41,64)]
assert constants[1]-constants[0]==-sp.Rational(5,16)
