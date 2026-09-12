"""Record reproducible graph searches for manually read source statements."""
import hashlib,json,re
from pathlib import Path
ROOT=Path('C:/WORKHOUSE');OUT=Path(__file__).resolve().parent
flux='ALL THEORY/theory/notes/NOTE_FLUX_singular_geometry_derivations_2026-08-28.md'
findings=[
('F01','Cubic quotient regularity trichotomy',flux,[75,104],r'regularity.trichotomy|C\^?\{?1,1|C\^?\{?3,1|notin.{0,4}C\^4'),
('F02','Equal-ray tomography and independent intercept holdout',flux,[133,199],r'equal.ray|ray.tomography|RAY_BLIND_INTERCEPT|b_?3\s*=\s*2b_?2'),
('F03','No uniformly localized finite translation frame',flux,[203,265],r'translation.frame|uniformly.localized|dipolar.principal|frame.bound.collaps'),
('F04','Joint rank-volume monotone scaling and sharp bound',flux,[269,354],r'joint.rank.volume|405/68|405\s*/\s*68|RANK_VOLUME_LOWER_ENDPOINT'),
('F05','Finite-order nested-quotient spectral reduction theorem','WORK_SINCE_LAST_SESSION/FINITE_ORDER_NESTED_QUOTIENT_SPECTRAL_REDUCTION_THEOREM_FULL_DERIVATION_2026-08-28.md',[178,547],r'Nested.Quotient Spectral Reduction|energy.decorated quotient graph|exact.history.merging'),
('F06','Residual-certified B6 SU3 shell word quotient','WORK_SINCE_LAST_SESSION/B6_SHELL_BLOCK_KRYLOV_REDUCTION_2026-08-28.md',[1,115],r'b6_shell_block_krylov|B6 shell quotient|1\.3039546641713|67\s*\+\s*3\s*\(?155'),
('F07','Positive matrix-measure isolated-pole persistence','WORK_SINCE_LAST_SESSION/WORKHOUSE_CARRIER_TO_PARTICLE_PROOF_DOSSIER.md',[607,730],r'pole.persistence|isolated pole survives|empty.annulus|Portmanteau'),
('F08','SU2 affine plaquette Laplacian identity','09_ARCHIVE/sorted_second_pass/05_affine_laplacian_law_analytic_proof.md',[54,198],r'affine.laplacian|12\s*-\s*12\s*B|Delta.{0,10}B_avg'),
('F09','Conditional matrix spectral floor and defect Jensen bound','09_ARCHIVE/sorted_second_pass/01_conditional_spectral_floor_monotonicity.md',[14,82],r'conditional.spectral.floor|defect.monotonicity|lambda_min.*conditional'),
('F10','Six disjoint staple coordinates in four dimensions','09_ARCHIVE/sorted_second_pass/LYAPUNOV_09_appendix_disjoint_staple_coordinates_d4.md',[51,180],r'disjoint.staple|six.local.link.variables|disjoint.star.*coordinates'),
('F11','Positive-sector phase isolation for theta tensor networks','09_ARCHIVE/sorted_second_pass/LATTICE_QCD_phase_isolation_principle.md',[28,114],r'phase.isolation|positive.coefficient.*generating|boundary.only.theta'),
('F12','VSU constitutive action and bounded-domain existence uniqueness','09_ARCHIVE/sorted_second_pass/VSU_Convex_Poisson_WellPosedness.md',[43,243],r'vacuum.stiffness|convex.poisson|VSU_|1-e\^.*modified.Poisson'),
]
rows=[json.loads(x) for x in (OUT/'baseline/index__claims.jsonl').read_text(encoding='utf-8').splitlines()]
data=[]
for fid,title,path,loc,query in findings:
    b=(ROOT/path).read_bytes();sha=hashlib.sha256(b).hexdigest();pat=re.compile(query,re.I)
    named=[r for r in rows if r['kind'] not in ('note','archive') and Path(path).name.lower() in json.dumps(r,ensure_ascii=False).lower()]
    matched=[r for r in rows if r['kind'] not in ('note','archive') and pat.search(json.dumps(r,ensure_ascii=False))]
    notes=[r for r in rows if r['kind']=='note' and sha[:12] in r.get('detail','')]
    data.append({'id':fid,'title':title,'source':path,'source_sha256':sha,'read_lines':loc,'query_regex':query,'noninventory_filename_hits':named,'noninventory_query_hits':matched,'inventory_nodes':notes,'interpretation':'Manual source reading and nearest-result comparison are in REPORT.md. Zero keyword matches alone do not prove semantic absence.'})
extra=['ALL THEORY/numerics/engines/ENGINE_FLUX_singular_geometry_derivations.py','WORK_SINCE_LAST_SESSION/b6_shell_block_krylov_reduction_certificate.json','WORK_SINCE_LAST_SESSION/cleanroom_b6_symbolic_certificate.json','09_ARCHIVE/sorted_second_pass/01_determinant_reduction_theorem.md','09_ARCHIVE/sorted_second_pass/LYAPUNOV_08_transversality_rank3_and_binomial_tail_drift.md']
sources={p:{'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),'size':(ROOT/p).stat().st_size} for p in {x[2] for x in findings}|set(extra)}
(OUT/'graph_comparison.json').write_text(json.dumps({'baseline_commit':'ffff7bb2e67b976ba50fe5cf7184966dd581535f','findings':data},indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'reviewed_source_manifest.json').write_text(json.dumps(sources,indent=2,ensure_ascii=False),encoding='utf-8')
for d in data:print(d['id'],len(d['inventory_nodes']),'inventory,',len(d['noninventory_filename_hits']),'filename,',len(d['noninventory_query_hits']),'terminology hits')

