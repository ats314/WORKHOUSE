"""Create suggested append rows without changing a shared registry."""
from hashlib import sha256
import json
from pathlib import Path

run = Path(__file__).resolve().parent
repo = run.parents[1]
out = Path(r"C:\WORKHOUSE\research\w6_bg_uniform_20260910\integration_rows.json")
manifest = json.loads((run / "source_manifest.json").read_text(encoding="utf-8"))
sources = []
by_name = {}
for source in manifest["sources"]:
    path = "runs/w6_bg_budget_2026-09-10/" + source["preserved_path"]
    campaign = "w6_bg_uniform_20260910" if "/campaign/" in path else "w6_subdivision_prior_20260910"
    name = Path(source["preserved_path"]).name
    sid = "DOC:RECENT:" + campaign + ":" + name
    by_name[name] = sid
    sources.append({"id": sid, "title": campaign + " / " + name,
                    "path": path, "original_path": source["original_path"],
                    "sha256": source["sha256"], "bytes": source["size_bytes"]})


def reference(name, anchor, locator):
    return {"id": by_name[name], "anchor": anchor, "locator": locator}


def link(kind, target, detail):
    return {"type": kind, "target": target, "detail": detail}


ground_id = "RESULT:W6_ACTUAL_COMPACT_GROUND_JETS"
budget_id = "RESULT:W6_COMPLETE_TRANSPORT_DERIVATIVE_BUDGET"
tail_id = "RESULT:W6_COMPACT_CONDITIONAL_SCORE_TAIL_CONTROL"
ground_statement = (
    "For the actual fixed compact square at sufficiently small positive coupling, the raw "
    "electric/magnetic and vacuum-subtracted form derivatives through order three obey explicit "
    "g^-j energy bounds. The actual ground-energy and normalized ground-vector derivatives through "
    "order three, and the vacuum-only skew generator through its second derivative, obey the "
    "corresponding inverse-power bounds with explicit constants from E and gamma."
)
budget_statement = (
    "For the complete actual positive-reference source/vacuum transport, energy-operator bounds "
    "||A^(r)(g)||_(q_g->q_g)<=d_r g^(-r-1), r=0,1,2, imply explicit all-energy "
    "M_j(s)<=c_j s^-j for j=1,2,3 and hence the complete compact Schur residual budget. "
    "The composite budget retains changing source energies and physical clock factors."
)
tail_statement = (
    "On the actual compact square, the global noncommuting inequality 1-w<=V and the true-ground transform "
    "prove g^-2 integral(1-w)|f|^2 <= (1+E/gamma)b_g[f] for every centered finite-energy source, uniformly "
    "at small coupling. The conditional-score Hardy constant is finite on every closed positive-coupling "
    "interval, with vanishing endpoint tail products. An exact Gaussian source-preserving dilation bump "
    "has vanishing averaged score control but Hardy constant at least exp(-2)/(2g^2). "
    "A specified phase-adapted local source-preserving field removes the centered leading phase term; "
    "its chart-restricted variance bound follows under stated conditional Poincare and amplitude-jet inputs. "
    "The additional score estimate K_g<=C0+C1 g^-2 E(V|w) would imply the explicit uniform Hardy bound, "
    "but that score estimate remains open."
)
verification = (
    "Analytic proof with independent peer review; 24 exact finite controls replayed in "
    "runs/w6_bg_budget_2026-09-10. The finite controls verify only their recorded coefficient, "
    "normalization, Leibniz and tail-product arithmetic. No full-statement Lean formalization or "
    "uniform interacting Wilson source/grid theorem is claimed."
)
nodes = [
    {"id": ground_id, "statement": ground_statement, "status": "proven", "evidence": "analytic", "tier": 3,
     "scope": "Actual fixed twelve-edge compact square, common electric form domain, positive T,V, "
              "uniform ground energy e_g<=E and actual physical gap gamma>0 for 0<g<g_*. "
              "The constants may depend on the square and are not claimed uniform on growing grids.",
     "detail": "R1-R8b prove raw form bounds (2,6,24), reduced-resolvent ground-energy derivatives "
               "including the third-order normalization term, normalized ground-jet recursion, and vacuum-only "
               "generator estimates. This removes raw operator and vacuum jets from the remaining full source-transport obligation.",
     "verification": verification,
     "sources": [reference("residual_analysis.md", "## 2. Raw electric and magnetic derivatives already have the required scaling", "R1-R8b, sections 2-3"),
                 reference("residual_checks.json", '"passed": 15', "Exact residual finite controls and source hashes")],
     "links": [link("depends_on", "RESULT:W6_SQUARE_FINITE_G_FLOOR", "Supplies the actual fixed-square physical gap."),
               link("depends_on", "RESULT:W6_QUANTUM_FIRST_JET_REMAINDER", "Supplies the uniform small-coupling bound on the actual ground energy."),
               link("bears_on", budget_id, "Supplies the raw centered-form and vacuum derivatives used in the complete transport bridge."),
               link("bears_on", "G19", "Advances the actual selected-pairing derivative budget on the fixed square.")]},
    {"id": budget_id, "statement": budget_statement, "status": "conditional", "evidence": "analytic", "tier": 3,
     "scope": "The actual common-domain compact square source/vacuum transport and nonreducing graph, "
              "conditional on full energy-operator generator jets through order two. Physical clock factors "
              "are retained; interacting grid bounds, coarse matching, and convergence of exact jets remain separate.",
     "detail": "R9-R12 give explicit c_j by energy Gronwall and Leibniz differentiation, retaining both "
               "source arguments and vacuum subtraction. R13-R15 use the prior subdivision result, distinguish "
               "composite from endpoint Taylor jets, and retain source-energy growth and clock-change terms. "
               "A first conditional source derivative into L2 does not by itself imply the missing energy jets.",
     "verification": verification,
     "sources": [reference("residual_analysis.md", "## 4. An explicit bridge from the actual transport generator to M1,M2,M3", "R9-R15 and section 5 norm implication boundary"),
                 reference("w6-subdivided-compact-transport-2026-09-10.md", "## S2. Compatible transport is a cocycle", "Prior project subdivision S2-S5; not new campaign work"),
                 reference("residual_checks.json", '"passed": 15', "Finite Leibniz and physical-clock arithmetic only")],
     "links": [link("depends_on", ground_id, "Supplies explicit raw operator and ground-energy derivative bounds."),
               link("depends_on", "RESULT:W6_COMPACT_POSITIVE_REFERENCE_COMPARISON", "Supplies the complete actual graph, source transport, residual and cubic Schur theorem."),
               link("bears_on", "ROUTE:RECENT_W6_UNIFORM_INTERACTING_TRANSFER", "Reduces its complete derivative input to actual source-generator energy regularity; does not close the route."),
               link("bears_on", "G19", "Supplies a conditional all-source derivative and clock-aware composite error budget.")]},
    {"id": tail_id, "statement": tail_statement, "status": "proven", "evidence": "analytic", "tier": 3,
     "scope": "Distinct scopes: actual fixed-square uniform all-source potential moment; positive-coupling endpoint/interval "
              "finiteness; an exact Gaussian counterexample to an inference, not to the actual compact dilation; "
              "a local phase-repair implication with g-independent phase/chart and conditional hypotheses. "
              "No uniform actual Hardy constant, whole-fiber phase repair, or interacting grid closure.",
     "detail": "M5 and M7-M9 prove the actual noncommuting holonomy and uniform all-source moment inequalities. "
               "M10 is open; M11-M15 conditionally yield the centered multiplier and Hardy constant "
               "C1+2(C0+C1E)/gamma, retaining the uncentered vacuum-energy term. "
               "B1 proves compact endpoint products vanish linearly. B2-B5a derive the exact rare-annulus "
               "lower bound exp(-2)/(2g^2) despite preserved averaged bounds and near-well jets. B6-B8 "
               "construct Z_y=(D_y Phi)^-1(Phi-D_q Phi z), making 2S-ZS coarse-only; the local variance "
               "bound retains chart-complement/mean gluing and fourth-moment obligations.",
     "verification": verification,
     "sources": [reference("bg_analysis.md", "## 1. What the actual compact endpoints do prove", "B1, actual fixed-square endpoint and positive-interval theorem"),
                 reference("bg_analysis.md", "## 2. Exact obstruction to inferring uniformity from averaged ground control", "B2-B5a, exact Gaussian norm-inference obstruction"),
                 reference("bg_analysis.md", "## 3. A concrete phase-adapted repair of the dangerous direction", "B6-B8 and explicitly conditional chart-restricted variance estimate"),
                 reference("bg_gaussian_cutoff_checks.json", '"checks_passed": 4', "Four exact symbolic arithmetic controls only"),
                 reference("actual_potential_moment.md", "## 2. Global noncommuting holonomy inequality", "M5 and M7-M9 actual source moment; M10 open and M11-M15 conditional"),
                 reference("bg_actual_potential_checks.json", '"checks_passed": 5', "Five finite exact SU2, normalization and source-budget controls")],
     "links": [link("depends_on", "RESULT:W6_QUANTILE_SOURCE_WEIGHT_CRITERION", "Identifies the exact coarse energy and Hardy tail-resistance quantity being controlled."),
               link("depends_on", "RESULT:W6_QUANTUM_GROUND_CONCENTRATION", "Supplies the actual averaged renormalized score bound whose implication boundary is tested."),
               link("depends_on", "RESULT:W6_SQUARE_FINITE_G_FLOOR", "Supplies the physical Poincare bound for the actual centered source moment and half-source Hardy reduction."),
               link("depends_on", "RESULT:W6_QUANTUM_FIRST_JET_REMAINDER", "Supplies the uniform actual fixed-square ground-energy bound E used in M8-M15."),
               link("bears_on", "ROUTE:RECENT_W6_UNIFORM_INTERACTING_TRANSFER", "Locates the actual rare-source tail and source-energy regularity still required."),
               link("bears_on", "G19", "Advances the all-source criterion without claiming uniform small-coupling closure.")]},
]

paths = ["docs/derivations/w6-ground-jets-and-transport-budget.md",
         "docs/derivations/w6-conditional-score-tail-control.md"]
aliases = ["W6_GROUND_JETS_TRANSPORT_BUDGET", "W6_CONDITIONAL_SCORE_TAIL_CONTROL"]
titles = ["Actual compact ground jets and conditional complete transport budget",
          "Actual compact source moment, conditional Hardy control and Gaussian inference obstruction"]
document_aliases = [{"alias": alias, "path": path, "title": title, "standing": "repo",
                     "note": "New analytic successor with exact standalone-source intake and scoped finite replay; no uniform Bg or grid closure.",
                     "bears_on": ["G19"]}
                    for alias, path, title in zip(aliases, paths, titles)]


def statement(sid, text, path, anchor, next_anchor, labels, status, hypotheses, depends, remaining):
    lines = (repo / path).read_text(encoding="utf-8").splitlines()
    first = lines.index(anchor) + 1
    last = lines.index(next_anchor) if next_anchor else len(lines)
    return {"id": sid, "statement": text, "locator": f"{anchor} (lines {first}-{last})",
            "anchor": anchor, "source_labels": labels, "status": status, "evidence": "analytic",
            "hypotheses": hypotheses, "depends_on": depends, "lean": [], "remaining": remaining}


ground_deriv = "DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:GROUND_JETS"
transport_deriv = "DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:COMPLETE_BUDGET"
tail_deriv = "DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:INTERVAL_OBSTRUCTION_REPAIR"
deriv_docs = [
    {"id": "CITE:" + aliases[0], "path": paths[0], "sha256": sha256((repo / paths[0]).read_bytes()).hexdigest(),
     "statements": [
         statement(ground_deriv, ground_statement, paths[0],
                   "## 2. Raw electric and magnetic derivatives already have the required scaling",
                   "## 4. An explicit bridge from the actual transport generator to M1,M2,M3",
                   ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R8a", "R8b"], "proven",
                   ["Actual compact fixed-square H_g=(g^2/2)T+g^-2V with nonnegative common-domain T,V.",
                    "Actual simple normalized real ground, smooth at positive coupling; 0<=e_g<=E and physical gap gamma>0 uniformly on the specified small-coupling interval."],
                   [], "No full-statement Lean formalization. Full conditional source-generator jets and growing-grid uniformity are not conclusions."),
         statement(transport_deriv, budget_statement, paths[0],
                   "## 4. An explicit bridge from the actual transport generator to M1,M2,M3",
                   "## 7. Consequence and verification boundary", ["R9", "R10", "R11", "R12", "R13", "R14", "R15"], "conditional",
                   ["Complete actual common-domain source/vacuum transport R'=A R and nonreducing graph from the positive-reference source theorem.",
                    "For q_g=H_g+gamma, full energy-space ||A^(r)(g)||<=d_r g^(-r-1), r=0,1,2, with finite uniform constants.",
                    "Local t in [s/2,s], fixed spectral window below the actual gap. The composite source growth and subdivision inputs are the prior S2-S5 theorem.",
                    "Positive physical clock tau_n; physical matching discrepancies are separately retained, not assumed zero."],
                   [ground_deriv], "Prove the actual complete conditional source-generator energy jets or exact mixed-form substitute; supply interacting-grid, coarse-matching and physical-clock convergence inputs.")
     ]},
    {"id": "CITE:" + aliases[1], "path": paths[1], "sha256": sha256((repo / paths[1]).read_bytes()).hexdigest(),
     "statements": [statement(tail_deriv, "The compact Hardy constant is finite on closed positive-coupling intervals; the Gaussian source-preserving rare-annulus example disproves an inference from averaged scores and near-well jets, and a local phase-adapted field removes the centered leading phase term under its explicit local hypotheses.", paths[1],
                   "## 1. What the actual compact endpoints do prove", "## 4. Current mathematical stopping point",
                   ["B1", "B2", "B3", "B4", "B5", "B5a", "B6", "B7", "B8"], "proven",
                   ["Actual positive smooth compact ground and conditional score at positive g; a closed interval [a,b] with a>0 for uniform endpoint bounds.",
                    "For the distinct Gaussian inference test: the stated independent Gaussian modes, rare-annulus smooth source-preserving bump, and theta=2 sqrt(2).",
                    "For the local phase implication: smooth g-independent conditional phase with nondegenerate minimum, g-independent parametric Morse chart and normalized chart-restricted conditional Poincare bound.",
                    "Amplitude eta derivatives are bounded by C'/g; any chart-complement tails/mean differences and the cutoff fourth-moment condition are separate explicit requirements."],
                   [], "No uniform actual small-g Hardy bound is proved. Construct actual phase/amplitude/global chart control, rare-fiber estimates and full source energy regularity."),
         statement("DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:ACTUAL_SOURCE_MOMENT",
                   "The actual four-face SU2 product obeys 1-w<=V globally. The exact true-ground source form gives g^-2 integral V|f|^2 <= b_g[f]+e_g||f||^2, hence the uniform centered bound integral a_g|f|^2 <=4(1+E/gamma)b_g[f]. If the additional open score inequality K_g<=C0+C1 g^-2 E(V|w) holds, the scalar Hardy constant is at most C1+2(C0+C1E)/gamma.",
                   paths[1], "## 6. Uniform actual source potential moment and sharper score criterion", None,
                   ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15"], "proven",
                   ["Actual four-face Wilson square with the original eight boundary-edge source derivatives and positive kinetic/potential forms.",
                    "Actual positive quantum ground with e_g<=E and physical gap gamma>0 on the specified small-coupling interval; centered finite-energy source for M8-M9.",
                    "M11-M15 additionally assume the expressly open actual conditional-score domination M10 with uniform nonnegative C0,C1."],
                   [], "Prove M10 or another sufficient actual conditional score estimate. The source moment alone does not establish uniform Hardy control, complete transport derivatives, or an interacting grid floor.")]
    }
]
run_row = {"id": "w6_bg_budget_2026-09-10", "dir": "runs/w6_bg_budget_2026-09-10",
           "title": "Actual compact ground jets, conditional source tails and complete derivative budget",
           "bears_on": [ground_id, budget_id, tail_id, "G19"],
           "detail": "Eleven exact source snapshots preserve new campaign notes/controls and prior subdivision work. "
                     "24 exact finite controls replayed; independent analytic peer review has its stated scope. "
                     "Actual ground jets and an actual uniform all-source potential moment are proved on the fixed square; "
                     "the conditional score-to-potential bound, full source-generator energy bounds, uniform actual Hardy constant and interacting-grid closure remain open."}
rows = {"schema": "w6-integration-append-suggestions/v1", "date": "2026-09-10",
        "instructions": "Append document_aliases to ledger/documents.yaml aliases; derivation_documents to ledger/derivation_statements.yaml documents; recent_sources and recent_nodes to ledger/recent_research.yaml; run_row to runs/index.yaml. No ledger file is modified by this helper. The new run source prefix requires the parent's explicit validator allowlist addition.",
        "document_aliases": document_aliases, "derivation_documents": deriv_docs,
        "recent_sources": sources, "recent_nodes": nodes, "run_row": run_row}
out.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"registration_json": str(out), "results": len(nodes),
                  "derivation_groups": sum(len(d["statements"]) for d in deriv_docs), "sources": len(sources)}))
