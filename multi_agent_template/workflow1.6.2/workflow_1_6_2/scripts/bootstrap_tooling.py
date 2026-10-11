#!/usr/bin/env python3
"""Create or remove the temporary package-local fallback tooling environment for workflow 1.6.2.

Standard library only. The environment lives inside the current review directory and is removed
after validation. It is used only when direct local tools (pdfinfo, pdftotext, pdftoppm/pdftocairo,
tesseract) are unavailable. Run from the paper-package root:

  python3 workflow_1_6_2/scripts/bootstrap_tooling.py create [--ocr]
  python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import venv
from pathlib import Path

TOOLING_DIR = Path(".ai_paper_validation/review_1_6_2/tooling")
VENV_DIR = TOOLING_DIR / "venv"
LOG_PATH = TOOLING_DIR / "bootstrap_log.json"
# Pinned for reproducibility; the floor specs are used only if a pinned wheel is unavailable for the
# local interpreter or platform, and that substitution is recorded.
PDF_PACKAGES = [("pymupdf==1.26.4", "pymupdf>=1.26.4"), ("pypdf==5.9.0", "pypdf>=5.9.0")]
OCR_PACKAGES = [("rapidocr-onnxruntime==1.3.24", "rapidocr-onnxruntime>=1.3.24")]


def venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def pip_install(spec: str) -> tuple[bool, str]:
    env = dict(os.environ, PIP_CACHE_DIR=str((TOOLING_DIR / "pip-cache").resolve()),
               PIP_DISABLE_PIP_VERSION_CHECK="1")
    result = subprocess.run(
        [str(venv_python()), "-m", "pip", "install", "--quiet", spec],
        capture_output=True, text=True, env=env,
    )
    return result.returncode == 0, (result.stderr or result.stdout).strip()[-800:]


def create(with_ocr: bool) -> int:
    if not Path(".ai_paper_validation").is_dir():
        print("Run from the paper-package root.", file=sys.stderr)
        return 2
    TOOLING_DIR.mkdir(parents=True, exist_ok=True)
    log: dict[str, object] = {
        "created_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "python": sys.version.split()[0],
        "platform": sys.platform,
        "venv": VENV_DIR.as_posix(),
        "packages": [],
        "status": "FAILED",
    }
    if not venv_python().is_file():
        venv.EnvBuilder(with_pip=True, clear=False).create(VENV_DIR)
    groups = PDF_PACKAGES + (OCR_PACKAGES if with_ocr else [])
    ok_all = True
    for pinned, floor in groups:
        ok, message = pip_install(pinned)
        record = {"requested": pinned, "installed_spec": pinned if ok else None, "pin_substituted": False}
        if not ok:
            ok, message2 = pip_install(floor)
            record.update(installed_spec=floor if ok else None, pin_substituted=ok,
                          error=None if ok else f"{message} | {message2}")
        ok_all &= ok
        log["packages"].append(record)
    freeze = subprocess.run([str(venv_python()), "-m", "pip", "freeze"], capture_output=True, text=True)
    log["pip_freeze"] = freeze.stdout.split()
    pdf_ok = all(item["installed_spec"] for item in log["packages"][: len(PDF_PACKAGES)])
    log["status"] = "READY" if ok_all else ("PARTIAL" if pdf_ok else "FAILED")
    LOG_PATH.write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": log["status"], "python": str(venv_python()), "log": LOG_PATH.as_posix()}))
    if log["status"] == "FAILED":
        print("Installation failed (often no network in the sandbox). Record this in "
              "tooling_record.md and continue with reusable assets and available tools.", file=sys.stderr)
        return 1
    return 0


def remove() -> int:
    removed = []
    for path in (VENV_DIR, TOOLING_DIR / "pip-cache"):
        if path.exists():
            shutil.rmtree(path)
            removed.append(path.as_posix())
    if LOG_PATH.is_file():
        log = json.loads(LOG_PATH.read_text(encoding="utf-8"))
        log["removed_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        LOG_PATH.write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"removed": removed}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    create_parser = sub.add_parser("create")
    create_parser.add_argument("--ocr", action="store_true", help="also install CPU OCR (only if tesseract is absent)")
    sub.add_parser("remove")
    args = parser.parse_args()
    return create(args.ocr) if args.command == "create" else remove()


if __name__ == "__main__":
    raise SystemExit(main())
