#!/usr/bin/env python3
"""Fallback equivalents of direct local PDF, OCR, and hashing tools for workflow 1.6.2.

Use a direct tool whenever it is available. Use this helper only for a capability that the tool
probe recorded as missing, with the interpreter of the temporary fallback environment for PDF/OCR
commands:

  python3 workflow_1_6_2/scripts/pdf_tools.py probe
  python3 workflow_1_6_2/scripts/pdf_tools.py sha256 FILE [FILE ...]
  VENV_PY workflow_1_6_2/scripts/pdf_tools.py info SOURCE.pdf
  VENV_PY workflow_1_6_2/scripts/pdf_tools.py text SOURCE.pdf --first N --last N OUT.txt [--layout]
  VENV_PY workflow_1_6_2/scripts/pdf_tools.py render SOURCE.pdf --page N OUT.png [--dpi 200]
  VENV_PY workflow_1_6_2/scripts/pdf_tools.py ocr PAGE.png OUT.txt

VENV_PY is .ai_paper_validation/review_1_6_2/tooling/venv/bin/python (Scripts\\python.exe on Windows).
The helper reads sources only and writes only the named output path.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

DIRECT_TOOLS = ("pdfinfo", "pdftotext", "pdftoppm", "pdftocairo", "tesseract", "libreoffice", "soffice",
                "pandoc", "sha256sum", "shasum")
MODULES = ("fitz", "pypdf", "rapidocr_onnxruntime")


def has_module(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def cmd_probe(_: argparse.Namespace) -> int:
    tools = {name: shutil.which(name) for name in DIRECT_TOOLS}
    modules = {name: has_module(name) for name in MODULES}
    capabilities = {
        "pdf_info": bool(tools["pdfinfo"]),
        "pdf_text": bool(tools["pdftotext"]),
        "pdf_render": bool(tools["pdftoppm"] or tools["pdftocairo"]),
        "ocr": bool(tools["tesseract"]),
        "office_conversion": bool(tools["libreoffice"] or tools["soffice"]),
        "sha256": True,  # this helper's sha256 command is always available
    }
    print(json.dumps({"python": sys.version.split()[0], "platform": sys.platform, "direct_tools": tools,
                      "python_modules_in_this_interpreter": modules,
                      "direct_capabilities": capabilities,
                      "fallback_environment_needed": not all(
                          capabilities[k] for k in ("pdf_info", "pdf_text", "pdf_render"))}, indent=2))
    return 0


def cmd_sha256(args: argparse.Namespace) -> int:
    for name in args.files:
        digest = hashlib.sha256()
        with open(name, "rb") as handle:
            for chunk in iter(lambda: handle.read(1 << 20), b""):
                digest.update(chunk)
        print(f"{digest.hexdigest()}  {name}")
    return 0


def open_fitz(path: str):
    import fitz  # PyMuPDF

    return fitz.open(path)


def cmd_info(args: argparse.Namespace) -> int:
    if has_module("fitz"):
        doc = open_fitz(args.source)
        info = {"pages": doc.page_count, "encrypted": doc.is_encrypted, "metadata": doc.metadata,
                "engine": "pymupdf"}
    elif has_module("pypdf"):
        from pypdf import PdfReader

        reader = PdfReader(args.source)
        info = {"pages": len(reader.pages), "encrypted": reader.is_encrypted,
                "metadata": {k: str(v) for k, v in (reader.metadata or {}).items()}, "engine": "pypdf"}
    else:
        print("No PDF engine available; run bootstrap_tooling.py create.", file=sys.stderr)
        return 3
    print(json.dumps(info, indent=2, default=str))
    return 0


def page_range(count: int, first: int, last: int) -> range:
    if not (1 <= first <= last <= count):
        raise SystemExit(f"Page range {first}-{last} is outside 1-{count}.")
    return range(first, last + 1)


def cmd_text(args: argparse.Namespace) -> int:
    chunks: list[str] = []
    if has_module("fitz"):
        doc = open_fitz(args.source)
        for number in page_range(doc.page_count, args.first, args.last):
            page = doc[number - 1]
            text = page.get_text("text", sort=True) if args.layout else page.get_text("text")
            chunks.append(text)
        engine = "pymupdf (sorted reading order)" if args.layout else "pymupdf"
    elif has_module("pypdf"):
        from pypdf import PdfReader

        reader = PdfReader(args.source)
        for number in page_range(len(reader.pages), args.first, args.last):
            page = reader.pages[number - 1]
            chunks.append(page.extract_text(extraction_mode="layout") if args.layout else page.extract_text())
        engine = "pypdf (layout mode)" if args.layout else "pypdf"
    else:
        print("No PDF engine available; run bootstrap_tooling.py create.", file=sys.stderr)
        return 3
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    # Form feed between pages matches pdftotext page separation.
    Path(args.out).write_text("\f".join(chunks), encoding="utf-8")
    print(json.dumps({"engine": engine, "pages": f"{args.first}-{args.last}", "out": args.out}))
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    if not has_module("fitz"):
        print("Page rendering needs PyMuPDF; run bootstrap_tooling.py create.", file=sys.stderr)
        return 3
    doc = open_fitz(args.source)
    page_range(doc.page_count, args.page, args.page)
    pixmap = doc[args.page - 1].get_pixmap(dpi=args.dpi)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    pixmap.save(args.out)
    print(json.dumps({"engine": "pymupdf", "page": args.page, "dpi": args.dpi, "out": args.out}))
    return 0


def cmd_ocr(args: argparse.Namespace) -> int:
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    if shutil.which("tesseract"):
        base = str(Path(args.out).with_suffix(""))
        subprocess.run(["tesseract", args.image, base, "-l", "eng", "--psm", "6"], check=True)
        engine = "tesseract"
    elif has_module("rapidocr_onnxruntime"):
        from rapidocr_onnxruntime import RapidOCR

        result, _ = RapidOCR()(args.image)
        lines = [item[1] for item in (result or [])]
        Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
        engine = "rapidocr-onnxruntime (CPU)"
    else:
        print("No OCR engine available; run bootstrap_tooling.py create --ocr, or inspect the rendered "
              "page visually and record the limitation.", file=sys.stderr)
        return 3
    print(json.dumps({"engine": engine, "image": args.image, "out": args.out}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("probe").set_defaults(func=cmd_probe)
    p = sub.add_parser("sha256"); p.add_argument("files", nargs="+"); p.set_defaults(func=cmd_sha256)
    p = sub.add_parser("info"); p.add_argument("source"); p.set_defaults(func=cmd_info)
    p = sub.add_parser("text"); p.add_argument("source"); p.add_argument("--first", type=int, required=True)
    p.add_argument("--last", type=int, required=True); p.add_argument("out"); p.add_argument("--layout", action="store_true")
    p.set_defaults(func=cmd_text)
    p = sub.add_parser("render"); p.add_argument("source"); p.add_argument("--page", type=int, required=True)
    p.add_argument("out"); p.add_argument("--dpi", type=int, default=200); p.set_defaults(func=cmd_render)
    p = sub.add_parser("ocr"); p.add_argument("image"); p.add_argument("out"); p.set_defaults(func=cmd_ocr)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
