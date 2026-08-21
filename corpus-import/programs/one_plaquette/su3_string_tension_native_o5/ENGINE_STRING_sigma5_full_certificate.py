"""sigma5 EXACT certificate (independent reconstruction).
Live gates: sigma2,sigma3 exact-rational. sigma5: CRT over 7 independent primes +
rational reconstruction from the native engine ALONE (no literature value used as input);
KPS value compared only post-hoc. Reads per-prime phase2 pickles produced by ftw.py."""
import pickle, importlib.util as iu, json
from fractions import Fraction as F
from math import isqrt, gcd
spec=iu.spec_from_file_location('W','/tmp/se/ftw.py'); W=iu.module_from_spec(spec); spec.loader.exec_module(W)
spec2=iu.spec_from_file_location('T','/tmp/se/ENGINE_STRING_su3_torelon.py'); Tt=iu.module_from_spec(spec2); spec2.loader.exec_module(Tt)
inv=W.inv; GATES=[]
def gate(name,cond,detail=""):
    assert cond, f"GATE FAILED: {name} {detail}"
    GATES.append({"gate":name,"pass":True,"detail":detail}); print(f"PASS  {name}  {detail}")

# exact-rational gates
r2=Tt.sigma_reduced(2)[4]; gate("sigma2_exact_rational", r2==F(-22,153), f"{r2}")
r3=Tt.sigma_reduced(3)[4]; gate("sigma3_exact_rational", r3==F(61,408), f"{r3}")

primes=[33554467,100000007,134217757,192999973,192999949,192999941,192999931]
counts=pickle.load(open('/tmp/se/s5_p1.pkl','rb'))['counts']
gate("sigma5_topo_count", len(counts)==22820, f"{len(counts)} canonical topos")
L=4; res_modp={}
for p in primes:
    r=pickle.load(open(f'/tmp/se/s5_mod_{p}.pkl','rb'))
    gate(f"sigma5_complete_p{p}", all(c in r for c in counts) and not any(r[c]=='BAD' for c in counts), "all topos, no bad")
    res_modp[p]=(sum(counts[c]*r[c] for c in counts)%p*inv(L,p))%p
def crt(rs,ms):
    R,M=0,1
    for r,m in zip(rs,ms):
        t=((r-R)*pow(M,-1,m))%m; R+=M*t; M*=m
    return R%M,M
R,M=crt([res_modp[p] for p in primes],primes)
gate("modulus_recon_safe", M.bit_length()>=163, f"{M.bit_length()}-bit modulus (need >=163)")
def rat_recon(a,m):
    a%=m; N=isqrt(m//2); r0,r1=m,a; t0,t1=0,1
    while r1>N:
        q=r0//r1; r0,r1=r1,r0-q*r1; t0,t1=t1,t0-q*t1
    n,d=r1,t1
    if d<0: n,d=-n,-d
    return (n,d) if (n-a*d)%m==0 and gcd(n,d)==1 else None
rec=rat_recon(R,M); gate("rational_reconstruction_succeeds", rec is not None)
n,d=rec; val=F(n,d)
gate("reconstruction_roundtrip_all7", all((val.numerator*inv(val.denominator,p))%p==res_modp[p] for p in primes), "matches all 7 residues")
Nb=isqrt(M//2)
gate("reconstruction_unique", abs(n)<=Nb and d<=Nb, f"|n| {abs(n).bit_length()}b, d {d.bit_length()}b < bound {Nb.bit_length()}b")
KPS=F(137767222189182735950309,2009803206414863779920000)
gate("posthoc_equals_KPS", val==KPS, "engine reconstruction coincides with KPS literature value (check only)")

cert={"title":"Native SU(3) sigma5 — independent reconstruction certificate (engine alone)",
 "date":"2026-06-15","method":"weight-zero-block fusion-tree GF(p) engine; CRT over 7 primes + Wang rational reconstruction",
 "primes":primes,"sigma5_residues":{str(p):int(res_modp[p]) for p in primes},
 "combined_modulus_bits":M.bit_length(),
 "sigma5_reduced_reconstructed":f"{n}/{d}",
 "sigma5_reduced_value":str(val),
 "reconstruction_uses_literature_value":False,
 "posthoc_equals_KPS":val==KPS,
 "n_canonical_topos":len(counts),"weight_block_dim_m7":240,
 "gates":GATES,
 "status":"sigma5 EXACT and INDEPENDENTLY RECONSTRUCTED from the native engine (no KPS input); coincides with KPS"}
json.dump(cert,open('/tmp/se/CERT_STRING_sigma5_exact_certificate.json','w'),indent=2)
print(f"\nALL {len(GATES)} GATES PASS. sigma5 = {val}")
print("independently reconstructed (no literature input); coincides with KPS:", val==KPS)
