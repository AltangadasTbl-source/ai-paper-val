#!/usr/bin/env python3
"""Reduce a v.2.3.1 review workbook to Setup, Checks, Papers, C_ sheets and Codebook.

Removes Start, Decisions, Paper_counts, Protocol_plan_table, Candidates, Evidence,
Links, Relations, Rule_defaults and Manifest, and makes the kept sheets
self-contained:
- G (validation hint): the key-membership lookup into Decisions/Candidates is
  replaced by a check that the key starts with "<year>::<paper>::".
- Checks: counts come directly from the C_ sheets; the Paper_counts row is dropped.
- Candidate-key hyperlinks to Evidence are removed.
- The Codebook row that pointed reviewers to removed sheets is reworded.

Usage: python trim_workbook.py IN.xlsx OUT.xlsx   (OUT may equal IN)
"""
import copy
import re
import sys
from pathlib import Path

import openpyxl

DROP = ["Start", "Decisions", "Paper_counts", "Protocol_plan_table", "Candidates",
        "Evidence", "Links", "Relations", "Rule_defaults", "Manifest"]
DROP_RX = re.compile(r"(?<![A-Za-z_])'?(" + "|".join(DROP) + r")'?!")
LOOKUP_RX = re.compile(
    r"COUNTIFS\((?:Decisions|Candidates)!\$[A-Z]+\$2:\$[A-Z]+\$\d+,A(\d+),"
    r"(?:Decisions|Candidates)!\$[A-Z]+\$2:\$[A-Z]+\$\d+,\"([^\"]+)\"\)<>1")
SOURCE_TEXT = "Where to check the source claim. Open the original documents named here (file and PDF page)."


def q(s):
    return "'" + s.replace("'", "''") + "'"


def main(src, dst):
    wb = openpyxl.load_workbook(src)
    year = str(wb["Setup"]["B5"].value)  # Setup B5 holds the year in every 2.3.1 workbook
    assert year in ("2018", "2019", "2024", "2025"), year
    csheets = [s for s in wb.sheetnames if s.startswith("C_")]
    ranges = {}
    for s in csheets:
        ws = wb[s]
        last = max(r for r in range(1, ws.max_row + 1) if ws.cell(r, 1).value)
        ranges[s] = last
        for r in range(2, last + 1):
            g = ws.cell(r, 7)
            if isinstance(g.value, str) and g.value.startswith("="):
                def rep(m):
                    row, paper = m.group(1), m.group(2)
                    pre = f"{year}::{paper}::"
                    return f'LEFT(A{row},LEN("{pre}"))<>"{pre}"'
                g.value = LOOKUP_RX.sub(rep, g.value)
            a = ws.cell(r, 1)
            if a.hyperlink is not None and a.hyperlink.location and DROP_RX.search(a.hyperlink.location + "!"):
                a.hyperlink = None
                a.font = copy.copy(ws.cell(r, 2).font)

    def total(fn):
        return "+".join(fn(q(s), ranges[s]) for s in csheets)

    ready = total(lambda s, n: f'COUNTIF({s}!$G$2:$G${n},"PRIMARY READY")')
    disc = total(lambda s, n: f'COUNTIF({s}!$D$2:$D${n},"discuss")')
    rdisc = total(lambda s, n: f'COUNTIFS({s}!$G$2:$G${n},"PRIMARY READY",{s}!$D$2:$D${n},"discuss")')

    ck = wb["Checks"]
    drop_rows = []
    for r in range(1, ck.max_row + 1):
        label = str(ck.cell(r, 1).value or "")
        v = ck.cell(r, 2).value
        if not (isinstance(v, str) and v.startswith("=") and DROP_RX.search(v)):
            continue
        low = label.lower()
        if "ready" in low and "discuss" in low:
            ck.cell(r, 2).value = "=" + rdisc
        elif "ready" in low:
            ck.cell(r, 2).value = "=" + ready
        elif "discuss" in low:
            ck.cell(r, 2).value = "=" + disc
        elif "papers with counts" in low:
            drop_rows.append(r)
        else:
            raise SystemExit(f"unhandled Checks row {r}: {label}")
    for r in range(1, ck.max_row + 1):
        v = ck.cell(r, 2).value
        if isinstance(v, str) and ("Decisions" in v or "counts" in v.lower() or "built-in results" in v):
            v = (v.replace("Filter Decisions by readiness, return to the C_ sheet, correct entries and manually confirm F.",
                           "Inspect G on each C_ sheet, correct entries and manually confirm F.")
                  .replace("Inspect G on paper sheets and readiness in Decisions.", "Inspect G on the C_ sheets.")
                  .replace("Inspect G on C_ sheets or filter Decisions readiness.", "Inspect G on the C_ sheets.")
                  .replace("Filter Decisions status; return to C_ inputs.", "Inspect G on the C_ sheets.")
                  .replace(" Discuss rows remain unresolved; affected paper counts are blank.", " Discuss rows remain unresolved.")
                  .replace(" with its built-in results.", ".")
                  .replace("; affected paper outcome counts are withheld.", ".")
                  .replace(" and prevents that paper’s outcome counts.", "."))
            ck.cell(r, 2).value = v
    for r in sorted(drop_rows, reverse=True):
        # only rows below reference cells above them, so deleting is safe; verified after
        ck.delete_rows(r)

    cb = wb["Codebook"]
    for row in cb.iter_rows():
        for c in row:
            if isinstance(c.value, str) and re.search(r"\b(Candidates|Evidence|Links|Relations)\b", c.value) and not c.value.startswith("="):
                c.value = SOURCE_TEXT

    for s in DROP:
        if s in wb.sheetnames:
            wb.remove(wb[s])
    wb.active = wb.sheetnames.index("Setup")
    for ws in wb.worksheets:
        ws.sheet_view.tabSelected = ws.title == "Setup"

    # post-checks: nothing in the kept sheets may reference a removed sheet
    probs = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("=") and DROP_RX.search(c.value):
                    probs.append(f"{ws.title}!{c.coordinate} formula")
                if c.hyperlink is not None and c.hyperlink.location and DROP_RX.search(c.hyperlink.location + "!"):
                    probs.append(f"{ws.title}!{c.coordinate} link")
        for dv in ws.data_validations.dataValidation:
            if dv.formula1 and DROP_RX.search(dv.formula1):
                probs.append(f"{ws.title} validation")
        for rng in ws.conditional_formatting:
            for rule in rng.rules:
                if any(DROP_RX.search(f) for f in (rule.formula or [])):
                    probs.append(f"{ws.title} conditional format")
    if probs:
        raise SystemExit("dangling references: " + "; ".join(probs[:10]))
    tmp = Path(dst).with_suffix(".tmp.xlsx")
    wb.save(tmp)
    tmp.replace(dst)
    print(f"{Path(dst).name}: sheets={wb.sheetnames[:4]}+{len(csheets)} C_+Codebook; Checks rows dropped={len(drop_rows)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
