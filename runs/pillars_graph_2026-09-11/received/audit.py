"""Replay exact review findings without changing the canonical repository.

Run with C:/WORKHOUSE/REPO/.venv/Scripts/python.exe audit.py.
Outputs are scoped review evidence, not new registered scientific claims.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess

from sympy import Matrix, Rational as R, eye, ones, simplify, symbols
from workhouse import constants as K

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent.parent
REPO = ROOT / "REPO"
INTAKE = ROOT / "INBOX/gemini-pillars_20260911"
ATTACHMENT = Path("C:/Users/Alex/.codex/attachments/ddccf2d6-9cf2-4813-bac6-7e7cdabbd948/pasted-text.txt")


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args], text=True, encoding="utf-8").strip()


claims = [json.loads(line) for line in (REPO / "index/claims.jsonl").read_text(encoding="utf-8").splitlines()]
by_id = {c["id"]: c for c in claims}
received = (INTAKE / "pasted-text.txt").read_text(encoding="utf-8")
refs = sorted(set(re.findall(r"(?:RESULT|DERIV):[A-Z0-9_]+", received)))

replacements = {
    "RESULT:SHARED_LINK_WEINGARTEN_WEIGHTS": ["CHK:second-order-all-ranks:the-shared-link-weights-are-weingarten-n-7c4292", "G24"],
    "RESULT:THIRD_ORDER_FACTORIZATION": ["CHK:su-3-second-and-third-order:e-flat-and-t-u-carry-the-ledger-coeffici-64f909"],
    "RESULT:CHARGE_ODD_FLAT_DISPERSION": ["CHK:su-3-second-and-third-order:e-flat-and-t-u-carry-the-ledger-coeffici-64f909", "G18"],
    "RESULT:FOURTH_ORDER_ADJUDICATION": ["CHK:the-third-implementation-and-the-histori-334c14:finding-c-shp-from-the-assembled-amplitu-deda6d", "G3", "C2"],
    "RESULT:PLANAR_BAND_SUPPRESSION": ["CHK:the-planar-limit-of-the-fourth-order-ban-d452f9:two-orders-cancel-in-every-cluster-the-l-3054e8", "G16"],
    "DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT": ["DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE", "DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF8_IF9"],
    "DERIV:WILSON_SC17_PHYSICAL_TIME_LIMIT": ["DERIV:WILSON_SC17_PHYSICAL_TIME_LIMIT:PHYSICAL_TIME_GAP", "DERIV:WILSON_SC17_PHYSICAL_TIME_LIMIT:P19_P20"],
}
for targets in replacements.values():
    assert all(t in by_id for t in targets), targets
crosswalk = [{"received": ref, "exact_id_exists": ref in by_id,
              "use_existing_locators": [ref] if ref in by_id else replacements[ref],
              "meaning": "retrieval locators; support scope must be read, not whole-theorem equivalence"}
             for ref in refs]
dump("graph-crosswalk.json", crosswalk)

checks = []


def check(name, passed, detail):
    checks.append({"name": name, "passed": bool(passed), "detail": str(detail)})


n, x = symbols("n x", real=True)
t = 2*n*(n*n-4)/((n*n-1)*(2*n*n-1)*(4*n*n-9))
check("hopping matches repository and SU(3)", simplify(t-K.hopping(n)) == 0 and t.subs(n, 3) == R(5,612), t)
# N=3+x, x>=0: positive coefficients in each numerator/denominator factor
# prove strict positivity for every real N>=3, not just a rank sample.
factors = [2*n, n*n-4, n*n-1, 2*n*n-1, 4*n*n-9]
check("hopping positivity on N>=3", all(all(c >= 0 for c in f.subs(n,x+3).as_poly(x).all_coeffs()) and f.subs(n,3)>0 for f in factors), "Each factor after N=3+x has positive constant and nonnegative coefficients")
correct_c = K.C_SHP_HISTORICAL + R(25,1024)
check("ADR 0024 exact value", correct_c == K.C_SHP_CONTINUATION_SHIFTED == R(-13035490122347,550663802582400), f"{correct_c} = {float(correct_c):.14f}; received -0.0202133 is incorrect")
q_old = R(17607806155349,1101327605164800)
q_new = 2*K.A_SHP_3+4*correct_c
check("received Q4 is historical", q_old == K.Q4_CROSS == K.BETA_PEN_3/4 and q_new-q_old == R(25,256), f"assembled cross coefficient = {q_new}; increase = 25/256")
mat = Matrix(3,3,lambda i,j: K.A_SHP_3 if i==j else q_new/2)
check("corrected Q4 remains strictly positive", all(e>0 for e in mat.eigenvals()), f"eigenvalues with multiplicities: {mat.eigenvals()}")
check("corrected Q4 explicit sum of squares", q_new/2>0 and K.A_SHP_3-q_new/2>0, f"Q4=({K.A_SHP_3-q_new/2}) sum L_i^2 + ({q_new/2})(sum L_i)^2")
q0 = R(4,5)+R(1,998)
check("blocked transfer contraction", 0<q0<1, f"q0={q0}; physical electric rate is -log(q0)/s1, not gamma")
check("source Gram lower bound", R(312481,419904)==R(559,648)**2 and R(312481,419904)>R(9,16), f"{R(312481,419904)} > 9/16")
P=ones(4)/4
Q=eye(4)-P
M=Matrix(4,4,range(16))
check("tetrahedral Hodge projection identities", P*P==P and Q*P==Matrix.zeros(4) and 4*P*Q*M*ones(4,1)==Matrix.zeros(4,1), "L_up=4P; L_up Q R psi=0 for arbitrary R")
p,r,s,m,c = symbols("p r s m c", positive=True)
star=(p+r)/m
rate=m*(r-2*s)/(p+r)
check("moving-time balance", simplify((m-(p+2*s)/c).subs(c,star)-rate)==0 and simplify(((r-2*s)/c).subs(c,star)-rate)==0, rate)
# Exact sufficient horizon for a desired positive target M.
target=symbols("M",positive=True)
gap= simplify((r-2*s)/target - (p+2*s)/(m-target))
check("target-rate feasibility identity", simplify(gap-(p+r)*(rate-target)/(target*(m-target)))==0, "For 0<M<m, admissible c has (p+2s)/(m-M)<=c<=(r-2s)/M and c<=c_max; equality gives support >=M via all E<M")
poly=lambda z: 6561*z**4+1458*z**3-81*z**2-72*z+1
check("SC17 endpoint bracket", poly(R(1,73))>0 and poly(R(1,72))<0, f"P(1/73)={poly(R(1,73))}; P(1/72)={poly(R(1,72))}; bracketing check, not uniqueness proof")
lean=(REPO / "lean/Workhouse/Basic.lean").read_text(encoding="utf-8")
check("received Lean hopping locator is absent", re.search(r"\btheorem\s+t_N_pos_of_ge_three\b",lean) is None, "Actual named inputs include Workhouse.hopping_three and Workhouse.rank_law_numerator; positivity proved by factor signs above")

dump("exact-findings.json", {"scope":"Review replay; algebraic controls, not full physical proofs", "passed":sum(c['passed'] for c in checks), "total":len(checks), "checks":checks})
assert all(c["passed"] for c in checks), checks

source_names = [
    "ledger/results.yaml", "ledger/recent_research.yaml", "ledger/derivation_statements.yaml",
    "lean/Workhouse/Basic.lean", "lean/Workhouse/HodgeFeshbach.lean",
    "lean/Workhouse/ThermodynamicLimit.lean", "lean/Workhouse/SpectralReconstruction.lean",
    "src/workhouse/constants.py", "src/workhouse/invariants/rank_law.py",
    "src/workhouse/invariants/su3.py", "src/workhouse/invariants/fourth_order.py",
    "docs/derivations/moving-time-spectral-gap.md", "docs/derivations/os-kernel-moving-time-gap.md",
    "docs/derivations/universal-cellular-hodge-tetrahedral.md",
    "docs/derivations/wilson-sc17-thermodynamic-limit.md", "docs/derivations/wilson-sc17-physical-time-limit.md",
    "paper/research_notes/G18_WILSON_INFINITE_VOLUME_PHYSICAL_BAND_20260905.md",
    "docs/decisions/0021-the-shared-link-amplitudes-computed-from-outside.md",
    "docs/decisions/0024-the-corner-cluster-from-a-third-implementation-and-the-ledger-that-was-here.md",
    "docs/decisions/0046-the-fourth-order-band-is-planar-suppressed-two-orders-below-its-channels.md",
]
pins = [{"path":name,"sha256":hashlib.sha256((REPO/name).read_bytes()).hexdigest(),"size":(REPO/name).stat().st_size} for name in source_names]
dump("reviewed-source-manifest.json", {"checkout":str(REPO),"revision":git("rev-parse","HEAD"),"files":pins})
raw=(INTAKE/"pasted-text.txt").read_bytes()
assert raw==ATTACHMENT.read_bytes()
manifest={"received_date":"2026-09-11","original_path":str(ATTACHMENT),"preserved_path":"pasted-text.txt","size":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
(INTAKE/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
dump("git-observation.json", {"observed_at":datetime.now(timezone.utc).isoformat(),"head":git("rev-parse","HEAD"),"branch":git("branch","--show-current"),"status":git("status","--short","--branch"),"remote_main":git("ls-remote","origin","refs/heads/main"),"local_origin_main":git("rev-parse","origin/main"),"difference":git("diff","--stat","HEAD","origin/main")})
print(json.dumps({"exact_findings_passed":len(checks),"graph_references":len(refs),"unresolved_received_ids":sum(ref not in by_id for ref in refs),"correct_c":str(correct_c),"correct_Q4_cross":str(q_new),"source_pins":len(pins)},indent=2))
