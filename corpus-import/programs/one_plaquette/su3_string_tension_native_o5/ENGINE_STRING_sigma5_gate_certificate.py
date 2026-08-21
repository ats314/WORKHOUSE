import importlib.util as iu, pickle, json, math, time
from fractions import Fraction as F
spec=iu.spec_from_file_location('W','/tmp/se/ftw.py'); W=iu.module_from_spec(spec); spec.loader.exec_module(W)
spec2=iu.spec_from_file_location('T','/tmp/se/ENGINE_STRING_su3_torelon.py'); Tt=iu.module_from_spec(spec2); spec2.loader.exec_module(Tt)
GATES=[]
def gate(name,cond,detail=""):
    assert cond, f"GATE FAILED: {name} {detail}"
    GATES.append({"gate":name,"pass":True,"detail":detail}); print(f"PASS  {name}  {detail}")

# --- live exact-rational gates: sigma2, sigma3 (and the single-link Haar primitives) ---
r2=Tt.sigma_reduced(2)[4]; gate("sigma2_exact_rational", r2==F(-22,153), f"{r2}")
r3=Tt.sigma_reduced(3)[4]; gate("sigma3_exact_rational", r3==F(61,408), f"{r3}")

# --- sigma5 three-prime residue gate (reads cached phase2 pickles) ---
KNOWN=W.KNOWN
counts=pickle.load(open('/tmp/se/s5_p1.pkl','rb'))['counts']
gate("sigma5_topo_count", len(counts)==22820, f"{len(counts)} canonical topos")
primes=[33554467,100000007,134217757]; residues={}
for p in primes:
    res=pickle.load(open(f'/tmp/se/s5_mod_{p}.pkl','rb'))
    assert all(c in res for c in counts), "missing topos"
    assert not any(res[c]=='BAD' for c in counts), "BAD prime"
    tot=sum(counts[c]*res[c] for c in counts)%p
    sig=(tot*W.inv(4,p))%p
    exp=(KNOWN[5].numerator*W.inv(KNOWN[5].denominator,p))%p
    residues[p]={"engine":int(sig),"expected":int(exp),"match":sig==exp}
    gate(f"sigma5_mod_{p}", sig==exp, f"engine={sig} expected={exp}")
prod=1
for p in primes: prod*=p
bits=math.log2(prod)
gate("three_prime_gate_strength", bits>75, f"{bits:.1f}-bit combined modulus")

cert={
 "title":"Native SU(3) determinant-sector string tension: sigma5 exact gate-grade certificate",
 "date":"2026-06-15",
 "method":"weight-zero-block fusion-tree singlet projector over GF(p), pure int64",
 "engine":"ftw.py (weight-blocked GF(p)); cluster machinery ENGINE_STRING_su3_torelon.py; folded weights ENGINE_Y6_folded_descloizeaux_preflight.py",
 "sigma5_known_reduced":"137767222189182735950309/2009803206414863779920000",
 "sigma2_exact":str(r2),"sigma3_exact":str(r3),
 "sigma5_three_prime_residues":residues,
 "combined_modulus":prod,
 "gate_bits":round(bits,2),
 "accidental_coincidence_prob":2.0**(-bits),
 "weight_block_dims":{"m7_(5,2)":240,"m7_full_3^7":2187,"reduction_factor":2187/240},
 "n_canonical_topos_sigma5":len(counts),
 "gates":GATES,
 "status":"sigma5 EXACT (gate-grade): reproduced by from-scratch native engine as residue mod 3 independent primes; ~%.0f-bit gate"%bits
}
json.dump(cert,open('/tmp/se/CERT_STRING_sigma5_exact_certificate.json','w'),indent=2)
print("\nALL GATES PASS — sigma5 EXACT gate-grade (%.1f-bit)."%bits)
print("combined modulus =",prod)
