#!/usr/bin/env python3
"""Summarize the completed R_A and R_Bulun reviews for the report (descriptive).

For each year and role: candidates, D counts, substantive count, E changes from
the AI suggestion, D x E table, H/I/J/K/L distributions, and a check that the
completed workbook's D/E/F/H-L/R cells equal judgments.json.

Usage: python summarize_runs.py [2018 2019 2024 2025]
"""
import collections
import json
import re
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ROLES = {"R_A": "R_A", "R_Bulun": "R_B"}  # role -> blank-workbook role
KEY_RE = re.compile(r"^\d{4}::[^:]+::C\d{3}$")
COL = {"D": 4, "E": 5, "F": 6, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "R": 18}


def sheet_rows(path):
    wb = openpyxl.load_workbook(path)
    out = {}
    for s in wb.sheetnames:
        if s.startswith("C_"):
            ws = wb[s]
            for r in range(2, ws.max_row + 1):
                k = ws.cell(r, 1).value
                if k and KEY_RE.match(str(k)):
                    out[k] = {f: ws.cell(r, c).value for f, c in COL.items()}
    return out, wb["Setup"]["B2"].value, wb["Setup"]["B4"].value


def substantive(r):
    if r["D"] != "retain":
        return False
    if r["E"] == "statistical_results":
        return r.get("H") in ("confirmed_issue", "probable_issue") and r.get("I") == "substantive"
    if r["E"] in ("report_internal_inconsistency", "plan_material"):
        return r.get("K") == "substantive_inconsistency"
    return False


def main(years):
    table = []
    for y in years:
        blank, _, _ = sheet_rows(ROOT / y / f"human_adjudication_v_2_4_1_{y}_R_A.xlsx")
        for role, tpl in ROLES.items():
            d = HERE / y / role
            rows = {r["key"]: r for r in json.loads((d / "judgments.json").read_text())["rows"]}
            wbp = d / f"human_adjudication_v_2_4_1_{y}_{role}_completed.xlsx"
            done, b2, b4 = sheet_rows(wbp)
            mism = []
            for k, j in rows.items():
                w = done.get(k)
                if w is None:
                    mism.append((k, "missing in workbook"))
                    continue
                for f in "DE":
                    if w[f] != j[f]:
                        mism.append((k, f))
                for f in "HIJKL":
                    v = j.get(f)
                    if v is not None and w[f] != v:
                        mism.append((k, f))
                if w["F"] != "primary_done":
                    mism.append((k, "F"))
                if (j.get("R") or "").strip() != (w["R"] or "").strip():
                    mism.append((k, "R"))
            D = collections.Counter(r["D"] for r in rows.values())
            sub = sum(substantive(r) for r in rows.values())
            echg = [(k, blank[k]["E"], r["E"]) for k, r in sorted(rows.items()) if r["E"] != blank[k]["E"]]
            table.append((y, role, len(rows), D["retain"], D["exclude"], D["discuss"], sub, len(echg)))
            print(f"== {y} {role}: n={len(rows)} blank_keys={len(blank)} Setup B2={b2!r} B4={b4!r} "
                  f"workbook/judgments mismatches={len(mism)}")
            for m in mism[:10]:
                print("   MISMATCH", m)
            print("   D:", dict(D), " substantive:", sub, " E changed:", len(echg))
            for k, a, b in echg:
                print(f"     E {k}: {a} -> {b}")
            de = collections.Counter((r["E"], r["D"]) for r in rows.values())
            for e in ("statistical_results", "report_internal_inconsistency", "plan_material", "protocol_report"):
                print(f"   {e:30s} retain={de[(e,'retain')]:3d} exclude={de[(e,'exclude')]:3d} discuss={de[(e,'discuss')]:3d}")
            ret = [r for r in rows.values() if r["D"] == "retain"]
            for f, doms in (("H", {"statistical_results"}), ("I", {"statistical_results"}), ("J", {"statistical_results"}),
                            ("K", {"report_internal_inconsistency", "plan_material"}), ("L", {"protocol_report"})):
                c = collections.Counter(r.get(f) or "(blank)" for r in ret if r["E"] in doms)
                print(f"   {f}: {dict(c)}")
            print("   discuss keys:", [k for k, r in sorted(rows.items()) if r["D"] == "discuss"])
    print("\n| Year | Role | Candidates | Retain | Exclude | Discuss | Substantive* | E changed |")
    print("|---|---|---:|---:|---:|---:|---:|---:|")
    for t in table:
        print("| " + " | ".join(str(x) for x in t) + " |")


if __name__ == "__main__":
    main(sys.argv[1:] or ["2018", "2019", "2024", "2025"])
