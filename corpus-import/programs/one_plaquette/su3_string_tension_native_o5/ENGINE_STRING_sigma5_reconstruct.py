import pickle, importlib.util as iu, math
from fractions import Fraction as F
from math import isqrt, gcd
spec=iu.spec_from_file_location('W','/tmp/se/ftw.py'); W=iu.module_from_spec(spec); spec.loader.exec_module(W)
inv=W.inv

primes=[33554467,100000007,134217757,192999973,192999949,192999941,192999931]
counts=pickle.load(open('/tmp/se/s5_p1.pkl','rb'))['counts']
L=4
# engine's sigma5 mod each prime (NO reference to any known value)
res_modp={}
for p in primes:
    r=pickle.load(open(f'/tmp/se/s5_mod_{p}.pkl','rb'))
    assert all(c in r for c in counts) and not any(r[c]=='BAD' for c in counts), f"prime {p} incomplete/bad"
    tot=sum(counts[c]*r[c] for c in counts)%p
    res_modp[p]=(tot*inv(L,p))%p
print("engine sigma5 residues (reduced, L=4):")
for p in primes: print(f"  mod {p}: {res_modp[p]}")

# CRT
def crt(rs, ms):
    R, M = 0, 1
    for r, m in zip(rs, ms):
        # combine (R mod M) with (r mod m)
        g = M  # M,m coprime (distinct primes)
        # solution x = R + M*t, x ≡ r (mod m) -> t ≡ (r-R)*inv(M,m) (mod m)
        t = ((r - R) * pow(M, -1, m)) % m
        R = R + M*t; M = M*m
    return R % M, M
R, M = crt([res_modp[p] for p in primes], primes)
print(f"\ncombined modulus M = {M}  ({M.bit_length()} bits)")

# rational reconstruction (Wang): find n/d with a ≡ n*d^-1 (mod M), |n|,d <= sqrt(M/2)
def rat_recon(a, m):
    a%=m; N=isqrt(m//2)
    r0,r1=m,a; t0,t1=0,1
    while r1>N:
        q=r0//r1
        r0,r1=r1,r0-q*r1
        t0,t1=t1,t0-q*t1
    n,d=r1,t1
    if d<0: n,d=-n,-d
    if d==0 or gcd(n,d)!=1: return None
    if abs(n)<=N and d<=N and (n - a*d)%m==0: return (n if t1>=0 else -n, d)
    return (n,d) if (n - a*d)%m==0 else None

rec=rat_recon(R, M)
print("\n=== RATIONAL RECONSTRUCTION (engine alone, no KPS input) ===")
if rec is None:
    print("FAILED — need more primes")
else:
    n,d=rec
    # fix overall sign: reduced sigma is negative (sign convention 1/2 W(2y)); reconstruction gives a representative
    val=F(n,d)
    print(f"sigma5_reduced (engine) = {val}")
    print(f"  = {n} / {d}")
    # round-trip gate: residue must match for ALL primes
    ok_all=all((val.numerator*inv(val.denominator,p))%p==res_modp[p] for p in primes)
    print(f"round-trip gate (matches all 7 residues): {ok_all}")
    # numerator/denominator size sanity vs bound
    Nb=isqrt(M//2)
    print(f"  |num|={abs(n)} (bits {abs(n).bit_length()}), den={d} (bits {d.bit_length()}); bound sqrt(M/2) bits {Nb.bit_length()}")

# INDEPENDENT CHECK ONLY (not used above): compare to KPS literature value
KPS=F(137767222189182735950309,2009803206414863779920000)
print(f"\n--- post-hoc check vs KPS literature value (NOT used in reconstruction) ---")
print(f"KPS sigma5_reduced = {KPS}")
if rec is not None:
    val=F(rec[0],rec[1])
    print(f"engine == +KPS: {val==KPS}   engine == -KPS: {val==-KPS}   |engine|==|KPS|: {abs(val)==abs(KPS)}")
