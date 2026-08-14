#!/usr/bin/env python3
"""Run page-scoped RapidOCR with CUDA and retain page-level provenance."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    return parser.parse_args()


def gpu_identity() -> str:
    command = [
        "nvidia-smi",
        "--query-gpu=name,memory.total,driver_version",
        "--format=csv,noheader",
    ]
    return subprocess.check_output(command, text=True).strip()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    prep = root / ".ai_paper_validation" / "preprocessing"
    scopes = {
        "DOC-001": range(3, 9),
        "DOC-003": [6, *range(14, 54)],
    }

    engine = RapidOCR(
        det_use_cuda=True,
        cls_use_cuda=True,
        rec_use_cuda=True,
        print_verbose=False,
    )
    sessions = [engine.text_det.infer, engine.text_cls.infer, engine.text_rec.session]
    providers = [session.session.get_providers() for session in sessions]
    if any(not provider_list or provider_list[0] != "CUDAExecutionProvider" for provider_list in providers):
        raise RuntimeError(f"CUDA is not the primary OCR provider: {providers}")

    backend = {
        "engine": "rapidocr_onnxruntime",
        "requested_backend": "gpu",
        "selected_backend": "rapidocr-cuda",
        "gpu": gpu_identity(),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", "not set"),
        "stage_providers": {
            "detector": providers[0],
            "classifier": providers[1],
            "recognizer": providers[2],
        },
    }
    (prep / "gpu_ocr_backend_report.json").write_text(
        json.dumps(backend, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    completed = 0
    for document_id, pages in scopes.items():
        image_dir = prep / document_id / "images"
        text_dir = prep / document_id / "ocr_pages"
        metadata_dir = prep / document_id / "ocr_metadata"
        text_dir.mkdir(parents=True, exist_ok=True)
        metadata_dir.mkdir(parents=True, exist_ok=True)
        for page in pages:
            image_path = image_dir / f"page_{page:03d}.png"
            if not image_path.exists():
                raise FileNotFoundError(image_path)
            result, elapsed = engine(str(image_path))
            rows = result or []
            text = "\n".join(str(row[1]) for row in rows)
            scores = [float(row[2]) for row in rows]
            output_path = text_dir / f"page_{page:03d}.txt"
            metadata_path = metadata_dir / f"page_{page:03d}.json"
            relative_image = image_path.relative_to(root).as_posix()
            header = (
                f"[[source_document_id: {document_id}]]\n"
                f"[[source_pdf_page: {page}]]\n"
                f"[[rendered_image: {relative_image}]]\n"
                "[[ocr_backend: rapidocr-cuda]]\n\n"
            )
            output_path.write_text(header + text + "\n", encoding="utf-8")
            metadata = {
                "status": "completed",
                "document_id": document_id,
                "source_pdf_page": page,
                "input_image": relative_image,
                "output_text": output_path.relative_to(root).as_posix(),
                "characters": len(text),
                "line_count": len(rows),
                "mean_confidence": sum(scores) / len(scores) if scores else None,
                "elapsed_seconds": elapsed,
                "ocr_backend": backend,
            }
            metadata_path.write_text(
                json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            completed += 1
            print(f"completed {document_id} p{page:03d}: {len(rows)} lines")

    print(f"GPU OCR complete: {completed} pages")


if __name__ == "__main__":
    main()
