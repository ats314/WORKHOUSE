"""Claims and symbols as machine-readable records.

Two files, both generated into ``index/``:

* ``claims.jsonl`` -- one record per claim this repository can point at: every
  invariant check, every registered constant, every ledger entry, every
  literature edge.
* ``symbols.jsonl`` -- the curated aliases from ``ledger/symbols.yaml``, joined
  to the claims that mention them.

**Nothing here is authored at generation time.** Every field is copied from a
curated source: a check's own name and detail line, a ``Constant``'s note and
provenance, a ledger entry's text. There is deliberately no ``summary`` or
``topics`` field, because a generated one-line gloss of a claim nobody wrote is
a place for an error to enter that no test can catch -- and it would then read
like an index rather than like a guess.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Any

import yaml

from . import constants as K
from . import ledger as ledger_mod
from . import literature as literature_mod
from .invariants import SUITES

ROOT = Path(__file__).resolve().parents[2]
INDEX_DIR = ROOT / "index"
CLAIMS = INDEX_DIR / "claims.jsonl"
SYMBOLS = INDEX_DIR / "symbols.jsonl"
SYMBOL_SOURCE = ROOT / "ledger" / "symbols.yaml"

KINDS = ("check", "constant", "contradiction", "gap", "register", "unifying", "paper")


@dataclass
class Claim:
    id: str
    kind: str
    #: The claim in the words of whoever curated it. Never generated here.
    statement: str
    #: 0-3, or None where the record is not a verification claim at all.
    tier: int | None = None
    #: Exact value as "p/q" where the claim has one, else the float's repr.
    value: str | None = None
    #: Float form, so a search by decimal prefix can reach it.
    decimal: float | None = None
    where: str = ""
    cites: str = ""
    reproduce: str = ""
    status: str = ""
    evidence: str = ""
    detail: str = ""
    related: list[str] = field(default_factory=list)


def _as_value(value: Any) -> tuple[str | None, float | None]:
    """Exact string and float form, keeping the exact/float distinction visible.

    A sympy Rational renders as "p/q"; a float renders as its repr. The two are
    never merged, because a float that reads as exact is the most dangerous bug
    in this repository.
    """
    if value is None:
        return None, None
    try:
        if hasattr(value, "p") and hasattr(value, "q"):  # sympy Rational
            return f"{value.p}/{value.q}", float(value)
        if isinstance(value, Fraction):
            return f"{value.numerator}/{value.denominator}", float(value)
        if isinstance(value, float):
            return repr(value), value
        if isinstance(value, int):
            return str(value), float(value)
        if getattr(value, "free_symbols", None):
            return str(value), None  # symbolic in N or L; no single float
        return str(value), float(value)
    except (TypeError, ValueError):
        return str(value), None


def _slug(text: str) -> str:
    keep = [c if c.isalnum() else "-" for c in text.lower()]
    return "".join(keep).strip("-").replace("--", "-")[:40]


def collect() -> list[Claim]:
    out: list[Claim] = []

    for suite in SUITES:
        for result in suite.run():
            out.append(
                Claim(
                    id=f"CHK:{_slug(suite.name)}:{_slug(result.name)}",
                    kind="check",
                    statement=result.name,
                    tier=result.tier,
                    where=f"src/workhouse/invariants.py:{result.line}",
                    cites=result.section,
                    reproduce=f"workhouse verify --only {result.name!r}",
                    detail=result.detail,
                    status="passing" if result.passed else "FAILING",
                )
            )

    for constant in K.REGISTRY:
        exact, decimal = _as_value(constant.value)
        out.append(
            Claim(
                id=f"CONST:{constant.name}",
                kind="constant",
                statement=constant.note or constant.name,
                # A registered constant is T3 on its own: the registry records
                # what the corpus says. Whatever checks it supplies the tier.
                tier=3,
                value=exact,
                decimal=decimal,
                where="src/workhouse/constants.py",
                cites=constant.source,
                status=constant.status,
                evidence=constant.evidence,
            )
        )

    # Module-level constants that REGISTRY does not curate. They carry no
    # status, evidence, or note -- which is exactly the point of recording them:
    # a name that search must reach, and a provenance gap someone should close.
    curated = {c.name for c in K.REGISTRY}
    for name in sorted(n for n in dir(K) if n.isupper() and not n.startswith("_")):
        if name in curated:
            continue
        raw = getattr(K, name)
        # Sets are closed vocabularies, not values, and their repr ordering is
        # not stable across runs -- which would make this file spuriously
        # "stale" on every regeneration.
        if isinstance(raw, (set, frozenset, dict, str)):
            continue
        if isinstance(raw, tuple):
            parts = [_as_value(v)[0] for v in raw]
            if any(part is None for part in parts):
                continue
            exact, decimal = ", ".join(parts), None
        else:
            exact, decimal = _as_value(raw)
        if exact is None:
            continue
        out.append(
            Claim(
                id=f"CONST:{name}",
                kind="constant",
                statement=name,
                tier=3,
                value=exact,
                decimal=decimal,
                where="src/workhouse/constants.py",
                status="module-level, not in REGISTRY",
            )
        )

    led = ledger_mod.load()
    for entry in led.contradictions:
        out.append(
            Claim(
                id=entry["id"],
                kind="contradiction",
                statement=entry["title"],
                tier=3,
                where="ledger/contradictions.yaml",
                cites=entry.get("section", ""),
                status=entry["status"],
                detail=" ".join(str(entry.get("resolution", "")).split()),
                related=sorted(entry.get("blocks", [])),
            )
        )
    for entry in led.gaps:
        out.append(
            Claim(
                id=entry["id"],
                kind="gap",
                statement=entry["title"],
                tier=3,
                where="ledger/gaps.yaml",
                status=f"tier {entry['tier']}"
                + (" load-bearing" if entry.get("load_bearing") else ""),
                detail=" ".join(str(entry.get("detail", "")).split()),
                related=sorted(entry.get("resolves", []) + entry.get("unblocks", [])),
            )
        )
    for entry in led.register:
        out.append(
            Claim(
                id=entry["id"],
                kind="register",
                statement=entry["title"],
                tier=3,
                where="ledger/governing_register.yaml",
                cites="MASTER_THEORY_UNIFIED v4.3 §14",
                detail=" ".join(str(entry["text"]).split()),
                related=sorted(entry["contradictions"] + entry["gaps"]),
            )
        )
    for entry in led.unifying_candidates:
        out.append(
            Claim(
                id=entry["id"],
                kind="unifying",
                statement=" ".join(str(entry["statement"]).split()),
                tier=3,
                where="ledger/gaps.yaml",
                status=entry["status"],
                detail="FALSIFIER: " + " ".join(str(entry["falsifier"]).split()),
                related=sorted(entry.get("supported_by", [])),
            )
        )

    for paper in literature_mod.load().papers:
        for edge in paper.get("bears_on", []):
            out.append(
                Claim(
                    id=f"LIT:{paper['id']}:{edge['target']}",
                    kind="paper",
                    statement=(
                        f"{paper['title']} ({paper['year']}) {edge['relation']} {edge['target']}"
                    ),
                    tier=3,
                    where="literature/index.yaml",
                    cites=paper.get("doi") or paper.get("arxiv") or "",
                    status=edge["status"],
                    detail=" ".join(str(edge["detail"]).split()),
                    related=[edge["target"]],
                )
            )

    return out


def load_symbols(path: Path | None = None) -> list[dict[str, Any]]:
    return yaml.safe_load((path or SYMBOL_SOURCE).read_text())["symbols"]


def symbol_records(claims: list[Claim] | None = None) -> list[dict[str, Any]]:
    """Curated aliases, joined to the claims that name them."""
    claims = claims if claims is not None else collect()
    records = []
    for symbol in load_symbols():
        haystacks = {
            symbol["canonical"],
            *symbol.get("code_names", []),
            *symbol.get("corpus_spellings", []),
        }
        mentions = sorted(
            c.id for c in claims if any(h and h in f"{c.statement} {c.detail}" for h in haystacks)
        )
        record = dict(symbol)
        record["mentioned_by"] = mentions
        record["search_keys"] = sorted(
            {
                *haystacks,
                *symbol.get("values", []),
                symbol["id"],
            }
        )
        records.append(record)
    return records


def write(directory: Path | None = None) -> tuple[Path, Path]:
    target = directory or INDEX_DIR
    target.mkdir(parents=True, exist_ok=True)
    claims = collect()
    (target / "claims.jsonl").write_text(
        "".join(json.dumps(asdict(c), sort_keys=True) + "\n" for c in claims)
    )
    (target / "symbols.jsonl").write_text(
        "".join(json.dumps(s, sort_keys=True) + "\n" for s in symbol_records(claims))
    )
    return target / "claims.jsonl", target / "symbols.jsonl"
