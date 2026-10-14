#!/usr/bin/env python3
"""Build the v.2.4.1 primary-review workbooks for 2024 (see ../BUILD_SPEC.md).

Reads <repo>/2024/<paper>/.ai_paper_validation/final_report_1_6_2.md (read-only),
writes candidates_2024.json, both workbooks and output_hashes.json into this folder.
Fails loudly on any unexpected report structure.

Run: PYTHONDONTWRITEBYTECODE=1 <repo>/human_adjudication/human_adjudication_v_2_3_1/2019/.venv/bin/python build_v_2_4_1.py
"""
import copy
import hashlib
import json
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import openpyxl
from openpyxl.worksheet.cell_range import MultiCellRange

YEAR = 2024
VERSION = "v.2.4.1"
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
YEAR_DIR = REPO / str(YEAR)
REPORT_REL = Path(".ai_paper_validation") / "final_report_1_6_2.md"
TEMPLATE = REPO / "human_adjudication/human_adjudication_v_2_3_1/2018/release/human_adjudication_v_2_3_1_2018_R_A.xlsx"

# Template constants (2018 canonical file).
TPL_PATTERN_SHEET = "C_jama.2017.21906"
TPL_PREFIX = "2018::jama.2017.21906::"
TPL_LAST = 7

# Papers without a workflow 1.6.2 report get an empty placeholder sheet. Empty since
# jama.2024.12829 received its 1.6.2 report (2026-10-11).
PLACEHOLDERS = {}

DOMAINS = ["statistical_results", "report_internal_inconsistency", "plan_material", "protocol_report"]
REQUIRED_FIELDS = ["Candidate statement", "Review domain", "Relationship type", "Exact source locations"]
FORMULA_COLS = "GHIJKL"
HIDDEN_COLS = "MNOPQ"
PENDING_RE = re.compile(r"\**\s*Pending Human Adjudication\b[^.*]*\.?\s*\**", re.I)
LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\((<[^>]*>|[^()\s]*(?:\([^()\s]*\)[^()\s]*)*)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^## (C\d{3}) — (.+?)(?:\s*\{#[^}]*\})?\s*$")
FIELD_RE = re.compile(r"^\*\*([^*]+?):\*\*\s*(.*)$")
ANOMALIES = []


class BuildError(RuntimeError):
    pass


def fail(msg):
    raise BuildError(msg)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def strip_pending(text, where):
    if re.search(r"pending human adjudication", text, re.I):
        new = PENDING_RE.sub(" ", text)
        ANOMALIES.append(f"{where}: stripped 'Pending Human Adjudication' boilerplate")
        if re.search(r"pending human adjudication", new, re.I):
            fail(f"{where}: could not strip boilerplate: {text!r}")
        return new
    return text


def md_plain(text, where):
    """Markdown -> plain text per spec column C/B rules."""
    def link(m):
        label, target = m.group(1), m.group(2)
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I) or target.startswith("#") or target == "":
            return label
        path = unquote(target.split("#", 1)[0])
        fname = posixpath.basename(path)
        if not fname:
            fail(f"{where}: link target without file name: {m.group(0)!r}")
        stem = fname.rsplit(".", 1)[0]
        if fname.lower() in label.lower() or stem.lower() in label.lower():
            return label
        page = re.search(r"#page=(\d+)", target)
        if page and not re.search(r"\d", label):
            ANOMALIES.append(f"{where}: link text {label!r} has no page number (target page {page.group(1)})")
        return f"{fname} — {label}"

    out = LINK_RE.sub(link, text)
    out = out.replace("**", "").replace("`", "")
    out = re.sub(r"<a id=\"[^\"]*\"></a>", "", out)
    out = re.sub(r"\s+", " ", out).strip()
    for bad in ("](", "**", "<a id"):
        if bad in out:
            fail(f"{where}: markdown/HTML residue {bad!r} in {out!r}")
    if re.search(r"<\s*/?[A-Za-z]", out):
        fail(f"{where}: HTML tag residue in {out!r}")
    if re.search(r"https?://", out):
        fail(f"{where}: bare URL in {out!r}")
    if re.search(r"(?<!\w)\*(?=\w)|(?<=\w)\*(?!\w)", out):
        ANOMALIES.append(f"{where}: single asterisk retained in {out!r}")
    return out


def table_after(lines, heading):
    """Return list of rows (list of cell strings) of the first table under '## heading'."""
    idx = [i for i, l in enumerate(lines) if l.strip() == f"## {heading}"]
    if len(idx) != 1:
        fail(f"expected exactly one '## {heading}' heading, found {len(idx)}")
    i = idx[0] + 1
    while i < len(lines) and not lines[i].startswith("|"):
        if lines[i].startswith("## "):
            fail(f"no table under '## {heading}'")
        i += 1
    rows = []
    while i < len(lines) and lines[i].startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        rows.append(cells)
        i += 1
    if len(rows) < 3 or not re.fullmatch(r"[-: |]+", "|".join(rows[1])):
        fail(f"malformed table under '## {heading}'")
    return rows[0], rows[2:]


def cell_plain(c):
    return re.sub(r"[*`]", "", c).strip()


def field_value(lines, i, rest, where, label):
    """Value of a **Label:** field starting at line i: same-line text, else the following list block."""
    if rest.strip():
        j = i + 1
        if j < len(lines) and lines[j].strip() and not FIELD_RE.match(lines[j]) and not lines[j].startswith("## "):
            fail(f"{where}: field {label!r} continues on following line {j + 1}: {lines[j][:80]!r}")
        return rest.strip(), rest.strip()
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    items = []
    raw = []
    while j < len(lines) and lines[j].strip():
        l = lines[j]
        if l.startswith("- "):
            items.append(l[2:].strip())
        elif l.startswith("  ") and items:
            items[-1] += " " + l.strip()
        else:
            fail(f"{where}: field {label!r} has unexpected block line {j + 1}: {l[:80]!r}")
        raw.append(l)
        j += 1
    if not items:
        fail(f"{where}: field {label!r} is empty")
    ANOMALIES.append(f"{where}: field {label!r} given as a {len(items)}-item bullet list; items joined with '; '")
    return "; ".join(it.rstrip(" ;.") for it in items), "\n".join(raw)


def parse_report(paper, path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    where0 = f"{paper}"
    # odd characters
    for ch, name in (("�", "replacement char"), ("​", "zero-width space"), ("﻿", "BOM"), ("­", "soft hyphen")):
        if ch in text:
            ANOMALIES.append(f"{paper}: report contains {name} U+{ord(ch):04X} ({text.count(ch)}x)")

    # Candidate Index
    hdr, rows = table_after(lines, "Candidate Index")
    hl = [h.lower() for h in hdr]
    try:
        di = next(k for k, h in enumerate(hl) if h == "review domain")
        ri = next(k for k, h in enumerate(hl) if h == "relationship type")
    except StopIteration:
        fail(f"{paper}: Candidate Index lacks Review domain / Relationship type columns: {hdr}")
    index = []
    for r in rows:
        m = re.match(r"^\[?\s*(C\d{3})\b", r[0])
        if not m:
            fail(f"{paper}: Candidate Index row without ID: {r}")
        index.append({"id": m.group(1), "domain": cell_plain(r[di]), "relationship": cell_plain(r[ri])})

    # Review-Domain Summary
    hdr, rows = table_after(lines, "Review-Domain Summary")
    if hdr[0].lower() != "review domain":
        fail(f"{paper}: first Review-Domain Summary table is not the domain table: {hdr}")
    summary = {}
    for r in rows:
        name = cell_plain(r[0])
        val = cell_plain(r[-1])
        if not re.fullmatch(r"\d+", val):
            fail(f"{paper}: non-integer domain summary count {r}")
        summary[name] = int(val)
    if set(summary) != set(DOMAINS) | {"Total"}:
        fail(f"{paper}: domain summary rows {sorted(summary)} unexpected")
    if sum(summary[d] for d in DOMAINS) != summary["Total"]:
        fail(f"{paper}: domain summary does not sum to its Total")

    # Cards
    for k, l in enumerate(lines):
        if re.match(r"^#+\s*C\d", l) and not HEADING_RE.match(l):
            fail(f"{paper}: unexpected candidate heading format at line {k + 1}: {l!r}")
    starts = [(k, HEADING_RE.match(l)) for k, l in enumerate(lines) if HEADING_RE.match(l)]
    cards = []
    for n, (k, m) in enumerate(starts):
        cid, title_md = m.group(1), m.group(2)
        where = f"{paper} {cid}"
        end = k + 1
        while end < len(lines) and not lines[end].startswith("## ") and not lines[end].startswith("# ") \
                and not lines[end].startswith("<a id"):
            end += 1
        fields = {}
        raws = {}
        for i in range(k + 1, end):
            fm = FIELD_RE.match(lines[i])
            if fm and fm.group(1) in REQUIRED_FIELDS:
                lab = fm.group(1)
                if lab in fields:
                    fail(f"{where}: duplicate field {lab!r}")
                fields[lab], raws[lab] = field_value(lines, i, fm.group(2), where, lab)
        missing = [f for f in REQUIRED_FIELDS if f not in fields]
        if missing:
            fail(f"{where}: missing fields {missing}")
        title = md_plain(strip_pending(title_md, where + " title"), where + " title")
        domain = cell_plain(fields["Review domain"])
        if domain not in DOMAINS:
            fail(f"{where}: invalid review domain {domain!r}")
        rel = cell_plain(fields["Relationship type"])
        if not re.fullmatch(r"S_W|S_C|P_R|P_P", rel):
            fail(f"{where}: unexpected relationship type {rel!r}")
        locs = md_plain(strip_pending(fields["Exact source locations"], where + " locations"), where + " locations")
        stmt = md_plain(strip_pending(fields["Candidate statement"], where + " statement"), where + " statement")
        for nm, v in (("title", title), ("locations", locs), ("statement", stmt)):
            if not v:
                fail(f"{where}: empty {nm}")
        cards.append({"id": cid, "title": title, "statement": stmt, "domain": domain,
                      "relationship_type": rel, "source_locations": locs,
                      "source_locations_markdown": raws["Exact source locations"]})

    ids = [c["id"] for c in cards]
    if ids != [f"C{i:03d}" for i in range(1, len(ids) + 1)]:
        fail(f"{paper}: card IDs not sequential from C001: {ids}")
    if [r["id"] for r in index] != ids:
        fail(f"{paper}: Candidate Index IDs {[r['id'] for r in index]} differ from cards {ids}")
    for r, c in zip(index, cards):
        if r["domain"] != c["domain"] or r["relationship"] != c["relationship_type"]:
            fail(f"{paper} {c['id']}: index ({r['domain']},{r['relationship']}) vs card ({c['domain']},{c['relationship_type']})")
    counts = {d: sum(c["domain"] == d for c in cards) for d in DOMAINS}
    if summary["Total"] != len(cards) or any(summary[d] != counts[d] for d in DOMAINS):
        fail(f"{paper}: Review-Domain Summary {summary} vs cards {counts} (n={len(cards)})")
    return cards, {"index_rows": len(index), "cards": len(cards), "summary_total": summary["Total"],
                   "summary": {d: summary[d] for d in DOMAINS}}


def g_to_l_formula(tpl_formula, row, last, prefix):
    """Template row-2 formula -> formula for `row` on a sheet whose last data row is `last`."""
    f = re.sub(r"(?<![A-Za-z$])([A-L])2(?![0-9])", lambda m: f"{m.group(1)}{row}", tpl_formula)
    f = f.replace(f"$A$2:$A${TPL_LAST}", f"$A$2:$A${last}")
    f = f.replace('"' + TPL_PREFIX + '"', '"' + prefix.replace('"', '""') + '"')
    return f


def copy_style(src, dst):
    dst._style = copy.copy(src._style)


def build_c_sheet(wb, tpl, name, rows, prefix):
    ws = wb.copy_worksheet(tpl)
    ws.title = name
    for key in [k for k in ws._cells if k[0] > 1]:
        del ws._cells[key]
    for r in [r for r in ws.row_dimensions if r > 1]:
        del ws.row_dimensions[r]
    ws["H1"] = "Statistical_or_numerical issue"
    ws.freeze_panes = "B2"
    ws.sheet_view.tabSelected = False
    if rows is None:
        return ws
    last = len(rows) + 1
    tpl_g = {c: tpl[f"{c}2"].value for c in FORMULA_COLS}
    for i, cand in enumerate(rows):
        r = i + 2
        src_row = 2 if r % 2 == 0 else 3
        for col in range(1, 19):
            copy_style(tpl.cell(src_row, col), ws.cell(r, col))
        ws.row_dimensions[r].height = tpl.row_dimensions[src_row].height
        ws[f"A{r}"] = cand["key"]
        ws[f"B{r}"] = cand["title"]
        ws[f"C{r}"] = cand["source_locations"]
        ws[f"E{r}"] = cand["domain"]
        ws[f"F{r}"] = "no"
        for c in FORMULA_COLS:
            ws[f"{c}{r}"] = g_to_l_formula(tpl_g[c], r, last, prefix)
    for dv in tpl.data_validations.dataValidation:
        rng = str(dv.sqref)
        m = re.fullmatch(r"(?P<c>[A-R])2:(?P=c)" + str(TPL_LAST), rng)
        if not m:
            fail(f"unexpected template DV sqref {rng}")
        nd = copy.deepcopy(dv)
        nd.sqref = MultiCellRange(f"{m.group(1)}2:{m.group(1)}{last}")
        ws.data_validations.append(nd)
    for cf_range, rules in tpl.conditional_formatting._cf_rules.items():
        rng = str(cf_range.sqref)
        m = re.fullmatch(r"(?P<c>[A-R])2:(?P=c)" + str(TPL_LAST), rng)
        if not m:
            fail(f"unexpected template CF sqref {rng}")
        for rule in rules:
            ws.conditional_formatting.add(f"{m.group(1)}2:{m.group(1)}{last}", copy.deepcopy(rule))
    ws.auto_filter.ref = f"A1:R{last}"
    return ws


def build_workbook(role, papers, catalog):
    wb = openpyxl.load_workbook(TEMPLATE)
    tpl = wb[TPL_PATTERN_SHEET]
    # sanity on template pattern sheet
    if tpl.max_row != TPL_LAST or tpl["H1"].value != "Statistcal_or_numerical issue":
        fail("template pattern sheet differs from expectation")

    setup = wb["Setup"]
    setup["B4"] = role
    setup["B5"] = YEAR
    if setup["B2"].value is not None or setup["B3"].value is not None:
        fail("template Setup B2/B3 not blank")

    # Papers
    pp = wb["Papers"]
    tpl_pp_styles = {r: [copy.copy(pp.cell(r, c)._style) for c in range(1, 4)] for r in (2, 3)}
    tpl_pp_height = pp.row_dimensions[2].height
    hdr_style = copy.copy(pp["C1"]._style)
    for key in [k for k in pp._cells if k[0] > 1]:
        del pp._cells[key]
    for r in [r for r in pp.row_dimensions if r > 1]:
        del pp.row_dimensions[r]
    if PLACEHOLDERS:
        pp["D1"] = "Note"
        pp["D1"]._style = copy.copy(hdr_style)
        pp.column_dimensions["D"].width = 60.0
    for i, p in enumerate(papers):
        r = i + 2
        styles = tpl_pp_styles[2 if r % 2 == 0 else 3]
        for c in range(1, 4):
            pp.cell(r, c)._style = copy.copy(styles[c - 1])
        pp.row_dimensions[r].height = tpl_pp_height
        pp.cell(r, 1, p["paper"])
        pp.cell(r, 2, p["sheet"])
        pp.cell(r, 3, p["candidates"])
        if p["placeholder"]:
            pp.cell(r, 4, PLACEHOLDERS[p["paper"]]["papers_note"])
            pp.cell(r, 4)._style = copy.copy(styles[2])

    # C_ sheets
    old = [ws for ws in wb.worksheets if ws.title.startswith("C_")]
    new = []
    for p in papers:
        rows = None if p["placeholder"] else [c for c in catalog if c["paper"] == p["paper"]]
        ws = build_c_sheet(wb, tpl, p["sheet"], rows, f"{YEAR}::{p['paper']}::")
        if p["placeholder"]:
            ws["A3"] = PLACEHOLDERS[p["paper"]]["sheet_note"]
            ws["A3"].font = copy.copy(tpl["A2"].font)
        new.append(ws)
    for ws in old:
        wb.remove(ws)

    # Checks
    ck = wb["Checks"]
    real = [p for p in papers if not p["placeholder"]]
    total = sum(p["candidates"] for p in real)
    ck["B3"] = total
    ck["B4"] = "=" + "+".join(f"COUNTIF('{p['sheet']}'!$G$2:$G${p['candidates'] + 1},\"PRIMARY READY\")" for p in real)
    ck["B5"] = "=" + "+".join(f"COUNTIF('{p['sheet']}'!$D$2:$D${p['candidates'] + 1},\"discuss\")" for p in real)

    # Codebook fixes
    cb = wb["Codebook"]
    fixes = {"Statistcal_or_numerical issue": "Statistical_or_numerical issue",
             "6  |  Candidate context": "5  |  Candidate context"}
    hits = {k: 0 for k in fixes}
    for row in cb.iter_rows():
        for c in row:
            if c.value in fixes:
                hits[c.value] += 1
                c.value = fixes[c.value]
            elif isinstance(c.value, str) and "Statistcal" in c.value:
                fail(f"unexpected 'Statistcal' text in Codebook {c.coordinate}")
    if any(v != 1 for v in hits.values()):
        fail(f"Codebook fix targets not found exactly once: {hits}")

    order = [wb["Setup"], wb["Checks"], wb["Papers"]] + new + [wb["Codebook"]]
    wb._sheets = order
    wb.active = 0
    for ws in wb.worksheets:
        ws.sheet_view.tabSelected = ws.title == "Setup"
    return wb


def main():
    papers_dirs = sorted(d.name for d in YEAR_DIR.iterdir() if d.is_dir() and d.name.startswith("jama."))
    hashes_before = {}
    for p in papers_dirs:
        rp = YEAR_DIR / p / REPORT_REL
        if rp.exists():
            hashes_before[p] = sha256(rp)
        elif p not in PLACEHOLDERS:
            fail(f"{p}: no final_report_1_6_2.md and not a declared placeholder")
    tpl_hash_before = sha256(TEMPLATE)

    catalog, papers, parse_info = [], [], {}
    for p in papers_dirs:
        if p in PLACEHOLDERS:
            if p in hashes_before:
                fail(f"{p}: declared placeholder but a 1.6.2 report exists")
            papers.append({"paper": p, "sheet": f"C_{p}", "candidates": 0, "placeholder": True,
                           "note": PLACEHOLDERS[p]["papers_note"], "report_path": None, "report_sha256": None})
            continue
        rp = YEAR_DIR / p / REPORT_REL
        cards, info = parse_report(p, rp)
        parse_info[p] = info
        rel = rp.relative_to(REPO).as_posix()
        for c in cards:
            catalog.append({"paper": p, "id": c["id"], "key": f"{YEAR}::{p}::{c['id']}", "title": c["title"],
                            "statement": c["statement"], "domain": c["domain"],
                            "relationship_type": c["relationship_type"],
                            "source_locations": c["source_locations"],
                            "source_locations_markdown": c["source_locations_markdown"],
                            "report_path": rel, "report_sha256": hashes_before[p]})
        papers.append({"paper": p, "sheet": f"C_{p}", "candidates": len(cards), "placeholder": False,
                       "note": None, "report_path": rel, "report_sha256": hashes_before[p],
                       "domain_counts": info["summary"]})
    if sorted(papers_dirs) != [p["paper"] for p in papers]:
        fail("paper order mismatch")
    if len({c["key"] for c in catalog}) != len(catalog):
        fail("duplicate keys")
    for sheetname in (p["sheet"] for p in papers):
        if len(sheetname) > 31:
            fail(f"sheet name too long: {sheetname}")

    outputs = {}
    for role in ("R_A", "R_B"):
        wb = build_workbook(role, papers, catalog)
        out = HERE / f"human_adjudication_v_2_4_1_{YEAR}_{role}.xlsx"
        wb.save(out)
        outputs[out.name] = sha256(out)

    hashes_after = {p: sha256(YEAR_DIR / p / REPORT_REL) for p in hashes_before}
    if hashes_after != hashes_before or sha256(TEMPLATE) != tpl_hash_before:
        fail("source report or template changed during build")

    doc = {"version": VERSION, "year": YEAR, "template": TEMPLATE.relative_to(REPO).as_posix(),
           "total_candidates": len(catalog), "papers": papers, "parse_checks": parse_info,
           "parse_notes": ANOMALIES, "candidates": catalog}
    (HERE / f"candidates_{YEAR}.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    oh = {"workbooks": outputs,
          "source_reports": {(YEAR_DIR / p / REPORT_REL).relative_to(REPO).as_posix(): h for p, h in hashes_before.items()},
          "template": {TEMPLATE.relative_to(REPO).as_posix(): tpl_hash_before}}
    (HERE / "output_hashes.json").write_text(json.dumps(oh, indent=2) + "\n", encoding="utf-8")

    for p in papers:
        print(p["paper"], p["candidates"], p.get("domain_counts", "placeholder"))
    print("total", len(catalog))
    for a in ANOMALIES:
        print("NOTE:", a)


if __name__ == "__main__":
    try:
        main()
    except BuildError as e:
        print("BUILD FAILED:", e, file=sys.stderr)
        sys.exit(1)
