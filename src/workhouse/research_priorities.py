"""Current derivation routes, distinct from necessary gap dependencies.

The selected order is authored in gaps.yaml. Only explicit ``blocked_by``
inputs govern readiness within that route. Neither relevance, a verification
tier nor missing Lean coverage makes a mathematical blocker.
"""

from __future__ import annotations

from . import derivation_statements, ledger, recent_research, results

ESTABLISHED = frozenset({"proven", "resolved", "discharged", "done"})
RETIRED = frozenset({"falsified", "superseded", "dead"})


def live_statuses(led: ledger.Ledgers) -> dict[str, str]:
    """Read authored truth/lifecycle status, never infer it from machine tier.

    Read live source registers rather than yesterday's generated catalogue.
    This intentionally does not collect checks or recurse into the graph.
    """
    from .claims import route_id

    statuses = {g["id"]: g["state"] for g in led.gaps}
    statuses.update({c["id"]: c["status"] for c in led.contradictions})
    statuses.update({r["id"]: r["status"] for r in results.load()})
    statuses.update({r["id"]: r["status"] for r in recent_research.load().nodes})
    for doc in derivation_statements.load()["documents"]:
        statuses.update({r["id"]: r["status"] for r in doc["statements"]})
    for gap in led.gaps:
        for step in gap.get("plan", []) or []:
            statuses[route_id(gap["id"], step["step"])] = step["state"]
    return statuses


def collect(led: ledger.Ledgers, statuses: dict[str, str] | None = None) -> list[dict]:
    """Return active selected routes with explicit unresolved completion inputs.

    ``ready`` means no recorded blocking input; it is not a feasibility claim.
    A conditional implication can be an available theorem while its actual
    model hypotheses remain open. Authors name those hypotheses separately.
    """
    from .claims import route_id

    statuses = live_statuses(led) if statuses is None else statuses
    out = []
    for gap in led.open_gaps:
        for step in gap.get("plan", []) or []:
            focus = step.get("frontier")
            if not focus or step["state"] not in {"live", "untried"}:
                continue
            target = focus.get("target")
            target_status = statuses.get(target, "unregistered") if target else None
            if target_status in ESTABLISHED | RETIRED:
                continue
            pending = [
                ref for ref in step.get("blocked_by", []) if statuses.get(ref) not in ESTABLISHED
            ]
            if target and target_status == "unregistered" and target not in pending:
                pending.append(target)
            invalid_inputs = [
                ref
                for ref in step.get("depends_on", [])
                if statuses.get(ref) in RETIRED
                or (ref.startswith(("RESULT:", "DERIV:", "ROUTE:")) and ref not in statuses)
            ]
            pending.extend(ref for ref in invalid_inputs if ref not in pending)
            out.append(
                {
                    **focus,
                    "id": route_id(gap["id"], step["step"]),
                    "gap": gap["id"],
                    "step": step["step"],
                    "state": step["state"],
                    "target_status": target_status,
                    "inputs": list(step.get("depends_on", [])),
                    "input_status": {
                        ref: statuses.get(ref, "source reference")
                        for ref in step.get("depends_on", [])
                    },
                    "invalid_inputs": invalid_inputs,
                    "pending": pending,
                    "pending_status": {ref: statuses.get(ref, "unregistered") for ref in pending},
                    "bears_on": list(step.get("bears_on", [])),
                    "ready": not pending,
                }
            )
    return sorted(out, key=lambda row: (row["priority"], row["id"]))


def detail(step: dict) -> str:
    """Keep exact objectives and tests visible in catalogue/search/why output."""
    parts = [" ".join(str(step.get("status", "")).split())]
    focus = step.get("frontier")
    if focus:
        parts.append(
            f"Research priority: {focus['priority']} (curated order, not a proof dependency)."
        )
        for field in ("target", "scope", "consequence", "decisive_test"):
            if field in focus:
                parts.append(f"{field.replace('_', ' ').capitalize()}: {focus[field]}")
    for field in ("depends_on", "blocked_by", "bears_on"):
        if step.get(field):
            parts.append(f"{field}: {', '.join(step[field])}")
    return "\n".join(part for part in parts if part)
