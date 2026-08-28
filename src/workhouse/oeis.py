"""The OEIS as an external witness, offline, by value, with the odds computed.

This corpus's coefficient families are integer sequences, and the OEIS is the
one external index that can be joined to them **by value** rather than by
concept -- the same join key this repository already uses everywhere else. A
match would connect a coefficient computed here to combinatorics computed by
people who had never heard of this program, which is what ``AGENTS.md`` means
by an independent result.

Three decisions make that join honest rather than decorative.

**Offline, against the official distribution.** ``oeis.org/robots.txt`` says
``Disallow: /search`` with ``Crawl-Delay: 10``, so this module never queries the
search endpoint -- not with a custom user agent, not slowly. It uses
``oeis.org/stripped.gz``, the maintainers' own published dump of every sequence
and its terms, fetched once. That is also better science: the search API shows
ten results and no total, while the dump gives the *exact* number of matching
sequences among all ~400,000 -- which is the only number the verdict depends on.

**The null model is measured, not assumed.** "It's in the OEIS" is worth
nothing until you know how many things are. A sequence of small integers
matches thousands of entries; ``1,2,6`` matched 8,399 when this was written.
So each query carries an expected-by-chance count from a unigram model built
from the dump itself: if value ``v`` occupies a fraction ``f(v)`` of all term
slots, then ``E = W * prod f(v_i)`` windows are expected to match ``k`` terms by
coincidence, where ``W`` is the number of term windows in the dump. A hit is
evidence only when ``E`` is small and the observed count is 1. The model is
checked against the observed counts along the whole prefix curve
(``oeis-null-model-tracks-observed``), because a null model nobody has tested
is another assertion.

**A closed form is not a discovery.** Most families here are rational functions
of the rank ``N``, and the OEIS contains polynomial families without number. A
hit on one identifies a *normalisation*, not a mechanism, so every entry in
``ledger/sequences.yaml`` declares ``generated_by``, and hits on a
``closed-form-in-N`` sequence are recorded with their verdict fixed at
``not-evidence`` however striking they look. Only ``census-output`` sequences --
ones whose terms came out of an enumeration nobody could have written down in
advance -- can carry a hit that means anything.

Nothing here promotes anything. A match becomes an ``OEIS:A######`` node with a
``matches`` edge to the sequence it matched; the sequence's own ``bears_on``
edges are what reach the claims. Both node kinds are T3, like every other
document node, and the verdict rides on the node rather than deciding whether
it exists -- a ``not-evidence`` match is still a match.
"""

from __future__ import annotations

import gzip
import hashlib
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import yaml

from . import constants as K

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "ledger" / "sequences.yaml"
#: Where ``--fetch`` puts the dump. Gitignored: 32 MB, and redistributing the
#: OEIS is the maintainers' call, not ours. The digest of the snapshot actually
#: used is recorded in the registry, so a scan stays reproducible without it.
SNAPSHOT = ROOT / "literature" / "oeis" / "stripped.gz"
SNAPSHOT_URL = "https://oeis.org/stripped.gz"
#: Sent when fetching the dump, and only then. oeis.org's front cache returns
#: 403 to the default ``Python-urllib`` string while serving the identical file
#: to any browser and to curl; identifying as a normal client is ordinary
#: client behaviour, not circumvention, and it is the same call
#: ``acquisition.py`` already made for the KEK preprint scans. It is NOT a way
#: past robots.txt: the disallowed path (``/search``) is not requested at all,
#: at any user agent.
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) workhouse-oeis"

#: Fewest terms that make something a sequence at all. Not the evidence gate --
#: that is the measured chance count below, which is strictly more informative
#: than a term count and gets the five-term sigma family right where a floor of
#: six would have thrown away a match on two twenty-digit integers.
MIN_TERMS = 3

#: How far the unigram null model below UNDERSTATES the chance of a match, as
#: measured against the snapshot on nine controls -- seven sequences the OEIS
#: certainly contains and two irregular decoys it certainly does not. The table
#: is recorded under `null_model_controls` in ledger/sequences.yaml:
#:
#:     catalan (k=5)      273 observed / 8.8e-01 predicted    ratio 3.1e+02
#:     catalan8 (k=8)      23 observed / 2.3e-10 predicted    ratio 1.0e+11
#:     factorial (k=5)    434 observed / 1.1e-02 predicted    ratio 4.1e+04
#:     primes (k=6)       597 observed / 6.8e-04 predicted    ratio 8.8e+05
#:     squares (k=6)      142 observed / 5.3e-05 predicted    ratio 2.7e+06
#:     fibonacci (k=8)    104 observed / 3.0e-06 predicted    ratio 3.5e+07
#:     partitions (k=8)   149 observed / 4.8e-06 predicted    ratio 3.1e+07
#:     decoy4 (k=4)         0 observed / 8.3e-06 predicted    exact
#:     decoy6 (k=6)         0 observed / 9.9e-17 predicted    exact
#:
#: OEIS entries are massively correlated -- the Catalan numbers occur inside
#: hundreds of sequences, so their terms are nothing like independent draws,
#: and the discrepancy grows with the number of terms rather than washing out.
#: The model was exact only on the irregular decoys, which is precisely the
#: regime this corpus's own sequences sit in.
#:
#: The error is one-directional, and that is what makes the model usable at
#: all: it can only under-count, so a large predicted count is a sound
#: REJECTION while a small one is not on its own an acceptance. The gate
#: therefore carries this factor, rounded up past the worst case measured.
#: It is deliberately brutal: at 1e12 no small-integer sequence can ever clear
#: the gate, which is the correct behaviour, while the corpus's own irregular
#: families clear it by thirty orders of magnitude.
CORRELATION_FACTOR = 1e12

#: Chance-match count above which a hit is coincidence, after the correction.
#: One in a thousand, the same bar `identify.EVIDENCE_MARGIN` sets for an
#: integer relation.
MAX_EXPECTED = 1e-3


# --------------------------------------------------------------------------
# the sequences this repository can honestly ask about
# --------------------------------------------------------------------------
def _rank_range(lo: int = 2, hi: int = 15) -> range:
    return range(lo, hi)


def t_n_numerators() -> list[int]:
    """Numerators of the all-rank C-odd hopping ``t_N = B_N - A_N``."""
    return [int(K.hopping(n).p) for n in _rank_range()]


def t_n_denominators() -> list[int]:
    return [int(K.hopping(n).q) for n in _rank_range()]


def a_n_denominators() -> list[int]:
    """Denominators of the antiparallel channel sum ``A_N``."""
    return [int(K.antiparallel_sum(n).q) for n in _rank_range()]


def b_n_denominators() -> list[int]:
    """Denominators of the parallel channel sum ``B_N``."""
    return [int(K.parallel_sum(n).q) for n in _rank_range()]


def alpha_pen_denominators() -> list[int]:
    """Denominators of the all-rank axial law ``alpha_N = 640/(N(N**2-1)**3)``."""
    return [int(K.alpha_pen(n).q) for n in _rank_range()]


def sigma_numerators() -> list[int]:
    """Numerators of the native string tension ``sigma_n``, n = 0, 2, 3, 4, 5.

    A census output, not a closed form: sigma_4 and sigma_5 came out of
    topology enumerations (22,820 topologies for sigma_5, reconstructed by CRT
    over seven primes). If these integers are in the OEIS at all, something
    external computed the same enumeration.
    """
    return [int(s.p) for s in (K.SIGMA_0, K.SIGMA_2, K.SIGMA_3, K.SIGMA_4, K.SIGMA_5)]


def sigma_denominators() -> list[int]:
    return [int(s.q) for s in (K.SIGMA_0, K.SIGMA_2, K.SIGMA_3, K.SIGMA_4, K.SIGMA_5)]


def fourth_order_denominators() -> list[int]:
    """Denominators of the fourth-order exact record: the C2 neighbourhood.

    ``q_band^(4)``, ``C_shp`` (historical), ``beta_pen``, the record quantum,
    and ``sigma_4`` -- the five exact denominators the fourth order is written
    over. If a common combinatorial normalisation exists, it lives here.
    """
    return [
        int(K.Q_BAND_4.q),
        int(K.C_SHP_HISTORICAL.q),
        int(K.BETA_PEN_3.q),
        int(K.X_QUANTUM.q),
        int(K.SIGMA_4.q),
    ]


def third_order_numerators() -> list[int]:
    """Numerators of the SU(3) third-order coefficients, as printed.

    Domino-engine census outputs over a shared denominator family (249696 and
    its multiples), so unlike the rank laws these are not a closed form in any
    index -- they are what one enumeration returned.
    """
    return [
        int(K.B_3.p),
        int(K.LEAK_3.p),
        int(K.D_3.p),
        int(K.T3_EVEN.p),
        int(K.D3_ODD_DOMINO.p),
        int(K.D3_EVEN_DOMINO.p),
        int(K.D_3_TOP.p),
        int(K.M3_EVEN_K0.p),
    ]


def dim_z2_terms() -> list[int]:
    """``dim Z_2(L) = L**3 + 2``, the harmonic-plane-corrected cycle count, L = 1..13.

    Registered as the CALIBRATION case, not as a question. It is a closed form
    in L and it does hit the OEIS, so it is the entry that exercises the
    ``closed-form-in-N -> not-evidence`` branch on a real match rather than a
    fabricated one -- and it demonstrates the branch is doing work: a hit here
    identifies the polynomial, which was known before the query was asked.
    """
    return [int(K.dim_z2(n)) for n in range(1, 14)]


def _significant_digits(value: float, count: int) -> list[int]:
    """The leading ``count`` significant decimal digits of ``value``.

    OEIS stores a constant as its digit sequence with the decimal point carried
    in the offset, leading zeros stripped -- so 0.0202133... enters as
    ``2,0,2,1,3,3,...``. That is the convention reproduced here.
    """
    digits = f"{abs(value):.{count + 20}e}".split("e")[0].replace(".", "")
    return [int(d) for d in digits[:count]]


def c_shp_new_digits() -> list[int]:
    """Leading digits of the v10a.26 ``C_shp``, truncated to what the run knows.

    Twelve, not seventeen: the run's own shift-invariance failure puts the noise
    floor at 4.6e-15, so digit thirteen onward is not the coefficient's. A
    truncated query is the honest one -- and it is also the only identification
    route the digit budget does not close, because an OEIS ``cons`` entry
    carries hundreds of digits and would supply the ones the run does not have.
    """
    return _significant_digits(K.C_SHP_NEW_NUM, 12)


def c_shp_historical_digits() -> list[int]:
    """Leading digits of the historical ``C_shp``, which is exact.

    Registered alongside the v10a.26 side so the question is put to both. This
    one is a rational with a known exact form, so a match would name the
    constant rather than identify it -- the asymmetry is in the evidence, not
    in the treatment.
    """
    return _significant_digits(float(K.C_SHP_HISTORICAL), 15)


def m_gamma_digits() -> list[int]:
    """Leading digits of the blind Gamma-point scalar, to its own spread."""
    return _significant_digits(K.M_GAMMA_4_NUM, 12)


#: Every builder a registry entry may name. A registry entry naming anything
#: else fails validation: terms are computed here, never transcribed, so the
#: registered sequence cannot drift away from the constants it came from.
BUILDERS: dict[str, Callable[[], list[int]]] = {
    "t_n_numerators": t_n_numerators,
    "t_n_denominators": t_n_denominators,
    "a_n_denominators": a_n_denominators,
    "b_n_denominators": b_n_denominators,
    "alpha_pen_denominators": alpha_pen_denominators,
    "sigma_numerators": sigma_numerators,
    "sigma_denominators": sigma_denominators,
    "fourth_order_denominators": fourth_order_denominators,
    "third_order_numerators": third_order_numerators,
    "dim_z2_terms": dim_z2_terms,
    "c_shp_new_digits": c_shp_new_digits,
    "c_shp_historical_digits": c_shp_historical_digits,
    "m_gamma_digits": m_gamma_digits,
}


# --------------------------------------------------------------------------
# the registry
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Sequence:
    """One registered sequence and the review recorded against it."""

    id: str
    title: str
    builder: str
    generated_by: str
    bears_on: tuple[str, ...]
    what_a_hit_would_mean: str
    scan: dict

    @property
    def terms(self) -> list[int]:
        return BUILDERS[self.builder]()


GENERATED_BY = frozenset({"closed-form-in-N", "census-output"})


def load(path: Path | None = None) -> list[Sequence]:
    doc = yaml.safe_load((path or REGISTRY).read_text(encoding="utf-8"))
    return [
        Sequence(
            id=e["id"],
            title=e["title"],
            builder=e["builder"],
            generated_by=e["generated_by"],
            bears_on=tuple(e.get("bears_on", ())),
            what_a_hit_would_mean=e["what_a_hit_would_mean"],
            scan=e.get("scan") or {},
        )
        for e in doc["sequences"]
    ]


def validate(sequences: list[Sequence]) -> list[str]:
    """Registry problems, as strings. Empty means the registry is coherent."""
    problems = []
    seen = set()
    for s in sequences:
        if s.id in seen:
            problems.append(f"{s.id}: duplicate id")
        seen.add(s.id)
        if s.builder not in BUILDERS:
            problems.append(f"{s.id}: unknown builder {s.builder!r}")
            continue
        if s.generated_by not in GENERATED_BY:
            problems.append(f"{s.id}: generated_by must be one of {sorted(GENERATED_BY)}")
        if len(s.terms) < 3:
            problems.append(f"{s.id}: {len(s.terms)} terms is not a sequence")
        if not s.what_a_hit_would_mean.strip():
            problems.append(f"{s.id}: no statement of what a hit would mean")
    return problems


# --------------------------------------------------------------------------
# the snapshot
# --------------------------------------------------------------------------
def snapshot_digest(path: Path | None = None) -> str:
    p = path or SNAPSHOT
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_snapshot(path: Path | None = None) -> list[tuple[str, str]]:
    """``(A-number, ",t1,t2,...,")`` for every sequence in the dump.

    The data field is kept as the dump's own comma-delimited string, leading and
    trailing comma included, so a contiguous-subsequence query is one substring
    test -- the same match semantics as the site's ``seq:`` search.
    """
    out = []
    with gzip.open(path or SNAPSHOT, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            aid, _, data = line.strip().partition(" ")
            if aid and data.startswith(","):
                out.append((aid, data.replace("-", "")))
    return out


def needle(terms: list[int]) -> str:
    """The comma-delimited run to search for, signs stripped.

    OEIS's own ``seq:`` query -- which is what a bare comma-separated list
    normalises to on the site -- "matches the sequence data, possibly by
    ignoring signs" (oeis.org/hints.html); ``signed:`` is the stricter variant.
    Matching signs exactly is therefore NOT the site's semantics, and the
    difference is measurable: across 50 queries against the live API, 17
    disagreed with a sign-exact match on the dump, always with the dump low
    (``1,2,6,24`` is 831 either way, but a mixed-sign query loses hits).
    Stripping signs on both sides reproduces the site. It matters most for the
    two registered families that are mostly negative -- ``SIGMA_NUM`` (4 of 5)
    and ``ORDER3_NUM`` (7 of 8) -- which are exactly where a sign-exact match
    could hide a hit that is really there.
    """
    return "," + ",".join(str(t).lstrip("-") for t in terms) + ","


def matches(snapshot: list[tuple[str, str]], terms: list[int]) -> list[str]:
    """A-numbers whose data contains ``terms`` as a contiguous run, signs ignored."""
    n = needle(terms)
    return [aid for aid, data in snapshot if n in data]


# --------------------------------------------------------------------------
# the null model, built from the snapshot itself
# --------------------------------------------------------------------------
def unigram_model(snapshot: list[tuple[str, str]], values: set[int]) -> tuple[dict[int, int], int]:
    """Occurrence counts of ``values`` across all term slots, and the slot total.

    Only the values actually asked about are counted, so this is one pass and a
    small dict rather than a frequency table over every integer in the OEIS.
    """
    wanted = {str(v).lstrip("-") for v in values}
    counts: Counter[str] = Counter()
    total = 0
    for _aid, data in snapshot:
        fields = data.split(",")
        # split of ",a,b," yields a leading and a trailing empty field
        total += len(fields) - 2
        for f in fields:
            if f in wanted:
                counts[f] += 1
    return {int(k): v for k, v in counts.items()}, total


def expected_by_chance(terms: list[int], counts: dict[int, int], total_slots: int) -> float:
    """Windows expected to match all of ``terms`` under the unigram null.

    ``total_slots * prod_i (count(v_i) / total_slots)``. A value the dump never
    contains is floored at one occurrence, so the estimate is never zero and the
    verdict never rests on a division that happened to vanish.

    This is a LOWER BOUND on the true chance count, not an estimate of it: the
    model treats term values as independent draws and they are emphatically not.
    See ``CORRELATION_FACTOR`` for the measurement, and
    :func:`corrected_expectation` for what the verdict uses instead.
    """
    if total_slots <= 0:
        return float("inf")
    e = float(total_slots)
    for t in terms:
        e *= max(counts.get(abs(t), 0), 1) / total_slots
    return e


#: The controls the correlation factor was measured on. Six sequences the OEIS
#: certainly contains and two irregular decoys it certainly does not, so the
#: measurement covers both ends: where the model fails, and where it is exact.
CONTROLS: dict[str, list[int]] = {
    "catalan": [1, 1, 2, 5, 14],
    "catalan8": [1, 1, 2, 5, 14, 42, 132, 429],
    "factorial": [1, 2, 6, 24, 120],
    "primes": [2, 3, 5, 7, 11, 13],
    "squares": [1, 4, 9, 16, 25, 36],
    "fibonacci": [1, 1, 2, 3, 5, 8, 13, 21],
    "partitions": [1, 1, 2, 3, 5, 7, 11, 15],
    "decoy4": [7, 41, 313, 2179],
    "decoy6": [7, 41, 313, 2179, 15451, 99991],
}


def measure_controls(snapshot: list[tuple[str, str]]) -> dict[str, dict]:
    """Observed against predicted match counts for :data:`CONTROLS`."""
    values = {v for t in CONTROLS.values() for v in t}
    counts, total = unigram_model(snapshot, values)
    out = {}
    for name, terms in CONTROLS.items():
        observed = len(matches(snapshot, terms))
        predicted = expected_by_chance(terms, counts, total)
        out[name] = {
            "terms": terms,
            "observed": observed,
            "predicted": predicted,
            "ratio": (observed / predicted) if predicted > 0 else None,
        }
    return out


# --------------------------------------------------------------------------
# the verdict
# --------------------------------------------------------------------------
def corrected_expectation(expected: float) -> float:
    """The chance count the verdict actually uses.

    :func:`expected_by_chance` assumes term values are independent draws, and
    the measurement recorded in ``CORRELATION_FACTOR`` says they are not, by up
    to eleven orders of magnitude. Multiplying through by the worst measured
    correction keeps the gate on the safe side of its own null model.
    """
    return expected * CORRELATION_FACTOR


def verdict(seq: Sequence, hits: list[str], expected: float) -> tuple[str, str]:
    """``(verdict, reason)`` for one scanned sequence. Never promotes anything.

    Absence is reported before anything else: a sequence with no match has no
    match whatever its length, and running it through the evidence gate first
    would report the informative "nothing in 400,000 sequences contains this"
    as though it were a failed test.
    """
    terms = seq.terms
    if len(terms) < MIN_TERMS:
        return "not-evidence", f"{len(terms)} terms is not a sequence"
    if not hits:
        return "no-hit", (
            f"no OEIS sequence contains these {len(terms)} terms "
            f"(largest |term| {max(abs(t) for t in terms)})"
        )
    corrected = corrected_expectation(expected)
    if seq.generated_by == "closed-form-in-N":
        return "not-evidence", (
            "a closed form in N; the OEIS holds polynomial families without number, "
            "so a hit identifies a normalisation and not a mechanism"
        )
    if corrected > MAX_EXPECTED:
        return "not-evidence", (
            f"expected by chance {expected:.2e} x {CORRELATION_FACTOR:.0e} correlation "
            f"correction = {corrected:.2e} > {MAX_EXPECTED:.0e}"
        )
    return "hit", (
        f"{len(hits)} match, chance count {corrected:.2e} after the "
        f"{CORRELATION_FACTOR:.0e} correlation correction"
    )


def scan(sequences: list[Sequence], snapshot: list[tuple[str, str]]) -> dict[str, dict]:
    """Scan every registered sequence against the snapshot. Network-free."""
    values = {v for s in sequences for v in s.terms}
    counts, total = unigram_model(snapshot, values)
    out = {}
    for s in sequences:
        terms = s.terms
        # The prefix curve IS the discriminating power, made visible: a match
        # count that collapses as terms are added is a query that discriminated,
        # and one that stays flat is a generic family.
        prefixes = {k: matches(snapshot, terms[:k]) for k in range(MIN_TERMS, len(terms) + 1)}
        curve = {k: len(v) for k, v in prefixes.items()}
        hits = prefixes[len(terms)]
        expected = expected_by_chance(terms, counts, total)
        v, reason = verdict(s, hits, expected)
        out[s.id] = {
            "terms": terms,
            "prefix_hits": curve,
            "hits": hits,
            "expected_by_chance": expected,
            "verdict": v,
            "reason": reason,
        }
    return out


def fetch(dest: Path | None = None) -> Path:
    """Download the official dump. The one network call in this module.

    ``robots.txt`` permits this path; it forbids ``/search``, which is why the
    search API appears nowhere here. See :data:`USER_AGENT` for why the request
    identifies itself as a browser would -- a front-cache filter on the default
    ``Python-urllib`` string, not an access control, and not a way around the
    disallowed path, which is simply never requested.
    """
    import urllib.request

    p = dest or SNAPSHOT
    p.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(SNAPSHOT_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=600) as r, p.open("wb") as fh:
        while chunk := r.read(1 << 20):
            fh.write(chunk)
    return p
