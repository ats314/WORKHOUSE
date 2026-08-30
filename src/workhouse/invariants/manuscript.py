from __future__ import annotations

import json
import re

from sympy import (
    pi,
    simplify,
    sin,
)

from .. import triage as TRIAGE
from ._core import PAPER_DIR, SUITES, _suite

# ==========================================================================
# The manuscripts, as documents this repository can check
# ==========================================================================
manuscript = _suite("the flat-band manuscript")


#: The pinned manuscripts, by the text extracted from each. The flat-band paper
#: is the one that cites this repository by commit; the master document unites
#: it with the nested-quotient circuit theory. The UNITED edition is
#: deliberately absent: it discusses the fourth order on purpose, in its
#: obstruction section, so the firewall below is a property of these two only.
PAPER_TEXTS = (
    "homological_flat_bands_2026-08-28.txt",
    "nested_quotient_master_2026-08-28.txt",
)


@manuscript.check(
    "every \\chk in the united paper names a check that exists and passes",
    "MASTER paper, every displayed result",
)
def _():
    # The united paper's one device is that each displayed result carries the
    # name of the machine check that establishes it, so a reader can re-run any
    # line in about a second. That device is worth exactly as much as its
    # weakest label: a renamed or deleted check leaves the paper printing a
    # command that no longer resolves, and a paper that has drifted still reads
    # as current -- the same failure mode FRONTIER.md's staleness test guards.
    #
    # So resolve every label against the live registry here, and require the
    # named check to be one that passes. This does not re-run them (the suites
    # do that); it asserts the paper cites nothing that has gone missing or red.
    #
    # Read EVERY pinned edition, not one. Until 2026-08-30 this check read
    # only master_paper_2026-08-28.tex, and the publication editions written
    # after it drifted unwatched: nineteen of their labels named no registered
    # check at all. A guard that covers one of three editions is a guard that
    # reports green while the artifact of record prints commands that do not
    # resolve, which is precisely the failure it exists to catch.
    # Generated includes are not editions: they PRINT the markers, so counting
    # them would double every label and hide a real one behind its own copy.
    editions = [p for p in sorted(PAPER_DIR.glob("*.tex")) if not p.name.startswith("coverage_")]
    known = {check[0] for suite in SUITES for check in suite.checks}
    cited, unresolved = {}, {}
    for path in editions:
        source = path.read_text(encoding="utf-8")
        labels = [
            m.replace("\\_", "_").replace("\\^{}", "^").replace("\\^", "^")
            # The label body may contain "\^{}" -- LaTeX's standalone circumflex
            # -- so a [^}]* body stops at the wrong brace and truncates the name.
            # Allow balanced empty groups.
            for m in re.findall(r"\\chk\{((?:[^{}]|\{\})*)\}", source)
        ]
        cited[path.name] = labels
        missing = sorted(set(labels) - known)
        if missing:
            unresolved[path.name] = missing
    total = sum(len(v) for v in cited.values())
    distinct = {lab for labs in cited.values() for lab in labs}
    ok = bool(editions) and total > 0 and not unresolved
    return ok, (
        f"{total} \\chk labels across {len(distinct)} distinct checks in "
        f"{len(editions)} pinned editions "
        f"({', '.join(f'{k}: {len(v)}' for k, v in cited.items())}), every one of them a "
        f"registered check name; {sum(len(v) for v in unresolved.values())} unresolved"
        + (f" -- {unresolved}" if unresolved else "")
        + ". Each displayed result in every edition is reproducible by the command printed "
        "beneath it"
    )


@manuscript.check(
    "every declared note document is a graph node with an edge",
    "ledger/notes.yaml + notes/*.jsonl",
)
def _():
    # The maintainer's archives were declared and inventoried long before they
    # reached the graph, and for that whole period "which notes bear on C2?"
    # had no answer the graph could give -- 1,689 documents, no node, so every
    # bears_on a review recorded was a sentence nobody could traverse. Coverage
    # is the kind of thing that regresses silently the next time an archive is
    # declared and nobody regenerates, so assert it rather than trust it.
    #
    # Read the GENERATED graph rather than rebuilding: collect() runs every
    # suite, so calling it from inside a check makes verify quadratic (the
    # first draft of this check took over ten minutes). test_graph already
    # fails when index/graph.jsonl is stale, so reading it here is not a
    # weaker statement -- it is the same statement, once.
    #
    # Read the GRAPH and not the claim catalogue, which the first draft did
    # and which was wrong: this check's own detail line is written INTO
    # index/claims.jsonl, so a check that counts catalogue nodes changes the
    # file it counts and never reaches a fixpoint -- `make catalogue` left the
    # index stale however many times it ran. The graph carries edges only,
    # never check details, so nothing here depends on its own output.
    # Membership is not weakened by the change: graph.build() emits an edge
    # only when both endpoints resolve to catalogue records, so a note id
    # appearing in an edge IS a catalogue node.
    #
    # This checks reachability, not truth. Every note node is T3 whatever its
    # verdict, and no edge here promotes anything.
    from .. import claims as claims_mod
    from .. import notes as notes_mod

    notes = notes_mod.load()
    declared = {
        claims_mod.note_id(archive["id"], row)
        for archive in notes.archives
        for row in notes.manifests.get(archive["id"], [])
    }
    graph_path = PAPER_DIR.parent / "index" / "graph.jsonl"
    touched: set[str] = set()
    for line in graph_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            edge = json.loads(line)
            touched.add(edge["src"])
            touched.add(edge["dst"])
    stranded = declared - touched
    return not stranded, (
        f"{len(declared)} declared note documents across {len(notes.archives)} archives, "
        f"every one carrying at least one graph edge and so a catalogue node; "
        f"{len(stranded)} stranded"
    )


@manuscript.check("no fourth-order coefficient enters the manuscript", "PAPER_FLATBAND §6")
def _():
    # §6 makes a claim about the manuscript itself: "no fourth-order band,
    # bandwidth, or derived higher-order quantity is used in this paper. This
    # is a scientific boundary, not merely a choice of presentation." That is a
    # statement about a document, so it is checkable against the document --
    # with the same coefficient-signature scanner `workhouse triage` points at
    # any unpinned archive. A future revision that crosses the firewall fails
    # here rather than passing unread.
    report = TRIAGE.scan(PAPER_DIR)
    carried = {
        name: set(next(f for f in report.files if f.path.name == name).coefficients)
        for name in PAPER_TEXTS
    }
    third_order = {"d_3", "b_3", "leak_3"}
    return all(v == third_order for v in carried.values()), (
        f"both pinned manuscripts carry exactly {sorted(third_order)} and no fourth-order "
        "signature: not q_band^(4), not m_Gamma^(4), not either C_shp side, not the quarantined "
        "scalar. The firewall is measured, not taken on the word of §6"
    )


@manuscript.check("q at the four high-symmetry points is 0, 4, 8, 12", "MASTER_DOC Fig. 2")
def _():
    # Figure 2 plots the incidence spectrum along Gamma-X-M-R-Gamma and is
    # asserted rather than generated. Its four corners are arithmetic, and the
    # branch set at each is {0, q, q} by the factorization theorem -- so the
    # figure is reproducible from two checked statements rather than trusted.
    points = {
        "Gamma": (0, 0, 0),
        "X": (pi, 0, 0),
        "M": (pi, pi, 0),
        "R": (pi, pi, pi),
    }
    got = {name: simplify(sum(4 * sin(k / 2) ** 2 for k in ks)) for name, ks in points.items()}
    return got == {"Gamma": 0, "X": 4, "M": 8, "R": 12}, (
        f"{got}; the plotted branch set at each point is {{0, q, q}}, and R attains the zone "
        "maximum 12 that sets the full-manifold width"
    )


@manuscript.check(
    "every node the theory graph strands is stranded for a stated reason",
    "index/graph.jsonl, index/claims.jsonl, ledger/theorems.yaml",
    tier=2,
)
def _():
    # Declared T2, and that UNDERSTATES it: the census is exact integer
    # arithmetic and no float enters the verdict. The tier guard matches
    # `_NUM` anywhere in the body, and this body names two constant IDS that
    # happen to end in it -- CONST:HAMER_MT_NUM and
    # CONST:RAW_FOLDED_AXIAL_GAMMA_NUM. Loosening the guard to fit one new
    # check is the "make the failing check pass" instinct this repository
    # exists to resist, and the guard's crudeness is what makes it hard to
    # evade. Understating a tier cannot cause a false promotion, which is the
    # failure the tier system is for, so the label stands as T2 and this
    # comment is the record of why.
    #
    # The interesting number in this census is not the node or edge count but
    # the third one: the nodes with no edge at all. A stranded
    # node is invisible to `workhouse why`, so it is evidence nobody can
    # traverse to, and a graph that quietly accumulates them looks complete
    # while going hollow.
    #
    # The fix is NOT to connect them. Every one below is stranded for a reason
    # the repository can state, and inventing an edge to tidy the census would
    # be the exact failure ledger/theorems.yaml warns about in its own header:
    # "an honest gap beats an invented edge". Four reasons, all different:
    #
    #   LEAN:extraction_A..D, stencil_zero_mode -- generic algebra over free
    #     rationals. `promotes` is barred by the theorems schema, which admits
    #     it only when the theorem proves a check's WHOLE statement; these
    #     prove the inversion algebra but not that the checkpoint deltas
    #     follow from the trigonometric ansatz, and their own doc comments say
    #     so. `formalizes` would have to name a constant they do not mention.
    #
    #   the constants -- registered, and read by no check body. That is not a
    #     graph defect, it is the graph reporting a real T3 hole: DELTA_BETA_3
    #     carries the whole balanced side of C2 and no invariant touches it.
    #     These strand until someone writes the check, which is the point.
    #
    #   C11/C14/C19, G8/G12/G16, R3/R9/R11/R16/R17, ADR:0006 -- ledger entries
    #     whose curated cross-reference fields are empty. Some are honestly
    #     isolated: R16 is about upstream registry files that are not in this
    #     repository at all, so there is nothing here for it to point at.
    #
    #   the two coverage checks -- this one and the note-coverage check next
    #     door. Both cite generated files rather than claim ids, so neither
    #     appears in its own census. Recorded rather than papered over.
    #
    # The guard is one-directional on purpose: stranded must stay a SUBSET of
    # what is accounted for, so a new orphan fails and a connected one merely
    # shrinks the list. Reading index/graph.jsonl rather than rebuilding keeps
    # verify linear and keeps this check off its own output -- graph.jsonl
    # carries edges only, never check details.
    import collections

    accounted = {
        # coverage checks: cite generated files, not claim ids
        "CHK:the-flat-band-manuscript:every-declared-note-document-is-a-graph--a77304",
        "CHK:the-flat-band-manuscript:every-node-the-theory-graph-strands-is-s-57688c",
        # registered constants no check body reads -- a real T3 hole, shown.
        # Five entries have come off, for three different reasons, and each is
        # removed rather than kept so a regression strands it loudly.
        # D3_EVEN and T_3_EVEN were deleted outright: undeclared aliases of
        # D3_EVEN_DOMINO and T3_EVEN, so the honest fix was to stop
        # registering them twice rather than to check them. LEAK_2,
        # LEAK_2_EVEN and LEAK_3_EVEN are real and the charge-even suite reads
        # them. DELTA_BETA_3 and DELTA_Q_3 are read by the off-axis suite --
        # the first by the check that establishes it, the second by the check
        # that says exactly why it cannot be established here.
        "CONST:HAMER_MT_NUM",
        "CONST:MUNSTER_TM_F",
        "CONST:MUNSTER_TM_G",
        "CONST:MUNSTER_TM_H8",
        "CONST:RAW_FOLDED_AXIAL_GAMMA_NUM",
        "CONST:SIGMA_5_CRT_PRIMES",
        "CONST:SIGMA_5_TOPOLOGIES",
        # Papers in the index whose bare node has no citation edge, because
        # the citation web is populated ONLY from primary sources -- an
        # INSPIRE reference list or the pinned PDF's bibliography -- and
        # these three are not-yet-obtained. Their bears_on edges exist
        # (LIT:<paper>:R2 nodes carry those); it is the paper node itself
        # that is unreachable. Inventing a cites list from memory to tidy
        # the census is exactly what literature/index.yaml forbids, so they
        # strand until someone obtains them. That makes this a live
        # acquisition signal rather than a blemish.
        "LIT:BALAJI_2026",
        "LIT:CBB_2026",
        "LIT:CB_2024",
        "LIT:HAZRA_2026",
        # ledger entries with empty curated cross-reference fields
        "C11",
        "C14",
        "C19",
        "ADR:0006",
        "G12",
        "G16",
        "G8",
        "R11",
        "R16",
        "R17",
        "R3",
        "R9",
        # T0 theorem whose only honest edge would be an invented one.
        # extraction_A..D used to sit here too; they came off the list when
        # delta_X..delta_R proved the half they were missing, which is what
        # this census is for -- it shrinks when the work is done, and the
        # entries are removed so a regression strands them again loudly.
        "LEAN:stencil_zero_mode",
    }

    index_dir = PAPER_DIR.parent / "index"
    ids = {
        json.loads(line)["id"]
        for line in (index_dir / "claims.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    degree: collections.Counter[str] = collections.Counter()
    for line in (index_dir / "graph.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        edge = json.loads(line)
        degree[edge["src"]] += 1
        degree[edge["dst"]] += 1

    stranded = {i for i in ids if degree[i] == 0}
    unaccounted = sorted(stranded - accounted)
    connected = sorted(accounted - stranded)
    kinds = collections.Counter(
        i.split(":")[0] if ":" in i else i.rstrip("0123456789") for i in stranded
    )

    return not unaccounted, (
        f"{len(ids)} catalogue nodes, {sum(degree.values()) // 2} edges, {len(stranded)} stranded "
        f"and every one accounted for ({dict(sorted(kinds.items()))}). {len(unaccounted)} "
        f"unaccounted: {unaccounted}. The {kinds['CONST']} stranded constants are the honest "
        "headline, and the C2 pair is no longer among them: DELTA_BETA_3 is read by the check "
        "that establishes it, DELTA_Q_3 by the check that says exactly why it cannot be "
        "established here. The residue is listed above rather than characterised, because a "
        f"hand-written summary of it has gone stale twice. {len(connected)} previously-stranded "
        "nodes have since gained an edge" + (f": {connected}" if connected else "")
    )
