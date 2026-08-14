#!/usr/bin/env python3
"""Run the exact OCR backend configured for one paper package."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tomllib
from pathlib import Path


VALID_PAIRS = {
    "gpu": {"rapidocr-cuda"},
    "cpu": {"rapidocr-cpu", "tesseract-cpu"},
}


def resolve_from(base: Path, path: Path) -> Path:
    return path.expanduser().resolve() if path.is_absolute() else (base / path).resolve()


def under_audit(path: Path, package: Path, label: str) -> Path:
    resolved = resolve_from(package, path)
    audit = (package / "audit").resolve()
    if not resolved.is_relative_to(audit):
        raise SystemExit(f"{label} must remain below {audit}: {resolved}")
    return resolved


def default_config() -> Path:
    return Path(__file__).resolve().parents[4] / "ai-validation.toml"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=default_config())
    parser.add_argument("--package", type=Path, default=Path.cwd())
    commands = parser.add_subparsers(dest="action", required=True)
    detect = commands.add_parser("detect")
    detect.add_argument("--output", type=Path, default=Path("audit/preprocessing/ocr_backend.json"))
    page = commands.add_parser("page")
    page.add_argument("image", type=Path)
    page.add_argument("output", type=Path)
    page.add_argument("--metadata", type=Path, required=True)
    args = parser.parse_args()

    package = args.package.expanduser().resolve()
    config_path = args.config.expanduser().resolve()
    with config_path.open("rb") as handle:
        settings = tomllib.load(handle)
    ocr = settings["ocr"]
    mode = str(ocr["mode"])
    required_backend = str(ocr["required_backend"])
    if ocr.get("allow_implicit_fallback") is not False:
        raise SystemExit("Implicit OCR fallback must remain disabled.")
    if mode not in VALID_PAIRS or required_backend not in VALID_PAIRS[mode]:
        raise SystemExit(
            "Configure gpu with rapidocr-cuda, or cpu with rapidocr-cpu or tesseract-cpu."
        )

    environment = os.environ.copy()
    environment["AI_VALIDATION_NVIDIA_SMI"] = str(ocr.get("nvidia_smi", "nvidia-smi"))
    scripts = Path(__file__).resolve().parent
    if args.action == "detect":
        output = under_audit(args.output, package, "OCR backend report")
        output.parent.mkdir(parents=True, exist_ok=True)
        command = [
            sys.executable,
            str(scripts / "detect_ocr_backend.py"),
            "--mode",
            mode,
            "--require-selected",
            required_backend,
            "--output",
            str(output),
        ]
    else:
        image = under_audit(args.image, package, "Rendered page")
        output = under_audit(args.output, package, "OCR text")
        metadata = under_audit(args.metadata, package, "OCR metadata")
        if not image.is_file():
            raise SystemExit(f"Rendered page does not exist: {image}")
        output.parent.mkdir(parents=True, exist_ok=True)
        metadata.parent.mkdir(parents=True, exist_ok=True)
        command = [
            sys.executable,
            str(scripts / "ocr_page.py"),
            str(image),
            str(output),
            "--mode",
            mode,
            "--require-selected",
            required_backend,
            "--metadata",
            str(metadata),
        ]
    raise SystemExit(subprocess.run(command, env=environment).returncode)


if __name__ == "__main__":
    main()
