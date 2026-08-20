#!/usr/bin/env python3
"""Prepare a fresh PDF/Office paper package with CPU-only local extraction and source hashes."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET


SOURCE_SUFFIXES = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv"}
LEGACY_MARKERS = {
    "candidate_set.md",
    "checker_outputs",
    "document_outputs",
    "verification",
    "critic",
    "final_report.md",
}
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
X_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def natural_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", value)]


def command_path(name: str) -> str | None:
    return shutil.which(name)


def existing_fresh_profile(audit: Path) -> bool:
    inventory = audit / "source_inventory.json"
    if not inventory.is_file():
        return False
    try:
        payload = json.loads(inventory.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return isinstance(payload, dict) and payload.get("profile") == "1.2.0"


def enforce_existing_source_baseline(package: Path, audit: Path, sources: list[Path]) -> None:
    baseline_path = audit / "source_hashes_before.json"
    try:
        payload = json.loads(baseline_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"EXISTING_BASELINE_INVALID: {error}") from error
    entries = payload.get("sources", []) if isinstance(payload, dict) else []
    if not isinstance(entries, list) or any(not isinstance(entry, dict) for entry in entries):
        raise SystemExit("EXISTING_BASELINE_INVALID: sources must be an array of objects.")
    expected = {str(entry.get("path", "")): entry for entry in entries}
    current = {source.name: source for source in sources}
    if set(expected) != set(current):
        raise SystemExit("SOURCE_SET_CHANGED: direct source files differ from the original 1.2.0 baseline.")
    for name, source in current.items():
        entry = expected[name]
        if source.stat().st_size != entry.get("bytes") or sha256(source) != entry.get("sha256"):
            raise SystemExit(f"SOURCE_INTEGRITY_FAILURE: {name} changed after the 1.2.0 baseline.")


def pdf_page_count(path: Path) -> int | None:
    executable = command_path("pdfinfo")
    if not executable:
        return None
    try:
        completed = subprocess.run(
            [executable, str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
    except OSError:
        return None
    if completed.returncode != 0:
        return None
    match = re.search(r"^Pages:\s+(\d+)\s*$", completed.stdout, flags=re.MULTILINE)
    return int(match.group(1)) if match else None


def extract_pdf_text(path: Path, destination: Path) -> dict[str, object]:
    executable = command_path("pdftotext")
    if not executable:
        return {"status": "TOOL_UNAVAILABLE", "tool": "pdftotext"}
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        completed = subprocess.run(
            [executable, "-layout", str(path), str(destination)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError as error:
        return {"status": "FAILED", "error": str(error)}
    if completed.returncode != 0:
        return {"status": "FAILED", "error": completed.stderr.strip()}
    characters = len(destination.read_text(encoding="utf-8", errors="replace"))
    return {"status": "EXTRACTED", "characters": characters, "path": str(destination)}


def extract_docx(path: Path, destination: Path) -> dict[str, object]:
    try:
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as error:
        return {"status": "FAILED", "error": str(error)}

    body = root.find(f"{{{W_NS}}}body")
    if body is None:
        return {"status": "FAILED", "error": "word/document.xml has no body"}
    output: list[str] = [f"# Structural extraction — {path.name}", ""]
    paragraph = 0
    table = 0
    for child in body:
        if child.tag == f"{{{W_NS}}}p":
            paragraph += 1
            text = "".join(node.text or "" for node in child.iter(f"{{{W_NS}}}t")).strip()
            if text:
                output.append(f"P{paragraph:04d}: {text}")
        elif child.tag == f"{{{W_NS}}}tbl":
            table += 1
            output.extend(["", f"## T{table:03d}", ""])
            rows = child.findall(f"{{{W_NS}}}tr")
            for row_index, row in enumerate(rows, start=1):
                cells = row.findall(f"{{{W_NS}}}tc")
                for column_index, cell in enumerate(cells, start=1):
                    text = " ".join(
                        "".join(node.text or "" for node in paragraph_node.iter(f"{{{W_NS}}}t"))
                        for paragraph_node in cell.findall(f".//{{{W_NS}}}p")
                    ).strip()
                    output.append(
                        f"T{table:03d} R{row_index:03d} C{column_index:03d}: {text}"
                    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(output) + "\n", encoding="utf-8")
    return {
        "status": "EXTRACTED",
        "paragraph_count": paragraph,
        "table_count": table,
        "path": str(destination),
    }


def normalized_xlsx_target(target: str) -> str:
    normalized = posixpath.normpath(target.replace("\\", "/")).lstrip("/")
    while normalized.startswith("../"):
        normalized = normalized[3:]
    pure = PurePosixPath(normalized)
    if pure.is_absolute():
        pure = PurePosixPath(*pure.parts[1:])
    if pure.parts and pure.parts[0] == "xl":
        return pure.as_posix()
    return (PurePosixPath("xl") / pure).as_posix()


def extract_xlsx(path: Path, json_destination: Path, markdown_destination: Path) -> dict[str, object]:
    try:
        archive = zipfile.ZipFile(path)
    except (OSError, zipfile.BadZipFile) as error:
        return {"status": "FAILED", "error": str(error)}
    with archive:
        try:
            workbook = ET.fromstring(archive.read("xl/workbook.xml"))
            relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        except (KeyError, ET.ParseError) as error:
            return {"status": "FAILED", "error": str(error)}

        shared: list[str] = []
        try:
            shared_root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in shared_root.findall(f"{{{X_NS}}}si"):
                shared.append("".join(node.text or "" for node in item.iter(f"{{{X_NS}}}t")))
        except KeyError:
            pass

        relation_targets = {
            node.attrib.get("Id", ""): normalized_xlsx_target(node.attrib.get("Target", ""))
            for node in relationships.findall(f"{{{PKG_REL_NS}}}Relationship")
        }
        sheet_records: list[dict[str, object]] = []
        sheets_parent = workbook.find(f"{{{X_NS}}}sheets")
        if sheets_parent is not None:
            for sheet in sheets_parent.findall(f"{{{X_NS}}}sheet"):
                name = sheet.attrib.get("name", "Unnamed")
                relation_id = sheet.attrib.get(f"{{{R_NS}}}id", "")
                target = relation_targets.get(relation_id, "")
                cells: list[dict[str, str]] = []
                try:
                    worksheet = ET.fromstring(archive.read(target))
                except (KeyError, ET.ParseError):
                    sheet_records.append({"name": name, "source_part": target, "cells": cells})
                    continue
                for cell in worksheet.iter(f"{{{X_NS}}}c"):
                    reference = cell.attrib.get("r", "")
                    value_node = cell.find(f"{{{X_NS}}}v")
                    formula_node = cell.find(f"{{{X_NS}}}f")
                    cell_type = cell.attrib.get("t", "")
                    raw = value_node.text if value_node is not None and value_node.text else ""
                    displayed = raw
                    if cell_type == "s" and raw.isdigit() and int(raw) < len(shared):
                        displayed = shared[int(raw)]
                    elif cell_type == "inlineStr":
                        displayed = "".join(
                            node.text or "" for node in cell.iter(f"{{{X_NS}}}t")
                        )
                    elif cell_type == "b":
                        displayed = "TRUE" if raw == "1" else "FALSE"
                    formula = formula_node.text if formula_node is not None and formula_node.text else ""
                    if displayed or formula:
                        cells.append(
                            {
                                "cell": reference,
                                "displayed_or_cached_value": displayed,
                                "formula": formula,
                                "cell_type": cell_type,
                            }
                        )
                sheet_records.append({"name": name, "source_part": target, "cells": cells})

    payload = {
        "schema_version": 1,
        "source": path.name,
        "note": "Formula results are cached workbook values; this extractor does not recalculate formulas.",
        "sheets": sheet_records,
    }
    json_destination.parent.mkdir(parents=True, exist_ok=True)
    json_destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [f"# Workbook extraction — {path.name}", "", payload["note"], ""]
    for sheet in sheet_records:
        lines.extend([f"## Worksheet: {sheet['name']}", "", "| Cell | Displayed/cached value | Formula |", "|---|---|---|"])
        for cell in sheet["cells"]:
            values = [str(cell[key]).replace("|", "\\|").replace("\n", " ") for key in ("cell", "displayed_or_cached_value", "formula")]
            lines.append(f"| {values[0]} | {values[1]} | {values[2]} |")
        lines.append("")
    markdown_destination.write_text("\n".join(lines), encoding="utf-8")
    return {
        "status": "EXTRACTED",
        "sheet_count": len(sheet_records),
        "nonempty_cell_count": sum(len(sheet["cells"]) for sheet in sheet_records),
        "json_path": str(json_destination),
        "markdown_path": str(markdown_destination),
    }


def extract_csv(path: Path, destination: Path) -> dict[str, object]:
    raw = path.read_bytes()
    encoding = "utf-8-sig"
    try:
        text = raw.decode(encoding)
    except UnicodeDecodeError:
        encoding = "latin-1"
        text = raw.decode(encoding)
    rows = list(csv.reader(text.splitlines()))
    output = [f"# CSV extraction — {path.name}", "", f"Encoding: `{encoding}`", ""]
    for index, row in enumerate(rows, start=1):
        output.append(f"Row {index}: " + " | ".join(f"C{column + 1}={value}" for column, value in enumerate(row)))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(output) + "\n", encoding="utf-8")
    return {"status": "EXTRACTED", "row_count": len(rows), "path": str(destination)}


def convert_office(path: Path, destination_dir: Path) -> dict[str, object]:
    executable = command_path("libreoffice") or command_path("soffice")
    if not executable:
        return {"status": "TOOL_UNAVAILABLE", "tool": "libreoffice"}
    destination_dir.mkdir(parents=True, exist_ok=True)
    try:
        completed = subprocess.run(
            [executable, "--headless", "--convert-to", "pdf", "--outdir", str(destination_dir), str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        return {"status": "FAILED", "error": "LibreOffice conversion timed out after 180 seconds."}
    except OSError as error:
        return {"status": "FAILED", "error": str(error)}
    pdfs = sorted(destination_dir.glob("*.pdf"))
    if completed.returncode != 0 or not pdfs:
        return {"status": "FAILED", "error": (completed.stderr or completed.stdout).strip()}
    derived = pdfs[0]
    return {
        "status": "CONVERTED",
        "path": str(derived),
        "bytes": derived.stat().st_size,
        "sha256": sha256(derived),
        "page_count": pdf_page_count(derived),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=Path("."))
    args = parser.parse_args()
    package = args.package.expanduser().resolve()
    audit = package / ".ai_paper_validation"

    if audit.is_dir():
        has_known_legacy_marker = any((audit / marker).exists() for marker in LEGACY_MARKERS)
        has_any_record = any(audit.iterdir())
        if has_known_legacy_marker or (has_any_record and not existing_fresh_profile(audit)):
            raise SystemExit(
                "LEGACY_OR_UNKNOWN_AUDIT_DETECTED: do not use 1.2.0; preserve the existing records "
                "and select the applicable recovery workflow."
            )

    sources = sorted(
        [path for path in package.iterdir() if path.is_file() and path.suffix.casefold() in SOURCE_SUFFIXES],
        key=lambda item: natural_key(item.name),
    )
    if not sources or not any(path.suffix.casefold() in {".pdf", ".doc", ".docx"} for path in sources):
        raise SystemExit("FRESH_PACKAGE_INVALID: no main-paper-capable PDF/DOC/DOCX source was found.")

    if existing_fresh_profile(audit):
        enforce_existing_source_baseline(package, audit, sources)

    audit.mkdir(parents=True, exist_ok=True)
    preprocessing = audit / "preprocessing"
    entries: list[dict[str, object]] = []
    for index, source in enumerate(sources, start=1):
        document_id = f"DOC{index:03d}"
        suffix = source.suffix.casefold()
        entry: dict[str, object] = {
            "document_id": document_id,
            "path": source.name,
            "format": suffix.lstrip(".").upper(),
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "page_count": pdf_page_count(source) if suffix == ".pdf" else None,
            "preparation": {},
        }
        preparation: dict[str, object] = entry["preparation"]  # type: ignore[assignment]
        if suffix == ".pdf":
            preparation["native_text"] = extract_pdf_text(
                source, preprocessing / "native_text" / f"{document_id}.txt"
            )
        elif suffix == ".docx":
            preparation["structural_text"] = extract_docx(
                source, preprocessing / "office_text" / f"{document_id}.md"
            )
            preparation["derived_pdf"] = convert_office(
                source, preprocessing / "converted_pdf" / document_id
            )
        elif suffix == ".doc":
            preparation["derived_pdf"] = convert_office(
                source, preprocessing / "converted_pdf" / document_id
            )
        elif suffix == ".xlsx":
            preparation["workbook_cells"] = extract_xlsx(
                source,
                preprocessing / "workbooks" / f"{document_id}.json",
                preprocessing / "workbooks" / f"{document_id}.md",
            )
            preparation["derived_pdf"] = convert_office(
                source, preprocessing / "converted_pdf" / document_id
            )
        elif suffix == ".xls":
            preparation["derived_pdf"] = convert_office(
                source, preprocessing / "converted_pdf" / document_id
            )
        elif suffix == ".csv":
            preparation["rows"] = extract_csv(
                source, preprocessing / "workbooks" / f"{document_id}.md"
            )
        entries.append(entry)

    created = dt.datetime.now(dt.timezone.utc).isoformat()
    payload = {
        "schema_version": 1,
        "profile": "1.2.0",
        "preflight_status": "FRESH_PACKAGE",
        "package": package.name,
        "created_at_utc": created,
        "runtime": {"platform": "linux", "cpu_only": True, "gpu_allowed": False},
        "sources": entries,
    }
    (audit / "source_inventory.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (audit / "source_hashes_before.json").write_text(
        json.dumps(
            {"schema_version": 1, "sources": [{key: entry[key] for key in ("path", "bytes", "sha256")} for entry in entries]},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (audit / "run_state.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "profile": "1.2.0",
                "status": "INITIALIZED",
                "started_at_utc": created,
                "autonomous": True,
                "cpu_only": True,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Fresh package source inventory",
        "",
        "- Profile: `1.2.0`",
        "- Preflight: `FRESH_PACKAGE`",
        "- Runtime: Linux CPU-only",
        "",
        "| Document | Source | Format | Bytes | SHA-256 | Pages |",
        "|---|---|---|---:|---|---:|",
    ]
    for entry in entries:
        lines.append(
            f"| {entry['document_id']} | `{entry['path']}` | {entry['format']} | {entry['bytes']} | `{entry['sha256']}` | {entry['page_count'] or ''} |"
        )
    (audit / "source_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "FRESH_PACKAGE",
                "profile": "1.2.0",
                "sources": len(entries),
                "cpu_only": True,
                "audit": str(audit),
            }
        )
    )


if __name__ == "__main__":
    main()
