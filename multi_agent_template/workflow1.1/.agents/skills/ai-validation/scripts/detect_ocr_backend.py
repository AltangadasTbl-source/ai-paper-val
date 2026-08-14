#!/usr/bin/env python3
"""Write a validated OCR-backend report for the PDF preprocessing workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ocr_backend import select_ocr_backend


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("auto", "gpu", "cpu"), default="auto")
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the JSON report here. The parent directory is created if needed.",
    )
    parser.add_argument(
        "--require-selected",
        choices=("rapidocr-cuda", "rapidocr-cpu", "tesseract-cpu"),
        help="Exit unsuccessfully unless this exact backend is selected.",
    )
    args = parser.parse_args()
    report = select_ocr_backend(args.mode)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    if args.require_selected and report.get("selected_backend") != args.require_selected:
        raise SystemExit(
            f"Required OCR backend {args.require_selected!r}, but selected "
            f"{report.get('selected_backend')!r}. See the backend report for details."
        )


if __name__ == "__main__":
    main()
