"""Finite exact controls of the explicit source-domain counterexample."""
import os
os.environ['SYMPY_GROUND_TYPES']='python'
import sympy as s
import json
from pathlib import Path
g,r=s.symbols('g r',positive=True)
theta=2*s.sqrt(2);k=s.Rational(3,2);beta=1/(8*s.sqrt(2))
checks=[]
def check(name,value):
    value=s.simplify(value)
    assert value==0,(name,value)
    checks.append({'name':name,'passed':True})
check('actual scaled source electric weight',16/g**2*(1-(1-g*g*r/4)**2)-r*(8-g*g*r))
check('Gaussian exponential mean',(1-theta*beta)**(-k)-(s.Rational(4,3))**k)
energy=8*beta**2*k*theta*(1-2*theta*beta)**(-k-1)
check('Gaussian exponential source energy',energy-s.Rational(3,2))
check('normalized counterexample source energy',s.Rational(2,3)*energy-1)
check('strict Gaussian L2 exponential decay',2*beta-1/theta+1/(4*s.sqrt(2)))
check('strict compact energy exponential growth',2*beta+1/(3*s.sqrt(2))-1/theta-1/(12*s.sqrt(2)))
result={'description':'Exact normalization and exponent controls for a Gaussian-energy source outside the exact compact transported form domain',
        'count':len(checks),'all_passed':True,'checks':checks}
Path(__file__).with_name('source_domain_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'count':len(checks),'all_passed':True}))
