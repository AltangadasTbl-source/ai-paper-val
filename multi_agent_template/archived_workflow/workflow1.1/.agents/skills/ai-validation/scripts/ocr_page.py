#!/usr/bin/env python3
"""OCR one rendered page with the validated GPU-first backend selection."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from statistics import fmean

from ocr_backend import initialize_selected_rapidocr, select_ocr_backend


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def _rapidocr(image: Path, report: dict[str, object]) -> tuple[str, float | None]:
    ocr = initialize_selected_rapidocr(report)
    result, _elapsed = ocr(str(image))
    lines: list[str] = []
    confidences: list[float] = []
    for item in result or []:
        if len(item) > 1:
            lines.append(str(item[1]))
        if len(item) > 2:
            try:
                confidences.append(float(item[2]))
            except (TypeError, ValueError):
                pass
    return "\n".join(lines) + ("\n" if lines else ""), fmean(confidences) if confidences else None


def _tesseract(image: Path, psm: int) -> tuple[str, float | None]:
    completed = subprocess.run(
        ["tesseract", str(image), "stdout", "--psm", str(psm)],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout, None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Rendered PNG or other image input.")
    parser.add_argument("output", type=Path, help="Destination UTF-8 OCR text file.")
    parser.add_argument("--mode", choices=("auto", "gpu", "cpu"), default="auto")
    parser.add_argument(
        "--require-selected",
        choices=("rapidocr-cuda", "rapidocr-cpu", "tesseract-cpu"),
        help="Fail unless the selected backend matches this exact value.",
    )
    parser.add_argument("--psm", type=int, default=3, help="Tesseract page segmentation mode if used.")
    parser.add_argument("--metadata", type=Path, help="Optional JSON record for the page manifest.")
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error(f"Input image does not exist: {args.image}")

    report = select_ocr_backend(args.mode)
    backend = report["selected_backend"]
    if args.require_selected and backend != args.require_selected:
        raise RuntimeError(
            f"Required OCR backend {args.require_selected!r}, but selected {backend!r}."
        )
    if args.mode == "gpu" and backend != "rapidocr-cuda":
        raise RuntimeError(
            "GPU OCR was required, but validated RapidOCR CUDA was not available. "
            f"Selected backend: {backend!r}. CPU fallback is disabled for GPU OCR tasks."
        )
    if backend.startswith("rapidocr-"):
        text, confidence = _rapidocr(args.image, report)
    elif backend == "tesseract-cpu":
        text, confidence = _tesseract(args.image, args.psm)
    else:
        raise RuntimeError(str(report["reason"]))

    _write_text(args.output, text)
    metadata = {
        "status": "completed",
        "input_image": str(args.image),
        "output_text": str(args.output),
        "characters": len(text),
        "mean_confidence": confidence,
        "ocr_backend": report,
    }
    if args.metadata:
        args.metadata.parent.mkdir(parents=True, exist_ok=True)
        args.metadata.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
