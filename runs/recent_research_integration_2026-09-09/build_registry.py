"""Author the scoped registry once, preserving cited campaign files byte for byte.

Existing differing destinations are rejected. Original scripts are preserved as
evidence; running them can write their own outputs or require historical paths.
The native registry loader needs only the copies inside this checkout.
"""

from pathlib import Path
import hashlib
import json
import re

import yaml

REPO = Path(__file__).resolve().parents[2]
BUNDLE = Path(__file__).resolve().parent
ORIGINAL = REPO.parents[1] / "research"
CAMPAIGNS = {
    "a": "anisotropy_variance_20260908",
    "r": "w6_continuation_20260909",
    "g": "w6_graph_path_20260909",
    "q": "w6_quantum_attempt_20260909",
    "c": "w6_combes_thomas_20260909",
    "d": "w6_adjacent_strip_20260909",
    "t": "w6_three_strip_20260909",
    "s": "w6_square_block_20260909",
    "p": "w6_compact_continuation_20260909",
}
SOURCES = {}
NODES = []
A = "RESULT:RECENT_ANISOTROPY_"
W = "RESULT:W6_"
R = "ROUTE:RECENT_"


def save(path, data):
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"Refusing to overwrite different existing bytes: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def source(campaign, filename, locator="Complete source argument", anchor=None):
    campaign = CAMPAIGNS[campaign]
    original = ORIGINAL / campaign / filename
    data = original.read_bytes()
    text = data.decode("utf-8-sig")
    anchor = anchor or next(line for line in text.splitlines() if line.strip())
    if anchor not in text:
        raise ValueError(f"Missing anchor in {original}: {anchor}")
    destination = BUNDLE / "sources" / campaign / filename
    if not destination.resolve().is_relative_to(REPO.resolve()):
        raise ValueError("Source destination must stay inside the checkout")
    save(destination, data)
    sid = "DOC:RECENT:" + campaign + ":" + re.sub(r"[^A-Za-z0-9_.-]", "-", filename)
    SOURCES[sid] = {
        "id": sid,
        "title": f"{campaign} / {filename}",
        "path": destination.relative_to(REPO).as_posix(),
        "original_path": original.as_posix(),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }
    return {"id": sid, "locator": locator, "anchor": anchor}


def controls(campaign, *filenames):
    return [
        source(campaign, filename, "Preserved historical control; not replayed by registry loading")
        for filename in filenames
    ]


def link(kind, target, detail):
    return {"type": kind, "target": target, "detail": detail}


def depends(target, detail):
    return link("depends_on", target, detail)


def relevance(target="G19", detail="Scoped input or remaining obligation for the selected inverse/continuum route."):
    return link("bears_on", target, detail)


def node(ident, statement, scope, detail, sources, links=(), status="proven", value=None):
    item = {
        "id": ident, "statement": statement, "status": status,
        "evidence": "analytic", "tier": 3, "scope": scope, "detail": detail,
        "verification": (
            "The located source supplies the analytic argument under this scope. "
            "Preserved executable controls and Lean artifacts establish their own scope. "
            "This integration verifies source identity and locators; it does not claim a fresh "
            "replay or full-statement native formalization. Separate native check/theorem edges "
            "identify any currently certified component."
        ),
        "sources": sources, "links": list(links),
    }
    if value is not None:
        item["value"] = value
    NODES.append(item)


node(A + "VARIANCE_CORE",
     "The carrier residual is ||QHp||^2=4 C^2 q^2 V, with V=sum x_i^3-(sum x_i^2)^2=sum_{i<j} x_i x_j(x_i-x_j)^2.",
     "Assembled SU(3) centered fourth-order kernel; q>0, x_i=a_i/q and the repository carrier convention. Finite-order, in-sector identity.",
     "Q removes the carrier-preserving terms. The remaining diagonal residual is its second moment minus squared first moment. The original verifier additionally checks the full Laurent kernel, beyond assuming the displayed decomposition.",
     [source("a", "THEORY.md", "Sections 1-2: definitions and residual proof", "## 2. Precise theory"),
      source("a", "TEST_REPORT.md", "Independent and Lean verification scope", "## Lean"),
      source("a", "Variance.lean", "variance_identity and variance_nonnegative", "theorem variance_identity")]
     + controls("a", "verify.py", "certificate.json", "test_independent.py"),
     [relevance("G11", "Computes the exact directional residual in the near-Gamma isolation mechanism."),
      relevance("G18", "Describes in-sector carrier rotation; physical source overlap is a separate statement.")])
node(A + "NODAL_SET",
     "The fourth-order carrier is unmixed exactly when all positive a_i are equal: axes, equal face diagonals, and equal body diagonals.",
     "q>0 and nonzero assembled C; equality concerns lattice sin^2(k_i/2). Gamma and higher-order mixing are excluded.",
     "Nonnegativity of each pairwise variance term proves the complete zero classification. The generic holdout (1/6,1/3,1/2) has V=5/324.",
     [source("a", "THEORY.md", "Section 3: zero-set proof", "## 3. Exact unmixed directions"),
      source("a", "Variance.lean", "axis_node, face_node, body_node, generic_holdout", "theorem generic_holdout")],
     [depends(A + "VARIANCE_CORE", "The pairwise nonnegative variance determines its zero set."), relevance("G11")], value="5/324")
node(A + "OVERLAP_ENERGY",
     "Directional variance gives 1-|<p,v0>|^2<=4 C^2 u^4 V/d^2 and 0<=mu-E0<=4 C^2 u^6 q V/d.",
     "Truncated M=t3*u^2*q*Q+u^4*H; 0<u^2<2/51 and d=t3-2*Ciso*u^2>0. Only its lowest in-sector band.",
     "Weyl separation and the exact residual variance prove overlap control; positivity of (M-E0)(M-E1) proves the energy inequality. There is no q loss in the overlap denominator. Physical source overlap is not established by this statement.",
     [source("a", "THEORY.md", "Section 4: spectral proof", "## 4. Sharper overlap and energy bounds")]
     + controls("a", "adversarial_certificate.json"),
     [depends(A + "VARIANCE_CORE", "Supplies the exact residual variance."), relevance("G18")])
node(A + "INDUCED_SIXTH",
     "Fourth-order virtual mixing induces -(4 C^2/t3)u^6 qV with shape ratio 1:3:-4 in e2/q, e3/q^2 and e2^2/q^3.",
     "Fixed nonzero momentum and the displayed truncated effective Hamiltonian. Induced mixing contribution only, not the complete sixth-order coefficient.",
     "Nondegenerate perturbation theory for M/u^2 yields the negative contribution. A direct sixth-order matrix, fifth-order terms and other sectors remain separate inputs in the complete expansion.",
     [source("a", "THEORY.md", "Section 5: perturbative derivation and boundary", "## 5. A sixth-order prediction"),
      source("a", "Variance.lean", "shape_identity and induced_coefficient", "theorem induced_coefficient")],
     [depends(A + "VARIANCE_CORE", "The residual determines the induced term."), relevance("G9"), relevance("G14")],
     value="-169924002729806205028788409/619343593697933825385600000")
node(R + "ANISOTROPY_DIRECT_SIXTH",
     "Extract the direct sixth-order carrier expectation and combine it with the induced mixing contribution in one convention.",
     "Complete sixth-order flux-band expansion, including direct and other-sector terms.",
     "Whether the 1:3:-4 shape survives or is canceled is an explicit remaining calculation. The induced contribution does not discharge G9.",
     [source("a", "THEORY.md", "Section 7: next calculation", "The next decisive research operation")],
     [depends(A + "INDUCED_SIXTH", "Computed component needed for direct-plus-induced assembly."), relevance("G9")], status="open")

node(W + "RESIDUAL_VARIATIONAL_IDENTITY",
     "The selected inverse difference equals -d[u,u]+||rho_p||^2_(a_g dual), with u=A0^-1 t and rho_p=a_g[.,u]-<.,t>.",
     "Positive closed fast forms in a compatible physical source chart; u in both form domains and a residual continuous in interacting energy.",
     "Completing the variational square proves R1. The literal mixed pairing requires a common-domain argument or its compatible weak extension. No global Gaussian/compact form-domain equality is assumed.",
     [source("r", "W6_PATH_FORWARD.md", "Section 1, R1 and proof", "## 1. Precise form statement")]
     + controls("r", "verify_w6.py", "verification.json"), [relevance()])
node(W + "RESIDUAL_CRITERION",
     "Independent lower-fast-form control plus diagonal and dual-residual estimates imply the stated W6 inverse bound.",
     "A_g>=kappa L with domain inclusion; |d[u,u]|<=a|g|b and ||rho||_(L dual)<=c|g|sqrt(b), uniform in all required parameters.",
     "Inverse order and R1 yield (a+c^2*g0/kappa)|g|b. Even a sqrt(|g|) residual estimate suffices for W6 order. The required coupled Wilson estimates remain hypotheses.",
     [source("r", "W6_PATH_FORWARD.md", "Section 2, R2-R4", "## 2. A sufficient estimate")],
     [depends(W + "RESIDUAL_VARIATIONAL_IDENTITY", "Exact identity before estimating both terms."), relevance()], status="conditional")
node(W + "NEAR_UNIT_GAUSSIAN_OBSTRUCTION",
     "A near-unit global lower Gaussian comparison fails on the SU(2) four-link cell in the stated retained-rank regime.",
     "Actual compact radial operator versus Gaussian oscillator; retained rank fixed or o(g^-2). No assertion about general infinite-rank retention.",
     "Radial conjugacy and interval bracketing give g^2 N(8/g^2)->8/pi>2, whereas the Gaussian count tends to 2. Interlacing contradicts a lower comparison tending to one. A smaller fixed coercivity fraction remains possible.",
     [source("r", "W6_PATH_FORWARD.md", "Section 5: radial counting obstruction", "g^2N_{H_g-e_g}"),
      source("r", "agent_route.md", "Independent radial conjugacy and counting proof")], [relevance()])
node(W + "FAST_HESSIAN_LOCAL_BOUND",
     "Fast restriction gives Hess S>=alpha*kappa_L/2 on a coupling-independent local chart.",
     "Hess S>=alpha(K-CrI), K restricted to EF>=kappa_L I, and r<=min(r_star,kappa_L/(2C)); fixed block/group and common tangent transport.",
     "Absorb the third-derivative Taylor error into fast coercivity. This is a classical fixed-tangent action statement, not a true quantum conditional or curved-source-fiber estimate.",
     [source("g", "GRAPH_PATH.md", "Section 3, G1-G3 proof and scope", "## 3. First established connection")]
     + controls("g", "verify_bridges.py", "bridge_checks.json"), [relevance()], status="conditional")
node(W + "LOCAL_DERIVATIVE_DUAL_CRITERION",
     "A controlled fast Dirichlet floor and bounded derivative overlap imply a residual dual estimate without product independence.",
     "D>=lambda I, A_g>=kappa D, compatible domains, and a complete centered residual representation with overlap m, derivative bound J and source synthesis bound C_B.",
     "Spectral calculus gives inverse energy<=ell[rho]/(kappa*lambda^2). Pointwise Cauchy-Schwarz gives m*J*C_B*g^2*b/(kappa*lambda^2), without assuming independent conditional variables.",
     [source("g", "GRAPH_PATH.md", "Section 4, G4-G8 proof", "## 4. Second established connection")],
     [link("bears_on", W + "RESIDUAL_CRITERION", "A sufficient route to its dual estimate; this derivative theorem is independently proved."), relevance()], status="conditional")
node(W + "BOUQUET_VERTICAL_GAP_OBSTRUCTION",
     "The actual SU(2) bouquet vertical conditional gap is at most 3g^2/4 while its full physical fast compression retains a positive floor.",
     "Eight-edge two-square bouquet, literal retained product U1 U2, true quantum ground and physical conditionally centered tests.",
     "Radial-ground concavity and gauge-invariant tests near central coarse holonomy give the vanishing vertical upper bound on positive-measure sets. Horizontal energy supplies what this surrogate omits. Neither Wilson W6 nor its full fast floor is refuted.",
     [source("q", "QUANTUM_CONTINUATION.md", "Section 1, Q1-Q2", "## 1. An actual Wilson obstruction"),
      source("q", "fast_agent.md", "Radial, domain and physical-localization proof")]
     + controls("q", "check_fast_agent.py", "fast_agent_controls.json"), [relevance()])
node(W + "HORIZONTAL_DENOMINATOR_COUNTEREXAMPLE",
     "An exact two-torus model satisfies the W6 dual bound while residual derivative and unweighted L2 bounds diverge over retained energies.",
     "H_g=-partial_k^2-(1+g cos k)partial_y^2, |g|<1/2, P=E_k and b=||partial_y p||^2. This model is not Wilson.",
     "The full inverse retains n^2+4 and yields g^2/[8(1-|g|)]. Dropping the horizontal denominator produces divergent all-mode ratios; a finite sample cannot certify their supremum.",
     [source("q", "QUANTUM_CONTINUATION.md", "Section 3, Q5", "## 3. The full residual"),
      source("q", "residual_agent.md", "Complete all-mode proof"),
      source("c", "CT_AUDIT.md", "Section 2, CT3-CT4", "## 2. The proposed extraction")]
     + controls("q", "verify_residual_agent.py", "residual_agent_checks.json"), [relevance()])
node(W + "ENERGY_WEIGHTED_CT",
     "Energy-weighted Combes-Thomas localization preserves horizontal inverse energy and gives exponential decay under the stated common-space hypotheses.",
     "Actual orthogonal block decomposition; A=D^(1/2)BD^(1/2), B>=kappa I, finite off-diagonal range R and row/column sum J, with the specified closed-form realization.",
     "Truncated weights yield mu=log(1+kappa/(2J))/R and weighted inverse decay 2 exp(-mu distance)/kappa. Energy-dual residual synthesis then controls the global residual. Actual Wilson compression, transport and uniform local synthesis remain inputs.",
     [source("c", "CT_AUDIT.md", "Section 5, CT6-CT12", "## 5. A correct energy-weighted"),
      source("c", "ct_repair.md", "Closed forms, weighted conjugation and many-body synthesis")]
     + controls("c", "verify_audit.py", "audit_checks.json"),
     [link("bears_on", W + "RESIDUAL_CRITERION", "A conditional localization realization of its dual estimate; the localization theorem is independently proved."), relevance()], status="conditional")
node(W + "PROJECTED_LOCALITY_COUNTEREXAMPLE",
     "Locality of a bare operator and a positive compressed gap do not imply spatial decay after nonlocal projection.",
     "Cycle of N sites, H=I, Q=I-|v><v| with constant v. Abstract projection example, not identification of Wilson Q.",
     "The embedded inverse is Q, with entries -1/N at separation N/2. No N-independent positive exponential rate bounds it; actual projected locality needs a separate proof.",
     [source("c", "CT_AUDIT.md", "Section 4, CT5", "## 4. A gap and a local bare operator"),
      source("c", "operator_audit.md", "Projection and operator-identification audit")], [relevance()])
node(R + "W6_VERTICAL_GAP_SURROGATE",
     "The unrestricted coupling-independent vertical-gap surrogate is falsified in the actual bouquet scope.",
     "Only the unrestricted conversion from local fast tangent positivity; good-background and full-quantum estimates remain distinct possibilities.",
     "Retain the failed surrogate and redirect to the complete quantum energy without retracting the full fast floor or W6.",
     [source("q", "QUANTUM_CONTINUATION.md", "Section 1: exact excluded scope", "it does not refute a conditional estimate")],
     [link("closed_by", W + "BOUQUET_VERTICAL_GAP_OBSTRUCTION", "Actual quantum tests give the vanishing vertical upper bound."),
      link("cannot_decide", "G19", "This failed surrogate neither proves nor refutes continuum construction.")], status="falsified")
node(R + "W6_UNWEIGHTED_RESIDUAL_SURROGATE",
     "The proposed all-energy unweighted local L2 residual estimate is falsified by the exact motivating model.",
     "Inference from finite controls or a fast floor to a uniform L2 residual operator bound; not Wilson W6 itself.",
     "The corrected route retains inverse denominators and estimates complete residuals in actual fast energy duals.",
     [source("c", "CT_AUDIT.md", "Sections 2 and 6: failed C0 extraction", "The desired local L2 operator norm C0 has infinite supremum")],
     [link("closed_by", W + "HORIZONTAL_DENOMINATOR_COUNTEREXAMPLE", "The proposed norm diverges over exact retained modes."),
      link("cannot_decide", "G19", "Failure of this stronger norm does not decide Wilson W6.")], status="falsified")

node(W + "ADJACENT_STRIP_CANCELLATION",
     "The actual adjacent shared-edge Wilson strip has identically zero complete first transported force.",
     "Seven-edge two-plaquette strip, literal source, true ground/marginal and full source-compatible transport.",
     "Electric, source and ground first corrections cancel only in their complete transported sum. The first nonzero force is second order.",
     [source("d", "ADJACENT_STRIP_RESULT.md", "Sections 1-3: actual operator and cancellation", "## 2. The complete first force vanishes"),
      source("d", "operator.md", "Original shared-edge fields"),
      source("d", "source_parity.md", "True-ground and literal-source corrections")], [relevance()])
node(W + "ADJACENT_SECOND_FORCE_BOUND",
     "The adjacent-strip second force satisfies inverse energy<=6561(4-sqrt(15))/5120 times retained energy for every radial finite-energy source.",
     "Actual complete adjacent-strip second coefficient, Gaussian radial source energy, with energy-norm closure and the stated positive shifted interval.",
     "The fast-degree-two force retains the full L_q+2sqrt(5) inverse. Exact matrix-action and Gaussian ladder inequalities prove the all-source estimate; the first excitation has its separate exact inverse-energy formula.",
     [source("d", "ADJACENT_STRIP_RESULT.md", "Sections 4-6, A8-A11", "## 6. Bound over all retained radial energies"),
      source("d", "residual.md", "Complete nonzero second force"),
      source("d", "inverse_synthesis_audit.md", "Independent all-energy synthesis proof")]
     + controls("d", "verify_inverse_synthesis.py", "inverse_synthesis_checks.json"),
     [depends(W + "ADJACENT_STRIP_CANCELLATION", "Identifies second order as the first nonzero coefficient."), relevance()])
node(W + "ALL_STRIP_CANCELLATION",
     "For every finite open strip, H1+[H0,K_n]=-(sum_i grad_i+grad_(n-1)/2).G and vanishes on physical states.",
     "Original-edge open strip of any finite length; complete source-compatible generator, true cubic ground correction and literal outer observation.",
     "The all-n index calculation includes the magnetic commutator and ground/source first-jet matching. It retains the nonreducing three-strip graph. The theorem is an analytic identity, not extrapolation from sampled lengths.",
     [source("t", "STRIP_RESULT.md"), source("t", "geometry.md", "Original-edge fields and all-length index proof"),
      source("t", "source.md", "True-ground/source matching"), source("t", "graph.md", "Nonreducing three-strip graph")]
     + controls("t", "check_general_strip.py", "general_strip_checks.json"), [relevance()])
node(W + "SQUARE_COMPLETE_FIRST_FORCE",
     "The actual square has nonzero complete first force t1 phi=((sqrt(2)-4)/7)(T023+T123) phi prime(a).",
     "Actual twelve-edge 2x2 plaquette block; a=|X2+X3|^2/2, full source-compatible unitary and Gaussian reference source.",
     "Shared-edge electric, coupled ground, literal observation and true marginal corrections are included. The second radial derivative cancels. The force retains one horizontal and two fast excitations in the reducing reference graph.",
     [source("s", "SQUARE_BLOCK_RESULT.md", "Complete first force", "## The square gives an actual nonzero force"),
      source("s", "geometry.md", "Original twelve-edge operator"), source("s", "source.md", "Complete source generator"),
      source("s", "graph.md", "Full cubic inverse and reducing source graph")], [relevance()])
node(W + "SQUARE_SHARP_INVERSE_ENERGY",
     "The square first force has sharp inverse-energy bound (4-sqrt(2))^3/1372 times b, attained by a-3sqrt(2).",
     "Every retained radial finite-energy state of the square Gaussian reference, keeping all three excitation energies in the inverse.",
     "Exact factorization and radial spectral closure prove the bound beyond polynomial probes. The constant is approximately 0.012601546560747265 and the first-excitation inverse energy is (528sqrt(2)-600)/343.",
     [source("s", "SQUARE_BLOCK_RESULT.md", "Sharp bound and first excitation", "## Sharp bound, with no radial-energy cutoff"),
      source("s", "inverse_synthesis.md", "Sharp factorization and all-source closure")]
     + controls("s", "verify_inverse_synthesis.py", "inverse_synthesis_checks.json"),
     [depends(W + "SQUARE_COMPLETE_FIRST_FORCE", "Bounds the complete operator coefficient."), relevance()])
node(W + "SQUARE_ALL_SOURCE_RESIDUAL",
     "The complete square residual coefficient obeys ||rho1 phi||^2<=b/256, inverse energy<=b/512 and <u0,W1u0>=0.",
     "rho1=Q W1 F0^-1 t1 on every retained radial finite-energy source of the actual square reference, with the full source generator.",
     "Keep the horizontal inverse before applying the defect. Gaussian moments, second-radial-derivative cancellation and radial integration by parts give K_res=0.0037824649150914063...<1/256. Parity proves the zero diagonal coefficient.",
     [source("s", "SQUARE_BLOCK_RESULT.md", "Complete residual coefficient", "## Complete defect insertion and all-source bound"),
      source("s", "residual_inverse.md", "Complete defect derivation"),
      source("s", "residual_all_energy.md", "Independent all-energy moment identity and closure")]
     + controls("s", "verify_residual_original_operator.py", "residual_original_operator_checks.json"),
     [depends(W + "SQUARE_SHARP_INVERSE_ENERGY", "Uses the complete reference inverse image."), relevance()])
node(W + "SQUARE_FINITE_G_FLOOR",
     "The actual compact square has physical fast floor F_g>=2I at sufficiently small nonzero g with true quantum vacuum subtraction.",
     "Fixed twelve-edge square; unique magnetic minimum, original-edge uniform ellipticity and physical literal-source complement. The threshold is fixed-block.",
     "Rescaled localization, compactness and min-max prove gap convergence to 2sqrt(2). The fast complement is orthogonal to the true vacuum. Combining this floor with the separate coefficient estimate bounds the leading interacting residual by g^2*b/512 under any unitary fast-space identification.",
     [source("s", "SQUARE_BLOCK_RESULT.md", "Actual finite-g quantum floor", "## Actual finite-g quantum coercivity"),
      source("s", "finite_g_quantum_floor.md", "Localization/min-max and true-vacuum compression proof")],
     [relevance(), link("supported_by", W + "SQUARE_ALL_SOURCE_RESIDUAL", "The independent coefficient estimate combines with this floor to bound the leading residual; it is not a premise of the floor.")])
node(W + "GAUSSIAN_SOURCE_DOMAIN_OBSTRUCTION",
     "The Gaussian quantile source transport is isometric but fails to preserve the full Gaussian energy domain at every fixed positive coupling.",
     "Actual square true quantum marginal; the exhibited centered exponential source has Gaussian b0=1 and infinite transported compact source energy.",
     "Endpoint asymptotics prove the obstruction. A compact Haar quantile chart instead gives a fixed weighted source domain and physical H1 preservation on closed positive-coupling intervals; a dense common core remains for Gaussian normalization.",
     [source("s", "SQUARE_BLOCK_RESULT.md", "Source-domain obstruction and repair", "## Finite-g source domain and precise remaining comparison"),
      source("s", "finite_g_source_domain.md", "Endpoint counterexample and admissible compact chart")]
     + controls("s", "verify_source_domain.py", "source_domain_checks.json"), [relevance()])
node(W + "COMPACT_POSITIVE_REFERENCE_COMPARISON",
     "At a positive compact reference s, the complete finite-coupling selected residual and mixed inverse comparison are bounded for every retained finite-energy source.",
     "Actual fixed square at positive nearby s,t; H1-preserving source/vacuum transport, exact nonreducing J_s and epsilon=M1|t-s|<1 with actual derivative constants.",
     "The full finite difference has residual bound beta*M1^2*epsilon^2*b_s/(1-epsilon), and mixed defect bound beta*M1^3*|t-s|*b_s/(1-epsilon). Cubic Schur remainder and source-energy comparison are included. Its reference/chart is not assumed equal to the Gaussian zero-coupling one.",
     [source("p", "CONTINUATION_RESULT.md", "Complete finite-step theorem", "## Complete finite-coupling residual at a positive compact reference"),
      source("p", "compact_residual.md", "Full compact form, transport and derivative constants")]
     + controls("p", "check_compact_residual.py", "check_compact_residual.json"),
     [depends(W + "GAUSSIAN_SOURCE_DOMAIN_OBSTRUCTION", "Uses the admissible compact chart and respects the Gaussian-domain distinction."), relevance()])
node(W + "SHARED_EDGE_GAUSSIAN_FLOOR",
     "Every open 2m by 2n shared-edge face grid has Gaussian fast floor F_(0,Lambda)>=1/sqrt(2), retaining all oscillator levels and its nonreducing source.",
     "Planar open rectangles retaining each 2x2 block full summed flux vector, then physical invariance. Gaussian tangent model; constants independent of m,n.",
     "C=4I-Adjacency and 2Q_E<=C<=8I. Actual retained directions are C^(1/4)E, not E. Positive-form transfer and second quantization give the floor and inverse norm<=sqrt(2). The interacting finite-g grid floor remains separate.",
     [source("p", "CONTINUATION_RESULT.md", "Shared-edge grid theorem", "## Shared-edge grid floor without a reduction assumption"),
      source("p", "grid_gaussian_floor.md", "Edge decomposition, nonreducing source and second quantization")]
     + controls("p", "grid_verify_gaussian_floor.py", "grid_gaussian_floor_checks.json"), [relevance()])
node(W + "QUANTUM_GROUND_CONCENTRATION",
     "Actual square quantum ground identities give exponential concentration and a bounded differentiated ground after subtracting a source-preserving dilation.",
     "Fixed compact square at small coupling; Delta_E V=48-3V, sum|EV|^2<=16V and rescaled ground energy e_g<=E.",
     "The source proves E_mu exp(V/(2g^2))<=2 exp(2E). Its explicit compact dilation preserves the full outer-trace algebra; the true differentiated-ground equation and weighted elliptic estimates bound both L2 and energy norms of partial_g Psi_g+D Psi_g/g.",
     [source("p", "CONTINUATION_RESULT.md", "Actual ground estimates", "## Actual quantum ground estimates toward zero coupling"),
      source("p", "quantile_scale.md", "Original-edge identities, dilation and differentiated-ground proof")]
     + controls("p", "check_quantile_scale.py", "check_quantile_scale.json"),
     [depends(W + "SQUARE_FINITE_G_FLOOR", "Uses the actual fixed-square quantum gap for differentiated-ground estimates."), relevance()])
node(W + "QUANTUM_FIRST_JET_REMAINDER",
     "The first-corrected Gaussian quasimode approximates the actual square ground in L2 and energy norm with O(g^2) remainder; |e_g-e0|=O(g^2).",
     "Fixed compact square, explicit first correction, original Taylor remainder and actual physical spectral gap.",
     "The true operator and spectral gap control the quasimode remainder rather than assuming a differentiated Gaussian expansion. All-source finite-g residual and growing-volume estimates remain separate.",
     [source("p", "CONTINUATION_RESULT.md", "Actual first-jet remainder", "first-corrected Gaussian quasimode"),
      source("p", "ground_first_jet_remainder.md", "Explicit quasimode, remainder and spectral proof")],
     [depends(W + "SQUARE_FINITE_G_FLOOR", "The actual gap controls the orthogonal quasimode error."), relevance()])
node(W + "QUANTILE_SOURCE_WEIGHT_CRITERION",
     "The actual conditional-frame variance satisfies integral K_g |f-nu_g f|^2 <= (8B_g+4 Kbar_g/gamma)b_g[f].",
     "Actual compact source form domain; K_g is conditional score variance after dilation, v_g=g^2(1-w^2)rho_g and B_g the explicit median tail-resistance supremum.",
     "Coarse Poincare, median decomposition and weighted Hardy prove the estimate without an essential-supremum assumption on K_g. Kbar_g is already bounded. A uniform B_g estimate remains the next all-source input.",
     [source("p", "CONTINUATION_RESULT.md", "Next uniform estimate", "## Precise next uniform estimate"),
      source("p", "quantile_source_weight.md", "W1-W8: actual weights, median/Hardy proof and B_g obligation")],
     [depends(W + "QUANTUM_GROUND_CONCENTRATION", "Supplies bounded average score variance after dilation."),
      depends(W + "SQUARE_FINITE_G_FLOOR", "Supplies the actual coarse Poincare inequality."), relevance()])
node(R + "W6_UNIFORM_INTERACTING_TRANSFER",
     "Bound the complete all-source small-coupling residual and derivative constants, establish the interacting growing-grid floor, and retain accumulated source-energy growth.",
     "Actual transported coupled Wilson family on admissible source domains; required backgrounds/shifts and uniformity in small coupling and growing volume.",
     "The fixed-square floor and first residual coefficient, positive-reference full comparison, uniform Gaussian grid floor and true-ground estimates are established inputs with distinct scopes. Uniform B_g, complete zero-reference remainder and interacting volume transfer remain open. The positive-reference budget keeps source-energy growth explicitly.",
     [source("p", "CONTINUATION_RESULT.md", "Precise remaining uniform transfer", "The uniform bound on B_g is not yet proved."),
      source("p", "positive_reference_budget.md", "Accumulated derivative-scaling and source-energy budget"),
      source("s", "SQUARE_BLOCK_RESULT.md", "Complete finite-g residual beyond its coefficient", "The remaining comparison is explicit:")],
     [depends(W + "RESIDUAL_CRITERION", "Sufficient selected inverse implication once its uniform estimates hold."),
      depends(W + "SQUARE_ALL_SOURCE_RESIDUAL", "Complete fixed-square first residual coefficient."),
      depends(W + "COMPACT_POSITIVE_REFERENCE_COMPARISON", "Actual finite-coupling comparisons away from zero."),
      depends(W + "SHARED_EDGE_GAUSSIAN_FLOOR", "Volume-uniform Gaussian reference floor."),
      depends(W + "QUANTUM_FIRST_JET_REMAINDER", "Actual fixed-square ground remainder."),
      depends(W + "QUANTILE_SOURCE_WEIGHT_CRITERION", "Reduces conditional-frame control to the explicit weighted tail-resistance bound."), relevance()], status="open")


NATIVE_SUPPORT = {
    "RESULT:RECENT_ANISOTROPY_VARIANCE_CORE": [
        (
            "supported_by",
            "CHK:anisotropy-variance-full-kernel-mixing-a-f83a4a:anisotropy-variance-is-exactly-the-simpl-e46297",
            "T1 checks the simplex variance and cubic-shape polynomial identities exactly; the full kernel identification is a separate check.",
        ),
        (
            "supported_by",
            "CHK:anisotropy-variance-full-kernel-mixing-a-f83a4a:anisotropy-mixing-residual-matches-the-f-b94f9b",
            "T1 checks the complete assembled Laurent residual identity exactly for the recorded coefficients; the normalized carrier statement uses q>0.",
        ),
        (
            "bears_on",
            "CHK:the-feshbach-channel-of-the-plaquette-ho-ef662f:neither-hodge-generator-leaves-the-carri-e60007",
            "Checks the carrier-preserving Hodge terms behind the residual decomposition; this related algebra is not independently the complete variance identity.",
        ),
    ],
    "RESULT:RECENT_ANISOTROPY_INDUCED_SIXTH": [
        (
            "supported_by",
            "CHK:anisotropy-variance-full-kernel-mixing-a-f83a4a:anisotropy-induced-sixth-order-coefficie-cd3d47",
            "T1 checks the exact rational coefficient -4*C^2/t3. The complete sixth-order Hamiltonian remains a separate calculation.",
        ),
        (
            "bears_on",
            "CHK:the-feshbach-channel-of-the-plaquette-ho-ef662f:two-r-insertions-unlock-the-l-4-tier-loc-87173c",
            "Checks the related sigma(RR)=q*e2+3*e3 algebra. This alone does not establish the complete 1:3:-4 induced-energy combination or its dynamical occurrence.",
        ),
    ],
    "RESULT:RECENT_ANISOTROPY_OVERLAP_ENERGY": [
        (
            "supported_by",
            "CHK:anisotropy-variance-full-kernel-mixing-a-f83a4a:anisotropy-finite-order-overlap-and-ener-e339a1",
            "T2 finite spectral probes support application of the analytic inequalities to the displayed truncated matrix; they do not prove the full analytic quantifiers or physical source overlap.",
        ),
    ],
    "RESULT:W6_RESIDUAL_VARIATIONAL_IDENTITY": [
        (
            "bears_on",
            "CHK:the-feshbach-resolvent-comparison:the-interacting-inverse-image-cancels--a-ab8923",
            "Checks the companion mixed-resolvent collapse on exact finite rational fixtures. It does not certify the full weak-form residual identity or its operator-domain hypotheses.",
        ),
    ],
}
for item in NODES:
    for kind, target, detail in NATIVE_SUPPORT.get(item["id"], []):
        item["links"].append(link(kind, target, detail))


registry = {
    "schema": "recent-research/v1",
    "title": "September 8-9 standalone research: exact results, analytic consequences and open W6 transfer",
    "source_scope": (
        "Nine campaigns: anisotropy variance and eight W6 continuations. "
        "Each statement retains its proof scope. Source identity does not imply "
        "a fresh replay or full-statement native formalization."
    ),
    "sources": sorted(SOURCES.values(), key=lambda item: item["id"]),
    "nodes": NODES,
}
save(REPO / "ledger/recent_research.yaml", yaml.safe_dump(
    registry, sort_keys=False, allow_unicode=True, width=100).encode("utf-8"))
manifest = {
    "schema": "recent-research-source-preservation/v1",
    "original_root": ORIGINAL.as_posix(),
    "source_files_modified": 0,
    "source_count": len(SOURCES),
    "sources": registry["sources"],
}
save(BUNDLE / "SOURCE_MANIFEST.json", (json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
save(BUNDLE / "SHA256SUMS", "".join(
    item["sha256"] + "  " + Path(item["path"]).relative_to(BUNDLE.relative_to(REPO)).as_posix() + "\n"
    for item in registry["sources"]
).encode("utf-8"))
print(json.dumps({"results_and_routes": len(NODES), "sources": len(SOURCES), "campaigns": len(CAMPAIGNS)}))
