#!/usr/bin/env python3
"""Run Tesseract CPU OCR on one selected page image and retain backend provenance."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("text", type=Path)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--language", default="eng")
    args = parser.parse_args()

    image = args.image.expanduser().resolve()
    output = args.text.expanduser().resolve()
    metadata = (args.metadata or output.with_suffix(".json")).expanduser().resolve()
    if not image.is_file():
        parser.error(f"Page image does not exist: {image}")
    executable = shutil.which("tesseract")
    if not executable:
        raise SystemExit("CPU_OCR_UNAVAILABLE: tesseract was not found; GPU fallback is forbidden.")

    output.parent.mkdir(parents=True, exist_ok=True)
    metadata.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        [executable, str(image), "stdout", "-l", args.language, "--psm", "6"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    record = {
        "schema_version": 1,
        "backend": "tesseract-cpu",
        "gpu_used": False,
        "image": str(image),
        "text": str(output),
        "language": args.language,
        "completed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "returncode": completed.returncode,
        "stderr": completed.stderr.strip(),
    }
    metadata.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if completed.returncode != 0:
        raise SystemExit(f"CPU_OCR_FAILED: {completed.stderr.strip()}")
    output.write_text(completed.stdout, encoding="utf-8")
    print(json.dumps({"status": "PASS", "backend": "tesseract-cpu", "text": str(output)}))


if __name__ == "__main__":
    main()
