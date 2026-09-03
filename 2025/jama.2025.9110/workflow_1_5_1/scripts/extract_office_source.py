#!/usr/bin/env python3
"""Extract stable DOCX/XLSX/CSV locations and optionally derive an Office PDF, CPU-only."""

from __future__ import annotations

import argparse
import csv
import json
import posixpath
import shutil
import subprocess
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
X_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def docx_extract(source: Path, markdown: Path) -> dict[str, object]:
    try:
        with zipfile.ZipFile(source) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as error:
        return {"status": "FAILED", "error": str(error)}
    body = root.find(f"{{{W_NS}}}body")
    if body is None:
        return {"status": "FAILED", "error": "DOCX body is absent."}
    lines = [f"# Structural extraction — {source.name}", ""]
    paragraph_count = table_count = 0
    for child in body:
        if child.tag == f"{{{W_NS}}}p":
            paragraph_count += 1
            value = "".join(node.text or "" for node in child.iter(f"{{{W_NS}}}t")).strip()
            if value:
                lines.append(f"P{paragraph_count:04d}: {value}")
        elif child.tag == f"{{{W_NS}}}tbl":
            table_count += 1
            lines.extend(["", f"## T{table_count:03d}", ""])
            for row_number, row in enumerate(child.findall(f"{{{W_NS}}}tr"), 1):
                for column_number, cell in enumerate(row.findall(f"{{{W_NS}}}tc"), 1):
                    value = " ".join(
                        "".join(node.text or "" for node in paragraph.iter(f"{{{W_NS}}}t"))
                        for paragraph in cell.findall(f".//{{{W_NS}}}p")
                    ).strip()
                    lines.append(
                        f"T{table_count:03d} R{row_number:03d} C{column_number:03d}: {value}"
                    )
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"status": "EXTRACTED", "paragraphs": paragraph_count, "tables": table_count}


def xlsx_part(target: str) -> str:
    normalized = posixpath.normpath(target.replace("\\", "/")).lstrip("/")
    while normalized.startswith("../"):
        normalized = normalized[3:]
    return normalized if normalized.startswith("xl/") else f"xl/{normalized}"


def xlsx_extract(source: Path, markdown: Path, json_path: Path) -> dict[str, object]:
    try:
        archive = zipfile.ZipFile(source)
    except (OSError, zipfile.BadZipFile) as error:
        return {"status": "FAILED", "error": str(error)}
    with archive:
        try:
            workbook = ET.fromstring(archive.read("xl/workbook.xml"))
            relations = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        except (KeyError, ET.ParseError) as error:
            return {"status": "FAILED", "error": str(error)}
        shared: list[str] = []
        try:
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            shared = ["".join(node.text or "" for node in item.iter(f"{{{X_NS}}}t")) for item in root.findall(f"{{{X_NS}}}si")]
        except (KeyError, ET.ParseError):
            pass
        targets = {
            node.attrib.get("Id", ""): xlsx_part(node.attrib.get("Target", ""))
            for node in relations.findall(f"{{{PKG_REL_NS}}}Relationship")
        }
        sheets: list[dict[str, object]] = []
        parent = workbook.find(f"{{{X_NS}}}sheets")
        for sheet in parent.findall(f"{{{X_NS}}}sheet") if parent is not None else []:
            name = sheet.attrib.get("name", "Unnamed")
            part = targets.get(sheet.attrib.get(f"{{{R_NS}}}id", ""), "")
            cells: list[dict[str, str]] = []
            try:
                worksheet = ET.fromstring(archive.read(part))
            except (KeyError, ET.ParseError):
                sheets.append({"worksheet": name, "part": part, "cells": cells})
                continue
            for cell in worksheet.iter(f"{{{X_NS}}}c"):
                value_node, formula_node = cell.find(f"{{{X_NS}}}v"), cell.find(f"{{{X_NS}}}f")
                raw = value_node.text if value_node is not None and value_node.text else ""
                value, cell_type = raw, cell.attrib.get("t", "")
                if cell_type == "s" and raw.isdigit() and int(raw) < len(shared):
                    value = shared[int(raw)]
                elif cell_type == "inlineStr":
                    value = "".join(node.text or "" for node in cell.iter(f"{{{X_NS}}}t"))
                formula = formula_node.text if formula_node is not None and formula_node.text else ""
                if value or formula:
                    cells.append({"cell": cell.attrib.get("r", ""), "value": value, "formula": formula})
            sheets.append({"worksheet": name, "part": part, "cells": cells})
    payload = {"source": source.name, "cached_values_not_recalculated": True, "sheets": sheets}
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [f"# Workbook extraction — {source.name}", "", "Formula values are cached and were not recalculated.", ""]
    for sheet in sheets:
        lines.extend([f"## Worksheet: {sheet['worksheet']}", "", "| Cell | Cached value | Formula |", "|---|---|---|"])
        for cell in sheet["cells"]:
            values = [str(cell[key]).replace("|", "\\|").replace("\n", " ") for key in ("cell", "value", "formula")]
            lines.append(f"| {values[0]} | {values[1]} | {values[2]} |")
        lines.append("")
    markdown.write_text("\n".join(lines), encoding="utf-8")
    return {"status": "EXTRACTED", "worksheets": len(sheets), "cells": sum(len(sheet["cells"]) for sheet in sheets)}


def csv_extract(source: Path, markdown: Path) -> dict[str, object]:
    raw = source.read_bytes()
    try:
        text, encoding = raw.decode("utf-8-sig"), "utf-8-sig"
    except UnicodeDecodeError:
        text, encoding = raw.decode("latin-1"), "latin-1"
    rows = list(csv.reader(text.splitlines()))
    lines = [f"# CSV extraction — {source.name}", "", f"Encoding: `{encoding}`", ""]
    lines.extend(
        f"Row {row_number}: " + " | ".join(f"C{column_number}={value}" for column_number, value in enumerate(row, 1))
        for row_number, row in enumerate(rows, 1)
    )
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"status": "EXTRACTED", "rows": len(rows), "encoding": encoding}


def derive_pdf(source: Path, output_dir: Path) -> dict[str, object]:
    executable = shutil.which("libreoffice") or shutil.which("soffice")
    if not executable:
        return {"status": "TOOL_UNAVAILABLE", "tool": "libreoffice"}
    try:
        completed = subprocess.run(
            [executable, "--headless", "--convert-to", "pdf", "--outdir", str(output_dir), str(source)],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180,
        )
    except subprocess.TimeoutExpired:
        return {"status": "FAILED", "error": "LibreOffice conversion timed out after 180 seconds."}
    except OSError as error:
        return {"status": "FAILED", "error": str(error)}
    pdf = output_dir / f"{source.stem}.pdf"
    return {"status": "CONVERTED", "path": str(pdf)} if completed.returncode == 0 and pdf.is_file() else {
        "status": "FAILED", "error": (completed.stderr or completed.stdout).strip()
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    source, output_dir = args.source.resolve(), args.output_dir.resolve()
    if not source.is_file():
        raise SystemExit(f"Source does not exist: {source}")
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix, stem = source.suffix.casefold(), source.stem
    if suffix == ".docx":
        extraction = docx_extract(source, output_dir / f"{stem}.md")
    elif suffix == ".xlsx":
        extraction = xlsx_extract(source, output_dir / f"{stem}.md", output_dir / f"{stem}.json")
    elif suffix == ".csv":
        extraction = csv_extract(source, output_dir / f"{stem}.md")
    elif suffix in {".doc", ".xls"}:
        extraction = {"status": "BINARY_OFFICE_REQUIRES_CONVERSION"}
    else:
        raise SystemExit("Supported formats are DOC, DOCX, XLS, XLSX, and CSV.")
    conversion = derive_pdf(source, output_dir) if suffix in {".doc", ".docx", ".xls", ".xlsx"} else {"status": "NOT_APPLICABLE"}
    summary = {"source": str(source), "cpu_only": True, "extraction": extraction, "derived_pdf": conversion}
    (output_dir / f"{stem}.extraction.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
