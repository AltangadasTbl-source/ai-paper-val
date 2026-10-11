#!/usr/bin/env python3
"""Post hoc R_A vs R_B agreement for AI-simulated reviews (descriptive only).

Run only after both roles of a year are complete. Reports raw agreement and
Cohen's kappa for D, E and a derived outcome, plus a disagreement list.
Agreement between two runs of the same model is NOT an estimate of human
inter-rater reliability.

Usage: python compare_roles.py 2019 [2018 2024 2025 ...]
"""
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def outcome(r):
    if r["D"] == "discuss":
        return "unresolved"
    if r["D"] == "exclude":
        return "excluded"
    e = r["E"]
    if e == "statistical_results":
        return "stat_issue_substantive" if r.get("H") in ("confirmed_issue", "probable_issue") and r.get("I") == "substantive" else "stat_other"
    if e in ("report_internal_inconsistency", "plan_material"):
        return "inconsistency_substantive" if r.get("K") == "substantive_inconsistency" else "inconsistency_other"
    return "protocol_report"


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca = collections.Counter(a for a, _ in pairs)
    cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n**2
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")


def main(years):
    for y in years:
        a = {r["key"]: r for r in json.loads((HERE / y / "R_A" / "judgments.json").read_text())["rows"]}
        b = {r["key"]: r for r in json.loads((HERE / y / "R_B" / "judgments.json").read_text())["rows"]}
        keys = sorted(set(a) & set(b))
        print(f"== {y}: n={len(keys)} (A only {len(set(a)-set(b))}, B only {len(set(b)-set(a))})")
        for name, f in [("D", lambda r: r["D"]), ("E", lambda r: r["E"]), ("outcome", outcome)]:
            po, k = kappa([(f(a[x]), f(b[x])) for x in keys])
            print(f"  {name:8s} agreement={po:.3f} kappa={k:.3f}")
        print("  outcome table (R_A rows x R_B cols):")
        t = collections.Counter((outcome(a[x]), outcome(b[x])) for x in keys)
        cats = sorted({c for p in t for c in p})
        print("    " + " | ".join(["A\\B"] + cats))
        for ca in cats:
            print("    " + " | ".join([ca] + [str(t[(ca, cb)]) for cb in cats]))
        for x in keys:
            if outcome(a[x]) != outcome(b[x]) or a[x]["E"] != b[x]["E"]:
                print(f"  DIFF {x}: A={a[x]['D']}/{a[x]['E']}/{outcome(a[x])}  B={b[x]['D']}/{b[x]['E']}/{outcome(b[x])}")


if __name__ == "__main__":
    main(sys.argv[1:])
