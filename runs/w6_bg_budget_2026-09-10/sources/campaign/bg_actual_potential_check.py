"""Exact controls for actual_potential_moment.md; not a uniform score proof."""
import json
from pathlib import Path
import sympy as s

I = s.I
Id = s.eye(2)
pauli = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-I],[I,0]]),
         s.Matrix([[1,0],[0,-1]])]

def su2(a, r):
    assert s.simplify(a*a + sum(x*x for x in r)) == 1
    return a*Id + I*sum((r[j]*pauli[j] for j in range(3)), s.zeros(2))

def norm2(M):
    return s.simplify(s.trace(M.conjugate().T*M))

def verify_word(faces):
    F1,F2,F3,F4 = faces
    U0,U1,U2,U3 = F2,F4,F1*F2,F3*F4
    Q = s.simplify(U2*U3)
    V = s.simplify(4*sum(1-s.trace(F)/2 for F in faces))
    w = s.simplify(s.trace(Q)/2)
    prefix = Id
    telescoping = s.zeros(2)
    for F in faces:
        assert s.simplify(F.conjugate().T*F-Id) == s.zeros(2)
        telescoping += prefix*(Id-F)
        prefix = prefix*F
    assert s.simplify(Id-Q-telescoping) == s.zeros(2)
    assert s.simplify(norm2(Id-Q)-4*(1-w)) == 0
    assert s.simplify(sum(norm2(Id-F) for F in faces)-V) == 0
    assert s.simplify(V-(1-w)) >= 0
    original_V = 4*(4-s.trace(U0)/2-s.trace(U1)/2
                    -s.trace(U2*U0.inv())/2-s.trace(U3*U1.inv())/2)
    assert s.simplify(original_V-V) == 0
    return {'V':str(V), 'one_minus_w':str(1-w)}

A=su2(s.Rational(3,5),[s.Rational(4,5),0,0])
B=su2(s.Rational(5,13),[0,s.Rational(12,13),0])
C=su2(s.Rational(1,2),[s.Rational(1,2)]*3)
D=su2(s.Rational(4,5),[0,0,s.Rational(3,5)])
assert A*B != B*A
noncommuting = verify_word([A,B,C,D])
equal_faces = verify_word([D,D,D,D])
# Original eight boundary-edge source constants and energy normalization.
g,w = s.symbols('g w', real=True)
assert s.simplify(8*(1-w*w)/4 - 2*(1-w*w)) == 0
assert 8*s.Rational(-3,4) == -6
assert s.simplify(g*g/2*(2*(1-w*w))-g*g*(1-w*w)) == 0
# Keep the uncentered vacuum energy in the half-source Hardy calculation.
C0,C1,E,gamma,b = s.symbols('C0 C1 E gamma b', positive=True)
anchored = C1*b+(C0+C1*E)*(2*b/gamma)
assert s.simplify(anchored-(C1+2*(C0+C1*E)/gamma)*b) == 0
centered = 4*(b+E*b/gamma)
assert s.simplify(centered-4*(1+E/gamma)*b) == 0
result={'checks_passed':5,
        'scope':'Two nontrivial exact SU(2) word/norm controls; original source normalization and two budget controls. General inequalities are analytic in actual_potential_moment.md.',
        'noncommuting_faces':noncommuting,'equal_faces':equal_faces,
        'uniform_conditional_score_bound_proved':False}
Path(__file__).with_name('bg_actual_potential_checks.json').write_text(
    json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
